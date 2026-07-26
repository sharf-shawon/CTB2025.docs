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

- You see a **403 Forbidden** error screen after clicking a link or saving a form.
- A **404 Not Found** page appears after following a bookmark or entering a URL.
- A **500 Server Error** screen occurs during form submission or report generation.
- The system displays a **Maintenance Mode** lock message.

______________________________________________________________________

## How to access this page

From the sidebar navigation, select **Reference → Error Pages** (`/user-guide/09-reference/error-pages/`).

______________________________________________________________________

## Prerequisites

- Active user session in CTB Admin.
- Accessible by all authenticated user roles (`staff`, `accountant`, `hr`, `admin`).

______________________________________________________________________

## Step-by-step instructions

1. Identify the HTTP status code or screen title (e.g., 403, 404, 500, or Maintenance Mode).
1. Match the error code against the **Common error screens and diagnostic matrix** in the Field reference section below.
1. Follow the exact remediation steps assigned to your user role in the **Exception handling & error recovery** section.
1. If the error persists, note the exact URL, error code, and timestamp before contacting a system administrator.

______________________________________________________________________

## Verification & definition of done

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

## Exception handling & error recovery

| Error Code / Symptom                   | Root Cause                                      | Step-by-step remediation procedure                                                                                                                                                                                                          | Actionable role required      |
| -------------------------------------- | ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- |
| **403** / "You do not have permission" | User account lacks specific permission codename | 1. Confirm current user role.<br>2. Contact an administrator to request the specific Django permission codename (e.g. `trade.add_invoice`).<br>3. Log out and log back in to refresh permissions.                                           | `staff` $\rightarrow$ `admin` |
| **404** / "Page or record not found"   | Invalid URL parameter or record deleted         | 1. Verify the record ID in the URL bar.<br>2. Open the module overview list and search for the record.<br>3. Check **Audit Log** to verify if another user deleted the record.                                                              | `staff` / `accountant` / `hr` |
| **500** / "Unexpected server error"    | Server exception or database timeout            | 1. Do NOT resubmit the form repeatedly.<br>2. Refresh the browser once to test if the connection recovers.<br>3. Open **Audit Log** to see if changes were partially saved.<br>4. Report the exact steps and timestamp to an administrator. | `staff` $\rightarrow$ `admin` |
| **503** / "System under maintenance"   | Administrator enabled Maintenance Mode          | 1. Wait for maintenance to finish (typically 10-15 minutes).<br>2. Superusers can sign in via `/admin/` to toggle **Maintenance Mode** off in **App Settings**.                                                                             | `staff` $\rightarrow$ `admin` |

______________________________________________________________________

## Related workflows & next steps

- **[App Settings](../08-settings-and-admin/app-settings.md)** — Toggle Maintenance Mode and update global parameters.
- **[Audit Log](../08-settings-and-admin/audit-log.md)** — Reconcile system errors and access attempts.

______________________________________________________________________

## Related pages

- **[Reference](../README.md)** — Glossary, error matrices, and shortcut guides.
