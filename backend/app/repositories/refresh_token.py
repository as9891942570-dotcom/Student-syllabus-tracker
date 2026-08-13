"""Refresh token data-access repository."""

from datetime import datetime, timezone
from typing import Optional
from uuid import UUID

from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.refresh_token import RefreshToken
from app.repositories.base import BaseRepository


class RefreshTokenRepository(BaseRepository[RefreshToken]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(RefreshToken, session)

    async def get_by_hash(self, token_hash: str) -> Optional[RefreshToken]:
        result = await self.session.execute(
            select(RefreshToken).where(RefreshToken.token_hash == token_hash),
        )
        return result.scalar_one_or_none()

    async def revoke(self, token: RefreshToken) -> RefreshToken:
        token.revoked_at = datetime.now(timezone.utc)
        return await self.update(token)

    async def revoke_all_for_user(self, user_id: UUID) -> None:
        await self.session.execute(
            update(RefreshToken)
            .where(
                RefreshToken.user_id == user_id,
                RefreshToken.revoked_at.is_(None),
            )
            .values(revoked_at=datetime.now(timezone.utc)),
        )
