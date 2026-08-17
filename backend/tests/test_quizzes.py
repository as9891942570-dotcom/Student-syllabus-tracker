"""Quiz system unit and API tests (topic-specific, session-free)."""

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
    TOPIC_COMPLETE_PERCENTAGE,
    QuizService,
    calculate_quiz_percentage,
    calculate_quiz_score,
    calculate_quiz_xp,
)
from app.services.quiz_seed import (
    LEGACY_PROMPT_FRAGMENTS,
    MAX_QUESTIONS_PER_TOPIC,
    contains_legacy_prompt,
    questions_for_topic,
)
from app.services.syllabus import SyllabusService
from app.services.topic_quiz_builder import is_meta_question, questions_match_topic, validate_question_bank


def test_score_percentage_and_xp_helpers() -> None:
    assert calculate_quiz_percentage(correct=3, total=3) == 100
    assert calculate_quiz_percentage(correct=1, total=4) == 25
    assert calculate_quiz_percentage(correct=0, total=0) == 0
    assert calculate_quiz_percentage(correct=8, total=10) == 80
    assert calculate_quiz_percentage(correct=6, total=10) == 60
    assert calculate_quiz_percentage(correct=5, total=10) == 50
    assert calculate_quiz_score(correct=2, total=4) == 50
    assert calculate_quiz_xp(percentage=30, correct_count=2) == 20 + 9 + 4
    assert calculate_quiz_xp(percentage=100, correct_count=3) == 20 + 30 + 6 + 15
    assert calculate_quiz_xp(percentage=100, correct_count=20) == 20 + 30 + 40 + 15
    assert TOPIC_COMPLETE_PERCENTAGE == 60


def test_topic_question_bank_is_topic_specific_and_capped() -> None:
    bank = questions_for_topic(
        "Coulomb's law",
        chapter_title="Electric Charges and Fields",
        subject_code="PHY",
        grade=12,
    )
    assert 1 <= len(bank) <= MAX_QUESTIONS_PER_TOPIC
    assert validate_question_bank("Coulomb's law", bank) == []
    for prompt, options in bank:
        assert not contains_legacy_prompt(prompt)
        assert not is_meta_question(prompt, options)
        assert sum(1 for _, ok in options if ok) == 1
        assert "while studying" not in prompt.lower()
        assert "definitions, relations, and applications" not in prompt.lower()


async def _ready_user(
    session: AsyncSession,
    email: str,
    *,
    grade: int = 8,
    stream_code: str | None = None,
):
    tokens = await AuthService(session).register(
        RegisterRequest(email=email, password="Secret123!", full_name="Quiz Student"),
    )
    user = await AuthService(session).get_user(tokens.user.id)
    profile_service = ProfileService(session)
    await profile_service.ensure_lookups()
    boards = await profile_service.list_boards()
    classes = await profile_service.list_classes()
    class_row = next(c for c in classes if c.grade == grade)
    profile = await profile_service.get_or_create_profile(user)
    profile.photo_url = "/media/profiles/demo.jpg"
    await profile_service.profiles.update(profile)
    update = {
        "mobile": "9876501234",
        "board_id": boards[0].id,
        "class_id": class_row.id,
    }
    if stream_code:
        streams = await profile_service.list_streams()
        update["stream_id"] = next(s.id for s in streams if s.code == stream_code)
    await profile_service.update_profile(user, ProfileUpdateRequest(**update))
    subjects = await SyllabusService(session).list_subjects(user)
    if grade >= 11:
        subject = next(s for s in subjects if s.code == "PHY")
    else:
        subject = subjects[0]
    detail = await SyllabusService(session).get_subject_chapters(user, subject.id)
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
    ordered = chapter.topics[:2]
    assert len(ordered) >= 2
    prompt_sets: list[set[str]] = []

    for topic in ordered:
        expected_prompts = [
            prompt
            for prompt, _ in questions_for_topic(
                topic.title,
                chapter_title=chapter.title,
                subject_code="HIST",
                grade=11,
            )
        ]
        assert 1 <= len(expected_prompts) <= MAX_QUESTIONS_PER_TOPIC

        quizzes = await service.list_for_topic(user, topic.id)
        assert quizzes[0].question_count == len(expected_prompts)

        attempt = await service.start(user, quizzes[0].id)
        assert attempt.total_questions == len(expected_prompts)

        from app.repositories.quiz import QuizRepository

        loaded = await QuizRepository(db_session).get_with_questions(quizzes[0].id)
        assert loaded is not None
        prompts = [q.prompt for q in sorted(loaded.questions, key=lambda item: item.sort_order)]
        assert prompts == expected_prompts
        prompt_sets.append(set(prompts))
        for prompt in prompts:
            assert not contains_legacy_prompt(prompt)
            for fragment in LEGACY_PROMPT_FRAGMENTS:
                assert fragment.lower() not in prompt.lower()

        for question in loaded.questions:
            correct = [o for o in question.options if o.is_correct]
            assert len(question.options) >= 2
            assert len(correct) == 1

        for _ in range(attempt.total_questions):
            question = await service.current_question(user, attempt.id)
            orm_q = next(q for q in loaded.questions if q.id == question.id)
            correct_opt = next(o for o in orm_q.options if o.is_correct)
            await service.submit_answer(
                user,
                attempt.id,
                SubmitAnswerRequest(option_id=correct_opt.id),
            )
            if question.question_number < question.total_questions:
                await service.next_question(user, attempt.id)
        result = await service.complete(user, attempt.id)
        assert result.topic_completed is True

    assert prompt_sets[0] != prompt_sets[1]


