# Project Mandates: CTB 2025 Docs

This file establishes the foundational mandates for all contributors (human and AI) in this workspace. These rules take precedence over subdirectory instructions.

## Workflow: Spec-Driven Development

All non-trivial changes MUST follow the **Research -> Strategy -> Execution** lifecycle managed by the `openspec` CLI.

### Non-Trivial Change Criteria

A change is considered non-trivial if it meets ANY of the following:

- Modifies more than 3 files.
- Involves architectural decisions or structural changes to the documentation.
- Introduces new features, automation scripts, or infrastructure components.
- Requires significant research to understand the current state.

### Mandatory Artifacts

For non-trivial changes, the following artifacts MUST be generated and approved (via self-review or peer review) before implementation:

1. **Proposal (`proposal.md`)**: Establish WHY the change is needed and WHAT high-level capabilities are being added/modified.
1. **Design (`design.md`)**: Detail HOW the implementation will be approached (if architectural decisions are needed).
1. **Specs (`specs/**/*.md`)**: Define exactly WHAT the system SHALL do with testable scenarios.
1. **Tasks (`tasks.md`)**: Break down the implementation into trackable steps.

### Fast Track Process

Minor changes may bypass the full OpenSpec lifecycle:

- Typo fixes, spelling corrections, or minor grammar improvements.
- Formatting changes that do not affect content meaning.
- Updating single-file documentation where the change is trivial and self-evident.

## AI Collaboration

- AI agents SHALL prioritize instructions in this `GEMINI.md` file.
- All AI-generated changes MUST be verified by running the project's build and linting tools.
- AI agents SHALL use the `openspec` workflow for all non-trivial tasks assigned to them.
