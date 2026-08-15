"""Shared XP awarding used by quizzes (and daily activity tracking)."""

from __future__ import annotations

from datetime import datetime, timedelta, timezone
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.models.daily_activity import DailyActivity
from app.repositories.daily_activity import DailyActivityRepository
from app.repositories.profile import StudentProfileRepository


async def award_xp(
    session: AsyncSession,
    *,
    user_id: UUID,
    xp_amount: int,
    study_seconds: int = 0,
    count_as_session: bool = False,
) -> int:
    """Persist XP on the student profile and daily activity. Returns new total XP."""
    if xp_amount < 0:
        xp_amount = 0

    profiles = StudentProfileRepository(session)
    daily_repo = DailyActivityRepository(session)

    profile = await profiles.get_by_user_id(user_id)
    if profile is None:
        return 0

    profile.total_xp = (profile.total_xp or 0) + xp_amount
    await profiles.update(profile)

    ist = timezone(timedelta(hours=5, minutes=30))
    today = datetime.now(ist).date()
    row = await daily_repo.get_for_user_date(user_id, today)
    if row is None:
        await daily_repo.create(
            DailyActivity(
                user_id=user_id,
                activity_date=today,
                sessions_completed=1 if count_as_session else 0,
                study_seconds=max(study_seconds, 0),
                xp_earned=xp_amount,
            ),
        )
    else:
        if count_as_session:
            row.sessions_completed += 1
        row.study_seconds += max(study_seconds, 0)
        row.xp_earned += xp_amount
        await daily_repo.update(row)

    return profile.total_xp
