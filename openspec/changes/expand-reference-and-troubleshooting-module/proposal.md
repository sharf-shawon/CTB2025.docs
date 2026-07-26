## Why

The **Reference** module (`09-reference/`) contains crucial operational guidelines such as offline mode behaviors and system error diagnostic steps. However, these files lack standardized H2 section architecture and explicit step-by-step technical verification procedures.

Standardizing and expanding the Reference and Troubleshooting guides ensures all users and technical staff can troubleshoot network disruptions, recover from application errors, and utilize keyboard shortcuts productively.

## What Changes

- **9-Section Structural Standardization**: Update all pages in `docs/user-guide/09-reference/` (`offline-mode.md`, `error-pages.md`) to the canonical `STYLE_SPEC.md` v2.0 section layout.
- **Offline & Offline Recovery Procedures**: Detail step-by-step instructions for verifying browser cache, auditing service worker offline status, and manual sync-conflict resolution.
- **Error Recovery Matrix Overhaul**: Add detailed exception handling tables for client-side and server-side HTTP errors.

## Capabilities

### New Capabilities

- `reference-standardization`: Canonical 9-section standardization across offline mode, system error screens, and glossary reference documents.
- `offline-recovery-procedures`: Operational procedures for Service Worker verification, IndexedDB checks, and offline data sync reconciliation.

### Modified Capabilities

*(None)*

## Impact

- **Documentation Pages**: Modifies all Markdown pages under `docs/user-guide/09-reference/`.
- **Quality Gates**: Verified using `python3 scripts/style_lint.py` and `uv run mkdocs build --strict`.
