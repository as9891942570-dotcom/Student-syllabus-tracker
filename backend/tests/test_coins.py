"""Coin rewards on first successful topic quiz (>=60%)."""

from __future__ import annotations

import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.auth import RegisterRequest
from app.schemas.profile import ProfileUpdateRequest
from app.schemas.quiz import SubmitAnswerRequest
from app.services.auth import AuthService
from app.services.coins import coin_reward_per_topic
from app.services.profile import ProfileService
from app.services.quiz import TOPIC_COMPLETE_PERCENTAGE, QuizService
from app.services.syllabus import SyllabusService


async def _ready_user(session: AsyncSession, email: str):
    tokens = await AuthService(session).register(
        RegisterRequest(email=email, password="Secret123!", full_name="Coin Student"),
    )
    user = await AuthService(session).get_user(tokens.user.id)
    profile_service = ProfileService(session)
    await profile_service.ensure_lookups()
    boards = await profile_service.list_boards()
    classes = await profile_service.list_classes()
    streams = await profile_service.list_streams()
    class_12 = next(c for c in classes if c.grade == 12)
    pcm = next(s for s in streams if s.code == "SCIENCE_PCM")
    profile = await profile_service.get_or_create_profile(user)
    profile.photo_url = "/media/profiles/demo.jpg"
    await profile_service.profiles.update(profile)
    await profile_service.update_profile(
        user,
        ProfileUpdateRequest(
            mobile="9876501234",
            board_id=boards[0].id,
            class_id=class_12.id,
            stream_id=pcm.id,
        ),
    )
    subjects = await SyllabusService(session).list_subjects(user)
    physics = next(s for s in subjects if s.code == "PHY")
    detail = await SyllabusService(session).get_subject_chapters(user, physics.id)
    chapter = await SyllabusService(session).get_chapter_topics(user, detail.chapters[0].id)
    return user, chapter.topics[0].id, chapter


async def _complete_quiz_with_correct_count(
    service: QuizService,
    user,
    quiz_id,
    *,
    correct_count: int,
):
    attempt = await service.start(user, quiz_id)
    orm_quiz = await service.quizzes.get_with_questions(quiz_id)
    assert orm_quiz is not None
    total = attempt.total_questions
    correct_count = max(0, min(correct_count, total))

    for index in range(total):
        question = await service.current_question(user, attempt.id)
        orm_q = next(q for q in orm_quiz.questions if q.id == question.id)
        if index < correct_count:
            option = next(o for o in orm_q.options if o.is_correct)
        else:
            option = next(o for o in orm_q.options if not o.is_correct)
        await service.submit_answer(
            user,
            attempt.id,
            SubmitAnswerRequest(option_id=option.id),
        )
        if question.question_number < question.total_questions:
            await service.next_question(user, attempt.id)
    return await service.complete(user, attempt.id)


def test_coin_reward_config_default() -> None:
    assert coin_reward_per_topic() == 10


