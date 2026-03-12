# Edit Client


The **Edit Client Page** allows you to create or update client information.
Fill in the necessary details and configure the client settings before saving.

---

## Steps to Add a Client
# Personal Infromation Section
this section allows the user to store  a client's personal information

![Personal Infromation Section](edit-client-personal-info.png)

1. Open the **Client Detail Page** from the **Client List Page**.

2. Enter the **Client Name**.

3. Use the **Is Enabled** switch to control the client status.

   - **ON** → The client is **active**.
   - **OFF** → The client is **inactive or an old client**.

4. Use the **Send SMS** switch to control invoice notifications.

   - **ON** → The client will **receive an SMS** after an invoice is created.
   - **OFF** → The client **will not receive SMS notifications**.

5. Enter the **Business Name** if the client has a business.

6. Enter the **Phone Number**.

7. Enter an **Alternative Phone Number** if available.

8. Enter the **Email Address** (optional).

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

---

!!! warning "Required Fields"
    Fields marked with a **red star (*)** are **mandatory** and must be filled in before saving.

!!! tip "SMS Notification"
    If **Send SMS** is enabled, the client will automatically receive an SMS when a new invoice is created.

!!! note
    Make sure the **phone number is correct**, as it is used for SMS notifications and communication.



# Business Details Section

The **Business Details** section allows you to store additional identification and contract information for the client.

![Business Details Section](edit-client-business-details.png)

---

### Steps to Fill Business Details

1. Enter the **NID Number** of the client.

2. Upload the **NID Card Front Photo** by clicking **Choose file to upload** and selecting the image from your computer.

3. Upload the **NID Card Back Photo** in the same way.

4. Upload a **Client Photo** if available.

5. Select the **Start Date** to define when the client relationship begins.

6. Select the **End Date** if the client has a defined contract period.

7. After completing the information, continue filling the remaining client details and **save the client profile**.

---

### Field Explanation

| Field                | Description                                                     |
| -------------------- | --------------------------------------------------------------- |
| NID Number           | National ID number of the client.                               |
| NID Card Front Photo | Image of the front side of the client's NID card.               |
| NID Card Back Photo  | Image of the back side of the client's NID card.                |
| Client Photo         | Profile photo of the client.                                    |
| Start Date           | The starting date of the business relationship with the client. |
| End Date             | The end date of the client relationship (if applicable).        |

---

!!! note
    Upload clear images of the **NID card** to ensure proper identification of the client.

!!! tip
    You can leave the **End Date** empty if the client relationship does not have a fixed end date.


## Balance & Discount Information

This section is used to configure the **client's financial limits, balances, and discount settings**.

![Balance and Discount Section](client-edit-balance-info.png)

---

### Steps to Configure Balance

1. Enter the **Balance** of the client.
   This represents the current financial balance associated with the client.

2. Enter the **Commission Balance**.
   This value represents the commission-related balance for the client.

3. Set the **Upper Balance Limit** if there is a maximum balance limit for the client.

4. Set the **Lower Balance Limit** to define the minimum allowed balance.

---

### Discount Information

The **Discount Information** section allows you to control the maximum discount that can be applied to this client.

1. View the **Discount Total**.
   This shows the total discount currently associated with the client.

2. Enter the **Discount Max Rate**.
   This defines the maximum discount percentage allowed for this client.

3. Enter the **Discount Max Amount**.
   This defines the maximum discount amount that can be applied.

---

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

---

!!! warning "Required Fields"
    Fields marked with a **red star (*)** are mandatory and must be filled before saving the client information.

!!! note
    Configure the **discount limits carefully** to ensure proper pricing control when creating invoices.


 After filling in the required information, **save the client details**.

---


