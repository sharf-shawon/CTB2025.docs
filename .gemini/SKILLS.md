# Gemini CLI Skills — CTB2025 Docs

<!-- Auto-loaded by gemini CLI when run from repo root -->

<!-- Source of truth: .github/STYLE_SPEC.md | Knowledge: .github/knowledge/ -->

## Common preamble (always include)

```bash
SPEC="$(cat .github/STYLE_SPEC.md)"
KNOWLEDGE="$(cat .github/knowledge/ctb-knowledge.md)"
LEARNINGS="$(cat .github/knowledge/copilot-learnings.md)"
```

______________________________________________________________________

## write-doc

**Token budget:** ~2,800 (STYLE_SPEC + knowledge + mkdocs.yml nav section)

```bash
# Usage: FILE=docs/user-guide/03-trade/banks/add-bank.md MODULE=trade \
#        TITLE="Add Bank" make write-doc
gemini -p "$SPEC $KNOWLEDGE" \
  "Write a new page at $FILE for module $MODULE, title: $TITLE. \
   Screenshot path: docs/user-guide/screenshots/$MODULE/. \
   Nav context: $(grep -A5 '$TITLE' mkdocs.yml || echo 'not yet in nav'). \
   Follow STYLE_SPEC section 3 template exactly. Output raw markdown only, no fences."
```

______________________________________________________________________

## standardize

**Token budget:** ~2,000 + file size (use when a page is known to be non-compliant)

```bash
# Usage: FILE=docs/user-guide/03-trade/invoices/create-invoice.md make standardize
gemini -p "$SPEC" \
  "Rewrite to STYLE_SPEC v1. Preserve all facts, screenshots, links. \
   Insert '<!-- STANDARDIZED: STYLE_SPEC v1 -->' on line 2. \
   Output raw markdown only. $(cat $FILE)"
```

______________________________________________________________________

## review-page

**Token budget:** ~2,000 + file size

```bash
# Usage: FILE=docs/user-guide/04-employee/salary/generate-salary.md make review-page
gemini -p "$SPEC $LEARNINGS" \
  "Review this page against STYLE_SPEC. For each violation output: \
   | Dimension | Severity | Finding | Fix |. \
   Then output a self-check table (STYLE_SPEC section 8). \
   $(cat $FILE)"
```

______________________________________________________________________

## audit-module

**Token budget:** ~15K (use Gemini 2.5 Pro; use for single module scans)

```bash
# Usage: MODULE=docs/user-guide/03-trade make audit-module
files-to-prompt $MODULE --extension md | \
  gemini -m gemini-2.5-pro -p "$SPEC $KNOWLEDGE" \
  "Audit all pages against STYLE_SPEC. Output: \
   1) Executive summary table (A-G dimensions). \
   2) File-by-file findings. \
   3) Prioritized backlog P1-P4. \
   4) Suggested agent dispatch table: | File | Agent | Priority |."
```

______________________________________________________________________

## full-audit

**Token budget:** LARGE — use gemini-2.5-pro; only run on-demand, never in CI

```bash
# Usage: make full-audit
files-to-prompt docs/user-guide --extension md | \
  gemini -m gemini-2.5-pro -p "$SPEC $KNOWLEDGE" \
  "Full audit all modules. Same output format as audit-module. \
   Flag all relocation candidates and duplicate content."
```

______________________________________________________________________

## analyze-relocation

**Token budget:** ~3,500 (includes full nav context)

```bash
# Usage: FILE=docs/user-guide/some-page.md make analyze-relocation
gemini -p "$SPEC $(cat mkdocs.yml)" \
  "Analyze optimal nav location for this page using STYLE_SPEC section 7. \
   Output Phase 1 analysis (location, rationale, impact) only. \
   Do NOT move any files. $(cat $FILE)"
```

______________________________________________________________________

## sync-nav

**Token budget:** ~500 (Python script only)

```bash
# Usage: make sync-nav
uv run python main.py nav-sync
```

______________________________________________________________________

## release-notes

**Token budget:** ~2,000 (git log only + STYLE_SPEC)

```bash
# Usage: SINCE="2 weeks ago" make release-notes
gemini -p "$SPEC" \
  "Summarize these git commits as user-facing release notes for \
   docs/user-guide/06-reference/production-release-summary.md. \
   Group by module. Use MkDocs admonitions. User audience, no code terms. \
   $(git -C ../CTB2025 log --oneline --since='$SINCE' 2>/dev/null || echo 'Git log unavailable')"
```

______________________________________________________________________

## Makefile snippet

Add these targets to a `Makefile` at repo root:

```makefile
SPEC := $(shell cat .github/STYLE_SPEC.md)
KNOWLEDGE := $(shell cat .github/knowledge/ctb-knowledge.md)

write-doc:
	@test -n "$(FILE)" || (echo "ERROR: FILE= required" && exit 1)
	gemini -p "$(SPEC) $(KNOWLEDGE)" "Write a new page at $(FILE). Follow STYLE_SPEC section 3. Output raw markdown only."

standardize:
	@test -n "$(FILE)" || (echo "ERROR: FILE= required" && exit 1)
	gemini -p "$(SPEC)" "Rewrite to STYLE_SPEC v1. Preserve all facts. Insert STANDARDIZED comment line 2. $(shell cat $(FILE))"

review-page:
	@test -n "$(FILE)" || (echo "ERROR: FILE= required" && exit 1)
	gemini -p "$(SPEC)" "Review against STYLE_SPEC. Output violations table + self-check. $(shell cat $(FILE))"

audit-module:
	@test -n "MODULE)" || (echo "ERROR: MODULE= required" && exit 1)
	files-to-prompt $(MODULE) --extension md | gemini -m gemini-2.5-pro -p "$(SPEC) $(KNOWLEDGE)" "Full module audit. Output P1-P4 backlog + dispatch table."

full-audit:
	files-to-prompt docs/user-guide --extension md | gemini -m gemini-2.5-pro -p "$(SPEC) $(KNOWLEDGE)" "Full audit all modules."

sync-nav:
	uv run python main.py nav-sync
```
