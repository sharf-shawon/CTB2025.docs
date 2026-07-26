---
tags: [module:commission, task:report, role:accountant]
---

# Employee Analytics

<!-- metadata: owner: sales_team, last_updated: 2026-07-26, git_ref: main, staging_verified: true -->

## Summary

Use this page to review and process employee commission performance analytics in CTB Admin. The system calculates units sold, payment collection percentages, target achievement levels, and net earned commission amounts for active and completed campaigns.

______________________________________________________________________

## When to use this page

- Auditing employee commission calculations following campaign completion
- Verifying whether individual commission records satisfy eligibility rules
- Triggering automated snapshot calculations via **Process Expired Campaigns**
- Manually entering or adjusting employee commission analytics vouchers

______________________________________________________________________

## How to access this page

From the sidebar navigation, select **Commission → Employee Analytics** (`/admin/commission/employeecommissionanalytics/`).

______________________________________________________________________

## Prerequisites

- **Permissions:** `commission.view_employeecommissionanalytics` / `commission.add_employeecommissionanalytics` permission codenames (Accountant, Sales Manager, or Superuser role).
- **Active Records:** Configured **Commission Campaign** and **Employee** profiles.

______________________________________________________________________

## Step-by-step instructions

1. Open **Commission → Employee Analytics** from the sidebar.
1. Review the list of employee analytics records, target achievements, and status pills.
1. Use the search bar or click **Filters** to locate specific employees or campaigns.
1. Click **Process Expired Campaigns** to generate snapshots for concluded campaigns.
1. Click **Add Employee Commission Analytics (+)** to enter manual adjustments when required.

______________________________________________________________________

## Verification and definition of done

- Commission analytics entries display calculated achievement quantities and earnings.
- Eligible records (`Is Eligible = True`) update the employee payout ledger upon campaign finalization.

______________________________________________________________________

## Field reference

### List summary

![Employee Analytics List Page](employee-analytics-list-page.png)

| Column            | Required | What to Do  | Description                                                    |
| ----------------- | -------- | ----------- | -------------------------------------------------------------- |
| Employee          | Yes      | Click link  | Target sales employee                                          |
| Campaign          | Yes      | View text   | Associated commission campaign name                            |
| Product           | Yes      | View text   | Campaign product item                                          |
| Achievement Qty   | Yes      | View number | Net units sold by employee during campaign                     |
| Commission Amount | Yes      | View amount | Calculated commission earnings                                 |
| Is Eligible       | Yes      | View status | Indicates whether eligibility rules are met                    |
| Status            | Yes      | View pill   | Processing state (`Calculated`, `Pending`, `Approved`, `Paid`) |

### Manual entry fields

![Add Employee Analytics](add-employee-commission-analytics.png)

| Step | Field                   | Required | What to Do       | Description                         |
| ---- | ----------------------- | -------- | ---------------- | ----------------------------------- |
| 1    | Campaign                | Yes      | Select campaign  | Parent commission campaign          |
| 2    | Employee                | Yes      | Select employee  | Target sales employee               |
| 3    | Product                 | Yes      | Select product   | Campaign product item               |
| 4    | Target Qty              | Yes      | Enter number     | Minimum target quota                |
| 5    | Achievement Qty         | Yes      | Enter number     | Actual units sold                   |
| 6    | Total Sales Qty         | Yes      | Enter number     | Gross units sold                    |
| 7    | Total Sales Amount      | Yes      | Enter amount     | Gross sales value                   |
| 8    | Total Payment Collected | Yes      | Enter amount     | Cash/check payments collected       |
| 9    | Payment Collection %    | Yes      | Enter percentage | Collection ratio percentage         |
| 10   | Commission Rate         | Yes      | Enter rate       | Fixed unit rate                     |
| 11   | Commission Amount       | Yes      | Enter amount     | `Achievement Qty * Commission Rate` |
| 12   | Is Eligible             | Yes      | Toggle switch    | Qualification flag                  |

______________________________________________________________________

## Exception handling and error recovery

| Symptom / Error Message              | Root Cause                                              | Remediation Action                                                          |
| ------------------------------------ | ------------------------------------------------------- | --------------------------------------------------------------------------- |
| Analytics missing for ended campaign | Automated snapshot job not triggered                    | Click **Process Expired Campaigns** in header to force snapshot generation  |
| `Is Eligible` shows false            | Payment collection ratio below `Collection Threshold %` | Collect outstanding Client invoice balances to achieve collection threshold |

______________________________________________________________________

## Related pages

- [Commission Campaigns](commission-campaigns.md) — Manage campaign rules and target products
- [Manager Analytics](manager-analytics.md) — Review manager override commission results
- [Payment History](payment-history.md) — Inspect commission payment records
