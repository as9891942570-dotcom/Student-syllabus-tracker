"""Force-refresh all active quizzes to curated concept banks (no meta fillers)."""

from __future__ import annotations

import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import selectinload

from app.core.config import get_settings
from app.db.session import init_database_schema
from app.models.quiz import Quiz
from app.models.quiz_question import QuizQuestion
from app.services.quiz_seed import ensure_quizzes_for_all_active_topics, refresh_all_topic_quizzes
from app.services.topic_quiz_builder import is_meta_question


async def main() -> None:
    await init_database_schema()
    settings = get_settings()
    engine = create_async_engine(settings.database_url, echo=False)
    Session = async_sessionmaker(
        bind=engine,
        class_=AsyncSession,
        expire_on_commit=False,
        autoflush=False,
    )
    async with Session() as session:
        updated = await refresh_all_topic_quizzes(session)
        await session.commit()
        stats = await ensure_quizzes_for_all_active_topics(session)
        await session.commit()

        empty = await session.execute(
            select(Quiz)
            .where(Quiz.is_active.is_(True))
            .options(selectinload(Quiz.questions), selectinload(Quiz.topic)),
        )
        deactivated_empty = 0
        for quiz in empty.scalars().unique().all():
            topic = quiz.topic
            if (not quiz.questions) or (topic is not None and not topic.is_active):
                quiz.is_active = False
                deactivated_empty += 1
        if deactivated_empty:
            await session.commit()

        meta = 0
        result = await session.execute(
            select(QuizQuestion.prompt)
            .join(Quiz, QuizQuestion.quiz_id == Quiz.id)
            .where(Quiz.is_active.is_(True)),
        )
        for (prompt,) in result.all():
            if is_meta_question(prompt):
                meta += 1

        qcount = await session.scalar(select(func.count()).select_from(QuizQuestion))
        print("refreshed_existing", updated)
        print("ensure_stats", stats)
        print("deactivated_empty_quizzes", deactivated_empty)
        print("total_questions", qcount)
        print("active_meta_questions", meta)
        if meta:
            raise SystemExit("Meta questions still present")
        print("OK: no active meta questions")
    await engine.dispose()


if __name__ == "__main__":
    asyncio.run(main())
