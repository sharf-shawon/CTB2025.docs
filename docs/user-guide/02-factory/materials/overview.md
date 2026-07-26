---
tags: [module:factory, task:view, role:staff]
---

# Material Overview

## Summary

Use the **Materials** section to manage all raw materials, track stock movement, and monitor inventory activity.

______________________________________________________________________

## When to use this page

- When you need to work with material overview in CTB Admin.

______________________________________________________________________

## How to access this page

From the sidebar, go to **Factory**, then open **Material Overview**.

______________________________________________________________________

## Step-by-step instructions

1. Open **Material Overview** from the **Factory** section of the sidebar.
1. Complete the **Table information** section described below.
1. Review the values you entered, then save the record.

______________________________________________________________________

## Field reference

### Table information

The table provides a real-time summary of your factory's resources:

| Column             | Description                                                                    |
| :----------------- | :----------------------------------------------------------------------------- |
| **SKU**            | Unique identifier (e.g., `MAT#0001`) and clickable link to the edit page.      |
| **Name**           | The descriptive name (e.g., "Blue Fabric") along with a thumbnail image.       |
| **Cost**           | The recorded cost per unit.                                                    |
| **Current Stock**  | Total quantity available. Items at **0** are highlighted in **red**.           |
| **Reorder Status** | Visual alerts such as **OUT OF STOCK** (red) or **OK** (green).                |
| **Last Movement**  | The timestamp of the most recent inventory transaction.                        |
| **Is Enabled**     | A green checkmark indicates if the material is currently active in the system. |

### Search

- Use the search bar to find materials by **name or SKU**

### Navigation to edit page

- Click on the **SKU, Photo, or Name**
- This opens the **Material Edit Page**

______________________________________________________________________

## Material list page

The **Material List** page displays all materials in a table format for quick access and management.
![Material List Page](material-list-page.png)

### Key features

- View all materials with essential details
- Quickly search and locate specific materials
- Access material edit page directly

______________________________________________________________________

## Material edit page tabs

The material edit page is divided into multiple tabs.
Each tab focuses on a different type of information.

______________________________________________________________________

## General tab

This tab contains the **basic material details**.

### Includes

- SKU
- Name
- Unit
- Photo
- Description
- Enable/Disable toggle

### Purpose

Used for managing identity and basic configuration of the material.

______________________________________________________________________

## Vouchers tab

This tab shows all **transactions related to the material**.

![Voucher-Tab](material-overview-voucher.png)

### Includes

- Linked vouchers where the material was used
- Transaction history records

### Purpose

Used to track where and how the material has been used in the system.

______________________________________________________________________

## Inventory in tab

This tab displays all **stock additions**.
![Inventory In Tab](material-overview-inventory-in.png)

### Includes

- Records of incoming stock
- Quantity added
- Date and reference

### Purpose

Used to monitor how stock is increasing over time.

______________________________________________________________________

## Inventory out tab

This tab displays all **stock deductions**.
![Inventory Out Tab](material-overview-inventory-out.png)

### Includes

- Records of used or removed stock
- Quantity deducted
- Date and reference

### Purpose

Used to track material usage and stock reduction.

______________________________________________________________________

## Material history button

This tab displays a **complete audit trail** of the material record.
![History Button](edit-material-history-button.png)

### Includes

- Chronological list of all actions (Created, Changed)
- Detailed log of value transitions (e.g., `Stock: 0 → 2000`)
- User identification and change reasons
- Option to revert to previous versions

______________________________________________________________________

## Best practices

- Use the **General tab** for updates, not inventory adjustments
- Always review **Inventory In/Out** before changing stock manually
- Use **Vouchers tab** to trace material usage issues

______________________________________________________________________

## Related pages

- **Add Material** — Create new material
- **Edit Material** — Update material details
- **Inventory In / Out** — Manage stock movement
