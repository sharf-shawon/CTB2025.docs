![CTB Admin Cover](docs/assets/images/ctb-cover.png)

## CTB Admin - Documentation

## App Overview

CTB Admin is a Django-based **bag/garment/fashion business management system** with five functional modules, all served through a customized Django Admin (Unfold theme). The primary modules are: **Business** (Clients & Vendors), **Factory** (Products, Materials, Inventory), **Trade** (Invoices, Payments, Checks, Vouchers), **Employee** (HR, Attendance, Salary/Wage), and **core/config** (User accounts, settings, SMS).

______________________________________________________________________

## Developer Instructions

### Prerequisites

- [Install Python `3.13`](https://www.python.org/downloads/release/python-31312/)
- [install `uv`](https://docs.astral.sh/uv/getting-started/installation/)

### Setup

```bash
git commit https://github.com/sharf-shawon/CTB2025.docs.git
cd CTB2025.docs
uv sync --extra dev
uv run pre-commit install
```

### Enable virtual environment (venv) (optional, if needed)

Run the activation command in shell inside the project directory:

| Platform  | Shell          | Activation Command            |
| --------- | -------------- | ----------------------------- |
| Windows   | Command Prompt | venv\\Scripts\\activate.bat   |
| Windows   | PowerShell     | venv\\Scripts\\Activate.ps1   |
| Mac/Linux | bash / zsh     | source venv/bin/activate      |
| Mac/Linux | fish           | source venv/bin/activate.fish |
| Mac/Linux | csh / tcsh     | source venv/bin/activate.csh  |


### Run Locally

```bash
uv run mkdocs serve
```

Then open the local docs URL shown by MkDocs (usually `http://127.0.0.1:8000`).

### Build and Validate

```bash
uv run mkdocs build --strict
uv run pre-commit run --all-files
```

### Common Warning (Safe to Ignore)

If you see:

`VIRTUAL_ENV=... does not match the project environment path .venv`

it means another virtual environment is active in your shell. `uv` will still use this project's environment.
To silence that warning, run `deactivate` (or `unset VIRTUAL_ENV`) before running commands.

### CI and Deployment

- CI build + checks: `.github/workflows/docs-ci.yml`
- GitHub Pages deploy: `.github/workflows/docs-deploy.yml`

### Copilot Project Guidance

Repository-specific Copilot guidance is in `.github/copilot-instructions.md`.

______________________________________________________________________

## Suggested Docs Directory Structure

Place this under the existing `/docs` folder already in the repo:

```
docs/
└── user-guide/
    │
    ├── README.md                          ← Docs index / table of contents
    ├── screenshots/                       ← All screenshots organized by module
    │   ├── auth/
    │   ├── dashboard/
    │   ├── business/
    │   ├── factory/
    │   ├── trade/
    │   ├── employee/
    │   └── settings/
    │
    ├── 00-getting-started/
    │   ├── overview.md                    ← What is CTB Admin, who uses it
    │   ├── login-and-logout.md            ← Login page, social auth, logout
    │   └── dashboard.md                  ← Main admin dashboard overview
    │
    ├── 01-business/
    │   ├── README.md                      ← Module intro
    │   ├── clients/
    │   │   ├── overview.md               ← Client list page
    │   │   ├── add-client.md             ← Add new client form
    │   │   ├── edit-client.md            ← Edit existing client
    │   │   ├── client-detail.md          ← Client detail/profile view
    │   │   └── client-reports.md         ← Client report view (ClientReportView)
    │   └── vendors/
    │       ├── overview.md               ← Vendor list page
    │       ├── add-vendor.md
    │       ├── edit-vendor.md
    │       └── vendor-detail.md
    │
    ├── 02-factory/
    │   ├── README.md
    │   ├── categories/
    │   │   ├── overview.md               ← Product category list
    │   │   ├── add-category.md
    │   │   └── edit-category.md
    │   ├── materials/
    │   │   ├── overview.md               ← Raw materials list
    │   │   ├── add-material.md
    │   │   └── edit-material.md
    │   ├── material-inventory/
    │   │   ├── overview.md               ← Inventory list & stock levels
    │   │   └── add-inventory-entry.md   ← Log new stock-in / stock-out
    │   └── products/
    │       ├── overview.md               ← Product list with stock/SKU
    │       ├── add-product.md
    │       ├── edit-product.md
    │       └── product-detail.md         ← Product detail, stock, pricing
    │
    ├── 03-trade/
    │   ├── README.md
    │   ├── invoices/
    │   │   ├── overview.md               ← Invoice list, filters, status badges
    │   │   ├── create-invoice.md         ← Create invoice (with inline items)
    │   │   ├── create-tender-invoice.md  ← Create tender invoice (t-invoice)
    │   │   ├── create-quotation.md       ← Create quotation
    │   │   ├── edit-invoice.md
    │   │   ├── invoice-detail.md         ← Invoice detail view
    │   │   ├── print-invoice.md          ← Print/PDF invoice view
    │   │   ├── print-chalan.md           ← Print/PDF chalan (delivery doc)
    │   │   └── invoice-reports.md        ← Invoice analytics dashboard
    │   ├── payments/
    │   │   ├── overview.md               ← Payment list
    │   │   ├── add-payment.md
    │   │   └── payment-detail.md
    │   ├── checks/
    │   │   ├── overview.md               ← Cheque management list
    │   │   ├── add-check.md
    │   │   └── check-detail.md
    │   ├── vouchers/
    │   │   ├── overview.md               ← Voucher list
    │   │   ├── add-voucher.md
    │   │   └── voucher-detail.md
    │   └── banks/
    │       ├── overview.md               ← Bank accounts list
    │       ├── add-bank.md
    │       └── bank-detail.md
    │
    ├── 04-employee/
    │   ├── README.md
    │   ├── departments/
    │   │   ├── overview.md
    │   │   └── add-edit-department.md
    │   ├── positions/
    │   │   ├── overview.md
    │   │   └── add-edit-position.md
    │   ├── employees/
    │   │   ├── overview.md               ← Employee list, search, filter
    │   │   ├── add-employee.md
    │   │   ├── edit-employee.md
    │   │   └── employee-detail.md        ← Profile, dept, position, salary info
    │   ├── attendance/
    │   │   ├── overview.md               ← Attendance list/calendar view
    │   │   └── record-attendance.md      ← Mark attendance manually
    │   ├── salary/
    │   │   ├── overview.md               ← Salary records list
    │   │   ├── generate-salary.md        ← Monthly salary generation
    │   │   └── salary-detail.md
    │   ├── wages/
    │   │   ├── overview.md               ← Daily/hourly wage records
    │   │   └── add-wage-entry.md
    │   ├── payouts/
    │   │   ├── overview.md
    │   │   └── create-payout.md          ← Issue a payout/advance
    │   ├── tasks/
    │   │   ├── overview.md               ← Employee task list
    │   │   └── create-edit-task.md
    │   └── purchase-balance/
    │       └── overview.md               ← Employee purchase balance/ledger
    │
    ├── 05-settings-and-admin/
    │   ├── README.md
    │   ├── user-management.md            ← Add/edit system users, permissions
    │   ├── app-settings.md               ← Constance/runtime settings panel
    │   ├── sms-notifications.md          ← SMS configuration and logs
    │   └── maintenance-mode.md           ← Enabling/disabling maintenance mode
    │
    └── 06-reference/
        ├── error-pages.md                ← What 403, 404, 500 etc. mean to users
        ├── offline-mode.md               ← PWA offline page behavior
        └── glossary.md                   ← Key terms (Chalan, Voucher, t-invoice)
```

______________________________________________________________________

## Module-to-App Mapping for Sourav

This table maps each documentation section directly to its source Django app so Sourav knows exactly where to look in the running app.

| Docs Section                    | Django App           | Key Models           |
| ------------------------------- | -------------------- | -------------------- |
| `00-getting-started`            | `allauth` / `config` | User, SocialAccount  |
| `01-business/clients`           | `Business`           | Client, Notes        |
| `01-business/vendors`           | `Business`           | Vendor               |
| `02-factory/categories`         | `Factory`            | Category             |
| `02-factory/materials`          | `Factory`            | Material             |
| `02-factory/material-inventory` | `Factory`            | MaterialInventory    |
| `02-factory/products`           | `Factory`            | Product              |
| `03-trade/invoices`             | `Trade`              | Invoice, InvoiceItem |
| `03-trade/payments`             | `Trade`              | Payment              |
| `03-trade/checks`               | `Trade`              | Checks               |
| `03-trade/vouchers`             | `Trade`              | Voucher              |
| `03-trade/banks`                | `Trade`              | Bank                 |
| `04-employee/departments`       | `Employee`           | Department           |
| `04-employee/positions`         | `Employee`           | Position             |
| `04-employee/employees`         | `Employee`           | Employee             |
| `04-employee/attendance`        | `Employee`           | Attendance           |
| `04-employee/salary`            | `Employee`           | Salary               |
| `04-employee/wages`             | `Employee`           | Wage                 |
| `04-employee/payouts`           | `Employee`           | Payout               |
| `04-employee/tasks`             | `Employee`           | Task                 |
| `05-settings-and-admin`         | `config`             | User, Constance, SMS |

______________________________________________________________________

## Key Special Pages to Document

These are non-obvious pages that Sourav must not miss:

- **Invoice PDF / Print view** → `GET /trade/invoices/<id>/invoice/` — the rendered print-friendly invoice page
- **Chalan PDF view** → `GET /trade/invoices/<id>/chalan/` — delivery document without prices (only for `status=sent` invoices)
- **Invoice Analytics Dashboard** → Custom admin view `InvoiceReportView` (admin → Trade → Invoice Reports)
- **Client Report View** → `Business/views/ClientReportView.py` — client-specific financial report
- **PWA Offline page** → `templates/offline.html` — what users see when offline

<!-- - **Maintenance Mode page** → accessible via `/maintenance/` -->

- **Error pages** → `400`, `401`, `403`, `404`, `500`, `502`, `503`, `504` — document briefly what these mean and what the user should do

______________________________________________________________________

## Screenshot Reuse Strategy

Since the app uses a **consistent Unfold admin theme**, Sourav should:

- Capture **one screenshot of the standard list page layout** and reuse it across the same module. Annotate steps, clicks and/or actions consistantly accorss the project.
- Capture **one screenshot of the standard add/edit form layout** and reuse similarly.
- Must take screenshots for unique pages including (but not limited to): Invoice print view, Chalan print view, Invoice Analytics charts, and the Login page — as these are visually distinct.
