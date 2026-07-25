# Product Return Report

## Summary

The Product Return Report lists product returns within a selected date range, showing return date, product, quantity, rate, total, client, returned-by user and originating invoice. Return amounts are applied to the client balance so the client's payable/credit is adjusted when a return is processed.

<!-- TODO: screenshot docs/user-guide/screenshots/reports/product-return-report.png -->

## When to use this page

- You need to review products returned by clients or by staff
- You want to reconcile returned goods with invoices and client balances
- You need a printable summary of returns for accounting or stock adjustments

## How to access this page

Open **Trade → Invoices → Product Return Report** in the left sidebar under **Trade**.

## Prerequisites

- Permission to view Reports or Trade reports (sales or finance role)
- Invoice and return records must exist for the selected date range
- Client accounts must exist to receive balance adjustments

## Step-by-step instructions

![Product Return Report Page](product-return-report-img.png)

1. Go to **Trade → Invoices → Product Return Report**.
1. Set the **Start Date** and **End Date** filters for the period you want to review
1. Optionally choose a **Client** or **Product** to narrow results
1. Click **Apply Filters** to refresh the report
1. Review each row showing **Return Date**, **Product**, **Qty**, **Rate**, **Total**, **Client**, **Returned By**, and **Invoice #**
1. Verify the **TOTAL** row at the bottom for aggregate returned quantity and amount
1. Note: When a return is recorded, its `Total` amount is applied to the client balance — reducing the client's payable or increasing their credit depending on your accounting setup
1. Use the **Invoice #** link to open the originating invoice for context
1. Click **Print Report** to export or print the current filtered view

## Field reference

- **Start Date** — First date included in the filter

- **End Date** — Last date included in the filter

- **Client** — Filter results by a specific client; defaults to **All Clients**

- **Product** — Filter results by a specific product; defaults to **All Products**

- **Apply Filters** — Button that refreshes the report data

- **Return Date** — Date the product was returned

- **Product** — Product name (clickable if product detail exists)

- **Qty** — Quantity returned (decimal values allowed)

- **Rate** — Unit rate used to calculate the return amount

- **Total** — Line amount (`Qty × Rate`) credited back to the client balance

- **Client** — Client name receiving the credit

- **Returned By** — User who recorded the return

- **Invoice #** — Originating invoice reference (clickable link)

## Business rules

- Return amounts adjust the client's balance immediately when the return is processed
- Negative returns or corrections are shown as negative quantities/amounts and will adjust balances accordingly
- Stock levels should be updated after returns are processed; verify inventory adjustments with the Material/Product Stock reports

!!! Tips and common issues

    - If totals do not match accounting records, check whether the return has been posted or remains in draft
    - Returns against cancelled or deleted invoices may not apply automatically to client balances; verify invoice status first
    - Use narrow date ranges for faster loading on large datasets
    
