# Edit Material

## Overview

The **Edit Material** page allows you to update existing material information.
This includes general details, inventory settings, and status control.

______________________________________________________________________

## When to Use

Use this page when:

- Updating material name or description
- Correcting unit, cost, or stock values
- Adjusting reorder levels
- Enabling or disabling a material

______________________________________________________________________

## How to Edit a Material

1. Go to **Factory → Materials**
1. In the material list, click on the **SKU, Photo, or Name** of the material
1. The **Edit Material** page will open

![Edit Material](edit-material.png)

______________________________________________________________________

## General Information

### Editable Fields

| Field       | Description                              |
| ----------- | ---------------------------------------- |
| SKU         | Unique identifier (usually not editable) |
| Is Enabled  | Enable or disable the material           |
| Name        | Update the material name                 |
| Unit        | Change measurement unit                  |
| Photo       | Upload or replace material image         |
| Description | Update additional details                |

______________________________________________________________________

## Inventory Information

| Field         | Description                       |
| ------------- | --------------------------------- |
| Stock         | Update current available quantity |
| Cost          | Modify cost per unit              |
| Reorder Level | Adjust minimum stock threshold    |

______________________________________________________________________

## Important Notes

!!! warning
Changing **Unit** after transactions exist can cause inconsistency in inventory data.

!!! warning
Editing **Stock manually** may not reflect actual inventory movement history.

______________________________________________________________________

## Best Practices

- Avoid changing the **Unit** after the material is already in use
- Update **Stock** through inventory transactions when possible
- Use **Disable** instead of deleting materials that are no longer used

______________________________________________________________________

## Related Pages

- **Add Material** — Create new materials
- **Inventory In** — Increase stock properly
- **Inventory Out** — Decrease stock properly
