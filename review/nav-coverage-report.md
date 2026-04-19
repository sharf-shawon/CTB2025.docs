# Navigation Coverage Audit Report

Date: 2026-04-19

## Scope

- Audited all Markdown files under `docs/`
- Compared against Markdown targets listed in the `nav:` section of `mkdocs.yml`

## Results

- Missing nav targets: `0`
- Orphan docs files: `3`

## Orphan file list

- `_Footer.md`
- `_Header.md`
- `_Sidebar.md`

## Orphan assessment

These three files are intentional helper/fragment files and are already excluded via `exclude_docs` in `mkdocs.yml`. They are not user-facing pages and should not be added to navigation.

## Release impact

- Navigation coverage is complete for user-facing pages.
- No nav references point to missing files.
- No release blocker identified from navigation coverage.
