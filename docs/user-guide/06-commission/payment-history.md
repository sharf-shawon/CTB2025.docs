---
tags: [module:commission, task:report, role:accountant]
---

# Payment History

<!-- metadata: owner: sales_team, last_updated: 2026-07-26, git_ref: main, staging_verified: true -->

## Summary

Use this page to audit and track commission and bonus Payouts recorded across campaigns in CTB Admin. The payment history provides a master audit ledger distinguishing settled payments from calculated analytics balances.

______________________________________________________________________

## When to use this page

- Verifying whether earned employee or manager commissions have been disbursed
- Auditing client bonus credit Payouts against campaign analytics
- Reconciling campaign ledger calculations against bank transfer or payout records
- Investigating payment queries or discrepancies raised by staff or clients

______________________________________________________________________

## How to access this page

From the sidebar navigation, select **Commission → Payment History** (`/admin/commission/commissionpaymenthistory/`).

______________________________________________________________________

## Prerequisites

- **Permissions:** `commission.view_commissionpaymenthistory` permission codename (Accountant, Finance Manager, or Superuser role).
- **Active Records:** Finalized **Commission Campaign** or **Client Bonus Campaign** analytics entries.

______________________________________________________________________

## Step-by-step instructions

1. Open **Commission → Payment History** from the sidebar.
1. Review listed payment records, Payout dates, and amounts.
1. Use the search bar to locate specific employees, managers, or client names.
1. Click **Filters** to narrow results by campaign, date range, or payment type.
1. Click a payment row to inspect transaction details or linked payout references.

______________________________________________________________________

## Verification and definition of done

- Payment history list displays settled transactions with confirmed Payout dates.
- Verified Payouts update linked employee payout vouchers or client credit balances.

______________________________________________________________________

## Field reference

### List summary

<!-- TODO: screenshot screenshots/commission/payment-history-list.png -->

| Column        | Required | What to Do  | Description                                                              |
| ------------- | -------- | ----------- | ------------------------------------------------------------------------ |
| Reference SKU | No       | View value  | Unique payment tracking reference code                                   |
| Campaign      | Yes      | View text   | Parent commission or client bonus campaign                               |
| Recipient     | Yes      | Click link  | Name of employee, manager, or client recipient                           |
| Type          | Yes      | View status | Payment type (`Employee Commission`, `Manager Override`, `Client Bonus`) |
| Amount Paid   | Yes      | View amount | Disbursed payment amount                                                 |
| Payment Date  | Yes      | View date   | Transaction settlement date                                              |
| Method        | No       | View text   | Disbursal method (`Bank Transfer`, `Cash`, `Ledger Credit`)              |

______________________________________________________________________

## Exception handling and error recovery

| Symptom / Error Message                           | Root Cause                                         | Remediation Action                                                                    |
| ------------------------------------------------- | -------------------------------------------------- | ------------------------------------------------------------------------------------- |
| Payment record missing despite approved analytics | Payout transaction not completed in payouts module | Process payout voucher under [Create Payout](../04-employee/payouts/create-payout.md) |
| Disbursed amount mismatch                         | Partial payment issued or deduction applied        | Compare payment history line item against [Employee Analytics](employee-analytics.md) |

______________________________________________________________________

## Related pages

- [Employee Analytics](employee-analytics.md) — Review employee campaign earnings
- [Manager Analytics](manager-analytics.md) — Review manager override earnings
- [Client Bonus Analytics](client-bonus-analytics.md) — Review client bonus earnings
- [Create Payout](../04-employee/payouts/create-payout.md) — Issue employee payouts
