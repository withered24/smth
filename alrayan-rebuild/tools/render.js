// Renders the ar-* Shopify sections into standalone HTML pages, using the same JSON templates
// that ship to the store, so the preview and the store can't drift apart.
const fs = require('fs');
const path = require('path');
const { Liquid, Tag } = require('liquidjs');

const SHOP = '/home/user/smth/alrayan-rebuild/shopify';
const OUT = '/home/user/smth/alrayan-rebuild/html';
const LOGO = '/home/user/smth/alrayan-rebuild/logo';
const CDN = 'https://alrayanrings.net/cdn/shop/files/';
const HANDLE = 'elegant-metal-intelligent-rings-with-digital-display-vibration-alerts-precise-prayer-warning-for-islamic-prayer-trackings';
const PREVIEW_ROOT = process.argv[2] || '';  // '' → standalone; otherwise base for page links

// ---------- placeholder art (preview only) ----------
function placeholderSVG(label, kind) {
  const ring = `<g transform="translate(400 300)"><ellipse rx="150" ry="150" fill="none" stroke="#1F5A2E" stroke-width="44" opacity=".9"/><rect x="-62" y="-196" width="124" height="58" rx="12" fill="#14201A"/><text y="-157" text-anchor="middle" font-family="monospace" font-size="34" fill="#C9A455">0033</text></g>`;
  const arch = `<path d="M330 470V300a70 70 0 0 1 140 0v170" fill="none" stroke="#C9A455" stroke-width="2" opacity=".7"/>`;
  return `<svg class="ar-ph" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 800" preserveAspectRatio="xMidYMid slice" role="img" aria-label="${label || 'placeholder'}"><defs><linearGradient id="g${Math.random().toString(36).slice(2, 7)}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#F6F1E6"/><stop offset="1" stop-color="#E9E0CC"/></linearGradient></defs><rect width="800" height="800" fill="#EFE8D8"/>${kind === 'product' ? ring : arch}<text x="400" y="${kind === 'product' ? 560 : 540}" text-anchor="middle" font-family="Inter, sans-serif" font-size="20" fill="#56615A">${label || ''}</text></svg>`;
}

// ---------- mock objects ----------
function image(ref, alt) {
  const file = ref.replace('shopify://shop_images/', '');
  return { file, src: CDN + file, alt: alt || '', width: 1600, height: 1600, aspect_ratio: 1, toString() { return this.src; } };
}
let mid = 100;
function media(file, alt) { const im = image('shopify://shop_images/' + file, alt); return { id: ++mid, alt, preview_image: im, media_type: 'image' }; }
const MEDIA = [media('ADIKRING.png', 'Al Rayan Dhikr Ring 2.0 in black and rose gold'), media('ADIKR2.png', 'Ring display close-up'),
  media('Screenshot_2026-09-25_at_4.05.51_PM.png', 'Wearing the ring'), media('DIKRINGSIZES.png', 'Available sizes'),
  media('Screenshot_2026-09-25_at_4.17.48_PM.png', 'Ring on the commute'), media('Screenshot_2026-09-25_at_4.24.02_PM.png', 'Ring at work')];
const colors = ['Black', 'Rose Gold'], sizes = ['18mm', '20mm', '22mm'];
let vid = 4000;
const variants = [];
colors.forEach((c, ci) => sizes.forEach(s => variants.push({
  id: ++vid, title: `${c} / ${s} / CN`, options: [c, s, 'CN'], option1: c, option2: s, option3: 'CN',
  available: true, price: 4999, compare_at_price: null, featured_media: { id: MEDIA[ci === 0 ? 0 : 1].id },
})));
const PRODUCT = {
  id: 9001, handle: HANDLE, title: 'Al Rayan Dhikr Ring 2.0', url: '/products/' + HANDLE, price: 4999,
  media: MEDIA, featured_media: MEDIA[0], variants, has_only_default_variant: false,
  selected_or_first_available_variant: variants[1],
  options_with_values: [
    { name: 'Color', position: 1, values: colors, selected_value: 'Black' },
    { name: 'Size', position: 2, values: sizes, selected_value: '20mm' },
    { name: 'Ships From', position: 3, values: ['CN'], selected_value: 'CN' },
  ],
};
PRODUCT.selected_or_first_available_variant.featured_media = { id: MEDIA[0].id };

