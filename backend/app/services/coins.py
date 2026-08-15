"""Coin rewards for successful topic quiz completion."""

from __future__ import annotations

from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import get_settings
from app.repositories.profile import StudentProfileRepository


def coin_reward_per_topic() -> int:
    """Configured coins for the first successful topic quiz (>=60%)."""
    return max(0, int(get_settings().coin_reward_per_topic))


async def award_coins(
    session: AsyncSession,
    *,
    user_id: UUID,
    coins_amount: int,
) -> int:
    """Add coins to the student profile. Returns new total_coins."""
    amount = max(0, int(coins_amount))
    profiles = StudentProfileRepository(session)
    profile = await profiles.get_by_user_id(user_id)
    if profile is None:
        return 0
    if amount:
        profile.total_coins = (profile.total_coins or 0) + amount
        await profiles.update(profile)
    return profile.total_coins or 0
