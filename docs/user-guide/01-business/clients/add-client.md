# Add Client

Use this page to register a new client in CTB Admin. A client record stores the contact details, business information, and financial settings used across invoices, payments, and reports.

## When to use this page

- Onboarding a new buyer or business partner.
- Creating a client profile before issuing the first invoice.
- Registering a client's contact details, identification documents, and discount limits.


1. Look at the **top-right corner** of the page.

2. Click the **purple (+) icon** to add a new client.
   \=======

## How to access this page

From the sidebar, go to **Business → Clients**. On the Client List page, click the **purple (+) icon** in the top-right corner.

> > > > > > > 562ba5bd032c0ffcfa2f03f0a69f3a08a5d7018f

![Add Client Icon](add-icon.png)




1. The system will open the **Client Detail Page**.

# Edit Client

The **Edit Client Page** allows you to create or update client information.
Fill in the necessary details and configure the client settings before saving.

______________________________________________________________________

## Steps to Add a Client

## Personal Infromation Section

this section allows the user to store a client's personal information

![Personal Infromation Section](edit-client-personal-info.png)

1. Open the **Client Detail Page** from the **Client List Page**.

1. Enter the **Client Name**.

1. Use the **Is Enabled** switch to control the client status.

   - **ON** → The client is **active**.
   - **OFF** → The client is **inactive or an old client**.

1. Use the **Send SMS** switch to control invoice notifications.

   - **ON** → The client will **receive an SMS** after an invoice is created.
   - **OFF** → The client **will not receive SMS notifications**.

1. Enter the **Business Name** if the client has a business.

1. Enter the **Phone Number**.

1. Enter an **Alternative Phone Number** if available.

1. Enter the **Email Address** (optional).

## Field Explanation

| Field             | Description                                                     |
| ----------------- | --------------------------------------------------------------- |
| SKU               | Automatically generated client ID.                              |
| Client Name       | Name of the client.                                             |
| Is Enabled        | Controls whether the client is active or inactive.              |
| Send SMS          | Controls whether the client receives invoice SMS notifications. |
| Business Name     | Name of the client's business.                                  |
| Phone Number      | Primary contact number of the client.                           |
| Alternative Phone | Secondary contact number (optional).                            |
| Email             | Client email address (optional).                                |

______________________________________________________________________

!!! warning "Required Fields"
Fields marked with a **red star (\*)** are **mandatory** and must be filled in before saving.

!!! tip "SMS Notification"
If **Send SMS** is enabled, the client will automatically receive an SMS when a new invoice is created.

!!! note
Make sure the **phone number is correct**, as it is used for SMS notifications and communication.

# Business Details Section

The **Business Details** section allows you to store additional identification and contract information for the client.

![Business Details Section](edit-client-business-details.png)

______________________________________________________________________

### Steps to Fill Business Details

1. Enter the **NID Number** of the client.

1. Upload the **NID Card Front Photo** by clicking **Choose file to upload** and selecting the image from your computer.

1. Upload the **NID Card Back Photo** in the same way.

1. Upload a **Client Photo** if available.

1. Select the **Start Date** to define when the client relationship begins.

1. Select the **End Date** if the client has a defined contract period.

1. After completing the information, continue filling the remaining client details and **save the client profile**.

______________________________________________________________________

### Field Explanation

| Field                | Description                                                     |
| -------------------- | --------------------------------------------------------------- |
| NID Number           | National ID number of the client.                               |
| NID Card Front Photo | Image of the front side of the client's NID card.               |
| NID Card Back Photo  | Image of the back side of the client's NID card.                |
| Client Photo         | Profile photo of the client.                                    |
| Start Date           | The starting date of the business relationship with the client. |
| End Date             | The end date of the client relationship (if applicable).        |

______________________________________________________________________

!!! note
Upload clear images of the **NID card** to ensure proper identification of the client.

!!! tip
You can leave the **End Date** empty if the client relationship does not have a fixed end date.

## Balance & Discount Information

This section is used to configure the **client's financial limits, balances, and discount settings**.

![Balance and Discount Section](client-edit-balance-info.png)

______________________________________________________________________

### Steps to Configure Balance

1. Enter the **Balance** of the client.
   This represents the current financial balance associated with the client.

1. Enter the **Commission Balance**.
   This value represents the commission-related balance for the client.

1. Set the **Upper Balance Limit** if there is a maximum balance limit for the client.

