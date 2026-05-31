# AGENTS.md — CTB2025 Documentation AI System

<!-- Loaded automatically by: Gemini CLI, Claude, and any AGENTS.md-aware tool -->

<!-- For Copilot: see .github/copilot-instructions.md (mirrors this content) -->

This repository contains MkDocs Material documentation for **CTB Admin** — a Django-based garment/fashion/bag business management system.

## Mandatory reading before any task

1. `.github/STYLE_SPEC.md` — canonical style, tone, structure, and terminology contract
1. `.github/knowledge/ctb-knowledge.md` — domain knowledge and module map
1. `.github/knowledge/copilot-learnings.md` — past lessons and mistakes to avoid
1. `mkdocs.yml` — current nav structure (grep the relevant section only)

## Available agents

| Agent             | File                                        | When to use                                   |
| ----------------- | ------------------------------------------- | --------------------------------------------- |
| doc-writer        | `.github/agents/doc-writer.agent.md`        | Write a new page from scratch                 |
| doc-improver      | `.github/agents/doc-improver.agent.md`      | Iteratively improve content for clarity/flow  |
| doc-updater       | `.github/agents/doc-updater.agent.md`       | Update existing docs with new feature details |
| doc-standardizer  | `.github/agents/doc-standardizer.agent.md`  | Rewrite existing page to match STYLE_SPEC     |
| doc-reviewer      | `.github/agents/doc-reviewer.agent.md`      | Review and produce structured feedback        |
| doc-relocator     | `.github/agents/doc-relocator.agent.md`     | Move a page to a better nav location          |
| nav-manager       | `.github/agents/nav-manager.agent.md`       | Update mkdocs.yml nav only                    |
| knowledge-curator | `.github/agents/knowledge-curator.agent.md` | Post-merge knowledge updates                  |
| doc-auditor       | `.github/agents/doc-auditor.agent.md`       | Full repo style/structure audit               |
| docs-infra        | `.github/agents/docs-infra.agent.md`        | Debug or extend documentation infrastructure  |

## Universal rules (all agents, all vendors)

1. STYLE_SPEC.md is the only style authority — check it before any writing decision
1. Never rename or move files without completing the relocation checklist (STYLE_SPEC §7)
1. Never edit `.github/knowledge/` mid-task — only knowledge-curator edits those, post-merge
1. Never generate content without a screenshot path or a `<!-- TODO: screenshot ... -->` placeholder
1. Never add `mkdocs.yml` nav entries for files that do not exist
1. One PR per task — keep changes minimal and scoped

## Gemini CLI quick-start

```bash
# Write a new page
gemini -p "$(cat .github/STYLE_SPEC.md) $(cat .github/knowledge/ctb-knowledge.md)" \
  "Write a new page. Module: 03-trade. Title: Add Bank. Screenshot: ../screenshots/trade/add-bank.png. Output file only."

# Standardize an old page
gemini -p "$(cat .github/STYLE_SPEC.md)" \
  "Rewrite to STYLE_SPEC. Preserve all content. Insert STANDARDIZED comment. Output file only. $(cat docs/user-guide/old-page.md)"

# Audit a module
files-to-prompt docs/user-guide/03-trade --extension md | \
  gemini -p "$(cat .github/STYLE_SPEC.md)" \
  "Audit against STYLE_SPEC. Output: executive summary table + findings + prioritized backlog."

# Check if a page should be relocated
gemini -p "$(cat .github/STYLE_SPEC.md) $(grep -A200 '^nav:' mkdocs.yml)" \
  "Analyze optimal nav location per STYLE_SPEC §7. $(cat docs/user-guide/some-page.md)"
```

## Copilot Chat quick-start

```
@doc-writer Write a new page for Trade → Add Bank with screenshot at ../screenshots/trade/add-bank.png
@doc-standardizer Standardize docs/user-guide/03-trade/banks/add-bank.md
@doc-reviewer Review docs/user-guide/03-trade/invoices/create-invoice.md
@doc-relocator Should the release checklist be in 06-reference or somewhere else?
@doc-auditor Audit all pages in the 04-employee module
```
