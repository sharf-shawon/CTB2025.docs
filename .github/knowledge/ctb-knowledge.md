# CTB Admin Knowledge Base

This file is a compact, high-signal knowledge base for Copilot agents working on CTB Admin documentation.
Each entry below is a **single, self-contained line** so agents can scan and quote facts without parsing long paragraphs.
Only the `knowledge-curator` agent (or a human maintainer) may edit this file.

## Guidelines

- Capture **stable domain knowledge** only (modules, terminology, key workflows, UI conventions, docs and screenshot locations).
- Keep every table cell concise and on one logical line; avoid nested lists, code fences, or multi-paragraph explanations.
- Prefer **one fact per row** so that agents can add, remove, or update entries surgically.

## Modules

| Module prefix | Sidebar label | Approximate scope |
| --- | --- | --- |
| `00-getting-started` | Getting Started | Login, overview, dashboard |
| `01-business` | Business | Clients, vendors, invoices, payments |
| `02-factory` | Factory | Production orders, materials, costing, inventory |
| `03-trade` | Trade | Invoices, payments, checks, vouchers, banks |
| `04-employee` | Employee | Staff, attendance, salary, wages, tasks |
| `05-settings-and-admin` | Settings / Admin | Users, roles, site configuration, SMS, runtime settings |
| `06-reference` | Reference | Glossary, shortcuts, FAQs, error pages, offline mode |

## Terminology

| Term used in docs | Meaning |
| --- | --- |
| Client | A customer account that places orders and receives invoices |
| Vendor | A supplier or service provider |
| Production Order | A factory job linked to a client order |
| Invoice | A billing document sent to a client |
| Payment | A recorded receipt against an invoice |
| Salary | A staff member's monthly compensation record |
| Payroll | Bulk salary generation for a pay period |
| Wage | A per-hour or per-day compensation record for work performed |
| Voucher | An accounting voucher used to record non-invoice transactions |
| Payout | A recorded disbursement to an employee or vendor |
| Attendance | A daily presence record for a staff member |
| Dashboard | The main CTB Admin home screen with summary widgets |
| Sidebar | The left-side navigation panel in CTB Admin |
| CTB Admin | The full product name; do not abbreviate to "CTB" or "admin" |

## Key Workflows

| Workflow | One-line summary |
| --- | --- |
| Client onboarding | Add Client → set opening balance info → start creating invoices for that client |
| Invoicing | Create Invoice → add line items → send/print → mark as Paid when payment is received |
| Production | Create Production Order → assign materials and costing → track progress until completion |
| Payroll | Add Employee → record attendance → generate Salary records → export or print payslips |
| Reporting | Use per-module report pages to filter, summarize, and export business data |

## UI Conventions

| Convention | One-line summary |
| --- | --- |
| Navigation | Primary navigation is via the left sidebar in CTB Admin using the Unfold theme |
| Sidebar behavior | Each module section in the sidebar can be expanded or collapsed to show nested pages |
| Add buttons | "Add" buttons appear in the top-right on list pages to create new records |
| Save actions | "Save" and "Save and continue editing" buttons appear at the bottom of every form |
| Required fields | Required fields are marked with an asterisk (\*) in forms |

## Screenshot Locations

| Path prefix | Meaning |
| --- | --- |
| `docs/user-guide/screenshots/auth/` | Screenshots for authentication and login/logout flows |
| `docs/user-guide/screenshots/dashboard/` | Screenshots for the main admin dashboard and overview widgets |
| `docs/user-guide/screenshots/business/` | Screenshots for Business module pages (clients, vendors, invoices, payments) |
| `docs/user-guide/screenshots/factory/` | Screenshots for Factory module pages (categories, materials, inventory, products) |
| `docs/user-guide/screenshots/trade/` | Screenshots for Trade module pages (invoices, payments, checks, vouchers, banks) |
| `docs/user-guide/screenshots/employee/` | Screenshots for Employee module pages (employees, attendance, salary, wages, tasks) |
| `docs/user-guide/screenshots/settings/` | Screenshots for Settings / Admin module pages (users, app settings, SMS, maintenance) |

## Docs File Locations

| Area | Path prefix | Notes |
| --- | --- | --- |
| Getting started | `docs/user-guide/00-getting-started/` | High-level overview, login, dashboard pages |
| Business module | `docs/user-guide/01-business/` | Clients, vendors, and client-facing reports |
| Factory module | `docs/user-guide/02-factory/` | Categories, materials, inventory, and products |
| Trade module | `docs/user-guide/03-trade/` | Invoices, payments, checks, vouchers, banks, analytics |
| Employee module | `docs/user-guide/04-employee/` | Departments, positions, employees, attendance, salary, wages, payouts, tasks |
| Settings & Admin | `docs/user-guide/05-settings-and-admin/` | User management, runtime settings, SMS, maintenance mode |
| Reference | `docs/user-guide/06-reference/` | Glossary, shortcuts, error pages, offline mode and other cross-cutting topics |

## Style Benchmarks

| File | Use as benchmark for |
| --- | --- |
| `docs/user-guide/00-getting-started/dashboard.md` | Full-length page with all mandatory sections |
| `docs/user-guide/00-getting-started/login-and-logout.md` | Short page, concise writing style |

## Automated Signals

| Date | Source | Modules touched | Signal |
| --- | --- | --- | --- |
| 2026-04-19 | PR #23 | No module pages changed | 0 docs file(s) updated in merged PR. |
