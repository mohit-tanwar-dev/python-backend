# python-backend

[![CI](https://github.com/mohit-tanwar-dev/python-backend/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/mohit-tanwar-dev/python-backend/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/python-3.11%20%7C%203.12-blue?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688?style=flat-square&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)
[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-261230?style=flat-square)](https://docs.astral.sh/ruff/)
[![GitHub release](https://img.shields.io/github/v/release/mohit-tanwar-dev/python-backend?style=flat-square)](https://github.com/mohit-tanwar-dev/python-backend/releases)

> A production-ready **FastAPI** scaffold with health checks, structured logging, configurable settings, and CI/CD out of the box.
> Use this as the starting point for any new Python backend service.

---

## ✨ Features

- 🚀 **FastAPI** async web framework with auto-generated OpenAPI docs (`/docs`, `/redoc`)
- ⚙️ **Pydantic v2 + pydantic-settings** for type-safe, environment-driven configuration
- 📋 **Health-check endpoint** at `/health` and `/api/v1/health` — perfect for Kubernetes probes and load balancers
- 🪵 **Structured logging** with consistent timestamps and log levels
- 🧪 **pytest** test suite with `httpx` + `TestClient` covering every endpoint
- 🧹 **Ruff** for linting and formatting (replaces black + isort + flake8)
- 🔍 **mypy** for static type checking
- 🤖 **GitHub Actions CI** running on every push & PR (Python 3.11 + 3.12 matrix)
- 📦 **Dependabot** for automated dependency updates
- 🐳 **Docker-ready** with multi-stage Dockerfile (optional)
- 📚 **Issue & PR templates**, **CONTRIBUTING.md**, **CODE_OF_CONDUCT.md**, **SECURITY.md**

---

## 🛠️ Tech stack

| Layer        | Tool                                |
| ------------ | ----------------------------------- |
| Framework    | [FastAPI](https://fastapi.tiangolo.com/) 0.115 |
| Server       | [Uvicorn](https://www.uvicorn.org/) 0.34       |
| Validation   | [Pydantic](https://pydantic.dev/) 2.10 + `pydantic-settings` |
| Testing      | [pytest](https://pytest.org/) 8.3 + `pytest-asyncio` |
| HTTP client  | [httpx](https://www.python-httpx.org/) 0.28    |
| Lint/format  | [Ruff](https://docs.astral.sh/ruff/) 0.8       |
| Type check   | [mypy](https://mypy-lang.org/) 1.14            |
| Python       | 3.12+ (3.11 supported)                          |

---

## 📁 Project structure

```
python-backend/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI app entrypoint
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py         # Pydantic settings
│   │   └── logging.py        # Structured logging
│   └── api/
│       ├── __init__.py
│       └── v1/
│           ├── __init__.py
│           ├── router.py      # Aggregates route modules
│           └── endpoints/
│               ├── __init__.py
│               └── health.py  # Health-check endpoint
├── tests/
│   ├── __init__.py
│   └── test_health.py
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
├── LICENSE
├── CHANGELOG.md
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── SECURITY.md
└── README.md
```

---

## 🚀 Quick start

### Option A — Local development

```bash
# 1. Clone
git clone https://github.com/mohit-tanwar-dev/python-backend.git
cd python-backend

# 2. Create a virtual environment
python -m venv .venv
source .venv/bin/activate          # Linux / macOS
# .venv\Scripts\activate           # Windows

# 3. Install dependencies
pip install -r requirements-dev.txt   # includes dev / test extras

# 4. (optional) configure env
cp .env.example .env

# 5. Run the server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Open in your browser:
- 🩺 Health — http://localhost:8000/health
- 📚 Swagger UI — http://localhost:8000/docs
- 📘 ReDoc — http://localhost:8000/redoc
- 📋 OpenAPI JSON — http://localhost:8000/openapi.json

### Option B — Docker

```bash
docker build -t python-backend:latest .
docker run --rm -p 8000:8000 --env-file .env python-backend:latest
```

---

## 🔌 API endpoints

| Method | Path              | Description                                    |
| ------ | ----------------- | ---------------------------------------------- |
| `GET`  | `/`               | Root — basic service info & docs link          |
| `GET`  | `/health`         | Public health check (no API prefix)            |
| `GET`  | `/api/v1/health`  | Versioned health check under `/api/v1` prefix  |

### Example response (`GET /health`)

```json
{
  "status": "ok",
  "app": "python-backend",
  "version": "0.1.0",
  "env": "local",
  "uptime_seconds": 12.345
}
```

---

## ⚙️ Configuration

All settings are loaded from environment variables (or a local `.env` file).
Every setting has a sensible default, so the service runs out-of-the-box.

| Variable        | Default          | Description                              |
| --------------- | ---------------- | ---------------------------------------- |
| `APP_NAME`      | `python-backend` | Human-readable app name                  |
| `APP_ENV`       | `local`          | Environment: `local` / `dev` / `prod`    |
| `APP_DEBUG`     | `true`           | Enable verbose logging & error details   |
| `APP_HOST`      | `0.0.0.0`        | Bind host                                |
| `APP_PORT`      | `8000`           | Bind port                                |
| `APP_LOG_LEVEL` | `INFO`           | Log level: DEBUG/INFO/WARNING/ERROR      |

Copy `.env.example` to `.env` and edit as needed.

---

## 🧪 Testing & quality checks

```bash
# Run tests
pytest -v

# Lint
ruff check .

# Format check (without writing)
ruff format --check .

# Format (write)
ruff format .

# Type check
mypy app tests
```

CI runs all of the above on every push and pull request, on Python 3.11 **and** 3.12.

---

## 🤝 Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for setup instructions, branch conventions, and PR guidelines.

1. Fork the repo
2. Create a feature branch: `git checkout -b feat/my-feature`
3. Commit using [Conventional Commits](https://www.conventionalcommits.org/)
4. Open a PR against `main`

Please follow the [Code of Conduct](CODE_OF_CONDUCT.md) in all interactions.

---

## 📜 Changelog

See [CHANGELOG.md](CHANGELOG.md) for release history.

---

## 🔐 Security

To report a vulnerability, see [SECURITY.md](SECURITY.md).

---

## 📄 License

[MIT](LICENSE) © Mohit Tanwar
