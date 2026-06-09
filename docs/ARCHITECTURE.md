# Architecture

## System overview

```text
Next.js web app
      |
      | HTTP/JSON
      v
FastAPI service
      |
      +-- markdown loader and chunker ---> Qdrant local
      |
      +-- retrieval and prompt builder --> OpenAI API
      |
      +-- feedback processor -----------> data/style/*.md

Source of truth: data/**/*.md
Derived search index: Qdrant
```

## Frontend

The Next.js application owns presentation and user interaction. It will collect
the job description, output type, optional recipient context, chat messages, and
feedback. It should not contain retrieval or prompt-building logic.

## Backend

FastAPI owns API validation, ingestion, retrieval, generation, and feedback
processing. Initial modules should stay small and direct. New orchestration
frameworks should only be introduced when a concrete need appears.

## Storage

Markdown files are authoritative. Qdrant stores derived embeddings and metadata
for semantic search. Re-indexing must be safe because the vector collection can
always be rebuilt from markdown.

No relational database is planned for the first version.

## Planned request flow

1. The frontend sends a generation request.
2. The backend validates the request and derives retrieval filters.
3. Qdrant returns relevant personal facts, stories, notes, and style rules.
4. The backend builds a grounded prompt with the job context.
5. OpenAI generates a response.
6. The API returns the output plus source references.

## Planned feedback flow

1. The user sends a message after a generated response.
2. The backend classifies it as a request, revision, or reusable feedback.
3. Reusable feedback is appended to the raw log.
4. A concise rule is added to writing preferences or banned phrases.
5. Updated style files are re-indexed for future requests.

## Configuration

Runtime settings come from environment variables. Secrets remain outside source
control. See `.env.example` for the expected names.
