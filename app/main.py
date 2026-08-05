"""FastAPI application entrypoint.

Run locally with:
    uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
"""

from __future__ import annotations

from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app import __version__
from app.api.v1.router import api_router
from app.core.config import settings
from app.core.logging import configure_logging


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    """Application startup / shutdown lifecycle hooks."""
    configure_logging()
    # Add any startup logic here (DB connections, cache warm-up, etc.)
    yield
    # Add any shutdown logic here (close connections, flush buffers, etc.)


app = FastAPI(
    title=settings.app_name,
    version=__version__,
    description="Python backend service built with FastAPI.",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
    debug=settings.debug,
    lifespan=lifespan,
)

# Mount v1 routes
app.include_router(api_router, prefix=settings.api_v1_prefix)

# Also expose a root-level /health for convenience (no API prefix)
app.include_router(api_router, include_in_schema=False, prefix="")


@app.get("/", summary="Root", include_in_schema=False)
def root() -> dict[str, str]:
    """Tiny root endpoint returning basic service info."""
    return {
        "service": settings.app_name,
        "version": __version__,
        "docs": "/docs",
    }
