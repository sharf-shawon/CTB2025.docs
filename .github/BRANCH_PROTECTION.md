# Branch Protection Baseline

This runbook defines recommended GitHub branch protections for `main`.

## Required Rules

1. Require a pull request before merging.
2. Require at least 1 approving review.
3. Dismiss stale approvals when new commits are pushed.
4. Require status checks to pass before merging.
5. Require branches to be up to date before merging.
6. Restrict force pushes and branch deletion.
7. Enforce CODEOWNERS review for docs governance paths.

## Required Status Checks

- Docs CI

## Recommended Additional Controls

- Require conversation resolution before merge.
- Restrict who can push directly to `main`.
- Enable secret scanning and push protection on the repository.
- Enable Dependabot security updates.

## Notes

- `Docs Deploy` should run only from trusted branches.
- The repository is public; keep Actions permissions least-privilege.
- For policy exceptions, document rationale in the PR description.
