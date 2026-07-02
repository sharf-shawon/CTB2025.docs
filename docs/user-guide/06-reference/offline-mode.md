# Offline Mode

CTB Admin documentation uses a service worker to cache pages and shared assets as you browse. When your connection drops, the site will try to serve the last cached version of the page first.

If you open a page for the first time while offline, the service worker shows a lightweight fallback shell so you still see a clear status page.

## How offline mode works

- Visited pages are saved locally in your browser cache.
- Shared assets such as styles and scripts are cached as they are requested.
- If a page is already cached, you can open it again even when the network is unavailable.
- If a page is not yet cached, the site falls back to a dedicated offline shell first, then to this page when available.

![Offline mode fallback page](offline-mode-photo.png)

## What to do when you are offline

1. Refresh the page if you think the connection just recovered.
1. Open a page you have already visited to load the cached copy.
1. Reconnect to the network and revisit any page that did not load from cache.

## What users should expect

- Already visited pages may still open even when the connection is weak.
- The first visit to a page may still need a working connection.
- Some images and assets may take longer to appear after a reconnect.

!!! Tips and common issues

```
- Refresh once after reconnecting instead of repeatedly reloading the page.
- If an image or page looks stale, clear the browser cache and try again.
- Tell users to revisit the site while online after a deployment so the cache can update.
```

## Related pages

- [Error Pages](error-pages.md)
- [Production Release Checklist](release-checklist.md)
