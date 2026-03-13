# CmdRunner — VS Code Extension

Build a VS Code extension called **cmdRunner** that allows developers to configure and run terminal commands directly from clickable buttons in the VS Code status bar. The extension must be secure, team-friendly, AI-agent-ready, and fully documented from day one.

______________________________________________________________________

## Core Functionality

- Read configuration from `.cmdrunner` (JSON) or `.cmdrunner.yml` (YAML) at the workspace root
- Support `.cmdrunner.local` / `.cmdrunner.local.yml` as a gitignored, user-specific override that deep-merges on top of the shared config
- Display each configured command as a **clickable button in the VS Code status bar**
- While a command is running, show `$(sync~spin)` spinner on the button; display exit code in the tooltip on completion
- Re-clicking a running command sends `Ctrl+C` and toggles the icon to `$(debug-stop)`
- Commands run in the **user's default VS Code terminal profile** unless a per-command `terminalProfile` override is set
- In **multi-root workspaces**, each folder loads its own `.cmdrunner`; buttons are grouped by folder name in the status bar

______________________________________________________________________

## Configuration Schema

```json
{
  "$schema": "./.vscode/cmdrunner.schema.json",
  "display": "auto",
  "maxVisible": 5,
  "terminalProfile": "default",
  "startupMode": "sequential",
  "cooldownMs": 1000,

  "profiles": {
    "dev":     { "env": { "DJANGO_ENV": "development" } },
    "staging": { "env": { "DJANGO_ENV": "staging" } },
    "prod":    { "env": { "DJANGO_ENV": "production" } }
  },
  "activeProfile": "dev",

  "startup": [
    { "label": "Activate venv", "command": "source .venv/bin/activate" },
    { "label": "Sync dependencies", "command": "uv sync" }
  ],

  "commands": [
    {
      "id": "dev-server",
      "label": "$(play) Run Dev",
      "command": "python manage.py runserver",
      "terminal": "Django Dev",
      "group": "Django",
      "cwd": "${workspaceFolder}",
      "color": "terminal.ansiGreen",
      "reuseTerminal": true,
      "keybinding": "ctrl+shift+r",
      "dependsOn": [],
      "env": { "PORT": "8000" },
      "checksum": "sha256:<hash-of-command-string>"
    },
    {
      "id": "run-tests",
      "label": "$(beaker) Tests",
      "command": "pytest -x --tb=short",
      "terminal": "Tests",
      "group": "Django",
      "reuseTerminal": false
    }
  ]
}
```

### Schema Field Reference

| Field           | Type                                    | Description                                                |
| --------------- | --------------------------------------- | ---------------------------------------------------------- |
| `display`       | `"auto"` \| `"sidebar"` \| `"dropdown"` | How commands appear in the status bar                      |
| `maxVisible`    | `number`                                | Max inline buttons before overflow to QuickPick dropdown   |
| `startupMode`   | `"sequential"` \| `"parallel"`          | Execution order for `startup` commands                     |
| `cooldownMs`    | `number`                                | Debounce delay (ms) between re-runs of the same command    |
| `profiles`      | `object`                                | Named env var sets switchable at runtime                   |
| `activeProfile` | `string`                                | Currently active profile                                   |
| `reuseTerminal` | `boolean`                               | Reuse and clear existing named terminal, or spawn new      |
| `dependsOn`     | `string[]`                              | Command IDs that must succeed before this one runs         |
| `color`         | `string`                                | VS Code theme color token for the status bar button        |
| `keybinding`    | `string`                                | Auto-registers a keyboard shortcut for this command        |
| `checksum`      | `string`                                | SHA-256 of the command string; warns on mismatch           |
| `group`         | `string`                                | Commands in the same group collapse into a labeled submenu |

### Variable Interpolation

Supported in `command` and `cwd` fields:
`${workspaceFolder}` `${workspaceName}` `${gitBranch}` `${userHome}` `${datetime}`

______________________________________________________________________

## Security Requirements

