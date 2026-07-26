## 1. Reference Pages Overhaul & Boilerplate Remediation

- [x] 1.1 Remove copy-paste template instructions from `docs/user-guide/09-reference/glossary.md` and expand business domain definitions.
- [x] 1.2 Overhaul `docs/user-guide/09-reference/error-pages.md` with visual error states, root cause matrices, and role recovery steps.
- [x] 1.3 Update `docs/user-guide/09-reference/offline-mode.md` with explicit caching behaviors, Service Worker operations, and reconnect steps.
- [x] 1.4 Expand `docs/user-guide/09-reference/permissions.md` and `troubleshooting.md` with explicit Django permission codenames and resolution matrices.

## 2. Canonical Structure & Metadata Enforcement across Modules

- [x] 2.1 Standardise `00-getting-started` and `01-business` module files with 9 canonical H2 headers and metadata blocks.
- [x] 2.2 Standardise `02-factory` module files with 9 canonical H2 headers and metadata blocks.
- [x] 2.3 Standardise `03-trade` module files with 9 canonical H2 headers and metadata blocks.
- [x] 2.4 Standardise `04-employee` module files with 9 canonical H2 headers and metadata blocks.
- [x] 2.5 Standardise `05-returns`, `06-commission`, `07-reports`, and `08-settings-and-admin` module files with 9 canonical H2 headers and metadata blocks.

## 3. Operational Depth & Dual-MCP Verification

- [x] 3.1 Deepen `03-trade` operational pages (Invoices, Payments, Checks, Vouchers, Banks) using `github-mcp-server` logic audit and `ctb-staging-mcp-server` DOM forms.
- [x] 3.2 Deepen `04-employee` operational pages (Salary, Attendance, Wages, Payouts) with verified field limits, validation rules, and Definition of Done criteria.
- [x] 3.3 Deepen `02-factory` and `05-returns` operational pages with verified stock ledger rules and error recovery steps.

## 4. Cross-Module Link Graph & Discoverability

- [x] 4.1 Embed contextual upstream/downstream workflow links across all trade and financial process documentation.
- [x] 4.2 Embed contextual upstream/downstream workflow links across employee, payroll, and factory process documentation.
- [x] 4.3 Optimize page frontmatter tags and keywords for search index discoverability.

## 5. Verification & Quality Gate Automation

- [x] 5.1 Run `python3 scripts/style_lint.py` to ensure zero canonical structure or formatting violations.
- [x] 5.2 Run `uv run mkdocs build --strict` to verify zero broken links or missing redirect warnings.
- [x] 5.3 Dispatch `@doc-auditor` to generate final Machine-Readable Documentation Audit Report.
