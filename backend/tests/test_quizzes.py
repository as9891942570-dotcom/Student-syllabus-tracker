"""Phase 6 quiz system unit and API tests."""

from datetime import datetime, timedelta, timezone
from io import BytesIO
from uuid import uuid4

import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.exceptions import ConflictError, ForbiddenError, NotFoundError, ValidationAppError
from app.models.quiz_attempt import QuizAttempt
from app.schemas.auth import RegisterRequest
from app.schemas.profile import ProfileUpdateRequest
from app.schemas.quiz import SubmitAnswerRequest
from app.services.auth import AuthService
from app.services.profile import ProfileService
from app.services.quiz import (
    QuizService,
    calculate_quiz_percentage,
    calculate_quiz_score,
    calculate_quiz_xp,
)
from app.services.quiz_seed import (
    LEGACY_PROMPT_FRAGMENTS,
    TOPIC_QUESTION_BANKS,
    contains_legacy_prompt,
    questions_for_topic,
)
from app.services.syllabus import SyllabusService


def test_score_percentage_and_xp_helpers() -> None:
    assert calculate_quiz_percentage(correct=3, total=3) == 100
    assert calculate_quiz_percentage(correct=1, total=4) == 25
    assert calculate_quiz_percentage(correct=0, total=0) == 0
    assert calculate_quiz_score(correct=2, total=4) == 50
    # base 20 + 30% of 30 (=9) + 2*2 correct + 0 perfect = 33
    assert calculate_quiz_xp(percentage=30, correct_count=2) == 20 + 9 + 4
    assert calculate_quiz_xp(percentage=100, correct_count=3) == 20 + 30 + 6 + 15


async def _ready_user(session: AsyncSession, email: str):
    tokens = await AuthService(session).register(
        RegisterRequest(email=email, password="Secret123!", full_name="Quiz Student"),
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
            mobile="9876501234",
            board_id=boards[0].id,
            class_id=class_8.id,
        ),
    )
    subjects = await SyllabusService(session).list_subjects(user)
    detail = await SyllabusService(session).get_subject_chapters(user, subjects[0].id)
    chapter = await SyllabusService(session).get_chapter_topics(
        user,
        detail.chapters[0].id,
    )
    return user, chapter.topics[0].id


async def _auth_header(client: AsyncClient, email: str) -> dict[str, str]:
    await client.post(
        "/api/v1/auth/register",
        json={
            "email": email,
            "password": "Secret123!",
            "full_name": "API Quiz Student",
        },
    )
    login = await client.post(
        "/api/v1/auth/login",
        json={"email": email, "password": "Secret123!"},
    )
    token = login.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}


async def _complete_profile(client: AsyncClient, headers: dict[str, str]) -> None:
    boards = (await client.get("/api/v1/boards", headers=headers)).json()
    classes = (await client.get("/api/v1/classes", headers=headers)).json()
    class_8 = next(c for c in classes if c["grade"] == 8)
    # photo required for completion
    await client.post(
        "/api/v1/profile/me/photo",
        headers=headers,
        files={"file": ("a.png", BytesIO(b"\x89PNG\r\n\x1a\nfake"), "image/png")},
    )
    await client.put(
        "/api/v1/profile/me",
        headers=headers,
        json={
            "mobile": "9876509999",
            "board_id": boards[0]["id"],
            "class_id": class_8["id"],
        },
    )


