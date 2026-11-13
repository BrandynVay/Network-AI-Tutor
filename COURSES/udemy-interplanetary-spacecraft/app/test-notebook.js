// Run: (cd dist && python3 -m http.server 8765 --bind 127.0.0.1 &) ; node test-notebook.js http://localhost:8765/
// Duo layout test: the sizes measured on the device, touch on. Also: no sideways overflow on any tab,
// export/import round trip, and the service worker on a localhost copy of dist/.
const { chromium } = require('playwright');
const path = require('path');
require('fs').mkdirSync(path.join(__dirname, 'nbshots'), { recursive: true });
const out = n => path.join(__dirname, 'nbshots', n);
const info = pg => pg.evaluate(() => { const st = document.getElementById('nbStage').getBoundingClientRect(), cx = innerWidth / 2;
  const panes = [...document.querySelectorAll('.nbpane')].map(p => p.getBoundingClientRect());
  const small = [...document.querySelectorAll('#nbRoot button')].filter(b => b.offsetParent && (b.offsetHeight < 44)).map(b => b.id || b.textContent.slice(0, 12));
  const crossing = [...document.querySelectorAll('#nbRoot.nbfocus .nbbar button, #nbRoot.nbfocus .nbpane')].filter(b => { const r = b.getBoundingClientRect(); return r.left < cx - 1 && r.right > cx + 1; }).length;
  return { mode: nb.L.mode, w: nb.L.w, h: nb.L.h, gap: nb.L.gap, num: document.getElementById('nbNum').textContent, panes: panes.map(r => [Math.round(r.left), Math.round(r.right)]), cx, crossing, small,
    loaded: [...document.querySelectorAll('#nbStage img')].every(i => i.complete && i.naturalWidth > 0), overflow: document.documentElement.scrollWidth - innerWidth }; });
(async () => {
  const b = await chromium.launch();
  const sizes = [[382, 580], [366, 600], [600, 366], [653, 515], [951, 585], [951, 630], [585, 951]];
  for (const [w, h] of sizes) {
    const ctx = await b.newContext({ viewport: { width: w, height: h }, deviceScaleFactor: 2, hasTouch: true, isMobile: true });
    const pg = await ctx.newPage();
    pg.on('pageerror', e => console.log(w + 'x' + h, 'PAGEERROR', e.message));
    await pg.goto(process.argv[2] || ('file://' + path.resolve(__dirname, 'space-x-study.html')));
    await pg.waitForTimeout(900);
    const over = {};
    for (const t of ['home', 'learn', 'quiz', 'cards', 'terms', 'numbers', 'teach', 'progress', 'notebook']) { await pg.click(`[data-tab="${t}"]`); await pg.waitForTimeout(120); const o = await pg.evaluate(() => document.documentElement.scrollWidth - innerWidth); if (o > 0) over[t] = o; }
    await pg.evaluate(() => nbGo(62));
    await pg.waitForTimeout(500);
    const n = await info(pg);
    await pg.click('#nbFocus'); await pg.waitForTimeout(600);
    const f = await info(pg);
    console.log(`${w}x${h} coarse=${await pg.evaluate(() => matchMedia('(pointer:coarse)').matches)} normal=${n.mode} ${n.w}x${n.h} | focus=${f.mode} ${f.w}x${f.h} gap=${f.gap} panes=${JSON.stringify(f.panes)} cx=${f.cx} crossing=${f.crossing} small=${JSON.stringify(f.small)} loaded=${f.loaded} tabOverflow=${JSON.stringify(over)}`);
    if ([382, 951, 653].includes(w) && h !== 630) await pg.screenshot({ path: out(`duo-${w}x${h}-focus.png`) });
    if (w === 951 && h === 585) { await pg.click('#nbFocus'); await pg.waitForTimeout(300); await pg.screenshot({ path: out('duo-951x585-normal.png') });
      await pg.click('#nbFocus'); await pg.waitForTimeout(300); await pg.click('#nbNext'); await pg.waitForTimeout(400); console.log('  next ->', (await info(pg)).num); }
    await ctx.close();
  }
  // laptop without touch must stay on whole page
  let pg = await b.newPage({ viewport: { width: 1440, height: 900 } });
  await pg.goto('file://' + path.resolve(__dirname, 'space-x-study.html')); await pg.waitForTimeout(300);
  await pg.click('[data-tab="notebook"]'); await pg.waitForTimeout(400);
  console.log('laptop 1440x900 ->', (await info(pg)).mode);
  // export / import round trip
  await pg.click('[data-tab="progress"]');
  await pg.evaluate(() => { rec('mc', '0', true); rec('cards', '3', false); });
  await pg.click('#expBtn'); const text = await pg.inputValue('#xferText');
  await pg.evaluate(() => { state = { mc: {}, why: {}, cards: {}, scenes: {}, sessions: [], runs: [] }; });
  await pg.click('#impBtn'); await pg.fill('#xferText', text); await pg.click('#impGo'); await pg.waitForTimeout(200);
  console.log('import ok:', await pg.evaluate(() => state.mc['0'].seen === 1 && state.cards['3'].wrong === 1), '|', await pg.textContent('#xferMsg'));
  await pg.click('#impBtn'); await pg.fill('#xferText', '{"nope":1}'); await pg.click('#impGo');
  console.log('bad import:', await pg.textContent('#xferMsg'));
  await pg.close();
  // service worker on the dist copy
  if (process.argv[2]) {
    const ctx = await b.newContext({ viewport: { width: 382, height: 580 } });
    pg = await ctx.newPage(); pg.on('pageerror', e => console.log('dist PAGEERROR', e.message));
    await pg.goto(process.argv[2]); await pg.waitForTimeout(1500);
    const reg = await pg.evaluate(async () => { const r = await navigator.serviceWorker.ready; return { scope: r.scope.replace(location.origin, ''), manifest: !!document.querySelector('link[rel=manifest]') }; });
    console.log('dist sw:', JSON.stringify(reg));
    for (let i = 0; i < 40; i++) { const n = await pg.evaluate(async () => { const c = await caches.open((await caches.keys())[0]); return (await c.keys()).length; }); if (n >= 173) { console.log('cache entries:', n); break; } await pg.waitForTimeout(1500); if (i === 39) console.log('cache entries (timeout):', n); }
    await ctx.setOffline(true);
    await pg.reload(); await pg.waitForTimeout(800);
    await pg.click('[data-tab="notebook"]'); await pg.evaluate(() => nbGo(140)); await pg.waitForTimeout(600);
    console.log('offline reload works:', await pg.evaluate(() => [...document.querySelectorAll('#nbStage img')].every(i => i.complete && i.naturalWidth > 0)), '| badge:', await pg.textContent('#syncBadge'));
    await ctx.close();
  }
  await b.close();
})().catch(e => { console.log('ERR', e.message); process.exit(1); });
