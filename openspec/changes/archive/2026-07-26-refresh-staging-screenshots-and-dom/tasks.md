## 1. Staging DOM Field & Form Layout Inspection

- [x] 1.1 Authenticate and inspect live DOM routes using `ctb-staging-mcp-server` across Trade, Business, Factory, and Employee modules.
- [x] 1.2 Verify rendered form input fields, labels, required indicators, and select options against documentation Field Reference tables.

## 2. Screenshot Asset Capture & Placeholder Remediation

- [x] 2.1 Capture fresh UI form and list view screenshots for core module pages.
- [x] 2.2 Standardize image assets in `docs/user-guide/screenshots/` and replace any `<!-- TODO: screenshot ... -->` comment placeholders with actual image references.

## 3. Image Link & Style Linter Verification

- [x] 3.1 Run `python3 scripts/style_lint.py` to confirm zero broken screenshot links or heading rule violations.
- [x] 3.2 Run `uv run mkdocs build --strict` to verify clean site compilation and image rendering.
