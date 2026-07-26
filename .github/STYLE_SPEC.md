# CTB2025 Documentation Style Specification

<!-- version: 1.0 · source-of-truth: .github/STYLE_SPEC.md -->

<!-- Gemini CLI: gemini -p "$(cat .github/STYLE_SPEC.md)" -->

<!-- Copilot: loaded via .github/copilot-instructions.md -->

<!-- VS Code: loaded via .vscode/settings.json codeGeneration.instructions -->

______________________________________________________________________

## 1 · Identity & Purpose

**CTB Admin** is a Django-based garment/fashion/bag business management system (Unfold-themed Django Admin UI). This documentation site is built with MkDocs Material.

**Primary audience:** Non-technical business users — factory managers, office staff, accountants, HR, and system administrators.
**Scope:** User-facing product documentation only. Never document application code, Django internals, or deployment infrastructure.

______________________________________________________________________

## 2 · Voice & Tone

| Attribute       | Required                    | Example                                                                |
| --------------- | --------------------------- | ---------------------------------------------------------------------- |
| Person          | Second person only          | "You can filter by date." ✅ "Users can filter." ❌                    |
| Mood            | Imperative for instructions | "Click **Save**." ✅ "The Save button should be clicked." ❌           |
| Register        | Professional, neutral       | No marketing language, no humor, no filler                             |
| Complexity      | Plain language              | "Click" not "interact with"; "see" not "observe"                       |
| Jargon          | Forbidden unless explained  | No: model, queryset, ORM, serializer, view, Django                     |
| Sentence length | Short to medium             | Max 25 words per sentence for procedural text                          |
| Negation        | Explicit                    | "You cannot delete a paid invoice." not "Deletion may be unavailable." |

**Prohibited phrases (never use):**

- "Simply", "just", "easily", "straightforward", "seamlessly"
- "Leverage", "utilize" (use "use")
- "Navigate to" (use "Go to" or "Open")
- "Please" in instructions
- "Note that", "It is worth noting", "It should be noted"
- Passive voice where active is possible

______________________________________________________________________

## 3 · Section Structure (Canonical Page Template)

Every page MUST contain all mandatory sections in this exact order.

```
# <Task-oriented title>           [MANDATORY] imperative verb + noun: "Add Client", "Generate Salary"
## Summary                         [MANDATORY] 1–2 sentences: what the page does and why it matters
## When to use this page           [MANDATORY] 3–5 bullets: concrete usage scenarios
## How to access this page         [MANDATORY] 1 paragraph: exact sidebar path using **bold UI labels**
## Prerequisites                   [OPTIONAL]  bullets: required permissions, records, or config
## Step-by-step instructions       [MANDATORY] numbered list: one action per step, state expected result
## Field reference                 [MANDATORY] table or bullets: every visible field, business meaning
## Tips and common issues          [OPTIONAL]  bullets: practical gotchas, edge cases
## Related pages                   [MANDATORY] bullet list of cross-links with one-line context
```

**Heading rules:**

- Sentence case: "Step-by-step instructions" ✅, "Step-By-Step Instructions" ❌
- No punctuation at end of headings
- No heading level skips (h2 → h4 is forbidden)
- Extra module-specific sections go AFTER Field reference and BEFORE Tips

______________________________________________________________________

## 4 · Formatting Conventions

### 4.1 UI Element References

| Element type            | Format            | Example                                |
| ----------------------- | ----------------- | -------------------------------------- |
| Button labels           | `**bold**`        | Click **Save**                         |
| Menu / sidebar items    | `**bold**`        | Go to **Trade → Invoices**             |
| Field labels in forms   | `**bold**`        | Enter a value in **Client Name**       |
| System-generated values | `` `code span` `` | Status changes to `Paid`               |
| File paths              | `` `code span` `` | `screenshots/trade/create-invoice.png` |

### 4.2 Admonitions (MkDocs Material — only these four types)

```markdown
!!! info "Title"
    Factual context the user benefits from knowing.

!!! tip "Title"
    A faster or better way to accomplish something.

!!! warning "Title"
    An action that may have unintended consequences.

!!! note "Title"
    A constraint, limitation, or read-only behavior.
```

### 4.3 Tables

- Pipe tables only — no HTML tables
- Column 1 is always a **bold** element name
- Descriptions start with capital letter, no trailing period
- Table rows must stay on a single line
- Annotated screenshot tables use `#` | `Element` | `Description` header pattern

### 4.4 Screenshots

