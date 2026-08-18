"""User data-access repository."""

from typing import Optional
from uuid import UUID

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user import User
from app.repositories.base import BaseRepository


class UserRepository(BaseRepository[User]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(User, session)

    async def list_by_email(self, email: str) -> list[User]:
        # Older accounts may have mixed-case emails; Postgres comparison is case-sensitive.
        normalized = (email or "").strip().lower()
        result = await self.session.execute(
            select(User)
            .where(func.lower(User.email) == normalized)
            .order_by(User.created_at),
        )
        return list(result.scalars().all())

    async def get_by_email(self, email: str) -> Optional[User]:
        users = await self.list_by_email(email)
        return users[0] if users else None

    async def get_by_id(self, user_id: UUID) -> Optional[User]:
        return await self.get(user_id)
