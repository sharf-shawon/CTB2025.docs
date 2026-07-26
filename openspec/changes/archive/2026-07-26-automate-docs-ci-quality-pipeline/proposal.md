## Why

Currently, documentation style linting (`style_lint.py`) and strict build verification (`mkdocs build --strict`) are executed manually, leaving open the risk of accidental style regressions or broken internal links being merged into the main branch.

Automating these quality gates via a GitHub Actions CI workflow enforces continuous compliance with `STYLE_SPEC.md` v2.0 and guarantees zero broken links across all pull requests.

## What Changes

- **GitHub Actions Workflow Integration**: Create `.github/workflows/docs-style-check.yml` to automatically execute `style_lint.py` and `uv run mkdocs build --strict` on pull requests and pushes to `main`.
- **Pre-Commit Hook Configuration**: Ensure `.pre-commit-config.yaml` includes local pre-commit hooks for running style linting before commits are finalized.
- **CI Build Reporting**: Configure detailed summary outputs in GitHub Actions to pinpoint any style violations or missing link targets directly in PR checks.

## Capabilities

### New Capabilities

- `ci-style-lint-automation`: Automated GitHub Actions workflow executing `python3 scripts/style_lint.py` on pull requests to enforce `STYLE_SPEC.md` section structure.
- `strict-build-and-link-checker`: Automated CI build check running `uv run mkdocs build --strict` to prevent broken links or compilation errors from entering `main`.

### Modified Capabilities

*(None)*

## Impact

- **Infrastructure Files**: Adds `.github/workflows/docs-style-check.yml` and updates `.pre-commit-config.yaml`.
- **Pull Requests**: Rejects PRs that contain non-canonical H2 headings, terminology violations, or broken internal markdown links.