- **Workspace Trust gate** — refuse all execution in untrusted workspaces; show a dismissible warning panel
- **`terminal.sendText()` only** — never use `child_process.exec()`, `spawn()`, or `eval()`; eliminate all shell injection surface
- **Schema validation on every load** — use Zod for runtime validation; reject malformed configs with specific, actionable error messages
- **`cmdrunner.blockedPatterns`** — VS Code setting accepting a regex array; commands matching any pattern are blocked before execution
- **Checksum verification** — if `checksum` is present and does not match the current command string, warn the user and require explicit confirmation before running
- **Secret masking** — env values matching secret patterns (`sk-`, `ghp_`, 40+ char alphanumeric) are masked in terminal output and audit logs
- **Audit log** — every execution appended to `~/.cmdrunner/audit.log` with ISO timestamp, workspace path, command ID, and exit code
- **Rate limiting** — `cooldownMs` per command prevents accidental rapid-fire execution
- **`SECURITY.md`** — vulnerability disclosure policy with contact and response SLA
- **Documentation warning** — explicitly state that secrets must never be stored in `.cmdrunner`; `.cmdrunner.local` must always be in `.gitignore`

______________________________________________________________________

## Developer Experience

- **IntelliSense** — register JSON Schema so `.cmdrunner` files get autocomplete, hover documentation, and inline error highlighting
- **Hot reload** — watch `.cmdrunner` for changes; rebuild the status bar without restarting VS Code
- **Command Palette** — every configured command accessible as `CmdRunner: Run > <label>`
- **`CmdRunner: Initialize .cmdrunner`** — scaffolds a starter config at the workspace root
- **`CmdRunner: Validate Config`** — validates `.cmdrunner` and reports all errors without executing anything
- **`CmdRunner: Switch Profile`** — QuickPick to change `activeProfile` at runtime
- **`CmdRunner: History`** — QuickPick showing recent commands with timestamps and exit codes
- **Onboarding Walkthrough** — VS Code Walkthrough API guides first-time users when no `.cmdrunner` is found
- **VS Code Task bridge** — expose `.cmdrunner` commands as VS Code tasks usable as `preLaunchTask` in `launch.json`
- **Settings UI** — expose `maxVisible`, `blockedPatterns`, `defaultProfile`, `auditLog` in VS Code's native Settings UI with full descriptions

______________________________________________________________________

## Code Quality Standards

- TypeScript with `"strict": true`; zero use of `any`
- Zod schemas in `types.ts` for all config structures — enforce at both compile time and runtime
- JSDoc on all public functions, classes, and modules
- Conventional Commits enforced via `commitlint`: `feat:` `fix:` `docs:` `chore:` `test:` `refactor:`
- Minimum **80% test coverage** enforced in CI via `c8`
- All commits — including agent-submitted PRs — must pass pre-commit hooks before submission

______________________________________________________________________

## Repository Structure