@pytest.mark.asyncio
async def test_history_topic_quizzes_use_subject_questions(db_session: AsyncSession) -> None:
    """Ancient / Medieval / Modern overview must seed history questions, not app meta."""
    tokens = await AuthService(db_session).register(
        RegisterRequest(
            email="quizhistory@example.com",
            password="Secret123!",
            full_name="History Student",
        ),
    )
    user = await AuthService(db_session).get_user(tokens.user.id)
    profile_service = ProfileService(db_session)
    await profile_service.ensure_lookups()
    boards = await profile_service.list_boards()
    classes = await profile_service.list_classes()
    streams = await profile_service.list_streams()
    class_11 = next(c for c in classes if c.grade == 11)
    arts = next(s for s in streams if s.code == "ARTS")
    profile = await profile_service.get_or_create_profile(user)
    profile.photo_url = "/media/profiles/demo.jpg"
    await profile_service.profiles.update(profile)
    await profile_service.update_profile(
        user,
        ProfileUpdateRequest(
            mobile="9876505555",
            board_id=boards[0].id,
            class_id=class_11.id,
            stream_id=arts.id,
        ),
    )

    subjects = await SyllabusService(db_session).list_subjects(user)
    history = next(s for s in subjects if s.name == "History")
    detail = await SyllabusService(db_session).get_subject_chapters(user, history.id)
    chapter = await SyllabusService(db_session).get_chapter_topics(
        user,
        detail.chapters[0].id,
    )

    service = QuizService(db_session)
    required = ("Ancient", "Medieval", "Modern overview")
    found = {t.title: t for t in chapter.topics if t.title in required}
    assert set(found) == set(required)

    for title, topic in found.items():
        expected_prompts = [prompt for prompt, _ in questions_for_topic(title)]
        assert len(expected_prompts) == 3

        quizzes = await service.list_for_topic(user, topic.id)
        assert quizzes[0].question_count == 3

        # Force a second ensure to prove legacy refresh path stays topic-correct.
        quizzes = await service.list_for_topic(user, topic.id)
        attempt = await service.start(user, quizzes[0].id)
        assert attempt.total_questions == 3

        from app.repositories.quiz import QuizRepository

        loaded = await QuizRepository(db_session).get_with_questions(quizzes[0].id)
        assert loaded is not None
        prompts = [q.prompt for q in sorted(loaded.questions, key=lambda item: item.sort_order)]
        assert prompts == expected_prompts
        for prompt in prompts:
            assert not contains_legacy_prompt(prompt)
            for fragment in LEGACY_PROMPT_FRAGMENTS:
                assert fragment.lower() not in prompt.lower()

        for question in loaded.questions:
            correct = [o for o in question.options if o.is_correct]
            assert len(question.options) >= 2
            assert len(correct) == 1

        # Complete so the next topic can start (one active attempt limit).
        await service.complete(user, attempt.id)

    # Banks themselves must never include legacy EduQuest prompts.
    for key, bank in TOPIC_QUESTION_BANKS.items():
        assert len(bank) == 3
        for prompt, options in bank:
            assert not contains_legacy_prompt(prompt)
            assert sum(1 for _, ok in options if ok) == 1


@pytest.mark.asyncio
async def test_seeded_quiz_has_three_questions_immediately(db_session: AsyncSession) -> None:
    """Questions must be associated in-session (not only via FK after reload)."""
    user, topic_id = await _ready_user(db_session, "quizseed@example.com")
    service = QuizService(db_session)

    quizzes = await service.list_for_topic(user, topic_id)
    assert len(quizzes) >= 1
    assert quizzes[0].question_count == 3

    detail = await service.get_quiz(user, quizzes[0].id)
    assert detail.question_count == 3

    attempt = await service.start(user, quizzes[0].id)
    assert attempt.total_questions == 3
    assert attempt.status == "active"
    assert attempt.seconds_remaining > 0

    question = await service.current_question(user, attempt.id)
    assert question.question_number == 1
    assert question.total_questions == 3
    assert len(question.options) >= 2
    assert "is_correct" not in question.model_dump()


@pytest.mark.asyncio
async def test_backfill_empty_quiz_questions(db_session: AsyncSession) -> None:
    user, topic_id = await _ready_user(db_session, "quizempty@example.com")
    from app.models.quiz import Quiz

    empty = Quiz(
        topic_id=topic_id,
        title="Broken empty quiz",
        time_limit_seconds=180,
        is_active=True,
        sort_order=0,
    )
    db_session.add(empty)
    await db_session.flush()

    service = QuizService(db_session)
    detail = await service.get_quiz(user, empty.id)
    assert detail.question_count == 3

    attempt = await service.start(user, empty.id)
    assert attempt.total_questions == 3


