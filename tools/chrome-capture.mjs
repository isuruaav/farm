// Small Chrome DevTools Protocol client. Uses Node's built-in WebSocket;
// no browser package or browser download is needed.
import { spawn } from 'node:child_process';
import { existsSync, readFileSync, writeFileSync } from 'node:fs';
import { join } from 'node:path';
import { setTimeout as delay } from 'node:timers/promises';

export async function launchChrome(runtime) {
  if (!globalThis.WebSocket) throw new Error('Screenshot capture needs Node.js 22 or newer.');
  const candidates = [
    process.env.SCREENSHOT_BROWSER,
    join(process.env.ProgramFiles || 'C:/Program Files', 'Google/Chrome/Application/chrome.exe'),
    join(process.env['ProgramFiles(x86)'] || 'C:/Program Files (x86)', 'Microsoft/Edge/Application/msedge.exe'),
    join(process.env.LOCALAPPDATA || '', 'Google/Chrome/Application/chrome.exe'),
    '/usr/bin/google-chrome', '/usr/bin/chromium', '/usr/bin/chromium-browser',
    '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
  ];
  const executable = candidates.find(candidate => candidate && existsSync(candidate));
  if (!executable) throw new Error('Install Chrome/Edge, or set SCREENSHOT_BROWSER to its executable path.');
  const profile = join(runtime, 'browser');
  const child = spawn(executable, [
    '--headless=new', '--remote-debugging-port=0', '--remote-debugging-address=127.0.0.1',
    `--user-data-dir=${profile}`, '--no-first-run', '--no-default-browser-check',
    '--disable-background-networking', '--hide-scrollbars', 'about:blank',
  ], { windowsHide: true, stdio: ['ignore', 'ignore', 'pipe'] });
  let startError;
  let log = '';
  child.on('error', error => { startError = error; });
  child.stderr.on('data', chunk => { log = (log + chunk).slice(-4000); });
  let client;
  try {
    let endpoint;
    for (let attempt = 0; attempt < 100; attempt++) {
      if (startError || child.exitCode !== null) throw new Error(`Browser could not start: ${startError?.message || log}`);
      const activePort = join(profile, 'DevToolsActivePort');
      if (existsSync(activePort)) {
        const [port, path] = readFileSync(activePort, 'utf8').trim().split(/\r?\n/);
        if (port && path) { endpoint = `ws://127.0.0.1:${port}${path}`; break; }
      }
      await delay(100);
    }
    if (!endpoint) throw new Error(`Browser did not open its capture connection. ${log}`);
    client = await Protocol.connect(endpoint);
    return {
      async newPage(options) {
        const { browserContextId } = await client.send('Target.createBrowserContext');
        const { targetId } = await client.send('Target.createTarget', { url: 'about:blank', browserContextId });
        const { sessionId } = await client.send('Target.attachToTarget', { targetId, flatten: true });
        const page = new CapturePage(client, sessionId, browserContextId);
        await page.send('Page.enable');
        await page.send('Network.enable');
        await page.send('Runtime.enable');
        await page.send('Emulation.setDeviceMetricsOverride', { ...options.viewport, deviceScaleFactor: 1, mobile: options.isMobile });
        await page.send('Emulation.setTouchEmulationEnabled', { enabled: options.hasTouch });
        await page.send('Emulation.setEmulatedMedia', { features: [{ name: 'prefers-reduced-motion', value: 'reduce' }] });
        await page.send('Emulation.setTimezoneOverride', { timezoneId: 'Asia/Colombo' });
        return page;
      },
      async close() {
        const exited = child.exitCode === null ? new Promise(accept => child.once('exit', accept)) : Promise.resolve();
        await client.send('Browser.close').catch(() => {});
        await Promise.race([exited, delay(3000)]);
        if (child.exitCode === null) { child.kill(); await exited; }
        client.socket.close();
      },
    };
  } catch (error) {
    client?.socket.close();
    if (child.exitCode === null && !startError) child.kill();
    throw error;
  }
}

