## 1. 9-Section Canonical Standardization

- [x] 1.1 Rewrite `app-settings.md` to full 9-section `STYLE_SPEC.md` standard including Maintenance Mode procedures and superuser bypass steps.
- [x] 1.2 Rewrite `audit-log.md` to full 9-section standard with security log filtering and action audit instructions.
- [x] 1.3 Rewrite `user-management.md` to full 9-section standard with complete Django permission codename mapping tables.

## 2. Admin Troubleshooting & Error Recovery Matrices

- [x] 2.1 Add 4-column Exception Handling & Error Recovery matrices across all modified admin module pages.
- [x] 2.2 Verify field reference tables and screenshot links across `08-settings-and-admin/`.

## 3. Linter & Site Build Verification

- [x] 3.1 Run `python3 scripts/style_lint.py` to confirm zero violations across modified admin files.
- [x] 3.2 Run `uv run mkdocs build --strict` to verify clean site compilation and image rendering.