@pytest.mark.asyncio
async def test_seeded_quiz_has_topic_questions_immediately(db_session: AsyncSession) -> None:
    user, topic_id = await _ready_user(db_session, "quizseed@example.com")
    service = QuizService(db_session)

    quizzes = await service.list_for_topic(user, topic_id)
    assert len(quizzes) >= 1
    assert 1 <= quizzes[0].question_count <= MAX_QUESTIONS_PER_TOPIC

    detail = await service.get_quiz(user, quizzes[0].id)
    assert detail.question_count == quizzes[0].question_count

    attempt = await service.start(user, quizzes[0].id)
    assert attempt.total_questions == quizzes[0].question_count
    assert attempt.status == "active"
    assert attempt.seconds_remaining > 0

    question = await service.current_question(user, attempt.id)
    assert question.question_number == 1
    assert question.total_questions == quizzes[0].question_count
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
    assert 1 <= detail.question_count <= MAX_QUESTIONS_PER_TOPIC

    attempt = await service.start(user, empty.id)
    assert attempt.total_questions == detail.question_count


@pytest.mark.asyncio
async def test_list_start_answer_complete_quiz(db_session: AsyncSession) -> None:
    user, topic_id = await _ready_user(db_session, "quiz1@example.com")
    service = QuizService(db_session)

    quizzes = await service.list_for_topic(user, topic_id)
    quiz = await service.get_quiz(user, quizzes[0].id)
    assert 1 <= quiz.question_count <= MAX_QUESTIONS_PER_TOPIC
    assert quiz.topic_id == topic_id

    attempt = await service.start(user, quiz.id)
    assert attempt.status == "active"
    assert attempt.total_questions == quiz.question_count

    orm_quiz = await service.quizzes.get_with_questions(quiz.id)
    assert orm_quiz is not None

    wrong_done = False
    for index in range(attempt.total_questions):
        question = await service.current_question(user, attempt.id)
        orm_q = next(q for q in orm_quiz.questions if q.id == question.id)
        if index == 1 and not wrong_done and attempt.total_questions > 1:
            option = next(o for o in orm_q.options if not o.is_correct)
            wrong_done = True
        else:
            option = next(o for o in orm_q.options if o.is_correct)
        answer = await service.submit_answer(
            user,
            attempt.id,
            SubmitAnswerRequest(option_id=option.id),
        )
        if index == 1 and wrong_done:
            assert answer.is_correct is False
            assert answer.correct_option_id != option.id
        if index == 0:
            assert answer.is_correct is True
            assert answer.correct_option_id == option.id
        if question.question_number < question.total_questions:
            await service.next_question(user, attempt.id)

    result = await service.complete(user, attempt.id)
    assert result.status == "completed"
    assert result.total_questions == quiz.question_count
    expected_incorrect = 1 if quiz.question_count > 1 else 0
    expected_correct = quiz.question_count - expected_incorrect
    assert result.correct_count == expected_correct
    assert result.incorrect_count == expected_incorrect
    assert result.percentage == calculate_quiz_percentage(
        correct=expected_correct,
        total=quiz.question_count,
    )
    assert result.topic_completed is (result.percentage >= 60)
    assert result.passed is (result.percentage >= 60)
    assert result.correct_answers == expected_correct
    assert result.wrong_answers == expected_incorrect
    history = await service.history(user)
    assert len(history) == 1
    assert history[0].passed is result.passed
    assert history[0].correct_count == expected_correct


