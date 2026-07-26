---
tags: [module:trade, task:view, role:accountant]
---

# Payment Detail

Use this page to view and manage a payment record after it has been created. The payment detail page displays all components of a payment—payment information, check and client selection, notes, and transaction status—with buttons to edit, view history, and manage the payment. Editing capabilities depend on the payment status.

## Summary

Use this page to verify payment records, monitor status-based restrictions, and review reconciliation details. It supports controlled edits while preserving audit integrity.

______________________________________________________________________

## When to use this page

- Viewing a complete payment record with all transaction information
- Checking payment status and financial impact
- Modifying payment details (if status permits)
- Linking or unlinking a payment from a bank check
- Reviewing the payment history and change log
- Validating payment amounts before reconciliation

______________________________________________________________________

## How to access this page

From the sidebar, go to **Trade → Payments**. On the Payments List page, click on any payment reference number or select a payment to open the **Payment Detail page**.

![Payment List Page](payment-list-page.png)

The page displays the payment record with all transaction details and action buttons at the top.

______________________________________________________________________

## Step-by-step instructions

1. Open **Trade → Payments** and select the payment record.
1. Review current status to confirm what can be edited.
1. Verify payment amount, date, reference, and linked party.
1. Check whether a linked check is affecting both balances.
1. Update allowed fields or notes if needed, then save changes.

______________________________________________________________________

## Field reference

- **Status** - Payment lifecycle state and permission controller.
- **Type** - Receive or Send transaction direction.
- **Reference** - Traceable identifier for reconciliation.
- **Amount** - Recorded payment value.
- **Check** - Optional check linkage that can affect both check and party balances.
- **Client/Vendor** - Counterparty linked to the payment.

______________________________________________________________________

## Page overview

The payment detail page includes action buttons at the top-right:

| Button  | Action                                  | Available When    |
| ------- | --------------------------------------- | ----------------- |
| Edit    | Open edit mode to modify payment fields | Pending status    |
| Delete  | Remove the payment from the system      | Pending or Failed |
| History | View past changes and modifications     | Always visible    |

!!! warning "Status Controls Permissions"

    Only payments with **Pending** or **Failed** status can be edited or deleted. Once a payment is marked **Passed**, it becomes read-only to protect financial records.

______________________________________________________________________

## Payment information section

![Payment Information](edit-payment-general-tab.png)

The Payment Information section displays core transaction details:

| Field     | Description                                         | Editable When |
| --------- | --------------------------------------------------- | ------------- |
| SKU       | Unique identifier for this payment (auto-generated) | Never         |
| Status    | Current state (Pending, Passed, Failed)             | Pending only  |
| Type      | Receive (from client) or Send (to vendor)           | Never         |
| Reference | Reference number or transaction ID for tracing      | Pending only  |
| Date      | Date the payment was made or received               | Pending only  |
| Amount    | Total payment amount in the default currency        | Pending only  |
| Discount  | Discount or adjustment applied (if any)             | Pending only  |

!!! note "Status Restrictions"

    Once a payment is marked **Passed**, critical fields like Amount and Date become locked to preserve the original transaction record. Pending payments are fully editable.

______________________________________________________________________

## Check and Client selection section

This section shows the parties involved in the payment:

| Field  | Description                                                                               | Editable When |
| ------ | ----------------------------------------------------------------------------------------- | ------------- |
| Check  | Bank check associated with this payment (if any). Selecting a check affects two balances. | Pending only  |
| Client | The client or vendor involved in the payment (client or vendor)                           | Never         |

!!! note "Check Impact on Balances"

    When a Check is linked to a payment, the payment amount reduces both the **client/vendor balance** AND the **check balance**. If no check is linked, only the client/vendor balance is reduced.

______________________________________________________________________

## Notes section

The Notes section contains internal comments and remarks:

| Field | Description                                    | Editable When |
| ----- | ---------------------------------------------- | ------------- |
| Notes | Internal notes, remarks, or special conditions | All statuses  |

!!! tip

    Use Notes to document payment terms, special instructions, reasons for discounts, or any other internal details related to the payment.

______________________________________________________________________

## Status and permissions

Payment management capabilities vary based on status:

| Status  | View Access | Edit Access           | Delete Access | Restrictions                                   |
| ------- | ----------- | --------------------- | ------------- | ---------------------------------------------- |
| Pending | Full        | All fields            | Yes           | None; fully editable                           |
| Passed  | Full        | Status and Notes only | No            | Cannot modify amount, date, client, or check   |
| Failed  | Full        | View only             | Yes           | Locked; preserves original reconciliation data |

!!! warning "Protect Passed Payments"

    Once a payment is marked Passed, it cannot be edited or deleted to ensure financial integrity and accurate reconciliation.

______________________________________________________________________

## Related actions

| Action       | Button/Link        | When to Use                                     |
| ------------ | ------------------ | ----------------------------------------------- |
| Edit         | **Edit** button    | Modify details for Pending payments only        |
| Delete       | **Delete** button  | Remove Pending or Failed payments               |
| Add Note     | **Notes** field    | Add internal comments or remarks (all statuses) |
| View History | **History** button | Review who changed what and when                |
| Go Back      | Back button        | Return to the Payments list                     |

______________________________________________________________________

## Tips and common issues

- **Cannot edit a Passed payment?** — Once a payment is marked Passed, it is locked. Only Status and Notes can be changed. Create a new adjustment payment if you need to modify the amount or date.
- **Delete disabled for Passed payments?** — Passed payments cannot be deleted to preserve the audit trail. Mark the payment as Failed first, then delete if needed.
- **Check linked to two balances** — Remember that selecting a check affects both the client/vendor balance and the check balance; leaving Check empty only affects the client/vendor balance.
- **Need to correct a Passed payment?** — Do not attempt to modify a Passed payment directly. Instead, create a new correction payment with the opposite amount.
- **Always save before leaving** — When editing, use the **Save** button at the bottom to apply changes. Unsaved edits will be lost.

______________________________________________________________________

## Related pages

- [Add Payment](add-payment.md)
- [Edit Payment](edit-payment.md)
- [Checks Overview](../checks/overview.md)
- [Invoices Overview](../invoices/overview.md)
