// Render tools/og.html to src/og.png at 1200x630. Run tools/share_image.py first.
const path = require('path');
const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1200, height: 630 } });
  await p.goto('file://' + path.join(__dirname, 'og.html'));
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(300);
  await p.screenshot({ path: path.join(__dirname, '..', 'src', 'og.png') });
  await b.close();
})();
