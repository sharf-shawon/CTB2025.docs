---
tags: [module:returns, task:view, role:staff]
---

# Product Repair

<!-- metadata: owner: operations_team, last_updated: 2026-08-16, git_ref: main, staging_verified: true -->

## Summary

Use this page to record products that are returned for repair and document the item status before the product is reworked or returned to stock. This keeps repair requests traceable and helps the team review who received the item, when it was logged, and what was returned.

______________________________________________________________________

## When to use this page

- When a client returns a damaged or faulty product for repair
- When you need to record who received the returned item and when it was received
- When you want to log the product, quantity, and repair notes for a repair request
- When a repair item must be tracked before it is repaired, reused, or returned to stock

______________________________________________________________________

## How to access this page

Go to **Return Management → Product Repair** in the sidebar. On the Product Repair list page, click the **purple (+) icon** or **Add** to open the repair form and create a new record.

______________________________________________________________________

## Prerequisites & Role Permissions

- **Permissions:** Access to create or edit product repair records in the Returns module.
- **Active Records:** A valid **Client** and at least one **Product** record must already exist.
- **Business Condition:** The returned product is physically received and is awaiting repair review or repair work.

______________________________________________________________________

## Step-by-step instructions

1. Open **Return Management → Product Repair** and click the **purple (+) icon**.
1. Select the **Status** for the repair request. Use `Received` when the item first arrives, then update it to `In Process`, `Completed`, or `Delivered` as the repair progresses.
1. Choose the **Client** and the **Received By** field.
1. Set the **Received Date** for the returned product.
1. In the **Product Repair Items** section, choose the **Product** that was returned.
1. Enter the **Quantity** of returned units.
1. Add notes in **Remarks** and enter the item **Weight** if required.
1. Click **Add another Product Repair Item** for multiple items in the same repair request.
1. Save the record to complete the repair entry.

______________________________________________________________________

## Verification & Definition of Done

- The product repair record is visible in the Product Repair list with the correct client and received date.
- The status reflects the current repair stage: `Received`, `In Process`, `Completed`, or `Delivered`.
- Each line shows the returned product, quantity, remarks, and weight.
- The record is ready for warehouse, quality, or operations follow-up.

______________________________________________________________________

## Field reference

![Product Repair](Add%20Product%20Repair-Page.png)

| Field | Required | What to do | Description |
| ----- | -------- | ---------- | ----------- |
| **Status** | Yes | Select status | Current repair stage (`Received`, `In Process`, `Completed`, `Delivered`) |
| **Client** | Yes | Choose client | Client who returned the product |
| **Received By** | Yes | Choose user or staff member | Person who received the returned product |
| **Received Date** | Yes | Select date | Date the product was received for repair |
| **Details** | No | Review section | Optional detail section for the product repair request |
| **Product** | Yes | Select product | Product returned for repair |
| **Quantity** | Yes | Enter quantity | Number of units returned |
| **Remarks** | No | Enter note | Repair notes or condition comments |
| **Weight** | Yes | Enter weight | Product weight for repair record tracking |

- **Remove** — Click to delete a product repair item row.
- **Add another Product Repair Item** — Add a new row when more than one product or unit needs recording.

______________________________________________________________________

## Exception Handling & Error Recovery

| Symptom / Error Message | Root Cause | Remediation Action |
| ---------------------- | ---------- | ------------------ |
| Repair record cannot be saved | Required field is missing | Fill in the missing **Client**, **Received Date**, or **Quantity** value |
| Wrong client is selected | The returned product belongs to a different client | Change the **Client** before saving |
| Item details are incomplete | Product information or remarks were not entered | Select the correct product and complete the quantity and weight |
| Record is not visible after save | The form was not submitted successfully | Reopen the record, correct validation errors, and click **Save** again |

______________________________________________________________________

## Related Workflows & Next Steps

- **[Product Returns](product-returns.md)** — Record returned finished goods for credit, refund, or replacement.
- **[Material Returns](material-returns.md)** — Track returned raw materials and vendor adjustments.
- **[Return Management Module](README.md)** — Overview of the full returns workflow in CTB Admin.
