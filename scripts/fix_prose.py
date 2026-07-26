#!/usr/bin/env python3
"""Targeted prose corrections that need judgement rather than a pattern.

The bulk transforms live in normalize_docs.py. These are the individual
sentences where a mechanical substitution would have produced bad English, so
each replacement is written out and asserted. Run from the repository root
after normalize_docs.py. Idempotent: an already-applied edit is skipped.
"""

from __future__ import annotations

import sys
from pathlib import Path

UG = Path("docs/user-guide")

EDITS: list[tuple[str, str, str]] = [
    # -- STYLE_SPEC section 5: approved terminology -------------------------
    (
        "09-reference/glossary.md",
        "A bill that lists what you sold, how much it costs, and what the client still owes.",
        "A record that lists what you sold, how much it costs, and what the client still owes.",
    ),
    (
        "09-reference/glossary.md",
        "Money received or recorded against a bill or other financial record.",
        "Money received or recorded against an invoice or other financial record.",
    ),
    (
        "09-reference/glossary.md",
        "A price reduction given to a client or applied to a bill.",
        "A price reduction given to a client or applied to an invoice.",
    ),
    (
        "09-reference/glossary.md",
        "A bill or payment that has been completed.",
        "An invoice or payment that has been completed.",
    ),
    (
        "01-business/clients/add-client.md",
        "- Onboarding a new buyer or business partner",
        "- Onboarding a new client or business partner",
    ),
    # -- STYLE_SPEC section 2: "navigate to" --------------------------------
    (
        "00-getting-started/login-and-logout.md",
        "Open your browser and navigate to your CTB Admin URL.",
        "Open your browser and go to your CTB Admin URL.",
    ),
    (
        "01-business/clients/overview.md",
        "Click the date arrows to navigate to a specific date",
        "Click the date arrows to move to a specific date",
    ),
    (
        "01-business/vendors/overview.md",
        "Click the date arrows to navigate to a specific date",
        "Click the date arrows to move to a specific date",
    ),
    (
        "03-trade/invoices/overview.md",
        "Click the date arrows to navigate to a specific date",
        "Click the date arrows to move to a specific date",
    ),
    (
        "04-employee/purchase-balance/overview.md",
        "Click the date arrows to navigate to a specific date",
        "Click the date arrows to move to a specific date",
    ),
    (
        "04-employee/salary/overview.md",
        "Use the calendar arrows to navigate to a specific month or payroll period",
        "Use the calendar arrows to move to a specific month or payroll period",
    ),
    (
        "03-trade/invoices/print-chalan.md",
        "1. Navigate to the **Invoices list** from **Trade → Invoices**",
        "1. Go to the **Invoices list** from **Trade → Invoices**",
    ),
    (
        "03-trade/invoices/print-invoice.md",
        "1. Navigate to the **Invoices list** from **Trade → Invoices**",
        "1. Go to the **Invoices list** from **Trade → Invoices**",
    ),
    (
        "08-settings-and-admin/app-settings.md",
        "then navigate to **CTB Settings** and select **Config**.",
        "then open **CTB Settings** and select **Config**.",
    ),
    # -- STYLE_SPEC section 2: "allows you to" ------------------------------
    (
        "01-business/clients/client-detail.md",
        "It allows you to review client information and perform actions such as editing or managing transactions.",
        "Use it to review client information and to edit the record or manage its transactions.",
    ),
    (
        "01-business/vendors/vendor-detail.md",
        "Each tab allows you to view or manage different types of vendor information.",
        "Each tab shows a different type of vendor information.",
    ),
    (
        "02-factory/categories/overview.md",
        "It allows you to quickly search, review, and manage categories used across products.",
        "Use it to search, review, and manage the categories used across products.",
    ),
    (
        "02-factory/materials/edit-material.md",
        "The **Edit Material** page allows you to update existing material information.",
        "Use the **Edit Material** page to update existing material information.",
    ),
    (
        "02-factory/materials/overview.md",
        "The **Materials** section allows you to manage all raw materials, track stock movement, and monitor inventory activity.",
        "Use the **Materials** section to manage all raw materials, track stock movement, and monitor inventory activity.",
    ),
    (
        "02-factory/products/overview.md",
        "The **Products** section allows you to manage all manufactured products, define material compositions, set pricing, and track inventory levels.",
        "Use the **Products** section to manage all manufactured products, define material compositions, set pricing, and track inventory levels.",
    ),
    (
        "02-factory/products/product-detail.md",
        "It allows you to review product information and perform actions such as editing or managing inventory.",
        "Use it to review product information and to edit the record or manage its inventory.",
    ),
    (
        "04-employee/employees/overview.md",
        "The **Employees** section allows you to manage all employee records",
        "Use the **Employees** section to manage all employee records",
    ),
    (
        "04-employee/positions/overview.md",
        "It allows you to quickly search, review, and manage employee positions used across your workforce.",
        "Use it to search, review, and manage the positions used across your workforce.",
    ),
    (
        "04-employee/tasks/create-task.md",
        "The **Notes** tab allows you to add internal comments or additional context about the task:",
        "Use the **Notes** tab to add internal comments or additional context about the task:",
    ),
    (
        "03-trade/invoices/print-chalan.md",
        "Most modern browsers allow you to save as PDF directly from the print dialog.",
        "Most modern browsers can save as PDF directly from the print dialog.",
    ),
    (
        "03-trade/invoices/print-invoice.md",
        "Most modern browsers allow you to save as PDF directly from the print dialog.",
        "Most modern browsers can save as PDF directly from the print dialog.",
    ),
    # -- STYLE_SPEC section 2: banned adverbs -------------------------------
    (
        "04-employee/salary/overview.md",
        "If zero, these fields simply do not add to the base salary.",
        "If zero, these fields do not add to the base salary.",
    ),
    (
        "08-settings-and-admin/app-settings.md",
        "one at a time to easily identify which change caused any issues.",
        "one at a time to identify which change caused any issues.",
    ),
    (
        "09-reference/offline-mode.md",
        "1. Refresh the page if you think the connection just recovered.",
        "1. Refresh the page if you think the connection has recovered.",
    ),
    # -- STYLE_SPEC section 2: address the reader as "you" ------------------
    (
        "07-reports/invoice-report.md",
        "- User must have access to the **Reports** module.",
        "- You have access to the **Reports** module.",
    ),
    (
        "07-reports/profit-report.md",
        "- User must have access to the **Trade** module.",
        "- You have access to the **Trade** module.",
    ),
    (
        "07-reports/voucher-report.md",
        "- User must have access to the **Reports** module.",
        "- You have access to the **Reports** module.",
    ),
    # -- STYLE_SPEC section 4.1: a UI button labelled "Log in →" ------------
    (
        "00-getting-started/login-and-logout.md",
        "1. Click **Log in ->** to open the Dashboard.",
        "1. Click **Log in →** to open the Dashboard.",
    ),
]


def main() -> int:
    if not UG.is_dir():
        print("error: run from the repository root", file=sys.stderr)
        return 1
    applied = already = missing = 0
    for rel, old, new in EDITS:
        path = UG / rel
        text = path.read_text(encoding="utf-8")
        if old in text:
            path.write_text(text.replace(old, new), encoding="utf-8")
            applied += 1
        elif new in text:
            already += 1
        else:
            print(f"  not found in {rel}: {old[:70]!r}", file=sys.stderr)
            missing += 1
    print(f"applied {applied}, already correct {already}, not found {missing}")
    return 1 if missing else 0


if __name__ == "__main__":
    raise SystemExit(main())
