## Context

The CTB Admin documentation repository uses MkDocs Material with custom agents, workflows, and guidelines defined in `.github/` and `.agent/`. A third-party evaluation gave the site 8.3/10, identifying gaps in content depth (7.0/10), definition of done / verification steps (7.2/10), exception handling, contextual cross-linking, and freshness metadata (7.1/10).

To address these gaps, we are designing a dual-MCP verification pipeline using `@mcp:github-mcp-server` (backend code & history) and `@mcp:ctb-staging-mcp-server` (live DOM form extraction & screenshots).

## Goals / Non-Goals

**Goals:**

- Upgrade `.github/STYLE_SPEC.md` with a 9-part canonical page template including Prerequisites & Role Permissions, Verification & Definition of Done, Exception Handling & Error Recovery, and Freshness Metadata headers.
- Update OpenSpec workflow definitions (`.agent/workflows/opsx-propose.md`, `opsx-apply.md`, `opsx-explore.md`, `opsx-archive.md`) to integrate dual-MCP inspection steps.
- Update AI Agent specifications (`.github/agents/doc-writer.agent.md`, `doc-updater.agent.md`, `doc-auditor.agent.md`, `doc-reviewer.agent.md`) to mandate dual-MCP tool execution.
- Update repository instructions (`AGENTS.md`) to mandate dual-MCP verification rules.

**Non-Goals:**

- Mass-updating all existing 100+ markdown files in `docs/` in a single PR (pages will be updated incrementally using the new workflows).
- Modifying Django application code or staging server backend configuration.

## Decisions

### Decision 1: Dual-MCP Mandatory Grounding Pipeline

- **Decision**: Documentation authoring, updating, and auditing MUST query both `github-mcp-server` (for Django models, views, forms, and permissions) and `ctb-staging-mcp-server` (for live route extraction, form fields, and screenshots).
- **Rationale**: Relying on AI memory or doc summaries causes hallucinated fields and missing validation rules. Dual-MCP verification provides ground truth from source code and runtime DOM.
- **Alternatives Considered**: Manual developer reviews (slow, error-prone), static code regex parsing (lacks live Unfold admin UI context).

### Decision 2: 9-Part Canonical Page Structure

- **Decision**: Update `STYLE_SPEC.md` canonical page template to:
    1. `# <Task-oriented title>` + HTML comment Metadata
    1. `## Summary`
    1. `## When to use this page`
    1. `## How to access this page`
    1. `## Prerequisites & Role Permissions`
    1. `## Step-by-step instructions`
    1. `## Verification & Definition of Done`
    1. `## Field reference`
    1. `## Exception Handling & Error Recovery`
    1. `## Related Workflows & Next Steps`
- **Rationale**: Directly resolves the 3rd party assessment gaps regarding procedure depth, verification, edge cases, cross-linking, and role permissions.

## Risks / Trade-offs

- **[Risk] Staging Environment Unavailability**: Staging server (`staging.ctbinfo.com`) may occasionally be offline or undergo maintenance during doc writing.
    - **Mitigation**: Agents can rely on `github-mcp-server` for source code truth and insert `<!-- TODO: screenshot ... -->` placeholders until staging comes back online.
- **[Risk] Increased Execution Time for OpenSpec Apply**: Dual-MCP calls add 5–10 seconds per doc task.
    - **Mitigation**: High quality, zero-hallucination documentation significantly outweighs slight tool call overhead.

## Migration Plan

1. Update `.github/STYLE_SPEC.md` with new page structure, metadata standards, and dual-MCP guidelines.
1. Update `.agent/workflows/` skills (`opsx-propose.md`, `opsx-apply.md`, `opsx-explore.md`, `opsx-archive.md`).
1. Update `.github/agents/` prompt specifications.
1. Update `AGENTS.md` to reflect new agent constraints.
1. Verify MkDocs build (`uv run mkdocs build --strict`) and pre-commit checks.
