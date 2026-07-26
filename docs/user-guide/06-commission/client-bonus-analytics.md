---
tags: [module:commission, task:report, role:accountant]
---

# Client Bonus Analytics

<!-- metadata: owner: sales_team, last_updated: 2026-07-26, git_ref: main, staging_verified: true -->

## Summary

Use this page to review client bonus campaign performance and earned bonus credits in CTB Admin. The analytics summary aggregates sales volumes, payment collection rates, target qualifications, and calculated bonus rewards for wholesale and retail clients.

______________________________________________________________________

## When to use this page

- Auditing client bonus eligibility following campaign completion
- Verifying client sales target achievements and collection ratios
- Reconciling client bonus credits before applying ledger adjustments
- Resolving client inquiries regarding promotional bonus earnings

______________________________________________________________________

## How to access this page

From the sidebar navigation, select **Commission → Client Bonus Analytics** (`/admin/commission/clientbonusanalytics/`).

______________________________________________________________________

## Prerequisites

- **Permissions:** `commission.view_clientbonusanalytics` permission codename (Accountant, Sales Manager, or Superuser role).
- **Active Records:** Configured **Client Bonus Campaign** and **Client** accounts.

______________________________________________________________________

## Step-by-step instructions

1. Open **Commission → Client Bonus Analytics** from the sidebar.
1. Review the list of client bonus records, achievement metrics, and qualification statuses.
1. Use the search bar to locate specific client accounts or campaign names.
1. Click **Filters** to narrow results by campaign date range or eligibility.
1. Click **Process Expired Campaigns** if end-of-campaign snapshots require generation.

______________________________________________________________________

## Verification and definition of done

- Master list renders client bonus records with calculated sales volumes and reward figures.
- Qualified client bonus entries (`Is Eligible = True`) post to client credit accounts upon finalization.

______________________________________________________________________

## Field reference

### List summary

<!-- TODO: screenshot screenshots/commission/client-bonus-analytics-list.png -->

| Column       | Required | What to Do      | Description                                                        |
| ------------ | -------- | --------------- | ------------------------------------------------------------------ |
| Client       | Yes      | Click link      | Target client account name                                         |
| Campaign     | Yes      | View text       | Client bonus campaign name                                         |
| Sales Volume | Yes      | View amount     | Qualifying invoice sales total                                     |
| Collection % | Yes      | View percentage | Payment collection ratio                                           |
| Bonus Amount | Yes      | View amount     | Calculated client bonus credit                                     |
| Is Eligible  | Yes      | View status     | Indicates whether qualification rules are satisfied                |
| Status       | Yes      | View pill       | Settlement state (`Calculated`, `Pending`, `Approved`, `Credited`) |

______________________________________________________________________

## Exception handling and error recovery

| Symptom / Error Message              | Root Cause                                      | Remediation Action                                                                                 |
| ------------------------------------ | ----------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| Client bonus not calculated          | Client sales volume below campaign target quota | Verify client invoices and collection ratio in [Client Bonus Campaigns](client-bonus-campaigns.md) |
| Credit missing from client statement | Bonus record status remains `Pending`           | Approve and finalize campaign snapshots to post credits to client ledger                           |

______________________________________________________________________

## Related pages

- [Client Bonus Campaigns](client-bonus-campaigns.md) — Configure client promotional campaigns
- [Payment History](payment-history.md) — Track settled bonus credit payments
- [Clients Overview](../01-business/clients/overview.md) — View client account balances
