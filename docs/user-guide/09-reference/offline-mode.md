---
tags: [module:reference, task:troubleshoot, role:staff]
---

# Offline Mode

<!-- metadata: owner: staff, last_updated: 2026-07-26, git_ref: main, staging_verified: true -->

Learn how CTB Admin handles network disconnections and Service Worker caching.

## Summary

CTB Admin uses Progressive Web App (PWA) Service Worker caching to store visited documentation pages, stylesheets, scripts, and media files locally in your browser. During a network disconnection, users can continue browsing previously cached documentation pages offline.

______________________________________________________________________

## When to use this page

- Navigating system documentation in low-connectivity factory or warehouse settings.
- Reconciling unvisited page offline fallback screens.
- Resolving stale caching behavior after a recent documentation deployment.
- Verifying the status of the local Service Worker or browser cache store.

______________________________________________________________________

## How to access this page

From the sidebar navigation, select **Reference → Offline Mode** (`/user-guide/09-reference/offline-mode/`).

______________________________________________________________________

## Prerequisites

- Modern browser with Service Worker and Cache Storage support (Chrome, Firefox, Safari, Edge).
- Active internet connection during the initial browse session to prime the cache.

______________________________________________________________________

## Step-by-step instructions

1. Open the documentation site while connected to the internet to initialize caching.
1. If the network connection drops, continue reading already cached pages.
1. If an unvisited page is requested while offline, review the **Offline Fallback Page** notice.
1. Verify browser cache state by opening Chrome DevTools (**F12** $\rightarrow$ **Application** $\rightarrow$ **Cache Storage**).
1. Reconnect to the internet and click **Refresh** to sync new updates.

______________________________________________________________________

## Verification & definition of done

- **Offline availability**: Disabling network connectivity in browser settings allows cached documentation pages to load.
- **Service worker active**: The browser DevTools console confirms `sw.js` registration is active and controlling caching.

______________________________________________________________________

## Field reference

### Offline functionality matrix

| Capability / Feature   | Online State    | Offline State    | Behavior Description                                                  |
| ---------------------- | --------------- | ---------------- | --------------------------------------------------------------------- |
| **Visited Pages**      | Full Access     | Full Access      | Loaded directly from local browser Cache Storage.                     |
| **Unvisited Pages**    | Full Access     | Offline Fallback | Displays offline notice shell prompting reconnection.                 |
| **Global Site Search** | Full Access     | Partial Access   | Searches across locally cached page titles and text.                  |
| **Admin Forms**        | Live Read/Write | Blocked          | Data entry forms require an active server connection to save records. |

![Offline mode fallback page](offline-mode-photo.png)

______________________________________________________________________

## Exception handling & error recovery

| Error Code / Symptom | Root Cause                                                     | Step-by-step remediation procedure                                                                                                                    | Actionable role required |
| -------------------- | -------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------ |
| Outdated content     | Browser Cache retains stale Service Worker asset bundle        | 1. Reconnect to the internet.<br>2. Perform a hard refresh (**Ctrl+F5** or **Cmd+Shift+R**).<br>3. Clear browser site cache if content remains stale. | `staff`                  |
| Fallback screen      | Attempted to access unvisited page while offline               | 1. Reconnect to active network.<br>2. Click link to download page to browser cache store.                                                             | `staff`                  |
| SW fails to register | Browser privacy settings block local storage / Service Workers | 1. Open browser settings.<br>2. Enable local site storage and Service Workers.                                                                        | `staff` / `admin`        |

______________________________________________________________________

## Related workflows & next steps

- **[Error Pages](error-pages.md)** — Diagnose standard HTTP status error screens.
- **[Troubleshooting Guide](troubleshooting.md)** — General browser and network resolution steps.

______________________________________________________________________

## Related pages

- **[Reference](../README.md)** — Glossary, error matrices, and shortcut guides.
