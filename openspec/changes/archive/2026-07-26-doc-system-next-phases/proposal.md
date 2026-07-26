## Why

Having completed the foundational structural standardisation and reference section overhaul (achieving clean quality gates across 103 files), the CTB Admin documentation system requires continuous operational depth expansion, automated UI screenshot pipeline integration, and automated CI freshness/sync workflows for future product releases.

Establishing these next phases ensures that documentation remains synchronized with live Django software releases, automatically captures high-resolution UI screenshots, and maintains zero-hallucination operational accuracy.

## What Changes

- **Automated Screenshot Capture Pipeline**: Build an automated browser screenshot capture workflow using `ctb-staging-mcp-server` to replace `<!-- TODO: screenshot ... -->` placeholders with real, optimized WebP/PNG assets in `gallery.md` and module pages.
- **Continuous Dual-MCP Verification**: Implement pre-commit and CI verification hooks that validate form fields, permission codenames, and status transitions against Django backend models (`github-mcp-server`) and staging DOM forms (`ctb-staging-mcp-server`).
- **Release Notes & Version Linkage**: Create an automated changelog and release-note synchronization module connecting CTB Admin software release tags with documentation reference guides.
- **SME Review Pipeline**: Generate a machine-readable review queue (`review/sme-checklist.md`) tracking pending product verification items and unverified edge cases.

## Capabilities

### New Capabilities

- `automated-screenshot-pipeline`: Automated browser subagent screenshot capture and asset optimization for MkDocs gallery and inline docs.
- `continuous-mcp-verification`: Real-time Django model and live DOM form validation pipeline for documentation updates.
- `release-notes-linkage`: Automated release notes and version-tagged changelog synchronization for MkDocs Material.

### Modified Capabilities

*None.*

## Impact

- `docs/user-guide/` module pages and screenshot asset directories (`gallery/`, `overrides/`).
- `.github/workflows/` CI automation scripts.
- `scripts/` style and nav audit utilities.
