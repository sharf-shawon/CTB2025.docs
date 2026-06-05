## ADDED Requirements

### Requirement: Mandatory OpenSpec Lifecycle

The workspace SHALL mandate the Research -> Strategy -> Execution lifecycle for all non-trivial changes. A change is considered non-trivial if it involves more than 3 files, architectural decisions, or new feature implementations.

#### Scenario: Human or AI initiates a non-trivial change

- **WHEN** a contributor starts a new task that meets the non-triviality criteria
- **THEN** they MUST create an OpenSpec proposal using `openspec new change` before writing code

### Requirement: Root GEMINI.md Foundational Mandates

The repository SHALL maintain a root `GEMINI.md` file containing high-level operational mandates that take precedence over all other documentation for AI agents.

#### Scenario: AI agent encounters a conflict in instructions

- **WHEN** an AI agent reads instructions from a subdirectory that conflict with the root `GEMINI.md`
- **THEN** it SHALL prioritize the mandates in the root `GEMINI.md`

### Requirement: OpenSpec Configuration

The repository SHALL maintain a valid `openspec/config.yaml` that defines the project's tech stack, conventions, and artifact-specific rules.

#### Scenario: OpenSpec artifact generation

- **WHEN** the `openspec` CLI generates a new artifact (e.g., proposal, design)
- **THEN** it SHALL incorporate the context and rules defined in `openspec/config.yaml`
