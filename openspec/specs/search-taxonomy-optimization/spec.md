# search-taxonomy-optimization Specification

## Purpose

TBD - created by archiving change enhance-docs-search-and-nav-experience. Update Purpose after archive.

## Requirements

### Requirement: Search Frontmatter Tag Taxonomy

All user documentation pages SHALL include frontmatter `tags:` incorporating module scope, action category, target user role, and domain term aliases.

#### Scenario: User searches for a domain synonym

- **WHEN** a user enters a domain alias term (e.g. "bill", "paycheck", "receipt") into the MkDocs search bar
- **THEN** the search engine MUST return the relevant operational page matching the frontmatter taxonomy tags.

### Requirement: Indexing Consistency Across Modules

Every task and reference page SHALL maintain consistent frontmatter metadata headers (`tags`, `metadata: owner`, `last_updated`, `git_ref`).

#### Scenario: Linter checks frontmatter headers

- **WHEN** `python3 scripts/style_lint.py` inspects markdown documentation files
- **THEN** frontmatter blocks MUST be valid YAML arrays following canonical tag naming conventions.