- Syntax: `![Short description](../screenshots/<module>/<filename>.png)`
- Place immediately after the section that describes the feature
- If no screenshot yet: `<!-- TODO: screenshot docs/user-guide/screenshots/<module>/<filename>.png -->`

### 4.5 Horizontal Rules

Use exactly 70 underscores as section dividers between major H2 sections:
`______________________________________________________________________`

### 4.6 Related Pages Format

```markdown
- **[Page Name](../path/to/page.md)** — One sentence on why this page is relevant.
```

______________________________________________________________________

## 5 · Terminology Glossary

| Use this term      | Do NOT use                    |
| ------------------ | ----------------------------- |
| Client             | Customer, buyer, account      |
| Vendor             | Supplier, seller              |
| Invoice            | Bill, receipt                 |
| Payment            | Receipt, collection           |
| Salary             | Monthly pay, paycheck         |
| Wage               | Per-day pay, daily rate       |
| Voucher            | Journal entry                 |
| Payout             | Disbursement                  |
| Attendance         | Presence, time record         |
| Production Order   | Job, work order, PO           |
| Material Inventory | Stock entry, raw material log |
| Dashboard          | Home screen, main screen      |
| Sidebar            | Left menu, navigation panel   |
| **CTB Admin**      | CTB, admin, the system        |

______________________________________________________________________

## 6 · Navigation & File Naming

### 6.1 File naming

- Lowercase kebab-case: `add-client.md`, `create-invoice.md`
- Action-first for task pages (verb-noun)
- No underscores, spaces, or capitals

### 6.2 Module path map

| Folder                   | Nav label          | Scope                                       |
| ------------------------ | ------------------ | ------------------------------------------- |
| `00-getting-started/`    | Getting Started    | Login, overview, dashboard                  |
| `01-business/`           | Business           | Clients, vendors                            |
| `02-factory/`            | Factory            | Categories, materials, inventory, products  |
| `03-trade/`              | Trade              | Invoices, payments, checks, vouchers, banks |
| `04-employee/`           | Employee           | Employees, attendance, salary, wages, tasks |
| `05-settings-and-admin/` | Settings and Admin | Users, app settings, SMS, audit log         |
| `06-reference/`          | Reference          | Glossary, errors, offline, release notes    |

### 6.3 URL stability rule

Never rename or move existing files without going through the doc-relocator agent workflow.

______________________________________________________________________

## 7 · Content Placement Rules (Information Architecture)

| Content type                                    | Canonical location                                             |
| ----------------------------------------------- | -------------------------------------------------------------- |
| How to add/edit/delete a record                 | Module sub-section (e.g., `01-business/clients/add-client.md`) |
| Overview of all sub-pages in a module           | `<module>/README.md`                                           |
| Shared field appearing in multiple modules      | Define in `06-reference/glossary.md`, link from module pages   |
| Error messages and HTTP error codes             | `06-reference/error-pages.md`                                  |
| Cross-module workflow (e.g., invoice → payment) | `06-reference/` or a cross-module guide in the relevant module |
| Permission requirements                         | Inline on each page in Prerequisites section                   |
| Release notes and checklists                    | `06-reference/`                                                |
| Gallery and screenshot index                    | `gallery.md` or `categories/<module>.md`                       |

**Relocation checklist (doc-relocator agent):**

1. Confirm content is NOT already at the target location
1. Create a redirect stub at the old path
1. Update `mkdocs.yml` nav atomically with the file move
1. Update all relative links in the moved file
1. Update all pages that linked to the old path

______________________________________________________________________

## 8 · Quality Gates

A page is complete when ALL are true:

- [ ] All mandatory sections present in canonical order
- [ ] At least one screenshot referenced (or `<!-- TODO: screenshot -->` placeholder)
- [ ] No prohibited phrases (section 2)
- [ ] All UI labels in **bold**, all code/values in `code span`
- [ ] Only the four approved admonition types used
- [ ] `mkdocs.yml` nav updated if page is new
- [ ] `uv run mkdocs build --strict` passes
- [ ] `uv run pre-commit run --all-files` passes

______________________________________________________________________

## 9 · Evolving This Spec

Update this file via PR when:

- A new UI pattern needs a formatting convention
- A new module is added to CTB Admin
- The knowledge-curator detects terminology drift
- An agent or writer repeatedly makes the same structural mistake

**Who may edit:** Any team member via PR. The knowledge-curator agent proposes amendments as PR comments but never edits this file directly.
