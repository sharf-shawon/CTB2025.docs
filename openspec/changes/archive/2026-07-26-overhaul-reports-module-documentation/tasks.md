## 1. 9-Section Canonical Standardization

- [x] 1.1 Rewrite `executive-summary.md` to full 9-section `STYLE_SPEC.md` standard including `## Verification & definition of done` and `## Exception handling & error recovery`.
- [x] 1.2 Rewrite `attendance-report.md` to full 9-section standard with detailed day grid legend and summary column reconciliation rules.
- [x] 1.3 Rewrite `product-return-report.md` to full 9-section standard with client balance adjustment guidelines and return audit procedures.

## 2. Export & Troubleshooting Matrix Enhancements

- [x] 2.1 Add 4-column Exception Handling & Error Recovery matrices across all 3 report pages.
- [x] 2.2 Add explicit print/PDF export and date filter step-by-step procedures across all 3 report pages.

## 3. Linter & Site Build Verification

- [x] 3.1 Run `python3 scripts/style_lint.py` to confirm zero violations across modified report files.
- [x] 3.2 Run `uv run mkdocs build --strict` to verify clean site compilation and image rendering.
