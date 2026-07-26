---
tags: [module:settings, task:configure, role:admin]
---

# App Settings

## Summary

App Settings contains global system configuration for CTB Admin, including company branding, invoice templates, balance thresholds, notification preferences, factory operational limits, and emergency maintenance mode settings. Changes made here apply across all users and modules immediately.

______________________________________________________________________

## When to use this page

- Configuring company branding, legal contact details, and logo links for client-facing invoices.
- Setting balance alert thresholds (orange/red warning levels) on dashboards.
- Enabling or disabling SMS notifications and configuring SMS provider API tokens.
- Adjusting standard factory workday durations (in minutes) for attendance and wage calculations.
- Toggling system-wide Maintenance Mode during scheduled updates.

______________________________________________________________________

## How to access this page

From the sidebar navigation, click **All applications**, then select **CTB Settings → Config** (`/admin/CTB_Setting/config/`).

![Config Page Navigation](ctb-setting-path-direction.png)

![Config Settings Page](ctb-config-page.png)

______________________________________________________________________

## Prerequisites

- Active user session with superuser rights or `CTB_Setting.change_config` permission.
- Received executive authorization prior to modifying production thresholds or API keys.

______________________________________________________________________

## Step-by-step instructions

1. Open **CTB Settings → Config** from the sidebar.
1. Select the configuration section you want to modify (e.g. **Brand details**, **Invoice settings**, **SMS settings**).
1. Update setting values as required.
1. Review all modified values to prevent operational disruption.
1. Click **Save** at the bottom of the page to apply global changes immediately.

______________________________________________________________________

## Verification & definition of done

- **Settings applied**: Saved parameters immediately update invoice rendering, warning colors, or SMS notifications.
- **Audit trail logged**: Configuration changes log an entry under **Settings and Admin → Audit Log**.

______________________________________________________________________

## Field reference

### App details & brand details

- **Company Trading Name** — Official business name printed on sales invoices.
- **Main Contact Phone Number** — Business phone number displayed on client headers.
- **Main Email Address** — System email address used on invoices and automated receipts.
- **Official Company Address** — Legal street address for tax and invoice headers.

### Invoice & factory settings

- **Standard Tax Rate (%)** — Default sales tax percentage applied to invoice items.
- **Standard VAT (%)** — Default Value Added Tax percentage.
- **Max Discount (%)** — Maximum allowable discount percentage on sales invoices.
- **Standard Workday (Minutes)** — Factory shift duration (default: `480` minutes for 8 hours).

### SMS settings

- **Enable SMS** — Master toggle switch to enable or disable outgoing SMS alerts.
- **SMS Bearer Token** — API authentication token for SMS gateway provider.
- **Approved Sender ID** — Registered sender name displayed on client SMS messages.

______________________________________________________________________

## Exception handling & error recovery

| Error Code / Symptom    | Root Cause                                                | Step-by-step remediation procedure                                                                                   | Actionable role required |
| ----------------------- | --------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | ------------------------ |
| `403 Forbidden` on save | User account lacks `CTB_Setting.change_config` permission | 1. Contact a superuser to assign `CTB_Setting.change_config`.<br>2. Log out and sign back in to refresh permissions. | `admin`                  |
| SMS delivery fails      | Invalid SMS Bearer Token or endpoint URL                  | 1. Verify API token with SMS service provider.<br>2. Confirm **Approved Sender ID** matches provider registration.   | `admin`                  |
| Maintenance mode lock   | Superuser enabled Maintenance Mode for non-superusers     | 1. Access `/admin/` using superuser credentials.<br>2. Toggle **Maintenance Mode** off under App Settings.           | `admin`                  |

______________________________________________________________________

## Related workflows & next steps

- **[User Management](user-management.md)** — Manage user accounts and Django permission codenames.
- **[Audit Log](audit-log.md)** — Review administrative configuration edit history.

______________________________________________________________________

## Related pages

- **[Settings and Admin](../README.md)** — All system configuration and security administration tools.
