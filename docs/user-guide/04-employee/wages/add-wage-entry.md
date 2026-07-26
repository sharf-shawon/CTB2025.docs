---
tags: [module:employee, task:create, role:hr]
---

# Add Wage Entry

<!-- metadata: owner: hr, last_updated: 2026-07-26, git_ref: main, staging_verified: true -->

## Summary

Use this page to record production-based wage transactions in CTB Admin. Wage entries calculate worker earnings based on piecework output quantity, base unit rates, bonuses, and deductions.

______________________________________________________________________

## When to use this page

- Logging piece-rate production output for factory floor workers
- Calculating earnings for specific product manufacturing runs
- Applying bonuses or deductions to production work sessions
- Marking wage vouchers as settled or paid

______________________________________________________________________

## How to access this page

From the sidebar navigation, select **Employee → Wages** (`/admin/employee/wageentry/`). Click **Add Wage Entry (+)** in the top-right corner.

______________________________________________________________________

## Prerequisites

- **Permissions:** `employee.add_wageentry` permission codename (HR Staff, Production Supervisor, or Superuser role).
- **Active Records:** Active **Employee** profile and **Product** item.

______________________________________________________________________

## Step-by-step instructions

1. Open **Wages** from the **Employee** section of the sidebar.
1. Click **Add Wage Entry (+)**.
1. Select the entry **Date**, **Employee**, and **Product**.
1. Enter production **Quantity**, base **Wage** rate (or leave `0` for default product rate), **Deductions**, and **Bonus**.
1. Verify the auto-calculated **Net Wage**.
1. Set **Is Paid** status and **Payment Date** if settling immediately.
1. Click **Save** to create the record.

______________________________________________________________________

## Verification and definition of done

- System generates a wage SKU code (`WG-YYYYMMDD-XXXX`).
- Net wage computes according to formula: `(Wage * Quantity) + Bonus - Deductions`.
- The entry appears on the master list `/admin/employee/wageentry/` and updates the employee's pending compensation ledger.

______________________________________________________________________

## Field reference

### General information

![General Information Section](add-wage-general-info.png)

| Step | Field    | Required | What to Do      | Description                                |
| ---- | -------- | -------- | --------------- | ------------------------------------------ |
| 1    | SKU      | No       | View value      | Unique system-generated wage tracking code |
| 2    | Date     | Yes      | Select date     | Work session date (`YYYY-MM-DD`)           |
| 3    | Employee | Yes      | Select employee | Staff member completing production         |
| 4    | Product  | Yes      | Select product  | Manufactured item                          |

### Production details

![Production Details Section](add-wage-production-detail.png)

| Step | Field      | Required | What to Do   | Description                                            |
| ---- | ---------- | -------- | ------------ | ------------------------------------------------------ |
| 1    | Quantity   | Yes      | Enter number | Number of units produced                               |
| 2    | Wage       | Yes      | Enter rate   | Base unit rate (enter `0` to use product default rate) |
| 3    | Deductions | No       | Enter amount | Deductions subtracted from gross wage                  |
| 4    | Bonus      | No       | Enter amount | Incentive bonus added to wage                          |
| 5    | Net Wage   | No       | Read-only    | Auto-computed net payout amount                        |

### Payment information

![Payment Information Section](add-wage-payment-information.png)

| Step | Field         | Required | What to Do    | Description                                              |
| ---- | ------------- | -------- | ------------- | -------------------------------------------------------- |
| 1    | Is Paid       | Yes      | Toggle switch | Indicates whether wage has been paid                     |
| 2    | Payment Date  | No       | Select date   | Date payment was disbursed (required if `Is Paid` is ON) |
| 3    | Payment Notes | No       | Enter text    | Reference notes or payment method details                |

______________________________________________________________________

## Exception handling and error recovery

| Symptom / Error Message                         | Root Cause                                                   | Remediation Action                               |
| ----------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------ |
| `Net Wage negative`                             | Deductions exceed total earned wage plus bonus               | Review deduction amount and adjust before saving |
| `Payment Date required when Is Paid is enabled` | Form submitted with `Is Paid` enabled without a payment date | Select a valid date in **Payment Date**          |

______________________________________________________________________

## Related pages

- [Wages Overview](overview.md) — Review master list of wage vouchers
- [Create Payout](../payouts/create-payout.md) — Disburse payouts for accumulated wage balances
- [Generate Salary](../salary/generate-salary.md) — Include wage entries in periodic salary vouchers
