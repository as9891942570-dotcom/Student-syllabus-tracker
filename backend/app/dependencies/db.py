"""Database and Redis FastAPI dependencies."""

from collections.abc import AsyncGenerator

from fastapi import Depends
from redis.asyncio import Redis
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.redis import get_redis_client
from app.db.session import get_db_session


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async for session in get_db_session():
        yield session


def get_redis() -> Redis:
    return get_redis_client()


DbSession = Depends(get_db)
RedisClient = Depends(get_redis)
