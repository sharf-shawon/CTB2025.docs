## Context

The `04-employee` and `06-commission` documentation modules in `docs/user-guide/` contain pages that predate `STYLE_SPEC.md` v2.0. They lack mandatory sections (`Prerequisites & Role Permissions`, `Verification & Definition of Done`, `Exception Handling & Error Recovery`), miss structured validation details in field reference tables, and contain non-standard headings.

## Goals / Non-Goals

**Goals:**

- Restructure all Markdown files in `docs/user-guide/04-employee/` and `docs/user-guide/06-commission/` to follow the canonical 9-section template.
- Verify all field labels, required flags, and permissions against CTB backend models (`sharf-shawon/CTB2025`) and staging UI (`ctb-staging-mcp-server`).
- Add explicit exception handling tables with clear symptoms, root causes, and resolutions.
- Pass pre-commit style linter (`uv run pre-commit run --all-files`) and MkDocs strict build (`uv run mkdocs build --strict`).

**Non-Goals:**

- Refactoring underlying Django source code or backend models.
- Re-architecting the global `mkdocs.yml` navigation tree.

## Decisions

- **Decision 1: Batch-standardize by domain area within modules.** Standardize employee subdirectories (`employees`, `departments`, `positions`, `attendance`, `salary`, `wages`, `payouts`, `purchase-balance`, `tasks`) and commission pages systematically.
    - *Rationale:* Ensures consistent terminology and linked workflow coverage across related entity pages.
    - *Alternatives considered:* Updating all pages in a single unorganized pass or standardizing purely alphabetically.
- **Decision 2: Dual-MCP verification pipeline.** Use `github-mcp-server` to inspect model schemas/permissions and `ctb-staging-mcp-server` to verify UI elements.
    - *Rationale:* Guarantees zero hallucinations for field attributes, validation rules, and required permission roles.
    - *Alternatives considered:* Relying solely on existing documentation text without verifying against backend source code.

## Risks / Trade-offs

- **[Risk] Missing screenshot assets on staging UI** → *Mitigation:* Insert standard placeholder comments `<!-- TODO: screenshot <relative_path> -->` per `STYLE_SPEC.md` §6 when staging screenshots are unavailable.
- **[Risk] Breaking internal anchor links** → *Mitigation:* Run `uv run mkdocs build --strict` to validate every internal markdown link and header anchor across the documentation site.
