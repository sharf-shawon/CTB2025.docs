# Consolidated Release Checklist

Use this checklist as the single source of truth before every documentation production release.

## Environment and dependencies

- [ ] Confirm `uv` is installed and available on CI and local maintainer machines.
- [ ] Run `uv sync --extra dev` from the repository root.
- [ ] Confirm `.venv` is created and tool versions resolve correctly.

## Build and quality gates

- [ ] Run `uv run mkdocs build --strict` with zero warnings.
- [ ] Run `uv run pre-commit run --all-files` with all checks passing.
- [ ] Confirm no unresolved conflict markers or trailing whitespace.

## Naming and structure consistency

- [ ] Ensure root project documentation file uses canonical `README.md` naming.
- [ ] Ensure documentation page filenames are lowercase kebab-case.
- [ ] Ensure each page H1 matches file intent (`Add`, `Edit`, `Detail`, `Overview`, `Create`, `Print`, `Generate`, `Record`).
- [ ] Ensure module folder prefixes remain consistent (`00` through `06`).

## Navigation and coverage

- [ ] Confirm every user-facing page is represented in `mkdocs.yml` navigation.
- [ ] Confirm intentionally excluded files are listed under `exclude_docs`.
- [ ] Confirm there are no missing nav targets.
- [ ] Confirm category and gallery pages render correctly.

## Content and media

- [ ] Verify screenshot links resolve from each module page.
- [ ] Verify terminology remains consistent with CTB Admin module language.
- [ ] Verify related pages sections point to valid existing docs.
- [ ] Verify no placeholder TODO comments remain for release-critical pages.

## Deployment readiness

- [ ] Confirm required environment variables are configured in deployment environment.
- [ ] Confirm CI workflows for docs build and deploy are green on `main`.
- [ ] Confirm published site URL and key module entry points load successfully.

## Post-release validation

- [ ] Review analytics and user feedback for broken or confusing pages.
- [ ] Open follow-up issues for non-blocking improvements.
- [ ] Update release notes and next iteration checklist.