async def _complete_with_correct_count(service: QuizService, user, quiz_id, *, correct_count: int):
    attempt = await service.start(user, quiz_id)
    loaded = await service.quizzes.get_with_questions(quiz_id)
    assert loaded is not None
    total = attempt.total_questions
    correct_count = max(0, min(correct_count, total))
    for index in range(total):
        question = await service.current_question(user, attempt.id)
        orm_q = next(q for q in loaded.questions if q.id == question.id)
        if index < correct_count:
            option = next(o for o in orm_q.options if o.is_correct)
        else:
            option = next(o for o in orm_q.options if not o.is_correct)
        await service.submit_answer(
            user, attempt.id, SubmitAnswerRequest(option_id=option.id),
        )
        if question.question_number < question.total_questions:
            await service.next_question(user, attempt.id)
    return await service.complete(user, attempt.id)


@pytest.mark.asyncio
async def test_quiz_complete_payload_shows_8_of_10_pass(db_session: AsyncSession) -> None:
    user, topic_id = await _ready_user(
        db_session,
        "score80pass@example.com",
        grade=11,
        stream_code="SCIENCE_PCM",
    )
    service = QuizService(db_session)
    quiz = (await service.list_for_topic(user, topic_id))[0]
    detail = await service.get_quiz(user, quiz.id)
    total = detail.question_count
    correct_needed = 8 if total == 10 else next(
        k
        for k in range(total + 1)
        if calculate_quiz_percentage(correct=k, total=total) == 80
    )
    expected_wrong = total - correct_needed

    profile_before = await service.profiles.get_by_user_id(user.id)
    assert profile_before is not None
    xp_before = profile_before.total_xp or 0
    coins_before = profile_before.total_coins or 0

    result = await _complete_with_correct_count(
        service, user, quiz.id, correct_count=correct_needed,
    )
    assert result.correct_count == correct_needed
    assert result.incorrect_count == expected_wrong
    assert result.correct_answers == correct_needed
    assert result.wrong_answers == expected_wrong
    assert result.total_questions == total
    assert result.percentage == 80
    assert result.passed is True
    assert result.topic_completed is True
    assert result.next_topic_unlocked is True
    assert result.xp_awarded is True
    assert result.xp_earned > 0
    assert result.coins_awarded is True
    assert result.coins_earned > 0
    assert result.total_xp > xp_before
    assert result.total_coins > coins_before

    refetch = await service.get_result(user, result.id)
    assert refetch.percentage == 80
    assert refetch.passed is True
    assert refetch.correct_count == correct_needed
    assert refetch.total_xp == result.total_xp
    assert refetch.total_coins == result.total_coins

    retry = await _complete_with_correct_count(
        service, user, quiz.id, correct_count=correct_needed,
    )
    assert retry.passed is True
    assert retry.xp_awarded is False
    assert retry.xp_earned == 0
    assert retry.coins_awarded is False
    assert retry.total_xp == result.total_xp
    assert retry.total_coins == result.total_coins


