import { spawn, spawnSync } from 'node:child_process';
import { randomBytes } from 'node:crypto';
import { mkdirSync, mkdtempSync, readFileSync, rmSync, writeFileSync } from 'node:fs';
import { createServer } from 'node:net';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { setTimeout as delay } from 'node:timers/promises';
import { launchChrome } from './chrome-capture.mjs';

const root = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const args = process.argv.slice(2);
if (args.includes('--help')) {
  console.log('npm run screenshots [-- --desktop | --mobile]\nCaptures all public pages, published products, staff pages and result screens.\nRequires Node.js 22+, PHP 8.1+ and Chrome or Edge. No extra packages.');
  process.exit(0);
}
if (args.some(arg => !['--desktop', '--mobile'].includes(arg))) throw new Error('Unknown option. Use --help.');
const viewports = [
  { name: 'desktop', viewport: { width: 1440, height: 900 }, isMobile: false, hasTouch: false },
  { name: 'mobile', viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true },
].filter(({ name }) => !args.length || args.includes(`--${name}`));
const dateParts = new Intl.DateTimeFormat('en-GB', {
  timeZone: 'Asia/Colombo', year: 'numeric', month: '2-digit', day: '2-digit',
  hour: '2-digit', minute: '2-digit', second: '2-digit', hourCycle: 'h23',
}).formatToParts(new Date());
const part = name => dateParts.find(item => item.type === name).value;
const stamp = `${part('year')}-${part('month')}-${part('day')}_${part('hour')}-${part('minute')}-${part('second')}`;
const output = join(root, 'screenshots', stamp);
mkdirSync(join(root, '.cache'), { recursive: true });
const runtime = mkdtempSync(join(root, '.cache', 'screenshots-'));
const env = { ...process.env, FOREST_STORAGE_DIR: join(runtime, 'storage') };
const php = process.env.PHP_BINARY || 'php';
const phpOptions = ['-d', `xdebug.log=${join(runtime, 'xdebug.log')}`, '-d', 'display_errors=0'];
const username = 'screenshot-demo';
const password = randomBytes(24).toString('hex');
const captures = [];
const failures = [];
let browser;
let server;
let serverError;
let serverLog = '';

async function availablePort() {
  const listener = createServer();
  await new Promise((accept, reject) => { listener.once('error', reject); listener.listen(0, '127.0.0.1', accept); });
  const port = listener.address().port;
  await new Promise((accept, reject) => listener.close(error => error ? reject(error) : accept()));
  return port;
}

async function readyForCapture(page) {
  await page.evaluate(async () => {
    document.querySelectorAll('img').forEach(image => { image.loading = 'eager'; });
    await Promise.race([
      Promise.all([
        document.fonts.ready,
        ...[...document.images].map(image => image.decode().catch(() => {})),
      ]),
      new Promise(accept => setTimeout(accept, 15000)),
    ]);
    window.scrollTo(0, 0);
    const style = document.createElement('style');
    style.textContent = 'html{scroll-behavior:auto!important}*,*::before,*::after{animation:none!important;transition:none!important;caret-color:transparent!important}.scroll-reveal{opacity:1!important;transform:none!important}';
    document.head.append(style);
  });
  await delay(200);
}

