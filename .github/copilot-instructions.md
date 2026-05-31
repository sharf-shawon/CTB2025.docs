# Copilot Instructions — CTB Admin Documentation

## Style contract

All tone, structure, template, terminology, and formatting rules live in **one file only**:

> `.github/STYLE_SPEC.md`

Read that file before any documentation task. Do not rely on memory for style rules.

## Available agents (invoke with @agent-name)

| Command | What it does |
|---|---|
| `@doc-writer` | Write a new page from scratch |
| `@doc-standardizer` | Rewrite an existing page to STYLE_SPEC |
| `@doc-reviewer` | Review a page and output structured feedback |
| `@doc-relocator` | Analyze or execute a page move |
| `@nav-manager` | Update `mkdocs.yml` nav entries |
| `@knowledge-curator` | Post-merge knowledge sync (run after merging only) |
| `@doc-auditor` | Full module or repo audit |

## Universal rules

1. STYLE_SPEC.md is the only style authority
2. Never rename or move files without doc-relocator relocation checklist
3. Never edit `.github/knowledge/` files mid-task
4. Every page needs a screenshot or `<!-- TODO: screenshot ... -->` placeholder
5. Every new page needs a matching `mkdocs.yml` nav entry
6. `uv run mkdocs build --strict` must pass after every change

## Context files to load for every task

- `.github/STYLE_SPEC.md`
- `.github/knowledge/ctb-knowledge.md`
- `.github/knowledge/copilot-learnings.md`
- `mkdocs.yml` (grep the relevant section only)

## Style benchmarks

- `docs/user-guide/00-getting-started/dashboard.md` — full-length page reference
- `docs/user-guide/00-getting-started/login-and-logout.md` — short-page reference
