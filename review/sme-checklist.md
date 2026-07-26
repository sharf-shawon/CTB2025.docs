# Subject-matter review checklist

Open items that need someone with access to a running CTB Admin instance. Every
entry is something the documentation deliberately does **not** state, because it
could not be verified from the repository. Nothing here was guessed at.

Regenerate the marker-derived part of this list with:

```bash
uv run python scripts/style_lint.py --report-unverified
```

______________________________________________________________________

## 1 · Business rules that are documented but unconfirmed

These are described on published pages and should be checked against the running
system. Where a page says something that turns out to be wrong, it is wrong on
the live site today.

### Trade — checks

- [ ] Confirm the exact check status names used by the UI (`Pending`, `Passed`, `Bounced`, or others).
- [ ] Confirm delete eligibility by status and by payment linkage.
- [ ] Decide whether archived checks should replace deletion in restricted cases.
- [ ] Rewrite "Deleting a check" in `03-trade/checks/check-detail.md` once the above are confirmed.
- [ ] Add a fallback note for users who cannot see the **Delete** button.

### Trade — invoice reporting

- [ ] `03-trade/invoices/invoice-reports.md` and `07-reports/invoice-report.md` describe overlapping
    functionality under different names, with different sidebar paths. Confirm whether these are
    two screens or one. If one, retire the duplicate and add a redirect.

______________________________________________________________________

## 2 · Pages published with an explicit gap

Each of these carries a `Needs product review` block naming exactly what is missing.
Supplying the answer is enough to complete the page.

| Page                                      | What is needed                                                                    |
| ----------------------------------------- | --------------------------------------------------------------------------------- |
| `06-commission/manager-analytics.md`      | List columns, filters, and available actions                                      |
| `06-commission/payment-history.md`        | List columns, filters, and available actions                                      |
| `06-commission/client-bonus-campaigns.md` | The campaign form fields and their business meaning                               |
| `06-commission/client-bonus-analytics.md` | List columns and available actions                                                |
| `09-reference/permissions.md`             | The default permission set per business role, and whether any module is read-only |

______________________________________________________________________

## 3 · Missing screenshots

Pages that describe a screen without showing it. Capture at the same window width
as the existing screenshots and save alongside the page, in lowercase kebab-case.

### Trade

- [ ] `03-trade/banks/overview.md` — bank list
- [ ] `03-trade/banks/add-bank.md` — Add Bank form
- [ ] `03-trade/banks/bank-detail.md` — Bank Detail page
- [ ] `03-trade/vouchers/overview.md` — vouchers list
- [ ] `03-trade/vouchers/add-voucher.md` — Add Voucher form
- [ ] `03-trade/vouchers/voucher-detail.md` — Voucher Detail page
- [ ] `03-trade/invoices/overview.md` — invoice list or status filter

### Employee

- [ ] `04-employee/attendance/record-attendance.md` — Record Attendance form
- [ ] `04-employee/salary/overview.md` — salary list
- [ ] `04-employee/salary/generate-salary.md` — salary generation workflow
- [ ] `04-employee/salary/salary-detail.md` — Salary Detail page
- [ ] `04-employee/payouts/overview.md` — payouts list
- [ ] `04-employee/payouts/create-payout.md` — Create Payout form
- [ ] `04-employee/tasks/manage-task.md` — Create/Edit Task form
- [ ] `04-employee/purchase-balance/overview.md` — purchase balance ledger
- [ ] `04-employee/departments/overview.md` — departments list
- [ ] `04-employee/departments/manage-department.md` — Add/Edit Department form
- [ ] `04-employee/positions/overview.md` — positions list
- [ ] `04-employee/positions/manage-position.md` — Add/Edit Position form
- [ ] `04-employee/wages/overview.md` — wages list
- [ ] `04-employee/wages/add-wage-entry.md` — Add Wage Entry form

### Reports

- [ ] `07-reports/attendance-report.md`
- [ ] `07-reports/executive-summary.md`
- [ ] `07-reports/product-return-report.md`

### Reference

- [ ] `09-reference/error-pages.md` — the 403, 404, 500, and maintenance screens
- [ ] `09-reference/offline-mode.md` — offline fallback screen

______________________________________________________________________

## 4 · Terminology

- [ ] Validate the definitions in `09-reference/glossary.md` with the business owners.
- [ ] Expand the glossary with module-specific terms that come up in support and training.
- [ ] Confirm the four business roles used by the `role:` tag facet (`staff`, `accountant`, `hr`,
    `admin`) match how the organisation actually divides the work. The vocabulary is enforced in
    `mkdocs.yml` and `scripts/style_lint.py`, so changing it means changing both.

______________________________________________________________________

## 5 · Style baseline

`scripts/style_lint_baseline.json` records violations that predate the style gate.
It may shrink but never grow. Drive it to zero, then delete the file and the
`--baseline` handling in `scripts/style_lint.py`.

```bash
uv run python scripts/style_lint.py --stats --no-baseline   # what remains
uv run python scripts/style_lint.py --update-baseline       # after fixing some
```
