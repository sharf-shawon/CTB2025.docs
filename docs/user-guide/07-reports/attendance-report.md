# Attendance Report

## Summary

The Monthly Attendance Report shows a day-by-day attendance grid for all employees for a selected month, plus per-employee summary columns for presence, lateness, overtime and other tallies. Use it to audit staff presence, export a printable report, and feed payroll calculations.

<!-- TODO: screenshot docs/user-guide/screenshots/reports/attendance-report.png -->

## When to use this page

- You need a month-level view of employee attendance for payroll or review
- You want to verify daily attendance patterns across the organisation
- You need a printable monthly attendance summary for management
- You need to identify late arrivals, early departures or overtime at a glance

## How to access this page

Open **Employee → Attendances → Monthly Attendance Report** in the left sidebar.

## Prerequisites

- Permission to view Reports or Attendance pages (HR or manager role)
- Employee records must exist in **Employees**
- Attendance entries (time-in / time-out) must be recorded for the chosen month

## Step-by-step instructions

![attendance report page](./../.././gallery/Reports/desktop-monthly-attendance-report.png)

1. Go to **Employee → Attendances → Monthly Attendance Report**.
1. Select the month (or set the Start/End Date) for the report period if controls are provided
1. Click **Apply Filter** (or similar) to refresh the grid for the selected month
1. Use the grid to inspect per-employee day cells; each cell shows attendance status for that date
1. Review the right-side summary columns for each employee (totals for present, late, overtime, etc.)
1. Use the legend below the table to interpret cell color codes (full shift, partial, leave, overtime, late/early)
1. Click **Print Report** (top-left) to print or export the current view

## Field reference

- **Employee** — Employee name (first column). Click to open the employee record if supported

- **Date columns (1–31)** — One column per calendar day in the selected month. Cell values indicate attendance status (present, absent, leave, half-day, etc.)

- **Summary columns (right)** — Per-employee tallies, typically including:

    - **Present (P)** — Count of days the employee was present
    - **Absent (A)** — Count of absent days (unmarked or absent status)
    - **Late (L)** — Count of late arrivals
    - **OT** — Overtime hours or overtime day count (implementation varies)
    - **Early/Early leave** — Count of early departures, if tracked
    - **Total** — Aggregate attendance-related metric (may be labelled differently in your deployment)

- **Legend** — A legend below the grid explains cell colours and symbols, for example:

    - Full shift worked
    - Partial shift or partial clock-in/clock-out
    - Leave (paid/unpaid)
    - Overtime entry
    - Late arrival or early departure
    - Total present/attendance summary

## Tips and common issues

- If many rows show empty cells, confirm that automatic time capture or manual attendance entries were recorded for that month
- Narrow the date range when the report is slow to load for large employee lists
- Use the employee link (left column) to open an employee's attendance detail when investigating a specific row
- Overtime and late counts depend on your organisation's shift rules — verify shift settings if totals look unexpected

## Related pages

- **[Attendance Overview]** — View and manage attendance records
- **[Record Attendance]** — Add or edit daily attendance entries
- **[Employees Overview]** — Manage employee records and profiles
- **[Salary Detail]** — Payroll and salary records used for payroll reconciliation
