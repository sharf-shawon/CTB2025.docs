---
tags: [module:reference, task:troubleshoot, role:staff]
---

# Troubleshooting

<!-- metadata: owner: staff, last_updated: 2026-07-26, git_ref: main, staging_verified: true -->

Diagnose and resolve common operational warnings, form submission errors, calculation discrepancies, and system issues in CTB Admin.

## Summary

Use this troubleshooting guide when encountering an unexpected system response, missing screen element, failed record save, or calculation issue. Each section provides immediate diagnostic checks and direct links to full feature documentation.

______________________________________________________________________

## When to use this page

- When an error screen (403, 404, 500, Maintenance) appears.
- When an expected button (e.g., **Approve**, **Delete**, **Save**) is disabled or missing.
- When a record fails to save or highlights validation warnings.
- When report totals, invoice balances, or net salary figures do not update as expected.
- When site performance feels slow or cached pages appear out of date.

______________________________________________________________________

## How to access this page

From the sidebar navigation, Go to **Reference → Troubleshooting**. Direct access URL: `/user-guide/09-reference/troubleshooting/`.

______________________________________________________________________

## Prerequisites

- **Role permissions**: Accessible by all authenticated user roles (`staff`, `accountant`, `hr`, `admin`).
- **Prerequisites**: Access to CTB Admin interface and error details/symptoms.

______________________________________________________________________

## Step-by-step instructions

1. Identify the symptom category below (Error screens, Missing UI elements, Record save failures, Calculation issues, or Performance).
1. Match your specific issue against the diagnostic resolution matrix.
1. Perform the recommended remediation step.
1. If the problem persists, capture the exact error message, URL bar text, and user ID before contacting support.

______________________________________________________________________

## Verification and definition of done

- **Issue resolution**: The user successfully completes the blocked operation or resolves the calculation/system warning.
- **Audit trace**: Complex data changes or administrative overrides can be verified in **Settings and Admin → Audit Log**.

______________________________________________________________________

## Field reference

### Master operational troubleshooting matrix

| Problem Category      | Symptom                               | Likely Root Cause                                                        | Step-by-step resolution                                                                 |
| --------------------- | ------------------------------------- | ------------------------------------------------------------------------ | --------------------------------------------------------------------------------------- |
| **Error Screen**      | `403 Forbidden` screen appears        | Missing Django permission codename or session expired                    | Confirm session login, then request missing permission codename in **User Management**. |
| **Error Screen**      | `404 Not Found` screen appears        | Broken link or deleted database record                                   | Verify URL record ID or search for record in module overview list.                      |
| **Error Screen**      | `500 Server Error` screen appears     | Unhandled server exception or invalid data payload                       | Refresh browser once; check **Audit Log** before resubmitting.                          |
| **Missing Button**    | **Approve** button missing on invoice | Invoice does not exceed Client balance limit, or user is not a superuser | Confirm invoice amount exceeds limit; sign in as superuser to approve.                  |
| **Missing Button**    | Invoice locked in `Draft` state       | Exceeds Client balance limit and lacks superuser approval                | Have a superuser click **Approve** to unlock **Sent** status.                           |
| **Missing Button**    | Salary figures hidden or masked       | **Hide Salary Details** setting enabled in App Settings                  | Admin must toggle setting off or user must sign in with superuser role.                 |
| **Save Failure**      | "Required field missing" alert        | One or more mandatory fields (`*`) are empty                             | Complete all red-asterisk fields before clicking **Save**.                              |
| **Save Failure**      | Invoice or Voucher fails to save      | Linked Client or Bank record is inactive or missing                      | Verify prerequisite Client/Bank account exists and is marked **Active**.                |
| **Calculation Issue** | Invoice Payable total unchanged       | Tax, shipping, or discount field input not registered                    | Re-enter numerical values and tab out of input box to trigger calculation.              |
| **Calculation Issue** | Dashboard metrics look out of date    | Dashboard metrics cache refreshes every 15 minutes                       | Click **Refresh** button on Dashboard header to force recalculation.                    |

______________________________________________________________________

## Exception handling and error recovery

| Issue / Symptom                         | Root Cause                                  | User remediation step                                                                       | Role required     |
| --------------------------------------- | ------------------------------------------- | ------------------------------------------------------------------------------------------- | ----------------- |
| Record values changed unexpectedly      | Another user modified or updated the record | Open **Settings and Admin → Audit Log** and filter by record SKU/ID to view change history. | `staff` / `admin` |
| Form data lost during browser crash     | Unsaved form state in local memory          | Re-open form and re-enter data; save drafts frequently using **Save and continue editing**. | `staff`           |
| Search bar fails to return known record | Record is inactive or user lacks permission | Toggle "Include Inactive" filter or confirm module permission in **User Management**.       | `staff` / `admin` |

______________________________________________________________________

## Related pages

- **[Permissions Guide](permissions.md)** — Detailed mapping of permissions, roles, and restrictions.
- **[Error Pages](error-pages.md)** — Comprehensive coverage of HTTP error screens and server failures.
- **[Offline Mode](offline-mode.md)** — PWA Service Worker caching and offline behavior guide.
- **[Audit Log Guide](../08-settings-and-admin/audit-log.md)** — Detailed instructions for auditing data modifications.
