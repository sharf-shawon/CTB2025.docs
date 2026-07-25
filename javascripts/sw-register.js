(function () {
  if (!('serviceWorker' in navigator)) {
    return;
  }

  window.addEventListener('load', function () {
    navigator.serviceWorker.register(new URL('/sw.js', window.location.origin).href).catch(function () {
      return;
    });
  });
}());
