## 1. Automated Screenshot Capture & Gallery Integration

- [x] 1.1 Configure browser subagent screenshot task scripts for `ctb-staging-mcp-server`.
- [x] 1.2 Replace `<!-- TODO: screenshot ... -->` placeholders across core module pages with captured assets.
- [x] 1.3 Register captured graphics in `gallery.md` categories (`admin.md`, `dashboard.md`, `mobile.md`, `reports.md`).

## 2. CI Dual-MCP Verification Automation

- [x] 2.1 Create `.github/workflows/docs-mcp-verify.yml` to run automated model & DOM field validation.
- [x] 2.2 Add pre-commit hook enforcing permission codename and status pill validation.

## 3. Release Tag & Versioning Linkage

- [x] 3.1 Implement GitHub Release tag sync script updating `09-reference/README.md` changelog links.
- [x] 3.2 Configure `git-revision-date-localized` release tags in `mkdocs.yml`.

## 4. SME Review Pipeline & Auditing

- [x] 4.1 Build automated `review/sme-checklist.md` generator tracking pending product verification items.
- [x] 4.2 Run final validation suite using `python3 scripts/style_lint.py` and `uv run mkdocs build --strict`.
