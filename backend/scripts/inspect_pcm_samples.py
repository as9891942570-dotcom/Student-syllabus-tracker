"""Inspect Class 12 PCM sample quizzes across subjects."""

from __future__ import annotations

import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import selectinload

from app.core.config import get_settings
from app.db.session import init_database_schema
from app.models.chapter import Chapter
from app.models.quiz import Quiz
from app.models.quiz_option import QuizOption  # noqa: F401
from app.models.quiz_question import QuizQuestion
from app.models.school_class import SchoolClass
from app.models.stream import Stream
from app.models.subject import Subject
from app.models.topic import Topic
from app.services.quiz_seed import ensure_quiz_for_topic
from app.services.topic_quiz_builder import resolve_concept_bank

SAMPLES: list[tuple[str, str, str]] = [
    ("PHY", "Electric Charges and Fields", "Coulomb's law"),
    ("PHY", "Electrostatic Potential and Capacitance", "Capacitors and capacitance"),
    ("PHY", "Electromagnetic Induction", "Lenz's law and conservation of energy"),
    ("CHEM", "Solutions", "Colligative properties"),
    ("CHEM", "Electrochemistry", "Nernst equation"),
    ("CHEM", "Coordination Compounds", "Bonding and isomerism"),
    ("MATH", "Matrices", "Types of matrices"),
    ("MATH", "Probability", "Bayes' theorem"),
    ("MATH", "Application of Derivatives", "Maxima and minima"),
    ("ENG", "Flamingo Prose", "The Last Lesson"),
    ("ENG", "Flamingo Poems", "Keeping Quiet"),
    ("ENG", "Vistas", "The Tiger King"),
]


async def main() -> None:
    await init_database_schema()
    settings = get_settings()
    engine = create_async_engine(settings.database_url, echo=False)
    Session = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False, autoflush=False)

    async with Session() as session:
        for code, chapter_title, topic_title in SAMPLES:
            row = (
                await session.execute(
                    select(Topic, Chapter, Subject)
                    .join(Chapter, Topic.chapter_id == Chapter.id)
                    .join(Subject, Chapter.subject_id == Subject.id)
                    .join(SchoolClass, Subject.class_id == SchoolClass.id)
                    .join(Stream, Subject.stream_id == Stream.id)
                    .where(
                        SchoolClass.grade == 12,
                        Stream.name == "Science (PCM)",
                        Subject.code == code,
                        Chapter.title == chapter_title,
                        Topic.title == topic_title,
                        Topic.is_active.is_(True),
                    )
                )
            ).first()
            if row is None:
                print(f"\nMISSING: {code} / {chapter_title} / {topic_title}")
                continue
            topic, chapter, subject = row
            await ensure_quiz_for_topic(session, topic.id, topic.title)
            await session.commit()

            quiz = (
                await session.execute(
                    select(Quiz)
                    .options(
                        selectinload(Quiz.questions).selectinload(QuizQuestion.options),
                    )
                    .where(Quiz.topic_id == topic.id, Quiz.is_active.is_(True))
                )
            ).scalar_one_or_none()

            mapped = resolve_concept_bank(
                topic.title,
                chapter_title=chapter.title,
                subject_code=subject.code,
            )
            print("=" * 72)
            print(f"SUBJECT: {subject.name} ({subject.code})")
            print(f"TOPIC: {topic.title}")
            print(f"CHAPTER: {chapter.title}")
            print(f"MAPPED_BANK: {'yes' if mapped else 'no'}")
            if quiz is None:
                print("QUESTIONS: 0 (no quiz)")
                continue
            questions = sorted(quiz.questions, key=lambda q: q.sort_order)
            print(f"QUESTIONS: {len(questions)}")
            for i, q in enumerate(questions[:3], start=1):
                opts = sorted(q.options, key=lambda o: o.sort_order)
                print(f"\nQuestion {i}: {q.prompt}")
                letters = "ABCD"
                correct = None
                for idx, opt in enumerate(opts):
                    tag = letters[idx] if idx < 4 else str(idx + 1)
                    mark = " (CORRECT)" if opt.is_correct else ""
                    print(f"  OPTION {tag}: {opt.text}{mark}")
                    if opt.is_correct:
                        correct = f"{tag}. {opt.text}"
                print(f"  CORRECT ANSWER: {correct}")

    await engine.dispose()


if __name__ == "__main__":
    asyncio.run(main())