@pytest.mark.asyncio
async def test_quiz_complete_payload_shows_5_of_10_fail(db_session: AsyncSession) -> None:
    user, topic_id = await _ready_user(
        db_session,
        "score50fail@example.com",
        grade=11,
        stream_code="SCIENCE_PCM",
    )
    service = QuizService(db_session)
    quiz = (await service.list_for_topic(user, topic_id))[0]
    detail = await service.get_quiz(user, quiz.id)
    total = detail.question_count
    correct_needed = 5 if total == 10 else next(
        k
        for k in range(total + 1)
        if calculate_quiz_percentage(correct=k, total=total) == 50
    )
    expected_wrong = total - correct_needed

    profile_before = await service.profiles.get_by_user_id(user.id)
    assert profile_before is not None
    xp_before = profile_before.total_xp or 0
    coins_before = profile_before.total_coins or 0

    result = await _complete_with_correct_count(
        service, user, quiz.id, correct_count=correct_needed,
    )
    assert result.correct_count == correct_needed
    assert result.incorrect_count == expected_wrong
    assert result.percentage == 50
    assert result.passed is False
    assert result.topic_completed is False
    assert result.next_topic_unlocked is False
    assert result.xp_awarded is False
    assert result.xp_earned == 0
    assert result.coins_awarded is False
    assert result.coins_earned == 0
    assert result.total_xp == xp_before
    assert result.total_coins == coins_before

    syllabus = SyllabusService(db_session)
    subjects = await syllabus.list_subjects(user)
    physics = next(s for s in subjects if s.code == "PHY")
    chapters = await syllabus.get_subject_chapters(user, physics.id)
    chapter = await syllabus.get_chapter_topics(user, chapters.chapters[0].id)
    assert chapter.topics[0].is_completed is False
    if len(chapter.topics) > 1:
        assert chapter.topics[1].is_locked is True

    refetch = await service.get_result(user, result.id)
    assert refetch.passed is False
    assert refetch.percentage == 50
    assert refetch.total_xp == xp_before


@pytest.mark.asyncio
async def test_quiz_returns_only_selected_topic_questions(db_session: AsyncSession) -> None:
    tokens = await AuthService(db_session).register(
        RegisterRequest(
            email="quiztopicisolation@example.com",
            password="Secret123!",
            full_name="Topic Isolation",
        ),
    )
    user = await AuthService(db_session).get_user(tokens.user.id)
    profile_service = ProfileService(db_session)
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
            mobile="9876504444",
            board_id=boards[0].id,
            class_id=class_12.id,
            stream_id=pcm.id,
        ),
    )
    subjects = await SyllabusService(db_session).list_subjects(user)
    physics = next(s for s in subjects if s.code == "PHY")
    detail = await SyllabusService(db_session).get_subject_chapters(user, physics.id)
    chapter = await SyllabusService(db_session).get_chapter_topics(user, detail.chapters[0].id)
    topic_a = chapter.topics[0]
    topic_b = next(t for t in chapter.topics if t.title == "Coulomb's law")

    service = QuizService(db_session)
    quiz_a = (await service.list_for_topic(user, topic_a.id))[0]
    attempt = await service.start(user, quiz_a.id)
    loaded = await service.quizzes.get_with_questions(quiz_a.id)
    assert loaded is not None
    for _ in range(attempt.total_questions):
        question = await service.current_question(user, attempt.id)
        orm_q = next(q for q in loaded.questions if q.id == question.id)
        correct = next(o for o in orm_q.options if o.is_correct)
        await service.submit_answer(
            user,
            attempt.id,
            SubmitAnswerRequest(option_id=correct.id),
        )
        if question.question_number < question.total_questions:
            await service.next_question(user, attempt.id)
    await service.complete(user, attempt.id)

    quiz_b = (await service.list_for_topic(user, topic_b.id))[0]
    loaded_a = await service.quizzes.get_with_questions(quiz_a.id)
    loaded_b = await service.quizzes.get_with_questions(quiz_b.id)
    assert loaded_a is not None and loaded_b is not None
    prompts_a = {q.prompt for q in loaded_a.questions}
    prompts_b = {q.prompt for q in loaded_b.questions}
    assert prompts_a != prompts_b
    assert all(questions_match_topic(p, topic_a.title) for p in prompts_a)
    assert all(questions_match_topic(p, topic_b.title) for p in prompts_b)
    assert all(not contains_legacy_prompt(p) for p in prompts_a | prompts_b)
    assert all(not is_meta_question(p) for p in prompts_a | prompts_b)
    assert len(loaded_a.questions) <= MAX_QUESTIONS_PER_TOPIC
    assert len(loaded_b.questions) <= MAX_QUESTIONS_PER_TOPIC


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
    assert result.percentage < 60
    assert result.xp_earned == 0
    assert result.coins_earned == 0
    assert result.topic_completed is False


