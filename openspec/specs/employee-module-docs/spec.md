# employee-module-docs Specification

## Purpose

TBD - created by archiving change standardize-employee-and-commission-modules. Update Purpose after archive.

## Requirements

### Requirement: Employee module documentation structure standardization

All documentation pages in `docs/user-guide/04-employee/` SHALL strictly adhere to the canonical 9-section template defined in `STYLE_SPEC.md` v2.0.

#### Scenario: Verify page heading hierarchy and order

- **WHEN** any page in `docs/user-guide/04-employee/` is inspected or linted
- **THEN** it SHALL contain all 9 mandatory canonical sections in exact order from `Summary` through `Related Workflows & Next Steps`.

### Requirement: Employee field reference dual-MCP verification

Field reference tables across employee, department, position, wage, attendance, payout, and salary pages SHALL include exact field labels, required flags, and backend validation constraints verified against backend models and staging UI.

#### Scenario: Verify employee page field tables

- **WHEN** inspecting the field reference table on an employee module page
- **THEN** every visible input field SHALL be documented with its required status, user action, and validation rules.

### Requirement: Employee error recovery matrices

Every employee documentation page SHALL include an `Exception Handling & Error Recovery` table.

#### Scenario: Verify troubleshooting table existence

- **WHEN** viewing an employee documentation page
- **THEN** it SHALL present a table mapping common failure symptoms to root causes and step-by-step resolution actions.
