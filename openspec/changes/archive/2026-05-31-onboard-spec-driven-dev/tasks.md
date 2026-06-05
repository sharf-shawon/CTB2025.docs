## 1. Core Configuration

- [x] 1.1 Update `openspec/config.yaml` with project context including the tech stack (MkDocs, Python, UV) and architectural patterns.
- [x] 1.2 Define artifact-specific rules in `openspec/config.yaml`, such as enforcing the 4-hashtag rule for scenarios in specs.

## 2. Foundational Mandates

- [x] 2.1 Create a root `GEMINI.md` file that establishes the Research -> Strategy -> Execution lifecycle as the mandatory workflow.
- [x] 2.2 Define the criteria for "non-trivial changes" in `GEMINI.md` that require the use of OpenSpec.
- [x] 2.3 Document the "Fast Track" process for minor documentation fixes (typos, formatting) in `GEMINI.md`.

## 3. Agent and Skill Orchestration

- [x] 3.1 Update the root `AGENTS.md` (or create it if missing) to index all specialized sub-agents found in `.github/agents/`.
- [x] 3.2 Ensure all custom skills in `.github/skills/` and `.gemini/skills/` (propose, apply, archive, explore) are correctly registered and accessible by the Gemini CLI.
- [x] 3.3 Verify that the `opsx` commands correctly delegate tasks to the specialized agents where appropriate.

## 4. Final Validation

- [x] 4.1 Perform a smoke test by initiating a dummy change using `/opsx:propose` to verify the end-to-end integration.
- [x] 4.2 Confirm that the Gemini CLI correctly prioritizes root `GEMINI.md` mandates over subdirectory instructions.