@pytest.mark.asyncio
async def test_quiz_api_auth_and_flow(client: AsyncClient) -> None:
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
    assert 1 <= detail["question_count"] <= MAX_QUESTIONS_PER_TOPIC
    assert "questions" not in detail

    # Session APIs must be gone.
    gone = await client.post(
        "/api/v1/study-sessions/start",
        headers=headers,
        json={"topic_id": topic_id},
    )
    assert gone.status_code == 404

    start = await client.post(f"/api/v1/quizzes/{quiz_id}/start", headers=headers)
    assert start.status_code == 201
    attempt_id = start.json()["id"]

    q = (
        await client.get(
            f"/api/v1/quiz-attempts/{attempt_id}/current-question",
            headers=headers,
        )
    ).json()
    assert "is_correct" not in q
    assert q.get("correct_option_id") in (None, "")

    ans = await client.post(
        f"/api/v1/quiz-attempts/{attempt_id}/answers",
        headers=headers,
        json={"option_id": q["options"][0]["id"]},
    )
    assert ans.status_code == 200
    assert "correct_option_id" in ans.json()
    assert ans.json()["is_correct"] in {True, False}

    after = (
        await client.get(
            f"/api/v1/quiz-attempts/{attempt_id}/current-question",
            headers=headers,
        )
    ).json()
    assert after["already_answered"] is True
    assert after["correct_option_id"] == ans.json()["correct_option_id"]

    done = await client.post(
        f"/api/v1/quiz-attempts/{attempt_id}/complete",
        headers=headers,
    )
    assert done.status_code == 200
    assert done.json()["status"] == "completed"
    if done.json()["percentage"] < 60:
        assert done.json()["xp_earned"] == 0
        assert done.json()["topic_completed"] is False
        assert done.json().get("coins_earned", 0) == 0
    else:
        assert done.json()["xp_earned"] >= 20
        assert done.json()["topic_completed"] is True

    hist = (await client.get("/api/v1/quiz-attempts/history", headers=headers)).json()
    assert len(hist) >= 1

    headers2 = await _auth_header(client, "quizapi2@example.com")
    await _complete_profile(client, headers2)
    forbidden = await client.get(
        f"/api/v1/quiz-attempts/{attempt_id}/result",
        headers=headers2,
    )
    assert forbidden.status_code == 403


@pytest.mark.asyncio
async def test_no_study_session_openapi_paths(client: AsyncClient) -> None:
    openapi = (await client.get("/openapi.json")).json()
    paths = openapi.get("paths", {})
    assert not any("study-session" in path for path in paths)