// ---------- liquid engine ----------
const engine = new Liquid({ root: [path.join(SHOP, 'sections'), path.join(SHOP, 'snippets')], extname: '.liquid', strictFilters: true });

engine.registerTag('schema', class extends Tag {
  constructor(token, remain, liquid) { super(token, remain, liquid); while (remain.length) { const t = remain.shift(); if (t.name === 'endschema') return; } }
  * render() { return ''; }
});
engine.registerTag('form', class extends Tag {
  constructor(token, remain, liquid) {
    super(token, remain, liquid);
    this.args = token.args; this.tpls = [];
    const stream = liquid.parser.parseStream(remain).on('tag:endform', () => stream.stop()).on('template', t => this.tpls.push(t)).on('end', () => { throw new Error('form not closed'); });
    stream.start();
  }
  * render(ctx, emitter) {
    const id = /id:\s*([\w]+)/.exec(this.args);
    const idVal = id ? yield this.liquid.evalValue(id[1], ctx) : 'product-form';
    const cls = /class:\s*'([^']+)'/.exec(this.args);
    emitter.write(`<form method="post" action="/cart/add" id="${idVal}" accept-charset="UTF-8" class="${cls ? cls[1] : ''}" enctype="multipart/form-data" novalidate><input type="hidden" name="form_type" value="product">`);
    ctx.push({ form: { id: idVal } });
    yield this.liquid.renderer.renderTemplates(this.tpls, ctx, emitter);
    ctx.pop();
    emitter.write('</form>');
  }
});

const money = c => (c == null || isNaN(c)) ? '' : '$' + (c / 100).toFixed(2).replace(/\B(?=(\d{3})+(?!\d))/g, ',');
engine.registerFilter('money', money);
engine.registerFilter('asset_url', n => n);
engine.registerFilter('stylesheet_tag', () => '');
engine.registerFilter('handleize', s => String(s || '').toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, ''));
engine.registerFilter('image_url', (im, ...args) => { if (!im) return ''; const src = im.src || String(im); return src; });
engine.registerFilter('image_tag', (src, ...args) => {
  const o = {}; for (const a of args) if (Array.isArray(a)) o[a[0]] = a[1];
  return `<img src="${src}" alt="${o.alt || ''}" loading="${o.loading || 'lazy'}" sizes="${o.sizes || '100vw'}" class="${o.class || ''}" width="1600" height="1600">`;
});
engine.registerFilter('placeholder_svg_tag', (name, cls) => placeholderSVG('Choose an image', String(name).startsWith('product') ? 'product' : 'life'));
engine.registerFilter('payment_button', () => `<div class="shopify-payment-button"><button type="button" class="shopify-payment-button__button" style="width:100%;min-height:54px;border:0;border-radius:999px;background:#5a31f4;color:#fff;font:600 16px Inter,sans-serif">Buy with <b>Shop</b>Pay</button><p class="shopify-payment-button__more-options" style="text-align:center;margin-top:8px">More payment options</p></div>`);
engine.registerFilter('structured_data', () => '{}');

// ---------- page assembly ----------
function resolveSettings(settings) {
  const out = {};
  for (const [k, v] of Object.entries(settings || {})) {
    if (typeof v === 'string' && v.startsWith('shopify://shop_images/')) out[k] = image(v);
    else if (k === 'product' && v) out[k] = PRODUCT;
    else out[k] = v;
  }
  return out;
}

async function renderPage(templateFile, isProduct) {
  const tpl = JSON.parse(fs.readFileSync(path.join(SHOP, 'templates', templateFile), 'utf8'));
  let html = '';
  for (const key of tpl.order) {
    const entry = tpl.sections[key];
    const blocks = (entry.block_order || []).map(id => ({ id, type: entry.blocks[id].type, settings: resolveSettings(entry.blocks[id].settings), shopify_attributes: '' }));
    const ctx = {
      section: { id: key, settings: resolveSettings(entry.settings), blocks },
      product: isProduct ? PRODUCT : null,
      shop: { money_format: '${{amount}}' },
      routes: { all_products_collection_url: '/collections/all' },
      template: { name: isProduct ? 'product' : 'index' },
    };
    const src = fs.readFileSync(path.join(SHOP, 'sections', entry.type + '.liquid'), 'utf8');
    const out = await engine.parseAndRender(src, ctx);
    html += `\n<div id="shopify-section-${key}" class="shopify-section">${out}</div>\n`;
  }
  return html.replace(/<script src="ar-rayan\.js" defer><\/script>/g, '');
}