@pytest.mark.asyncio
async def test_list_start_answer_complete_quiz(db_session: AsyncSession) -> None:
    user, topic_id = await _ready_user(db_session, "quiz1@example.com")
    service = QuizService(db_session)

    quizzes = await service.list_for_topic(user, topic_id)
    assert len(quizzes) >= 1
    quiz = await service.get_quiz(user, quizzes[0].id)
    assert quiz.question_count == 3
    assert quiz.topic_id == topic_id

    attempt = await service.start(user, quiz.id)
    assert attempt.status == "active"
    assert attempt.total_questions == 3
    assert attempt.xp_earned == 0

    question = await service.current_question(user, attempt.id)
    assert "is_correct" not in question.model_dump()
    assert all("is_correct" not in o.model_dump() for o in question.options)
    assert len(question.options) >= 2

    # Find correct option from ORM (not API)
    orm_q = next(q for q in (await service.quizzes.get_with_questions(quiz.id)).questions if q.id == question.id)
    correct_opt = next(o for o in orm_q.options if o.is_correct)
    wrong_opt = next(o for o in orm_q.options if not o.is_correct)

    submit = await service.submit_answer(
        user,
        attempt.id,
        SubmitAnswerRequest(option_id=correct_opt.id),
    )
    assert submit.is_correct is True
    assert submit.correct_count == 1

    with pytest.raises(ConflictError):
        await service.submit_answer(
            user,
            attempt.id,
            SubmitAnswerRequest(option_id=wrong_opt.id),
        )

    await service.next_question(user, attempt.id)
    q2 = await service.current_question(user, attempt.id)
    orm_q2 = next(q for q in (await service.quizzes.get_with_questions(quiz.id)).questions if q.id == q2.id)
    wrong2 = next(o for o in orm_q2.options if not o.is_correct)
    await service.submit_answer(user, attempt.id, SubmitAnswerRequest(option_id=wrong2.id))

    await service.next_question(user, attempt.id)
    q3 = await service.current_question(user, attempt.id)
    orm_q3 = next(q for q in (await service.quizzes.get_with_questions(quiz.id)).questions if q.id == q3.id)
    correct3 = next(o for o in orm_q3.options if o.is_correct)
    await service.submit_answer(user, attempt.id, SubmitAnswerRequest(option_id=correct3.id))

    result = await service.complete(user, attempt.id)
    assert result.status == "completed"
    assert result.total_questions == 3
    assert result.answered_count == 3
    assert result.correct_count == 2
    assert result.incorrect_count == 1
    assert result.percentage == 67
    assert result.score == 67
    assert result.xp_earned == calculate_quiz_xp(percentage=67, correct_count=2)
    assert result.total_xp == result.xp_earned
    assert result.topic_completed is True

    with pytest.raises(ConflictError):
        await service.submit_answer(
            user,
            attempt.id,
            SubmitAnswerRequest(option_id=correct3.id),
        )

    history = await service.history(user)
    assert len(history) == 1
    assert history[0].percentage == 67
    assert history[0].completed is True


@pytest.mark.asyncio
async def test_invalid_quiz_topic_option_and_auth(db_session: AsyncSession) -> None:
    user, topic_id = await _ready_user(db_session, "quiz2@example.com")
    other, _ = await _ready_user(db_session, "quiz2b@example.com")
    service = QuizService(db_session)

    with pytest.raises(NotFoundError):
        await service.list_for_topic(user, uuid4())

    with pytest.raises(NotFoundError):
        await service.get_quiz(user, uuid4())

    with pytest.raises(NotFoundError):
        await service.start(user, uuid4())

    quizzes = await service.list_for_topic(user, topic_id)
    attempt = await service.start(user, quizzes[0].id)
    question = await service.current_question(user, attempt.id)

    with pytest.raises(ValidationAppError):
        await service.submit_answer(
            user,
            attempt.id,
            SubmitAnswerRequest(option_id=uuid4()),
        )

    with pytest.raises(ForbiddenError):
        await service.current_question(other, attempt.id)

    # Correct answer not in public payload
    dumped = question.model_dump()
    assert "is_correct" not in dumped
    for opt in dumped["options"]:
        assert "is_correct" not in opt
        assert "correct" not in opt


