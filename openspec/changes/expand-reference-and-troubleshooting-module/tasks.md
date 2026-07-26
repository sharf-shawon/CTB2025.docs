## 1. 9-Section Canonical Standardization

- [x] 1.1 Rewrite `offline-mode.md` to full 9-section `STYLE_SPEC.md` standard including browser cache inspection guidelines.
- [x] 1.2 Rewrite `error-pages.md` to full 9-section standard with detailed HTTP diagnostic matrices.

## 2. Troubleshooting & Recovery Matrices

- [x] 2.1 Add 4-column Exception Handling & Error Recovery tables for synchronization failures and client/server network disruptions.
- [x] 2.2 Reconcile related links and cross-module page references.

## 3. Linter & Site Build Verification

- [x] 3.1 Run `python3 scripts/style_lint.py` to confirm zero violations across modified reference files.
- [x] 3.2 Run `uv run mkdocs build --strict` to verify clean site compilation and link resolution.
