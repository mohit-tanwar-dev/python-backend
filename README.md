# python-backend

[![CI](https://github.com/mohit-tanwar-dev/python-backend/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/mohit-tanwar-dev/python-backend/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/python-3.11%20%7C%203.12-blue?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688?style=flat-square&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)
[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-261230?style=flat-square)](https://docs.astral.sh/ruff/)
[![GitHub release](https://img.shields.io/github/v/release/mohit-tanwar-dev/python-backend?style=flat-square)](https://github.com/mohit-tanwar-dev/python-backend/releases)

[![Code Coverage](https://img.shields.io/badge/coverage-XX%25-red?style=flat-square)](./htmlcov/index.html)

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

## Development Workflow

For local development, it's recommended to use a virtual environment. The project uses `ruff` for linting and formatting, and `mypy` for type checking. `pre-commit` hooks are configured to ensure code quality before commits.

### Local Setup

```bash
# Install pre-commit hooks
pre-commit install
```

### Running Linters and Type Checks

```bash
ruff check .
ruff format --check .
mypy app tests
```

These checks are also run in the CI pipeline.

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

## Production Deployment

For production deployments, it is recommended to use a production-ready ASGI server like Gunicorn with Uvicorn workers. Below are examples for running the application in a production environment.

### Gunicorn with Uvicorn Workers

```bash
gunicorn -w 4 -k uvicorn.workers.UvicornWorker app.main:app --bind 0.0.0.0:8000
```

This command starts Gunicorn with 4 Uvicorn worker processes, binding to all network interfaces on port 8000.

### Health Check Path

The application provides a health check endpoint at `/health` (or `/api/v1/health` for the versioned API) that can be used by load balancers or container orchestration systems to verify the application's status.

## Logging Configuration

The application uses structured logging, configured via `app/core/logging.py`. The log level can be controlled using the `APP_LOG_LEVEL` environment variable (e.g., `INFO`, `DEBUG`, `WARNING`, `ERROR`). Logs are typically output to `stdout` and `stderr`, making them suitable for containerized environments and centralized logging solutions.

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

## Release Process

Releases are managed via GitHub releases. A new release can be cut by creating a new tag (e.g., `v1.0.0`). The CI/CD pipeline is configured to automatically build and publish artifacts upon a new tag. Changelog conventions are maintained in `CHANGELOG.md`.

## Changelog

See [CHANGELOG.md](CHANGELOG.md).

## Security

See [SECURITY.md](SECURITY.md).

## License

MIT — see [LICENSE](LICENSE).
