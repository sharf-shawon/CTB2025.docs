## ADDED Requirements

### Requirement: 9-Section Canonical Report Structure

All Markdown pages in `07-reports/` SHALL contain the exact 9 canonical H2 headings defined in `STYLE_SPEC.md` v2.0.

#### Scenario: Linter checks report page structure

- **WHEN** `python3 scripts/style_lint.py` inspects pages in `docs/user-guide/07-reports/`
- **THEN** all pages MUST pass with zero heading structure or terminology violations.

### Requirement: Verification and Definition of Done Section

Every report page SHALL include a `## Verification & definition of done` section detailing exact steps to confirm report accuracy and data reconciliation.

#### Scenario: User verifies generated report output

- **WHEN** a user generates an Executive Summary or Attendance Report
- **THEN** the documentation MUST explain how to reconcile output totals against underlying invoice or attendance ledger records.
