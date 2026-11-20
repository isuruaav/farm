import assert from 'node:assert/strict';
import { readFileSync, readdirSync } from 'node:fs';
import { transform } from 'lightningcss';

const read = file => readFileSync(file, 'utf8');
const manifest = JSON.parse(read('package.json'));
const css = read('assets/css/utilities.css');
const expectedVersion = manifest.devDependencies.tailwindcss;
assert.ok(expectedVersion.startsWith('4.'), 'The project must use Tailwind CSS v4.');
assert.equal(manifest.devDependencies['@tailwindcss/cli'], expectedVersion);
assert.ok(css.includes(`tailwindcss v${expectedVersion}`), 'The compiled CSS is stale. Run npm run build.');
assert.doesNotMatch(css, /@(?:import|theme|source|tailwind)\b/, 'Uncompiled Tailwind directives in production CSS.');

const classes = new Set();
const layerStack = [];
const headingLayers = new Set();
const utilityLayers = new Map();
const layerOrder = [];
function collectClasses(node) {
  if (!node || typeof node !== 'object') return;
  if (node.type === 'class') classes.add(node.name);
  for (const value of Object.values(node)) {
    if (value && typeof value === 'object') {
      if (Array.isArray(value)) value.forEach(collectClasses);
      else collectClasses(value);
    }
  }
}
transform({
  code: Buffer.from(css),
  visitor: {
    Rule(rule) {
      if (rule.type === 'layer-block') {
        const name = rule.value.name.join('.');
        layerStack.push(name);
        layerOrder.push(name);
      }
      if (rule.type !== 'style') return;
      collectClasses(rule.value.selectors);
      for (const selector of rule.value.selectors) {
        if (selector.length === 1 && selector[0].type === 'type' && selector[0].name === 'h1') headingLayers.add(layerStack.at(-1));
        const ownClass = selector.find(part => part.type === 'class');
        if (ownClass) utilityLayers.set(ownClass.name, layerStack.at(-1));
        if (layerStack.at(-1) === 'components' && selector.some(part => part.type === 'type' && ['table','th','td'].includes(part.name))) {
          assert.ok(selector.some(part => part.type === 'class' && part.name === 'admin-body'), 'Staff table styling must not affect public tables.');
        }
      }
    },
    RuleExit(rule) { if (rule.type === 'layer-block') layerStack.pop(); }
  }
});
transform({ code: Buffer.from(read('assets/vendor/fontawesome/css/all.min.css')), visitor: {
  Rule(rule) { if (rule.type === 'style') collectClasses(rule.value.selectors); }
}});

assert.ok(layerOrder.indexOf('components') < layerOrder.indexOf('utilities'), 'Utility styles must override component defaults.');
assert.ok(headingLayers.has('components'), 'Branded heading styles must stay in the component layer.');
for (const utility of ['text-white','bg-forest','bg-gold','text-2xs','sm:grid-cols-2','lg:grid-cols-4','focus:ring-gold','shadow-xs']) {
  assert.equal(utilityLayers.get(utility), 'utilities', `Missing or incorrectly layered utility: ${utility}`);
}
for (const name of ['admin-body','request-detail','standalone-panel','scroll-reveal','is-pending','form-feedback','home-hero','industry-explorer','product-card','product-detail-layout','admin-tabs','editor-panel']) {
  assert.ok(classes.has(name), `Missing shared application style: ${name}`);
}

const hooks = new Set(['group','dynamic-inquiry-form','prod-cat-btn','gallery-filter-btn','product-item','gallery-item']);
const missing = new Map();
const used = new Set();
const templates = ['request-result.php'];
for (const folder of ['views','includes','admin']) {
  for (const file of readdirSync(folder).filter(file => file.endsWith('.php'))) templates.push(`${folder}/${file}`);
}
for (const file of templates) {
  const text = read(file).replace(/<\?[\s\S]*?(?:\?>|$)/g, '');
  for (const match of text.matchAll(/class="([^"]+)"/g)) {
    for (const name of match[1].split(/\s+/).filter(Boolean)) {
      used.add(name);
      if (!classes.has(name) && !hooks.has(name) && !name.endsWith('-')) missing.set(name, file);
    }
  }
}
assert.deepEqual([...missing], [], 'Some template classes are missing from the compiled CSS.');
for (const file of ['includes/header.php','admin/index.php','request-result.php']) {
  assert.match(read(file), /assets\/css\/utilities\.css\?v=4\./, `${file} must load the v4 application bundle.`);
  assert.doesNotMatch(read(file), /href="[^\"]*assets\/css\/(?:styles|admin)\.css/, `${file} must not bypass the CSS layers.`);
}
console.log(`PASS: Tailwind ${expectedVersion}; ${used.size} template classes, CSS layer order, responsive/brand utilities, staff/result pages and scroll animation styles.`);
