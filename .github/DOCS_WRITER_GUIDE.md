# CTB2025 Documentation Writer Guide

This guide is the single source of truth for documentation writer standards in this repository.

## Purpose and scope

- This repository is for CTB2025 public documentation only.
- The CTB2025 application source repository is private.
- Focus on docs structure, docs quality, screenshots, and docs tooling.
- Do not modify application code from other repositories.

## Audience and tone

Write for non-technical business users, including:

- Factory managers
- Office staff
- Accountants
- HR staff
- System administrators

Tone and language rules:

- Use second person (you).
- Use imperative actions (Click Save, Select Client, Open Trade).
- Keep sentences short and practical.
- Avoid backend framework jargon unless explicitly requested.
- Keep headings task-oriented and predictable.

## Documentation structure

Primary docs root:

- `docs/user-guide/`

Module folders:

- `00-getting-started`
- `01-business`
- `02-factory`
- `03-trade`
- `04-employee`
- `08-settings-and-admin`
- `09-reference`

Screenshot root:

- `docs/user-guide/screenshots/`

Screenshot module folders:

- `auth/`
- `dashboard/`
- `business/`
- `factory/`
- `trade/`
- `employee/`
- `settings/`

## Required page template and section order

Use this order for new or rewritten page docs:

1. `# <Task-oriented page title>`
1. `## Summary`
1. `## When to use this page`
1. `## How to access this page`
1. `## Prerequisites` (only when relevant)
1. `## Step-by-step instructions`
1. `## Field reference`
1. `## Tips and common issues`
1. `## Related pages`

Rules:

- Keep section names stable and in this order.
- Include only fields visible in screenshot or explicitly provided in request.
- Use numbered steps for workflows.

## Style benchmark pages

Match style, heading rhythm, and level of detail from:

- `docs/user-guide/00-getting-started/overview.md`
- `docs/user-guide/01-business/clients/add-client.md`

## File naming conventions

Naming rules for docs pages:

- Use lowercase kebab-case.
- Use action-first names for task pages.
- Keep names concise and explicit.

Examples:

- `add-client.md`
- `create-invoice.md`
- `generate-salary.md`
- `invoice-reports.md`

Naming rules for screenshots:

- Use lowercase kebab-case.
- Include clear page/action context in filename.
- Keep naming stable across revisions when possible.

Examples:

- `add-client.png`
- `create-invoice-form.png`
- `invoice-report-dashboard.png`

## Screenshot rules

When a screenshot path is provided, reference it with standard Markdown image syntax.

Example:

```markdown
![Add Client form](../screenshots/business/add-client.png)
```

Operational screenshot policy:

- Do not write docs without a screenshot path.
- Use screenshots that match the described workflow.
- Keep screenshot paths valid and module-aligned.
- Prefer one screenshot near the main steps section.
- Use additional screenshots only for visually distinct workflows.

## Screenshot reuse policy

Because CTB Admin uses a consistent admin UI:

- Reuse one standard list-page screenshot pattern per module when layout is identical.
- Reuse one standard add/edit form screenshot pattern per module when layout is identical.
- Capture unique screenshots for pages with distinct UI, including:
    - Invoice print view
    - Chalan print view
    - Invoice analytics dashboard
    - Login page
    - PWA/offline view

## Screenshot tooling

Recommended tools:

- Markup Hero desktop app: https://markuphero.com/download
- Markup Hero browser extension: https://chromewebstore.google.com/detail/scrolling-screenshot-full/bnlghmkgojdehkigfkkblmmeldkmoccb
- Markup Hero online annotation: https://markuphero.com/new

Annotation conventions:

- Use callout arrows to mark click points.
- Use a consistent highlight style throughout a page set.
- For multi-step screenshots, annotate as Click 1, Click 2, Click 3 and reference those labels in doc steps.

## Navigation and URL stability rules

- Never rename or move existing docs pages unless explicitly requested.
- When adding a new page, update `mkdocs.yml` nav in the same change.
- Keep existing module naming conventions and numbering.
- Preserve URL stability and section hierarchy.

## Knowledge-first workflow

Before writing or updating docs, always read:

- `.github/knowledge/copilot-learnings.md`
- `.github/knowledge/ctb-knowledge.md`

Use those files to:

- Reuse known terminology.
- Avoid repeated issues from previous tasks.
- Keep module naming and workflow terms consistent.

## Module to app mapping reference

- `00-getting-started` -> allauth/config
- `01-business/clients` -> Business
- `01-business/vendors` -> Business
- `02-factory/categories` -> Factory
- `02-factory/materials` -> Factory
- `02-factory/material-inventory` -> Factory
- `02-factory/products` -> Factory
- `03-trade/invoices` -> Trade
- `03-trade/payments` -> Trade
- `03-trade/checks` -> Trade
- `03-trade/vouchers` -> Trade
- `03-trade/banks` -> Trade
- `04-employee/*` -> Employee
- `08-settings-and-admin` -> config

## Special pages that must not be missed

- Invoice print/PDF page
- Chalan print/PDF page
- Invoice analytics dashboard
- Client report view
- Offline/PWA page
- Error pages (400, 401, 403, 404, 500, 502, 503, 504)

## Writer completion checklist

Before submitting a docs change:

- Confirm screenshot path is valid.
- Confirm module and naming conventions match standards.
- Confirm page sections follow required order.
- Confirm `mkdocs.yml` nav was updated if a page was added.
- Confirm tone is second-person and action-oriented.
- Run:

```bash
uv run mkdocs build --strict
uv run pre-commit run --all-files
```
