## Context

CTB Admin is a Django-based management system serving garment and fashion operations across Trade, Business, Factory, and Employee modules. While page navigation and basic UI overviews are documented, operational doc pages currently lack full parameter schemas, role-permission requirements, and actionable recovery protocols for common business error states.

To bring the documentation up to standard (`STYLE_SPEC.md` v2.0), we need a standardized content expansion pattern that integrates Dual-MCP source verification (`github-mcp-server` for Django backend models/forms and `ctb-staging-mcp-server` for live UI fields).

## Goals / Non-Goals

**Goals:**

- Implement standardized 9-section structure on all updated pages per `STYLE_SPEC.md`.
- Document explicit field validation rules, input constraints, required vs. optional indicators, and role permissions.
- Provide step-by-step UI task instructions for high-value workflows in Business, Factory, Trade, and Employee modules.
- Add structured operational troubleshooting and failure mode recovery procedures to key workflows.
- Validate zero style/heading violations using `python3 scripts/style_lint.py`.

**Non-Goals:**

- Modifying backend Django source code or changing CTB Admin UI layout.
- Adding interactive JS components to MkDocs output beyond standard Material features.

## Decisions

### 1. Verification Strategy: Dual-MCP Source Inspection

- **Decision**: Cross-reference Django backend models/forms via `github-mcp-server` (`sharf-shawon/CTB2025`) and verify live form layout using `ctb-staging-mcp-server`.
- **Rationale**: Guarantees zero-hallucination mandate for required form fields, field length limits, choices/enums, and Django permissions.
- **Alternatives Considered**: Manual inspection or relying solely on memory/comments, which risks documenting outdated or non-existent fields.

### 2. Module Target Selection: Prioritized High-Value Operational Pages

- **Decision**: Focus content depth expansion on primary transactional pages:
    - Trade (`create-invoice.md`, `add-payment.md`, `add-voucher.md`)
    - Business (`add-client.md`, `add-vendor.md`)
    - Employee (`add-employee.md`, `record-attendance.md`, `generate-salary.md`)
    - Factory (`production-orders.md`, `inventory-management.md`)
- **Rationale**: These core workflows represent 80%+ of user operational tasks and carry the highest support overhead when errors occur.
- **Alternatives Considered**: Broad, shallow updates to all 103 pages, which dilutes effort and delays high-impact operational documentation.

### 3. Error Recovery Structure: Standardized Troubleshooting Blocks

- **Decision**: Use a uniform format for operational errors: Diagnostic Symptom $\rightarrow$ Root Cause $\rightarrow$ Resolution Steps.
- **Rationale**: Allows users to quickly search for specific error messages or behavior and follow clear recovery steps.
- **Alternatives Considered**: Ad-hoc warning callouts embedded randomly in paragraphs, which reduces readability and search indexability.

## Risks / Trade-offs

- **[Risk]** Staging environment data or state might differ slightly from backend master schema.
    - **Mitigation**: Fallback to direct inspection of Django `models.py` and `forms.py` via `github-mcp-server` as the ultimate source of truth.
- **[Risk]** Expanding page depth could increase line counts and trigger linter structural warnings if H2 headings deviate.
    - **Mitigation**: Strictly follow the standard 9-section H2 schema mandated in `STYLE_SPEC.md` §3 and run `python3 scripts/style_lint.py`.
