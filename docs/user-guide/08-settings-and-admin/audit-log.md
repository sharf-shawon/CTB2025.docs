---
tags: [module:settings, task:configure, role:admin]
---

# Audit Log

## Summary

The Audit Log records an immutable system trail of user actions across CTB Admin, capturing who created, modified, or deleted data, exact timestamps, and before/after field changes. Use it to verify operational activity, investigate data anomalies, and support security reviews.

______________________________________________________________________

## When to use this page

- Investigating who created, edited, or deleted an invoice, payment, voucher, or employee record.
- Auditing security events and administrative setting changes.
- Verifying compliance with internal control policies and financial audit requirements.
- Resolving dispute discrepancies regarding transaction dates or record modifications.

______________________________________________________________________

## How to access this page

From the sidebar navigation, select **Audit Log** (`/admin/admin/logentry/`).

![Audit Log page](audit-log.png)

______________________________________________________________________

## Prerequisites

- Active user session with `admin.view_logentry` or superuser permissions.
- Audit logging enabled in CTB Admin backend settings.

______________________________________________________________________

## Step-by-step instructions

1. Open **Settings and Admin → Audit Log** from the sidebar.
1. Apply **User**, **Action** (Addition, Change, Deletion), or **Date** filters to narrow search results.
1. Locate the specific log entry for the target object or user session.
1. Click the log entry link to view complete **Change Details** including before/after values.
1. Note the timestamp, user ID, and modified field names for your compliance record.

______________________________________________________________________

## Verification & definition of done

- **Log entry generated**: Every database addition, change, or deletion automatically appends a corresponding log entry to the table.
- **Traceability confirmed**: Log entries contain valid links to target model objects and user accounts.

______________________________________________________________________

## Field reference

- **User** — User account responsible for performing the action.
- **Action** — Type of database operation: `Addition`, `Change`, or `Deletion`.
- **Object** — Name and primary key identifier of the affected record.
- **Module/App** — System module where the event occurred (e.g., `Trade`, `Business`, `Employee`).
- **Timestamp** — Exact server date and time (`YYYY-MM-DD HH:MM:SS`) when the event was saved.
- **Change Details** — JSON representation or bulleted summary of before and after field values.

______________________________________________________________________

## Exception handling & error recovery

| Error Code / Symptom          | Root Cause                                                             | Step-by-step remediation procedure                                                                                                           | Actionable role required |
| ----------------------------- | ---------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------ |
| `403 Forbidden` on log access | User account lacks `admin.view_logentry` permission                    | 1. Contact a system administrator to request `admin.view_logentry`.<br>2. Re-authenticate to apply updated permissions.                      | `admin`                  |
| Missing audit entries         | Action performed via direct database bypass without Django ORM signals | 1. Ensure all administrative operations occur via CTB Admin UI or authenticated API.<br>2. Review server access logs for direct DB sessions. | `admin`                  |

______________________________________________________________________

## Related workflows & next steps

- **[User Management](user-management.md)** — Review and manage user permissions.
- **[App Settings](app-settings.md)** — Adjust system-wide settings and security parameters.

______________________________________________________________________

## Related pages

- **[Settings and Admin](../README.md)** — All system configuration and security administration tools.
