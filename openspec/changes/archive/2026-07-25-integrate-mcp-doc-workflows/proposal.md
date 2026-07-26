## Why

A recent third-party audit of the CTB Admin documentation site (`docs.ctbinfo.com`) highlighted strong information architecture (9.3/10) and task orientation (9.2/10), but flagged major gaps in content depth (7.0/10), definition of done / verification steps (7.2/10), exception handling, contextual cross-linking, and freshness metadata (7.1/10).

Historically, documentation authoring relied on manual extrapolation, leading to shallow pages lacking exact backend validation rules, role permission requirements, and error recovery steps. To solve this permanently, we need to integrate two active Model Context Protocol (MCP) servers—`github-mcp-server` (for inspecting Django source code, models, forms, and commits in `sharf-shawon/CTB2025`) and `ctb-staging-mcp-server` (for extracting live DOM form fields and capturing real-life UI screenshots)—into the OpenSpec workflows and documentation agent specifications. This ensures AI agents and human authors write zero-hallucination, 100% verified real-world operational documentation.

## What Changes

- **Enhanced Style Specification (`.github/STYLE_SPEC.md`)**: Expand the canonical page template to a 9-part structure featuring mandatory **Prerequisites & Role Permissions**, **Verification & Definition of Done**, **Exception Handling & Error Recovery**, **Related Workflows**, and structured **Freshness Metadata** headers.
- **MCP-Integrated OpenSpec Workflows (`.agent/workflows/`)**:
    - `/opsx:propose`: Scaffold verification specs requiring explicit backend code files (`sharf-shawon/CTB2025`) and live staging URL routes to verify.
    - `/opsx:apply`: Mandate a 3-step execution pipeline: (1) inspect backend logic via `github-mcp-server`, (2) extract DOM fields & take screenshots via `ctb-staging-mcp-server`, and (3) write verified documentation.
    - `/opsx:explore`: Enable live auditing of staging routes and backend code against existing documentation.
    - `/opsx:archive`: Automatically attach commit SHA, verification timestamp, and update metadata log.
- **Upgraded Agent Role Instructions (`.github/agents/`)**: Update `doc-writer`, `doc-updater`, `doc-auditor`, and `doc-reviewer` agent definitions to mandate dual-MCP tool usage before generating or approving content.

## Capabilities

### New Capabilities

- `mcp-doc-verification`: Dual-MCP (GitHub + Staging) verification pipeline to inspect source code logic, extract live form fields, capture real screenshots, and validate documentation without hallucinated features.
- `enhanced-doc-standards`: Upgraded 9-part canonical documentation page template and metadata specification addressing content depth, verification steps, exception handling, and freshness signals.

### Modified Capabilities

<!-- None -->

## Impact

- Documentation style spec: `.github/STYLE_SPEC.md`
- OpenSpec workflow skills: `.agent/workflows/opsx-propose.md`, `.agent/workflows/opsx-apply.md`, `.agent/workflows/opsx-explore.md`, `.agent/workflows/opsx-archive.md`
- AI Agent definitions: `.github/agents/doc-writer.agent.md`, `.github/agents/doc-updater.agent.md`, `.github/agents/doc-auditor.agent.md`, `.github/agents/doc-reviewer.agent.md`
- Project entrypoint instructions: `AGENTS.md`
