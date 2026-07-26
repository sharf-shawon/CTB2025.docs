---
tags: [module:employee, task:view, role:hr]
---

# Salary Detail

<!-- metadata: owner: hr, last_updated: 2026-07-26, git_ref: main, staging_verified: true -->

## Summary

Use this page to inspect, edit, or settle an existing employee salary record in CTB Admin. The detail view exposes base salary rates, work units, overtime hours, bonuses, deductions, net salary totals, and payment status flags.

______________________________________________________________________

## When to use this page

- Auditing complete salary component breakdowns for a specific payroll period
- Modifying overtime, bonus, or deduction adjustments prior to Payout
- Updating payment status flags (`Is Paid`, `Payment Date`, `Payment Notes`)
- Reviewing audit history for salary voucher updates

______________________________________________________________________

## How to access this page

1. Go to **Employee → Salaries** (`/admin/employee/salary/`) from the sidebar.
1. Click any salary SKU or row in the listing table.

![Salaries List Page](salary-detail-list-page.png)

______________________________________________________________________

## Prerequisites

- **Permissions:** `employee.view_salary` / `employee.change_salary` permission codenames (HR Manager, Accountant, or Superuser role).
- **Active Records:** Targeted salary record must exist in CTB Admin database.

______________________________________________________________________

## Step-by-step instructions

1. Open the target salary record from **Employee → Salaries**.
1. Inspect or update fields in **General information**, **Salary components**, or **Payment details**.
1. Verify that the auto-calculated **Net Salary** reflects expected earnings.
1. If dispersing payment, toggle **Is Paid** to ON and set **Payment Date**.
1. Click **Save** to confirm changes.

______________________________________________________________________

## Verification and definition of done

- Confirmation message appears: `Salary "SLR-XXXX" was changed successfully.`
- Updated net payable figures reflect in employee ledger and payout tabs.

______________________________________________________________________

## Field reference

### General information

![Salary Detail General Information](salary-detail-general-page.png)

| Step | Field    | Required | What to Do  | Description                                        |
| ---- | -------- | -------- | ----------- | -------------------------------------------------- |
| 1    | Employee | Yes      | View/Select | Target staff member assigned to this salary record |
| 2    | Month    | Yes      | View/Select | Salary coverage month date (`YYYY-MM-DD`)          |

### Salary components

![Salary Components Section](salary-detail-componant-section.png)

| Step | Field            | Required | What to Do  | Description                                                  |
| ---- | ---------------- | -------- | ----------- | ------------------------------------------------------------ |
| 1    | SKU              | No       | View value  | Auto-generated salary voucher code                           |
| 2    | Salary           | Yes      | Edit rate   | Base salary rate (enter `0` to use employee profile default) |
| 3    | Salary Units     | Yes      | Edit units  | Number of attended workdays or billable work hours           |
| 4    | Overtime (hours) | No       | Edit hours  | Overtime hours worked in this period                         |
| 5    | Bonus            | No       | Edit amount | Additional incentive bonus added to base earnings            |
| 6    | Deductions       | No       | Edit amount | Penalty or loan deductions subtracted from gross pay         |
| 7    | Net Salary       | No       | Read-only   | Auto-calculated net payable amount                           |

### Payment details

![Payment Details Section](salary-detail-payment-section.png)

| Step | Field         | Required    | What to Do    | Description                                             |
| ---- | ------------- | ----------- | ------------- | ------------------------------------------------------- |
| 1    | Is Paid       | No          | Toggle switch | Settlement status flag (`Paid` / `Unpaid`)              |
| 2    | Payment Date  | Conditional | Select date   | Payment transfer date (required when `Is Paid` is True) |
| 3    | Payment Notes | No          | Enter text    | Reference memo or bank transaction code                 |

______________________________________________________________________

## Exception handling and error recovery

| Symptom / Error Message                         | Root Cause                                                      | Remediation Action                                                  |
| ----------------------------------------------- | --------------------------------------------------------------- | ------------------------------------------------------------------- |
| `Payment Date is required when Is Paid is true` | Form submitted with `Is Paid` toggled on without a payment date | Select a valid date in **Payment Date**                             |
| Cannot delete salary record                     | Record is linked to approved payouts or ledger entries          | Unlink or reverse related payout entries before attempting deletion |

______________________________________________________________________

## Related pages

- [Generate Salary](generate-salary.md) — Create a new salary calculation record
- [Salaries Overview](overview.md) — Review master salary listings
- [Create Payout](../payouts/create-payout.md) — Issue payout Payouts for approved salaries
