## ADDED Requirements

### Requirement: Task documentation SHALL include explicit upstream and downstream workflow links

Every procedural task page SHALL include a `Related Workflows & Next Steps` section containing Markdown links with explicit context explaining upstream prerequisites and downstream next steps.

#### Scenario: Navigating from Invoice Creation to Payment

- **WHEN** a user finishes reading `docs/user-guide/03-trade/invoices/create-invoice.md`
- **THEN** `Related Workflows & Next Steps` provides direct links to `add-payment.md`, `print-chalan.md`, and `invoice-reports.md` with explanatory notes for each link.

### Requirement: Site navigation and tags SHALL optimize task and field search discoverability

Page frontmatter tags (`module:`, `task:`, `role:`) and inline keywords SHALL be structured to support direct search lookup of task phrases and field names in MkDocs search.

#### Scenario: Searching for a task phrase or error message

- **WHEN** a user types a common field name or error phrase into the MkDocs top search bar
- **THEN** MkDocs search suggests the exact target documentation page containing that field or workflow.
