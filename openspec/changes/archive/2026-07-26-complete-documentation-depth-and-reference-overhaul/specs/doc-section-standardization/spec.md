## ADDED Requirements

### Requirement: Documentation pages SHALL conform to canonical section headers

All user-guide documentation files in `docs/user-guide/` SHALL include the mandatory 9 H2 section headers in canonical order as specified in `STYLE_SPEC.md` §3.

#### Scenario: Validating canonical H2 headers

- **WHEN** `python3 scripts/style_lint.py` audits any page in `docs/user-guide/`
- **THEN** it confirms the presence of `Summary`, `When to use this page`, `How to access this page`, `Prerequisites & Role Permissions`, `Step-by-step instructions`, `Verification & Definition of Done`, `Field reference`, `Exception Handling & Error Recovery`, and `Related Workflows & Next Steps` in exact sequential order without skipped levels.

### Requirement: Documentation pages SHALL carry metadata headers

Every documentation file in `docs/user-guide/` SHALL include an inline HTML metadata comment block immediately below the H1 title.

#### Scenario: Inspecting page metadata header

- **WHEN** an agent or lint script parses a page in `docs/user-guide/`
- **THEN** it finds a valid `<!-- metadata: owner: <role>, last_updated: <YYYY-MM-DD>, git_ref: <sha>, staging_verified: <true|false> -->` comment.

### Requirement: Reference documentation SHALL NOT contain template form instructions

Reference pages in `docs/user-guide/09-reference/` SHALL NOT contain copy-paste boilerplate text or form editing steps.

#### Scenario: Auditing reference page step-by-step instructions

- **WHEN** `docs/user-guide/09-reference/glossary.md` or `error-pages.md` is inspected
- **THEN** it contains specific lookup/remediation procedures rather than generic "Complete the Terms section... save the record" instructions.
