"""Critical EduQuest product rules (auth, syllabus, unlock, quiz, rewards)."""

from __future__ import annotations

import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.exceptions import ForbiddenError, UnauthorizedError
from app.data.syllabus.catalog import subjects_for_profile, SUPPORTED_BOARDS
from app.schemas.auth import LoginRequest, RegisterRequest
from app.schemas.profile import ProfileUpdateRequest
from app.schemas.quiz import SubmitAnswerRequest
from app.schemas.syllabus import TopicProgressUpdate
from app.services.auth import AuthService
from app.services.coins import coin_reward_per_topic
from app.services.profile import ProfileService
from app.services.quiz import TOPIC_COMPLETE_PERCENTAGE, QuizService
from app.services.quiz_seed import MAX_QUESTIONS_PER_TOPIC, questions_for_topic
from app.services.syllabus import SyllabusService
from app.services.topic_quiz_builder import is_meta_question, validate_question_bank


async def _ready(
    session: AsyncSession,
    email: str,
    *,
    password: str = "Secret123!",
    name: str = "Rule Student",
    grade: int = 8,
    stream_code: str | None = None,
    board_code: str = "CBSE",
):
    tokens = await AuthService(session).register(
        RegisterRequest(email=email, password=password, full_name=name),
    )
    user = await AuthService(session).get_user(tokens.user.id)
    profile_service = ProfileService(session)
    await profile_service.ensure_lookups()
    boards = await profile_service.list_boards()
    board = next(item for item in boards if item.code == board_code)
    classes = await profile_service.list_classes()
    streams = await profile_service.list_streams()
    school_class = next(item for item in classes if item.grade == grade)
    stream = next((item for item in streams if item.code == stream_code), None)
    profile = await profile_service.get_or_create_profile(user)
    profile.photo_url = "/media/profiles/demo.jpg"
    await profile_service.profiles.update(profile)
    await profile_service.update_profile(
        user,
        ProfileUpdateRequest(
            mobile="9876500000",
            board_id=board.id,
            class_id=school_class.id,
            stream_id=stream.id if stream else None,
        ),
    )
    return user, tokens


async def _chapter(session: AsyncSession, user, subject_code: str | None = None):
    subjects = await SyllabusService(session).list_subjects(user)
    subject = subjects[0] if subject_code is None else next(s for s in subjects if s.code == subject_code)
    detail = await SyllabusService(session).get_subject_chapters(user, subject.id)
    return await SyllabusService(session).get_chapter_topics(user, detail.chapters[0].id)


async def _complete_with_correct(service: QuizService, user, quiz_id, correct_count: int):
    attempt = await service.start(user, quiz_id)
    orm_quiz = await service.quizzes.get_with_questions(quiz_id)
    assert orm_quiz is not None
    total = attempt.total_questions
    correct_count = max(0, min(correct_count, total))
    for index in range(total):
        question = await service.current_question(user, attempt.id)
        orm_q = next(q for q in orm_quiz.questions if q.id == question.id)
        option = next(
            o for o in orm_q.options
            if o.is_correct is (index < correct_count)
        )
        await service.submit_answer(user, attempt.id, SubmitAnswerRequest(option_id=option.id))
        if question.question_number < question.total_questions:
            await service.next_question(user, attempt.id)
    return await service.complete(user, attempt.id)


@pytest.mark.asyncio
async def test_same_email_password_selects_account(db_session: AsyncSession) -> None:
    email = "house@example.com"
    user_a, _ = await _ready(db_session, email, password="PasswordA1!", name="Student A", grade=12, stream_code="SCIENCE_PCM")
    user_b, _ = await _ready(db_session, email, password="PasswordB1!", name="Student B", grade=11, stream_code="SCIENCE_PCB")
    login_a = await AuthService(db_session).login(LoginRequest(email=email, password="PasswordA1!"))
    login_b = await AuthService(db_session).login(LoginRequest(email=email, password="PasswordB1!"))
    assert login_a.user.id == user_a.id
    assert login_b.user.id == user_b.id
    with pytest.raises(UnauthorizedError):
        await AuthService(db_session).login(LoginRequest(email=email, password="WrongPass1!"))
    switched = await AuthService(db_session).login(
        LoginRequest(user_id=user_b.id, password="PasswordB1!"),
    )
    assert switched.user.id == user_b.id


@pytest.mark.asyncio
async def test_icse_and_state_load_class_subjects(db_session: AsyncSession) -> None:
    for board in ("ICSE", "STATE"):
        user, _ = await _ready(
            db_session,
            f"{board.lower()}@example.com",
            grade=8,
            board_code=board,
        )
        subjects = await SyllabusService(db_session).list_subjects(user)
        assert {s.code for s in subjects} >= {"MATH", "SCI", "ENG", "SST"}
        blueprint = subjects_for_profile(board, 8, None)
        assert {spec["code"] for spec in blueprint} == {s.code for s in subjects}


