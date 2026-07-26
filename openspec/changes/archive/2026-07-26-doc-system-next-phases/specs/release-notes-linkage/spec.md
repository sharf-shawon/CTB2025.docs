## ADDED Requirements

### Requirement: System documentation SHALL link software release tags to reference release notes

The documentation site SHALL provide version-tagged release notes and link Git release tags directly to system reference guides.

#### Scenario: Linking software release to reference documentation

- **WHEN** a new release tag (e.g. `v2.5.0`) is published in `CTB2025`
- **THEN** the documentation build updates version badges and links release changelogs under `09-reference/README.md`.
