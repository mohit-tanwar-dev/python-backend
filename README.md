# python-backend

[![CI](https://github.com/mohit-tanwar-dev/python-backend/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/mohit-tanwar-dev/python-backend/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/python-3.11%20%7C%203.12-blue?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688?style=flat-square&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)
[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-261230?style=flat-square)](https://docs.astral.sh/ruff/)
[![GitHub release](https://img.shields.io/github/v/release/mohit-tanwar-dev/python-backend?style=flat-square)](https://github.com/mohit-tanwar-dev/python-backend/releases)

FastAPI scaffold with health endpoint, structured logging, env-driven config, pytest suite, ruff/mypy, and GitHub Actions CI.

## Stack

- Python 3.12 (3.11 supported)
- FastAPI 0.115, Uvicorn
- Pydantic v2 + pydantic-settings
- pytest + httpx
- Ruff (lint + format), mypy
- GitHub Actions CI, Dependabot
- Multi-stage Dockerfile (non-root user, healthcheck)

## Project structure

```
python-backend/
├── app/
│   ├── main.py
│   ├── core/
│   │   ├── config.py
│   │   └── logging.py
│   └── api/v1/
│       ├── router.py
│       └── endpoints/health.py
├── tests/test_health.py
├── .github/
│   ├── workflows/ci.yml
│   ├── ISSUE_TEMPLATE/
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── dependabot.yml
├── requirements.txt
├── requirements-dev.txt
├── pytest.ini
├── ruff.toml
├── .env.example
├── Dockerfile
├── CHANGELOG.md
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
└── SECURITY.md
```

## Quick start

```bash
git clone https://github.com/mohit-tanwar-dev/python-backend.git
cd python-backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements-dev.txt
cp .env.example .env   # optional — defaults work
uvicorn app.main:app --reload
```

Endpoints:

- `GET /` — service info
- `GET /health` — health check
- `GET /api/v1/health` — versioned health check
- `GET /docs` — Swagger UI
- `GET /redoc` — ReDoc

Docker:

```bash
docker build -t python-backend:latest .
docker run --rm -p 8000:8000 --env-file .env python-backend:latest
```

## Configuration

Settings loaded from environment variables or `.env`. All have defaults.

| Variable        | Default          | Description                              |
| --------------- | ---------------- | ---------------------------------------- |
| `APP_NAME`      | `python-backend` | Service name                             |
| `APP_ENV`       | `local`          | `local` / `dev` / `prod`                 |
| `APP_DEBUG`     | `true`           | Verbose logs and error details           |
| `APP_HOST`      | `0.0.0.0`        | Bind host                                |
| `APP_PORT`      | `8000`           | Bind port                                |
| `APP_LOG_LEVEL` | `INFO`           | DEBUG / INFO / WARNING / ERROR           |

## Tests

```bash
pytest -v
ruff check .
ruff format --check .
mypy app tests
```

CI runs all of the above on Python 3.11 and 3.12.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Fork, branch from `main`, open a PR.

## Changelog

See [CHANGELOG.md](CHANGELOG.md).

## Security

See [SECURITY.md](SECURITY.md).

## License

MIT — see [LICENSE](LICENSE).
