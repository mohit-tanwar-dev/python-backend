# Contributing to python-backend

## Development setup

```bash
git clone https://github.com/<your-username>/python-backend.git
cd python-backend
python -m venv .venv
source .venv/bin/activate          # Linux / macOS
# .venv\Scripts\activate           # Windows
pip install -r requirements-dev.txt
cp .env.example .env
uvicorn app.main:app --reload
pytest -v
ruff check .
ruff format --check .
mypy app tests
```

## Branch and commit conventions

- Branch from `main`: `feat/...`, `fix/...`, `docs/...`
- Use [Conventional Commits](https://www.conventionalcommits.org/):
  - `feat: add /ready endpoint`
  - `fix: handle missing env var gracefully`
  - `docs: clarify setup steps`
  - `refactor: split health endpoint logic`
  - `test: add tests for /api/v1/health`
  - `chore: bump ruff to 0.8.5`

## Pull request flow

1. Open a PR against `main`.
2. CI must pass (ruff + pytest on Python 3.11 and 3.12).
3. Squash-and-merge once approved.

## Code style

- Python 3.12+ syntax (PEP 695 type hints)
- Line length: 100 chars (`ruff.toml`)
- All functions and modules have docstrings
- Tests live in `tests/` named `test_*.py`

## Code of conduct

Be kind. Be patient. Be helpful.
