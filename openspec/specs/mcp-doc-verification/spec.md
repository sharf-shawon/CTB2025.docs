## ADDED Requirements

### Requirement: AI Agents SHALL inspect source code via GitHub MCP Server

AI agents writing, updating, or auditing documentation MUST call `github-mcp-server` to inspect backend Django model definitions, admin choices, permission requirements, form validations, and recent git commits in `sharf-shawon/CTB2025`.

#### Scenario: Authoring a documentation page with source code verification

- **WHEN** an AI agent starts writing or updating a documentation page for a feature
- **THEN** the agent SHALL execute `github-mcp-server` search or file content tools to inspect backend models, views, forms, and permission gates before generating text

### Requirement: AI Agents SHALL verify live UI and extract forms via Staging MCP Server

AI agents writing or updating documentation MUST call `ctb-staging-mcp-server` to extract live DOM form fields, input options, and visual layout details from staging endpoints.

#### Scenario: Extracting form fields from live staging

- **WHEN** an AI agent creates a Field reference section for a documentation page
- **THEN** the agent SHALL run `ctb_staging_browse` with `include_forms=True` on the staging path to extract precise field labels, types, and required flags

### Requirement: AI Agents SHALL capture real screenshots using Staging MCP Server

AI agents writing new or updated documentation pages MUST capture real UI screenshots using `ctb_staging_screenshot` on staging paths.

#### Scenario: Capturing a screenshot for a documentation section

- **WHEN** an AI agent adds or updates a UI walkthrough step
- **THEN** the agent SHALL call `ctb_staging_screenshot` with the staging path and save the resulting image into `docs/user-guide/screenshots/<module>/`
