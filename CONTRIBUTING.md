# Contributing to python-backend

Thanks for taking the time to contribute! 🎉

This document describes how to set up your environment and submit changes.

## 🛠️ Development setup

```bash
# 1. Fork & clone
git clone https://github.com/<your-username>/python-backend.git
cd python-backend

# 2. Create a virtual environment
python -m venv .venv
source .venv/bin/activate          # Linux / macOS
# .venv\Scripts\activate           # Windows

# 3. Install dev dependencies
pip install -r requirements-dev.txt

# 4. Copy env file (optional — defaults work out of the box)
cp .env.example .env

# 5. Run the server
uvicorn app.main:app --reload

# 6. Run tests / lint
pytest -v
ruff check .
ruff format --check .
mypy app tests
```

## 🌿 Branch & commit conventions

- Branch from `main`: `feat/my-feature`, `fix/my-bugfix`, `docs/my-change`
- Use [Conventional Commits](https://www.conventionalcommits.org/):
  - `feat: add /ready endpoint`
  - `fix: handle missing env var gracefully`
  - `docs: clarify setup steps`
  - `refactor: split health endpoint logic`
  - `test: add tests for /api/v1/health`
  - `chore: bump ruff to 0.8.5`

## 🚦 Pull request flow

1. Open a PR against `main`.
2. CI must pass (ruff + pytest on Python 3.11 & 3.12).
3. Request a review.
4. Squash-and-merge once approved.

## ✅ Code style

- Python 3.12+ syntax is fine (PEP 695 type hints, etc.)
- Line length: 100 chars (configured in `ruff.toml`)
- All functions / modules have docstrings
- Tests live in `tests/` and are named `test_*.py`

## 📜 Code of conduct

Be kind. Be patient. Be helpful.
