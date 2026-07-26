## 1. Search Taxonomy & Metadata Tag Optimization

- [x] 1.1 Enrich frontmatter tags across Trade, Business, Factory, and Employee module pages with domain aliases (e.g. `bill`, `receipt`, `paycheck`, `slip`).
- [x] 1.2 Audit page titles and H2 headings to optimize search keyword indexing for common business user queries.

## 2. Cross-Module Workflow Link Graph Integration

- [x] 2.1 Establish explicit bidirectional workflow links in `## Related workflows & next steps` connecting Client $\rightarrow$ Invoice $\rightarrow$ Payment $\rightarrow$ Voucher operations.
- [x] 2.2 Link Employee Attendance $\rightarrow$ Salary Generation $\rightarrow$ Payout workflows across `04-employee/` and `03-trade/`.

## 3. Verification & Link Integrity Validation

- [x] 3.1 Run `python3 scripts/style_lint.py` to ensure zero structural or frontmatter syntax errors.
- [x] 3.2 Run `uv run mkdocs build --strict` to verify site compilation, search indexing, and internal link resolution.
