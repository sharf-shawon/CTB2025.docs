---
tags: [module:reference, task:view, role:staff]
---

# Glossary

<!-- metadata: owner: staff, last_updated: 2026-07-26, git_ref: main, staging_verified: true -->

Look up business and operational definitions used across CTB Admin screens and documentation.

## Summary

The glossary provides standard business definitions for system terms, record states, trade documents, factory components, and accounting concepts. Use it to align team terminology across sales, production, payroll, and financial operations.

______________________________________________________________________

## When to use this page

- When you encounter an unfamiliar button label, status pill, or field name on a CTB Admin screen.
- When onboarding new factory, office, HR, or accounting staff.
- When distinguishing between similar financial documents such as a Chalan, Invoice, Voucher, or Tender Invoice.
- When verifying record lifecycle states (Draft, Sent, Paid, Cancelled).

______________________________________________________________________

## How to access this page

From the sidebar navigation, Go to **Reference → Glossary**. The direct URL path is `/user-guide/09-reference/glossary/`.

______________________________________________________________________

## Prerequisites

- **Role permissions**: Accessible by all authenticated user roles (`staff`, `accountant`, `hr`, `admin`).
- **Prerequisites**: Active CTB Admin user account and access to the web interface.

______________________________________________________________________

## Step-by-step instructions

1. Open **Reference → Glossary** from the left sidebar navigation.
1. Locate the relevant business category (General, Trade, Factory, Employee, Admin, or Record States).
1. Use the browser search shortcut (**Ctrl+F** or **Cmd+F**) or the top search bar to quickly highlight a specific term.
1. Click any cross-referenced link in the definition to open the operational guide for that module.

______________________________________________________________________

## Verification and definition of done

- **Term resolution**: The targeted term is found in the taxonomy table with a clear, non-technical business definition.
- **Workflow context**: The term links directly to its parent workflow page in CTB Admin.

______________________________________________________________________

## Field reference

### General business terms

| Term                    | Meaning                                                                                                 |
| ----------------------- | ------------------------------------------------------------------------------------------------------- |
| **Client**              | A business partner or Client purchasing finished goods or services from CTB.                            |
| **Vendor**              | A Vendor or raw material vendor from whom CTB purchases fabric, hardware, or services.                  |
| **Invoice**             | A legal request for payment detailing sold items, taxes, discounts, shipping, and total payable.        |
| **Payment**             | A financial transaction recording incoming funds from a Client or outgoing funds to a Vendor.           |
| **Bank**                | A registered financial institution account tracking company deposits, withdrawals, and check clearings. |
| **Balance**             | The current net amount owed by a Client or payable to a Vendor.                                         |
| **Opening Balance**     | The initial credit or debit amount assigned to a Client or Vendor account upon setup.                   |
| **Discount**            | A price reduction applied to an invoice total or individual line item.                                  |
| **Commission Balance**  | An accumulated reward balance earned by sales representatives or Clients.                               |
| **Upper Balance Limit** | The maximum allowed debt balance for a Client before superuser approval is required.                    |
| **Lower Balance Limit** | The minimum balance floor enforced on Client or Vendor accounts.                                        |
| **Status**              | The current lifecycle state of a record (Draft, Sent, Paid, Cancelled, Approved).                       |
| **Active**              | A usable record available for selection in new transactions and daily operations.                       |
| **Inactive**            | An archived record hidden from active selection lists but preserved for historical audit.               |

### Trade and financial terms

| Term               | Meaning                                                                                             |
| ------------------ | --------------------------------------------------------------------------------------------------- |
| **Chalan**         | A delivery dispatch note accompanying shipped goods, listing items without price totals.            |
| **Voucher**        | A non-invoice accounting entry recording general expenses, income, or internal cash movements.      |
| **Tender Invoice** | A formal proposal invoice prepared for corporate or government bidding prior to contract execution. |
| **Quotation**      | An estimated price quote provided to a Client prior to placing an official order.                   |
| **Check**          | A physical bank check logged for tracking through deposit, clearing, or bounce states.              |
| **Payable**        | The net outstanding balance owed by CTB to Vendors or employees.                                    |
| **Receivable**     | The net outstanding money owed to CTB by Clients.                                                   |
| **Reconciliation** | The audit process matching internal CTB bank ledger transactions with bank statements.              |

### Factory and inventory terms

| Term                   | Meaning                                                                                             |
| ---------------------- | --------------------------------------------------------------------------------------------------- |
| **Category**           | A classification group organizing materials or finished products (e.g., Bags, Fabric, Accessories). |
| **Material**           | Raw inventory items used during factory production (e.g., zippers, leather, thread).                |
| **Material Inventory** | The stock ledger logging raw material arrivals, factory consumption, and adjustments.               |
| **Stock**              | Physical quantity of raw materials or finished products currently available in the warehouse.       |
| **Product**            | Manufactured finished goods ready for Client sales or catalog inventory.                            |
| **Costing**            | The total direct material and production cost required to manufacture a product unit.               |
| **Production Order**   | A factory manufacturing work order specifying items and quantities to produce.                      |

### Employee and payroll terms

| Term                 | Meaning                                                                                            |
| -------------------- | -------------------------------------------------------------------------------------------------- |
| **Department**       | An operational department grouping staff members (e.g., Cutting, Sewing, Accounting, HR).          |
| **Position**         | The official job title assigned to an employee within a department.                                |
| **Employee**         | A registered worker whose attendance, daily wages, or monthly salary are managed in CTB Admin.     |
| **Attendance**       | Daily log of employee check-in time, check-out time, work minutes, and overtime.                   |
| **Salary**           | Regular monthly fixed compensation generated during monthly payroll processing.                    |
| **Wage**             | Daily or piece-rate pay calculated from actual hours worked or units produced.                     |
| **Payroll**          | The monthly process compiling attendance, salaries, overtime, and deductions into final pay slips. |
| **Payout**           | Advance cash Payouts or bonus payments made to staff outside standard payroll cycles.              |
| **Purchase Balance** | An internal credit balance tracking employee purchases of factory goods on credit.                 |

### System and administration terms

| Term                  | Meaning                                                                                                  |
| --------------------- | -------------------------------------------------------------------------------------------------------- |
| **User Management**   | System administration portal where user accounts and role permissions are controlled.                    |
| **App Settings**      | Global system configuration parameters controlling company details and default options.                  |
| **SMS Notifications** | Automated mobile SMS alerts sent to Clients or staff upon order dispatch or payment receipt.             |
| **Maintenance Mode**  | Administrative system lock restricting user access during updates or database maintenance.               |
| **Audit Log**         | Immutable system history logging every record creation, modification, and deletion with user timestamps. |

______________________________________________________________________

## Exception handling and error recovery

| Symptom / Issue            | Root Cause                                        | User remediation step                                                                        | Role required     |
| -------------------------- | ------------------------------------------------- | -------------------------------------------------------------------------------------------- | ----------------- |
| Term missing from glossary | New system feature or custom field added recently | Report missing term to documentation administrator or check **Reference → Troubleshooting**. | `staff` / `admin` |
| Link on term does not load | Changed URL path or broken document bookmark      | Use top search bar to locate the target topic by module name.                                | `staff`           |

______________________________________________________________________

## Related pages

- **[Permissions Guide](permissions.md)** — Understand role permissions mapped to system modules.
- **[Troubleshooting Guide](troubleshooting.md)** — Learn how to resolve common system warnings and errors.
- **[Error Pages](error-pages.md)** — Review standard system error screens (403, 404, 500, Maintenance).
