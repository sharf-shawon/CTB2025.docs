## Context

The `08-settings-and-admin/` module covers critical security and system management pages:

- App Settings (`app-settings.md`)
- Audit Log (`audit-log.md`)
- SMS Settings (`sms-settings.md`)
- User & Role Management (`users.md` / `roles.md`)

These pages require complete 9-section canonical structure (`STYLE_SPEC.md` v2.0), explicit permission codenames, and detailed troubleshooting procedures for administrative lockouts or gateway errors.

## Goals / Non-Goals

**Goals:**

- Standardize all pages in `docs/user-guide/08-settings-and-admin/` to canonical 9-section structure.
- Add explicit step-by-step procedures for audit trail inspection, user permission assignment, and Maintenance Mode toggles.
- Add 4-column Exception Handling & Error Recovery matrices covering 403 Forbidden errors, gateway timeouts, and invalid API keys.

**Non-Goals:**

- Modifying backend Django auth permissions or database migrations in `CTB2025`.
- Exposing secret API keys or production environment passwords in documentation examples.

## Decisions

### 1. Permission Codename Mapping Table

- **Decision**: Document exact Django permission codenames (e.g. `auth.add_user`, `admin.change_logentry`) in Prerequisites and Field Reference sections.
- **Rationale**: Enables system administrators to configure fine-grained role permissions in Django admin without guessing codenames.
- **Alternatives Considered**: Generic textual descriptions like "needs user management rights", which are too ambiguous for security administration.

### 2. Maintenance Mode Safeguards

- **Decision**: Explicitly document superuser bypass procedures (`/admin/` URL access) during active Maintenance Mode lockouts.
- **Rationale**: Prevents administrators from being locked out of the system if Maintenance Mode is enabled inadvertently.

## Risks / Trade-offs

- **[Risk]** Security exposure of internal configuration keys.
    - **Mitigation**: Use explicit placeholders (e.g. `SMS_API_KEY_XXXXX`) in all code blocks and screenshot examples.
