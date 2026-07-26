## ADDED Requirements

### Requirement: Every documentation page SHALL include Prerequisites and Role Permissions

All user documentation pages MUST specify the required user permissions and prerequisite database records needed to execute the workflow.

#### Scenario: Documenting permission prerequisites

- **WHEN** a documentation page is written or updated
- **THEN** it SHALL contain a `## Prerequisites & Role Permissions` section listing explicit Django permission names and active record requirements

### Requirement: Every documentation page SHALL include Verification and Definition of Done

All task-oriented documentation pages MUST detail explicit steps to confirm successful task execution and verify state changes.

#### Scenario: Documenting verification steps

- **WHEN** a user completes a step-by-step instruction list on a doc page
- **THEN** the page SHALL contain a `## Verification & Definition of Done` section explaining status pill changes, auto-created downstream records, and ledger updates

### Requirement: Every documentation page SHALL include Exception Handling and Error Recovery

Documentation pages MUST contain a structured table detailing common error messages, root causes, and step-by-step remediation procedures.

#### Scenario: Documenting error recovery

- **WHEN** an operational error or validation failure can occur during a workflow
- **THEN** the documentation page SHALL include an `## Exception Handling & Error Recovery` section with error symptoms, causes, and recovery actions

### Requirement: Every documentation page SHALL include Freshness Metadata headers

Documentation files MUST include structured HTML comment metadata headers containing owner role, last updated date, git commit SHA, and staging verification status.

#### Scenario: Adding freshness signals to documentation header

- **WHEN** a documentation page is created or updated
- **THEN** the page header SHALL include `<!-- metadata: owner: <role>, last_updated: <YYYY-MM-DD>, git_ref: <sha>, staging_verified: true -->`
