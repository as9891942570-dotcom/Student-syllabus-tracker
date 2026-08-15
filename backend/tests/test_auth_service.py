"""Unit tests for auth security helpers and AuthService."""

import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.exceptions import ConflictError, UnauthorizedError
from app.core.security import (
    create_access_token,
    create_refresh_token,
    decode_token,
    hash_password,
    verify_password,
)
from app.schemas.auth import LoginRequest, RegisterRequest
from app.services.auth import AuthService
from app.utils.tokens import hash_token


def test_password_hash_and_verify() -> None:
    hashed = hash_password("Secret123!")
    assert hashed != "Secret123!"
    assert verify_password("Secret123!", hashed)
    assert not verify_password("wrong", hashed)


def test_access_and_refresh_token_claims() -> None:
    access = create_access_token("user-1")
    refresh = create_refresh_token("user-1")
    access_claims = decode_token(access)
    refresh_claims = decode_token(refresh)
    assert access_claims["sub"] == "user-1"
    assert access_claims["type"] == "access"
    assert refresh_claims["type"] == "refresh"


def test_hash_token_stable() -> None:
    assert hash_token("abc") == hash_token("abc")
    assert hash_token("abc") != hash_token("abcd")


@pytest.mark.asyncio
async def test_register_and_login(db_session: AsyncSession) -> None:
    service = AuthService(db_session)
    tokens = await service.register(
        RegisterRequest(
            email="student@example.com",
            password="Secret123!",
            full_name="Ankit Student",
        ),
    )
    assert tokens.user.email == "student@example.com"
    assert tokens.access_token
    assert tokens.refresh_token

    login_tokens = await service.login(
        LoginRequest(email="student@example.com", password="Secret123!"),
    )
    assert login_tokens.user.id == tokens.user.id


@pytest.mark.asyncio
async def test_register_same_email_different_password(db_session: AsyncSession) -> None:
    service = AuthService(db_session)
    first = await service.register(
        RegisterRequest(
            email="dup@example.com",
            password="Secret123!",
            full_name="Account A",
        ),
    )
    second = await service.register(
        RegisterRequest(
            email="dup@example.com",
            password="Secret456!",
            full_name="Account B",
        ),
    )
    assert first.user.id != second.user.id
    assert first.user.email == second.user.email

    with pytest.raises(ConflictError):
        await service.register(
            RegisterRequest(
                email="dup@example.com",
                password="Secret123!",
                full_name="Account A again",
            ),
        )

    login_a = await service.login(
        LoginRequest(email="dup@example.com", password="Secret123!"),
    )
    login_b = await service.login(
        LoginRequest(email="dup@example.com", password="Secret456!"),
    )
    assert login_a.user.id == first.user.id
    assert login_b.user.id == second.user.id

    by_id = await service.login(
        LoginRequest(user_id=first.user.id, password="Secret123!"),
    )
    assert by_id.user.id == first.user.id

    with pytest.raises(UnauthorizedError):
        await service.login(
            LoginRequest(user_id=first.user.id, password="Secret456!"),
        )


@pytest.mark.asyncio
async def test_login_invalid_password(db_session: AsyncSession) -> None:
    service = AuthService(db_session)
    await service.register(
        RegisterRequest(
            email="badpass@example.com",
            password="Secret123!",
            full_name="Bad Pass",
        ),
    )
    with pytest.raises(UnauthorizedError):
        await service.login(
            LoginRequest(email="badpass@example.com", password="nope"),
        )


@pytest.mark.asyncio
async def test_refresh_rotates_token(db_session: AsyncSession) -> None:
    service = AuthService(db_session)
    original = await service.register(
        RegisterRequest(
            email="refresh@example.com",
            password="Secret123!",
            full_name="Refresh User",
        ),
    )
    rotated = await service.refresh(original.refresh_token)
    assert rotated.access_token != original.access_token
    with pytest.raises(UnauthorizedError):
        await service.refresh(original.refresh_token)


@pytest.mark.asyncio
async def test_logout_revokes_refresh(db_session: AsyncSession) -> None:
    service = AuthService(db_session)
    tokens = await service.register(
        RegisterRequest(
            email="logout@example.com",
            password="Secret123!",
            full_name="Logout User",
        ),
    )
    await service.logout(tokens.refresh_token)
    with pytest.raises(UnauthorizedError):
        await service.refresh(tokens.refresh_token)


@pytest.mark.asyncio
async def test_forgot_password_stub(db_session: AsyncSession) -> None:
    service = AuthService(db_session)
    from app.schemas.auth import ForgotPasswordRequest

    message = await service.forgot_password(
        ForgotPasswordRequest(email="missing@example.com"),
    )
    assert "password reset" in message.lower()
