import fs from 'node:fs';
import path from 'node:path';
import zlib from 'node:zlib';

const KEY = Buffer.from('EruvMapSecureProtection2026!@#');
const srcPath = path.resolve('data/eruvs.geojson');
const outDir = path.resolve('public/data');
const outPath = path.join(outDir, 'eruvs.bin');

if (!fs.existsSync(srcPath)) {
  console.error(`❌ Source file not found: ${srcPath}`);
  process.exit(1);
}

if (!fs.existsSync(outDir)) {
  fs.mkdirSync(outDir, { recursive: true });
}

const raw = fs.readFileSync(srcPath);
const compressed = zlib.deflateSync(raw, { level: 9 });

const masked = Buffer.alloc(compressed.length);
for (let i = 0; i < compressed.length; i++) {
  masked[i] = compressed[i] ^ KEY[i % KEY.length];
}

fs.writeFileSync(outPath, masked);

const originalMb = (raw.length / (1024 * 1024)).toFixed(2);
const obfuscatedKb = (masked.length / 1024).toFixed(1);
const reduction = (((raw.length - masked.length) / raw.length) * 100).toFixed(1);

console.log(
  `🔒 Obfuscated binary dataset generated: ${originalMb} MB -> ${obfuscatedKb} KB (-${reduction}%) at public/data/eruvs.bin`
);
