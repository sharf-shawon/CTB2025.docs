# Check Detail

Use this page to view and manage a check after it has been created or received. The check detail page displays all information related to a check—general details, financial information, status, and supporting documents. You can update check status, add front and back photos, and track payment records linked to this check.

## Summary

Use this page to review check records, verify linked payments, and update allowed status fields. It supports reconciliation and audit review for incoming or issued checks.

## When to use this page

- Viewing a complete check record with all details and payment information
- Updating check status (Pending, Cleared, Bounced, etc.)
- Adding front and back photos of the check for verification
- Reviewing linked payments and transactions
- Verifying check information for bank reconciliation

## How to access Check Detail

From the sidebar, go to **Trade Management → Checks**. On the Checks List page, click on any check SKU or select a check to open the **Check Detail page**.

## Step-by-step instructions

1. Open **Trade -> Checks** and select the check record.
1. Review the check information and client information sections.
1. Update the status if the bank has cleared, bounced, or cancelled the check.
1. Add or verify front and back photos.
1. Review linked payments before saving changes.

## Field reference

- **SKU** - Unique system identifier for the check.
- **Check Number** - Number printed on the physical check.
- **Bank** - Bank account associated with the check.
- **Amount** - Face value recorded when the check was created.
- **Balance** - Remaining amount available after linked payments.
- **Status** - Current lifecycle state of the check.
- **Client** - Client or vendor linked to the check.

______________________________________________________________________

## Check Information

![Check Information Section](check-info.png)

The Check Information section displays core check details:

| Field        | Description                                    |
| ------------ | ---------------------------------------------- |
| SKU          | Unique system identifier for this check        |
| Check Number | Bank check number (printed on the check)       |
| Bank         | Associated bank account (linked to check)      |
| Date         | Date the check was written in the check page   |
| Amount       | Monetary value of the check                    |
| Balance      | Current balance (may reflect partial payments) |
| Type         | Check type (Receive, Send etc.)                |

!!! info "Read-Only Fields"
SKU, Check Number, Bank, Date, and Amount are typically set at check creation and cannot be changed on this detail page. To modify these, you must edit the check or create a new record.

______________________________________________________________________

## Client Information

| Field  | Description                           |
| ------ | ------------------------------------- |
| Client | Client or vendor linked to this check |

The Client field shows who the check is issued to or received from. Click the client name to view their profile.

______________________________________________________________________

## Status Information

![Status Section](check-details-status-info.png)

| Field  | Description                                                       |
| ------ | ----------------------------------------------------------------- |
| Status | Current check status (Pending, Cleared, Bounced, Cancelled, etc.) |

Update the **Status** dropdown to track the check through its lifecycle:

- **Pending** — Check has been recorded but not yet processed by the bank
- **passed** — Bank has processed and cleared the check
- **Bounced** — Check was rejected by the bank (insufficient funds, etc.)

!!! warning "Status Changes"
Changing a check status may trigger notifications or affect linked payments. Review implications before updating.

______________________________________________________________________

## Photos

The page includes two photo upload sections:

| Section     | Purpose                                                         |
| ----------- | --------------------------------------------------------------- |
| Front Photo | Clear photo of the front side of the check                      |
| Back Photo  | Clear photo of the back side of the check (if any endorsements) |

**To upload a photo:**

1. Click **Choose file to upload** in the Front Photo or Back Photo section
1. Select an image from your computer (JPG, PNG, or PDF formats recommended)
1. The system displays "Check front photo or scan copy here" as placeholder text
1. After upload, the image preview appears below

!!! tip "Photo Guidelines"

- Capture check details clearly and in full
- Ensure adequate lighting and no glare
- Back photo is optional but recommended for auditing purposes
- Store high-resolution images for bank verification

______________________________________________________________________

## Check Dates Section

| Field             | Description                                        |
| ----------------- | -------------------------------------------------- |
| Check Sheet Date  | The date written on the physical check page        |
| Check Passed Date | Date the check was cleared and passed by the bank  |
| Check Bounce Date | Date the check was rejected or bounced by the bank |

These dates help track check timing for bank reconciliation:

- **Check Sheet Date** is the date printed or written on the physical check itself
- **Check Passed Date** is filled when the check status changes to **Passed** (bank cleared the check)
- **Check Bounce Date** is filled when the check status changes to **Bounced** (bank rejected the check)

______________________________________________________________________

## Payments Tab

The **Payments** section at the bottom tracks all payments or transactions linked to this check:

| Column    | Description                   |
| --------- | ----------------------------- |
| Reference | Payment or invoice reference  |
| Amount    | Payment amount                |
| Discount  | Discount applied (if any)     |
| Status    | Payment status                |
| Date      | Date of the payment           |
| From/To   | Payment source or destination |

!!! info "Linked Payments"
A single check may be linked to multiple payments. Use this section to verify which transactions are tied to this check.

______________________________________________________________________

## Step-by-step: Updating a Check

1. Open the **Checks list** and click on a check SKU
1. Review the **Check Information** section for details
1. Update the **Status** dropdown if the check status has changed
1. Click **Choose file to upload** to add a Front Photo of the check
1. (Optional) Add a Back Photo for additional verification
1. Enter or verify **Check Sheet Date** and **Check Source Date**
1. Review linked payments in the **Payments** section
1. Scroll to the top and click **Save** to apply your changes

!!! warning "Save Changes"
After making edits, you must click **Save** at the bottom-right to apply your changes. Unsaved changes will be lost.

______________________________________________________________________

!!! warning "Deleting a Check"

```
You can delete a c  check, but only under specific conditions based on its status and payment state:

### When you **can delete a check**:
- **Status is Pending** — If the check is in Pending status and has no linked payments, you can delete it
### When you **cannot delete a check**:
- **Check has partial payment** — If any payment is linked to this check (even if incomplete), the check cannot be deleted
- **Status is Bounced** — Bounced checks are locked and cannot be deleted (they must be kept for audit and reconciliation records)
- **Status is Passed** — Passed (cleared) checks cannot be deleted (they must be retained as confirmed transactions)
- **Status is Failed** — Failed checks cannot be deleted (they must be kept for bank reconciliation)
warning "Deletion Rules"
Once a check status changes from Pending, or if any payment is linked to it, the delete option becomes unavailable. Plan carefully before initializing payments against a check.
**To delete a check:**
1. Open the check detail page
2. Verify the status is **Pending** and there are **no linked payments**
3. Click the **Delete Check** button (appears only if conditions are met)
4. Confirm the deletion when prompted
info "Cannot Delete?"
If the Delete button is not visible, check:
- Is the status **Pending**?
- Are there **any linked payments** in the Payments tab?
- If either condition fails, the check cannot be deleted. You can archive it or contact support instead.
```

______________________________________________________________________

## Tips and common issues

- **Check details locked?** — SKU, Check Number, Bank, Date, and Amount are set at creation. If you need to modify these, change the status to Pending and click save to continue editing.
- **Photos not uploading?** — Verify the file format (JPG, PNG, or PDF) and size. Large files may fail; re-export at lower resolution if needed.
- **Payment not showing in Payments tab?** — The payment may not be linked to this check. Review payment creation to ensure the check reference was selected.
- **Cannot delete check?** — Once a check is cleared or used in a transaction, it may be locked from deletion. Archive or cancel it instead.

______________________________________________________________________

## Related pages

- [Checks Overview](overview.md) — List and manage all checks
- [Add Check](add-check.md) — Create a new check record
- [Payments](../payments/overview.md) — View and manage payments linked to checks
- [Banks](../banks/overview.md) — Manage bank accounts
