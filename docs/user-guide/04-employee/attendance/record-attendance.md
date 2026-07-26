---
tags: [module:employee, task:edit, role:hr]
---

# Record Attendance

<!-- metadata: owner: hr_team, last_updated: 2026-07-26, git_ref: main, staging_verified: true -->

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

From the sidebar, go to **Employee → Attendance** (`/en/admin/Employee/attendance/`). On the Attendance List page, click the **purple (+) icon** in the top-right corner.

______________________________________________________________________

## Prerequisites

- **Active Employee Record**: Target worker must exist in **Employee → Employees**.
- **Required User Permissions**:
    - `Employee | Attendance | Can add Attendance` (`employee.add_attendance`)
    - `Employee | Attendance | Can change Attendance` (`employee.change_attendance`)

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

## Verification & definition of done

- **Unique SKU Assigned**: System generates an attendance SKU (`ATT-YYYYMMDD-XXXX`).
- **Attendance Logged**: Entry appears under **Employee → Attendance** for the specified date.
- **Salary Unit Computation**: Recorded minutes aggregate into the employee's monthly **Salary Units** summary.

______________________________________________________________________

## Field reference

| Field Name           | Type    | Required | Backend Validation / Constraints                | Description                               |
| :------------------- | :------ | :------- | :---------------------------------------------- | :---------------------------------------- |
| **SKU**              | Text    | Auto     | Prefix `ATT`, read-only                         | System-generated tracking SKU.            |
| **Employee**         | Select  | Yes      | Foreign Key (`Employee.Employee`), `PROTECT`    | Staff member present for shift.           |
| **Date**             | Date    | Yes      | Valid date (`YYYY-MM-DD`), default today        | Attendance shift date.                    |
| **Check-in Time**    | Time    | Yes      | Valid time (`HH:MM:SS`)                         | Work shift start timestamp.               |
| **Check-out Time**   | Time    | No       | Valid time (`HH:MM:SS`)                         | Work shift end timestamp.                 |
| **Salary Type**      | Select  | Yes      | Choices: `Monthly`, `Daily`, `Hourly`           | Pay model assigned to shift.              |
| **Salary Rate**      | Decimal | Yes      | Max 13 digits, 3 decimal places, default `0.00` | Rate applied to calculate daily earnings. |
| **Work Minutes**     | Integer | Yes      | Positive integer                                | Total regular shift work minutes.         |
| **Overtime Minutes** | Integer | No       | Default `0`                                     | Additional shift overtime minutes.        |

______________________________________________________________________

## Exception handling & error recovery

| Error Symptom / Message                                    | Root Cause                                                           | Step-by-Step Remediation                                                                                           |
| :--------------------------------------------------------- | :------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------- |
| **"Attendance for this employee and date already exists"** | Unique constraint (`employee`, `date`) prevents multiple daily logs. | 1. Open the existing attendance record for the date.<br>2. Edit the existing record instead of adding a duplicate. |
| **Check-out time earlier than Check-in time**              | Invalid time entry sequence.                                         | 1. Check shift logs.<br>2. Correct Check-out Time to be later than Check-in Time before saving.                    |

______________________________________________________________________

## Related workflows & next steps

- **Generate Salary** — Process monthly salary using aggregated attendance logs.
- **Attendance Report** — Inspect daily attendance summary across factory teams.

______________________________________________________________________

## Related pages

- **Attendance Overview** — Review and search attendance records
- **Generate Salary** — Create payroll using attendance and salary data
- **Salaries Overview** — View salary records and payment status
- **Employees** — Manage employee details used in attendance records
