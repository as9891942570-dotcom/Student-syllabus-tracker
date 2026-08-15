"""Inspect 5 sample topics for real concept questions (not meta)."""

from __future__ import annotations

import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import selectinload

from app.core.config import get_settings
from app.models.chapter import Chapter
from app.models.quiz import Quiz
from app.models.quiz_question import QuizQuestion
from app.models.subject import Subject
from app.models.topic import Topic
from app.services.topic_quiz_builder import is_meta_question, resolve_concept_bank


SAMPLES = [
    ("Coulomb's law", "PHY"),
    ("Electric charge", "PHY"),
    ("Mole concept and stoichiometry", "CHEM"),
    ("Solving quadratic equations", "MATH"),
    ("Calvin cycle", "BIO"),
]


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
        for title, code in SAMPLES:
            bank = resolve_concept_bank(title)
            print("=" * 72)
            print("TOPIC:", title)
            print("MAPPED_BANK:", "yes" if bank else "NO — insufficient concept mapping")
            result = await session.execute(
                select(Topic, Chapter, Subject, Quiz)
                .join(Chapter, Topic.chapter_id == Chapter.id)
                .join(Subject, Chapter.subject_id == Subject.id)
                .outerjoin(Quiz, (Quiz.topic_id == Topic.id) & (Quiz.is_active.is_(True)))
                .where(Topic.title == title, Subject.code == code, Topic.is_active.is_(True))
                .limit(1),
            )
            row = result.first()
            if row is None:
                print("DB_ROW: missing")
                continue
            topic, chapter, subject, quiz_ref = row
            print("CHAPTER:", chapter.title)
            print("SUBJECT:", subject.code, subject.name)
            if quiz_ref is None:
                print("QUIZ: none")
                continue
            quiz = (
                await session.execute(
                    select(Quiz)
                    .where(Quiz.id == quiz_ref.id)
                    .options(
                        selectinload(Quiz.questions).selectinload(QuizQuestion.options),
                    ),
                )
            ).scalar_one()
            print("QUESTIONS:", len(quiz.questions))
            for i, question in enumerate(
                sorted(quiz.questions, key=lambda q: q.sort_order)[:5],
                start=1,
            ):
                meta = is_meta_question(
                    question.prompt,
                    [(o.text, o.is_correct) for o in question.options],
                )
                print(f"\nQuestion {i}: {question.prompt}")
                if meta:
                    print("  !! META (INVALID)")
                for option in sorted(question.options, key=lambda o: o.sort_order):
                    mark = "CORRECT" if option.is_correct else "option"
                    print(f"  - ({mark}) {option.text}")
    await engine.dispose()


if __name__ == "__main__":
    asyncio.run(main())
