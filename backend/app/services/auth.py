"""Authentication business logic."""

from datetime import datetime, timedelta, timezone
from typing import Optional
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import get_settings
from app.core.exceptions import ConflictError, UnauthorizedError, ValidationAppError
from app.core.security import (
    create_access_token,
    create_refresh_token,
    decode_token,
    hash_password,
    verify_password,
    verify_password_result,
)
from app.models.refresh_token import RefreshToken
from app.models.user import User
from app.repositories.refresh_token import RefreshTokenRepository
from app.repositories.user import UserRepository
from app.schemas.auth import (
    ForgotPasswordRequest,
    LoginRequest,
    RegisterRequest,
    TokenResponse,
    UserResponse,
)
from app.utils.tokens import hash_token


class AuthService:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session
        self.users = UserRepository(session)
        self.refresh_tokens = RefreshTokenRepository(session)
        self.settings = get_settings()

    async def register(self, payload: RegisterRequest) -> TokenResponse:
        existing = await self.users.list_by_email(payload.email)
        for account in existing:
            if verify_password(payload.password, account.password_hash):
                raise ConflictError(
                    "An account with this email and password already exists",
                )

        user = User(
            email=payload.email.lower(),
            password_hash=hash_password(payload.password),
            full_name=payload.full_name.strip(),
            is_active=True,
        )
        user = await self.users.create(user)
        return await self._issue_tokens(user)

    async def login(self, payload: LoginRequest) -> TokenResponse:
        if payload.user_id is not None:
            matched = await self.users.get_by_id(payload.user_id)
            if matched is None:
                raise UnauthorizedError("Invalid email or password")
            valid, should_rehash = verify_password_result(
                payload.password,
                matched.password_hash,
            )
            if not valid:
                raise UnauthorizedError("Invalid email or password")
        else:
            candidates = await self.users.list_by_email(payload.email or "")
            matched = None
            should_rehash = False
            for account in candidates:
                valid, should_rehash = verify_password_result(
                    payload.password,
                    account.password_hash,
                )
                if valid:
                    matched = account
                    break
            if matched is None:
                raise UnauthorizedError("Invalid email or password")
        if not matched.is_active:
            raise UnauthorizedError("Account is inactive")
        if should_rehash:
            matched.password_hash = hash_password(payload.password)
            await self.users.update(matched)
        return await self._issue_tokens(matched)

    async def refresh(self, refresh_token: Optional[str]) -> TokenResponse:
        if not refresh_token:
            raise UnauthorizedError("Refresh token is required")

        try:
            claims = decode_token(refresh_token)
        except ValueError as exc:
            raise UnauthorizedError("Invalid refresh token") from exc

        if claims.get("type") != "refresh":
            raise UnauthorizedError("Invalid refresh token type")

        token_row = await self.refresh_tokens.get_by_hash(hash_token(refresh_token))
        if token_row is None or token_row.revoked_at is not None:
            raise UnauthorizedError("Refresh token has been revoked")

        expires_at = token_row.expires_at
        if expires_at.tzinfo is None:
            expires_at = expires_at.replace(tzinfo=timezone.utc)
        if expires_at < datetime.now(timezone.utc):
            raise UnauthorizedError("Refresh token has expired")

        user = await self.users.get_by_id(token_row.user_id)
        if user is None or not user.is_active:
            raise UnauthorizedError("User not found or inactive")

        await self.refresh_tokens.revoke(token_row)
        return await self._issue_tokens(user)

    async def logout(self, refresh_token: Optional[str], user_id: Optional[UUID] = None) -> None:
        if refresh_token:
            token_row = await self.refresh_tokens.get_by_hash(hash_token(refresh_token))
            if token_row is not None and token_row.revoked_at is None:
                await self.refresh_tokens.revoke(token_row)
                return
        if user_id is not None:
            await self.refresh_tokens.revoke_all_for_user(user_id)

    async def forgot_password(self, payload: ForgotPasswordRequest) -> str:
        # Stub: do not reveal whether the email exists.
        _ = await self.users.get_by_email(payload.email)
        return (
            "Password reset by email is not available yet. "
            "No reset message will be sent."
        )

    async def get_user(self, user_id: UUID) -> User:
        user = await self.users.get_by_id(user_id)
        if user is None or not user.is_active:
            raise UnauthorizedError("User not found or inactive")
        return user

    async def _issue_tokens(self, user: User) -> TokenResponse:
        subject = str(user.id)
        access_token = create_access_token(subject)
        refresh_token = create_refresh_token(subject)
        expires_at = datetime.now(timezone.utc) + timedelta(
            days=self.settings.refresh_token_expire_days,
        )
        await self.refresh_tokens.create(
            RefreshToken(
                user_id=user.id,
                token_hash=hash_token(refresh_token),
                expires_at=expires_at,
            ),
        )
        return TokenResponse(
            access_token=access_token,
            refresh_token=refresh_token,
            user=UserResponse.model_validate(user),
        )

    @staticmethod
    def validate_password_strength(password: str) -> None:
        if len(password) < 8:
            raise ValidationAppError("Password must be at least 8 characters")
