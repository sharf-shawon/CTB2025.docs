# Knowledge System

This folder stores reusable project knowledge for Copilot and maintainers.

## Files

- `ctb-knowledge.md`: stable CTB domain knowledge, module map, terminology, and docs path conventions.
- `copilot-learnings.md`: one-line lessons captured from merged docs pull requests.

## Update Model

1. Docs pull request is merged.
2. `Docs Audit` workflow runs once for that PR.
3. Workflow appends one learning row to `copilot-learnings.md` if missing.
4. Workflow appends one automation signal row to `ctb-knowledge.md` if missing.

## Guardrails

- Keep rows compact and single-line.
- Do not delete historical learnings.
- Use `YYYY-MM-DD` dates.
- Use module names and paths exactly as documented.

## Why this matters

Agents use these files to avoid repeated mistakes and maintain consistent terminology across all documentation updates.
