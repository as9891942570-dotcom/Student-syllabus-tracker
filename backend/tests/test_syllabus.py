"""Syllabus tracking tests."""

from io import BytesIO

import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.auth import RegisterRequest
from app.schemas.profile import ProfileUpdateRequest
from app.schemas.syllabus import TopicProgressUpdate
from app.services.auth import AuthService
from app.services.profile import ProfileService
from app.services.syllabus import SyllabusService


async def _complete_profile(
    session: AsyncSession,
    email: str,
    *,
    grade: int,
    with_stream: bool,
):
    tokens = await AuthService(session).register(
        RegisterRequest(email=email, password="Secret123!", full_name="Syllabus Student"),
    )
    user = await AuthService(session).get_user(tokens.user.id)
    profile_service = ProfileService(session)
    await profile_service.ensure_lookups()
    boards = await profile_service.list_boards()
    classes = await profile_service.list_classes()
    streams = await profile_service.list_streams()
    school_class = next(c for c in classes if c.grade == grade)
    stream = next(s for s in streams if s.code == "SCIENCE_PCM")

    profile = await profile_service.get_or_create_profile(user)
    profile.photo_url = "/media/profiles/demo.jpg"
    await profile_service.profiles.update(profile)

    payload = ProfileUpdateRequest(
        mobile="9876543210",
        board_id=boards[0].id,
        class_id=school_class.id,
        stream_id=stream.id if with_stream else None,
    )
    await profile_service.update_profile(user, payload)
    return tokens, user


@pytest.mark.asyncio
async def test_class_10_subjects_and_topic_toggle(db_session: AsyncSession) -> None:
    _, user = await _complete_profile(
        db_session,
        "syl10@example.com",
        grade=10,
        with_stream=False,
    )
    service = SyllabusService(db_session)
    subjects = await service.list_subjects(user)
    assert len(subjects) == 4
    assert all(s.completion_percentage == 0 for s in subjects)

    detail = await service.get_subject_chapters(user, subjects[0].id)
    assert detail.chapter_count >= 1
    chapter = await service.get_chapter_topics(user, detail.chapters[0].id)
    assert len(chapter.topics) >= 1

    topic = chapter.topics[0]
    updated = await service.set_topic_progress(
        user,
        topic.id,
        TopicProgressUpdate(is_completed=True),
    )
    assert updated.is_completed is True

    subjects_after = await service.list_subjects(user)
    assert subjects_after[0].completed_topic_count == 1
    assert subjects_after[0].completion_percentage > 0

    completion = await service.get_completion(user)
    assert completion.completed_topics == 1
    assert completion.overall_completion_percentage > 0


@pytest.mark.asyncio
async def test_class_11_uses_stream_subjects(db_session: AsyncSession) -> None:
    _, user = await _complete_profile(
        db_session,
        "syl11@example.com",
        grade=11,
        with_stream=True,
    )
    service = SyllabusService(db_session)
    subjects = await service.list_subjects(user)
    codes = {s.code for s in subjects}
    assert "PHY" in codes
    assert "MATH" in codes
    assert "SST" not in codes


@pytest.mark.asyncio
async def test_syllabus_api_flow(client: AsyncClient) -> None:
    register = await client.post(
        "/api/v1/auth/register",
        json={
            "email": "sylapi@example.com",
            "password": "Secret123!",
            "full_name": "API Syllabus",
        },
    )
    token = register.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    boards = await client.get("/api/v1/boards", headers=headers)
    classes = await client.get("/api/v1/classes", headers=headers)
    class_9 = next(c for c in classes.json() if c["grade"] == 9)

    await client.post(
        "/api/v1/profile/me/photo",
        headers=headers,
        files={"file": ("a.png", BytesIO(b"\x89PNG\r\n\x1a\nfake"), "image/png")},
    )
    await client.put(
        "/api/v1/profile/me",
        headers=headers,
        json={
            "mobile": "9123456780",
            "board_id": boards.json()[0]["id"],
            "class_id": class_9["id"],
        },
    )

    subjects = await client.get("/api/v1/syllabus/subjects", headers=headers)
    assert subjects.status_code == 200
    assert len(subjects.json()) == 4

    subject_id = subjects.json()[0]["id"]
    detail = await client.get(f"/api/v1/syllabus/subjects/{subject_id}", headers=headers)
    assert detail.status_code == 200
    chapter_id = detail.json()["chapters"][0]["id"]

    topics = await client.get(
        f"/api/v1/syllabus/chapters/{chapter_id}/topics",
        headers=headers,
    )
    assert topics.status_code == 200
    topic_id = topics.json()["topics"][0]["id"]

    progress = await client.patch(
        f"/api/v1/syllabus/topics/{topic_id}/progress",
        headers=headers,
        json={"is_completed": True},
    )
    assert progress.status_code == 403
    assert topics.json()["topics"][0]["is_completed"] is False
    assert topics.json()["topics"][0]["is_locked"] is False
    if len(topics.json()["topics"]) > 1:
        assert topics.json()["topics"][1]["is_locked"] is True

    again = await client.get(
        f"/api/v1/syllabus/chapters/{chapter_id}/topics",
        headers=headers,
    )
    assert again.json()["topics"][0]["is_completed"] is False
    if len(again.json()["topics"]) > 1:
        assert again.json()["topics"][1]["is_locked"] is True

    completion = await client.get("/api/v1/syllabus/completion", headers=headers)
    assert completion.status_code == 200
    assert completion.json()["completed_topics"] == 0

    structure = await client.get("/api/v1/syllabus/structure", headers=headers)
    assert structure.status_code == 200
    assert structure.json()["total_topics"] > 0
