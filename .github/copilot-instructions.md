# Copilot Instructions for CTB Admin Documentation

## Project Purpose

This repository contains the MkDocs-based documentation site for **CTB Admin**, a Django-based bag/garment/fashion business management system served through a customized Django Admin (Unfold theme).

Focus all work in this repo on **documentation structure, content quality, and docs tooling** only. Do not modify application code from other repositories.

## Stack and Tooling

- Python 3.13
- MkDocs with Material theme
- Dependency management and execution via `uv`
- Quality gates via `pre-commit`

## Docs Structure

- Main docs live under `docs/`.
- End-user documentation is organized under `docs/user-guide/` using module folders:
  - `00-getting-started`
  - `01-business`
  - `02-factory`
  - `03-trade`
  - `04-employee`
  - `05-settings-and-admin`
  - `06-reference`
- Screenshot files live under `docs/user-guide/screenshots/` with subfolders that mirror modules (for example: `business/`, `factory/`, `trade/`, `employee/`, `settings/`, `dashboard/`, `auth/`).
- Follow the detailed suggested directory structure and module-to-app mapping in `readme.md` when deciding where to place or update a page.

## Core Rules for Changes

1. Keep changes minimal and scoped to the user request.
1. Do **not** rename or move existing docs paths unless explicitly requested.
1. When adding a new page under `docs/user-guide/`, update the `nav` section in `mkdocs.yml` in the same change so the page is reachable.
1. Preserve existing section naming conventions, numeric module prefixes, and URL stability.
1. Use Markdown headings and wording that are practical for end users and operators, not developers.

## Target Audience and Tone

- Write for non-technical business users: factory managers, office staff, accountants, HR, and admins who use CTB Admin through the Django Admin UI.
- Use **second person** (“you”) and imperative mood (“Click Save”, “Select a Client”).
- Avoid backend/framework jargon (models, views, serializers) unless the user prompt explicitly asks for technical details.
- Prefer short sentences and neutral, professional tone. Do not be chatty.

## Per-Page Documentation Template

When the user asks you to generate or update documentation for a specific page (and provides the page/module name and screenshot path), produce a Markdown file that follows this structure, in this order:

1. `# <Page title>`

   - Use a task-oriented title such as “Add Client”, “Create Invoice”, “Generate Salary”, “Invoice Reports Dashboard”.

1. **Summary**

   - 1–2 sentences describing what this page lets the user do and why it matters to the business.

1. **When to use this page**

   - Bullet list of typical scenarios (for example: onboarding a new client, issuing an invoice, recording salary payout).

1. **How to access this page**

   - Brief description of how to reach the page from the CTB Admin sidebar/menu, referencing labels as shown in the UI (for example: “From the sidebar, go to **Business → Clients → Add Client**.”).

1. **Prerequisites** (optional section)

   - Only include if relevant (for example: required permissions, configuration, or existing records like Clients or Products).

1. **Step-by-step instructions**

   - Numbered list that walks the user through the workflow from start to finish.
   - Each step should describe a clear user action and expected result.
   - When a screenshot is provided, reference it inline using text such as “See the screenshot below” rather than inventing HTML.

1. **Field reference**

   - Table or bullet list explaining the key fields or options on the page.
   - For each field, use this pattern:
     - **Field label** — What the field means in business terms, and how it affects the outcome (for example, reporting, pricing, access control).
   - Only include fields that are visible in the screenshot or that the user has explicitly described.

1. **Tips and common issues** (optional but recommended)

   - Short bullets with practical advice, warnings, or common pitfalls (for example: “You cannot change the Client once an Invoice is marked Paid.”).

1. **Related pages**

   - List of other docs pages that naturally follow or precede this workflow (for example: “See **Client Reports** for analytics on this data.”).

Always include headings in this order, even if some optional sections end up being short.

## Screenshot Handling Rules

- The user will either:

  - Provide a new screenshot, or
  - Refer to an existing screenshot path under `docs/user-guide/screenshots/...`.

- When a screenshot path is provided, assume the image exists and reference it in the Markdown using standard image syntax:

  ```markdown
  ![Short description](../screenshots/<module>/<file-name>.png)
  ```

---

## 📚 Knowledge First

ALWAYS read these files before starting any documentation task:

- `.github/knowledge/copilot-learnings.md` — past lessons, things to do and avoid
- `.github/knowledge/ctb-knowledge.md` — CTB Admin domain knowledge, terminology, and module map

---

## 🎨 Style Benchmarks

Match the tone, structure, and heading style of these existing files exactly:

- `docs/user-guide/00-getting-started/overview.md`
- `docs/user-guide/01-business/clients/add-client.md`

---

## 🚫 NEVER DO

- Delete or rename existing docs files
- Change `mkdocs.yml` nav without adding a corresponding new page
- Write documentation without a screenshot path
- Touch `.github/knowledge/` files during a documentation write task — knowledge files are only updated after a PR is merged, never mid-task
- Remove any line from a knowledge file unless the user explicitly requests the removal or the information is factually wrong
- Trigger the audit workflow more than once per PR

---

## 🔄 Self-Learning

After a PR is merged, append exactly one row to the table in `.github/knowledge/copilot-learnings.md`. Each field must fit on a single line — no newlines inside a cell.

```
| YYYY-MM-DD | <short task summary> | <what was done> | <what the user approved> | <what to avoid next time> |
```
