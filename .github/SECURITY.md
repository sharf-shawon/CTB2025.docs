# Security Policy

## Supported Scope

This repository hosts public documentation for CTB Admin.

In-scope items:

- GitHub Actions workflows in `.github/workflows/`
- Documentation build and deployment configuration (`mkdocs.yml`, `pyproject.toml`)
- Documentation source in `docs/`
- Automation and agent governance files in `.github/`

Out-of-scope items:

- The private CTB2025 application source repository
- Application runtime vulnerabilities that cannot be reproduced in this documentation repository

## Reporting a Vulnerability

Do not open a public issue for security findings.

Report vulnerabilities privately by emailing: security@ctbinfo.com

Include:

- A short summary
- Reproduction steps
- Affected file paths and workflow names
- Impact assessment
- Suggested mitigation if available

## Response Targets

- Initial acknowledgment: within 3 business days
- Triage and severity assessment: within 7 business days
- Remediation plan: communicated after triage based on severity

## Disclosure Policy

- Coordinated disclosure is required.
- We will notify reporters when fixes are deployed.
- Public disclosure should happen only after the fix is available and validated.

## Hardening Baseline

- Least-privilege GitHub Actions permissions
- Required CI checks on pull requests
- Locked dependency graph via `uv.lock`
- Pre-commit quality gates for all changes
