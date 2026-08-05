# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0] - 2026-08-04

### Added
- FastAPI application scaffold with `lifespan` event hooks.
- `/health` and `/api/v1/health` endpoints returning service status, version, and uptime.
- Root `/` endpoint returning basic service info.
- Pydantic-settings based configuration with sensible defaults.
- Structured logging via stdlib `logging`.
- `pytest` test suite covering all endpoints.
- `ruff` lint + format configuration targeting Python 3.12.
- `mypy` for static type checking.
- `.env.example` documenting all supported environment variables.
- MIT License.

[Unreleased]: https://github.com/mohit-tanwar-dev/python-backend/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/mohit-tanwar-dev/python-backend/releases/tag/v0.1.0
