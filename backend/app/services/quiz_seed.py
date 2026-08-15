"""Topic quiz seeding — original questions bound to each topic (max 20).

Reuses the Phase 6 Quiz / QuizQuestion / QuizOption models.
Does not create a second quiz system and does not depend on study sessions.
"""

from __future__ import annotations

from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from sqlalchemy.orm.attributes import set_committed_value

from app.models.quiz import Quiz
from app.models.quiz_option import QuizOption
from app.models.quiz_question import QuizQuestion
from app.models.topic import Topic
from app.services.topic_quiz_builder import (
    MAX_QUESTIONS_PER_TOPIC,
    QuestionBank,
    build_topic_questions,
    is_meta_question,
)

# Re-export for tests and callers.
__all__ = [
    "MAX_QUESTIONS_PER_TOPIC",
    "LEGACY_PROMPT_FRAGMENTS",
    "contains_legacy_prompt",
    "questions_for_topic",
    "ensure_quiz_for_topic",
    "ensure_quiz_has_questions",
    "refresh_all_topic_quizzes",
    "ensure_quizzes_for_all_active_topics",
]

# Fragments that identify bad/legacy/meta prompts (must never remain active).
LEGACY_PROMPT_FRAGMENTS: tuple[str, ...] = (
    "EduQuest",
    "syllabus progress",
    "XP be awarded",
    "tracking a topic as complete",
    "Which approach best helps you review",
    "What should you focus on while studying",
    "ready to mark as progress",
    "While studying",
    "what should a student primarily focus on",
    "best describes",
    "definitions, relations, and applications",
    "Which chapter contains the topic",
    "stays on-topic for",
    "avoid other topics",
    "progress should reflect",
    "mark progress on",
    "unlock the next topic",
    "Ideas and methods used to understand",
    "belongs under which chapter context",
)

SECONDS_PER_QUESTION = 45


def contains_legacy_prompt(prompt: str) -> bool:
    if is_meta_question(prompt):
        return True
    lowered = prompt.lower()
    return any(fragment.lower() in lowered for fragment in LEGACY_PROMPT_FRAGMENTS)


def questions_for_topic(
    topic_title: str,
    *,
    chapter_title: str = "",
    subject_code: str = "GEN",
    grade: int = 10,
) -> QuestionBank:
    return build_topic_questions(
        topic_title=topic_title,
        chapter_title=chapter_title or topic_title,
        subject_code=subject_code,
        grade=grade,
    )


def quiz_time_limit_seconds(question_count: int) -> int:
    return max(180, min(question_count, MAX_QUESTIONS_PER_TOPIC) * SECONDS_PER_QUESTION)


def quiz_needs_content_refresh(
    quiz: Quiz,
    topic_title: str,
    *,
    chapter_title: str,
    subject_code: str,
    grade: int,
) -> bool:
    """True when questions are missing, meta/legacy, or out of date for the topic."""
    if any(contains_legacy_prompt(q.prompt) for q in quiz.questions):
        return True
    if any(is_meta_question(q.prompt) for q in quiz.questions):
        return True
    if len(quiz.questions) > MAX_QUESTIONS_PER_TOPIC:
        return True

    expected = [
        prompt
        for prompt, _ in questions_for_topic(
            topic_title,
            chapter_title=chapter_title,
            subject_code=subject_code,
            grade=grade,
        )
    ]
    current = [q.prompt for q in sorted(quiz.questions, key=lambda item: item.sort_order)]
    # Empty expected means unmapped topic — clear any leftover filler.
    if not expected:
        return len(current) > 0
    if len(quiz.questions) == 0:
        return True
    return current != expected


def _add_questions(quiz: Quiz, bank: QuestionBank) -> None:
    if len(bank) > MAX_QUESTIONS_PER_TOPIC:
        bank = bank[:MAX_QUESTIONS_PER_TOPIC]
    for q_index, (prompt, options) in enumerate(bank):
        question = QuizQuestion(prompt=prompt, sort_order=q_index)
        quiz.questions.append(question)
        correct_count = sum(1 for _, is_correct in options if is_correct)
        if correct_count != 1:
            raise ValueError(f"Seed question must have exactly one correct option: {prompt}")
        if len(options) < 2:
            raise ValueError(f"Seed question must have multiple options: {prompt}")
        for o_index, (text, is_correct) in enumerate(options):
            question.options.append(
                QuizOption(
                    text=text,
                    is_correct=is_correct,
                    sort_order=o_index,
                ),
            )


async def _load_topic_context(
    session: AsyncSession,
    topic_id: UUID,
) -> tuple[str, str, str, int]:
    from app.models.chapter import Chapter
    from app.models.school_class import SchoolClass
    from app.models.subject import Subject

    result = await session.execute(
        select(Topic, Chapter, Subject, SchoolClass)
        .join(Chapter, Topic.chapter_id == Chapter.id)
        .join(Subject, Chapter.subject_id == Subject.id)
        .join(SchoolClass, Subject.class_id == SchoolClass.id)
        .where(Topic.id == topic_id),
    )
    row = result.first()
    if row is None:
        return "Topic", "Chapter", "GEN", 10
    topic, chapter, subject, school_class = row
    return topic.title, chapter.title, subject.code, school_class.grade


