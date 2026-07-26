---
tags: [module:factory, task:edit, role:staff]
---

# Edit Material

## Summary

Use the **Edit Material** page to update existing material information.
This includes general details, inventory settings, and status control.

______________________________________________________________________

## When to use this page

Use this page when:

- Updating material name or description
- Correcting unit, cost, or stock values
- Adjusting reorder levels
- Enabling or disabling a material

______________________________________________________________________

## How to access this page

From the sidebar, go to **Factory**, then open **Edit Material**.

______________________________________________________________________

## Step-by-step instructions

1. Open **Edit Material** from the **Factory** section of the sidebar.
1. Complete the **General information** section described below.
1. Complete the **Inventory information** section described below.
1. Complete the **History table details** section described below.
1. Complete the **Best practices** section described below.
1. Review the values you entered, then save the record.

______________________________________________________________________

## Field reference

### General information

![General Information](material-general-tab.png)

### Editable fields

| Field       | Description                              |
| ----------- | ---------------------------------------- |
| SKU         | Unique identifier (usually not editable) |
| Is Enabled  | Enable or disable the material           |
| Name        | Update the material name                 |
| Unit        | Change measurement unit                  |
| Photo       | Upload or replace material image         |
| Description | Update additional details                |

### Inventory information

| Field         | Description                       |
| ------------- | --------------------------------- |
| Stock         | Update current available quantity |
| Cost          | Modify cost per unit              |
| Reorder Level | Adjust minimum stock threshold    |

### History table details

The history table breaks down every modification with the following columns:

| Column            | Description                                                                 |
| :---------------- | :-------------------------------------------------------------------------- |
| **Object**        | The specific material ID and name being tracked.                            |
| **Date/time**     | The exact timestamp when the change occurred.                               |
| **Comment**       | The type of action performed (e.g., **Created**, **Changed**).              |
| **Changed by**    | The username of the person who performed the action (e.g., `tester`).       |
| **Change reason** | A note or justification provided by the user at the time of the change.     |
| **Changes**       | A detailed log of what specifically was modified (e.g., `Stock: 0 → 2000`). |

### Best practices

- **Review Before Reverting:** Always check the **Changes** column to understand exactly what will be modified before choosing to revert to an older version.
- **Provide Change Reasons:** When prompted by the system during an edit, provide a clear "Change reason" to help colleagues understand why a modification was made (e.g., "Monthly stock count correction").
- **Audit Regularly:** Use this page to investigate discrepancies between physical stock and system records.

______________________________________________________________________

## How to edit a Material

1. Go to **Factory → Materials**
1. In the material list, click on the **SKU, Photo, or Name** of the material
1. The **Edit Material** page will open

![Edit Material](edit-material.png)

______________________________________________________________________

## Best practices

- Avoid changing the **Unit** after the material is already in use
- Update **Stock** through inventory transactions when possible
- Use **Disable** instead of deleting materials that are no longer used

______________________________________________________________________

## Material history page

![History Button](edit-material-history-button.png)

The **Material History** page provides a comprehensive audit trail for a specific material. It allows administrators to track changes, identify who made modifications, and revert to previous versions if necessary.

______________________________________________________________________

## Overview

![History Page](material-history-page.png)

This page displays a chronological list of all actions performed on a material object (e.g., `MAT#0001 - runner`).

> **Tip:** Choose a date from the list to revert to a previous version of this object.

______________________________________________________________________

## Key functionalities

### 1. Tracking stock movements

The **Changes** column explicitly shows value transitions. For example, you can see exactly when stock was initialized or adjusted, moving from an old value to a new one.

### 2. Version control (revert)

By clicking on a specific entry, you can view the state of the material at that exact moment. This is essential for correcting accidental data entry or unauthorized changes.

### 3. Audit accountability

The **Changed by** column ensures that every update is tied to a specific user account, providing transparency for inventory management.

______________________________________________________________________

## Important notes

!!! warning

    Changing **Unit** after transactions exist can cause inconsistency in inventory data.

!!! warning

    Editing **Stock manually** may not reflect actual inventory movement history.

______________________________________________________________________

## Related pages

- **Add Material** — Create new materials
- **Inventory In** — Increase stock properly
- **Inventory Out** — Decrease stock properly
