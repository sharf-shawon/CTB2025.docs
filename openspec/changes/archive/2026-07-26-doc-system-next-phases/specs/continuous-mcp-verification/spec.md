## ADDED Requirements

### Requirement: CI pipeline SHALL perform Dual-MCP verification on pull requests

The CI pipeline SHALL inspect changed documentation pages against Django backend source code (`github-mcp-server`) and staging DOM forms (`ctb-staging-mcp-server`) to verify field labels, permission codenames, and status transition logic.

#### Scenario: Detecting hallucinated form field or permission

- **WHEN** a documentation pull request introduces an unverified field name or permission codename
- **THEN** the Dual-MCP CI verification check fails with a detailed report listing the unverified symbols.
