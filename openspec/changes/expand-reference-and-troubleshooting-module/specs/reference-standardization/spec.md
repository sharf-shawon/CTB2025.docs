## ADDED Requirements

### Requirement: 9-Section Canonical Reference Documentation

All Markdown pages in `09-reference/` SHALL contain the exact 9 canonical H2 headings defined in `STYLE_SPEC.md` v2.0.

#### Scenario: Linter checks reference module pages

- **WHEN** `python3 scripts/style_lint.py` inspects files in `docs/user-guide/09-reference/`
- **THEN** all files MUST pass with zero heading structure or terminology violations.

### Requirement: Common Error Diagnostic Matrix

The system error page documentation SHALL include a detailed matrix mapping HTTP status codes to root causes and remediation procedures.

#### Scenario: Operator encounters a server error

- **WHEN** a user receives a 500 Internal Server Error screen
- **THEN** the error page documentation MUST define the root causes and outline explicit role-based recovery steps.
