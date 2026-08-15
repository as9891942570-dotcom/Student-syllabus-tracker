"""Application settings loaded from environment variables."""

from functools import lru_cache
from pathlib import Path
from typing import List

from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

BACKEND_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_SQLITE_URL = f"sqlite+aiosqlite:///{(BACKEND_ROOT / 'eduquest.db').resolve().as_posix()}"


class Settings(BaseSettings):
    """Central configuration for EduQuest API."""

    model_config = SettingsConfigDict(
        env_file=str(BACKEND_ROOT / ".env"),
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    app_name: str = "EduQuest"
    app_version: str = "0.1.0"
    env: str = "development"
    debug: bool = True
    api_v1_prefix: str = "/api/v1"
    # Local default: SQLite (no Docker required). Docker Compose overrides with Postgres.
    database_url: str = Field(default=DEFAULT_SQLITE_URL)
    redis_url: str = Field(default="redis://localhost:6379/0")
    auto_create_tables: bool = True

    jwt_secret_key: str = Field(default="change-me-in-production-use-long-secret")
    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    refresh_token_expire_days: int = 14

    # Stored as JSON array in .env for pydantic-settings compatibility.
    cors_origins: List[str] = Field(
        default_factory=lambda: [
            "http://localhost:3000",
            "http://127.0.0.1:3000",
            "http://localhost:3001",
            "http://127.0.0.1:3001",
        ],
    )
    log_level: str = "INFO"
    timezone: str = "Asia/Kolkata"

    # Coins awarded once on first successful topic quiz (>=60%).
    coin_reward_per_topic: int = 10

    media_root: str = str(BACKEND_ROOT / "uploads")
    media_url_path: str = "/media"
    max_upload_bytes: int = 2 * 1024 * 1024
    allowed_image_types: List[str] = Field(
        default_factory=lambda: ["image/jpeg", "image/png", "image/webp"],
    )

    @property
    def is_sqlite(self) -> bool:
        return self.database_url.startswith("sqlite")

    @field_validator("cors_origins", "allowed_image_types", mode="before")
    @classmethod
    def parse_list_env(cls, value: object) -> object:
        if isinstance(value, str):
            raw = value.strip()
            if not raw:
                return []
            if raw.startswith("["):
                import json

                return json.loads(raw)
            return [item.strip() for item in raw.split(",") if item.strip()]
        return value


@lru_cache
def get_settings() -> Settings:
    return Settings()