async def _replace_quiz_questions(
    session: AsyncSession,
    quiz: Quiz,
    *,
    topic_title: str,
    chapter_title: str,
    subject_code: str,
    grade: int,
) -> None:
    for question in list(quiz.questions):
        await session.delete(question)
    await session.flush()
    set_committed_value(quiz, "questions", [])
    bank = questions_for_topic(
        topic_title,
        chapter_title=chapter_title,
        subject_code=subject_code,
        grade=grade,
    )
    _add_questions(quiz, bank)
    quiz.time_limit_seconds = quiz_time_limit_seconds(len(bank))
    quiz.title = f"{topic_title} Challenge"
    await session.flush()


async def ensure_quiz_for_topic(
    session: AsyncSession,
    topic_id: UUID,
    topic_title: str | None = None,
) -> Quiz:
    """Create/refresh one active quiz with up to 20 topic-specific MCQs."""
    title, chapter_title, subject_code, grade = await _load_topic_context(session, topic_id)
    if topic_title:
        title = topic_title

    result = await session.execute(
        select(Quiz)
        .where(Quiz.topic_id == topic_id, Quiz.is_active.is_(True))
        .options(selectinload(Quiz.questions).selectinload(QuizQuestion.options))
        .order_by(Quiz.sort_order, Quiz.title)
        .limit(1),
    )
    quiz = result.scalar_one_or_none()

    if quiz is not None:
        if quiz_needs_content_refresh(
            quiz,
            title,
            chapter_title=chapter_title,
            subject_code=subject_code,
            grade=grade,
        ):
            await _replace_quiz_questions(
                session,
                quiz,
                topic_title=title,
                chapter_title=chapter_title,
                subject_code=subject_code,
                grade=grade,
            )
            if not quiz.questions:
                quiz.is_active = False
        return quiz

    bank = questions_for_topic(
        title,
        chapter_title=chapter_title,
        subject_code=subject_code,
        grade=grade,
    )
    if not bank:
        # Do not persist empty filler quizzes for unmapped topics.
        quiz = Quiz(
            topic_id=topic_id,
            title=f"{title} Challenge",
            time_limit_seconds=quiz_time_limit_seconds(0),
            is_active=False,
            sort_order=0,
        )
        set_committed_value(quiz, "questions", [])
        return quiz

    quiz = Quiz(
        topic_id=topic_id,
        title=f"{title} Challenge",
        time_limit_seconds=quiz_time_limit_seconds(len(bank)),
        is_active=True,
        sort_order=0,
    )
    set_committed_value(quiz, "questions", [])
    _add_questions(quiz, bank)
    session.add(quiz)
    await session.flush()
    return quiz


async def ensure_quiz_has_questions(session: AsyncSession, quiz: Quiz) -> Quiz:
    """Backfill or refresh sample questions for an existing quiz."""
    result = await session.execute(
        select(Quiz)
        .where(Quiz.id == quiz.id)
        .options(
            selectinload(Quiz.questions).selectinload(QuizQuestion.options),
            selectinload(Quiz.topic),
        ),
    )
    loaded = result.scalar_one()
    topic_id = loaded.topic_id
    title, chapter_title, subject_code, grade = await _load_topic_context(session, topic_id)
    if quiz_needs_content_refresh(
        loaded,
        title,
        chapter_title=chapter_title,
        subject_code=subject_code,
        grade=grade,
    ):
        await _replace_quiz_questions(
            session,
            loaded,
            topic_title=title,
            chapter_title=chapter_title,
            subject_code=subject_code,
            grade=grade,
        )
    return loaded


async def refresh_all_topic_quizzes(session: AsyncSession) -> int:
    """Refresh every active quiz so local DBs pick up topic-specific content."""
    result = await session.execute(
        select(Quiz)
        .where(Quiz.is_active.is_(True))
        .options(
            selectinload(Quiz.questions).selectinload(QuizQuestion.options),
            selectinload(Quiz.topic),
        ),
    )
    quizzes = list(result.scalars().unique().all())
    updated = 0
    for quiz in quizzes:
        title, chapter_title, subject_code, grade = await _load_topic_context(
            session,
            quiz.topic_id,
        )
        if quiz_needs_content_refresh(
            quiz,
            title,
            chapter_title=chapter_title,
            subject_code=subject_code,
            grade=grade,
        ):
            await _replace_quiz_questions(
                session,
                quiz,
                topic_title=title,
                chapter_title=chapter_title,
                subject_code=subject_code,
                grade=grade,
            )
            updated += 1
    return updated


async def ensure_quizzes_for_all_active_topics(session: AsyncSession) -> dict[str, int]:
    """Idempotently ensure every active topic has a topic-specific quiz when mapped."""
    result = await session.execute(select(Topic).where(Topic.is_active.is_(True)))
    topics = list(result.scalars().all())
    created_or_refreshed = 0
    total_questions = 0
    for topic in topics:
        before = await session.execute(
            select(Quiz)
            .where(Quiz.topic_id == topic.id, Quiz.is_active.is_(True))
            .options(selectinload(Quiz.questions))
            .limit(1),
        )
        existing = before.scalar_one_or_none()
        quiz = await ensure_quiz_for_topic(session, topic.id, topic.title)
        if quiz.is_active and quiz.id is not None:
            if existing is None or len(existing.questions) != len(quiz.questions):
                created_or_refreshed += 1
            total_questions += len(quiz.questions)
    return {
        "topics": len(topics),
        "quizzes_touched": created_or_refreshed,
        "question_rows_linked": total_questions,
    }


# Backwards-compatible export for older tests that imported the name.
TOPIC_QUESTION_BANKS: dict[str, QuestionBank] = {}
