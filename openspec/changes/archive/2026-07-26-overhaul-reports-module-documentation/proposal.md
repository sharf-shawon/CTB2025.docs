## Why

The **Reports** module (`07-reports/`) contains crucial executive dashboards, attendance tallies, and product return analytics. However, the existing pages lack standardized 9-section canonical structure (`STYLE_SPEC.md` v2.0), missing structured verification steps and explicit role-based filter instructions.

Standardizing and expanding the Reports module ensures accounts, HR managers, and executives can reliably generate, audit, and export operational business reports.

## What Changes

- **9-Section Structural Standardization**: Update all pages in `docs/user-guide/07-reports/` to follow canonical `STYLE_SPEC.md` section structure (`## Summary`, `## When to use this page`, `## How to access this page`, `## Prerequisites`, `## Step-by-step instructions`, `## Verification & definition of done`, `## Field reference`, `## Exception handling & error recovery`, `## Related workflows & next steps`, `## Related pages`).
- **Filter & Export Operational Guides**: Add explicit step-by-step instructions for date range filtering, print/PDF export, and summary metric reconciliation.
- **Error Recovery Matrices**: Add structured tables detailing common reporting edge cases (e.g. zero transaction results, timezone shifts, unposted draft items).

## Capabilities

### New Capabilities

- `reports-procedural-standardization`: Full 9-section canonical standardization across Executive Summary, Monthly Attendance, and Product Return reports.
- `report-export-and-filter-guides`: Operational guidelines for multi-filter queries, export procedures, and balance verification.

### Modified Capabilities

*(None)*

## Impact

- **Documentation Pages**: Modifies all Markdown pages in `docs/user-guide/07-reports/`.
- **Quality Assurance**: Verified via `python3 scripts/style_lint.py` and `uv run mkdocs build --strict`.