1. Set the **Lower Balance Limit** to define the minimum allowed balance.

______________________________________________________________________

### Discount Information

The **Discount Information** section allows you to control the maximum discount that can be applied to this client.

1. View the **Discount Total**.
   This shows the total discount currently associated with the client.

1. Enter the **Discount Max Rate**.
   This defines the maximum discount percentage allowed for this client.

1. Enter the **Discount Max Amount**.
   This defines the maximum discount amount that can be applied.

______________________________________________________________________

### Field Explanation

| Field               | Description                                         |
| ------------------- | --------------------------------------------------- |
| Balance             | Current financial balance of the client.            |
| Commission Balance  | Balance related to commission transactions.         |
| Upper Balance Limit | Maximum balance limit allowed for the client.       |
| Lower Balance Limit | Minimum balance limit allowed for the client.       |
| Discount Total      | Total discount amount currently applied.            |
| Discount Max Rate   | Maximum discount percentage allowed for the client. |
| Discount Max Amount | Maximum discount amount allowed for the client.     |

______________________________________________________________________

!!! warning "Required Fields"
Fields marked with a **red star (\*)** are mandatory and must be filled before saving the client information.

!!! note
Configure the **discount limits carefully** to ensure proper pricing control when creating invoices.

After filling in the required information, **save the client details**.

______________________________________________________________________

\=======
The system opens the **Add Client** form, which is split into three sections: Personal Information, Business Details, and Balance & Discount Information.

______________________________________________________________________

## Personal Information

![Personal Information Section](edit-client-personal-info.png)

1. Enter the **Client Name**.
1. Use the **Is Enabled** switch to set the client's active status:
   - **2.1 ON** → The client is **active** and can be selected on new invoices.
   - **2.2 OFF** → The client is **inactive** (for example, a former client) and will not appear in invoice dropdowns.
1. Use the **Send SMS** switch to control invoice notifications:
   - **3.1 ON** → The client receives an SMS each time a new invoice is created.
   - **3.2 OFF** → No SMS notifications are sent to this client.
1. Enter the **Business Name** if the client operates under a business.
1. Enter the **Phone Number** (required for SMS notifications).
1. Enter an **Alternative Phone Number** if available.
1. Enter the **Email Address** (optional).

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
Fields marked with a **red star (\*)** are mandatory and must be filled in before saving.

!!! tip "SMS Notification"
Make sure the **Phone Number is correct** before enabling **Send SMS**. The phone number is used for all automated SMS messages.

______________________________________________________________________

## Business Details

![Business Details Section](edit-client-business-details.png)

1. Enter the **NID Number** of the client.
1. Upload the **NID Card Front Photo**:
   - **2.1** Click **Choose file to upload**.
   - **2.2** Select the image file from your computer.
1. Upload the **NID Card Back Photo** in the same way.
1. Upload a **Client Photo** if available.
1. Select the **Start Date** to record when the client relationship begins.
1. Select the **End Date** if there is a defined contract end date.
   - Leave this field empty if the relationship has no fixed end date.
1. Once all business details are filled, continue to the next section.

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

5. View the **Discount Total**.
   This is a read-only field showing the total discount currently applied to this client.
1. Enter the **Discount Max Rate**.
   This is the maximum discount percentage that can be applied when creating invoices for this client.
1. Enter the **Discount Max Amount**.
   This is the maximum discount amount (in currency) that can be applied.

### Field Reference — Balance and Discount

| Field               | Description                                                                 |
| ------------------- | --------------------------------------------------------------------------- |
| Balance             | Current financial balance of the client account.                            |
| Commission Balance  | Balance related to commission transactions for this client.                 |
| Upper Balance Limit | Maximum allowable balance for this client.                                  |
| Lower Balance Limit | Minimum allowable balance for this client.                                  |
| Discount Total      | Total discount currently applied to the client. This field is read-only.    |
| Discount Max Rate   | Maximum percentage discount allowed when creating invoices for this client. |
| Discount Max Amount | Maximum discount amount (in currency) allowed per invoice for this client.  |

!!! warning "Required Fields"
Fields marked with a **red star (\*)** are mandatory and must be filled in before saving.

!!! note
Set **Discount Max Rate** and **Discount Max Amount** carefully. These limits apply each time an invoice is created for this client, preventing over-discounting.

______________________________________________________________________

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

> > > > > > > 562ba5bd032c0ffcfa2f03f0a69f3a08a5d7018f
