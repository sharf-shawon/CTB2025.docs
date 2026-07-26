## ADDED Requirements

### Requirement: Automated Style Linter GitHub Action

The CI pipeline SHALL run `python3 scripts/style_lint.py` on all pull requests and pushes targeting the main branch.

#### Scenario: Pull request submitted with style violations

- **WHEN** a pull request containing non-canonical H2 headings or prohibited terminology is opened
- **THEN** the `docs-style-check.yml` workflow MUST fail and output specific line-level error details.

### Requirement: Local Pre-Commit Hook Integration

The local git environment SHALL support pre-commit hooks that execute `style_lint.py` on staged markdown files prior to commit creation.

#### Scenario: Developer commits staged markdown files locally

- **WHEN** a developer runs `git commit` with staged `.md` files
- **THEN** the local pre-commit hook MUST run `scripts/style_lint.py` and abort the commit if violations are detected.
