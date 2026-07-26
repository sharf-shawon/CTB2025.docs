---
tags: [module:reference, task:troubleshoot, role:staff]
---

# Error Pages

Use this page to understand the standard error screens users may see in CTB Admin and what to do next.

## Summary

Error pages help users recover from missing pages, permission issues, or server problems. Use this page as a quick support reference when a user reports an unexpected screen.

______________________________________________________________________

## When to use this page

- When a user reports a page is missing.
- When a user cannot access a record.
- When the site shows a server or maintenance message.

<!-- TODO: Add screenshots for the most common error states if they are captured in the UI. -->

______________________________________________________________________

## How to access this page

From the sidebar, go to **Reference**, then open **Error Pages**.

______________________________________________________________________

## Step-by-step instructions

1. Open **Error Pages** from the **Reference** section of the sidebar.
1. Complete the **Common error pages** section described below.
1. Review the values you entered, then save the record.

______________________________________________________________________

## Field reference

### Common error pages

| Error       | What it means                                | What you should do                                          |
| ----------- | -------------------------------------------- | ----------------------------------------------------------- |
| 403         | You do not have permission to view the page. | Confirm your role or ask an administrator to grant access.  |
| 404         | The page or record could not be found.       | Check the link, search again, or return to the module list. |
| 500         | The server encountered a problem.            | Refresh the page and report the issue if it continues.      |
| Maintenance | The site is temporarily restricted.          | Wait until maintenance is complete and try again later.     |

______________________________________________________________________

## Tips and common issues

- Check the exact error code before giving support advice.
- Confirm the user is logged in before treating a 403 as a system problem.
- Use the audit log if the missing page is tied to a record change.

______________________________________________________________________

## Related pages

- [Offline Mode](offline-mode.md)
- [Audit Log](../08-settings-and-admin/audit-log.md)
