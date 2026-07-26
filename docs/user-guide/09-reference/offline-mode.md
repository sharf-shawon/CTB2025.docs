---
tags: [module:reference, task:troubleshoot, role:staff]
---

# Offline Mode

## Summary

CTB Admin documentation uses a service worker to cache pages and shared assets as you browse. When your connection drops, the site will try to serve the last cached version of the page first.

______________________________________________________________________

## When to use this page

- When you need to work with offline mode in CTB Admin.

______________________________________________________________________

## How to access this page

From the sidebar, go to **Reference**, then open **Offline Mode**.

______________________________________________________________________

## How offline mode works

- Visited pages are saved locally in your browser cache.
- Shared assets such as styles and scripts are cached as they are requested.
- If a page is already cached, you can open it again even when the network is unavailable.
- If a page is not yet cached, the site falls back to a dedicated offline shell first, then to this page when available.

![Offline mode fallback page](offline-mode-photo.png)

______________________________________________________________________

## What to do when you are offline

1. Refresh the page if you think the connection has recovered.
1. Open a page you have already visited to load the cached copy.
1. Reconnect to the network and revisit any page that did not load from cache.

______________________________________________________________________

## What users should expect

- Already visited pages may still open even when the connection is weak.
- The first visit to a page may still need a working connection.
- Some images and assets may take longer to appear after a reconnect.

______________________________________________________________________

## Step-by-step instructions

1. Refresh the page if you think the connection has recovered.
1. Open a page you have already visited to load the cached copy.
1. Reconnect to the network and revisit any page that did not load from cache.
1. Clear the browser cache if a page or image still looks out of date.

______________________________________________________________________

## Field reference

Not applicable. This page describes browser and cache behaviour rather than a form.

______________________________________________________________________

## Tips and common issues

- Refresh once after reconnecting instead of repeatedly reloading the page.
- If an image or page looks stale, clear the browser cache and try again.
- Tell users to revisit the site while online after a deployment so the cache can update.

______________________________________________________________________

## Related pages

- [Error Pages](error-pages.md)
- [Troubleshooting](troubleshooting.md)
