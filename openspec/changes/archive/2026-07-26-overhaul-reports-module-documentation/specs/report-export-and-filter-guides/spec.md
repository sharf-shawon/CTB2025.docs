## ADDED Requirements

### Requirement: Structured Exception Handling Matrix

All report pages SHALL include an `## Exception handling & error recovery` section featuring a 4-column matrix for common reporting edge cases.

#### Scenario: Report returns zero results or calculation discrepancy

- **WHEN** a report yields no matching rows or a balance discrepancy
- **THEN** the error recovery matrix MUST provide explicit remediation steps and actionable role requirements.

### Requirement: Export and Filter Procedure Guidelines

Report pages SHALL document exact step-by-step procedures for date range filtering, client/product filtering, and PDF/Print export operations.

#### Scenario: User exports report to PDF

- **WHEN** a user follows instructions to export or print a report
- **THEN** the step-by-step guide MUST outline exact filter application and print button interactions.
