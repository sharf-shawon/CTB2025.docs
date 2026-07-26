---
tags: [module:employee, task:edit, role:hr]
---

# Manage Task

<!-- metadata: owner: hr, last_updated: 2026-07-26, git_ref: main, staging_verified: true -->

## Summary

Use this page to update an existing task in CTB Admin. Managing tasks lets you reassign work items, update priority levels, adjust status progress, and record completion dates.

______________________________________________________________________

## When to use this page

- Updating task progress status (`To Do` → `In Progress` → `Completed`)
- Reassigning an active task to another employee
- Adjusting task priority level or work instructions

______________________________________________________________________

## How to access this page

1. Go to **Employee → Tasks** (`/admin/employee/employeetask/`) from the sidebar.
1. Click any **Task Name** or row in the task list view.

![Task list page](edit-task-list-page.png)

______________________________________________________________________

## Prerequisites

- **Permissions:** `employee.change_employeetask` permission codename (HR Staff, Manager, or Superuser role).
- **Active Records:** Target task record must exist in the database.

______________________________________________________________________

## Step-by-step instructions

1. Open **Employee → Tasks** and click the target task title.
1. Modify fields in **Task Name**, **Description**, **Assigned To**, **Status**, or **Priority**.
1. Click **Save** to apply changes and update the task log.

![Edit Task Page](edit-task-page.png)

______________________________________________________________________

## Verification and definition of done

- System confirms: `Employee Task "Name" was changed successfully.`
- Updated status pill and assignee reflect immediately on the **Tasks Overview** page.

______________________________________________________________________

## Field reference

| Step | Field       | Required | What to Do      | Description                                                                |
| ---- | ----------- | -------- | --------------- | -------------------------------------------------------------------------- |
| 1    | Task Name   | Yes      | Edit title      | Title or name of the task                                                  |
| 2    | Description | No       | Edit text       | Detailed work instructions                                                 |
| 3    | Assigned To | Yes      | Select user     | Employee assigned to execute the task                                      |
| 4    | Status      | Yes      | Select status   | Workflow progress state (`To Do`, `In Progress`, `Completed`, `Cancelled`) |
| 5    | Priority    | Yes      | Select priority | Urgency level (`Low`, `Medium`, `High`, `Urgent`)                          |
| 6    | Due Date    | No       | Select date     | Expected completion date                                                   |
| 7    | Note        | No       | Enter text      | Internal comments or progress remarks                                      |

______________________________________________________________________

## Exception handling and error recovery

| Symptom / Error Message | Root Cause                                  | Remediation Action                                                          |
| ----------------------- | ------------------------------------------- | --------------------------------------------------------------------------- |
| Cannot reassign task    | Target employee account is disabled         | Verify employee status under [Employees Overview](../employees/overview.md) |
| Task status locked      | User lacks `change_employeetask` permission | Request elevated manager permissions from administrator                     |

______________________________________________________________________

## Related pages

- [Create Task](create-task.md) — Register a new task assignment
- [Tasks Overview](overview.md) — Monitor team workload and task completion status
- [Employees Overview](../employees/overview.md) — Manage staff accounts
