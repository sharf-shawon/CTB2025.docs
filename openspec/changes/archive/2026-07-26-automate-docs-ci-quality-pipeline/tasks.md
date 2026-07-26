## 1. GitHub Actions CI Workflow Setup

- [x] 1.1 Create `.github/workflows/docs-style-check.yml` configured to trigger on pull requests and pushes to `main`.
- [x] 1.2 Add jobs executing `python3 scripts/style_lint.py` and `uv run mkdocs build --strict` with `astral-sh/setup-uv` dependency caching.

## 2. Local Pre-Commit Hook Configuration & Guidance

- [x] 2.1 Update `.pre-commit-config.yaml` to include a local `style-lint` hook target.
- [x] 2.2 Update `AGENTS.md` and repository README notes with instructions for initializing pre-commit hooks locally.

## 3. Workflow Testing & Build Verification

- [x] 3.1 Verify pre-commit hook execution locally using `uv run pre-commit run --all-files`.
- [x] 3.2 Verify GitHub Actions workflow syntax using local linter/validation commands.
