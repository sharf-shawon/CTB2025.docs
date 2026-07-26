---
tags: [module:commission, task:report, role:accountant]
---

# Manager Analytics

<!-- metadata: owner: sales_team, last_updated: 2026-07-26, git_ref: main, staging_verified: true -->

## Summary

Use this page to review manager override commission analytics in CTB Admin. Manager commissions calculate earnings based on aggregate team sales totals, manager trigger conditions, and percentage override rates defined on commission campaigns.

______________________________________________________________________

## When to use this page

- Auditing team sales manager override commissions post-campaign completion
- Verifying whether team aggregate sales satisfy campaign trigger conditions
- Reconciling manager commission earnings prior to payroll Payout
- Resolving manager inquiries regarding team sales override calculations

______________________________________________________________________

## How to access this page

From the sidebar navigation, select **Commission → Manager Analytics** (`/admin/commission/managercommissionanalytics/`).

______________________________________________________________________

## Prerequisites

- **Permissions:** `commission.view_managercommissionanalytics` permission codename (Accountant, Sales Director, or Superuser role).
- **Active Records:** Configured **Commission Campaign** with defined manager trigger rules.

______________________________________________________________________

## Step-by-step instructions

1. Open **Commission → Manager Analytics** from the sidebar.
1. Review the list of manager analytics entries, team sales volumes, and override commission amounts.
1. Use the search bar to locate specific managers or campaign names.
1. Click **Filters** to narrow results by campaign period or eligibility.
1. Click **Process Expired Campaigns** if end-of-campaign calculations require refresh.

______________________________________________________________________

## Verification and definition of done

- Master list displays manager override entries with aggregate team sales totals and percentage override figures.
- Qualified manager commission entries (`Is Eligible = True`) post to manager payout balances upon campaign finalization.

______________________________________________________________________

## Field reference

### List summary

<!-- TODO: screenshot screenshots/commission/manager-analytics-list.png -->

| Column            | Required | What to Do      | Description                                                    |
| ----------------- | -------- | --------------- | -------------------------------------------------------------- |
| Manager           | Yes      | Click link      | Sales manager employee name                                    |
| Campaign          | Yes      | View text       | Commission campaign name                                       |
| Team Sales Total  | Yes      | View amount     | Aggregate sales value achieved by team members                 |
| Trigger Condition | Yes      | View text       | Required team sales threshold for qualification                |
| Override Rate %   | Yes      | View percentage | Override commission percentage                                 |
| Commission Amount | Yes      | View amount     | `Team Sales Total * Override Rate %`                           |
| Is Eligible       | Yes      | View status     | Indicates whether team trigger condition is satisfied          |
| Status            | Yes      | View pill       | Processing state (`Calculated`, `Pending`, `Approved`, `Paid`) |

______________________________________________________________________

## Exception handling and error recovery

| Symptom / Error Message         | Root Cause                                                                        | Remediation Action                                                                          |
| ------------------------------- | --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| Manager analytics entry missing | Campaign setup lacks `Manager Trigger Condition` or `Manager Commission Rate (%)` | Open campaign in [Commission Campaigns](commission-campaigns.md) and set manager parameters |
| `Is Eligible` shows false       | Aggregate team sales total did not reach required trigger threshold               | Audit team sales invoices to verify total sales volume                                      |

______________________________________________________________________

## Related pages

- [Commission Campaigns](commission-campaigns.md) — Configure manager trigger rules and override rates
- [Employee Analytics](employee-analytics.md) — Review individual employee commission breakdowns
- [Payment History](payment-history.md) — Inspect commission payment Payouts
