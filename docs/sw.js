const CACHE_NAME = 'ctb-admin-docs-v3';
const OFFLINE_SHELL_URL = '/offline.html';
const OFFLINE_FALLBACK_URL = '/user-guide/06-reference/offline-mode/';
const PRECACHE_URLS = [
  '/',
  OFFLINE_SHELL_URL,
  OFFLINE_FALLBACK_URL,
  '/assets/images/ctb-logo.svg',
  '/assets/images/ctb-cover.png',
  '/assets/images/favicon.png',
  '/assets/javascripts/bundle.79ae519e.min.js',
  '/assets/javascripts/workers/search.2c215733.min.js',
  '/assets/stylesheets/main.484c7ddc.min.css',
  '/assets/stylesheets/palette.ab4e12ef.min.css',
  '/stylesheets/ctb-theme.css',
];

const normalizeNavigationUrl = (url) => {
  const parsedUrl = new URL(url);
  let path = parsedUrl.pathname;

  if (path.endsWith('/index.html')) {
    path = path.slice(0, -'index.html'.length);
  }

  if (!path.endsWith('/')) {
    path = `${path}/`;
  }

  return `${parsedUrl.origin}${path}`;
};

self.addEventListener('install', (event) => {
  event.waitUntil((async () => {
    const cache = await caches.open(CACHE_NAME);
    await cache.addAll(PRECACHE_URLS);
    self.skipWaiting();
  })());
});

self.addEventListener('activate', (event) => {
  event.waitUntil((async () => {
    const cacheNames = await caches.keys();

    await Promise.all(
      cacheNames
        .filter((cacheName) => cacheName !== CACHE_NAME)
        .map((cacheName) => caches.delete(cacheName)),
    );

    await self.clients.claim();
  })());
});

self.addEventListener('fetch', (event) => {
  const { request } = event;
  const isNavigation = request.mode === 'navigate';

  if (request.method !== 'GET') {
    return;
  }

  const requestUrl = new URL(request.url);

  if (requestUrl.origin !== self.location.origin) {
    return;
  }

  event.respondWith((async () => {
    const cache = await caches.open(CACHE_NAME);
    const navigationCacheKey = isNavigation ? normalizeNavigationUrl(request.url) : null;
    const cachedResponse =
      await cache.match(request) ||
      await cache.match(request, { ignoreSearch: true }) ||
      (isNavigation ? await cache.match(navigationCacheKey) : undefined);

    const updateCache = async () => {
      const networkResponse = await fetch(request);

      if (networkResponse && networkResponse.ok) {
        const responseClone = networkResponse.clone();
        await cache.put(request, responseClone);

        const responseContentType = networkResponse.headers.get('content-type') || '';

        if (isNavigation && responseContentType.includes('text/html')) {
          await cache.put(new Request(navigationCacheKey), networkResponse.clone());
        }
      }

      return networkResponse;
    };

    if (cachedResponse) {
      event.waitUntil(updateCache().catch(() => undefined));
      return cachedResponse;
    }

    try {
      return await updateCache();
    } catch (error) {
      if (isNavigation) {
        const fallbackResponse =
          await cache.match(OFFLINE_SHELL_URL) ||
          await cache.match(OFFLINE_FALLBACK_URL) ||
          await cache.match('/');

        if (fallbackResponse) {
          return fallbackResponse;
        }
      }

      throw error;
    }
  })());
});
