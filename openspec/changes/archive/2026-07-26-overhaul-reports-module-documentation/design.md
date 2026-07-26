## Context

The `07-reports/` module provides essential management summaries (Executive Summary, Monthly Attendance Report, Product Return Report). While basic instructions exist, the pages lack canonical 9-section structure, explicit verification steps, and error recovery matrices.

## Goals / Non-Goals

**Goals:**

- Rewrite all 3 pages in `docs/user-guide/07-reports/` to conform strictly to `STYLE_SPEC.md` v2.0 9-section structure.
- Add explicit step-by-step filter configuration, export procedures, and calculation formulas.
- Add structured Exception Handling & Error Recovery matrices detailing zero-result handling, timezone shifts, and balance discrepancies.

**Non-Goals:**

- Modifying underlying backend Django reporting views or SQL queries in `CTB2025`.
- Creating new report pages that do not currently exist in the software application.

## Decisions

### 1. Section Header Standardization

- **Decision**: Update all report pages to use exact 9 H2 headings:
    - `## Summary`
    - `## When to use this page`
    - `## How to access this page`
    - `## Prerequisites`
    - `## Step-by-step instructions`
    - `## Verification & definition of done`
    - `## Field reference`
    - `## Exception handling & error recovery`
    - `## Related workflows & next steps`
    - `## Related pages`
- **Rationale**: Ensures total consistency across all modules in the documentation suite.
- **Alternatives Considered**: Retaining legacy 6-section layout, which fails `style_lint.py` checks.

### 2. Error Recovery Matrix Structure

- **Decision**: Provide 4-column Markdown tables (`Error Code / Symptom / Step-by-step remediation procedure / Actionable role required`).
- **Rationale**: Gives accountants and HR managers unambiguous troubleshooting steps when reports return unexpected numbers or fail to render.

## Risks / Trade-offs

- **[Risk]** Missing or invalid screenshot image paths causing lint errors.
    - **Mitigation**: Ensure all image references use valid relative paths to existing screenshots in `screenshots/reports/` or `gallery/Reports/`.