const svg = f => fs.readFileSync(path.join(LOGO, f), 'utf8').replace(/ width="\d+" height="\d+"/, '').trim();
const css = fs.readFileSync(path.join(SHOP, 'assets/ar-rayan.css'), 'utf8');
const js = fs.readFileSync(path.join(SHOP, 'assets/ar-rayan.js'), 'utf8');

const FRAME_CSS = `
body{margin:0;background:#fff}
.arx-bar{background:#14201A;color:#F6F1E6;text-align:center;font:500 13px/1 Inter,sans-serif;letter-spacing:.04em;padding:11px 16px}
.arx-bar b{color:#C9A455;font-weight:600}
.arx-head{position:sticky;top:0;z-index:40;background:rgba(255,255,255,.96);backdrop-filter:blur(8px);border-bottom:1px solid #E4DCCB}
.arx-head__in{max-width:1200px;margin:0 auto;padding:0 20px;height:76px;display:grid;grid-template-columns:1fr auto 1fr;align-items:center}
.arx-nav{display:flex;gap:28px;font:500 14.5px Inter,sans-serif}
.arx-nav a{color:#14201A;text-decoration:none}
.arx-logo svg{height:52px;width:auto;display:block}
.arx-icons{justify-self:end;display:flex;gap:18px;color:#14201A}
.arx-icons svg{width:22px;height:22px;stroke:currentColor;fill:none;stroke-width:1.6}
.arx-foot{background:#163F21;color:#F6F1E6;font:14px/1.6 Inter,sans-serif}
.arx-foot__in{max-width:1200px;margin:0 auto;padding:64px 20px 28px;display:grid;grid-template-columns:1.4fr 1fr 1fr 1.4fr;gap:40px}
.arx-foot h4{font:600 12px Inter,sans-serif;letter-spacing:.14em;text-transform:uppercase;color:#C9A455;margin:0 0 14px}
.arx-foot ul{list-style:none;margin:0;padding:0;display:grid;gap:8px}
.arx-foot a{color:rgba(246,241,230,.82);text-decoration:none}
.arx-foot__logo svg{height:64px;width:auto}
.arx-foot p{color:rgba(246,241,230,.7);margin:14px 0 0;max-width:300px}
.arx-news{display:flex;gap:8px;margin-top:14px}
.arx-news input{flex:1;min-width:0;height:46px;border-radius:999px;border:1px solid rgba(246,241,230,.3);background:transparent;color:#F6F1E6;padding:0 18px;font:14px Inter,sans-serif}
.arx-news button{height:46px;padding:0 20px;border-radius:999px;border:0;background:#C9A455;color:#14201A;font:600 14px Inter,sans-serif}
.arx-legal{max-width:1200px;margin:0 auto;padding:20px;border-top:1px solid rgba(246,241,230,.14);display:flex;justify-content:space-between;flex-wrap:wrap;gap:12px;font-size:12.5px;color:rgba(246,241,230,.6)}
@media(max-width:849px){.arx-nav{display:none}.arx-head__in{grid-template-columns:auto 1fr;height:64px}.arx-logo svg{height:40px}.arx-foot__in{grid-template-columns:1fr 1fr}.arx-foot__brand,.arx-foot__news{grid-column:1/-1}}
`;
const PREVIEW_JS = `
// preview only: when a store image can't load here, show a labelled placeholder instead
document.querySelectorAll('img').forEach(function(img){
  img.loading='eager';
  function swap(){ if(img.dataset.ph) return; img.dataset.ph=1; var f=(img.getAttribute('src')||'').split('/').pop().split('?')[0];
    var s=${JSON.stringify(placeholderSVG('__F__', 'life'))}.split('__F__').join(decodeURIComponent(f).slice(0,40));
    img.src='data:image/svg+xml;charset=utf-8,'+encodeURIComponent(s.replace('class="ar-ph" ',''));
    img.removeAttribute('srcset'); }
  if(img.complete && img.naturalWidth===0) swap(); img.addEventListener('error', swap);
});
document.querySelectorAll('form[action="/cart/add"]').forEach(function(f){ f.addEventListener('submit', function(e){ e.preventDefault(); alert('Preview: this adds variant ' + f.querySelector('[name=id]').value + ' to the cart in Shopify.'); }); });
`;

