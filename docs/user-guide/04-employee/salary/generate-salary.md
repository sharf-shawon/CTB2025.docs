---
tags: [module:employee, task:edit, role:hr]
---

# Generate Salary

<!-- metadata: owner: hr_team, last_updated: 2026-07-26, git_ref: main, staging_verified: true -->

## Summary

Use this page to generate monthly salary records for staff in CTB Admin. A salary entry computes total compensation by combining base salary rate, attended work units, overtime hours, bonuses, and deductions into a net payable amount.

______________________________________________________________________

## When to use this page

- Generating individual or monthly payroll records for factory and office personnel
- Computing net compensation incorporating overtime, performance bonuses, or tardiness deductions
- Logging monthly salary payment execution dates and reference transaction numbers
- Maintaining audit history for monthly payroll payouts

______________________________________________________________________

## How to access this page

From the sidebar, go to **Employee → Salaries** (`/en/admin/Employee/salary/`). On the Salaries List page, click the **purple (+) icon** in the top-right corner.

______________________________________________________________________

## Prerequisites

- **Active Employee Record**: Staff member must be registered in **Employee → Employees**.
- **Attendance Verification**: Monthly attendance records should be finalized in **Employee → Attendance**.
- **Required User Permissions**:
    - `Employee | Salary | Can add Salary` (`employee.add_salary`)
    - `Employee | Salary | Can change Salary` (`employee.change_salary`)

______________________________________________________________________

## Step-by-step instructions

1. Open **Employee → Salaries** and click **(+) Add Salary**.
1. Select the target **Employee** from the dropdown menu.
1. Select the **Month** and year for the salary calculation.
1. Enter the base **Salary** rate (or enter `0` to apply default profile salary).
1. Specify **Salary Units** (number of attended workdays or billable hours).
1. Input total **Overtime (hours)** worked during the period.
1. Enter any **Bonus** or **Deductions** in local currency.
1. Review the auto-calculated **Net Salary**.
1. If paying immediately, toggle **Is Paid** to ON and set **Payment Date**.
1. Click **Save** to generate the salary record.

______________________________________________________________________

## Verification & definition of done

- **Unique SKU Assigned**: System generates a unique salary SKU (`SLR-YYYYMMDD-XXXX`).
- **Net Salary Formula Validated**: `Net Salary = (Salary Rate × Units) + Overtime + Bonus - Deductions`.
- **Payroll Payout**: Salary entry appears under **Employee → Payouts** as payable balance.

______________________________________________________________________

## Field reference

| Field Name           | Type    | Required    | Backend Validation / Constraints                        | Description                                             |
| :------------------- | :------ | :---------- | :------------------------------------------------------ | :------------------------------------------------------ |
| **SKU**              | Text    | Auto        | Prefix `SLR`, read-only                                 | Unique tracking SKU.                                    |
| **Employee**         | Select  | Yes         | Foreign Key (`Employee.Employee`), `PROTECT`            | Target staff member.                                    |
| **Month**            | Date    | Yes         | Valid date (`YYYY-MM-DD`)                               | Billing month and year.                                 |
| **Salary**           | Decimal | Yes         | Max 13 digits, 3 decimal places, `MinValueValidator(0)` | Period salary rate. Enter `0` for profile default rate. |
| **Salary Units**     | Decimal | Yes         | Max 13 digits, 3 decimal places, default `1`            | Attended days or work hours.                            |
| **Overtime (hours)** | Decimal | No          | Default `0.00`, 3 decimal places                        | Overtime hours logged.                                  |
| **Bonus**            | Decimal | No          | Default `0.00`, 3 decimal places                        | Additional incentive or bonus.                          |
| **Deductions**       | Decimal | No          | Default `0.00`, 3 decimal places                        | Deductions for absences, loans, or fines.               |
| **Net Salary**       | Decimal | Auto        | Max 13 digits, 3 decimal places                         | Final net compensation payable.                         |
| **Is Paid**          | Boolean | No          | Default `False`                                         | Settlement status flag.                                 |
| **Payment Date**     | Date    | Conditional | Valid date, required if `Is Paid` is True               | Date salary payment was transferred.                    |
| **Payment Notes**    | Text    | No          | Max 50 characters                                       | Transaction memo or bank reference.                     |

______________________________________________________________________

## Exception handling & error recovery

| Error Symptom / Message                                        | Root Cause                                           | Step-by-Step Remediation                                                                                                   |
| :------------------------------------------------------------- | :--------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- |
| **"Salary record for this employee and month already exists"** | Duplicate monthly salary entry attempted.            | 1. Open existing salary record from **Employee → Salaries** list.<br>2. Edit existing record rather than adding a new one. |
| **"Payment Date is required when Is Paid is true"**            | Toggled `Is Paid` without selecting a payment date.  | 1. Enter the transaction date in **Payment Date**.<br>2. Save the salary record.                                           |
| **Net Salary negative error**                                  | Deductions exceed calculated base salary plus bonus. | 1. Verify deduction amount.<br>2. Adjust deductions to ensure non-negative net balance.                                    |

______________________________________________________________________

## Related workflows & next steps

- **[Record Attendance](../attendance/record-attendance.md)** — Audit monthly attendance units before salary generation.
- **[Add Payment](../../03-trade/payments/add-payment.md)** — Process net salary payment transfer.
- **Salary History** — Inspect historical payroll changes.

______________________________________________________________________

## Related pages

- **Salaries Overview** — View and manage all salary records
- **Employees** — Manage employee profiles and default salary rates
- **Wages** — Record production-based wage entries for employees
- **Payouts** — Process and track salary payouts
- **Attendance** — Review attendance records used for salary unit calculation
