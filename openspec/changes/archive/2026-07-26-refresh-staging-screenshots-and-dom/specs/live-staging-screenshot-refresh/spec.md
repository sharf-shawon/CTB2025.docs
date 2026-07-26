## ADDED Requirements

### Requirement: Live Staging UI Screenshot Capture

The documentation asset library SHALL maintain up-to-date visual screenshots captured directly from the live CTB Admin staging environment (`staging.ctbinfo.com`).

#### Scenario: User views form documentation with UI graphics

- **WHEN** a user views a task guide containing embedded screenshots
- **THEN** the documentation MUST display high-resolution UI captures reflecting the active Unfold admin theme layout without placeholder markers.

### Requirement: Image Asset Directory Normalization

All visual documentation screenshots SHALL be stored in dedicated module subdirectories under `docs/user-guide/screenshots/<module>/` with standard kebab-case naming.

#### Scenario: Linter checks image references

- **WHEN** `style_lint.py` or `mkdocs build --strict` runs on documentation pages
- **THEN** all image references MUST resolve to existing image files in the correct module screenshot folder.
