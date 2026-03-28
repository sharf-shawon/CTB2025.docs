# Add Client

Use this page to register a new client in CTB Admin. A client record stores the contact details, business information, and financial settings used across invoices, payments, and reports.

## When to use this page

- Onboarding a new buyer or business partner.
- Creating a client profile before issuing the client's first invoice.
- Registering a client's contact details, identification documents, and discount limits.

## How to access this page

From the sidebar, go to **Business → Clients**. On the **Client List** page, click the **purple (+) icon** in the top-right corner.

![Add Client Icon](add-icon.png)

The system opens the **Add Client** form, which is split into three sections: **Personal Information**, **Business Details**, and **Balance & Discount Information**.

______________________________________________________________________

## Personal Information

![Personal Information Section](edit-client-personal-info.png)

1. Enter the **Client Name**.

1. Use the **Is Enabled** switch to set the client's active status.

   - **2.1 ON** → The client is **active** and can be selected when creating new invoices.
   - **2.2 OFF** → The client is **inactive** (for example, a former client) and will not appear in invoice dropdowns.

1. Use the **Send SMS** switch to control invoice notifications.

   - **3.1 ON** → The client receives an SMS each time a new invoice is created.
   - **3.2 OFF** → No SMS notifications are sent to this client.

1. Enter the **Business Name** if the client operates under a business.

1. Enter the **Phone Number**.

1. Enter an **Alternative Phone Number** if available.

1. Enter the **Email Address** (optional).

### Field Reference — Personal Information

| Field             | Description                                                                                              |
| ----------------- | -------------------------------------------------------------------------------------------------------- |
| SKU               | Automatically generated client ID. You cannot edit this field.                                           |
| Client Name       | Full name of the client. This name appears on invoices and reports.                                      |
| Is Enabled        | Determines whether the client is active. Inactive clients cannot be selected when creating new invoices. |
| Send SMS          | When enabled, the client automatically receives an SMS notification when a new invoice is created.       |
| Business Name     | Trade or business name of the client, if different from the personal name.                               |
| Phone Number      | Primary contact number used for SMS notifications and communication.                                     |
| Alternative Phone | Secondary contact number (optional).                                                                     |
| Email             | Client email address (optional).                                                                         |

!!! warning "Required Fields"
Fields marked with a **red star (\*)** are mandatory and must be filled in before saving.

!!! tip "SMS Notification"
Make sure the **Phone Number** is correct before enabling **Send SMS**, as this number will receive automated SMS notifications.

______________________________________________________________________

## Business Details

![Business Details Section](edit-client-business-details.png)

1. Enter the **NID Number** of the client.

1. Upload the **NID Card Front Photo**.

   - Click **Choose file to upload**.
   - Select the image file from your computer.

1. Upload the **NID Card Back Photo** in the same way.

1. Upload a **Client Photo** if available.

1. Select the **Start Date** to record when the client relationship begins.

1. Select the **End Date** if there is a defined contract end date.

   - Leave this field empty if the relationship has no fixed end date.

1. Once all business details are filled, continue to the next section.

### Field Reference — Business Details

| Field                | Description                                                             |
| -------------------- | ----------------------------------------------------------------------- |
| NID Number           | National ID number of the client used for identity verification.        |
| NID Card Front Photo | Image of the front side of the client's NID card.                       |
| NID Card Back Photo  | Image of the back side of the client's NID card.                        |
| Client Photo         | Profile photo of the client.                                            |
| Start Date           | The date the business relationship with this client began.              |
| End Date             | The date the client relationship ends. Leave blank for ongoing clients. |

!!! note
Upload clear and readable images of the **NID card** to ensure proper identification in records.

______________________________________________________________________

## Balance and Discount Information

![Balance and Discount Section](client-edit-balance-info.png)

### Balance

1. Enter the **Balance**.
   This is the current financial balance associated with the client account.

1. Enter the **Commission Balance**.
   This tracks commission-related transactions for the client.

1. Set the **Upper Balance Limit** to define the maximum balance allowed for this client.

1. Set the **Lower Balance Limit** to define the minimum allowed balance.

### Discount Information

1. View the **Discount Total**.
   This is a read-only field showing the total discount currently applied to the client.

1. Enter the **Discount Max Rate**.
   This is the maximum discount percentage allowed when creating invoices for this client.

1. Enter the **Discount Max Amount**.
   This is the maximum discount amount that can be applied per invoice.

### Field Reference — Balance and Discount

| Field               | Description                                                                 |
| ------------------- | --------------------------------------------------------------------------- |
| Balance             | Current financial balance of the client account.                            |
| Commission Balance  | Balance related to commission transactions for the client.                  |
| Upper Balance Limit | Maximum allowable balance for this client.                                  |
| Lower Balance Limit | Minimum allowable balance for this client.                                  |
| Discount Total      | Total discount currently applied to the client. This field is read-only.    |
| Discount Max Rate   | Maximum percentage discount allowed when creating invoices for this client. |
| Discount Max Amount | Maximum discount amount allowed per invoice.                                |

!!! warning "Required Fields"
Fields marked with a **red star (\*)** are mandatory and must be filled before saving.

!!! note
Configure **Discount Max Rate** and **Discount Max Amount** carefully. These limits prevent excessive discounts when creating invoices.

______________________________________________________________________

## Saving the Client

After completing all sections, click **Save** to create the client record.
The system will redirect you to the **Client Detail** page for the newly created client.

______________________________________________________________________

## Tips and Common Issues

- If a required field is left empty, the form will display a red error message next to that field.
- The **SKU** field is automatically generated and cannot be edited.
- The **Discount Total** field is calculated automatically and cannot be modified manually.

______________________________________________________________________

## Related Pages

- **Edit Client** — Update an existing client's information.
- **Client Detail** — View the complete client profile, invoice history, and balances.
- **Client Reports** — Analyze client data and financial summaries.
