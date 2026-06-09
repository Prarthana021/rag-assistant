# Roadmap

Each milestone follows **Plan -> Execute -> Test -> Commit -> Push**. A milestone
must pass its documented checks before work begins on the next one.

## Milestone 1: Foundation

- [x] Define product requirements and architecture.
- [x] Scaffold Next.js and FastAPI applications.
- [x] Add local Qdrant configuration.
- [x] Create the markdown knowledge-base structure.
- [x] Add lint, type-check, and backend test configuration.

## Milestone 2: Application shell

- [ ] Build the basic page layout.
- [ ] Add output-type selection.
- [ ] Add job-description and context inputs.
- [ ] Add a non-functional chat panel with typed UI models.
- [ ] Add focused frontend tests.

## Milestone 3: Knowledge ingestion

- [ ] Parse markdown by headings and sections.
- [ ] Define chunk metadata and stable document IDs.
- [ ] Generate embeddings with OpenAI.
- [ ] Upsert and rebuild a local Qdrant collection.
- [ ] Add ingestion tests using fixtures.

## Milestone 4: Retrieval API

- [ ] Add semantic retrieval with metadata filters.
- [ ] Return source references and retrieval diagnostics.
- [ ] Add API validation and retrieval tests.

## Milestone 5: Grounded generation

- [ ] Define prompt templates by output type.
- [ ] Generate responses from retrieved facts and style rules.
- [ ] Prevent unsupported personal claims.
- [ ] Connect the frontend to the generation API.

## Milestone 6: Feedback memory

- [ ] Classify request, revision, and reusable feedback messages.
- [ ] Append raw feedback with timestamps.
- [ ] Extract and deduplicate preference rules.
- [ ] Re-index updated style memory.
- [ ] Add user-visible confirmation and tests.

## Milestone 7: Quality and hardening

- [ ] Add representative evaluation cases for every output type.
- [ ] Add loading, error, and empty states.
- [ ] Add local data backup and re-index instructions.
- [ ] Review privacy, prompt injection, and failure behavior.