class Protocol {
  static async connect(endpoint) {
    const socket = new WebSocket(endpoint);
    await new Promise((accept, reject) => {
      socket.addEventListener('open', accept, { once: true });
      socket.addEventListener('error', () => reject(new Error('Browser capture connection failed.')), { once: true });
    });
    return new Protocol(socket);
  }
  constructor(socket) {
    this.socket = socket; this.nextId = 0; this.pending = new Map(); this.listeners = new Set();
    socket.addEventListener('message', event => {
      const message = JSON.parse(event.data);
      if (message.id) {
        const request = this.pending.get(message.id);
        if (!request) return;
        clearTimeout(request.timer); this.pending.delete(message.id);
        if (message.error) request.reject(new Error(message.error.message));
        else request.accept(message.result);
      } else this.listeners.forEach(listener => listener(message));
    });
    socket.addEventListener('close', event => {
      this.pending.forEach(request => { clearTimeout(request.timer); request.reject(new Error(`Browser capture connection closed (${event.code}${event.reason ? `: ${event.reason}` : ''}).`)); });
      this.pending.clear();
    });
  }
  send(method, params = {}, sessionId) {
    if (this.socket.readyState !== WebSocket.OPEN) return Promise.reject(new Error('Browser capture connection is no longer open.'));
    const id = ++this.nextId;
    return new Promise((accept, reject) => {
      const timer = setTimeout(() => { this.pending.delete(id); reject(new Error(`${method} timed out.`)); }, 30000);
      this.pending.set(id, { accept, reject, timer });
      this.socket.send(JSON.stringify({ id, method, params, ...(sessionId ? { sessionId } : {}) }));
    });
  }
  waitFor(method, sessionId) {
    let listener;
    let timer;
    const cancel = () => { clearTimeout(timer); this.listeners.delete(listener); };
    const promise = new Promise((accept, reject) => {
      listener = event => { if (event.method === method && event.sessionId === sessionId) { cancel(); accept(event.params); } };
      timer = setTimeout(() => { cancel(); reject(new Error(`${method} timed out.`)); }, 30000);
      this.listeners.add(listener);
    });
    return { promise, cancel };
  }
}

class CapturePage {
  constructor(client, sessionId, contextId) {
    this.client = client; this.sessionId = sessionId; this.contextId = contextId; this.errors = []; this.status = 0;
    this.listener = event => {
      if (event.sessionId !== sessionId) return;
      if (event.method === 'Network.responseReceived' && event.params.type === 'Document') this.status = event.params.response.status;
      if (event.method === 'Runtime.exceptionThrown') this.errors.push(event.params.exceptionDetails.exception?.description || event.params.exceptionDetails.text);
    };
    client.listeners.add(this.listener);
  }
  send(method, params) { return this.client.send(method, params, this.sessionId); }
  async evaluate(fn, value) {
    const result = await this.send('Runtime.evaluate', { expression: `(${fn.toString()})(${JSON.stringify(value) ?? ''})`, returnByValue: true, awaitPromise: true, userGesture: true });
    if (result.exceptionDetails) throw new Error(result.exceptionDetails.exception?.description || result.exceptionDetails.text);
    return result.result.value;
  }
  async navigation(action) {
    const loaded = this.client.waitFor('Page.domContentEventFired', this.sessionId);
    try { await action(); await loaded.promise; }
    finally { loaded.cancel(); }
    return { status: this.status, url: await this.evaluate(() => location.href) };
  }
  async goto(url) {
    return this.navigation(async () => {
      const result = await this.send('Page.navigate', { url });
      if (result.errorText) throw new Error(result.errorText);
    });
  }
  async submit(fn, value) { return this.navigation(() => this.evaluate(fn, value)); }
  async screenshot(path) {
    const { cssContentSize } = await this.send('Page.getLayoutMetrics');
    const result = await this.send('Page.captureScreenshot', {
      format: 'png', captureBeyondViewport: true, fromSurface: true,
      clip: { x: 0, y: 0, width: Math.ceil(cssContentSize.width), height: Math.ceil(cssContentSize.height), scale: 1 },
    });
    const png = Buffer.from(result.data, 'base64');
    writeFileSync(path, png);
    return { width: png.readUInt32BE(16), height: png.readUInt32BE(20) };
  }
  async close() {
    this.client.listeners.delete(this.listener);
    await this.client.send('Target.disposeBrowserContext', { browserContextId: this.contextId });
  }
}