const escapeHtml = value => String(value).replace(/[&<>"']/g, char => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[char]));

function writeGallery() {
  writeFileSync(join(output, 'manifest.json'), JSON.stringify({
    capturedAt: new Date().toISOString(), timezone: 'Asia/Colombo',
    content: 'Current public catalog/settings; isolated demo staff account and inquiries.',
    screenshots: captures, failures,
  }, null, 2));
  const groups = viewports.map(({ name }) => `<h2>${name}</h2><div class="grid">${captures.filter(item => item.viewport === name).map(item => `<a href="${escapeHtml(item.file)}" target="_blank" rel="noopener"><img src="${escapeHtml(item.file)}" loading="lazy" alt="${escapeHtml(item.name)}"><strong>${escapeHtml(item.name)}</strong><span>${item.width} × ${item.height}</span>${item.brokenImages.length ? '<span>Some images could not load; see manifest.</span>' : ''}</a>`).join('')}</div>`).join('');
  writeFileSync(join(output, 'index.html'), `<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>FOREST LANKA screenshots</title><style>body{margin:32px;font:16px system-ui;background:#f3f6f4;color:#163d2a}h1{margin-bottom:8px}.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:20px}a{display:block;background:white;border-radius:12px;overflow:hidden;color:inherit;text-decoration:none;border:1px solid #d9e4de}img{display:block;width:100%;height:280px;object-fit:cover;object-position:top;border-bottom:1px solid #d9e4de}strong,span{display:block;margin:10px 12px}span{font-size:13px;color:#52675b}</style><h1>FOREST LANKA screenshots</h1><p>${captures.length} full-page PNGs · ${stamp} (Asia/Colombo). Click a preview to open the complete image.</p><p>Current public content. Staff screens contain demo customer data.</p>${failures.length ? `<p>${failures.length} captures failed. See manifest.json.</p>` : ''}${groups}</html>`);
}

try {
  const fixture = spawnSync(php, [...phpOptions, join(root, 'tools/screenshot-fixture.php')], {
    cwd: root, env, windowsHide: true, encoding: 'utf8',
    input: JSON.stringify({ username, password, sourceStorage: resolve(process.env.FOREST_STORAGE_DIR || join(root, 'storage')) }),
  });
  if (fixture.error) throw new Error(`PHP could not start: ${fixture.error.message}. Put PHP on PATH or set PHP_BINARY.`);
  if (fixture.status !== 0) throw new Error(`Screenshot data setup failed: ${fixture.stderr || fixture.stdout}`);
  const data = JSON.parse(fixture.stdout);
  const port = await availablePort();
  const baseURL = `http://127.0.0.1:${port}/`;
  server = spawn(php, [...phpOptions, '-S', `127.0.0.1:${port}`, '-t', root, join(root, 'router.php')], {
    cwd: root, env, windowsHide: true, stdio: ['ignore', 'ignore', 'pipe'],
  });
  server.on('error', error => { serverError = error; });
  server.stderr.on('data', chunk => { serverLog = (serverLog + chunk).slice(-4000); });
  let ready = false;
  for (let attempt = 0; attempt < 40; attempt++) {
    if (serverError || server.exitCode !== null) throw new Error(`PHP server failed: ${serverError?.message || serverLog}`);
    try { if ((await fetch(`${baseURL}index.php`, { signal: AbortSignal.timeout(1000) })).ok) { ready = true; break; } }
    catch { /* Wait briefly for PHP to bind its port. */ }
    await delay(200);
  }
  if (!ready) throw new Error(`PHP server did not become ready. ${serverLog}`);
  browser = await launchChrome(runtime);
  mkdirSync(output, { recursive: true });
  const pages = Object.keys(JSON.parse(readFileSync(join(root, 'data/pages.json'), 'utf8')));
  const publicRoutes = pages.map(name => ({ name, route: `${name}.php` }));
  publicRoutes.push(...data.products.map(sku => ({ name: `product-${sku.toLowerCase()}`, route: `product.php?sku=${encodeURIComponent(sku)}` })));
  publicRoutes.push({ name: '404', route: 'page-not-found-screenshot', status: 404 });
  const staffRoutes = [
    { name: 'admin-dashboard', route: 'admin/' },
    { name: 'admin-request', route: `admin/?id=${data.requestId}` },
    { name: 'admin-catalog', route: 'admin/catalog.php' },
    { name: 'admin-product-new', route: 'admin/catalog.php?new=1' },
    ...(data.products.length ? [{ name: 'admin-product-edit', route: `admin/catalog.php?sku=${encodeURIComponent(data.products[0])}` }] : []),
    { name: 'admin-industries', route: 'admin/industries.php' },
    { name: 'admin-site', route: 'admin/site.php' },
  ];

  for (const profile of viewports) {
    const { name: viewport, ...contextOptions } = profile;
    const page = await browser.newPage(contextOptions);
    mkdirSync(join(output, viewport), { recursive: true });

    async function capture({ name, route, status = 200 }, navigate = true) {
      try {
        page.errors.length = 0;
        if (navigate) {
          const response = await page.goto(new URL(route, baseURL).href);
          if (response.status !== status) throw new Error(`HTTP ${response.status}, expected ${status}`);
          if (response.url !== new URL(route, baseURL).href) throw new Error(`Unexpected redirect to ${response.url}`);
        }
        await readyForCapture(page);
        const brokenImages = await page.evaluate(() => [...document.images].filter(image => image.currentSrc && image.naturalWidth === 0).map(image => image.currentSrc));
        const file = `${viewport}/${name}.png`;
        const dimensions = await page.screenshot(join(output, file));
        captures.push({ name, viewport, route, file, ...dimensions, brokenImages, pageErrors: [...page.errors] });
        console.log(`Saved ${file}${brokenImages.length ? ` (${brokenImages.length} unloaded images)` : ''}`);
      } catch (error) {
        failures.push({ name, viewport, route, error: error.message });
        console.error(`Failed ${viewport}/${name}: ${error.message}`);
      }
    }

    for (const route of publicRoutes) await capture(route);
    for (const invalid of [false, true]) {
      await page.goto(`${baseURL}contact.php`);
      const result = await page.submit(invalid => {
          const values = Object.fromEntries(new FormData(document.querySelector('form[data-inquiry="contact"]')));
          Object.assign(values, { name: 'Demo Customer', company: 'Demo Company', country: 'Sri Lanka', email: 'demo@example.test', phone: '+94712345678', inquiry_type: 'other', industry: 'ind_poultry', message: 'Sample inquiry for website screenshots only.', consent: '1' });
          if (invalid) values.csrf_token = 'screenshot-invalid-token';
          const form = document.createElement('form');
          form.method = 'post'; form.action = 'api/inquiries.php';
          for (const [name, value] of Object.entries(values)) {
            const input = document.createElement('input'); input.type = 'hidden'; input.name = name; input.value = value; form.append(input);
          }
          document.body.append(form); form.submit();
        }, invalid);
      const expectedHeading = invalid ? 'Please check your request.' : 'Thank you. Your request is saved.';
      if (result.url !== `${baseURL}request-result.php` || await page.evaluate(() => document.querySelector('h1')?.textContent) !== expectedHeading) throw new Error('Form result screen did not render.');
      await capture({ name: invalid ? 'request-error' : 'request-success', route: 'request-result.php' }, false);
    }
    await capture({ name: 'admin-login', route: 'admin/' });
    await page.submit(({ username, password }) => {
      document.querySelector('#username').value = username;
      document.querySelector('#password').value = password;
      document.querySelector('#username').form.submit();
    }, { username, password });
    if (await page.evaluate(() => document.querySelector('h1')?.textContent) !== 'Your inquiry desk') throw new Error('Demo staff login failed.');
    for (const route of staffRoutes) await capture(route);
    await page.close();
    writeGallery();
  }
  console.log(`\n${captures.length} full-page screenshots saved.\nGallery: ${join(output, 'index.html')}`);
  const warnings = captures.filter(item => item.brokenImages.length || item.pageErrors.length);
  if (warnings.length) console.warn(`${warnings.length} screenshots have asset or JavaScript warnings; see manifest.json.`);
  if (failures.length) process.exitCode = 1;
} catch (error) {
  console.error(error.message);
  if (captures.length) writeGallery();
  process.exitCode = 1;
} finally {
  await browser?.close();
  if (server && server.exitCode === null && !serverError) {
    const closed = new Promise(accept => server.once('close', accept));
    server.kill();
    await closed;
  }
  // runtime is always generated by mkdtemp inside this project's .cache directory.
  rmSync(runtime, { recursive: true, force: true, maxRetries: 5, retryDelay: 200 });
}
