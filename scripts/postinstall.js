// Postinstall: replace markdown-it-katex's bundled KaTeX 0.6.0 with modern KaTeX
// Must be a JS script (not shell) for cross-platform compatibility on CI
const { rmSync, cpSync, existsSync } = require('fs');
const src = 'node_modules/katex';
const dst = 'node_modules/markdown-it-katex/node_modules/katex';

if (!existsSync(src)) {
  console.warn('[postinstall] KaTeX not found at', src, '- skipping');
  process.exit(0);
}

if (existsSync(dst)) {
  rmSync(dst, { recursive: true, force: true });
  console.log('[postinstall] Removed ancient KaTeX from markdown-it-katex');
}

cpSync(src, dst, { recursive: true });
console.log('[postinstall] Copied modern KaTeX to markdown-it-katex');
