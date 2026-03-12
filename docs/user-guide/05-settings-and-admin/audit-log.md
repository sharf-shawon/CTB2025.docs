# Audit Log

## Summary

Use this page to review who changed data in CTB Admin, what was changed, and when the action happened. Audit logs help you verify activity, investigate unexpected changes, and support internal control checks.

![Audit Log page](../screenshots/settings/audit-log.png)

## When to use this page

- When you need to verify who created, edited, or deleted a record.
- When you investigate incorrect values in business, factory, trade, or employee data.
- When management asks for a history of admin activity.
- When you need evidence for compliance, internal review, or dispute resolution.

## How to access this page

From the left sidebar menu, go to **Audit Log**. It appears as the last item in the menu.

## Prerequisites

- You have permission to view audit records.
- Users have already performed actions in the system, so logs exist to review.

## Step-by-step instructions

1. Open **Audit Log** from the left sidebar.
1. Review the most recent entries first to understand current activity.
1. Identify the key details for each row: who performed the action, what object was affected, and when it occurred.
1. Use available search or filter controls on the page to narrow records by user, model, or date range.
1. Open a log entry if details are available, then compare old and new values to confirm exactly what changed.
1. Cross-check the affected record in its original module (for example Clients, Invoices, or Employees) if follow-up is needed.
1. Record the relevant log details before escalating to management or operations.

## Field reference

- **User** - The account that performed the action.
- **Action** - The type of operation, such as add, change, or delete.
- **Object** - The record or entity that was affected.
- **Module/App** - The area of CTB Admin where the change happened.
- **Timestamp** - Date and time when the action was saved.
- **Change Details** - Before/after values or a summary of the edited fields.
- **IP/Source (if available)** - Request origin information useful for security checks.

This page reads audit trail data for admin activity. Use it as the system source when checking history related to records like `Business.models.Client` and other operational objects.

## Tips and common issues

- Check system date and time settings if log times look inconsistent.
- Filter by a short date range first when there are many records.
- Use both **User** and **Object** together to find the correct event faster.
- If no entries appear, confirm that the action was actually saved and that your account has viewing permission.
- Export or screenshot important entries during incident review so your team has a fixed reference.

## Related pages

- See [User Management](user-management.md) to control who can access and change data.
- See [Maintenance Mode](maintenance-mode.md) before performing controlled system updates.
- See [App Settings](app-settings.md) for global behavior that may affect user activity.