function frame(title, desc, body, current) {
  const home = PREVIEW_ROOT + 'index.html', prod = PREVIEW_ROOT + 'product.html';
  return `<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>${title}</title>
<meta name="description" content="${desc}">
<link rel="icon" href="data:image/svg+xml,${encodeURIComponent(svg('al-rayan-app-icon.svg'))}">
<style>${css}
${FRAME_CSS}</style>
</head>
<body>
<div class="arx-bar">Free US shipping <b>·</b> 60-day money-back guarantee <b>·</b> 1-year warranty</div>
<header class="arx-head"><div class="arx-head__in">
  <nav class="arx-nav"><a href="${home}">Home</a><a href="${prod}">Shop</a><a href="${home}#faq">FAQ</a><a href="#contact">Contact</a></nav>
  <a class="arx-logo" href="${home}" aria-label="Al Rayan Rings home">${svg('al-rayan-logo-horizontal.svg')}</a>
  <div class="arx-icons"><svg viewBox="0 0 24 24"><circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/></svg><svg viewBox="0 0 24 24"><circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/></svg><svg viewBox="0 0 24 24"><path d="M5 8h14l-1 12H6zM9 8V6a3 3 0 0 1 6 0v2"/></svg></div>
</div></header>
<main>${body}</main>
<footer class="arx-foot" id="contact"><div class="arx-foot__in">
  <div class="arx-foot__brand"><span class="arx-foot__logo">${svg('al-rayan-logo-horizontal-reversed.svg').replace('<rect width', '<rect fill-opacity="0" width')}</span><p>Smart dhikr rings that help Muslims keep their remembrance close, wherever the day goes.</p></div>
  <div><h4>Shop</h4><ul><li><a href="${prod}">Dhikr Ring 2.0</a></li><li><a href="${home}#reviews">Reviews</a></li><li><a href="${home}#faq">FAQ</a></li></ul></div>
  <div><h4>Help</h4><ul><li><a href="#">Contact us</a></li><li><a href="#">Shipping policy</a></li><li><a href="#">Refund policy</a></li><li><a href="#">Terms of service</a></li><li><a href="#">Privacy policy</a></li></ul></div>
  <div class="arx-foot__news"><h4>Notes from the Al Rayan studio</h4><p>Gentle reminders and new releases, a few times a month.</p><form class="arx-news" onsubmit="event.preventDefault()"><input type="email" placeholder="Your email" aria-label="Email"><button>Subscribe</button></form></div>
</div><div class="arx-legal"><span>© 2026 Al Rayan Rings</span><span>Secure checkout · Shop Pay · Apple Pay · Visa · Mastercard · PayPal</span></div></footer>
<script>${js}</script>
<script>${PREVIEW_JS}</script>
</body>
</html>`;
}

(async () => {
  fs.mkdirSync(OUT, { recursive: true });
  const home = await renderPage('index.json', false);
  fs.writeFileSync(path.join(OUT, 'index.html'), frame('Al Rayan Rings', 'Smart dhikr rings: silent counting, gentle vibrations at 33, 66 and 99, and prayer-time alerts.', home));
  const prod = await renderPage('product.al-rayan.json', true);
  fs.writeFileSync(path.join(OUT, 'product.html'), frame('Al Rayan Dhikr Ring 2.0', 'The Al Rayan Dhikr Ring 2.0: a featherlight smart tasbih ring.', prod));
  console.log('ok', fs.statSync(path.join(OUT, 'index.html')).size, fs.statSync(path.join(OUT, 'product.html')).size);
})().catch(e => { console.error(e); process.exit(1); });
