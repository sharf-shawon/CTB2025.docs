## ADDED Requirements

### Requirement: AI Agent Discovery via AGENTS.md

The repository SHALL maintain an `AGENTS.md` file in the root that lists all available custom AI agents, their locations, and their specialized roles.

#### Scenario: Orchestrator needs to delegate a task

- **WHEN** the primary AI agent (e.g., Gemini CLI) identifies a task suitable for a specialized sub-agent
- **THEN** it SHALL consult `AGENTS.md` to find the most relevant agent to invoke

### Requirement: Custom Skill Registration

All custom `opsx` skills (e.g., propose, apply, explore) SHALL be registered and discoverable by the Gemini CLI within the `.gemini/skills/` or `.github/skills/` directories.

#### Scenario: User runs an opsx command

- **WHEN** a user executes a command like `/opsx:propose`
- **THEN** the system SHALL load the corresponding skill from the designated skills directory and follow its procedural guidance

### Requirement: Automated Artifact Verification

The spec-driven workflow SHALL include automated verification of artifact structural integrity (e.g., correct number of hashtags in scenarios).

#### Scenario: Developer saves a spec file

- **WHEN** a developer or AI agent writes to a `spec.md` file
- **THEN** the system SHALL verify that scenarios use exactly 4 hashtags (`####`)
