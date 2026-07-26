---
tags: [module:employee, task:view, role:hr]
---

# Wage Overview

<!-- metadata: owner: hr, last_updated: 2026-07-26, git_ref: main, staging_verified: true -->

## Summary

Use the **Wage Overview** page to audit, filter, and track piecework wage entries in CTB Admin. The listing displays product quantities, gross wage rates, bonuses, deductions, and net payable amounts across employees.

______________________________________________________________________

## When to use this page

- Auditing piecework wage calculations across production batches
- Filtering wage vouchers by payment status (`Paid` vs `Unpaid`)
- Verifying unit rates, bonuses, and deduction breakdowns
- Accessing new wage entry creation forms

______________________________________________________________________

## How to access this page

From the sidebar navigation, select **Employee → Wages** (`/admin/employee/wageentry/`).

______________________________________________________________________

## Prerequisites

- **Permissions:** `employee.view_wageentry` permission codename (HR, Production Supervisor, Accountant, or Superuser role).
- **Active Records:** None.

______________________________________________________________________

## Step-by-step instructions

1. Open **Wages** from the **Employee** section of the sidebar.
1. Review the list of wage vouchers and payment status pills (`Paid`, `Unpaid`).
1. Use the search bar to locate vouchers by SKU or employee name.
1. Click **Filters** to narrow records by date range, payment state, or product.
1. Click **Add Wage Entry (+)** to record new piece-rate output.

______________________________________________________________________

## Verification and definition of done

- Master list renders wage vouchers with accurate net calculation columns.
- Payment status pills correctly indicate settled (`Paid`) versus pending (`Unpaid`) entries.

______________________________________________________________________

## Field reference

### Table summary

![Wage List Page](wage-overview-list-page.png)

| Column     | Required | What to Do  | Description                           |
| ---------- | -------- | ----------- | ------------------------------------- |
| SKU        | No       | View value  | Unique wage tracking identifier       |
| Date       | Yes      | View date   | Work session entry date               |
| Employee   | Yes      | Click link  | Name and SKU of employee              |
| Product    | Yes      | View text   | Manufactured product item             |
| Qty        | Yes      | View number | Production unit quantity              |
| Wage       | Yes      | View rate   | Base rate per unit                    |
| Deductions | No       | View amount | Deducted penalty or adjustment        |
| Bonus      | No       | View amount | Additional incentive bonus            |
| Net Wage   | No       | View total  | Net payable wage                      |
| Status     | Yes      | View pill   | Settlement state (`Paid` or `Unpaid`) |
| Paid On    | No       | View date   | Payment settlement timestamp          |

______________________________________________________________________

## Exception handling and error recovery

| Symptom / Error Message           | Root Cause                                            | Remediation Action                                                           |
| --------------------------------- | ----------------------------------------------------- | ---------------------------------------------------------------------------- |
| Wage voucher missing from listing | Active filter excluding target date or payment status | Click **Filters** and reset active filter selections                         |
| Net Wage mismatch                 | Incorrect deduction or bonus amount recorded          | Open the entry in [Add Wage Entry](add-wage-entry.md) and correct line items |

______________________________________________________________________

## Related pages

- [Add Wage Entry](add-wage-entry.md) — Log new production output vouchers
- [Create Payout](../payouts/create-payout.md) — Issue payments for pending wage vouchers
- [Employees Overview](../employees/overview.md) — Manage staff profile records
