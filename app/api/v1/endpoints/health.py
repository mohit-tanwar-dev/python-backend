"""Health-check endpoint.

Useful for:
- Kubernetes liveness/readiness probes
- Load balancer health checks
- Uptime monitoring
"""

from __future__ import annotations

import time
from typing import Any

from fastapi import APIRouter

from app import __version__
from app.core.config import settings

router = APIRouter()

# Process start time (used to report uptime)
_START_TIME = time.time()


@router.get("/health", summary="Service health check")
def health() -> dict[str, Any]:
    """Return a simple health payload indicating the service is alive.

    Response schema:
        {
            "status": "ok",
            "app": "python-backend",
            "version": "0.1.0",
            "env": "local",
            "uptime_seconds": 12.34
        }
    """
    return {
        "status": "ok",
        "app": settings.app_name,
        "version": __version__,
        "env": settings.app_env,
        "uptime_seconds": round(time.time() - _START_TIME, 3),
    }
