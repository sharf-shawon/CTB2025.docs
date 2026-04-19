# Contributing to CTB2025.docs

Thanks for improving CTB Admin documentation.

## Repository Purpose

This repository is the public documentation site for CTB Admin.
The CTB2025 application code repository is private and is not maintained here.

## Before You Start

1. Read the Documentation Writer Guide: [.github/DOCS_WRITER_GUIDE.md](.github/DOCS_WRITER_GUIDE.md).
1. Read `.github/copilot-instructions.md`.
1. Read `.github/knowledge/ctb-knowledge.md` for module names and terminology.
1. Read `.github/knowledge/copilot-learnings.md` to avoid repeated mistakes.

## Local Setup

1. Install Python 3.13 and `uv`.
1. Run:

```bash
uv sync --extra dev
uv run pre-commit install
```

3. Serve docs locally:

```bash
uv run mkdocs serve
```

## Quality Gates

Run these before opening a PR:

```bash
uv run mkdocs build --strict
uv run pre-commit run --all-files
```

## Documentation Request Flow

1. Open an issue using the correct template in `.github/ISSUE_TEMPLATE/`.
1. Provide an accurate screenshot path under `docs/user-guide/screenshots/...`.
1. Add the correct `docs/*` label.
1. Comment `@copilot ready-to-write` when ready.

## Knowledge and Learnings Flow

- `.github/knowledge/copilot-learnings.md` stores one-row lessons from merged docs PRs.
- `.github/knowledge/ctb-knowledge.md` stores stable domain knowledge.
- Knowledge files are updated by the post-merge docs audit automation and curator workflow.

## Pull Request Expectations

- Keep changes scoped to the request.
- Do not rename or move docs paths unless requested.
- Update `mkdocs.yml` nav whenever adding a new page.
- Use end-user language (imperative, second person).
- Ensure screenshots are referenced with valid repository paths.

## Security

For vulnerabilities, follow `.github/SECURITY.md` and report privately.
