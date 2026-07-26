## Context

The repository currently has the `openspec` CLI installed and some custom AI agents in `.github/agents/` and skills in `.github/skills/`. However, there is no formal configuration tying them together, and no foundational mandates (`GEMINI.md`) to ensure that both human and AI contributors follow the spec-driven development lifecycle.

## Goals / Non-Goals

**Goals:**

- Configure `openspec/config.yaml` with project context (MkDocs, Python, UV) and artifact-specific rules.
- Create a root `GEMINI.md` that mandates the Research -> Strategy -> Execution lifecycle and the use of OpenSpec for all non-trivial changes.
- Integrate custom agents from `.github/agents/` into the `openspec` workflow by documenting their roles and ensuring they are discoverable.
- Ensure all custom skills (propose, apply, archive, explore) are correctly configured and usable.

**Non-Goals:**

- Modifying the existing documentation content itself.
- Changing the build system (MkDocs) or deployment pipelines.

## Decisions

- **Decision: Populate `openspec/config.yaml` with Rich Context**

    - **Rationale**: The OpenSpec CLI uses this context to ground artifact generation. Including details about the tech stack and documentation standards will improve the quality of generated proposals and designs.
    - **Alternatives**: Keeping a minimal config and relying on general AI knowledge, which often leads to generic or incorrect assumptions.

- **Decision: Establish `GEMINI.md` as the "Source of Truth" for Workflow**

    - **Rationale**: The Gemini CLI specifically prioritizes `GEMINI.md` for operational mandates. This is the most effective place to enforce the spec-driven workflow.
    - **Alternatives**: Putting workflow instructions in `CONTRIBUTING.md`, which is intended for humans and may be ignored by the AI agent's core loop.

- **Decision: Reference Custom Agents in `AGENTS.md`**

    - **Rationale**: A central index of agents allows the orchestrator to understand the specialized capabilities available for delegation.
    - **Alternatives**: Hardcoding agent paths in individual skills.

## Risks / Trade-offs

- **[Risk]** → **Over-engineering minor changes**: Forcing a proposal for a one-word fix is inefficient.

- **[Mitigation]** → Define a "Fast Track" in `GEMINI.md` for trivial changes (typos, formatting) that bypass the OpenSpec lifecycle.

- **[Risk]** → **Knowledge fragmentation**: Having instructions in both `GEMINI.md` and `openspec/config.yaml`.

- **[Mitigation]** → Use `GEMINI.md` for *mandates* (what to do) and `openspec/config.yaml` for *context* (how to do it/technical constraints).
