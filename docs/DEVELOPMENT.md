# Development Workflow

## Plan

Before changing code:

1. choose one roadmap milestone or a small part of one;
2. state the expected behavior and what is out of scope;
3. identify the files and tests likely to change.

## Execute

Keep changes limited to the agreed step. Update product or architecture docs
when behavior or technical boundaries change.

## Test

Run the checks relevant to the changed area.

Frontend:

```bash
cd frontend
npm run lint
npm run typecheck
npm run build
```

Backend:

```bash
cd backend
source .venv/bin/activate
ruff check .
mypy app
pytest
```

Infrastructure:

```bash
docker compose config
```

## Commit and push

Commit only after the milestone checks pass. Use a focused commit message, then
push to `main` unless a branch or pull-request workflow has been agreed.

Never commit API keys, `.env`, virtual environments, Qdrant storage, or personal
content that is not intended to be public.