```
cmdrunner-vscode/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.yml
│   │   ├── feature_request.yml
│   │   └── docs_update.yml
│   ├── workflows/
│   │   ├── ci.yml                  # Lint, type-check, test, coverage on every PR
│   │   ├── build.yml               # Package signed VSIX artifact on main push
│   │   ├── release.yml             # Publish to Marketplace + Open VSX on v* tag
│   │   ├── regression.yml          # Nightly: test on last 3 VS Code versions
│   │   ├── dependency-review.yml   # PR: flag packages with known CVEs
│   │   └── agent-learn.yml         # Weekly: agents update knowledge-base
│   ├── copilot-instructions.md
│   └── PULL_REQUEST_TEMPLATE.md
├── .agents.md
├── .cmdrunner                      # Dogfooding: extension used in its own repo
├── .vscode/
│   ├── cmdrunner.schema.json       # JSON Schema (kept in sync with types.ts)
│   └── settings.json
├── src/
│   ├── extension.ts                # Activation entry point
│   ├── configLoader.ts             # Parse + validate .cmdrunner / .cmdrunner.yml
│   ├── statusBar.ts                # Status bar lifecycle, spinner, stop toggle
│   ├── terminalRunner.ts           # sendText, kill, reuse, dependsOn logic
│   ├── startupRunner.ts            # Sequential / parallel startup orchestration
│   ├── profileManager.ts           # Profile switching and env var merging
│   ├── security.ts                 # Trust gate, blockedPatterns, checksum, masking
│   ├── auditLog.ts                 # Append-only audit log writer
│   ├── variableResolver.ts         # ${workspaceFolder}, ${gitBranch}, etc.
│   ├── taskBridge.ts               # VS Code Task provider integration
│   ├── walkthrough.ts              # Onboarding walkthrough registration
│   └── types.ts                    # Zod schemas + TypeScript interfaces
├── test/
│   └── suite/
│       ├── configLoader.test.ts
│       ├── security.test.ts
│       ├── statusBar.test.ts
│       ├── profileManager.test.ts
│       ├── variableResolver.test.ts
│       └── integration/
│           └── terminalRunner.integration.test.ts
├── docs/
│   ├── architecture.md
│   ├── configuration-reference.md
│   ├── security.md
│   ├── contributing.md
│   ├── roadmap.md
│   └── agent-knowledge-base.md     # Living doc; dated + tagged entries
├── .husky/
│   ├── pre-commit
│   └── commit-msg
├── SECURITY.md
├── README.md
├── CHANGELOG.md
├── package.json
└── tsconfig.json
```

______________________________________________________________________

## CI/CD Workflows

| Workflow                | Trigger        | Actions                                                                       |
| ----------------------- | -------------- | ----------------------------------------------------------------------------- |
| `ci.yml`                | Every PR       | ESLint, Prettier, `tsc --noEmit`, Mocha + c8 (≥80%), VSIX dry-run             |
| `build.yml`             | Push to `main` | Package and sign `.vsix`; upload as artifact                                  |
| `release.yml`           | Push `v*` tag  | Publish to VS Code Marketplace + Open VSX via `VSCE_PAT` / `OVSX_PAT` secrets |
| `regression.yml`        | Nightly        | Test VSIX on VS Code `stable`, `1.95`, `1.90`; auto-file issue on failure     |
| `dependency-review.yml` | Every PR       | Block merge on packages with known CVEs                                       |
| `agent-learn.yml`       | Weekly         | Scan merged PRs + issues; append to `docs/agent-knowledge-base.md`            |

______________________________________________________________________

## AI Agent Configuration

### `.github/copilot-instructions.md`

Copilot must adhere to the following protocol on every task:

1. **Read `docs/agent-knowledge-base.md` first** — understand all prior decisions, patterns, and developer preferences before writing any code
1. **Never submit a PR where `husky pre-commit` fails** — fix all hook failures locally before opening a PR
1. **Update `/docs` on every code change** — every PR touching `src/` must include corresponding documentation updates; the `cmdrunner-docs` agent is auto-triggered on merge but agents should not rely on it as a fallback
1. **Append a tagged learning entry** to `agent-knowledge-base.md` after completing each task using the format:
   ```
   [YYYY-MM-DD][category] Description of decision, pattern, or lesson.
   ```
   Valid categories: `architecture` `security` `ux` `dx` `testing` `preference` `mistake-avoided`
1. **Review past knowledge-base entries** before starting work — self-improvement loop; avoid repeating resolved mistakes; maintain consistency across the codebase
1. **Enforce security rules without exception** — workspace trust gate and `terminal.sendText()` exclusivity are hard, non-negotiable requirements
1. **Use Conventional Commits exclusively** — `commitlint` will reject any other format
1. **Proactively identify and fix documentation gaps** — if code exists without corresponding docs, write the docs unprompted without waiting to be asked
1. **Sync schema on type changes** — any modification to `types.ts` must be reflected in `cmdrunner.schema.json` and `docs/configuration-reference.md` in the same PR

### `.agents.md`

