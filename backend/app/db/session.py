"""Async SQLAlchemy engine and session factory."""

from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.pool import NullPool

from app.core.config import get_settings

settings = get_settings()

_engine_kwargs: dict = {
    "echo": settings.debug,
}
if settings.is_sqlite:
    # SQLite: avoid pooled connections across event loops in reload/tests.
    _engine_kwargs["poolclass"] = NullPool
else:
    _engine_kwargs["pool_pre_ping"] = True

engine = create_async_engine(settings.database_url, **_engine_kwargs)

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False,
)


async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise


async def check_database_connection() -> bool:
    from sqlalchemy import text

    try:
        async with engine.connect() as conn:
            await conn.execute(text("SELECT 1"))
        return True
    except Exception:
        return False


async def _ensure_sqlite_column(conn, table: str, column: str, ddl: str) -> None:
    from sqlalchemy import text

    result = await conn.execute(text(f"PRAGMA table_info({table})"))
    columns = {row[1] for row in result.fetchall()}
    if column not in columns:
        await conn.execute(text(ddl))


async def init_database_schema() -> None:
    """Create tables in development / SQLite when migrations are not applied yet."""
    if not settings.auto_create_tables:
        return
    # Ensure models are registered on metadata.
    import app.models  # noqa: F401
    from app.db.base import Base
    from sqlalchemy import text

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        if settings.is_sqlite:
            # create_all does not alter existing tables — add later-phase columns.
            result = await conn.execute(text("PRAGMA table_info(student_profiles)"))
            profile_columns = {row[1] for row in result.fetchall()}
            if "total_xp" not in profile_columns:
                await conn.execute(
                    text(
                        "ALTER TABLE student_profiles "
                        "ADD COLUMN total_xp INTEGER NOT NULL DEFAULT 0",
                    ),
                )
            if "total_coins" not in profile_columns:
                await conn.execute(
                    text(
                        "ALTER TABLE student_profiles "
                        "ADD COLUMN total_coins INTEGER NOT NULL DEFAULT 0",
                    ),
                )
            await _ensure_sqlite_column(
                conn,
                "quiz_attempts",
                "coins_earned",
                "ALTER TABLE quiz_attempts ADD COLUMN coins_earned INTEGER NOT NULL DEFAULT 0",
            )
            await _ensure_sqlite_column(
                conn,
                "subjects",
                "curriculum_version",
                "ALTER TABLE subjects ADD COLUMN curriculum_version VARCHAR(32) NOT NULL DEFAULT 'CBSE 2026-27'",
            )
            await _ensure_sqlite_column(
                conn,
                "subjects",
                "is_active",
                "ALTER TABLE subjects ADD COLUMN is_active BOOLEAN NOT NULL DEFAULT 1",
            )
            await _ensure_sqlite_column(
                conn,
                "chapters",
                "curriculum_version",
                "ALTER TABLE chapters ADD COLUMN curriculum_version VARCHAR(32) NOT NULL DEFAULT 'CBSE 2026-27'",
            )
            await _ensure_sqlite_column(
                conn,
                "chapters",
                "is_active",
                "ALTER TABLE chapters ADD COLUMN is_active BOOLEAN NOT NULL DEFAULT 1",
            )
            await _ensure_sqlite_column(
                conn,
                "topics",
                "curriculum_version",
                "ALTER TABLE topics ADD COLUMN curriculum_version VARCHAR(32) NOT NULL DEFAULT 'CBSE 2026-27'",
            )
            await _ensure_sqlite_column(
                conn,
                "topics",
                "is_active",
                "ALTER TABLE topics ADD COLUMN is_active BOOLEAN NOT NULL DEFAULT 1",
            )
            # Study sessions removed — drop leftover local table if present.
            await conn.execute(text("DROP TABLE IF EXISTS study_sessions"))
            # Household accounts may share an email; password selects the user.
            index_rows = (await conn.execute(text("PRAGMA index_list(users)"))).fetchall()
            for row in index_rows:
                index_name = row[1]
                is_unique = int(row[2] or 0) == 1
                if not is_unique:
                    continue
                cols = (
                    await conn.execute(text(f"PRAGMA index_info({index_name})"))
                ).fetchall()
                if [col[2] for col in cols] == ["email"]:
                    await conn.execute(text(f'DROP INDEX IF EXISTS "{index_name}"'))
            await conn.execute(
                text("CREATE INDEX IF NOT EXISTS ix_users_email ON users (email)"),
            )
