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
            # create_all does not alter existing tables — add Phase 5 column if missing.
            result = await conn.execute(text("PRAGMA table_info(student_profiles)"))
            columns = {row[1] for row in result.fetchall()}
            if "total_xp" not in columns:
                await conn.execute(
                    text(
                        "ALTER TABLE student_profiles "
                        "ADD COLUMN total_xp INTEGER NOT NULL DEFAULT 0",
                    ),
                )