@pytest.mark.asyncio
async def test_failing_quiz_awards_no_coins(db_session: AsyncSession) -> None:
    user, topic_id, chapter = await _ready_user(db_session, "coinsfail@example.com")
    service = QuizService(db_session)
    quiz = (await service.list_for_topic(user, topic_id))[0]
    detail = await service.get_quiz(user, quiz.id)
    total = detail.question_count
    # Just under 60%.
    correct = max(0, (TOPIC_COMPLETE_PERCENTAGE * total - 1) // 100)

    profile_before = await service.profiles.get_by_user_id(user.id)
    assert profile_before is not None
    coins_before = profile_before.total_coins or 0
    xp_before = profile_before.total_xp or 0

    result = await _complete_quiz_with_correct_count(
        service, user, quiz.id, correct_count=correct,
    )
    assert result.percentage < TOPIC_COMPLETE_PERCENTAGE
    assert result.topic_completed is False
    assert result.coins_earned == 0
    assert result.coins_awarded is False
    assert result.xp_earned == 0
    assert result.xp_awarded is False
    assert result.total_coins == coins_before
    assert result.total_xp == xp_before

    profile = await service.profiles.get_by_user_id(user.id)
    assert profile is not None
    assert profile.total_coins == coins_before
    assert (profile.total_xp or 0) == xp_before

    refreshed = await SyllabusService(db_session).get_chapter_topics(user, chapter.id)
    assert refreshed.topics[0].is_completed is False
    if len(refreshed.topics) > 1:
        assert refreshed.topics[1].is_locked is True


@pytest.mark.asyncio
async def test_exactly_sixty_percent_awards_coins(db_session: AsyncSession) -> None:
    user, topic_id, chapter = await _ready_user(db_session, "coins60@example.com")
    service = QuizService(db_session)
    quiz = (await service.list_for_topic(user, topic_id))[0]
    detail = await service.get_quiz(user, quiz.id)
    total = detail.question_count
    # Smallest correct count that reaches >= 60%.
    correct = max(1, (TOPIC_COMPLETE_PERCENTAGE * total + 99) // 100)

    profile_before = await service.profiles.get_by_user_id(user.id)
    assert profile_before is not None
    coins_before = profile_before.total_coins or 0
    xp_before = profile_before.total_xp or 0

    result = await _complete_quiz_with_correct_count(
        service, user, quiz.id, correct_count=correct,
    )
    assert result.percentage >= TOPIC_COMPLETE_PERCENTAGE
    assert result.topic_completed is True
    assert result.coins_earned == coin_reward_per_topic()
    assert result.coins_awarded is True
    assert result.total_coins == coins_before + coin_reward_per_topic()
    assert result.total_xp >= xp_before

    profile = await service.profiles.get_by_user_id(user.id)
    assert profile is not None
    assert profile.total_coins == coins_before + coin_reward_per_topic()
    assert (profile.total_xp or 0) >= xp_before

    refreshed = await SyllabusService(db_session).get_chapter_topics(user, chapter.id)
    assert refreshed.topics[0].is_completed is True
    if len(refreshed.topics) > 1:
        assert refreshed.topics[1].is_locked is False


@pytest.mark.asyncio
@pytest.mark.parametrize("ratio", [0.8, 1.0])
async def test_high_score_awards_coins(db_session: AsyncSession, ratio: float) -> None:
    user, topic_id, _ = await _ready_user(db_session, f"coins{int(ratio*100)}@example.com")
    service = QuizService(db_session)
    quiz = (await service.list_for_topic(user, topic_id))[0]
    detail = await service.get_quiz(user, quiz.id)
    correct = int(round(detail.question_count * ratio))
    profile_before = await service.profiles.get_by_user_id(user.id)
    assert profile_before is not None
    coins_before = profile_before.total_coins or 0

    result = await _complete_quiz_with_correct_count(
        service, user, quiz.id, correct_count=correct,
    )
    assert result.percentage >= TOPIC_COMPLETE_PERCENTAGE
    assert result.topic_completed is True
    assert result.coins_earned == coin_reward_per_topic()
    assert result.coins_awarded is True
    assert result.total_coins == coins_before + coin_reward_per_topic()

    profile = await service.profiles.get_by_user_id(user.id)
    assert profile is not None
    assert profile.total_coins == coins_before + coin_reward_per_topic()


@pytest.mark.asyncio
async def test_retry_does_not_award_coins_again(db_session: AsyncSession) -> None:
    user, topic_id, _ = await _ready_user(db_session, "coinsretry@example.com")
    service = QuizService(db_session)
    quiz = (await service.list_for_topic(user, topic_id))[0]
    detail = await service.get_quiz(user, quiz.id)

    first = await _complete_quiz_with_correct_count(
        service, user, quiz.id, correct_count=detail.question_count,
    )
    assert first.topic_completed is True
    assert first.coins_earned == coin_reward_per_topic()
    assert first.coins_awarded is True
    coins_after_first = first.total_coins
    xp_after_first = first.total_xp

    second = await _complete_quiz_with_correct_count(
        service, user, quiz.id, correct_count=detail.question_count,
    )
    assert second.topic_completed is True
    assert second.coins_earned == 0
    assert second.coins_awarded is False
    assert second.total_coins == coins_after_first
    assert second.xp_awarded is False
    assert second.xp_earned == 0
    assert second.total_xp == xp_after_first

    profile = await service.profiles.get_by_user_id(user.id)
    assert profile is not None
    assert profile.total_coins == coins_after_first
    assert profile.total_xp == xp_after_first


@pytest.mark.asyncio
async def test_profile_exposes_total_coins(db_session: AsyncSession) -> None:
    user, topic_id, _ = await _ready_user(db_session, "coinsprofile@example.com")
    service = QuizService(db_session)
    quiz = (await service.list_for_topic(user, topic_id))[0]
    detail = await service.get_quiz(user, quiz.id)
    await _complete_quiz_with_correct_count(
        service, user, quiz.id, correct_count=detail.question_count,
    )

    profile = await ProfileService(db_session).get_profile(user)
    assert profile.total_coins == coin_reward_per_topic()
    assert profile.total_xp > 0
