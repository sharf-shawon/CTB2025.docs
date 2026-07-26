## Why

The `04-employee` and `06-commission` documentation modules contain legacy heading structures, missing canonical 9-section requirements (such as explicit role permissions, verification / definition of done, and exception handling tables), and non-standard field references. Standardizing these modules guarantees alignment with `STYLE_SPEC.md` v2.0 and enforces full zero-hallucination compliance across all HR, payroll, attendance, and commission management workflows.

## What Changes

- Re-structure and standardize all Markdown pages in `docs/user-guide/04-employee/` and `docs/user-guide/06-commission/` according to the canonical 9-section structure.
- Add explicit `Prerequisites & Role Permissions` for every employee and commission page, mapping Django permissions (`hr`, `payroll`, `admin`).
- Expand `Field reference` tables with required flags, exact UI inputs, and backend validation constraints verified via dual-MCP checks.
- Add `Exception Handling & Error Recovery` tables mapping common user error symptoms to root causes and step-by-step remediations.
- Ensure strict formatting compliance (sentence case headings, valid MkDocs Material admonitions, active voice, bold UI elements).

## Capabilities

### New Capabilities

- `employee-module-docs`: Standardized 9-section documentation covering employee management, departments, positions, attendance, wages, payouts, and salary generation workflows.
- `commission-module-docs`: Standardized 9-section documentation covering commission campaigns, client bonus rules, employee commission analytics, and payment history.

### Modified Capabilities

<!-- None -->

## Impact

- `docs/user-guide/04-employee/**/*.md` documentation files
- `docs/user-guide/06-commission/**/*.md` documentation files
- `mkdocs.yml` nav alignment verification