@pytest.mark.asyncio
async def test_expired_attempt_auto_completes(db_session: AsyncSession) -> None:
    user, topic_id = await _ready_user(db_session, "quiz3@example.com")
    service = QuizService(db_session)
    quizzes = await service.list_for_topic(user, topic_id)
    attempt = await service.start(user, quizzes[0].id)

    row = await db_session.get(QuizAttempt, attempt.id)
    assert row is not None
    row.expires_at = datetime.now(timezone.utc) - timedelta(seconds=5)
    await db_session.flush()

    with pytest.raises(ConflictError):
        await service.current_question(user, attempt.id)

    result = await service.get_result(user, attempt.id)
    assert result.status == "expired"
    assert result.xp_earned > 0


@pytest.mark.asyncio
async def test_quiz_api_auth_and_flow(client: AsyncClient) -> None:
    # Unauthenticated
    unauth = await client.get(f"/api/v1/quizzes/topics/{uuid4()}")
    assert unauth.status_code == 401

    headers = await _auth_header(client, "quizapi@example.com")
    await _complete_profile(client, headers)

    subjects = (await client.get("/api/v1/syllabus/subjects", headers=headers)).json()
    chapters = (
        await client.get(f"/api/v1/syllabus/subjects/{subjects[0]['id']}", headers=headers)
    ).json()
    topics = (
        await client.get(
            f"/api/v1/syllabus/chapters/{chapters['chapters'][0]['id']}/topics",
            headers=headers,
        )
    ).json()
    topic_id = topics["topics"][0]["id"]

    quizzes = (await client.get(f"/api/v1/quizzes/topics/{topic_id}", headers=headers)).json()
    assert len(quizzes) >= 1
    quiz_id = quizzes[0]["id"]

    detail = (await client.get(f"/api/v1/quizzes/{quiz_id}", headers=headers)).json()
    assert detail["question_count"] == 3
    assert "questions" not in detail

    start = await client.post(f"/api/v1/quizzes/{quiz_id}/start", headers=headers)
    assert start.status_code == 201
    attempt = start.json()
    attempt_id = attempt["id"]

    q = (
        await client.get(
            f"/api/v1/quiz-attempts/{attempt_id}/current-question",
            headers=headers,
        )
    ).json()
    assert "is_correct" not in q
    for opt in q["options"]:
        assert "is_correct" not in opt

    # Submit first option (may be wrong) then finish remaining via complete
    ans = await client.post(
        f"/api/v1/quiz-attempts/{attempt_id}/answers",
        headers=headers,
        json={"option_id": q["options"][0]["id"]},
    )
    assert ans.status_code == 200
    assert "is_correct" in ans.json()

    done = await client.post(
        f"/api/v1/quiz-attempts/{attempt_id}/complete",
        headers=headers,
    )
    assert done.status_code == 200
    body = done.json()
    assert body["status"] == "completed"
    assert body["xp_earned"] >= 20

    hist = (await client.get("/api/v1/quiz-attempts/history", headers=headers)).json()
    assert len(hist) >= 1

    # Other user cannot access
    headers2 = await _auth_header(client, "quizapi2@example.com")
    await _complete_profile(client, headers2)
    forbidden = await client.get(
        f"/api/v1/quiz-attempts/{attempt_id}/result",
        headers=headers2,
    )
    assert forbidden.status_code == 403
