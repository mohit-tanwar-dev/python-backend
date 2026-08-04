"""Tests for the health endpoint."""

from __future__ import annotations

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_returns_ok() -> None:
    """The health endpoint should return status=ok and a 200 response."""
    response = client.get("/health")
    assert response.status_code == 200

    payload = response.json()
    assert payload["status"] == "ok"
    assert "app" in payload
    assert "version" in payload
    assert "uptime_seconds" in payload
    assert payload["uptime_seconds"] >= 0


def test_health_v1_prefix_also_works() -> None:
    """The health endpoint should also be reachable under the /api/v1 prefix."""
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_root_returns_service_info() -> None:
    """The root endpoint should return service metadata."""
    response = client.get("/")
    assert response.status_code == 200

    payload = response.json()
    assert payload["service"] == "python-backend"
    assert "version" in payload
    assert payload["docs"] == "/docs"
