---
tags: [module:employee, task:edit, role:hr]
---

# Record Attendance

<!-- metadata: owner: hr, last_updated: 2026-07-26, git_ref: main, staging_verified: true -->

## Summary

Use this page to log or correct daily employee attendance in CTB Admin. Recording attendance captures check-in/check-out timestamps, regular work minutes, overtime minutes, and applicable salary rates required for accurate monthly salary generation.

______________________________________________________________________

## When to use this page

- Recording daily manual check-in and check-out times for factory floor workers
- Correcting missing or distorted automatic biometric attendance entries
- Logging overtime minutes worked beyond standard shift schedules
- Setting daily work minutes used in monthly salary unit calculations

______________________________________________________________________

## How to access this page

From the sidebar, go to **Employee → Attendance** (`/admin/employee/attendance/`). On the Attendance List page, click the **purple (+) icon** in the top-right corner.

______________________________________________________________________

## Prerequisites

- **Permissions:** `employee.add_attendance` / `employee.change_attendance` permission codenames (HR Staff or Superuser role).
- **Active Records:** Active target employee record in **Employee → Employees**.

______________________________________________________________________

## Step-by-step instructions

1. Open **Employee → Attendance** and click **(+) Add Attendance**.
1. Select the **Employee** from the dropdown menu.
1. Select the attendance **Date** (`YYYY-MM-DD`).
1. Enter the **Check-in Time** (`HH:MM:SS`) and **Check-out Time**.
1. Select the **Salary Type** (`Monthly`, `Hourly`, `Daily`) and set **Salary Rate**.
1. Enter total **Work Minutes** completed during the shift.
1. Enter any **Overtime Minutes** worked.
1. Click **Save** to store the attendance log.

______________________________________________________________________

## Verification and definition of done

- System generates a unique attendance SKU (`ATT-YYYYMMDD-XXXX`).
- Logged attendance entry appears under **Employee → Attendance** for the specified date.
- Recorded minutes aggregate into the employee's monthly salary calculation summary.

______________________________________________________________________

## Field reference

![Add Attendance Form](add-attendance.png)

| Step | Field            | Required | What to Do      | Description                                                    |
| ---- | ---------------- | -------- | --------------- | -------------------------------------------------------------- |
| 1    | SKU              | No       | Read-only       | System-generated tracking code                                 |
| 2    | Employee         | Yes      | Select employee | Staff member present for shift                                 |
| 3    | Date             | Yes      | Select date     | Shift date (`YYYY-MM-DD`)                                      |
| 4    | Check-in Time    | Yes      | Enter time      | Shift start timestamp (`HH:MM:SS`)                             |
| 5    | Check-out Time   | No       | Enter time      | Shift end timestamp (`HH:MM:SS`)                               |
| 6    | Salary Type      | Yes      | Select type     | Pay structure assigned to shift (`Monthly`, `Daily`, `Hourly`) |
| 7    | Salary Rate      | Yes      | Enter rate      | Base rate applied for shift earnings calculation               |
| 8    | Work Minutes     | Yes      | Enter number    | Total regular shift work minutes                               |
| 9    | Overtime Minutes | No       | Enter number    | Additional overtime shift minutes                              |

______________________________________________________________________

## Exception handling and error recovery

| Symptom / Error Message                                | Root Cause                                                              | Remediation Action                                                      |
| ------------------------------------------------------ | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `Attendance for this employee and date already exists` | Unique constraint (`employee`, `date`) prevents duplicate daily records | Open existing attendance record for the date and edit it                |
| `Check-out time earlier than Check-in time`            | Out-of-order time entry                                                 | Verify shift log and adjust check-out timestamp to occur after check-in |

______________________________________________________________________

## Related pages

- [Attendance Overview](overview.md) — Review and search daily attendance logs
- [Generate Salary](../salary/generate-salary.md) — Run monthly salary calculation vouchers
- [Employees Overview](../employees/overview.md) — Manage employee profiles
