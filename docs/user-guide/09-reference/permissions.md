---
tags: [module:reference, task:configure, role:admin]
---

# Permissions

Who can see and change each area of CTB Admin, and the specific restrictions that apply to individual actions.

## Summary

CTB Admin controls access at three levels: an account-wide **Staff status** and **Superuser** flag, module-specific permissions, and action-level permissions within each module. Use this page to work out which of the three is blocking an action before you change anything.

______________________________________________________________________

## When to use this page

- A user reports a `403` error or a missing sidebar entry.
- A button such as **Approve** or **Delete** is not visible to a user who expects it.
- You are deciding what to grant a new account on the **User Management** page.
- You need to confirm whether a restriction is a permission or a record-state rule.

______________________________________________________________________

## How to access this page

Permissions themselves are set in **Settings and Admin → User Management**. This page is reference material and needs no permission to read.

______________________________________________________________________

## Prerequisites

- Superuser or administrator permission to change any of the settings described here.

______________________________________________________________________

## Step-by-step instructions

1. Confirm the user is signed in. A signed-out session produces the same `403` screen as a genuine permission problem.
1. Check **Staff status** on the account. Without it the user cannot reach the CTB Admin interface at all.
1. Check the module permission for the area in question.
1. Check the action permission (Add, Change, Delete) within that module.
1. If all three are granted and the action is still unavailable, check the record-state restrictions in the table below — those are business rules, not permissions, and cannot be granted away.

______________________________________________________________________

## Field reference

The three permission levels, as set on the **User Management** page:

| **Permission**                  | What to do                       | Description                                                         |
| ------------------------------- | -------------------------------- | ------------------------------------------------------------------- |
| **Staff status**                | Enable for most users            | Grants access to the CTB Admin interface at all                     |
| **Superuser**                   | Grant sparingly                  | Admin-level access to every module and setting                      |
| **Module-specific permissions** | Grant per module                 | Access to Business, Factory, Trade, Employee, and the other modules |
| **Action-level permissions**    | Grant per action within a module | Controls Add, Change, and Delete separately inside each module      |

Assign the minimum permissions a role needs.

______________________________________________________________________

## Restrictions documented elsewhere in this guide

These are the access rules stated on individual module pages. Each links back to the page that describes it in full.

| **Area**                 | Restriction                                                                                                         | Page                                                             |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| **Dashboard Analytics**  | Requires the **Can view admin dashboard** permission. Without it the page loads but the analytics section is hidden | [Dashboard](../00-getting-started/dashboard.md)                  |
| **Invoice approval**     | Only a superuser can click **Approve** when an invoice exceeds the client's balance limit                           | [Create Invoice](../03-trade/invoices/create-invoice.md)         |
| **Invoice status**       | Until a superuser approves, an over-limit invoice stays locked to `Draft` and cannot be set to `Sent`               | [Create Invoice](../03-trade/invoices/create-invoice.md)         |
| **Salary visibility**    | The **Hide Salary Details** toggle restricts salary visibility to superusers                                        | [App Settings](../08-settings-and-admin/app-settings.md)         |
| **Salary deletion**      | A salary record linked to a payout or marked `Paid` may not be deletable; contact an administrator                  | [Generate Salary](../04-employee/salary/generate-salary.md)      |
| **Bank deletion**        | A bank can be deleted only when it has no linked records and the user has delete permission                         | [Bank Detail](../03-trade/banks/bank-detail.md)                  |
| **Developer settings**   | Should be changed only by technical administrators; incorrect values can break deployments or tracking              | [App Settings](../08-settings-and-admin/app-settings.md)         |
| **Maintenance mode**     | Requires permission to enable and disable maintenance mode                                                          | [Maintenance Mode](../08-settings-and-admin/maintenance-mode.md) |
| **Audit log**            | Requires permission to view audit records                                                                           | [Audit Log](../08-settings-and-admin/audit-log.md)               |
| **Reports**              | Requires access to the **Reports** module; individual reports may also need a sales, finance, or HR role            | [Reports](../07-reports/README.md)                               |
| **Returns**              | Requires permission to create or edit product and material return records                                           | [Returns](../05-returns/README.md)                               |
| **Commission campaigns** | Requires permission to manage commission campaigns                                                                  | [Commission and Campaigns](../06-commission/README.md)           |

!!! note "Record state is not a permission"

    Several restrictions above depend on the state of a record rather than on the account. An invoice locked to `Draft` because it exceeds a balance limit, or a salary that cannot be deleted because it is linked to a payout, will not become available by granting a permission.

______________________________________________________________________

## Role matrix

!!! warning "Needs product review"

    CTB Admin's permissions are assigned per account rather than through named roles, and the repository does not define a standard permission set for each job function. A role-by-module matrix therefore cannot be published without confirmation from the product owner.

    Required to complete this section: the default permission set granted to each role the business recognises (office staff, accountant, HR, administrator), and whether any module is read-only for a role rather than fully hidden. Tracked in `review/sme-checklist.md`.

______________________________________________________________________

## Tips and common issues

- A missing sidebar entry and a `403` page usually have the same cause: the module permission is not granted.
- If a user can open a page but not save, check the action-level permission rather than the module permission.
- Grant **Staff status** before anything else. Module permissions have no effect without it.
- After changing permissions, ask the user to sign out and back in.

______________________________________________________________________

## Related pages

- **[User Management](../08-settings-and-admin/user-management.md)** — Where accounts and their permissions are created and changed.
- **[Troubleshooting](troubleshooting.md)** — What to do about specific error messages and blocked actions.
- **[Audit Log](../08-settings-and-admin/audit-log.md)** — Who changed a record, and when.
