"""Health endpoint tests (unit-level, Redis/DB may be degraded without Docker)."""

from unittest.mock import AsyncMock, patch

import pytest
from httpx import ASGITransport, AsyncClient

from app.main import create_app
from app.schemas.common import HealthDependencyStatus, HealthResponse


@pytest.mark.asyncio
async def test_health_endpoint_healthy() -> None:
    app = create_app()
    healthy = HealthResponse(
        status="healthy",
        app="EduQuest",
        version="0.1.0",
        dependencies=HealthDependencyStatus(database=True, redis=True),
    )

    with patch(
        "app.services.health.HealthService.get_health",
        new=AsyncMock(return_value=healthy),
    ):
        transport = ASGITransport(app=app)
        async with AsyncClient(transport=transport, base_url="http://test") as client:
            response = await client.get("/api/v1/health")

    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "healthy"
    assert payload["dependencies"]["database"] is True
    assert payload["dependencies"]["redis"] is True


@pytest.mark.asyncio
async def test_openapi_available() -> None:
    app = create_app()
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.get("/openapi.json")
    assert response.status_code == 200
    assert response.json()["info"]["title"] == "EduQuest"
