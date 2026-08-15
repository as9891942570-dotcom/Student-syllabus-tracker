"""Health check service."""

from app.core.config import get_settings
from app.db.redis import check_redis_connection
from app.db.session import check_database_connection
from app.schemas.common import HealthDependencyStatus, HealthResponse


class HealthService:
    async def get_health(self) -> HealthResponse:
        settings = get_settings()
        db_ok = await check_database_connection()
        redis_ok = await check_redis_connection()
        # Redis is an optional cache. Database availability determines API health.
        status = "healthy" if db_ok else "unhealthy"
        return HealthResponse(
            status=status,
            app=settings.app_name,
            version=settings.app_version,
            dependencies=HealthDependencyStatus(database=db_ok, redis=redis_ok),
        )
