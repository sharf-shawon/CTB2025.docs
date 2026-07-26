---
tags: [module:employee, task:edit, role:hr]
---

# Edit Employee

<!-- metadata: owner: hr, last_updated: 2026-07-26, git_ref: main, staging_verified: true -->

## Summary

Use this page to update an existing employee's profile and settings. Any adjustments to contact details, job role, department, or salary rate immediately take effect for future attendance entries, wage calculations, and payroll cycles.

______________________________________________________________________

## When to use this page

- Updating employee contact or personal details
- Transferring an employee to a new department or job position
- Adjusting salary rates, balance limits, or notification settings
- Updating NID document scans or profile photos

______________________________________________________________________

## How to access this page

1. Go to **Employee → Employees** (`/admin/employee/employee/`) from the sidebar.
1. Click the employee name or row in the list view.

![Edit Employee List Page](edit-employee-list-page.png)

______________________________________________________________________

## Prerequisites

- **Permissions:** `employee.change_employee` permission codename (HR Manager or Superuser role).
- **Active Records:** Target employee record must exist in the database.

______________________________________________________________________

## Step-by-step instructions

1. Open the target employee record from **Employee → Employees**.
1. Modify the required fields in **General information**, **Emergency contact**, **Employment details**, or **Salary information**.
1. Click **Save** to apply changes and return to the list, or **Save and continue editing** to remain on the form.

______________________________________________________________________

## Verification and definition of done

- System displays notification: `Employee "Name" was changed successfully.`
- Updated values appear immediately in the **Employees** list and employee profile view.
- Subsequent salary calculations and attendance records reflect the updated configuration.

______________________________________________________________________

## Field reference

### General information

![Edit Employee General Information](edit-employee-personal-info.png)

| Step | Field                | Required | What to Do    | Description                                                       |
| ---- | -------------------- | -------- | ------------- | ----------------------------------------------------------------- |
| 1    | SKU                  | No       | Read-only     | System-generated employee code                                    |
| 2    | Employee Photo       | No       | Replace image | Profile photo used across employee listings and detail views      |
| 3    | Employee Name        | Yes      | Edit text     | Primary name used on payroll documents and reports                |
| 4    | Is Enabled           | Yes      | Toggle switch | Controls whether the employee record is active                    |
| 5    | Send SMS             | No       | Toggle switch | Enables automated SMS notifications for payouts and salary events |
| 6    | Hide Salary Details  | No       | Toggle switch | Restricts salary information visibility in employee-facing views  |
| 7    | Date of Birth        | No       | Select date   | Birth date for personal record-keeping                            |
| 8    | Phone Number         | Yes      | Edit text     | Primary contact number for identity and notification lookup       |
| 9    | Address              | No       | Edit text     | Current residential address                                       |
| 10   | NID Number           | No       | Edit text     | National identity card or passport number                         |
| 11   | NID Card Front Photo | No       | Replace image | Front side scan or image of NID card                              |
| 12   | NID Card Back Photo  | No       | Replace image | Back side scan or image of NID card                               |

### Emergency contact

![Emergency Contact Section](edit-employee-emargency-info.png)

| Step | Field                  | Required | What to Do | Description                              |
| ---- | ---------------------- | -------- | ---------- | ---------------------------------------- |
| 1    | Emergency Contact Name | No       | Edit text  | Primary emergency contact person         |
| 2    | Emergency Phone Number | No       | Edit text  | Primary emergency contact phone number   |
| 3    | Emergency Address      | No       | Edit text  | Residential address of emergency contact |

### Employment details

![Employment Details Section](edit-employee-work-delails.png)

| Step | Field            | Required | What to Do        | Description                                             |
| ---- | ---------------- | -------- | ----------------- | ------------------------------------------------------- |
| 1    | Work Position    | Yes      | Select position   | Job position assigned to the employee                   |
| 2    | Work Department  | Yes      | Select department | Department assignment for reporting and hierarchy       |
| 3    | Purchase Balance | No       | Edit balance      | Starting balance for internal purchase balance tracking |
| 4    | Start Date       | Yes      | Select date       | Official employment start date                          |
| 5    | End Date         | No       | Select date       | Contract termination date (leave empty if active)       |

### Salary information

![Salary Information Section](edit-employee-salary-info.png)

| Step | Field               | Required | What to Do  | Description                                               |
| ---- | ------------------- | -------- | ----------- | --------------------------------------------------------- |
| 1    | Salary Type         | Yes      | Select type | Calculation mode (`Monthly`, `Daily`, `Production-based`) |
| 2    | Salary Rate         | Yes      | Edit rate   | Base rate used for salary calculations                    |
| 3    | Balance             | No       | Edit amount | Current employee ledger balance                           |
| 4    | Upper Balance Limit | No       | Edit amount | Maximum credit limit allowed for advances                 |
| 5    | Lower Balance Limit | No       | Edit amount | Minimum threshold trigger for balance alerts              |

______________________________________________________________________

## Exception handling and error recovery

| Symptom / Error Message                            | Root Cause                                   | Remediation Action                                                |
| -------------------------------------------------- | -------------------------------------------- | ----------------------------------------------------------------- |
| `Cannot disable employee with active transactions` | Employee has pending ledger entries          | Complete or settle active transactions before disabling           |
| `Duplicate Phone Number`                           | Phone number matches another employee record | Ensure phone number is unique across all active employee profiles |

______________________________________________________________________

## Related pages

- [Add Employee](add-employee.md) — Create a new employee record
- [Employee Detail](employee-detail.md) — View full employee profile
- [Generate Salary](../salary/generate-salary.md) — Process salary for updated rate settings
