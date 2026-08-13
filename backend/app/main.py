"""FastAPI application factory."""

from contextlib import asynccontextmanager
from collections.abc import AsyncIterator
from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.api.v1.router import api_router
from app.core.config import get_settings
from app.core.exceptions import register_exception_handlers
from app.core.logging import get_logger, setup_logging
from app.db.redis import close_redis, init_redis
from app.db.session import init_database_schema
from app.middleware import RequestLoggingMiddleware

logger = get_logger(__name__)


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    setup_logging()
    settings = get_settings()
    logger.info("Starting %s", settings.app_name)
    logger.info("Database: %s", settings.database_url.split("://")[0])
    Path(settings.media_root).mkdir(parents=True, exist_ok=True)
    try:
        await init_database_schema()
        logger.info("Database schema ready")
    except Exception:
        logger.exception("Failed to initialize database schema")
        raise
    try:
        await init_redis()
    except Exception:
        logger.warning("Redis unavailable at startup; continuing without cache")
    yield
    await close_redis()
    logger.info("Shutdown complete")


def create_app() -> FastAPI:
    settings = get_settings()
    app = FastAPI(
        title=settings.app_name,
        version=settings.app_version,
        docs_url="/docs",
        redoc_url="/redoc",
        openapi_url="/openapi.json",
        lifespan=lifespan,
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.add_middleware(RequestLoggingMiddleware)
    register_exception_handlers(app)
    app.include_router(api_router, prefix=settings.api_v1_prefix)

    media_root = Path(settings.media_root)
    media_root.mkdir(parents=True, exist_ok=True)
    app.mount(
        settings.media_url_path,
        StaticFiles(directory=str(media_root)),
        name="media",
    )
    return app


app = create_app()
