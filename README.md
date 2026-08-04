# Python backend service

A Python backend service built with [FastAPI](https://fastapi.tiangolo.com/).

## Stack

- **Python 3.12**
- **FastAPI** — async web framework
- **Uvicorn** — ASGI server
- **Pydantic v2** — data validation & settings
- **pytest** + **httpx** — testing

## Project structure

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
├── requirements.txt
├── requirements-dev.txt
└── README.md
```

## Quick start

```bash
# 1. Create a virtual environment
python -m venv .venv
source .venv/bin/activate          # Linux / macOS
# .venv\Scripts\activate           # Windows

# 2. Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt   # dev / test extras

# 3. Run the server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Open http://localhost:8000/health to verify, and http://localhost:8000/docs for the interactive Swagger UI.

## Environment variables

The service reads configuration from environment variables (or a local `.env` file). All settings have sensible defaults, so it runs out-of-the-box without any env config.

| Variable        | Default | Description                          |
| --------------- | ------- | ------------------------------------ |
| `APP_NAME`      | python-backend | Human-readable app name        |
| `APP_ENV`       | local   | Environment: `local`/`dev`/`prod`    |
| `APP_DEBUG`     | true    | Enable verbose logging & error details |
| `APP_HOST`      | 0.0.0.0 | Bind host                            |
| `APP_PORT`      | 8000    | Bind port                            |
| `APP_LOG_LEVEL` | INFO    | Log level: DEBUG/INFO/WARNING/ERROR  |

## Tests

```bash
pytest -v
```

## License

MIT
