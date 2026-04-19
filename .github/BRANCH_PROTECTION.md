# Branch Protection Baseline

This runbook defines recommended GitHub branch protections for `main`.

## Required Rules

1. Require a pull request before merging.
1. Require at least 1 approving review.
1. Dismiss stale approvals when new commits are pushed.
1. Require status checks to pass before merging.
1. Require branches to be up to date before merging.
1. Restrict force pushes and branch deletion.
1. Enforce CODEOWNERS review for docs governance paths.

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
