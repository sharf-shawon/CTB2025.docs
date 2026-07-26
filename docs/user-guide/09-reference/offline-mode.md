---
tags: [module:reference, task:troubleshoot, role:staff]
---

# Offline Mode

<!-- metadata: owner: staff, last_updated: 2026-07-26, git_ref: main, staging_verified: true -->

Learn how CTB Admin handles network disconnections and Service Worker caching.

## Summary

CTB Admin documentation uses an automated Progressive Web App (PWA) Service Worker to cache visited documentation pages, stylesheets, scripts, and graphics locally in your browser. When network connectivity drops, users can continue reading previously cached documentation pages offline.

______________________________________________________________________

## When to use this page

- When working in low-connectivity factory or warehouse environments.
- When an offline fallback page appears while browsing documentation.
- When understanding what content remains available during network outages.
- When troubleshooting outdated or stale cached documentation assets after a deployment.

______________________________________________________________________

## How to access this page

From the sidebar navigation, Go to **Reference → Offline Mode**. The direct URL path is `/user-guide/09-reference/offline-mode/`.

______________________________________________________________________

## Prerequisites

- **Role permissions**: Accessible by all authenticated user roles (`staff`, `accountant`, `hr`, `admin`).
- **Prerequisites**: A modern web browser supporting Service Workers (Chrome, Firefox, Edge, Safari).

______________________________________________________________________

## Step-by-step instructions

1. Browse CTB Admin documentation while connected to the internet to prime your browser cache.
1. If your internet connection drops, continue navigating visited pages normally.
1. If you attempt to open an unvisited page while offline, review the **Offline Fallback Page**.
1. Once network connectivity is restored, click **Refresh** to sync the latest content updates.

______________________________________________________________________

## Verification and definition of done

- **Cache verification**: Visited documentation pages load without internet access.
- **Service Worker active**: Browser developer tools confirm `sw-register.js` is active and controlling document caching.

______________________________________________________________________

## Field reference

### Offline functionality matrix

| Capability / Feature              | Online State    | Offline State    | Behavior Description                                                  |
| --------------------------------- | --------------- | ---------------- | --------------------------------------------------------------------- |
| **Visited Documentation Pages**   | Full Access     | Full Access      | Served directly from local browser Cache Storage.                     |
| **Unvisited Documentation Pages** | Full Access     | Offline Fallback | Displays offline notice shell guiding user to reconnect.              |
| **Global Site Search**            | Full Access     | Partial Access   | Searches across locally cached page titles and text.                  |
| **CTB Admin Application Forms**   | Live Read/Write | Blocked          | Data entry forms require an active server connection to save records. |

![Offline mode fallback page](offline-mode-photo.png)

______________________________________________________________________

## Exception handling and error recovery

| Issue / Symptom                                  | Root Cause                                                     | User remediation step                                                                                                                    | Role required     |
| ------------------------------------------------ | -------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| Page displays outdated content after site update | Browser cache is retaining old Service Worker asset bundle     | 1. Reconnect to internet.<br>2. Perform hard refresh (**Ctrl+F5** or **Cmd+Shift+R**).<br>3. Clear browser site cache if issue persists. | `staff`           |
| Unvisited page fails to load offline             | Page HTML was not cached prior to network loss                 | Reconnect to internet and click the link to cache the page for offline availability.                                                     | `staff`           |
| Service Worker fails to register                 | Browser privacy settings block local storage / Service Workers | Enable local site storage and Service Workers in browser settings.                                                                       | `staff` / `admin` |

______________________________________________________________________

## Related pages

- **[Error Pages](error-pages.md)** — Diagnostics for 403, 404, 500, and Maintenance errors.
- **[Troubleshooting Guide](troubleshooting.md)** — Step-by-step solutions for connectivity and browser caching issues.
