---
tags: [module:business, task:edit, role:staff]
---

# Edit Client

Use this page to update an existing client's information in CTB Admin. This includes contact details, identification documents, and financial settings.

## Summary

Use this page to keep existing client records accurate after profile, document, or balance changes. Updates made here immediately affect future transactions and reporting.

______________________________________________________________________

## When to use this page

- Updating client contact or business information
- Changing client status (active/inactive)
- Modifying balance limits or financial data
- Updating identification documents or photos

______________________________________________________________________

## How to access this page

1. Go to **Business → Clients** from the sidebar
1. On the Client List page, select a client
1. Click on the **Photo** or **SKU** or **Client Name**

The system opens the **Edit Client Page**.

______________________________________________________________________

## Step-by-step instructions

1. Open **Business → Clients** from the sidebar.
1. Select the client by **Photo**, **SKU**, or **Client Name**.
1. Update the required fields across personal, business, and balance sections.
1. Review financial changes carefully before saving.
1. Click **Save** to apply the updates.

______________________________________________________________________

## Field reference

- **Client Name** - Display name used across CTB Admin.
- **Is Enabled** - Controls whether the client can be used in new transactions.
- **Phone Number** - Main contact number, especially important when SMS is enabled.
- **NID fields** - Identity information and document images for verification.
- **Balance and limits** - Financial controls that affect statements and validation rules.

______________________________________________________________________

## What's different from add Client

- All fields are **pre-filled** with existing client data
- You are **modifying**, not creating a new record
- Some fields may already contain system-generated or historical values
- Changes will immediately affect future transactions

______________________________________________________________________

## Personal information

![Personal Information Section](client-edit-personal-info.png)

Update the following fields as needed:

| Field             | What you can change | Notes                                        |
| ----------------- | ------------------- | -------------------------------------------- |
| Client Name       | Edit                | Updates how the client appears in the system |
| Is Enabled        | Toggle ON/OFF       | Disabling prevents usage in new transactions |
| Send SMS          | Enable/Disable      | Controls notification behavior               |
| Business Name     | Edit                | Optional                                     |
| Phone Number      | Edit                | Must be valid if SMS is enabled              |
| Alternative Phone | Edit                | Optional                                     |
| Email             | Edit                | Optional                                     |

______________________________________________________________________

## Business details

![Business Details Section](client-edit-business-details.png)

| Field           | What you can change | Notes                                    |
| --------------- | ------------------- | ---------------------------------------- |
| NID Number      | Edit                | Ensure accuracy for verification         |
| NID Front Photo | Replace             | Upload a new image if needed             |
| NID Back Photo  | Replace             | Upload updated image                     |
| Start Date      | Edit                | Should reflect actual relationship start |
| End Date        | Set/Update          | Leave empty if ongoing                   |

!!! note

    Replacing images will overwrite previous uploads.

______________________________________________________________________

## Balance and discount information

![Balance and Discount Section](client-balance-discount.png)

| Field               | What you can change | Notes                                  |
| ------------------- | ------------------- | -------------------------------------- |
| Balance             | Adjust if required  | Be careful — affects financial records |
| Commission Balance  | Adjust if required  | Be careful — affects financial records |
| Upper Balance Limit | Modify              | Controls maximum allowed balance       |
| Lower Balance Limit | Modify              | Controls minimum allowed balance       |
| Discount Max Rate   | Modify              | Controls maximum discount rate         |
| Discount Max Amount | Modify              | Controls maximum discount amount       |

!!! warning

    Changing balance-related fields can impact financial tracking and reports.

______________________________________________________________________

## Saving changes

After updating the required fields:

- Click **Save** to apply changes
- Changes are immediately reflected across the system

______________________________________________________________________

## Tips and common issues

- The **SKU** field cannot be changed after a client is created.
- Disabling a client prevents it from being used in future transactions
- Ensure **Phone number is correct** before enabling SMS
- Avoid unnecessary changes to **Balance**, as it affects reports
- Always verify **NID information** before saving

______________________________________________________________________

## Related pages

- **Add Client** — Create a new client
- **Client Detail** — View client profile and history
- **Client Reports** — Analyze client financial data
