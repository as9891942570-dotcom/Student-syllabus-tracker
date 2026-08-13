"""Student profile repository."""

from typing import Optional
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.models.student_profile import StudentProfile
from app.repositories.base import BaseRepository


class StudentProfileRepository(BaseRepository[StudentProfile]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(StudentProfile, session)

    async def get_by_user_id(self, user_id: UUID) -> Optional[StudentProfile]:
        result = await self.session.execute(
            select(StudentProfile)
            .where(StudentProfile.user_id == user_id)
            .options(
                selectinload(StudentProfile.board),
                selectinload(StudentProfile.school_class),
                selectinload(StudentProfile.stream),
                selectinload(StudentProfile.user),
            ),
        )
        return result.scalar_one_or_none()
