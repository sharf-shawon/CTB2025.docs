## Context

Documentation visual assets in `docs/user-guide/` must accurately reflect the live CTB Admin Unfold theme layout (`staging.ctbinfo.com`). While content depth was expanded in previous changes, visual screenshots and DOM field mappings require automated capture and structural validation using `ctb-staging-mcp-server` and browser tools.

## Goals / Non-Goals

**Goals:**

- Perform systematic DOM inspection of live form fields across primary CTB Admin routes (`/en/admin/Trade/*`, `/en/admin/Business/*`, `/en/admin/Employee/*`).
- Capture fresh high-resolution UI screenshots for major forms and list views.
- Audit all image references in documentation to eliminate broken paths and unformatted placeholders.
- Verify zero warnings during `python3 scripts/style_lint.py` and `uv run mkdocs build --strict`.

**Non-Goals:**

- Modifying backend Django templates or frontend Unfold CSS stylesheets.
- Creating placeholder graphics; all assets must be captured from live staging.

## Decisions

### 1. Verification Engine: Staging MCP & Playwright Browser Automation

- **Decision**: Use `ctb-staging-mcp-server` (`ctb_staging_browse`, `ctb_staging_screenshot`) in combination with local Playwright browser tools to capture exact DOM element states.
- **Rationale**: Guarantees authentic visual screenshots and exact DOM element attributes (name, label, required state, type).
- **Alternatives Considered**: Manual browser screenshots, which lead to inconsistent crop ratios, window sizes, and missing retina resolutions.

### 2. Asset Storage Standard: Modular Image Directory Structure

- **Decision**: Store module screenshots under `docs/user-guide/screenshots/<module>/` using kebab-case names matching task titles (e.g. `create-invoice-general-info.png`).
- **Rationale**: Follows `STYLE_SPEC.md` §6 image organization standards and keeps image paths predictable.
- **Alternatives Considered**: Storing all images in a flat single directory, which causes filename collisions and bloats module folders.

## Risks / Trade-offs

- **[Risk]** Staging environment network latency or authentication timeouts during automated browsing.
    - **Mitigation**: Use `ctb_staging_login` with stored session credentials and set appropriate timeout parameters.
- **[Risk]** Large screenshot PNG image sizes slowing down MkDocs build or git repository size.
    - **Mitigation**: Crop UI viewports to relevant form sections and optimize PNG compression prior to committing.
