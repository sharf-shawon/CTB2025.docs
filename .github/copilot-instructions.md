# Copilot Instructions for CTB2025.wiki

## Project Purpose

This repository contains the MkDocs-based documentation site for CTB Admin.
Focus all changes on documentation structure, content quality, and docs tooling.

## Stack and Tooling

- Python 3.13
- MkDocs + Material theme
- Dependency management and execution via `uv`
- Quality gates via `pre-commit`

## Core Rules for Changes

1. Keep changes minimal and scoped to the user request.
1. Do not rename/move existing docs paths unless explicitly requested.
1. When adding a new page under `docs/user-guide`, update `mkdocs.yml` nav in the same change.
1. Preserve existing section naming conventions and numeric module prefixes.
1. Use Markdown headings and wording that are practical for end users and operators.

## Documentation Structure Expectations

- Main docs live under `docs/`.
- User documentation is organized under `docs/user-guide/` with these modules:
  - `00-getting-started`
  - `01-business`
  - `02-factory`
  - `03-trade`
  - `04-employee`
  - `05-settings-and-admin`
  - `06-reference`
- Screenshot placeholders live in `docs/user-guide/screenshots/*`.

## Content Conventions

- Keep language clear and operational.
- Prefer task-oriented titles, for example: “Add Client”, “Create Invoice”, “Maintenance Mode”.
- For special pages (invoice print, chalan, report dashboards, offline page, maintenance), keep dedicated pages.
- Avoid filler text in final docs updates; provide actionable steps and field-level guidance.

## Validation Checklist

Before considering work complete:

1. Run strict docs build:
   - `uv run mkdocs build --strict`
1. Run hooks for quality:
   - `uv run pre-commit run --all-files`
1. Confirm no broken nav links introduced in `mkdocs.yml`.

## Commands to Prefer

- Sync dependencies: `uv sync --extra dev`
- Serve docs locally: `uv run mkdocs serve`
- Build docs: `uv run mkdocs build --strict`
- Run quality checks: `uv run pre-commit run --all-files`

## What to Avoid

- Do not add unrelated application code changes.
- Do not change CI workflow intent unless requested.
- Do not add new design systems or custom frontend frameworks.
