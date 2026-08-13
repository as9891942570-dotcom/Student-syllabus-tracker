"""Async Redis client lifecycle helpers."""

from typing import Optional

import redis.asyncio as redis

from app.core.config import get_settings
from app.core.logging import get_logger

logger = get_logger(__name__)

_redis_client: Optional[redis.Redis] = None


async def init_redis() -> redis.Redis:
    global _redis_client
    settings = get_settings()
    _redis_client = redis.from_url(
        settings.redis_url,
        encoding="utf-8",
        decode_responses=True,
    )
    await _redis_client.ping()
    logger.info("Redis connection established")
    return _redis_client


async def close_redis() -> None:
    global _redis_client
    if _redis_client is not None:
        await _redis_client.aclose()
        _redis_client = None
        logger.info("Redis connection closed")


def get_redis_client() -> redis.Redis:
    if _redis_client is None:
        raise RuntimeError("Redis client is not initialized")
    return _redis_client


async def check_redis_connection() -> bool:
    try:
        client = get_redis_client()
        await client.ping()
        return True
    except Exception:
        return False
