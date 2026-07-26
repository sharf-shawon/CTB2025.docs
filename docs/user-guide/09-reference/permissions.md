---
tags: [module:reference, task:configure, role:admin]
---

# Permissions

<!-- metadata: owner: admin, last_updated: 2026-07-26, git_ref: main, staging_verified: true -->

Manage system access control levels, user role privileges, and explicit Django permission codenames in CTB Admin.

## Summary

CTB Admin enforces a three-tier security model: account-wide **Staff status** and **Superuser** flags, module-level view permissions, and granular action-level permissions (Add, Change, Delete) mapped directly to underlying Django permission codenames. Use this page to configure user permissions and diagnose access restrictions.

______________________________________________________________________

## When to use this page

- When onboarding new system users in **Settings and Admin → User Management**.
- When assigning job-specific access roles (Office Staff, Accountant, HR, Administrator).
- When investigating a `403 Forbidden` error or a missing sidebar module entry.
- When troubleshooting why a specific button (e.g., **Approve**, **Delete**, **Export**) is hidden for a user.

______________________________________________________________________

## How to access this page

From the sidebar navigation, Go to **Reference → Permissions**. Permissions are managed administratively under **Settings and Admin → User Management**.

______________________________________________________________________

## Prerequisites

- **Role permissions**: Reading this reference page is available to all users (`staff`, `admin`). Modifying user permissions requires **Superuser** status or `auth.change_user` permission.
- **Prerequisites**: Active administrator access to **User Management**.

______________________________________________________________________

## Step-by-step instructions

1. Confirm the target user account has **Staff status** enabled; without this flag, access to CTB Admin is blocked completely.
1. Identify the specific business module and action the user requires (e.g., creating an invoice or viewing salary details).
1. Go to **Settings and Admin → User Management** and edit the target user account.
1. Check the explicit Django permission codename corresponding to the required action (see the Permission Codename Matrix below).
1. Click **Save** and instruct the user to sign out and log back in to refresh their permission session.

______________________________________________________________________

## Verification and definition of done

- **Access verification**: The user logs in and can view the assigned module sidebar entry and perform allowed actions without encountering a 403 error.
- **Audit logging**: Permission changes are logged under **Settings and Admin → Audit Log**.

______________________________________________________________________

## Field reference

### Core access tier definitions

| Access Tier                | Granting Option       | Functional Scope                                                                                               |
| -------------------------- | --------------------- | -------------------------------------------------------------------------------------------------------------- |
| **Staff Status**           | Checkbox in User Form | Master toggle enabling entry to the CTB Admin web interface.                                                   |
| **Superuser Flag**         | Checkbox in User Form | Bypasses all permission checks; grants full read/write/delete access across all modules and balance overrides. |
| **Module View Permission** | Assigned Permission   | Controls sidebar visibility and page load access for a specific module.                                        |
| **Action Permission**      | Assigned Codename     | Controls specific Add, Change, or Delete operations within a module.                                           |

### Module-to-Django permission codename matrix

| Module Area  | Action                     | Explicit Django Permission Codename | Functional Access Granted                                         |
| ------------ | -------------------------- | ----------------------------------- | ----------------------------------------------------------------- |
| **Business** | Add Client                 | `business.add_client`               | Create new Client profiles and configure credit limits.           |
| **Business** | Edit Client                | `business.change_client`            | Update Client contact information or balance limits.              |
| **Trade**    | Create Invoice             | `trade.add_invoice`                 | Generate sales Invoices, Tender Invoices, and Quotations.         |
| **Trade**    | Edit Invoice               | `trade.change_invoice`              | Modify draft invoice items or amounts.                            |
| **Trade**    | Approve Over-Limit Invoice | `superuser_only`                    | Approve Invoices exceeding Client balance limits.                 |
| **Trade**    | Record Payment             | `trade.add_payment`                 | Log incoming Client payments or outgoing Vendor funds.            |
| **Employee** | Record Attendance          | `employee.add_attendance`           | Log manual employee check-in/check-out and overtime.              |
| **Employee** | Generate Salary            | `employee.add_salary`               | Process monthly Salary payroll records.                           |
| **Employee** | View Salary Details        | `employee.view_salary`              | View staff Salary rates (if **Hide Salary Details** is disabled). |
| **Admin**    | App Settings               | `settings.change_appsetting`        | Configure global system options and maintenance mode.             |
| **Admin**    | View Audit Log             | `admin.view_auditlog`               | Inspect immutable system audit history.                           |

______________________________________________________________________

## Exception handling and error recovery

| Issue / Symptom                                      | Root Cause                                       | User remediation step                                                     | Role required     |
| ---------------------------------------------------- | ------------------------------------------------ | ------------------------------------------------------------------------- | ----------------- |
| User cannot access CTB Admin login at all            | Account lacks **Staff status** flag              | Open **User Management**, edit account, check **Staff status**, and save. | `admin`           |
| Module missing from sidebar after permission granted | User session cache retains old permission state  | Instruct user to sign out and log back in to reload permission tokens.    | `staff` / `admin` |
| **Approve** button hidden on over-limit invoice      | Balance limit overrides require Superuser status | A superuser must sign in to click **Approve** on the invoice form.        | `superuser`       |

______________________________________________________________________

## Related pages

- **[User Management Guide](../08-settings-and-admin/user-management.md)** — Step-by-step instructions for managing user permissions.
- **[Troubleshooting Guide](troubleshooting.md)** — Self-service diagnostic steps for permission blockages.
- **[Error Pages](error-pages.md)** — Explanations and recovery steps for 403 Forbidden screens.
