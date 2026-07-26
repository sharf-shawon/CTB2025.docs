---
tags: [module:factory, task:create, role:staff]
---

# Add Product

<!-- metadata: owner: factory_team, last_updated: 2026-07-26, git_ref: main, staging_verified: true -->

## Summary

Use this page to define new finished products, unit selling rates, production wage allocations, and raw material bill-of-materials (BOM) costings in CTB Admin. Registering products enables stock management, inventory tracking, sales invoicing, and production costing.

______________________________________________________________________

## When to use this page

- Adding a new garment, bag, or fashion item to the manufacturing catalog
- Defining unit selling rates, production wages, and minimum restock alert levels
- Assigning raw material recipes (Product Costings) for unit cost calculation
- Configuring public vs. internal catalog visibility flags

______________________________________________________________________

## How to access this page

From the sidebar, go to **Factory → Products** (`/en/admin/Factory/product/`). On the Products List page, click the **purple (+) icon** in the top-right corner.

______________________________________________________________________

## Prerequisites

- **Product Category**: Target category must exist under **Factory → Categories**.
- **Material Catalog**: Raw materials required for product recipes must exist in **Factory → Materials**.
- **Required User Permissions**:
    - `Factory | Product | Can add Product` (`factory.add_product`)
    - `Factory | Product | Can change Product` (`factory.change_product`)

______________________________________________________________________

## Step-by-step instructions

1. Open **Factory → Products** and click **(+) Add Product**.
1. Input the product **Name** and select its **Category**.
1. Select the measurement **Unit** (e.g. `Pieces`, `Dozens`, `Meters`).
1. Enter the unit **Selling Rate** and **Production Wage** per unit.
1. Set initial **Stock** quantity and minimum **Restock Level** threshold.
1. Switch to the **Product Costings** tab to add raw material recipes.
1. Select a **Material**, enter required **Quantity**, and unit **Cost**.
1. Click **Add another Product Costing** for additional material components.
1. Toggle **Is Enabled** to activate the product for invoicing and stock tracking.
1. Click **Save** to finalize product registration.

______________________________________________________________________

## Verification & definition of done

- **Unique SKU Assigned**: System generates a unique product SKU (`PRD-YYYYMMDD-XXXX`).
- **Product Costing Calculated**: Total recipe cost updates automatically under product costing summary.
- **Invoice Availability**: Product appears in the dropdown list under **Trade → Create Invoice**.

______________________________________________________________________

## Field reference

| Field Name          | Type    | Required | Backend Validation / Constraints                | Description                                                   |
| :------------------ | :------ | :------- | :---------------------------------------------- | :------------------------------------------------------------ |
| **SKU**             | Text    | Auto     | Prefix `PRD`, read-only                         | System-generated tracking SKU.                                |
| **Name**            | Text    | Yes      | Max 50 characters                               | Product title used across invoices and manufacturing reports. |
| **Category**        | Select  | Yes      | Foreign Key (`Factory.Category`), `PROTECT`     | Product organizational category.                              |
| **Unit**            | Select  | Yes      | Choices: `Pieces`, `Dozens`, `Kg`, `Meters`     | Base unit of measurement.                                     |
| **Selling Rate**    | Decimal | Yes      | Max 13 digits, 2 decimal places, default `0.00` | Standard wholesale or retail selling price per unit.          |
| **Production Wage** | Decimal | No       | Max 13 digits, 2 decimal places, default `0.00` | Worker wage paid to manufacture one product unit.             |
| **Stock**           | Decimal | No       | Default `0.00`, 3 decimal places                | Current finished goods stock count in warehouse.              |
| **Restock Level**   | Decimal | No       | Default `0.00`, 3 decimal places                | Minimum stock count before triggering low-stock alert.        |
| **Is Enabled**      | Boolean | No       | Default `True`                                  | Active status toggle.                                         |
| **Is Public**       | Boolean | No       | Default `False`                                 | Visibility toggle for public catalog or storefront.           |

______________________________________________________________________

## Exception handling & error recovery

| Error Symptom / Message                                 | Root Cause                                                           | Step-by-Step Remediation                                                                                                 |
| :------------------------------------------------------ | :------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------- |
| **"Cannot delete material linked to product costings"** | Foreign Key constraint (`models.PROTECT`) prevents material removal. | 1. Remove material from **Product Costings** tab on linked products.<br>2. Save product before deleting material record. |
| **Product missing from Create Invoice dropdown**        | **Is Enabled** flag set to `False`.                                  | 1. Open product in edit mode.<br>2. Toggle **Is Enabled** to `True` and click **Save**.                                  |
| **Low stock alert triggered unexpectedly**              | Warehouse **Stock** count fell below configured **Restock Level**.   | 1. Inspect finished goods stock inventory.<br>2. Update stock count or adjust **Restock Level** threshold.               |

______________________________________________________________________

## Related workflows & next steps

- **Create Invoice** — Sell finished products to clients.
- **Material Inventory** — Monitor raw material stock availability for product recipes.
- **Category Management** — Organize products by apparel types or lines.

______________________________________________________________________

## Related pages

- **Products Overview** — View and filter finished products
- **Edit Product** — Update product details, pricing, and costings
- **Categories** — Manage product classification categories
- **Materials** — Manage raw material specifications and costs
