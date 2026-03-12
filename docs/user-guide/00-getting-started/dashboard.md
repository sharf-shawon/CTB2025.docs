# Dashboard

The Dashboard is the first page you see after logging in to CTB Admin. It gives you an at-a-glance view of business performance, quick access to every module, and real-time operational data — all from a single screen.

## When to use this page

- Reviewing key business metrics at the start of the day.
- Navigating quickly to any module or record-creation page.
- Monitoring invoice status, stock levels, and outstanding balances.
- Reading the daily Quran quote displayed for staff motivation.

## How to access this page

The Dashboard opens automatically after login. You can return to it at any time by clicking **Dashboard** at the top of the left sidebar.

______________________________________________________________________

## Page overview

![Dashboard](dashboard.png)

______________________________________________________________________

## Top navigation bar

The top bar runs across every page in CTB Admin. The labelled items below match the annotations in the screenshot above.

| #   | Element                 | Description                                                                                        |
| --- | ----------------------- | -------------------------------------------------------------------------------------------------- |
| 1   | **CTB Fashion** (logo)  | Displays the company brand. Click it to return to the Dashboard from any page.                     |
| 2   | **Breadcrumbs**         | Shows your current location in the navigation hierarchy (for example, **Home › Dashboard**).       |
| 3   | **Side menu toggle**    | Collapses or expands the left sidebar to give more screen space to the main content area.          |
| 4   | **Link menu**           | Opens a menu of pinned or frequently used links for fast access.                                   |
| 5   | **Search**              | Global search bar — type any keyword to find records, pages, or settings across the entire system. |
| 6   | **App Mode**            | Switches between **Dark** and **Light** display modes.                                             |
| 7   | **App Language menu**   | Changes the interface language.                                                                    |
| 8   | **Theme Switch**        | Cycles through available colour themes for the admin interface.                                    |
| 9   | **Task menu**           | Opens the task panel showing your pending and assigned tasks.                                      |
| 10  | **User Name**           | Displays the currently logged-in user. Click to access your profile, password settings, or logout. |
| 2A  | **Current App Version** | Shows the deployed version of CTB Admin, visible at the bottom of the sidebar.                     |

______________________________________________________________________

## Left sidebar

The sidebar groups all modules into collapsible sections. Each section expands to show its individual pages.

| Section                       | Items                                                                                    |
| ----------------------------- | ---------------------------------------------------------------------------------------- |
| **Reports**                   | Invoice Report, CTB Chat                                                                 |
| **Trade Management**          | Invoices, Vouchers, Banks, Checks, Payments, Purchase Balances                           |
| **Business Management**       | Clients                                                                                  |
| **Tender Management**         | Tender Invoices, Tender Quotations, Tender Payments, Tender Checks                       |
| **Factory Management**        | Products, Categories, Materials, Material Inventory                                      |
| **Employee Management**       | Employees, Positions, Departments, Salary, Wages, Payouts, Attendance, Facial Attendance |
| **User and Group Management** | Users, Groups, Audit Log, All Applications                                               |

Click any section header to expand or collapse it. The sidebar can be fully hidden using the **Side menu toggle** (item 3) in the top bar.

______________________________________________________________________

## The Holy Quran section

Below the top bar, the Dashboard displays a randomly selected **Quran verse** in Arabic, along with its English reference and a direct link to the full Surah. This quote refreshes each time the Dashboard is loaded or manually refreshed.

| Control                           | Description                                                            |
| --------------------------------- | ---------------------------------------------------------------------- |
| **Refresh Quran Quote** (item 11) | Loads a new random verse immediately without reloading the whole page. |

______________________________________________________________________

## Quick Access Pages

The **Quick Access Pages** section (item 12 — toggle to show/hide) displays every major model in CTB Admin as a colourful card. Each card gives you two actions:

- **Click anywhere on the card** — opens the **list page** for that model.
- **Click the + (Add) button** on the card — opens the **create new record** page for that model.

You can mark frequently used pages as **Favourites** by clicking the heart icon on any card. Favourited cards appear at the top of the section.

