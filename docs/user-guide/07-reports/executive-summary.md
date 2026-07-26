---
tags: [module:reports, task:view, role:accountant]
---

# Executive Summary

## Summary

The Executive Summary page provides a consolidated, printable report of key business metrics across invoices, payments, checks, vouchers, materials purchased, and product stock levels for a selectable date range. Use it to get a quick management-level view and drill into specific underlying transactions.

______________________________________________________________________

## When to use this page

- You need a one-page overview of recent invoicing and payment activity.
- Preparing a printable summary for executive management review.
- Verifying cashflow items (sent/received payments and checks) for a specific date range.
- Reviewing material purchases and current product stock levels.

______________________________________________________________________

## How to access this page

Open **Reports → Executive Summary** in the left sidebar under **Reports**.

______________________________________________________________________

## Prerequisites

- Active user session with `reports.view_executivesummary` permission.
- Relevant transactions (invoices, payments, checks, vouchers, purchases, stock) must exist for the selected date range.

______________________________________________________________________

## Step-by-step instructions

![Executive Summary Page](executive-summary-page-img.png)

1. Open **Reports → Executive Summary** from the left sidebar.
1. Select the **Start Date** and **End Date** in the Date Range Filter.
1. Click **Apply Filter** to recalculate metrics for the selected period.
1. Inspect the **Invoice & Tender Invoice Statistics** section for per-date invoice totals.
1. Review cleared cashflow items in **Sent Payments**, **Received Payments**, **Sent Checks**, and **Received Checks**.
1. Inspect **Bounced & Upcoming Checks** to identify returned or scheduled check items.
1. Check **Client Transactions Summary** to review client-level debit/credit balances.
1. Review **Voucher Statistics**, **Materials Purchased**, and **Product Stock Levels**.
1. Click **Print Report** (top-right) to generate a PDF or print a hard copy summary.

______________________________________________________________________

## Verification & definition of done

- **Data accuracy**: Summary grand totals match the sum of individual cleared ledger entries for the period.
- **Export confirmation**: Clicking **Print Report** renders a clean print layout without browser chrome or sidebar navigation.

______________________________________________________________________

## Field reference

- **Start Date** — First date included in the report filter range.
- **End Date** — Last date included in the report filter range.
- **Apply Filter** — Refreshes all summary metrics and tables for the selected date range.
- **Invoice & Tender Invoice Statistics** — Table listing per-date invoice count, subtotal, discounts, and payable amounts.
- **Sent Payments (Passed)** — List of sent/cleared vendor payments with date, vendor, and amount.
- **Received Payments (Passed)** — List of received/cleared client payments with date, client, and amount.
- **Sent Checks (Passed) / Received Checks (Passed)** — Tables showing cleared bank checks.
- **Bounced & Upcoming Checks** — List of scheduled or returned bank checks.
- **Client Transactions Summary** — Per-client summary showing debit balances, credit balances, and discounts.
- **Voucher Statistics** — Date-wise count and aggregate value of approved purchase vouchers.
- **Materials Purchased** — List of raw material purchases with quantity, unit, and total cost.
- **Product Stock Levels** — Current finished goods inventory snapshot.

______________________________________________________________________

## Exception handling & error recovery

| Error Code / Symptom     | Root Cause                                                         | Step-by-step remediation procedure                                                                                        | Actionable role required           |
| ------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------- | ---------------------------------- |
| Zero results in report   | Filter date range excludes active transactions or no records exist | 1. Expand **Start Date** and **End Date** filters.<br>2. Verify invoices and payments exist in **Trade** for that period. | `accountant`                       |
| Discrepancy in totals    | Draft or unposted transactions excluded from report                | 1. Open **Trade → Invoices**.<br>2. Confirm draft invoices are posted or approved.                                        | `accountant` / `admin`             |
| Negative material amount | Recorded material return exceeds gross purchase quantity           | 1. Open **Factory → Materials**.<br>2. Verify return vouchers and stock adjustment logs.                                  | `staff` $\rightarrow$ `accountant` |

______________________________________________________________________

## Related workflows & next steps

- **[Product Return Report](product-return-report.md)** — Audit client product returns affecting net sales figures.
- **[Monthly Attendance Report](attendance-report.md)** — Review labor costs and attendance grid tallies.

______________________________________________________________________

## Related pages

- **[Reports](../README.md)** — All available executive and operational reporting tools.