```markdown
## Agent: cmdrunner-dev
Skills: TypeScript, VS Code Extension API, Zod, ESLint, Mocha, c8
Permissions: read/write src/, test/, docs/
Forbidden: .github/workflows/ (read-only), package.json version field
Pre-submit: husky pre-commit must pass; coverage must not drop below 80%

## Agent: cmdrunner-docs
Skills: Markdown, technical writing, Keep a Changelog format
Permissions: read/write docs/, README.md, CHANGELOG.md, SECURITY.md
Trigger: auto-activated on every merged PR containing src/ changes
Must-do: update configuration-reference.md whenever types.ts or schema changes

## Agent: cmdrunner-schema
Skills: JSON Schema Draft-07, TypeScript interfaces, Zod
Permissions: read/write .vscode/cmdrunner.schema.json, src/types.ts, docs/configuration-reference.md
Trigger: any PR adding or modifying config keys in types.ts
Must-do: keep schema, Zod types, and docs in perfect sync — all three in one PR

## Agent: cmdrunner-release
Skills: semver, VSIX packaging, VS Code Marketplace, Open VSX
Permissions: read/write package.json (version field only), .github/workflows/release.yml
Trigger: manual workflow dispatch or milestone close
Pre-release: verify all CI checks green; verify CHANGELOG.md has release entry
```

______________________________________________________________________

## Pre-commit Hooks

```bash
# .husky/pre-commit
npx lint-staged          # ESLint --fix + Prettier on staged files
npx tsc --noEmit         # Full TypeScript type check — zero errors required
npm test -- --exit       # Unit tests with c8 coverage enforcement

# .husky/commit-msg
npx commitlint --edit $1 # Conventional Commits format — no exceptions
```

```json
// package.json — lint-staged config
"lint-staged": {
  "*.ts": ["eslint --fix", "prettier --write"],
  "*.{json,yml,md}": ["prettier --write"]
}
```

______________________________________________________________________

## README Requirements

The `README.md` must cover all of the following sections, in order:

1. Marketplace badges (version, installs, rating, build status, coverage)
1. Quick Start — install → create `.cmdrunner` → click status bar (completable in under 60 seconds)
1. Full Configuration Reference — every schema key with type, default, and example
1. Startup Commands — sequential vs. parallel; use cases like `uv sync` and venv activation
1. Environment Profiles — defining and switching between `dev` / `staging` / `prod`
1. Display Modes — `auto`, `sidebar`, `dropdown` with screenshots
1. Terminal Profiles — per-command override vs. global default
1. Variable Interpolation — all supported `${}` tokens with examples
1. Security Model — workspace trust, blocked patterns, checksum verification, audit log
1. VS Code Task Bridge — using `.cmdrunner` commands as `preLaunchTask`
1. AI Agent Onboarding — Copilot setup, agent roles, knowledge-base protocol
1. Contributing Guide — pre-commit hooks, conventional commits, coverage requirement, PR checklist

______________________________________________________________________

## Deliverables Checklist

- [ ] All `src/` modules with full JSDoc and zero `any`
- [ ] Zod-based `types.ts` enforcing config structure at runtime and compile time
- [ ] `cmdrunner.schema.json` in sync with `types.ts`
- [ ] Full test suite — unit + integration — with ≥80% coverage
- [ ] All six GitHub Actions workflows
- [ ] `SECURITY.md` with disclosure policy and response SLA
- [ ] `.github/copilot-instructions.md` with full self-learning protocol (9 rules)
- [ ] `.agents.md` with four agent definitions and scoped permissions
- [ ] Bug report, feature request, and docs update issue templates
- [ ] PR template with checklist (tests, docs, hooks, conventional commit)
- [ ] Husky `pre-commit` and `commit-msg` hooks with `lint-staged` and `commitlint`
- [ ] All six `docs/` documents, including seeded `agent-knowledge-base.md`
- [ ] `README.md` with all twelve sections and marketplace badges
- [ ] `.cmdrunner` at repo root (dogfooding the extension in its own development workflow)
- [ ] Open VSX publish step in `release.yml` alongside Marketplace publish
