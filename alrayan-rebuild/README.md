# Al Rayan Rings: site rebuild (V1)

## What's here

| Path | What it is |
|---|---|
| `html/index.html`, `html/product.html` | The two full pages as standalone HTML. Open them in a browser. Images load from your store's CDN (`alrayanrings.net/cdn/shop/files/…`); any that can't load show a labelled placeholder. |
| `shopify/sections/ar-*.liquid` | 13 Shopify sections, each fully editable in the theme editor (text, images, blocks, colours). |
| `shopify/snippets/ar-*.liquid` | 4 shared snippets (icons, stars, images, asset loader). |
| `shopify/assets/ar-rayan.css`, `ar-rayan.js` | Shared styles and behaviour. Everything is scoped under `.ar`, so it won't affect the rest of your theme. |
| `shopify/templates/index.json`, `product.al-rayan.json` | The two page layouts, pre-filled with your existing image files. |
| `al-rayan-theme-upload.zip` | Your current theme with all of the above already added. **This is the easiest way to install.** |
| `logo/` | Your logo set as SVG and transparent PNG (horizontal, stacked, reversed, mark, app icon). |
| `screenshots/` | Desktop and mobile captures of both pages. |

## Install: Option A (recommended, about 5 minutes)

1. Shopify admin → **Online Store → Themes → Add theme → Upload zip file** → choose `al-rayan-theme-upload.zip`.
   It uploads as a new, **unpublished** copy, so your live store doesn't change.
2. Click **Customize** on the new theme and check the home page and the ring's product page.
   The product page is applied to the template your ring already uses (`product.elegant-metal-…`).
3. In **Theme settings → Logo**, upload `logo/al-rayan-logo-horizontal.png` (or the `.svg`).
4. Update the **announcement bar** text in the header to: `Free US shipping · 60-day money-back guarantee`.
5. Under **Settings → Policies**, make sure the Refund and Shipping policies match the 60-day guarantee, then add them to the footer menu.
6. Preview everything on your phone, then click **Publish**.

## Install: Option B (add to your current theme by hand)

1. **Duplicate your live theme first** (Themes → ⋯ → Duplicate).
2. On the copy, go to **Edit code** and create each file with the same name, pasting in its contents:
   - Assets: `ar-rayan.css`, `ar-rayan.js`
   - Snippets: `ar-assets`, `ar-icon`, `ar-image`, `ar-stars`
   - Sections: all 13 `ar-*` files
3. Then either:
   - paste `templates/index.json` over your home template and create a product template from `product.al-rayan.json`, or
   - open **Customize** → **Add section** and add the "AR · …" sections wherever you want them.

## Sections

| Section | Used on |
|---|---|
| AR · Hero | Home |
| AR · Trust bar | Home, Product |
| AR · Intention (problem + hadith) | Home |
| AR · Moments (commute / work / home) | Home |
| AR · Features (+ spec strip) | Home, Product |
| AR · How it works | Product |
| AR · Comparison | Home, Product |
| AR · Reviews | Home, Product |
| AR · Founder story | Home |
| AR · Guarantee (60 days) | Home, Product |
| AR · FAQ (+ FAQ rich-results data) | Home, Product |
| AR · Final call to action | Home, Product |
| AR · Product (gallery, variant picker, size guide, sticky add-to-cart) | Product |

## Product section notes

- The **"Ships From"** option is hidden from shoppers (setting: *Hide these options*); its first value is used automatically.
- Size buttons show "US 8 / 10 / 12" hints (setting: *Size hints*).
- The size guide opens from the Size option and uses your `DIKRINGSIZES.png` chart plus a measurement table.
- Express checkout (Shop Pay / Apple Pay) and the sticky add-to-cart bar can each be switched off.

## Things to confirm before publishing

- **Delivery time:** the old site said both "3–5 business days from Chicago/Phoenix" and "10–15 days", and the variant says "Ships from CN". The new pages only promise *free US shipping*. Add a delivery estimate once you've settled on one.
- **"Getting started" and "Specifications"** accordions on the product page: check these match the ring exactly (for example, the alloy finish).
- **Reviews:** the six testimonials are carried over from your current site. Tick "Verified buyer" only on reviews from real orders. Your Forge reviews app block can still be added below the product section if you want live reviews.
- **Founder section:** a real photo of you, or your hands with the ring, will do more than a stock image.
- The "Every purchase supports Islamic education initiatives" banner was left out. Add it back only if it's an active programme.
