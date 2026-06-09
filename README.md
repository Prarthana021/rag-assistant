# Personal Career RAG Assistant

A local-first AI assistant that uses personal markdown files as its source of
truth to produce tailored career writing.

This repository is being built in small, tested milestones. Product behavior is
documented before implementation, and each completed milestone is committed and
pushed independently.

## Current milestone

Milestone 1 establishes the project foundation only:

- Next.js, TypeScript, and Tailwind CSS frontend
- FastAPI backend with a health endpoint
- local Qdrant configuration
- markdown knowledge-base structure
- project requirements, architecture, and roadmap documentation

Chat, document ingestion, retrieval, generation, and feedback learning are not
implemented yet.

## Repository layout

```text
frontend/   Next.js web application
backend/    FastAPI service and future RAG pipeline
data/       Personal knowledge base and writing preferences
docs/       Product requirements, architecture, and roadmap
```

## Prerequisites

- Node.js 22
- npm 11+
- Python 3.11+
- Docker with Docker Compose
- An OpenAI API key (not required for the health-check milestone)

## Setup

```bash
cp .env.example .env

cd frontend
npm install

cd ../backend
python3 -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
```

Start Qdrant:

```bash
docker compose up -d qdrant
```

Run the backend:

```bash
cd backend
source .venv/bin/activate
uvicorn app.main:app --reload --port 8000
```

Run the frontend in another terminal:

```bash
cd frontend
npm run dev
```

## Development workflow

Every milestone follows **Plan -> Execute -> Test -> Commit -> Push**. See
[docs/ROADMAP.md](docs/ROADMAP.md) for the milestone sequence and
[docs/DEVELOPMENT.md](docs/DEVELOPMENT.md) for validation commands.

Product scope and behavior are defined in [docs/FEATURES.md](docs/FEATURES.md).
