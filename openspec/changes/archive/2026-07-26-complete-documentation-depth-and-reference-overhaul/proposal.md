## Why

The third-party documentation assessment and internal `doc-auditor` evaluation revealed that while the CTB Admin documentation system has strong information architecture (9.3/10) and purpose clarity (9.5/10), it suffers from lower content depth (7.0/10), reference quality (7.2/10), and maintainability signals (7.1/10). Critical operational details—such as definition of done, verification steps, role permissions, failure recovery matrices, and cross-workflow links—are absent or incomplete across module pages and reference docs.

Elevating the documentation from a well-structured index into an authoritative operational reference manual requires expanding procedural depth, eliminating template copy-paste bugs, overhauling reference pages, and building dense cross-workflow link graphs.

## What Changes

- **Canonical Structure Standardisation**: Enforce strict adherence to `.github/STYLE_SPEC.md` canonical section headers across all 103 user-guide documentation files (adding `Prerequisites & Role Permissions`, `Verification & Definition of Done`, `Exception Handling & Error Recovery`, and `Related Workflows & Next Steps`).
- **Operational & Procedural Deepening**: Deepen task-oriented guides across core business modules (`03-trade`, `04-employee`, `02-factory`, `05-returns`, `06-commission`, `07-reports`, `08-settings-and-admin`) using Dual-MCP verification (`github-mcp-server` for Django backend logic and `ctb-staging-mcp-server` for live DOM form fields/screenshots).
- **Reference Section Overhaul**: Rewrite `09-reference/` pages (`glossary.md`, `error-pages.md`, `offline-mode.md`, `permissions.md`, `troubleshooting.md`), removing copy-paste form instructions and introducing comprehensive error catalogues, role permission matrices, and failure recovery steps.
- **Cross-Workflow Link Graph**: Establish dense contextual cross-linking between upstream and downstream business processes (e.g., Invoice creation linking directly to Payment recording, Check tracking, Voucher entries, and Client balance reports).
- **Metadata & Trust Infrastructure**: Inject standardized HTML comment metadata blocks (`owner`, `last_updated`, `git_ref`, `staging_verified`) into all user-guide documentation files.

## Capabilities

### New Capabilities

- `doc-section-standardization`: Mandates and validates canonical section structure, frontmatter metadata, and boilerplate-free reference content across all MkDocs pages.
- `operational-depth-expansion`: Integrates verified Django backend logic, validation rules, superuser permission gates, and explicit verification steps into module procedural guides.
- `reference-recovery-system`: Provides comprehensive error catalogues, step-by-step failure remediation procedures, and expanded glossary/offline operational reference pages.
- `workflow-interlinking-graph`: Maps and enforces explicit upstream/downstream cross-links between trade, employee, factory, and financial operations pages.

### Modified Capabilities

*None.*

## Impact

- All 103 Markdown documentation files under `docs/user-guide/`.
- `mkdocs.yml` navigation, redirects, and search configuration.
- CI quality gate scripts (`scripts/style_lint.py`, `mkdocs build --strict`, `pre-commit`).
