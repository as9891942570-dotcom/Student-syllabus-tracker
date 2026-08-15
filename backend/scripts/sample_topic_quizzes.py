"""Print sample topic quizzes and aggregate stats."""

from __future__ import annotations

import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from sqlalchemy import func, select, text
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import selectinload

from app.core.config import get_settings
from app.models.chapter import Chapter
from app.models.quiz import Quiz
from app.models.quiz_attempt import QuizAttempt
from app.models.quiz_question import QuizQuestion
from app.models.student_profile import StudentProfile
from app.models.student_topic_progress import StudentTopicProgress
from app.models.subject import Subject
from app.models.topic import Topic
from app.services.topic_quiz_builder import questions_match_topic


async def main() -> None:
    settings = get_settings()
    engine = create_async_engine(settings.database_url, echo=False)
    Session = async_sessionmaker(
        bind=engine,
        class_=AsyncSession,
        expire_on_commit=False,
        autoflush=False,
    )
    async with Session() as session:
        try:
            n = await session.scalar(text("SELECT COUNT(*) FROM study_sessions"))
            print("study_sessions_rows", n)
        except Exception as exc:
            print("study_sessions", "DROPPED", type(exc).__name__)
            await session.rollback()

        qcount = await session.scalar(select(func.count()).select_from(QuizQuestion))
        quizcount = await session.scalar(
            select(func.count()).select_from(Quiz).where(Quiz.is_active.is_(True)),
        )
        topics = await session.scalar(
            select(func.count()).select_from(Topic).where(Topic.is_active.is_(True)),
        )
        rows = (
            await session.execute(
                select(func.count(QuizQuestion.id))
                .select_from(QuizQuestion)
                .join(Quiz, QuizQuestion.quiz_id == Quiz.id)
                .where(Quiz.is_active.is_(True))
                .group_by(Quiz.topic_id),
            )
        ).scalars().all()
        print("active_topics", topics)
        print("active_quizzes", quizcount)
        print("quiz_questions", qcount)
        print(
            "q_per_topic_min",
            min(rows),
            "max",
            max(rows),
            "avg",
            round(sum(rows) / len(rows), 1),
        )
        print("topics_with_>20", sum(1 for r in rows if r > 20))
        print(
            "progress_rows",
            await session.scalar(select(func.count()).select_from(StudentTopicProgress)),
        )
        print(
            "quiz_attempts",
            await session.scalar(select(func.count()).select_from(QuizAttempt)),
        )
        print(
            "total_xp_sum",
            await session.scalar(
                select(func.coalesce(func.sum(StudentProfile.total_xp), 0)),
            ),
        )

        samples = [
            ("Electric charge", "PHY"),
            ("Coulomb's law", "PHY"),
            ("The international system of units", "PHY"),
        ]
        for title, code in samples:
            result = await session.execute(
                select(Topic, Chapter, Subject, Quiz)
                .join(Chapter, Topic.chapter_id == Chapter.id)
                .join(Subject, Chapter.subject_id == Subject.id)
                .join(Quiz, Quiz.topic_id == Topic.id)
                .where(
                    Topic.title == title,
                    Subject.code == code,
                    Topic.is_active.is_(True),
                    Quiz.is_active.is_(True),
                )
                .limit(1),
            )
            row = result.first()
            if row is None:
                print("MISSING", title)
                continue
            topic, chapter, subject, quiz_ref = row
            quiz = (
                await session.execute(
                    select(Quiz)
                    .where(Quiz.id == quiz_ref.id)
                    .options(
                        selectinload(Quiz.questions).selectinload(QuizQuestion.options),
                    ),
                )
            ).scalar_one()
            print("=" * 60)
            print("TOPIC:", topic.title)
            print("CHAPTER:", chapter.title)
            print("SUBJECT:", subject.code, subject.name)
            print("QUESTIONS:", len(quiz.questions))
            for question in sorted(quiz.questions, key=lambda item: item.sort_order):
                ok = questions_match_topic(question.prompt, topic.title)
                print(f"  [{'OK' if ok else '??'}] {question.prompt}")
                for option in sorted(question.options, key=lambda item: item.sort_order):
                    mark = "*" if option.is_correct else " "
                    print(f"      {mark} {option.text}")

    await engine.dispose()


if __name__ == "__main__":
    asyncio.run(main())