@pytest.mark.asyncio
async def test_class_11_measurement_of_length_quiz_unlocks_only_mass(
    db_session: AsyncSession,
) -> None:
    tokens = await AuthService(db_session).register(
        RegisterRequest(
            email="c11length@example.com",
            password="Secret123!",
            full_name="Class 11 Physics",
        ),
    )
    user = await AuthService(db_session).get_user(tokens.user.id)
    profile_service = ProfileService(db_session)
    await profile_service.ensure_lookups()
    boards = await profile_service.list_boards()
    classes = await profile_service.list_classes()
    streams = await profile_service.list_streams()
    class_11 = next(c for c in classes if c.grade == 11)
    pcm = next(s for s in streams if s.code == "SCIENCE_PCM")
    profile = await profile_service.get_or_create_profile(user)
    profile.photo_url = "/media/profiles/demo.jpg"
    await profile_service.profiles.update(profile)
    await profile_service.update_profile(
        user,
        ProfileUpdateRequest(
            mobile="9876501111",
            board_id=boards[0].id,
            class_id=class_11.id,
            stream_id=pcm.id,
        ),
    )

    subjects = await SyllabusService(db_session).list_subjects(user)
    physics = next(s for s in subjects if s.code == "PHY")
    detail = await SyllabusService(db_session).get_subject_chapters(user, physics.id)
    units = next(c for c in detail.chapters if c.title == "Units and Measurements")
    chapter = await SyllabusService(db_session).get_chapter_topics(user, units.id)
    si, length, mass, time = chapter.topics[0], chapter.topics[1], chapter.topics[2], chapter.topics[3]
    assert si.title == "The international system of units"
    assert length.title == "Measurement of length"
    assert mass.title == "Measurement of mass"
    assert time.title == "Measurement of time"
    assert length.is_locked is True
    assert mass.is_locked is True
    assert time.is_locked is True

    service = QuizService(db_session)

    # Completing the first topic must not create a quiz for later topics.
    si_quizzes = await service.list_for_topic(user, si.id)
    assert si_quizzes
    await _perfect_quiz(service, user, si_quizzes[0].id)

    chapter = await SyllabusService(db_session).get_chapter_topics(user, units.id)
    assert chapter.topics[0].is_completed is True
    assert chapter.topics[1].is_current is True
    assert chapter.topics[1].is_locked is False
    assert chapter.topics[2].is_locked is True
    assert chapter.topics[3].is_locked is True

    length_quizzes = await service.list_for_topic(user, length.id)
    assert length_quizzes, "Current topic Measurement of length must have a Start Quiz quiz"
    loaded = await service.quizzes.get_with_questions(length_quizzes[0].id)
    assert loaded is not None
    assert 1 <= len(loaded.questions) <= MAX_QUESTIONS_PER_TOPIC
    joined = " ".join(q.prompt for q in loaded.questions).lower()
    assert "coulomb" not in joined
    assert any(
        w in joined
        for w in ("parallax", "parsec", "astronomical", "light year", "vernier", "fermi")
    )

    xp_before = (await profile_service.get_profile(user)).total_xp
    coins_before = (await profile_service.get_profile(user)).total_coins
    result = await _perfect_quiz(service, user, length_quizzes[0].id)
    assert result.percentage >= 60
    assert result.topic_completed is True
    assert result.xp_awarded is True
    assert result.xp_earned > 0
    assert result.coins_awarded is True
    assert result.next_topic_unlocked is True
    assert result.next_topic_id == mass.id
    assert result.next_topic_title == "Measurement of mass"

    chapter = await SyllabusService(db_session).get_chapter_topics(user, units.id)
    assert chapter.topics[1].is_completed is True
    assert chapter.topics[2].is_locked is False
    assert chapter.topics[2].is_current is True
    assert chapter.topics[3].is_locked is True

    profile = await profile_service.get_profile(user)
    assert profile.total_xp > xp_before
    assert profile.total_coins > coins_before

    retry = await _perfect_quiz(service, user, length_quizzes[0].id)
    assert retry.xp_awarded is False
    assert retry.xp_earned == 0
    assert retry.total_xp == profile.total_xp

    # Fail the next current topic: Measurement of time must stay locked.
    mass_quizzes = await service.list_for_topic(user, mass.id)
    fail = await _fail_quiz(service, user, mass_quizzes[0].id)
    assert fail.percentage < 60
    assert fail.topic_completed is False
    chapter = await SyllabusService(db_session).get_chapter_topics(user, units.id)
    assert chapter.topics[2].is_completed is False
    assert chapter.topics[3].is_locked is True


async def _perfect_quiz(service: QuizService, user, quiz_id):
    attempt = await service.start(user, quiz_id)
    loaded = await service.quizzes.get_with_questions(quiz_id)
    assert loaded is not None
    for _ in range(attempt.total_questions):
        question = await service.current_question(user, attempt.id)
        orm_q = next(q for q in loaded.questions if q.id == question.id)
        correct = next(o for o in orm_q.options if o.is_correct)
        await service.submit_answer(user, attempt.id, SubmitAnswerRequest(option_id=correct.id))
        if question.question_number < question.total_questions:
            await service.next_question(user, attempt.id)
    return await service.complete(user, attempt.id)


async def _fail_quiz(service: QuizService, user, quiz_id):
    attempt = await service.start(user, quiz_id)
    loaded = await service.quizzes.get_with_questions(quiz_id)
    assert loaded is not None
    for _ in range(attempt.total_questions):
        question = await service.current_question(user, attempt.id)
        orm_q = next(q for q in loaded.questions if q.id == question.id)
        wrong = next(o for o in orm_q.options if not o.is_correct)
        await service.submit_answer(user, attempt.id, SubmitAnswerRequest(option_id=wrong.id))
        if question.question_number < question.total_questions:
            await service.next_question(user, attempt.id)
    return await service.complete(user, attempt.id)
