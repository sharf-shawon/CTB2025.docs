---
tags: [module:trade, task:create, role:accountant]
---

# Create Invoice

<!-- metadata: owner: trade_team, last_updated: 2026-07-26, git_ref: main, staging_verified: true -->

## Summary

Use this page to create client invoices with line items, applicable taxes, shipping charges, and total calculations in one unified workflow. A correctly prepared invoice records sales transactions, manages accounts receivable, and ensures accurate financial reporting.

______________________________________________________________________

## When to use this page

- Selling CTB garment or bag products directly to registered client accounts
- Issuing billing documentation for completed production orders or stock shipments
- Creating commercial tender invoices or quotations for client approval
- Recording direct sales transactions to track sales commissions and accounts receivable

______________________________________________________________________

## How to access this page

From the sidebar, go to **Trade → Invoices** (`/en/admin/Trade/invoice/`). On the Invoices List page, click the **purple (+) icon** in the top-right corner.

______________________________________________________________________

## Prerequisites

- **Active Client**: The target client account must exist in **Business → Clients** with valid contact information.
- **Client Balance Limit**: The client account should have an assigned balance limit. If an invoice exceeds this limit, the system locks its status to `Draft` until approved.
- **Required User Permissions**:
    - `Trade | Invoice | Can add Invoice` (`trade.add_invoice`)
    - `Trade | Invoice | Can view invoice reports and analytics` (`trade.view_invoice_reports`) for historical reporting
    - **Superuser Privilege**: Required to click **Approve** on invoices exceeding a client's credit balance limit.

______________________________________________________________________

## Step-by-step instructions

1. Open **Trade → Invoices** and click **(+) Add Invoice**.
1. In the **General Information** tab, select the target **Client** from the dropdown menu.
1. Confirm or set the **Invoice Date** and assign a **Salesperson** for commission attribution.
1. Set the initial **Status** (`Draft`, `Sent`, `Quotation`, etc.).
1. Switch to the **Items** tab and select a **Product** from the line-item dropdown.
1. Enter the **Quantity** and unit **Selling Rate**. The system calculates the item total automatically.
1. Click **Add another Item** if billing multiple products on the same invoice.
1. Enter optional order charges in **Payment Details**: **Tax**, **VAT**, **Shipping**, or **Discount**.
1. Add internal notes or payment terms under **Notes** if required.
1. Click **Save** to complete invoice generation or **Save and continue editing** to verify calculations.

______________________________________________________________________

## Verification & definition of done

- **Database Record Created**: The invoice displays a unique SKU/Invoice Number format (`INV-YYYYMMDD-XXXX`).
- **Status Verification**: The invoice status pill reflects `Draft` or `Sent` on the list view.
- **Client Ledger Update**: If saved as `Sent`, the payable amount is credited to the client's balance statement.
- **Commission Attribution**: The invoice appears under the designated salesperson's sales summary report.

______________________________________________________________________

## Field reference

| Field Name         | Type    | Required | Backend Validation / Constraints                                      | Description                                                                |
| :----------------- | :------ | :------- | :-------------------------------------------------------------------- | :------------------------------------------------------------------------- |
| **Invoice Number** | Text    | Yes      | Max 20 characters, unique constraint                                  | Unique tracking number for the invoice. Auto-generated if left blank.      |
| **Invoice Date**   | Date    | Yes      | Valid date (`YYYY-MM-DD`)                                             | Billing date used in financial accounting and reporting periods.           |
| **Client**         | Select  | Yes      | Foreign Key (`Business.Client`), `PROTECT` on delete                  | The registered client account being billed.                                |
| **Salesperson**    | Select  | No       | Foreign Key (`Employee.Employee`), `SET_NULL`                         | Staff member responsible for the sale. Used for commission calculation.    |
| **Status**         | Select  | Yes      | Choices: `Draft`, `Sent`, `Cancelled`, `Pending Approval`             | Current lifecycle state. Exceeding client balance locks status to `Draft`. |
| **Type**           | Select  | Yes      | Choices: `Invoice`, `Tender Invoice`, `Quotation`, `Tender Quotation` | Category of document issued to the client.                                 |
| **Subtotal**       | Decimal | Auto     | Max 13 digits, 3 decimal places                                       | Sum of all line item totals (`Quantity × Rate`).                           |
| **Tax**            | Decimal | No       | Default `0.00`, 2 decimal places                                      | Additional tax charge applied to the total order.                          |
| **VAT**            | Decimal | No       | Default `0.00`, 3 decimal places                                      | Value-added tax amount.                                                    |
| **Shipping**       | Decimal | No       | Default `0.00`, 3 decimal places                                      | Freight or delivery charges.                                               |
| **Discount**       | Decimal | No       | Default `0.00`, 2 decimal places                                      | Total order discount deducted from payable amount.                         |
| **Payable**        | Decimal | Auto     | `Subtotal + Tax + VAT + Shipping - Discount`                          | Final net amount due from the client.                                      |

______________________________________________________________________

## Exception handling & error recovery

| Error Symptom / Message                            | Root Cause                                                                              | Step-by-Step Remediation                                                                                                                                                 |
| :------------------------------------------------- | :-------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Status locked to Draft / Cannot change to Sent** | Invoice payable total exceeds the client's balance limit set in **Business → Clients**. | 1. Contact a superuser to review the invoice.<br>2. Superuser opens the invoice and clicks **Approve**.<br>3. Once approved, update status to `Sent` and click **Save**. |
| **"Invoice Number already exists"**                | Duplicate invoice number entered manually.                                              | 1. Clear the **Invoice Number** field to let the system generate a unique sequence.<br>2. Alternatively, enter a non-conflicting manual number.                          |
| **"Cannot delete client with existing invoices"**  | Django protection constraint (`models.PROTECT`) prevents client removal.                | 1. Reassign or delete associated invoices before deleting the client record.<br>2. Mark client as inactive instead of deleting.                                          |
| **Subtotal / Payable mismatch**                    | Deleted line items still cached in form state prior to saving.                          | 1. Click **Save and continue editing** to recalculate totals.<br>2. Verify each line item quantity and rate.                                                             |

______________________________________________________________________

## Related workflows & next steps

- **Add Payment** — Record client payments received against this invoice.
- **Edit Invoice** — Modify items or charges on existing draft invoices.
- **Print Invoice** — Export a PDF or print a hard copy invoice for the client.
- **Invoice Reports** — View accounts receivable summaries and sales analytics.

______________________________________________________________________

## Related pages

- **Invoice Detail** — View or edit invoice details after creation
- **Edit Invoice** — Update invoice information and items
- **Print Invoice** — Generate a printable or shareable invoice document
- **Invoice Reports** — Analyze sales data and outstanding payments
