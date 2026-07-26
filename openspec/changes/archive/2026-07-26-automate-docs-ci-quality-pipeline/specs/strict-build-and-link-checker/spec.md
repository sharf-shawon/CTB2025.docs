## ADDED Requirements

### Requirement: Strict MkDocs CI Build Execution

The CI pipeline SHALL run `uv run mkdocs build --strict` on all pull requests to verify full site compilation and internal link validity.

#### Scenario: Pull request introduces broken markdown links

- **WHEN** a pull request containing invalid relative file paths or broken links is submitted
- **THEN** the CI build step MUST fail with a non-zero exit code and report missing link targets.
