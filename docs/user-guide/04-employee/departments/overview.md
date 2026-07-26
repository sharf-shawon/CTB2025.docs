---
tags: [module:employee, task:view, role:hr]
---

# Departments Overview

<!-- metadata: owner: hr, last_updated: 2026-07-26, git_ref: main, staging_verified: true -->

## Summary

Use this page to review and manage all organizational departments in CTB Admin. The listing provides a real-time overview of active and disabled department records, descriptions, and audit timestamps.

______________________________________________________________________

## When to use this page

- Auditing department structure across the organization
- Searching for specific departments by name or SKU
- Inspecting active status indicators before assigning employees
- Accessing department creation and editing forms

______________________________________________________________________

## How to access this page

From the sidebar navigation, select **Employee → Departments** (`/admin/employee/workdepartment/`).

______________________________________________________________________

## Prerequisites

- **Permissions:** `employee.view_workdepartment` permission codename (HR, Accountant, Manager, or Superuser role).
- **Active Records:** None.

______________________________________________________________________

## Step-by-step instructions

1. Open **Departments** from the **Employee** section of the sidebar.
1. Review the list of department records and status indicators in the **Is Enabled** column.
1. Type in the **Type to search** bar to filter results by department name.
1. Click **Add Department (+)** to create a new department, or click an existing row to edit details.

______________________________________________________________________

## Verification and definition of done

- Master department directory renders with correct status checkmarks.
- Search filter accurately narrows visible rows in real time.

______________________________________________________________________

## Field reference

### Table columns

![Department Overview List Page](department-overview-list-page.png)

| Column          | Required | What to Do     | Description                                  |
| --------------- | -------- | -------------- | -------------------------------------------- |
| SKU             | No       | View value     | Auto-generated unique identifier code        |
| Department Name | Yes      | Click link     | Name of the department                       |
| Description     | No       | View text      | Operational summary or notes                 |
| Is Enabled      | Yes      | View checkmark | Green checkmark if active; empty if disabled |
| Created At      | No       | View timestamp | Creation date and time                       |
| Updated At      | No       | View timestamp | Last modification date and time              |

______________________________________________________________________

## Exception handling and error recovery

| Symptom / Error Message                  | Root Cause                                     | Remediation Action                                                          |
| ---------------------------------------- | ---------------------------------------------- | --------------------------------------------------------------------------- |
| Target department missing from dropdowns | Department is disabled (`Is Enabled` is false) | Enable the department on the [Manage Department](manage-department.md) form |
| Search returns no matching departments   | Search query typo or restrictive filter active | Clear search input and reset active filter parameters                       |

______________________________________________________________________

## Related pages

- [Manage Department](manage-department.md) — Create or edit department details
- [Positions Overview](../positions/overview.md) — View work position listings
- [Employees Overview](../employees/overview.md) — Assign employees to departments
