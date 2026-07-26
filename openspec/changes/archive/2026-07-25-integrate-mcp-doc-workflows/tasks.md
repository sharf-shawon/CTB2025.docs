## 1. Documentation Style Specification Update

- [x] 1.1 Update `.github/STYLE_SPEC.md` canonical page template to include Prerequisites & Role Permissions, Verification & Definition of Done, Exception Handling & Error Recovery, and Freshness Metadata headers.
- [x] 1.2 Add Dual-MCP verification rules and zero-hallucination mandate to `.github/STYLE_SPEC.md`.

## 2. OpenSpec Workflow Integration

- [x] 2.1 Update `.agent/workflows/opsx-propose.md` to include required backend code files (`sharf-shawon/CTB2025`) and staging URL routes in proposal/specs scaffolding.
- [x] 2.2 Update `.agent/workflows/opsx-apply.md` to embed the 3-phase Dual-MCP verification pipeline (code inspection -> staging DOM & screenshot -> verified doc writing).
- [x] 2.3 Update `.agent/workflows/opsx-explore.md` and `opsx-archive.md` with MCP exploration and metadata logging rules.

## 3. AI Agent Role Specifications Update

- [x] 3.1 Update `.github/agents/doc-writer.agent.md` and `doc-updater.agent.md` to mandate `github-mcp-server` and `ctb-staging-mcp-server` tool usage before content generation.
- [x] 3.2 Update `.github/agents/doc-auditor.agent.md` and `doc-reviewer.agent.md` to audit documentation against source code and live staging.
- [x] 3.3 Update `AGENTS.md` and `.github/copilot-instructions.md` with universal dual-MCP verification instructions.

## 4. Verification

- [x] 4.1 Validate MkDocs build using `uv run mkdocs build --strict`.
- [x] 4.2 Validate pre-commit checks using `uv run pre-commit run --all-files`.
