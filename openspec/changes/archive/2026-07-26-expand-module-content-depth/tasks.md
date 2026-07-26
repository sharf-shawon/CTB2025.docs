## 1. Trade Module Operational & Error Recovery Expansion

- [x] 1.1 Inspect backend model & form definitions for Trade (`create-invoice.md`, `add-payment.md`, `add-voucher.md`) via `github-mcp-server`.
- [x] 1.2 Update `docs/user-guide/03-trade/invoices/create-invoice.md` with complete step-by-step UI task instructions, field catalog table, required permissions, and troubleshooting section.
- [x] 1.3 Update `docs/user-guide/03-trade/payments/add-payment.md` and `vouchers/add-voucher.md` with field validation constraints and voucher posting recovery procedures.

## 2. Business Module Field Validation & Workflow Depth

- [x] 2.1 Cross-reference Django models and staging UI for `add-client.md` and `add-vendor.md`.
- [x] 2.2 Standardize `docs/user-guide/01-business/clients/add-client.md` and `vendors/add-vendor.md` with full form parameter schemas and domain error resolution steps.

## 3. Employee & Factory Module Content Enhancement

- [x] 3.1 Inspect employee salary calculation, attendance model, and factory production order models.
- [x] 3.2 Update `docs/user-guide/04-employee/payroll/generate-salary.md` and `attendance/record-attendance.md` with operational step-by-step procedures, role callouts, and batch error recovery.
- [x] 3.3 Update `docs/user-guide/02-factory/products/add-product.md` with material allocation constraints and status lifecycle error handling.

## 4. Quality Verification & Linter Audit

- [x] 4.1 Run `python3 scripts/style_lint.py` to verify zero structural, section heading, or formatting errors.
- [x] 4.2 Run `uv run mkdocs build --strict` to verify site compilation and internal link integrity.
