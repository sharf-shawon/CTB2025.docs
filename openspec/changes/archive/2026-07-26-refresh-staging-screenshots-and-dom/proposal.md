## Why

As CTB Admin UI evolves, embedded documentation screenshots and DOM form field descriptions can become outdated, leading to visual drift and confusion for end users.

Refreshing live staging screenshots and validating DOM field layouts using `ctb-staging-mcp-server` ensures 100% visual fidelity, eliminates broken image links, and verifies that documented form fields match the live Unfold-themed Django Admin UI.

## What Changes

- **Live Staging Screenshot Audit**: Inspect and capture fresh high-resolution UI screenshots from `staging.ctbinfo.com` across Trade, Business, Factory, Employee, and Settings modules.
- **Image Asset Normalization**: Replace outdated image PNGs with standardized, crisp UI captures following `STYLE_SPEC.md` §6 image conventions.
- **DOM Form Field Audit**: Verify live HTML `<input>`, `<select>`, and `<textarea>` elements against documented Field Reference tables.
- **Screenshot Placeholder Remediation**: Replace all `<!-- TODO: screenshot ... -->` comments in documentation with verified image paths.

## Capabilities

### New Capabilities

- `live-staging-screenshot-refresh`: Systematic visual audit and image capture pipeline for all CTB Admin documentation screenshot assets.
- `dom-field-verification-pipeline`: Real-time DOM inspection and form schema verification using `ctb-staging-mcp-server`.

### Modified Capabilities

*(None)*

## Impact

- **Documentation Assets**: Updates image files in `docs/user-guide/screenshots/` and module subdirectories (`auth/`, `trade/`, `business/`, `factory/`, `employee/`, `settings/`).
- **Markdown Pages**: Updates image links and DOM field tables in `docs/user-guide/` module pages.
- **Verification Integrity**: Guarantees zero broken image paths and accurate visual representation during `mkdocs build --strict`.
