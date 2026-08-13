"""Profile service and API tests."""

from io import BytesIO

import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.exceptions import ValidationAppError
from app.schemas.auth import RegisterRequest
from app.schemas.profile import ProfileUpdateRequest
from app.services.auth import AuthService
from app.services.profile import ProfileService


async def _register_user(session: AsyncSession, email: str):
    tokens = await AuthService(session).register(
        RegisterRequest(
            email=email,
            password="Secret123!",
            full_name="Profile Student",
        ),
    )
    user = await AuthService(session).get_user(tokens.user.id)
    return tokens, user


@pytest.mark.asyncio
async def test_completion_class_10_without_stream(db_session: AsyncSession) -> None:
    _, user = await _register_user(db_session, "class10@example.com")
    service = ProfileService(db_session)
    await service.ensure_lookups()
    boards = await service.list_boards()
    classes = await service.list_classes()
    class_10 = next(c for c in classes if c.grade == 10)

    # Upload-less completion path: set fields then mark photo manually via service internals
    profile = await service.get_or_create_profile(user)
    profile.photo_url = "/media/profiles/demo.jpg"
    await service.profiles.update(profile)

    result = await service.update_profile(
        user,
        ProfileUpdateRequest(
            mobile="9876543210",
            board_id=boards[0].id,
            class_id=class_10.id,
        ),
    )
    assert result.stream is None
    assert result.is_complete is True
    assert result.completion_percentage == 100


@pytest.mark.asyncio
async def test_class_11_requires_stream(db_session: AsyncSession) -> None:
    _, user = await _register_user(db_session, "class11@example.com")
    service = ProfileService(db_session)
    await service.ensure_lookups()
    boards = await service.list_boards()
    classes = await service.list_classes()
    streams = await service.list_streams()
    class_11 = next(c for c in classes if c.grade == 11)

    with pytest.raises(ValidationAppError):
        await service.update_profile(
            user,
            ProfileUpdateRequest(
                mobile="9876543210",
                board_id=boards[0].id,
                class_id=class_11.id,
            ),
        )

    result = await service.update_profile(
        user,
        ProfileUpdateRequest(
            mobile="9876543210",
            board_id=boards[0].id,
            class_id=class_11.id,
            stream_id=streams[0].id,
        ),
    )
    assert result.stream is not None
    assert "stream" not in result.missing_fields


@pytest.mark.asyncio
async def test_class_6_rejects_stream(db_session: AsyncSession) -> None:
    _, user = await _register_user(db_session, "class6@example.com")
    service = ProfileService(db_session)
    await service.ensure_lookups()
    classes = await service.list_classes()
    streams = await service.list_streams()
    class_6 = next(c for c in classes if c.grade == 6)

    with pytest.raises(ValidationAppError):
        await service.update_profile(
            user,
            ProfileUpdateRequest(
                class_id=class_6.id,
                stream_id=streams[0].id,
            ),
        )


@pytest.mark.asyncio
async def test_profile_api_flow(client: AsyncClient) -> None:
    register = await client.post(
        "/api/v1/auth/register",
        json={
            "email": "profileapi@example.com",
            "password": "Secret123!",
            "full_name": "API Profile",
        },
    )
    assert register.status_code == 201
    token = register.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    me = await client.get("/api/v1/profile/me", headers=headers)
    assert me.status_code == 200
    assert me.json()["is_complete"] is False
    assert me.json()["completion_percentage"] < 100

    boards = await client.get("/api/v1/boards", headers=headers)
    classes = await client.get("/api/v1/classes", headers=headers)
    assert boards.status_code == 200
    assert len(boards.json()) == 3
    class_8 = next(c for c in classes.json() if c["grade"] == 8)

    photo = await client.post(
        "/api/v1/profile/me/photo",
        headers=headers,
        files={"file": ("avatar.png", BytesIO(b"\x89PNG\r\n\x1a\nfake"), "image/png")},
    )
    assert photo.status_code == 200
    assert photo.json()["photo_url"]

    updated = await client.put(
        "/api/v1/profile/me",
        headers=headers,
        json={
            "mobile": "9988776655",
            "board_id": boards.json()[0]["id"],
            "class_id": class_8["id"],
        },
    )
    assert updated.status_code == 200
    body = updated.json()
    assert body["is_complete"] is True
    assert body["completion_percentage"] == 100
    assert body["school_class"]["grade"] == 8
    assert body["stream"] is None
