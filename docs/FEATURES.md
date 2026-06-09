# Product Requirements

## Goal

Build a personal AI assistant that understands the user's background, work
experience, projects, interview preparation, and writing preferences. It should
generate personalized career content without requiring the same background to
be explained repeatedly.

Every generated response must be tailored to both:

1. the user's personal knowledge base;
2. the target company, role, job description, and requested output type.

## Core principles

- Personal markdown files are the source of truth.
- No relational database.
- Local-first storage and development.
- Use a simple retrieval pipeline before considering more orchestration.
- Writing should sound specific, concise, and human.
- Natural-language feedback should improve future outputs.
- The user reviews generated content before using it.

## Supported outputs

### LinkedIn recruiter message

Inputs: recruiter name, company, and job description.

Output: a short outreach message focused on role fit.

### LinkedIn founder message

Inputs: founder name, company, and job description.

Output: founder-specific outreach that discusses the company before asking
about opportunities.

### Recruiter cold email

Inputs: recruiter name, company, and job description.

Output: a concise, personalized email focused on relevant experience.

### Founder cold email

Inputs: founder name, company, and job description.

Output: a concise email connecting the company's work with relevant experience.

### Job application answer

Inputs: job description and application question.

Output: a tailored answer grounded in the most relevant experience or story.

Example questions include:

- Why this company?
- Why this role?
- What are you proud of?
- Describe a project.

### Resume customization

Inputs: job description and selected resume content.

Output: suggested edits grounded in existing facts. The assistant must not
invent experience, metrics, or skills.

## Chat experience

The web application should allow the user to:

- chat with the assistant;
- paste a job description;
- select an output type;
- provide optional contact and company context;
- revise an output through normal chat messages;
- provide natural-language feedback without using a separate form;
- inspect which personal sources informed a response.

## Feedback learning

The backend should classify a message as a request, revision, or reusable
feedback. For reusable feedback it should:

1. preserve the raw feedback in `data/style/feedback_log.md`;
2. extract a concise, reusable preference;
3. update the appropriate markdown preference file;
4. include relevant preferences in future retrieval and generation;
5. avoid saving one-off instructions as permanent preferences.

Preference updates must remain human-readable and editable.

## Knowledge base

Personal source files live under `data/personal/`. Writing memory lives under
`data/style/`. Role-specific interview notes live under
`data/personal/interview_preparation/`.

Documents will be split into retrievable chunks with source path, section,
document type, role tags, and experience tags stored as Qdrant metadata.

## Safety and quality requirements

- Never invent personal facts or metrics.
- Distinguish sourced facts from suggestions.
- Keep personal markdown and Qdrant data local by default.
- Never commit secrets or `.env` files.
- Make retrieved source references available for debugging.
- Allow preferences to be edited or removed manually.
- Require explicit confirmation before replacing source markdown content.

## Out of scope for the first version

- relational databases;
- multi-user accounts;
- autonomous job applications;
- complicated multi-agent workflows;
- automatic scraping of private accounts;
- training or fine-tuning a custom model;
- cloud deployment before the local workflow is stable.
