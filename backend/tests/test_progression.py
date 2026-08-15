"""Phase 7 progression, level, and topic unlock tests."""

from __future__ import annotations

import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.exceptions import ForbiddenError
from app.schemas.auth import RegisterRequest
from app.schemas.profile import ProfileUpdateRequest
from app.schemas.quiz import SubmitAnswerRequest
from app.schemas.syllabus import TopicProgressUpdate
from app.services.auth import AuthService
from app.services.level import calculate_level, calculate_level_progress
from app.services.profile import ProfileService
from app.services.progression import ProgressionService
from app.services.quiz import QuizService
from app.services.syllabus import SyllabusService


def test_level_thresholds() -> None:
    assert calculate_level(0) == 1
    assert calculate_level(99) == 1
    assert calculate_level(100) == 2
    assert calculate_level(249) == 2
    assert calculate_level(250) == 3
    assert calculate_level(499) == 3
    assert calculate_level(500) == 4
    assert calculate_level(999) == 4
    assert calculate_level(1000) == 5
    assert calculate_level(1999) == 5
    assert calculate_level(2000) == 6
    assert calculate_level(4000) == 7

    progress = calculate_level_progress(125)
    assert progress.level == 2
    assert progress.level_floor_xp == 100
    assert progress.next_level_xp == 250
    assert progress.xp_into_level == 25
    assert progress.xp_needed_for_next == 150


async def _ready_user(session: AsyncSession, email: str):
    tokens = await AuthService(session).register(
        RegisterRequest(email=email, password="Secret123!", full_name="Progress Student"),
    )
    user = await AuthService(session).get_user(tokens.user.id)
    profile_service = ProfileService(session)
    await profile_service.ensure_lookups()
    boards = await profile_service.list_boards()
    classes = await profile_service.list_classes()
    class_8 = next(c for c in classes if c.grade == 8)
    profile = await profile_service.get_or_create_profile(user)
    profile.photo_url = "/media/profiles/demo.jpg"
    await profile_service.profiles.update(profile)
    await profile_service.update_profile(
        user,
        ProfileUpdateRequest(
            mobile="9876507777",
            board_id=boards[0].id,
            class_id=class_8.id,
        ),
    )
    return user


async def _chapter_topics(session: AsyncSession, user):
    subjects = await SyllabusService(session).list_subjects(user)
    detail = await SyllabusService(session).get_subject_chapters(user, subjects[0].id)
    return await SyllabusService(session).get_chapter_topics(user, detail.chapters[0].id)


@pytest.mark.asyncio
async def test_first_topic_unlocked_others_locked(db_session: AsyncSession) -> None:
    user = await _ready_user(db_session, "prog1@example.com")
    chapter = await _chapter_topics(db_session, user)
    assert len(chapter.topics) >= 2
    assert chapter.topics[0].is_locked is False
    assert chapter.topics[0].is_current is True
    assert chapter.topics[1].is_locked is True
    assert chapter.topics[1].is_current is False


@pytest.mark.asyncio
async def test_opening_topics_does_not_unlock(db_session: AsyncSession) -> None:
    user = await _ready_user(db_session, "progopen@example.com")
    chapter = await _chapter_topics(db_session, user)
    locked = chapter.topics[1]
    await QuizService(db_session).list_for_topic(user, locked.id)
    again = await _chapter_topics(db_session, user)
    assert again.topics[0].is_locked is False
    assert again.topics[1].is_locked is True
    if len(again.topics) > 2:
        assert again.topics[2].is_locked is True


@pytest.mark.asyncio
async def test_locked_topic_cannot_start_quiz(db_session: AsyncSession) -> None:
    user = await _ready_user(db_session, "prog2@example.com")
    chapter = await _chapter_topics(db_session, user)
    locked = chapter.topics[1]

    with pytest.raises(ForbiddenError):
        await SyllabusService(db_session).set_topic_progress(
            user,
            locked.id,
            TopicProgressUpdate(is_completed=True),
        )

    quizzes = await QuizService(db_session).list_for_topic(user, locked.id)
    with pytest.raises(ForbiddenError):
        await QuizService(db_session).start(user, quizzes[0].id)


@pytest.mark.asyncio
async def test_quiz_completion_unlocks_next_and_awards_xp_once(
    db_session: AsyncSession,
) -> None:
    user = await _ready_user(db_session, "prog3@example.com")
    chapter = await _chapter_topics(db_session, user)
    topic1 = chapter.topics[0]
    topic2 = chapter.topics[1]
    topic3 = chapter.topics[2] if len(chapter.topics) > 2 else None

    quiz_service = QuizService(db_session)
    quizzes = await quiz_service.list_for_topic(user, topic1.id)
    quiz_id = quizzes[0].id

    async def _perfect_complete() -> None:
        attempt = await quiz_service.start(user, quiz_id)
        for _ in range(attempt.total_questions):
            question = await quiz_service.current_question(user, attempt.id)
            loaded = await quiz_service.quizzes.get_with_questions(quiz_id)
            orm_q = next(q for q in loaded.questions if q.id == question.id)
            correct = next(o for o in orm_q.options if o.is_correct)
            await quiz_service.submit_answer(
                user,
                attempt.id,
                SubmitAnswerRequest(option_id=correct.id),
            )
            if question.question_number < question.total_questions:
                await quiz_service.next_question(user, attempt.id)
        return await quiz_service.complete(user, attempt.id)

    result = await _perfect_complete()
    assert result.topic_completed is True
    assert result.xp_earned > 0
    assert result.xp_awarded is True
    assert result.next_topic_unlocked is True
    assert result.next_topic_id == topic2.id
    assert result.level >= 1

    chapter = await _chapter_topics(db_session, user)
    assert chapter.topics[0].is_completed is True
    assert chapter.topics[1].is_locked is False
    assert chapter.topics[1].is_current is True
    if topic3 is not None:
        assert chapter.topics[2].is_locked is True

    first_xp = result.total_xp

    # Retry same quiz — XP must not be awarded twice.
    retry = await _perfect_complete()
    assert retry.xp_awarded is False
    assert retry.xp_earned == 0
    assert retry.total_xp == first_xp

    profile = await ProfileService(db_session).get_profile(user)
    assert profile.total_xp == first_xp
    assert profile.level == calculate_level(first_xp)


@pytest.mark.asyncio
async def test_progression_survives_reload(db_session: AsyncSession) -> None:
    user = await _ready_user(db_session, "prog4@example.com")
    chapter = await _chapter_topics(db_session, user)
    topic1 = chapter.topics[0]

    await SyllabusService(db_session).set_topic_progress(
        user,
        topic1.id,
        TopicProgressUpdate(is_completed=True),
    )

    # Simulate "new request" by constructing fresh services.
    chapter2 = await SyllabusService(db_session).get_chapter_topics(
        user,
        chapter.id,
    )
    assert chapter2.topics[0].is_completed is True
    assert chapter2.topics[1].is_locked is False

    progression = await ProgressionService(db_session).get_me(user)
    assert progression.completed_topic_count >= 1
    assert progression.current_topic is not None
    assert progression.current_topic.id == chapter2.topics[1].id
    assert progression.total_xp >= 0
    assert progression.level >= 1
