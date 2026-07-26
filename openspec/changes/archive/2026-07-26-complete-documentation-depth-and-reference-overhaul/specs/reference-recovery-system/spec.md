## ADDED Requirements

### Requirement: Error pages documentation SHALL provide actionable remediation matrices

The `docs/user-guide/09-reference/error-pages.md` and `troubleshooting.md` pages SHALL include structured exception tables mapping symptoms, HTTP status codes, root causes, and step-by-step remediation procedures for non-technical users.

#### Scenario: Diagnosing a system error screen

- **WHEN** a user encounters a 403, 404, 500, or Maintenance Mode screen
- **THEN** `error-pages.md` provides a diagnostic table specifying the exact root cause, required role access, and recovery steps.

### Requirement: Glossary documentation SHALL provide deep domain business definitions

The `docs/user-guide/09-reference/glossary.md` page SHALL provide authoritative definitions for all business and domain-specific terms used throughout CTB Admin.

#### Scenario: Looking up business domain terminology

- **WHEN** a user searches for domain terms such as "Chalan", "Voucher", "Tender Invoice", or "Purchase Balance"
- **THEN** `glossary.md` defines the term, explains its context within CTB Admin, and links to the relevant task module.

### Requirement: Offline mode documentation SHALL specify offline operational behaviors

The `docs/user-guide/09-reference/offline-mode.md` page SHALL detail Service Worker caching mechanisms, offline fallback capabilities, read vs write limitations, and network reconnection procedures.

#### Scenario: Operating CTB Admin documentation while offline

- **WHEN** a user loses network connectivity while accessing the documentation
- **THEN** `offline-mode.md` documents what cached content remains accessible and how to refresh stale assets upon reconnecting.
