"""Study session unit and API tests."""

from io import BytesIO

import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.exceptions import ConflictError
from app.schemas.auth import RegisterRequest
from app.schemas.profile import ProfileUpdateRequest
from app.schemas.study_session import (
    CompleteSessionRequest,
    SessionActivityRequest,
    StartSessionRequest,
)
from app.services.auth import AuthService
from app.services.profile import ProfileService
from app.services.study_session import (
    StudySessionService,
    calculate_session_score,
    calculate_session_xp,
)
from app.services.syllabus import SyllabusService


def test_score_and_xp_helpers() -> None:
    assert calculate_session_score(8, 2) == 80
    assert calculate_session_score(0, 0) == 50
    xp = calculate_session_xp(duration_seconds=600, score=80, correct_count=5)
    assert xp >= 15
    assert xp == 15 + 20 + 16 + 10  # base + duration + score + correct


async def _ready_user(session: AsyncSession, email: str):
    tokens = await AuthService(session).register(
        RegisterRequest(email=email, password="Secret123!", full_name="Quest Student"),
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


@pytest.mark.asyncio
async def test_start_complete_session_awards_xp(db_session: AsyncSession) -> None:
    user, topic_id = await _ready_user(db_session, "session1@example.com")
    service = StudySessionService(db_session)

    started = await service.start(user, StartSessionRequest(topic_id=topic_id))
    assert started.status == "active"
    assert started.xp_earned == 0

    await service.record_activity(
        user,
        started.id,
        SessionActivityRequest(result="correct"),
    )
    await service.record_activity(
        user,
        started.id,
        SessionActivityRequest(result="incorrect"),
    )

    with pytest.raises(ConflictError):
        await service.start(user, StartSessionRequest(topic_id=topic_id))

    result = await service.complete(
        user,
        started.id,
        CompleteSessionRequest(),
    )
    assert result.status == "completed"
    assert result.duration_seconds >= 0
    assert result.correct_count == 1
    assert result.incorrect_count == 1
    assert result.score == 50
    assert result.xp_earned > 0
    assert result.total_xp == result.xp_earned

    profile = await ProfileService(db_session).get_profile(user)
    assert profile.total_xp == result.xp_earned


@pytest.mark.asyncio
async def test_study_session_api(client: AsyncClient) -> None:
    register = await client.post(
        "/api/v1/auth/register",
        json={
            "email": "sessionapi@example.com",
            "password": "Secret123!",
            "full_name": "API Session",
        },
    )
    token = register.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    boards = await client.get("/api/v1/boards", headers=headers)
    classes = await client.get("/api/v1/classes", headers=headers)
    class_7 = next(c for c in classes.json() if c["grade"] == 7)
    await client.post(
        "/api/v1/profile/me/photo",
        headers=headers,
        files={"file": ("a.png", BytesIO(b"\x89PNG\r\n\x1a\nfake"), "image/png")},
    )
    await client.put(
        "/api/v1/profile/me",
        headers=headers,
        json={
            "mobile": "9000011122",
            "board_id": boards.json()[0]["id"],
            "class_id": class_7["id"],
        },
    )

    subjects = await client.get("/api/v1/syllabus/subjects", headers=headers)
    subject_id = subjects.json()[0]["id"]
    detail = await client.get(f"/api/v1/syllabus/subjects/{subject_id}", headers=headers)
    chapter_id = detail.json()["chapters"][0]["id"]
    topics = await client.get(
        f"/api/v1/syllabus/chapters/{chapter_id}/topics",
        headers=headers,
    )
    topic_id = topics.json()["topics"][0]["id"]

    start = await client.post(
        "/api/v1/study-sessions/start",
        headers=headers,
        json={"topic_id": topic_id},
    )
    assert start.status_code == 201
    session_id = start.json()["id"]

    active = await client.get("/api/v1/study-sessions/active", headers=headers)
    assert active.status_code == 200
    assert active.json()["id"] == session_id

    activity = await client.post(
        f"/api/v1/study-sessions/{session_id}/activity",
        headers=headers,
        json={"result": "correct"},
    )
    assert activity.status_code == 200
    assert activity.json()["correct_count"] == 1

    complete = await client.post(
        f"/api/v1/study-sessions/{session_id}/complete",
        headers=headers,
        json={},
    )
    assert complete.status_code == 200
    body = complete.json()
    assert body["status"] == "completed"
    assert body["xp_earned"] > 0
    assert body["total_xp"] >= body["xp_earned"]

    profile = await client.get("/api/v1/profile/me", headers=headers)
    assert profile.json()["total_xp"] == body["total_xp"]
