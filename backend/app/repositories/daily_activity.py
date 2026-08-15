"""Daily activity repository (XP aggregation — independent of study sessions)."""

from datetime import date
from typing import Optional
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.daily_activity import DailyActivity
from app.repositories.base import BaseRepository


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
