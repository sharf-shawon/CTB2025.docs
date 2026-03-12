# CTB Admin Knowledge Base

## Modules

| Module prefix | Sidebar label | Django apps (approx.) |
|---------------|---------------|----------------------|
| `01-business` | Business | clients, vendors, invoices, payments |
| `02-factory` | Factory | production orders, materials, costing |
| `03-trade` | Trade | purchase orders, import tracking |
| `04-employee` | Employee | staff, attendance, salary, payroll |
| `05-settings-and-admin` | Settings / Admin | users, roles, site config |
| `06-reference` | Reference | glossary, shortcuts, FAQs |

## Terminology

| Term used in docs | Meaning |
|-------------------|---------|
| Client | A customer account that places orders and receives invoices |
| Vendor | A supplier or service provider |
| Production Order | A factory job linked to a client order |
| Invoice | A billing document sent to a client |
| Payment | A recorded receipt against an invoice |
| Salary | A staff member's monthly compensation record |
| Payroll | Bulk salary generation for a pay period |

## Key Workflows

- **Client onboarding:** Add Client → set balance info → link to invoices
- **Invoicing:** Create Invoice → add line items → mark as Paid when payment received
- **Production:** Create Production Order → assign materials → track progress
- **Payroll:** Add Employee → record attendance → Generate Salary → export payslip
- **Reporting:** Use report pages under each module for filtered summaries

## UI Conventions

- Navigation is via the left sidebar in Django Admin (Unfold theme).
- Each module section collapses and expands.
- "Add" buttons are top-right on list pages.
- "Save" and "Save and continue editing" are at the bottom of every form.
- Required fields are marked with an asterisk (*).

## Screenshot Paths

Screenshots live under `docs/user-guide/screenshots/` with subfolders:

```
screenshots/
├── auth/
├── business/
├── dashboard/
├── employee/
├── factory/
├── settings/
└── trade/
```

Reference images with a relative path from the docs page, e.g.:
`../screenshots/business/add-client.png`

## Docs File Locations

```
docs/user-guide/
├── 00-getting-started/
├── 01-business/
├── 02-factory/
├── 03-trade/
├── 04-employee/
├── 05-settings-and-admin/
└── 06-reference/
```

Every new page must also be added to the `nav` section of `mkdocs.yml`.