@pytest.mark.asyncio
async def test_class_11_pcm_not_pcb_subjects(db_session: AsyncSession) -> None:
    user, _ = await _ready(
        db_session,
        "pcm@example.com",
        grade=11,
        stream_code="SCIENCE_PCM",
    )
    codes = {s.code for s in await SyllabusService(db_session).list_subjects(user)}
    assert codes == {"PHY", "CHEM", "MATH", "ENG"}
    assert "BIO" not in codes
    assert "SST" not in codes


def test_class_6_to_10_does_not_require_stream() -> None:
    for grade in range(6, 11):
        blueprint = subjects_for_profile("CBSE", grade, "SCIENCE_PCM")
        codes = {spec["code"] for spec in blueprint}
        assert "PHY" not in codes
        assert {"MATH", "SCI", "ENG", "SST"} <= codes


@pytest.mark.asyncio
async def test_class_11_12_require_stream_and_match_subjects(db_session: AsyncSession) -> None:
    user, _ = await _ready(
        db_session,
        "streamreq@example.com",
        grade=12,
        stream_code="SCIENCE_PCM",
    )
    codes = {s.code for s in await SyllabusService(db_session).list_subjects(user)}
    assert codes == {spec["code"] for spec in subjects_for_profile("CBSE", 12, "SCIENCE_PCM")}
    assert codes == {"PHY", "CHEM", "MATH", "ENG"}


@pytest.mark.asyncio
async def test_clicking_or_opening_does_not_unlock(db_session: AsyncSession) -> None:
    user, _ = await _ready(db_session, "click@example.com")
    chapter = await _chapter(db_session, user)
    assert chapter.topics[0].is_locked is False
    assert chapter.topics[1].is_locked is True
    await QuizService(db_session).list_for_topic(user, chapter.topics[1].id)
    await SyllabusService(db_session).get_topic_lock_state(user, chapter.topics[1].id)
    with pytest.raises(ForbiddenError):
        await SyllabusService(db_session).set_topic_progress(
            user,
            chapter.topics[1].id,
            TopicProgressUpdate(is_completed=True),
        )
    quizzes = await QuizService(db_session).list_for_topic(user, chapter.topics[1].id)
    assert quizzes, "Locked topic still has a quiz, but start must be rejected"
    with pytest.raises(ForbiddenError):
        await QuizService(db_session).start(user, quizzes[0].id)
    again = await SyllabusService(db_session).get_chapter_topics(user, chapter.id)
    assert again.topics[1].is_locked is True
    if len(again.topics) > 2:
        assert again.topics[2].is_locked is True


@pytest.mark.asyncio
async def test_pass_unlocks_only_next_topic(db_session: AsyncSession) -> None:
    user, _ = await _ready(db_session, "unlockchain@example.com", grade=12, stream_code="SCIENCE_PCM")
    chapter = await _chapter(db_session, user, "PHY")
    assert len(chapter.topics) >= 3
    service = QuizService(db_session)

    quiz1 = (await service.list_for_topic(user, chapter.topics[0].id))[0]
    first = await _complete_with_correct(service, user, quiz1.id, quiz1.question_count)
    assert first.topic_completed is True
    after1 = await SyllabusService(db_session).get_chapter_topics(user, chapter.id)
    assert after1.topics[0].is_completed is True
    assert after1.topics[1].is_locked is False
    assert after1.topics[1].is_current is True
    assert after1.topics[2].is_locked is True

    quiz2 = (await service.list_for_topic(user, after1.topics[1].id))[0]
    second = await _complete_with_correct(service, user, quiz2.id, quiz2.question_count)
    assert second.topic_completed is True
    after2 = await SyllabusService(db_session).get_chapter_topics(user, chapter.id)
    assert after2.topics[2].is_locked is False
    assert after2.topics[2].is_current is True
    if len(after2.topics) > 3:
        assert after2.topics[3].is_locked is True


@pytest.mark.asyncio
async def test_current_topic_has_startable_quiz(db_session: AsyncSession) -> None:
    user, _ = await _ready(db_session, "startquiz@example.com")
    chapter = await _chapter(db_session, user)
    current = next(t for t in chapter.topics if t.is_current)
    quizzes = await QuizService(db_session).list_for_topic(user, current.id)
    assert quizzes
    assert 1 <= quizzes[0].question_count <= MAX_QUESTIONS_PER_TOPIC


