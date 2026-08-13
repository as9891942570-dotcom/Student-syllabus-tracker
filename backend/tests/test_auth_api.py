"""API-level authentication tests."""

import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_register_login_me_flow(client: AsyncClient) -> None:
    register = await client.post(
        "/api/v1/auth/register",
        json={
            "email": "api@example.com",
            "password": "Secret123!",
            "full_name": "API Student",
        },
    )
    assert register.status_code == 201
    body = register.json()
    assert body["token_type"] == "bearer"
    access = body["access_token"]

    me = await client.get(
        "/api/v1/auth/me",
        headers={"Authorization": f"Bearer {access}"},
    )
    assert me.status_code == 200
    assert me.json()["email"] == "api@example.com"

    login = await client.post(
        "/api/v1/auth/login",
        json={"email": "api@example.com", "password": "Secret123!"},
    )
    assert login.status_code == 200
    assert login.json()["user"]["full_name"] == "API Student"


@pytest.mark.asyncio
async def test_refresh_and_logout_endpoints(client: AsyncClient) -> None:
    register = await client.post(
        "/api/v1/auth/register",
        json={
            "email": "rotate@example.com",
            "password": "Secret123!",
            "full_name": "Rotate Student",
        },
    )
    refresh_token = register.json()["refresh_token"]

    refreshed = await client.post(
        "/api/v1/auth/refresh",
        json={"refresh_token": refresh_token},
    )
    assert refreshed.status_code == 200
    new_refresh = refreshed.json()["refresh_token"]

    logout = await client.post(
        "/api/v1/auth/logout",
        json={"refresh_token": new_refresh},
    )
    assert logout.status_code == 200

    reuse = await client.post(
        "/api/v1/auth/refresh",
        json={"refresh_token": new_refresh},
    )
    assert reuse.status_code == 401


@pytest.mark.asyncio
async def test_me_requires_auth(client: AsyncClient) -> None:
    response = await client.get("/api/v1/auth/me")
    assert response.status_code == 401


@pytest.mark.asyncio
async def test_forgot_password_stub(client: AsyncClient) -> None:
    response = await client.post(
        "/api/v1/auth/forgot-password",
        json={"email": "anyone@example.com"},
    )
    assert response.status_code == 200
    assert response.json()["code"] == "forgot_password_stub"


@pytest.mark.asyncio
async def test_register_validation_error(client: AsyncClient) -> None:
    response = await client.post(
        "/api/v1/auth/register",
        json={"email": "bad", "password": "short", "full_name": "A"},
    )
    assert response.status_code == 422
