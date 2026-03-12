# Add Client

Use this page to register a new client in CTB Admin. A client record stores the contact details, business information, and financial settings used across invoices, payments, and reports.

## When to use this page

- Onboarding a new buyer or business partner.
- Creating a client profile before issuing the first invoice.
- Registering a client's contact details, identification documents, and discount limits.

## How to access this page

From the sidebar, go to **Business → Clients**. On the Client List page, click the **purple (+) icon** in the top-right corner.

![Add Client Icon](add-icon.png)

The system opens the **Add Client** form, which is split into three sections: Personal Information, Business Details, and Balance & Discount Information.

---

## Personal Information

![Personal Information Section](edit-client-personal-info.png)

1. Enter the **Client Name**.
2. Use the **Is Enabled** switch to set the client's active status:
    - **2.1 ON** → The client is **active** and can be selected on new invoices.
    - **2.2 OFF** → The client is **inactive** (for example, a former client) and will not appear in invoice dropdowns.
3. Use the **Send SMS** switch to control invoice notifications:
    - **3.1 ON** → The client receives an SMS each time a new invoice is created.
    - **3.2 OFF** → No SMS notifications are sent to this client.
4. Enter the **Business Name** if the client operates under a business.
5. Enter the **Phone Number** (required for SMS notifications).
6. Enter an **Alternative Phone Number** if available.
7. Enter the **Email Address** (optional).

### Field Reference — Personal Information

| Field             | Description                                                                                                 |
| ----------------- | ----------------------------------------------------------------------------------------------------------- |
| SKU               | Automatically generated client ID. You cannot edit this field.                                              |
| Client Name       | Full name of the client. This name appears on invoices and reports.                                         |
| Is Enabled        | Determines whether the client is active. Inactive clients cannot be selected when creating new invoices.    |
| Send SMS          | When enabled, the client automatically receives an SMS notification when a new invoice is created for them. |
| Business Name     | Trade or business name of the client, if different from the personal name.                                  |
| Phone Number      | Primary contact number. Used for SMS notifications and general communication.                               |
| Alternative Phone | Secondary contact number (optional).                                                                        |
| Email             | Client email address (optional).                                                                            |

!!! warning "Required Fields"
    Fields marked with a **red star (*)** are mandatory and must be filled in before saving.

!!! tip "SMS Notification"
    Make sure the **Phone Number is correct** before enabling **Send SMS**. The phone number is used for all automated SMS messages.

---

## Business Details

![Business Details Section](edit-client-business-details.png)

1. Enter the **NID Number** of the client.
2. Upload the **NID Card Front Photo**:
    - **2.1** Click **Choose file to upload**.
    - **2.2** Select the image file from your computer.
3. Upload the **NID Card Back Photo** in the same way.
4. Upload a **Client Photo** if available.
5. Select the **Start Date** to record when the client relationship begins.
6. Select the **End Date** if there is a defined contract end date.
    - Leave this field empty if the relationship has no fixed end date.
7. Once all business details are filled, continue to the next section.

### Field Reference — Business Details

| Field                | Description                                                               |
| -------------------- | ------------------------------------------------------------------------- |
| NID Number           | National ID number of the client. Used for identity verification.         |
| NID Card Front Photo | Scanned or photographed image of the front side of the client's NID card. |
| NID Card Back Photo  | Scanned or photographed image of the back side of the client's NID card.  |
| Client Photo         | Profile photo of the client.                                              |
| Start Date           | The date the business relationship with this client officially began.     |
| End Date             | The date the client relationship ends. Leave blank for ongoing clients.   |

!!! note
    Upload clear, well-lit images of the NID card to ensure proper client identification in records and reports.

---

## Balance and Discount Information

![Balance and Discount Section](client-edit-balance-info.png)

### Balance

1. Enter the **Balance**.
   This is the current financial balance associated with the client account.
2. Enter the **Commission Balance**.
   This tracks commission-related transactions for the client.
3. Set the **Upper Balance Limit** to define the maximum balance allowed for this client.
4. Set the **Lower Balance Limit** to define the minimum allowed balance.

### Discount Information

5. View the **Discount Total**.
   This is a read-only field showing the total discount currently applied to this client.
6. Enter the **Discount Max Rate**.
   This is the maximum discount percentage that can be applied when creating invoices for this client.
7. Enter the **Discount Max Amount**.
   This is the maximum discount amount (in currency) that can be applied.

### Field Reference — Balance and Discount

| Field               | Description                                                                          |
| ------------------- | ------------------------------------------------------------------------------------ |
| Balance             | Current financial balance of the client account.                                     |
| Commission Balance  | Balance related to commission transactions for this client.                          |
| Upper Balance Limit | Maximum allowable balance for this client.                                           |
| Lower Balance Limit | Minimum allowable balance for this client.                                           |
| Discount Total      | Total discount currently applied to the client. This field is read-only.             |
| Discount Max Rate   | Maximum percentage discount allowed when creating invoices for this client.          |
| Discount Max Amount | Maximum discount amount (in currency) allowed per invoice for this client.           |

!!! warning "Required Fields"
    Fields marked with a **red star (*)** are mandatory and must be filled in before saving.

!!! note
    Set **Discount Max Rate** and **Discount Max Amount** carefully. These limits apply each time an invoice is created for this client, preventing over-discounting.

---

## Saving the Client

After completing all three sections, click **Save** to create the client record. The system redirects you to the **Client Detail** page for the newly created client.

## Tips and Common Issues

- If a required field is left empty, the form will display a red error message next to that field. Fill in all required fields before saving again.
- The **SKU** field is auto-generated and cannot be set manually.
- The **Discount Total** field is calculated automatically and cannot be edited directly.

## Related Pages

- **Edit Client** — Update an existing client's information.
- **Client Detail** — View the full profile, invoice history, and balances for a client.
- **Client Reports** — Analyze client data and financial summaries.
