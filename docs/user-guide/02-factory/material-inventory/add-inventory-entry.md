---
tags: [module:factory, task:create, role:staff]
---

# Add Inventory

## Summary

The **Add Inventory** page is used to record stock movement for materials.
You can add stock, remove stock, or transfer stock using this page.

______________________________________________________________________

## When to use this page

Use this page when:

- Adding new stock to inventory
- Recording material usage or consumption
- Managing stock transfers

______________________________________________________________________

## How to access this page

From the sidebar, go to **Factory**, then open **Add Inventory**.

______________________________________________________________________

## Step-by-step instructions

1. Open **Add Inventory** from the **Factory** section of the sidebar.
1. Complete the **Basic information** section described below.
1. Complete the **Type behavior (important)** section described below.
1. Complete the **Transaction details** section described below.
1. Complete the **System fields** section described below.
1. Review the values you entered, then save the record.

______________________________________________________________________

## Field reference

### Basic information

![Add Inventory](add-inventory.png)

| Field | Description                                      |
| ----- | ------------------------------------------------ |
| SKU   | Auto-generated inventory reference               |
| Date  | Date of the transaction                          |
| Type  | Defines the inventory action (In, Out, Transfer) |

### Type behavior (important)

The form changes based on the selected **Type**:

### In (stock increase)

- **Vendor field appears**
- Used when purchasing or receiving materials

### Out (stock decrease)

- **Employee field appears**
- Used when materials are issued or consumed

### Transfer

- **Both Vendor and Employee fields are hidden**
- Used for internal stock movement

!!! warning

    Selecting the wrong type will result in incorrect inventory records.

### Transaction details

| Field    | Description                          |
| -------- | ------------------------------------ |
| Material | Select the material                  |
| Quantity | Amount of stock to add/remove        |
| Cost     | Cost per unit (mainly used for "In") |

### System fields

| Field      | Description      |
| ---------- | ---------------- |
| Notes      | Optional remarks |
| Created By | System-generated |
| Updated By | System-generated |
| Created At | Auto timestamp   |
| Updated At | Auto timestamp   |

______________________________________________________________________

## How to add Inventory

1. Go to **Factory → Material Inventory**
1. Click the **+ (Add)** button

______________________________________________________________________

## Best practices

- Always select the correct **Type** before entering data
- Use accurate **Quantity** to maintain stock integrity
- Add **Notes** for traceability

______________________________________________________________________

## Related pages

- **Materials** — Manage material details
- **Inventory In / Out Tabs** — View stock history
