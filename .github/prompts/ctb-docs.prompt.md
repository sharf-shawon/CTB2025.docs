---
mode: agent
description: CTB Admin documentation — universal prompt for all Copilot Chat tasks
tools: [read_file, create_file, replace_string_in_file, insert_edit_into_file, semantic_search, file_search, run_terminal_command]
---

You are working on **CTB Admin** documentation (`CTB2025.docs`).

## Mandatory: read these files before acting

1. `.github/STYLE_SPEC.md` — your complete editorial contract
1. `.github/knowledge/ctb-knowledge.md` — domain knowledge
1. `.github/knowledge/copilot-learnings.md` — past lessons

## Select the right agent

| Task                             | Agent to invoke      |
| -------------------------------- | -------------------- |
| Write a new doc page             | `@doc-writer`        |
| Rewrite old page to new spec     | `@doc-standardizer`  |
| Review a page for compliance     | `@doc-reviewer`      |
| Move a page to a better location | `@doc-relocator`     |
| Update mkdocs.yml nav            | `@nav-manager`       |
| Run after a PR merges            | `@knowledge-curator` |
| Audit a module or all docs       | `@doc-auditor`       |

## Output rules

- Output only markdown content for doc pages (no code fences wrapping the output)
- Always include the self-check table (STYLE_SPEC §8) at the end of your response
- Confirm: `uv run mkdocs build --strict` would pass
