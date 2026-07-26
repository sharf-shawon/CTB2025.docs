## Context

The `09-reference/` module covers critical troubleshooting and runtime guidance pages:

- Offline Mode (`offline-mode.md`)
- Error Pages (`error-pages.md`)

These pages require complete 9-section canonical structure (`STYLE_SPEC.md` v2.0), explicit technical step-by-step procedures for IndexedDB and service worker operations, and 4-column Exception Handling & Error Recovery matrices.

## Goals / Non-Goals

**Goals:**

- Rewrite `offline-mode.md` and `error-pages.md` to conform strictly to `STYLE_SPEC.md` v2.0 9-section structure.
- Add explicit step-by-step instructions for inspecting browser cache, verifying offline database status (IndexedDB), and manual synchronization.
- Add detailed 4-column Exception Handling & Error Recovery tables for HTTP status codes and synchronization conflict errors.

**Non-Goals:**

- Implementing any backend service workers or IndexedDB synchronization code in `CTB2025`.
- Rewriting or modifying code under `scripts/`.

## Decisions

### 1. Section Header Standardization

- **Decision**: Update both reference pages to use exact 9 H2 headings matching the canonical structure.
- **Rationale**: Ensures complete uniformity across the reference module and passes the style lint tool checks.
- **Alternatives Considered**: Keeping current custom sections, which violates the style guide contract.

### 2. Client-Side State Verification Steps

- **Decision**: Document Chrome DevTools Application tab procedures for checking Service Worker status, Cache Storage, and IndexedDB keys.
- **Rationale**: Provides system operators with concrete debugging steps when transactions are not syncing automatically.

## Risks / Trade-offs

- **[Risk]** Over-complicating technical instructions for non-technical users.
    - **Mitigation**: Separate simple operator steps from advanced developer/administrator console instructions in the step-by-step guide.
