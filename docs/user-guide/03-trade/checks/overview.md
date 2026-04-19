# Checks Overview

Document cheque management list and states.

The **Checks** module in CTB Admin manages all bank check records used in your business transactions. A check represents a physical bank check that is either received from a client (money coming in) or issued to a vendor (money going out). Each check record tracks the check number, bank account, amount, current balance, and status throughout its lifecycle. Check records help you monitor check usage, link payments to specific checks, and manage bank account reconciliation.

## What you can do in this module

- **Record received checks** — Register checks received from clients with their bank, number, date, and amount.
- **Record issued checks** — Register checks issued to vendors for payments.
- **Track check balances** — Monitor how much of a check has been used or remains available.
- **Update check status** — Track whether checks are Pending, Cleared (Passed), Bounced, or Cancelled.
- **Link payments to checks** — Associate payment records with specific checks to reduce their balance.
- **Store check photos** — Upload front and back images of checks for verification and archival.
- **View check history** — Access the complete audit trail of all changes made to a check record.

## Module structure

| Page         | Purpose                                                           |
| ------------ | ----------------------------------------------------------------- |
| Overview     | This page. Module summary and navigation guide.                   |
| Checks List  | View all checks with filters, search, and quick actions.          |
| Add Check    | Create a new check record with all required details.              |
| Edit Check   | Update check details (only when conditions allow editing).        |
| Check Detail | View a check's full record, photos, linked payments, and history. |

______________________________________________________________________

## Check lifecycle

A check moves through the following states during its lifecycle:

| Status        | Description                                                             |
| ------------- | ----------------------------------------------------------------------- |
| **Pending**   | Check has been recorded but not yet processed by the bank.              |
| **Passed**    | Bank has cleared and honored the check.                                 |
| **Bounced**   | Bank rejected the check (insufficient funds, signature mismatch, etc.). |
| **Cancelled** | Check has been cancelled before it was processed.                       |

______________________________________________________________________

## Typical workflow

1. **Add** a new check when you receive a check from a client or issue one to a vendor.
1. **View the Check Detail** page to verify the check was recorded correctly.
1. **Link payments** to the check when recording transactions that use this check.
1. **Update the status** to Passed when the bank clears the check.
1. **Record a bounce** if the bank rejects the check.

______________________________________________________________________

## Related modules

- **Trade → Payments** — Payment records are linked to checks to track check usage and reduce check balances.
- **Trade → Banks** — Bank accounts are linked to checks to identify which bank issued or received the check.
- **Business → Clients** — Checks received from clients are linked to client records.
- **Business → Vendors** — Checks issued to vendors are linked to vendor records.
- **Trade → Invoices** — Invoices may be settled using bank checks.
