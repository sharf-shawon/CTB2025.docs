---
tags: [module:commission, task:create, role:accountant]
---

# Client Bonus Campaigns

<!-- metadata: owner: sales_team, last_updated: 2026-07-26, git_ref: main, staging_verified: true -->

## Summary

Use this page to create and manage client bonus campaigns in CTB Admin. Client bonus campaigns reward wholesale or retail clients based on sales targets, order quantities, and payment collection thresholds.

______________________________________________________________________

## When to use this page

- Launching promotional bonus programs for key client accounts
- Setting client sales target thresholds and reward percentage tiers
- Managing active bonus campaign dates and client eligibility rules
- Reviewing client bonus calculation parameters

______________________________________________________________________

## How to access this page

From the sidebar navigation, select **Commission → Client Bonus Campaigns** (`/admin/commission/clientbonuscampaign/`).

______________________________________________________________________

## Prerequisites

- **Permissions:** `commission.add_clientbonuscampaign` / `commission.change_clientbonuscampaign` permission codenames (Accountant, Sales Manager, or Superuser role).
- **Active Records:** Active **Client** profiles and **Product** catalog entries.

______________________________________________________________________

## Step-by-step instructions

1. Open **Commission → Client Bonus Campaigns** from the sidebar.
1. Click **Add Client Bonus Campaign (+)**.
1. Enter the **Campaign Name**, **Start Date**, and **End Date**.
1. Select the target **Clients** participating in the promotion.
1. Set the **Collection Threshold %** and **Bonus Rate (%)**.
1. Click **Save** to activate the client bonus campaign.

______________________________________________________________________

## Verification and definition of done

- System creates the client bonus campaign record (`CBC-YYYYMMDD-XXXX`).
- Campaign lists under `/admin/commission/clientbonuscampaign/` and applies to eligible client sales orders.

______________________________________________________________________

## Field reference

### Campaign details

![Client Bonus Campaigns](Add-Client-Bonus-Campaign.png)

| Step | Field                  | Required | What to Do       | Description                                              |
| ---- | ---------------------- | -------- | ---------------- | -------------------------------------------------------- |
| 1    | Campaign Name          | Yes      | Enter name       | Descriptive client bonus campaign title                  |
| 2    | Start Date             | Yes      | Select date      | First day of client bonus eligibility period             |
| 3    | End Date               | Yes      | Select date      | Last day of client bonus eligibility period              |
| 4    | Client                 | Yes      | Select client    | Target wholesale or retail client account                |
| 5    | Collection Threshold % | Yes      | Enter percentage | Minimum collection percentage for bonus eligibility      |
| 6    | Bonus Rate (%)         | Yes      | Enter percentage | Bonus reward percentage applied to eligible sales volume |
| 7    | Is Finalized           | Yes      | Toggle switch    | Indicates whether bonus snapshots have been locked       |

______________________________________________________________________

## Exception handling and error recovery

| Symptom / Error Message       | Root Cause                                                  | Remediation Action                                                     |
| ----------------------------- | ----------------------------------------------------------- | ---------------------------------------------------------------------- |
| Client bonus not calculated   | Order sales volume below threshold or collection incomplete | Ensure client invoice payments satisfy collection threshold percentage |
| Cannot edit campaign settings | Campaign is marked `Is Finalized`                           | Uncheck `Is Finalized` state before making rule adjustments            |

______________________________________________________________________

## Related pages

- [Client Bonus Analytics](client-bonus-analytics.md) — Review client bonus performance and balances
- [Commission Campaigns](commission-campaigns.md) — Manage employee commission campaigns
- [Clients Overview](../01-business/clients/overview.md) — Manage client directory profiles
