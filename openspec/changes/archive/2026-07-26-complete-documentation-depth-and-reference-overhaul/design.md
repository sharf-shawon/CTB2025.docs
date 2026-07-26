## Context

CTB Admin is a Django-based garment/fashion/bag business management system. Its user documentation site is built with MkDocs Material across 103 Markdown files grouped into 10 modules (`00-getting-started` through `09-reference`).

An audit against `.github/STYLE_SPEC.md` and third-party evaluation revealed structural drift, light operational procedural depth, boilerplate template errors on reference pages, and lack of cross-workflow navigational links.

## Goals / Non-Goals

**Goals:**

- Standardise canonical section structure across all 103 user-guide documentation files.
- Deepen procedural operational details (Prerequisites, Definition of Done, Validation Rules, Error Recovery) using Dual-MCP verification (`github-mcp-server` and `ctb-staging-mcp-server`).
- Overhaul `09-reference/` pages (`glossary.md`, `error-pages.md`, `offline-mode.md`, `permissions.md`, `troubleshooting.md`) with authoritative failure catalogues and remediation matrices.
- Embed explicit upstream/downstream contextual links across trade, employee, factory, and financial workflows.
- Inject standardized metadata headers into all documentation files.

**Non-Goals:**

- Modifying Django backend application code or database schemas.
- Changing MkDocs theme CSS or custom HTML overrides unless required for navigation search tags.
- Documenting internal developer APIs or server infrastructure.

## Decisions

### Decision 1: Phase-by-Module Agent Dispatch with Dual-MCP Verification

**Rationale:** Updating 103 files in scoped module batches (`03-trade`, `04-employee`, `02-factory`, `05-returns`, `09-reference`, etc.) using dedicated AI documentation agents (`doc-standardizer`, `doc-updater`, `doc-writer`) prevents unmanageable diffs and allows strict pre-commit verification. Every operational claim is verified against Django source code (`github-mcp-server`) and staging DOM forms (`ctb-staging-mcp-server`).

**Alternatives Considered:** A single massive regex/bulk edit script (rejected because it cannot write domain-accurate operational logic or contextual workflow descriptions).

### Decision 2: Strict Canonical 9-Section Header Standardisation

**Rationale:** Every task and reference page MUST implement the exact canonical H2 heading layout defined in `STYLE_SPEC.md` §3 (`Summary`, `When to use this page`, `How to access this page`, `Prerequisites & Role Permissions`, `Step-by-step instructions`, `Verification & Definition of Done`, `Field reference`, `Exception Handling & Error Recovery`, `Related Workflows & Next Steps`).

**Alternatives Considered:** Allowing module-specific custom H2 headings (rejected because it fragments navigation and breaks automated `style_lint.py` structural checks).

### Decision 3: Multi-Tiered Failure Recovery & Operational Matrices

**Rationale:** Transforming light text lists into structured pipe tables with standard headers (`Symptom` | `Root Cause` | `User Remediation Step` | `Role Required`) gives staff immediate operational clarity when errors occur.

**Alternatives Considered:** Generic troubleshooting paragraphs (rejected because non-technical staff require clear diagnostic tables).

## Risks / Trade-offs

- **[Risk]** Bulk modifications across 103 Markdown files could introduce relative link breakage or style lint failures.
    - **Mitigation:** Execute `python3 scripts/style_lint.py` and `uv run mkdocs build --strict` after processing each module.
- **[Risk]** Staging environment unavailability could block Dual-MCP UI verification.
    - **Mitigation:** Fall back to Django model/view code inspection via `github-mcp-server` and set `staging_verified: false` in file metadata until live DOM testing is performed.
