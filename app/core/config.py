"""Application configuration via pydantic-settings.

All settings are loaded from environment variables (or a local .env file).
Each setting has a sensible default so the app runs out-of-the-box.
"""

from __future__ import annotations

from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Runtime configuration for the service."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_prefix="APP_",
        case_sensitive=False,
        extra="ignore",
    )

    # --- Identity ---
    app_name: str = Field(default="python-backend", description="Human-readable service name.")
    app_env: str = Field(default="local", description="Deployment environment.")
    debug: bool = Field(default=True, description="Enable verbose logs & error details.")

    # --- Server ---
    host: str = Field(default="0.0.0.0", description="Bind host.")
    port: int = Field(default=8000, ge=1, le=65535, description="Bind port.")

    # --- Logging ---
    log_level: str = Field(default="INFO", description="Log level.")

    # --- API ---
    api_v1_prefix: str = Field(default="/api/v1", description="Prefix for v1 routes.")


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """Return a cached Settings instance.

    Cached so reads don't re-parse the environment on every call.
    """
    return Settings()


settings = get_settings()