def test_subject_banks_are_not_physics_fallback() -> None:
    chem = questions_for_topic("Mole concept", chapter_title="Some Basic Concepts of Chemistry", subject_code="CHEM", grade=11)
    math = questions_for_topic("Types of matrices", chapter_title="Matrices", subject_code="MATH", grade=12)
    eng = questions_for_topic("The Last Lesson", chapter_title="Flamingo – Prose", subject_code="ENG", grade=12)
    phy = questions_for_topic(
        "The international system of units",
        chapter_title="Units and Measurements",
        subject_code="PHY",
        grade=11,
    )
    assert len(chem) <= MAX_QUESTIONS_PER_TOPIC and len(chem) >= 4
    assert len(math) <= MAX_QUESTIONS_PER_TOPIC and len(math) >= 4
    assert len(eng) <= MAX_QUESTIONS_PER_TOPIC and len(eng) >= 4
    assert len(phy) <= MAX_QUESTIONS_PER_TOPIC and len(phy) >= 8
    chem_text = " ".join(p for p, _ in chem).lower()
    math_text = " ".join(p for p, _ in math).lower()
    eng_text = " ".join(p for p, _ in eng).lower()
    phy_text = " ".join(
        [p for p, _ in phy] + [opt for _, options in phy for opt, _ in options]
    ).lower()
    assert "coulomb" not in chem_text
    assert "electric charge" not in math_text
    assert "coulomb" not in eng_text
    assert "metre" in phy_text or "kilogram" in phy_text or "dimension" in phy_text
    assert validate_question_bank("Mole concept", chem) == []
    assert all(not is_meta_question(p, o) for p, o in chem + math + eng + phy)


@pytest.mark.asyncio
async def test_fifty_nine_fails_sixty_passes(db_session: AsyncSession) -> None:
    user, _ = await _ready(db_session, "threshold@example.com", grade=12, stream_code="SCIENCE_PCM")
    chapter = await _chapter(db_session, user, "PHY")
    service = QuizService(db_session)
    quiz = (await service.list_for_topic(user, chapter.topics[0].id))[0]
    total = quiz.question_count
    fail_count = max(0, (TOPIC_COMPLETE_PERCENTAGE * total - 1) // 100)
    fail = await _complete_with_correct(service, user, quiz.id, fail_count)
    assert fail.percentage < 60
    assert fail.topic_completed is False
    assert fail.xp_awarded is False
    assert fail.coins_awarded is False
    locked = await SyllabusService(db_session).get_chapter_topics(user, chapter.id)
    assert locked.topics[0].is_completed is False
    assert locked.topics[1].is_locked is True

    pass_count = max(1, (TOPIC_COMPLETE_PERCENTAGE * total + 99) // 100)
    passed = await _complete_with_correct(service, user, quiz.id, pass_count)
    assert passed.percentage >= 60
    assert passed.topic_completed is True
    assert passed.coins_earned == coin_reward_per_topic()
    assert passed.xp_awarded is True


@pytest.mark.asyncio
async def test_logout_revokes_refresh_not_other_account(db_session: AsyncSession) -> None:
    email = "logout-house@example.com"
    user_a, tokens_a = await _ready(db_session, email, password="PasswordA1!", name="Student A")
    user_b, tokens_b = await _ready(db_session, email, password="PasswordB1!", name="Student B", grade=9)
    await AuthService(db_session).logout(tokens_a.refresh_token, user_id=user_a.id)
    with pytest.raises(UnauthorizedError):
        await AuthService(db_session).refresh(tokens_a.refresh_token)
    still_b = await AuthService(db_session).refresh(tokens_b.refresh_token)
    assert still_b.user.id == user_b.id


@pytest.mark.asyncio
async def test_eighty_and_hundred_percent_pass_and_retry_is_idempotent(
    db_session: AsyncSession,
) -> None:
    user, _ = await _ready(db_session, "rewards@example.com", grade=12, stream_code="SCIENCE_PCM")
    chapter = await _chapter(db_session, user, "PHY")
    service = QuizService(db_session)
    quiz = (await service.list_for_topic(user, chapter.topics[0].id))[0]
    total = quiz.question_count
    eighty = max(1, (80 * total + 99) // 100)
    first = await _complete_with_correct(service, user, quiz.id, eighty)
    assert first.percentage >= 60
    assert first.topic_completed is True
    assert first.xp_awarded is True
    assert first.coins_awarded is True
    xp_after = first.total_xp
    coins_after = first.total_coins

    perfect = await _complete_with_correct(service, user, quiz.id, total)
    assert perfect.percentage == 100
    assert perfect.topic_completed is True
    assert perfect.xp_awarded is False
    assert perfect.coins_awarded is False
    assert perfect.total_xp == xp_after
    assert perfect.total_coins == coins_after

    refreshed = await ProfileService(db_session).get_profile(user)
    assert refreshed.total_xp == xp_after
    assert refreshed.total_coins == coins_after


def test_central_catalog_covers_supported_boards() -> None:
    assert set(SUPPORTED_BOARDS) == {"CBSE", "ICSE", "STATE"}
    for board in SUPPORTED_BOARDS:
        blueprint = subjects_for_profile(board, 10, None)
        assert {spec["code"] for spec in blueprint} >= {"MATH", "SCI", "ENG", "SST"}
        pcm = subjects_for_profile(board, 12, "SCIENCE_PCM")
        assert {spec["code"] for spec in pcm} == {"PHY", "CHEM", "MATH", "ENG"}
