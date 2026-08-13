"""Minimal quiz seed data for verifying Phase 6.

Keeps educational content tiny and easy to extend later.
Questions are topic-specific tracking quizzes — not teaching content.
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

QuestionBank = list[tuple[str, list[tuple[str, bool]]]]

# Old Phase 6 placeholders — must never appear in seeded quizzes.
LEGACY_PROMPT_FRAGMENTS: tuple[str, ...] = (
    "EduQuest",
    "syllabus progress",
    "XP be awarded",
    "tracking a topic as complete",
)

# Topic-title keyed banks (normalized lowercase). Exactly 3 questions each.
TOPIC_QUESTION_BANKS: dict[str, QuestionBank] = {
    "ancient": [
        (
            "Which ancient civilization is known for carefully planned cities like Harappa and Mohenjo-daro?",
            [
                ("Indus Valley Civilization", True),
                ("Roman Empire", False),
                ("Ottoman Empire", False),
                ("Vijayanagara Empire", False),
            ],
        ),
        (
            "Ashoka is most closely associated with which ancient Indian empire?",
            [
                ("Maurya Empire", True),
                ("Mughal Empire", False),
                ("British Empire", False),
                ("Gupta trading companies", False),
            ],
        ),
        (
            "The Vedas are sacred texts that belong mainly to which historical period?",
            [
                ("Ancient India", True),
                ("Medieval Europe", False),
                ("Modern industrial age", False),
                ("Contemporary digital age", False),
            ],
        ),
    ],
    "medieval": [
        (
            "Which period in Indian history is most associated with the Delhi Sultanate?",
            [
                ("Medieval period", True),
                ("Ancient Indus age", False),
                ("Modern industrial period", False),
                ("Prehistoric stone age", False),
            ],
        ),
        (
            "Akbar was a famous ruler of which medieval dynasty?",
            [
                ("Mughal dynasty", True),
                ("Maurya dynasty", False),
                ("Chola maritime guilds only", False),
                ("British East India Company", False),
            ],
        ),
        (
            "The Bhakti and Sufi traditions grew especially strong during which era?",
            [
                ("Medieval India", True),
                ("Only after Indian Independence", False),
                ("Only in the Indus Valley cities", False),
                ("Only in the Space Age", False),
            ],
        ),
    ],
    "modern overview": [
        (
            "The Revolt of 1857 is an important event of which historical period?",
            [
                ("Modern Indian history", True),
                ("Indus Valley period", False),
                ("Early Vedic period only", False),
                ("Prehistoric cave art period", False),
            ],
        ),
        (
            "The Indian National Congress was founded in which century?",
            [
                ("19th century", True),
                ("5th century BCE", False),
                ("12th century", False),
                ("21st century only", False),
            ],
        ),
        (
            "India gained independence from British rule in which year?",
            [
                ("1947", True),
                ("1857", False),
                ("1526", False),
                ("320 BCE", False),
            ],
        ),
    ],
}


def normalize_topic_key(topic_title: str) -> str:
    return " ".join(topic_title.strip().lower().split())


def _default_questions_for_topic(topic_title: str) -> QuestionBank:
    """Small non-app fallback for topics without a dedicated history bank."""
    title = topic_title.strip() or "this topic"
    return [
        (
            f"Which approach best helps you review \"{title}\"?",
            [
                ("Recall the main ideas listed in the topic outline", True),
                ("Skip the outline and study unrelated subjects only", False),
                ("Replace the topic with unrelated game rules", False),
                ("Ignore the checklist items completely", False),
            ],
        ),
        (
            f"What should you focus on while studying \"{title}\"?",
            [
                ("Key concepts and checklist items for the topic", True),
                ("Unrelated entertainment trivia", False),
                ("Topics from a different subject only", False),
                ("Skipping every outline item", False),
            ],
        ),
        (
            f"When is \"{title}\" ready to mark as progress?",
            [
                ("After you have reviewed the topic outline items", True),
                ("Before opening the topic at all", False),
                ("Only after finishing every other subject first", False),
                ("Never - progress tracking is unused", False),
            ],
        ),
    ]


def questions_for_topic(topic_title: str) -> QuestionBank:
    key = normalize_topic_key(topic_title)
    bank = TOPIC_QUESTION_BANKS.get(key)
    if bank is not None:
        return bank
    return _default_questions_for_topic(topic_title)


def contains_legacy_prompt(prompt: str) -> bool:
    lowered = prompt.lower()
    return any(fragment.lower() in lowered for fragment in LEGACY_PROMPT_FRAGMENTS)


def quiz_needs_content_refresh(quiz: Quiz, topic_title: str) -> bool:
    """True when questions are missing, legacy, or out of date for a known topic bank."""
    if len(quiz.questions) == 0:
        return True
    if any(contains_legacy_prompt(q.prompt) for q in quiz.questions):
        return True

    key = normalize_topic_key(topic_title)
    if key not in TOPIC_QUESTION_BANKS:
        return False

    expected = [prompt for prompt, _ in questions_for_topic(topic_title)]
    current = [q.prompt for q in sorted(quiz.questions, key=lambda item: item.sort_order)]
    return current != expected


def _add_sample_questions(quiz: Quiz, topic_title: str) -> None:
    """Attach 3 MCQs via the relationship so the collection stays consistent."""
    for q_index, (prompt, options) in enumerate(questions_for_topic(topic_title)):
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


async def _replace_quiz_questions(
    session: AsyncSession,
    quiz: Quiz,
    topic_title: str,
) -> None:
    for question in list(quiz.questions):
        await session.delete(question)
    await session.flush()
    set_committed_value(quiz, "questions", [])
    _add_sample_questions(quiz, topic_title)
    await session.flush()


async def ensure_quiz_for_topic(session: AsyncSession, topic_id: UUID, topic_title: str) -> Quiz:
    """Create one active quiz with 3 MCQs if the topic has none; refresh legacy content."""
    result = await session.execute(
        select(Quiz)
        .where(Quiz.topic_id == topic_id, Quiz.is_active.is_(True))
        .options(selectinload(Quiz.questions).selectinload(QuizQuestion.options))
        .order_by(Quiz.sort_order, Quiz.title)
        .limit(1),
    )
    quiz = result.scalar_one_or_none()

    if quiz is not None:
        if quiz_needs_content_refresh(quiz, topic_title):
            await _replace_quiz_questions(session, quiz, topic_title)
        return quiz

    # Append questions before flush so async code never triggers a lazy load.
    quiz = Quiz(
        topic_id=topic_id,
        title=f"{topic_title} Challenge",
        time_limit_seconds=180,
        is_active=True,
        sort_order=0,
    )
    set_committed_value(quiz, "questions", [])
    _add_sample_questions(quiz, topic_title)
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
    topic_title = loaded.topic.title if loaded.topic is not None else "Topic"
    if quiz_needs_content_refresh(loaded, topic_title):
        await _replace_quiz_questions(session, loaded, topic_title)
    return loaded


async def refresh_all_topic_quizzes(session: AsyncSession) -> int:
    """Refresh every active quiz so local DBs pick up corrected topic content."""
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
        topic_title = quiz.topic.title if quiz.topic is not None else "Topic"
        if quiz_needs_content_refresh(quiz, topic_title):
            await _replace_quiz_questions(session, quiz, topic_title)
            updated += 1
    return updated