!!! info "Caching"
The Dashboard — including Quick Access Pages and Dashboard Analytics — is **cached for 15 minutes** to reduce server load. The data you see may be up to 15 minutes old.

```
To force an immediate recalculation of all data, click the **Refresh** button (item 12 area). Use this sparingly, as it places extra load on the server.
```

______________________________________________________________________

## Dashboard Analytics

The **Dashboard Analytics** section (item 13 — toggle to show/hide) presents live business data through summary cards and charts. All figures are drawn from multiple modules.

!!! note "Read-only section"
The Dashboard does not accept any data input. All analytics are calculated from records entered in other modules.

### Summary cards

| Card                 | Description                                                |
| -------------------- | ---------------------------------------------------------- |
| **Total Invoices**   | Count of all invoices recorded in the system.              |
| **Total Clients**    | Count of all registered client accounts.                   |
| **Total Revenue**    | Sum of revenue from all paid and outstanding invoices.     |
| **Pending Payments** | Total value of invoices that have not yet been fully paid. |

### Charts and tables

| Chart / Table                            | Description                                                                                                                                                     |
| ---------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Invoice Count by Type**                | Bar chart showing the number of invoices broken down by type (for example, regular, tender, quotation).                                                         |
| **Invoice Status Distribution**          | Chart showing the share of invoices in each status (for example, Paid, Unpaid, Partial).                                                                        |
| **Top 5 Clients by Revenue**             | Bar chart ranking the five clients who have generated the most revenue.                                                                                         |
| **Invoice Revenue Trend (Last 90 Days)** | Area chart showing daily revenue over the past 90 days, useful for spotting growth or slowdowns.                                                                |
| **Top 10 Selling Products**              | Bar chart ranking products by quantity sold.                                                                                                                    |
| **Product Stock Levels**                 | Bar chart showing current stock quantities for all products.                                                                                                    |
| **Low Stock Alert**                      | Table listing products whose current stock has dropped to or below the reorder level. Statuses are shown as **Critical** (red) when immediate action is needed. |
| **Top 10 Client Balances**               | Bar chart showing the ten clients with the highest outstanding balance.                                                                                         |
| **Top 10 Vendor Balances**               | Bar chart showing the ten vendors with the highest outstanding balance.                                                                                         |
| **Top 10 Employee Balances**             | Bar chart showing the ten employees with the highest outstanding payable balance.                                                                               |
| **Voucher Count by Vendor**              | Chart showing how many vouchers have been issued per vendor.                                                                                                    |
| **Material Stock Levels**                | Bar chart showing current stock quantities for raw materials.                                                                                                   |
| **Payment Status Overview**              | Chart summarising payment records by their status (for example, Received, Pending).                                                                             |
| **Check Status Overview**                | Chart summarising check records by status (for example, Cleared, Bounced).                                                                                      |
| **Recent Payments (Last 5)**             | Table listing the five most recently recorded payments with date, reference, party, amount, and status.                                                         |
| **Recent Checks (Last 5)**               | Table listing the five most recently recorded checks with date, check number, bank, party, amount, and status.                                                  |

______________________________________________________________________

## Permissions

Access to the Dashboard Analytics section is controlled by the **"Can view admin dashboard"** permission. Users without this permission will see the page but the analytics section will not be displayed.

Contact your system administrator to request access if the analytics section is missing from your Dashboard.

______________________________________________________________________

## Tips and common issues

- If the analytics data looks outdated, click the **Refresh** button to force a recalculation. Remember that this increases server load, so avoid clicking it repeatedly.
- If the **Dashboard Analytics** section is not visible, you may not have the **"Can view admin dashboard"** permission. Ask your administrator to grant it.
- Use the **heart icon** on Quick Access cards to pin your most-used pages to the top of the section.
- The sidebar version number (item 2A) is useful when reporting a bug — always include it when contacting support.

______________________________________________________________________

## Related pages

- **Login and Logout** — How to sign in and sign out of CTB Admin.
- **Overview** — A summary of all modules available in CTB Admin.
- **Invoice Reports** — Detailed invoice analytics and export options.
- **Client Reports** — Client-level financial summaries.
