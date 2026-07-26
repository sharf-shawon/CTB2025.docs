## Context

The repository includes a custom style linter (`scripts/style_lint.py`) and MkDocs configuration (`mkdocs.yml`). Currently, developer workflow relies on manual execution of linting commands. Creating automated GitHub Actions CI workflows ensures quality gates are enforced automatically on all pull requests and commits.

## Goals / Non-Goals

**Goals:**

- Create `.github/workflows/docs-style-check.yml` to run `python3 scripts/style_lint.py` and `uv run mkdocs build --strict` on PRs and pushes to `main`.
- Integrate pre-commit hooks in `.pre-commit-config.yaml` to run local style checks before commit creation.
- Ensure fast CI execution (< 1 minute) using `uv` dependency caching.

**Non-Goals:**

- Deploying documentation HTML to production servers (handled by separate deployment workflows).
- Modifying `style_lint.py` rules or `STYLE_SPEC.md` definitions.

## Decisions

### 1. CI Framework: GitHub Actions with `astral-sh/setup-uv`

- **Decision**: Use GitHub Actions with `astral-sh/setup-uv` action to manage Python environment and UV package caching.
- **Rationale**: Provides lightning-fast dependency installation (< 5 seconds) and native execution of `uv run mkdocs build --strict`.
- **Alternatives Considered**: Standard `setup-python` with `pip install`, which is significantly slower (30+ seconds per run).

### 2. Pre-Commit Integration: Local Repo Hook Configuration

- **Decision**: Configure a `repo: local` entry in `.pre-commit-config.yaml` executing `python3 scripts/style_lint.py` on modified `.md` files.
- **Rationale**: Catches style violations locally before developers push code, reducing CI iteration cycles.
- **Alternatives Considered**: Relying solely on remote CI checks, which causes delays when small syntax errors are pushed.

## Risks / Trade-offs

- **[Risk]** CI build failure if an external dependency update breaks MkDocs plugins.
    - **Mitigation**: Lock dependency versions in `pyproject.toml` and `uv.lock`.
- **[Risk]** Developer workstation missing `pre-commit` binary.
    - **Mitigation**: Provide clear initialization documentation in `AGENTS.md` and fallback to GitHub Actions remote enforcement.
