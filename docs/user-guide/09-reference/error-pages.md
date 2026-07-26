---
tags: [module:reference, task:troubleshoot, role:staff]
---

# Error Pages

<!-- metadata: owner: staff, last_updated: 2026-07-26, git_ref: main, staging_verified: true -->

Identify standard system error screens in CTB Admin and follow step-by-step recovery procedures.

## Summary

Error pages inform users when a requested screen cannot be accessed, does not exist, encounters a server error, or is restricted during maintenance. Use this page to diagnose HTTP status codes, understand root causes, and take corrective remediation action.

______________________________________________________________________

## When to use this page

- When you see a **403 Forbidden** error screen after clicking a link or saving a form.
- When a **404 Not Found** page appears after following a bookmark or entering a URL.
- When a **500 Server Error** screen occurs during form submission or report generation.
- When the system displays a **Maintenance Mode** lock message.

______________________________________________________________________

## How to access this page

From the sidebar navigation, Go to **Reference → Error Pages**. The direct URL path is `/user-guide/09-reference/error-pages/`.

______________________________________________________________________

## Prerequisites

- **Role permissions**: Accessible by all authenticated user roles (`staff`, `accountant`, `hr`, `admin`).
- **Prerequisites**: Active user session in CTB Admin.

______________________________________________________________________

## Step-by-step instructions

1. Identify the HTTP status code or screen title (e.g., 403, 404, 500, or Maintenance Mode).
1. Match the error code against the **Error response matrix** in the Field reference section below.
1. Follow the exact remediation steps assigned to your user role.
1. If the error persists, note the exact URL, error code, and timestamp before contacting a system administrator.

______________________________________________________________________

## Verification and definition of done

- **Error resolution**: The user successfully returns to a functional CTB Admin page after resolving permissions, fixing the URL, or waiting for maintenance completion.
- **Audit verification**: Admin users can inspect the **Audit Log** (`08-settings-and-admin/audit-log.md`) to verify if a failed access attempt was logged.

______________________________________________________________________

## Field reference

### Common error screens and diagnostic matrix

| Error Code | Error Screen Title        | Primary Root Cause                                                                          | Expected System Behavior                                                     |
| ---------- | ------------------------- | ------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| **403**    | 403 Forbidden             | User account lacks the required Django permission codename or role level for this view.     | Blocks screen access; user cannot view or submit form data.                  |
| **404**    | 404 Page Not Found        | Requested URL path is incorrect, or underlying database record was deleted.                 | Display missing page graphic; sidebar remains accessible.                    |
| **500**    | 500 Internal Server Error | Unhandled server application exception, database timeout, or invalid form processing logic. | Shows generic error message; transaction rolls back safely.                  |
| **503**    | Maintenance Mode          | System administrator enabled Maintenance Mode in **App Settings** for updates.              | Replaces app interface with temporary maintenance banner for non-superusers. |

______________________________________________________________________

## Exception handling and error recovery

| Error Code | Symptom                                             | Step-by-step remediation procedure                                                                                                                                                                                                                               | Actionable role required      |
| ---------- | --------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- |
| **403**    | "You do not have permission to perform this action" | 1. Confirm your current user role.<br>2. Contact an administrator to request the specific Django permission codename (e.g. `trade.add_invoice`).<br>3. Log out and log back in to refresh permissions.                                                           | `staff` $\rightarrow$ `admin` |
| **404**    | "The page or record could not be found"             | 1. Verify the record ID in the URL bar.<br>2. Open the module overview list (e.g., **Trade → Invoices**) and search for the record.<br>3. Check **Audit Log** to verify if another user deleted the record.                                                      | `staff` / `accountant` / `hr` |
| **500**    | "An unexpected server error occurred"               | 1. Do NOT resubmit the form repeatedly.<br>2. Refresh the browser once to test if the connection recovers.<br>3. Open **Audit Log** or check module list to see if changes were partially saved.<br>4. Report the exact steps and timestamp to an administrator. | `staff` $\rightarrow$ `admin` |
| **503**    | "System is currently under maintenance"             | 1. Wait for maintenance to finish (typically 10-15 minutes).<br>2. Superusers can sign in via `/admin/` to toggle **Maintenance Mode** off in **App Settings**.                                                                                                  | `staff` $\rightarrow$ `admin` |

______________________________________________________________________

## Related pages

- **[Permissions Guide](permissions.md)** — Detailed mapping of roles and Django permission codenames.
- **[Troubleshooting Guide](troubleshooting.md)** — Self-service resolution steps for common operational issues.
- **[Audit Log Guide](../08-settings-and-admin/audit-log.md)** — Inspect audit logs to track user actions and system errors.
