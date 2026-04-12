# Create Quotation

Use this page to create a quotation for a client. A quotation is a formal price estimate or proposal document that outlines products or services, quantities, and pricing. Quotations help clients understand costs before committing to a purchase order.

## When to use Create Quotation

- Responding to a client's inquiry with a price estimate
- Providing a cost breakdown for custom or bulk orders
- Creating a formal quotation document for sales negotiations
- Tracking proposed pricing and terms for potential deals

## How to access this page

From the sidebar, go to **Trade Management → Quotations**. On the Quotations List page, click the **purple (+) icon** in the top-right corner.

The system opens the **Create Quotation Page**.

______________________________________________________________________

## General Information

Fill in the following fields on the General tab:

| Step | Field            | What to Do              | Description                                  |
| ---- | ---------------- | ----------------------- | -------------------------------------------- |
| 1    | Quotation Number | Auto-generated or enter | Unique identifier for this quotation         |
| 2    | Quotation Date   | Select date             | Date the quotation is issued                 |
| 3    | Client           | Select client           | The customer receiving the quotation         |
| 4    | Status           | Select status           | Current state (Draft, Sent, Cancelled, etc.) |
| 5    | Valid Until      | Select date             | Expiration date for the quotation validity   |

!!! warning "Required Fields"
Fields marked with a **red star (\*)** are mandatory.

______________________________________________________________________

## Payment Details

After adding items, configure the financial details:

| Step | Field    | What to Do      | Description                                                        |
| ---- | -------- | --------------- | ------------------------------------------------------------------ |
| 1    | Subtotal | Auto-calculated | Sum of all item totals (Quantity × Rate)                           |
| 2    | Tax      | Enter amount    | Tax to be charged on the quotation                                 |
| 3    | VAT      | Enter amount    | Value-added tax if applicable                                      |
| 4    | Shipping | Enter amount    | Shipping or delivery charges if applicable                         |
| 5    | Discount | Enter amount    | Discount offered on the quotation                                  |
| 6    | Total    | Auto-calculated | Final proposed amount (Subtotal + Tax + VAT + Shipping - Discount) |

!!! note
The total is calculated automatically based on items and payment adjustments.

______________________________________________________________________

## Add Items

Add products or services to the quotation:

| Step | Field   | What to Do           | Description                         |
| ---- | ------- | -------------------- | ----------------------------------- |
| 1    | Product | Select from dropdown | The product or service being quoted |
| 2    | Rate    | Enter or select      | Proposed unit price                 |
| 3    | Qty     | Enter quantity       | Number of units being quoted        |
| 4    | Total   | Auto-calculated      | Qty × Rate for this line item       |

- Click **Add another Item** to add multiple products to the quotation
- Click the **trash icon** to remove an item
- Use the **edit icon** to modify an item's details

!!! tip
Each item's total is calculated automatically once you enter Rate and Qty.

______________________________________________________________________

## Terms and Notes

Add optional terms, conditions, or internal notes:

| Step | Field | What to Do | Description                                          |
| ---- | ----- | ---------- | ---------------------------------------------------- |
| 1    | Terms | Enter text | Payment terms, delivery conditions, or special notes |
| 2    | Note  | Enter text | Internal comments about the quotation                |

______________________________________________________________________

## Saving the Quotation

After completing all sections:

- Click **Save** to create the quotation as Draft/sent/cancelled based on the status you selected
- Click **Save and continue editing** to save and stay on the page
- Click **Save and add another** to save and create another quotation immediately

The quotation is now ready to be sent to the client for review.

______________________________________________________________________

!!! Tips and Common Issues

- **Client is required** — You must select a client before saving <br>
- **Valid Until date matters** — Set an expiration date so the quotation doesn't stay valid indefinitely <br>
- **Status tracks progression** — Use Status to mark quotations as Draft, Sent, Accepted, Rejected, etc. <br>
- **Keep detailed Terms** — Include payment terms, delivery timeframe, and any conditions in the Terms field <br>
- **Quotation differs from Invoice** — Quotations are proposals; they become invoices only after the client accepts <br>

______________________________________________________________________

## Related Pages

- **Quotation Detail** — View quotation details and client feedback
- **Edit Quotation** — Update terms and items before sending
- **Convert to Invoice** — Convert an accepted quotation into a standard invoice
- **Invoice Reports** — Track accepted quotations and revenue forecasts
