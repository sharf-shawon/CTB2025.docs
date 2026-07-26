---
tags: [module:reference, task:troubleshoot, role:staff]
---

# Troubleshooting

Common problems in CTB Admin, what causes them, and what to do about each.

## Summary

Use this page when something does not work as expected: an error screen, a button that is not there, a total that does not update, or a page that will not load. Each entry links to the module page that covers the feature in full.

______________________________________________________________________

## When to use this page

- You see an error code or an unexpected screen.
- A button or section you expect is missing.
- A record will not save, or a calculated value looks wrong.
- The site is slow, stale, or unavailable.

______________________________________________________________________

## How to access this page

From the sidebar, go to **Reference → Troubleshooting**. You can also reach it from the search box on any page.

______________________________________________________________________

## Step-by-step instructions

1. Find the closest match to your symptom in the sections below.
1. Apply the suggested check.
1. If the entry links to a module page, open it for the full description of the feature.
1. If nothing here matches, note the exact error text and the record you were working on, then contact your administrator.

______________________________________________________________________

## Field reference

Not applicable. This page describes symptoms rather than a screen.

______________________________________________________________________

## Error screens

| **Error**       | What it means                               | What to do                                                              |
| --------------- | ------------------------------------------- | ----------------------------------------------------------------------- |
| **403**         | You do not have permission to view the page | Confirm you are signed in, then check your role or ask an administrator |
| **404**         | The page or record could not be found       | Check the link, search again, or return to the module list              |
| **500**         | The server encountered a problem            | Refresh the page, and report the issue if it continues                  |
| **Maintenance** | The site is temporarily restricted          | Wait until maintenance is complete and try again                        |

Check the exact error code before acting on it. A signed-out session produces the same `403` screen as a genuine permission problem, so confirm the user is logged in first.

If a missing page relates to a record that was changed, the [Audit Log](../08-settings-and-admin/audit-log.md) shows who changed it and when.

______________________________________________________________________

## A button or section is missing

| **Symptom**                                     | Likely cause                                                                              | Where to look                                                  |
| ----------------------------------------------- | ----------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| **Dashboard Analytics** section is not shown    | The account lacks the **Can view admin dashboard** permission                             | [Permissions](permissions.md)                                  |
| **Approve** button is not visible on an invoice | The button appears only to superusers, and only when the invoice exceeds the client limit | [Create Invoice](../03-trade/invoices/create-invoice.md)       |
| Invoice status will not change from `Draft`     | The invoice exceeds the client's balance limit and needs superuser approval first         | [Create Invoice](../03-trade/invoices/create-invoice.md)       |
| Salary figures are hidden                       | **Hide Salary Details** restricts salary visibility to superusers                         | [App Settings](../08-settings-and-admin/app-settings.md)       |
| **Delete** is unavailable on a record           | The record is linked to another record, or the account lacks delete permission            | [Permissions](permissions.md)                                  |
| A whole module is missing from the sidebar      | The module permission is not granted for the account                                      | [User Management](../08-settings-and-admin/user-management.md) |

______________________________________________________________________

## A record will not save

- Fields marked with a red star are mandatory. The form will not save until each is filled.
- A return record needs at least one returned item before it can be saved.
- Check that a required linked record exists first: an invoice needs a client, a salary needs an employee, and a payment needs the invoice it applies to.
- Save before leaving the page. Entered data is not kept when you move away without saving.

______________________________________________________________________

## A total or calculated value looks wrong

- Calculated fields update when their inputs change. If a total has not moved, re-enter the quantity or rate that feeds it.
- Net Salary recalculates from Salary, Salary Units, Overtime, Bonus, and Deductions. Changing any of them updates it.
- Setting a salary to `0` applies the default rate from the employee's profile rather than paying zero.
- Outstanding invoice figures reflect payments that have been posted. Re-check after recording a payment.
- The Dashboard is cached for 15 minutes, so figures there can be up to 15 minutes behind. Use **Refresh** to force a recalculation.

______________________________________________________________________

## The site is stale, slow, or offline

CTB Admin caches pages in your browser so previously visited pages keep working when the connection drops.

- Refresh once after reconnecting rather than reloading repeatedly.
- Open a page you have already visited to load the cached copy.
- If an image or page looks out of date, clear the browser cache and try again.
- The first visit to a page still needs a working connection.
- After a deployment, visit the site once while online so the cache can update.

See [Offline Mode](offline-mode.md) for the full description of what is cached and when.

______________________________________________________________________

## Search is not finding a record

- Search by SKU where possible. It is the most precise match.
- Check spelling and remove extra spaces.
- Confirm your account has permission to view that record type. Records you cannot view do not appear in results.

______________________________________________________________________

## Tips and common issues

- Note the exact error text before refreshing. It is the fastest way for an administrator to identify the cause.
- After a permission change, sign out and back in before retesting.
- Use shorter date ranges first when a report is slow to load.
- Check the [Audit Log](../08-settings-and-admin/audit-log.md) when a record's values are not what you expect.

______________________________________________________________________

## Related pages

- **[Permissions](permissions.md)** — Which role can see and change each area.
- **[Error Pages](error-pages.md)** — The error screens in detail.
- **[Offline Mode](offline-mode.md)** — What works without a connection.
- **[Glossary](glossary.md)** — Definitions of the terms used above.
- **[Audit Log](../08-settings-and-admin/audit-log.md)** — History of changes to a record.
