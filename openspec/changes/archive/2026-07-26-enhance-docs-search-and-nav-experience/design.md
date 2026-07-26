## Context

MkDocs Material builds a client-side search index based on page titles, headers, frontmatter tags, and body text. Currently, user search queries for non-canonical or regional business terms (e.g. "slip", "bill", "paycheck", "vendor receipt") may yield sub-optimal search ranking or missing results. Furthermore, users navigating multi-step operational workflows need explicit links between prerequisite tasks and downstream operations.

## Goals / Non-Goals

**Goals:**

- Enrich page frontmatter `tags:` across all primary modules with standardized module, task, role, and domain alias terms.
- Add explicit cross-module workflow link graphs in `## Related workflows & next steps` and `## Related pages` across Trade, Business, Factory, and Employee modules.
- Ensure all internal markdown links resolve cleanly without broken link warnings in `mkdocs build --strict`.
- Verify zero structural or heading violations using `python3 scripts/style_lint.py`.

**Non-Goals:**

- Installing third-party JavaScript search plugins outside standard MkDocs Material built-ins.
- Modifying backend Django routing or core site navigation hierarchy in `mkdocs.yml` unless broken nav entries are found.

## Decisions

### 1. Frontmatter Tagging Standard: Multi-Dimensional Tag Taxonomy

- **Decision**: Structure frontmatter `tags:` using standard key-value patterns:
    `tags: [module:<name>, task:<action>, role:<role>, alias:<term1>, alias:<term2>]`
- **Rationale**: MkDocs Material indexes tags directly into its search engine, allowing instant search matching for colloquial or synonym terms without cluttering readable body prose.
- **Alternatives Considered**: Adding synonym word lists in raw paragraph text, which dilutes document readability and violates `STYLE_SPEC.md` §2 filler rules.

### 2. Workflow Link Graph Design: Upstream / Downstream Mapping

- **Decision**: Map explicit bidirectional links between related operations:
    - Client Onboarding $\leftrightarrow$ Invoice Creation $\leftrightarrow$ Payment Receipt $\leftrightarrow$ Client Ledger
    - Vendor Registration $\leftrightarrow$ Purchase Voucher $\leftrightarrow$ Vendor Payout $\leftrightarrow$ Material Inventory
    - Attendance Record $\leftrightarrow$ Monthly Salary Generation $\leftrightarrow$ Salary Payout
- **Rationale**: Guides business users through multi-stage operational lifecycles without requiring manual sidebar navigation searches.
- **Alternatives Considered**: Generic single links to module root folders, which fails to provide context-aware next steps.

## Risks / Trade-offs

- **[Risk]** Adding relative file links could introduce broken path warnings during MkDocs build.
    - **Mitigation**: Always run `uv run mkdocs build --strict` to validate every internal link path.
- **[Risk]** Frontmatter tag inflation making YAML header unreadable.
    - **Mitigation**: Limit tags to 4-7 relevant terms per page focusing strictly on primary domain aliases.
