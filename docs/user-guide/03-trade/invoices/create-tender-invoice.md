---
tags: [module:trade, task:create, role:accountant]
---

# Create Tender Invoice

## Summary

Use this page to create a tender invoice for a client. A tender invoice is a quotation or formal bid document used to propose itemized goods or services and pricing before a client commits to purchase. Tender invoices help track proposals and negotiate terms with clients.

______________________________________________________________________

## When to use this page

- Processing orders for tender order products
- Creating invoices for custom or special requests received from clients
- Issuing payment requests for tender-based products or services

______________________________________________________________________

## How to access this page

From the sidebar, go to **Trade → Tender Invoices**. On the Tender Invoices List page, click the **purple (+) icon** in the top-right corner.

The system opens the **Create Tender Invoice Page**.

______________________________________________________________________

## Step-by-step instructions

1. Open **Create Tender Invoice** from the **Trade** section of the sidebar.
1. Complete the **General information** section described below.
1. Complete the **Payment details** section described below.
1. Complete the **Add items** section described below.
1. Complete the **Terms and conditions** section described below.
1. Follow **Saving the Tender Invoice** below to finish.

______________________________________________________________________

## Field reference

### General information

Fill in the following fields on the General tab:

| Step | Field         | What to Do              | Description                              |
| ---- | ------------- | ----------------------- | ---------------------------------------- |
| 1    | Tender Number | Auto-generated or enter | Unique identifier for this tender        |
| 2    | Tender Date   | Select date             | Date the tender is issued                |
| 3    | Client        | Select client           | The client receiving the tender proposal |
| 4    | Status        | Select status           | Current state (Draft, sent, cancelled)   |
| 5    | Valid Until   | Select date             | Expiration date for the tender offer     |

!!! warning "Required Fields"

    Fields marked with a **red star (\*)** are mandatory.

### Payment details

Configure the financial details of the tender proposal:

| Step | Field    | What to Do      | Description                                                        |
| ---- | -------- | --------------- | ------------------------------------------------------------------ |
| 1    | Subtotal | Auto-calculated | Sum of all item totals (Quantity × Rate)                           |
| 2    | Tax      | Enter amount    | Tax if applicable                                                  |
| 3    | VAT      | Enter amount    | Value-added tax if applicable                                      |
| 4    | Shipping | Enter amount    | Shipping or delivery charges if applicable                         |
| 5    | Discount | Enter amount    | Discount offered on the tender proposal                            |
| 6    | Total    | Auto-calculated | Final proposed amount (Subtotal + Tax + VAT + Shipping - Discount) |

!!! note

    The total is calculated automatically based on items and payment adjustments.

### Add items

Add products or services to the tender proposal:

| Step | Field   | What to Do           | Description                         |
| ---- | ------- | -------------------- | ----------------------------------- |
| 1    | Product | Select from dropdown | The product or service being quoted |
| 2    | Rate    | Enter or select      | Proposed unit price                 |
| 3    | Qty     | Enter quantity       | Number of units being quoted        |
| 4    | Total   | Auto-calculated      | Qty × Rate for this line item       |

- Click **Add another Item** to add multiple products to the tender
- Click the **trash icon** to remove an item
- Use the **edit icon** to modify an item's details

!!! tip

    Keep rates competitive but profitable. Each item's total calculates automatically.

### Terms and conditions

Add optional notes or special terms:

| Step | Field | What to Do | Description                                          |
| ---- | ----- | ---------- | ---------------------------------------------------- |
| 1    | Terms | Enter text | Payment terms, delivery conditions, or special notes |
| 2    | Note  | Enter text | Internal comments about the tender                   |

______________________________________________________________________

## Saving the Tender Invoice

After completing all sections:

- Click **Save** to create the tender as Draft/sent/cancelled based on the status you selected
- Click **Save and continue editing** to save and stay on the page
- Click **Save and add another** to save and create another tender immediately

The tender invoice is now ready to be sent to the client or processed for payment.

______________________________________________________________________

## Tips and common issues

- **Client is required** — You must select a client before saving
- **Valid Until date matters** — Set an expiration date so the tender doesn't stay open indefinitely
- **Status tracks the tender lifecycle** — Use Status to mark tenders as Draft, Sent, Cancelled
- **Keep detailed Terms** — Include payment terms, delivery date, and any conditions in the Terms field

______________________________________________________________________

## Related pages

- **Tender Detail** — View tender details and client responses
- **Edit Tender Invoice** — Update terms and items before sending
- **Convert to Invoice** — Convert an accepted tender into a standard invoice
- **Invoice Reports** — Track accepted tenders and revenue forecasts
