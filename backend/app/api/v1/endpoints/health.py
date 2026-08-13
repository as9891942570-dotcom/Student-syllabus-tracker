"""Health check endpoint."""

from fastapi import APIRouter

from app.schemas.common import HealthResponse
from app.services.health import HealthService

router = APIRouter(tags=["health"])


@router.get("/health", response_model=HealthResponse)
async def health_check() -> HealthResponse:
    return await HealthService().get_health()
