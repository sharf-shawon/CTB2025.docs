---
tags: [module:employee, task:edit, role:hr]
---

# Manage Position

<!-- metadata: owner: hr, last_updated: 2026-07-26, git_ref: main, staging_verified: true -->

## Summary

Use this page to add or update a job position in CTB Admin. Positions define specific job titles and roles held by employees (e.g., Cutter, Sewing Operator, Store Keeper).

______________________________________________________________________

## When to use this page

- Defining a new job title or position in the company
- Updating the title name, status, or description of an existing position
- Deactivating job positions no longer in active use

______________________________________________________________________

## How to access this page

From the sidebar navigation, select **Employee → Positions** (`/admin/employee/workposition/`). Click **Add Position (+)** to create a new record, or click an existing position row to edit.

______________________________________________________________________

## Prerequisites

- **Permissions:** `employee.add_workposition` / `employee.change_workposition` permission codenames (HR Manager or System Administrator role).
- **Active Records:** None.

______________________________________________________________________

## Step-by-step instructions

1. Open **Positions** from the **Employee** section of the sidebar.
1. Click **Add Position (+)** or select an existing position row.
1. Enter the **Position Name** and optional **Description**.
1. Set the **Is Enabled** toggle switch state.
1. Click **Save** to apply changes.

______________________________________________________________________

## Verification and definition of done

- System confirms: `Work Position "Name" was added/changed successfully.`
- The position is listed in `/admin/employee/workposition/` and is available in employee profile forms.

______________________________________________________________________

## Field reference

### Position information

![Manage Position Page](manage-position-page.png)

| Step | Field         | Required | What to Do    | Description                                   |
| ---- | ------------- | -------- | ------------- | --------------------------------------------- |
| 1    | SKU           | No       | View value    | System-generated unique identifier code       |
| 2    | Position Name | Yes      | Enter title   | Official job position title                   |
| 3    | Description   | No       | Enter text    | Detailed role description and duties          |
| 4    | Is Enabled    | Yes      | Toggle switch | Controls availability for employee assignment |

______________________________________________________________________

## Exception handling and error recovery

| Symptom / Error Message                  | Root Cause                                     | Remediation Action                                               |
| ---------------------------------------- | ---------------------------------------------- | ---------------------------------------------------------------- |
| `Position with this Name already exists` | Duplicate position title entry                 | Use a distinct job position name or update the existing position |
| Cannot delete position                   | Active employees are assigned to this position | Reassign active employees to another position before deleting    |

______________________________________________________________________

## Related pages

- [Positions Overview](overview.md) — View master list of all positions
- [Departments Overview](../departments/overview.md) — Manage department definitions
- [Add Employee](../employees/add-employee.md) — Assign positions to new staff members
