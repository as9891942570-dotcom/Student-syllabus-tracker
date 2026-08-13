"""Study session and daily activity repositories."""

from datetime import date
from typing import Optional
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.models.daily_activity import DailyActivity
from app.models.study_session import StudySession
from app.repositories.base import BaseRepository


class StudySessionRepository(BaseRepository[StudySession]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(StudySession, session)

    async def get_active_for_user(self, user_id: UUID) -> Optional[StudySession]:
        result = await self.session.execute(
            select(StudySession)
            .where(
                StudySession.user_id == user_id,
                StudySession.status == "active",
            )
            .options(
                selectinload(StudySession.subject),
                selectinload(StudySession.chapter),
                selectinload(StudySession.topic),
            )
            .limit(1),
        )
        return result.scalar_one_or_none()

    async def get_for_user(
        self,
        session_id: UUID,
        user_id: UUID,
    ) -> Optional[StudySession]:
        result = await self.session.execute(
            select(StudySession)
            .where(
                StudySession.id == session_id,
                StudySession.user_id == user_id,
            )
            .options(
                selectinload(StudySession.subject),
                selectinload(StudySession.chapter),
                selectinload(StudySession.topic),
            ),
        )
        return result.scalar_one_or_none()


class DailyActivityRepository(BaseRepository[DailyActivity]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(DailyActivity, session)

    async def get_for_user_date(
        self,
        user_id: UUID,
        activity_date: date,
    ) -> Optional[DailyActivity]:
        result = await self.session.execute(
            select(DailyActivity).where(
                DailyActivity.user_id == user_id,
                DailyActivity.activity_date == activity_date,
            ),
        )
        return result.scalar_one_or_none()
