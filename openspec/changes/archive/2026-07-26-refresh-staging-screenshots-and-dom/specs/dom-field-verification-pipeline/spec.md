## ADDED Requirements

### Requirement: DOM Form Field Attribute Verification

Documentation field reference tables SHALL match the actual rendered DOM input attributes, label strings, select choices, and required flags on live staging form pages.

#### Scenario: User inspects form field specifications

- **WHEN** a user compares a documented Field Reference table against the live CTB Admin web page
- **THEN** field names, required indicators (`*`), and dropdown options MUST match the live DOM state exactly.

### Requirement: Zero Placeholder Screenshot Audit

Documentation pages SHALL NOT contain unrendered `<!-- TODO: screenshot ... -->` comments in published guides.

#### Scenario: Build pipeline audits markdown pages

- **WHEN** the documentation build pipeline executes
- **THEN** every documented procedure MUST either contain a valid screenshot link or explicit step instructions without broken comment stubs.
