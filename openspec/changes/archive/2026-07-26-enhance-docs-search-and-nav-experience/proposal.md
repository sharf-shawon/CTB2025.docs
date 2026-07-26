## Why

While individual documentation pages are detailed, users often struggle to discover pages using colloquial business search terms (e.g., "paycheck", "bill", "slip") or transition smoothly between connected business workflows (e.g. Invoice $\rightarrow$ Payment $\rightarrow$ Voucher).

Enhancing search taxonomy indexing and establishing explicit cross-module workflow link graphs enables seamless site navigation and instant search discovery across all 10 documentation modules.

## What Changes

- **Search Taxonomy & Keyword Indexing**: Add comprehensive tags, aliases, and common domain search terms (e.g. `bill`, `slip`, `receipt`, `paycheck`) to page YAML frontmatter and content sections.
- **Cross-Module Link Graph Integration**: Build bidirectional contextual links in `## Related workflows & next steps` and `## Related pages` across interconnected processes (e.g., Client $\rightarrow$ Invoice $\rightarrow$ Payment $\rightarrow$ Voucher).
- **Navigation & Sub-Section Alignment**: Audit and align `mkdocs.yml` navigation structure to ensure logical hierarchy and zero orphan pages.

## Capabilities

### New Capabilities

- `search-taxonomy-optimization`: Standardized metadata frontmatter indexing and search keyword mapping for MkDocs search discovery.
- `cross-module-link-graph`: Structured workflow linking connecting upstream prerequisite actions to downstream financial and inventory operations.

### Modified Capabilities

*(None)*

## Impact

- **Frontmatter & Navigation**: Modifies `tags:` in page frontmatter across `docs/user-guide/` files and updates `mkdocs.yml`.
- **Search Performance**: Improves instant query relevance for non-technical users in MkDocs Material search.
- **Build Integrity**: Checked via `python3 scripts/style_lint.py` and `uv run mkdocs build --strict`.
