## Context

The initial structural cleanup and reference overhaul phase brought all 103 user-guide documentation files into 100% compliance with `.github/STYLE_SPEC.md` section templates and quality gates.

The next evolutionary phases focus on automation, image assets, continuous backend verification, and software release tag synchronization.

## Goals / Non-Goals

**Goals:**

- Build an automated screenshot pipeline using `ctb-staging-mcp-server` to capture and optimize staging UI screenshots.
- Implement continuous Dual-MCP validation checking Django models (`github-mcp-server`) and staging forms (`ctb-staging-mcp-server`) during pre-commit and CI.
- Automate release-note synchronization between software releases and documentation reference pages.
- Create an automated SME review checklist pipeline (`review/sme-checklist.md`).

**Non-Goals:**

- Modifying core Django application models or database schemas.
- Replacing MkDocs Material theme with custom themes.

## Decisions

### Decision 1: Staging Subagent Screenshot Automation

**Rationale:** Utilizing `ctb-staging-mcp-server` tools (`ctb_staging_screenshot`, `ctb_staging_browse`) inside browser subagents enables standardizing image resolutions, dark/light mode screenshots, and kebab-case file naming next to the documentation page referencing them.

**Alternatives Considered:** Manual browser screenshots (rejected due to inconsistent dimensions, formatting, and human effort).

### Decision 2: Automated Pre-Commit & CI Dual-MCP Verification

**Rationale:** Wiring Dual-MCP checks into CI ensures zero-hallucination guarantees for future documentation edits, catching field name drifts or deleted Django permission codenames before PR approval.

**Alternatives Considered:** Pure manual code review (rejected as drift-prone over time).

## Risks / Trade-offs

- **[Risk]** Staging environment network downtime could block automated screenshot generation.
    - **Mitigation:** Fallback to explicit `<!-- TODO: screenshot <filename>.png -->` comment placeholders with automated entries in `review/sme-checklist.md`.
