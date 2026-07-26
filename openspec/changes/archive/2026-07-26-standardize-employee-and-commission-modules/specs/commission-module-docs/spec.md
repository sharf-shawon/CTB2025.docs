## ADDED Requirements

### Requirement: Commission module documentation structure standardization

All documentation pages in `docs/user-guide/06-commission/` SHALL strictly adhere to the canonical 9-section template defined in `STYLE_SPEC.md` v2.0.

#### Scenario: Verify commission page heading hierarchy and order

- **WHEN** any page in `docs/user-guide/06-commission/` is inspected or linted
- **THEN** it SHALL contain all 9 mandatory canonical sections in exact order from `Summary` through `Related Workflows & Next Steps`.

### Requirement: Commission analytics and campaign field verification

Field reference tables across commission campaigns, bonus structures, analytics, and payment history pages SHALL include exact field labels, required flags, and backend validation constraints verified against backend models and staging UI.

#### Scenario: Verify commission campaign field tables

- **WHEN** inspecting the field reference table on a commission module page
- **THEN** every visible input field SHALL be documented with its required status, user action, and validation rules.

### Requirement: Commission error recovery matrices

Every commission documentation page SHALL include an `Exception Handling & Error Recovery` table.

#### Scenario: Verify commission troubleshooting table existence

- **WHEN** viewing a commission documentation page
- **THEN** it SHALL present a table mapping common failure symptoms to root causes and step-by-step resolution actions.
