"""Same-email household accounts stay isolated."""

from __future__ import annotations

import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.auth import LoginRequest, RegisterRequest
from app.schemas.profile import ProfileUpdateRequest
from app.schemas.quiz import SubmitAnswerRequest
from app.services.auth import AuthService
from app.services.profile import ProfileService
from app.services.quiz import QuizService
from app.services.syllabus import SyllabusService


async def _register_pcm(session: AsyncSession, *, email: str, password: str, name: str, grade: int):
    tokens = await AuthService(session).register(
        RegisterRequest(email=email, password=password, full_name=name),
    )
    user = await AuthService(session).get_user(tokens.user.id)
    profile_service = ProfileService(session)
    await profile_service.ensure_lookups()
    boards = await profile_service.list_boards()
    classes = await profile_service.list_classes()
    streams = await profile_service.list_streams()
    school_class = next(c for c in classes if c.grade == grade)
    pcm = next(s for s in streams if s.code == "SCIENCE_PCM")
    pcb = next(s for s in streams if s.code == "SCIENCE_PCB")
    profile = await profile_service.get_or_create_profile(user)
    profile.photo_url = "/media/profiles/demo.jpg"
    await profile_service.profiles.update(profile)
    await profile_service.update_profile(
        user,
        ProfileUpdateRequest(
            mobile="9876508888",
            board_id=boards[0].id,
            class_id=school_class.id,
            stream_id=pcm.id if grade >= 11 and grade == 12 else pcb.id if grade == 11 else None,
        ),
    )
    return user


async def _perfect_quiz(session: AsyncSession, user) -> None:
    subjects = await SyllabusService(session).list_subjects(user)
    physics = next(s for s in subjects if s.code == "PHY")
    detail = await SyllabusService(session).get_subject_chapters(user, physics.id)
    chapter = await SyllabusService(session).get_chapter_topics(user, detail.chapters[0].id)
    topic = chapter.topics[0]
    service = QuizService(session)
    quiz = (await service.list_for_topic(user, topic.id))[0]
    attempt = await service.start(user, quiz.id)
    loaded = await service.quizzes.get_with_questions(quiz.id)
    assert loaded is not None
    for _ in range(attempt.total_questions):
        question = await service.current_question(user, attempt.id)
        orm_q = next(q for q in loaded.questions if q.id == question.id)
        correct = next(o for o in orm_q.options if o.is_correct)
        await service.submit_answer(user, attempt.id, SubmitAnswerRequest(option_id=correct.id))
        if question.question_number < question.total_questions:
            await service.next_question(user, attempt.id)
    await service.complete(user, attempt.id)


@pytest.mark.asyncio
async def test_same_email_accounts_do_not_share_progress(db_session: AsyncSession) -> None:
    email = "siblings@example.com"
    user_a = await _register_pcm(
        db_session, email=email, password="PasswordA1!", name="Student A", grade=12,
    )
    user_b = await _register_pcm(
        db_session, email=email, password="PasswordB1!", name="Student B", grade=11,
    )
    assert user_a.id != user_b.id

    await _perfect_quiz(db_session, user_a)

    profile_a = await ProfileService(db_session).get_profile(user_a)
    profile_b = await ProfileService(db_session).get_profile(user_b)
    assert profile_a.total_xp > 0
    assert profile_a.total_coins > 0
    assert profile_b.total_xp == 0
    assert profile_b.total_coins == 0
    assert profile_a.school_class and profile_a.school_class.grade == 12
    assert profile_b.school_class and profile_b.school_class.grade == 11

    subjects_a = await SyllabusService(db_session).list_subjects(user_a)
    subjects_b = await SyllabusService(db_session).list_subjects(user_b)
    phy_a = next(s for s in subjects_a if s.code == "PHY")
    phy_b = next(s for s in subjects_b if s.code == "PHY")
    assert phy_a.completed_topic_count >= 1
    assert phy_b.completed_topic_count == 0

    login_a = await AuthService(db_session).login(
        LoginRequest(email=email, password="PasswordA1!"),
    )
    login_b = await AuthService(db_session).login(
        LoginRequest(email=email, password="PasswordB1!"),
    )
    assert login_a.user.id == user_a.id
    assert login_b.user.id == user_b.id
