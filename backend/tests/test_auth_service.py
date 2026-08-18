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
    verify_password_result,
)
from app.models.user import User
from app.schemas.auth import LoginRequest, RegisterRequest
from app.services.auth import AuthService
from app.utils.tokens import hash_token


def test_password_hash_and_verify() -> None:
    hashed = hash_password("Secret123!")
    assert hashed != "Secret123!"
    assert verify_password("Secret123!", hashed)
    assert not verify_password("wrong", hashed)
    assert verify_password("", hashed) is False
    assert verify_password("Secret123!", "") is False
    assert verify_password("Secret123!", "not-a-hash") is False


def test_native_bcrypt_hash_still_verifies() -> None:
    import bcrypt

    native = bcrypt.hashpw(b"LegacyPass1!", bcrypt.gensalt(rounds=4, prefix=b"2a")).decode()
    assert native.startswith("$2a$")
    assert verify_password("LegacyPass1!", native)
    assert not verify_password("wrong-pass", native)
    valid, should_rehash = verify_password_result("LegacyPass1!", native)
    assert valid is True
    assert should_rehash is True


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
    assert "not available" in message.lower()


@pytest.mark.asyncio
async def test_login_mixed_case_legacy_email(db_session: AsyncSession) -> None:
    service = AuthService(db_session)
    user = User(
        email="OldStudent@Example.COM",
        password_hash=hash_password("Secret123!"),
        full_name="Legacy Student",
        is_active=True,
    )
    await service.users.create(user)

    tokens = await service.login(
        LoginRequest(email="oldstudent@example.com", password="Secret123!"),
    )
    assert tokens.user.id == user.id
    assert tokens.access_token

    with pytest.raises(UnauthorizedError) as exc:
        await service.login(
            LoginRequest(email="oldstudent@example.com", password="WrongPass1!"),
        )
    assert "Invalid email or password" in str(exc.value)


@pytest.mark.asyncio
async def test_login_native_bcrypt_hash_and_upgrade(db_session: AsyncSession) -> None:
    import bcrypt

    service = AuthService(db_session)
    native = bcrypt.hashpw(b"Secret123!", bcrypt.gensalt(rounds=4, prefix=b"2a")).decode()
    user = User(
        email="legacyhash@example.com",
        password_hash=native,
        full_name="Hash Upgrade",
        is_active=True,
    )
    await service.users.create(user)

    tokens = await service.login(
        LoginRequest(email="legacyhash@example.com", password="Secret123!"),
    )
    assert tokens.user.id == user.id
    refreshed = await service.users.get_by_id(user.id)
    assert refreshed is not None
    assert refreshed.password_hash != native
    assert refreshed.password_hash.startswith("$2b$")
    assert verify_password("Secret123!", refreshed.password_hash)
