import { spawnSync } from 'node:child_process';
import { copyFileSync, cpSync, mkdirSync, readFileSync, renameSync, rmSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const packageJson = JSON.parse(readFileSync(join(root, 'package.json'), 'utf8'));
const tailwind = JSON.parse(readFileSync(join(root, 'node_modules/tailwindcss/package.json'), 'utf8'));
const cli = JSON.parse(readFileSync(join(root, 'node_modules/@tailwindcss/cli/package.json'), 'utf8'));
if (!tailwind.version.startsWith('4.') || tailwind.version !== packageJson.devDependencies.tailwindcss || cli.version !== tailwind.version) {
  throw new Error('Tailwind CSS and its v4 CLI must match package.json. Run npm ci.');
}

const output = join(root, 'assets/css/utilities.css');
const temporaryOutput = join(root, 'assets/css/utilities.build.css');
try {
  const result = spawnSync(process.execPath, [
    join(root, 'node_modules/@tailwindcss/cli/dist/index.mjs'),
    '-i', join(root, 'assets/css/tailwind-input.css'),
    '-o', temporaryOutput, '--minify'
  ], { cwd: root, stdio: 'inherit', windowsHide: true });
  if (result.error) throw result.error;
  if (result.status !== 0) throw new Error(`Tailwind compilation failed (${result.status}).`);

  const fontRoot = join(root, 'node_modules/@fortawesome/fontawesome-free');
  const vendor = join(root, 'assets/vendor/fontawesome');
  mkdirSync(join(vendor, 'css'), { recursive: true });
  copyFileSync(join(fontRoot, 'css/all.min.css'), join(vendor, 'css/all.min.css'));
  cpSync(join(fontRoot, 'webfonts'), join(vendor, 'webfonts'), { recursive: true });
  copyFileSync(join(fontRoot, 'LICENSE.txt'), join(vendor, 'LICENSE.txt'));

  // Publish the stylesheet only after compilation and asset copying both succeed.
  renameSync(temporaryOutput, output);
  console.log(`Built Tailwind CSS ${tailwind.version}, shared application styles and local icons.`);
} finally {
  rmSync(temporaryOutput, { force: true });
}
