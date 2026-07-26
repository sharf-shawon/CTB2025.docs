---
tags: [module:trade, task:create, role:accountant]
---

# Add Payment

<!-- metadata: owner: trade_team, last_updated: 2026-07-26, git_ref: main, staging_verified: true -->

## Summary

Use this page to record cash, bank transfer, or check payments received from clients or paid to vendors. Accurately entering payment records updates financial ledgers, calculates sales commissions, and supports bank reconciliation.

______________________________________________________________________

## When to use this page

- Recording a payment received from a client for an outstanding invoice
- Recording a payment sent to a vendor for stock or raw material purchases
- Applying payments using a physical bank check linked to a registered check record
- Documenting discounts or adjustments during invoice settlements
- Recording collector commissions for account officers

______________________________________________________________________

## How to access this page

From the sidebar, go to **Trade → Payments** (`/en/admin/Trade/payment/`). On the Payments List page, click the **purple (+) icon** in the top-right corner.

______________________________________________________________________

## Prerequisites

- **Active Counterparty**: The target client or vendor record must exist in **Business → Clients** or **Business → Vendors**.
- **Bank Check (Optional)**: If linking a bank check, the check record must be registered under **Trade → Checks**.
- **Required User Permissions**:
    - `Trade | Payment | Can add Payment` (`trade.add_payment`)
    - `Trade | Payment | Can change Payment` (`trade.change_payment`) for post-entry approvals.

______________________________________________________________________

## Step-by-step instructions

1. Open **Trade → Payments** and click **(+) Add Payment**.
1. Select the payment **Type** (`Receive` for client receipts, `Send` for vendor payouts).
1. Select either a **Client** or a **Vendor** depending on the payment direction.
1. Enter the **Reference** number (transaction ID, bank slip, or receipt number).
1. Specify the payment **Date** and total **Amount**.
1. Enter an optional **Discount** if an adjustment was granted.
1. Select the **Collected By** employee for commission tracking.
1. Select a registered **Check** if payment was made via bank check.
1. Toggle **Is Approved** if you have verification authority.
1. Click **Save** to create the payment record.

______________________________________________________________________

## Verification & definition of done

- **Auto-Generated SKU**: System assigns a unique payment SKU (`PMN-YYYYMMDD-XXXX`).
- **Ledger Deduction**:
    - For client receipts (`Receive`), the client's outstanding balance is credited.
    - For vendor payments (`Send`), vendor payable balance is reduced.
- **Check Reconciliation**: If a check was selected, both counterparty balance and check balance update simultaneously.
- **Commission Allocation**: The payment amount registers under the designated `Collected By` employee's monthly report.

______________________________________________________________________

## Field reference

| Field Name       | Type    | Required    | Backend Validation / Constraints                           | Description                                                        |
| :--------------- | :------ | :---------- | :--------------------------------------------------------- | :----------------------------------------------------------------- |
| **SKU**          | Text    | Auto        | Prefix `PMN`, read-only                                    | Unique system-generated tracking code.                             |
| **Type**         | Select  | Yes         | Choices: `Send`, `Receive`; Default: `Receive`             | Transaction direction.                                             |
| **Client**       | Select  | Conditional | Foreign Key (`Business.Client`), `PROTECT`                 | Target client for `Receive` payments. Required if Vendor is empty. |
| **Vendor**       | Select  | Conditional | Foreign Key (`Business.Vendor`), `PROTECT`                 | Target vendor for `Send` payments. Required if Client is empty.    |
| **Reference**    | Text    | Yes         | Max 50 characters                                          | External receipt, invoice, or transaction reference code.          |
| **Date**         | Date    | Yes         | Default: `timezone.now`                                    | Date payment was executed.                                         |
| **Amount**       | Decimal | Yes         | Max 13 digits, 3 decimal places                            | Total payment value recorded.                                      |
| **Discount**     | Decimal | No          | Default `0.00`, 3 decimal places                           | Discount or adjustment applied.                                    |
| **Status**       | Select  | Yes         | Choices: `Pending`, `Passed`, `Failed`, `Pending Approval` | Current payment status.                                            |
| **Is Approved**  | Boolean | No          | Default `False`                                            | Administrative approval flag.                                      |
| **Check**        | Select  | No          | Foreign Key (`Trade.Checks`), soft-delete protection       | Optional check record linked to this payment.                      |
| **Collected By** | Select  | No          | Foreign Key (`Employee.Employee`), `SET_NULL`              | Staff member responsible for payment collection.                   |

______________________________________________________________________

## Exception handling & error recovery

| Error Symptom / Message                               | Root Cause                                                                            | Step-by-Step Remediation                                                                                                             |
| :---------------------------------------------------- | :------------------------------------------------------------------------------------ | :----------------------------------------------------------------------------------------------------------------------------------- |
| **"Cannot delete counterparty with linked payments"** | Foreign Key protection constraint (`models.PROTECT`) prevents client/vendor deletion. | 1. Soft-delete or archive the payment records prior to deleting counterparty.<br>2. Keep client active while payments remain posted. |
| **Payment amount did not update check balance**       | Payment created without selecting a check in **Check** dropdown.                      | 1. Edit the payment record.<br>2. Select the valid check from **Check** dropdown and click **Save**.                                 |
| **Double balance deduction error**                    | Multiple payments linked to the same check record.                                    | 1. Inspect **Trade → Checks** to verify linked payment history.<br>2. Disassociate duplicate payment entries.                        |

______________________________________________________________________

## Related workflows & next steps

- **Manage Checks** — View, add, or clear linked bank checks.
- **Client Ledger** — Review updated client account statements.
- **Commission Reports** — Track payment collection commissions per employee.

______________________________________________________________________

## Related pages

- **Payments Overview** — View all payments
- **Payment Detail** — View payment details and history
- **Checks Overview** — Manage bank checks
- **Invoices Overview** — Manage invoices and sales records
