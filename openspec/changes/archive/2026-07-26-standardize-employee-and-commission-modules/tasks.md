## 1. Employee Module Standardization

- [x] 1.1 Standardize `04-employee/employees/` pages (`add-employee.md`, `edit-employee.md`, `employee-detail.md`, `overview.md`) to 9-section template with dual-MCP verified fields and error handling tables.
- [x] 1.2 Standardize `04-employee/departments/` and `04-employee/positions/` pages to canonical 9-section structure.
- [x] 1.3 Standardize `04-employee/attendance/`, `04-employee/wages/`, `04-employee/salary/`, and `04-employee/payouts/` pages to canonical 9-section structure.
- [x] 1.4 Standardize `04-employee/purchase-balance/` and `04-employee/tasks/` pages to canonical 9-section structure.

## 2. Commission Module Standardization

- [x] 2.1 Standardize `06-commission/commission-campaigns.md` and `06-commission/client-bonus-campaigns.md` to 9-section template.
- [x] 2.2 Standardize `06-commission/employee-analytics.md`, `06-commission/client-bonus-analytics.md`, `06-commission/manager-analytics.md`, and `06-commission/payment-history.md` to 9-section template.

## 3. Verification & Quality Assurance

- [x] 3.1 Run `uv run pre-commit run --all-files` to ensure zero style specification or formatting linter regressions.
- [x] 3.2 Run `uv run mkdocs build --strict` to verify site build and link integrity.
