// Space X Study service worker (self-hosted copy only).
// Cache-first for everything in this folder; a new release changes VERSION, which replaces the cache.
const VERSION = "sxs-22";
const SHELL = ["./", "manifest.webmanifest", "icons/icon-192.png", "icons/icon-512.png"];

self.addEventListener("install", e => {
  e.waitUntil(caches.open(VERSION).then(c => c.addAll(SHELL)).then(() => self.skipWaiting()));
});

self.addEventListener("activate", e => {
  e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== VERSION).map(k => caches.delete(k)))).then(() => self.clients.claim()));
});

self.addEventListener("fetch", e => {
  const u = new URL(e.request.url);
  if (e.request.method !== "GET" || u.origin !== location.origin) return;
  const key = u.pathname.endsWith("/index.html") ? new Request(u.href.replace(/index\.html$/, "")) : e.request;
  e.respondWith(caches.open(VERSION).then(c => c.match(key, { ignoreSearch: true }).then(hit => hit || fetch(e.request).then(r => {
    if (r.ok && r.type === "basic") c.put(key, r.clone());
    return r;
  }))));
});

// The page sends the list of notebook page images once it is idle; fetch the missing ones two at a time.
self.addEventListener("message", e => {
  const list = e.data && e.data.warm;
  if (!Array.isArray(list)) return;
  e.waitUntil(caches.open(VERSION).then(async c => {
    const todo = [];
    for (const p of list) if (typeof p === "string" && /^nb\/p\d{3}\.webp$/.test(p) && !(await c.match(p))) todo.push(p);
    const worker = async () => { while (todo.length) { const p = todo.shift(); try { const r = await fetch(p); if (r.ok) await c.put(p, r); } catch (err) { return; } } };
    await Promise.all([worker(), worker()]);
  }));
});
