# ad_01 prompts — FINAL

## Swipe port — source: Yaqeen Books · 126182379 (analysis: C:/Users/rayan/OneDrive/Desktop/ADS/ad-runs/2026-10-05-al-rayan-dhikr-ring/02-creative-research/gethookd/yaqeen-books-126182379/analysis.md)

Brand context: palette below · font classes below · voice persona-styled first-person confession (no name, no stats) · avatar A1 discreet daily rememberer · product PNG C:/Users/rayan/OneDrive/Desktop/ADS/ad-runs/2026-10-05-al-rayan-dhikr-ring/00-intake/product_black.png

### Teardown (viewed media.jpg, 1638x2048, 4:5)
- Zones: full-bleed portrait photo, shot from above-left down a narrow kitchen counter. Lit phone bottom-centre (68-85% of height, brightest object, blue-white glow), mug centre (47-62%), cluttered counter and dish rack right (30-65%), warm under-cabinet light strip top right (15-30%), left 25% of frame near-black. Zero overlay text, no logo.
- Focal flow: 1 glowing phone -> 2 mug -> 3 cluttered counter -> 4 warm light top right. Gets the point in about 1 s ("someone alone, up late, on their phone").
- Palette (est.): shadows #0F0D0A (about 45%), counter #C9B98A, phone glow #DCEBFF, mug #4A4A48, light strip #F2D9A0.
- Style: native lo-fi phone photo, low light, grain, slight motion blur, tilted framing. No people. Product absent.
- Every visible string: none on the image. All words live in the primary text (first person, 1:14 AM story) and the headline field "I recited the Quran for 20 years without understanding it" (hook type: story-confession / curiosity inversion; visual device native_ui_spoof / in_media_res).
- Promise: "you were never doing it wrong, it is fixable in a tiny daily habit". Angle: hidden shame -> ease (primary), curiosity (secondary).

### Keep / swap / adapt / never
| Element | Swipe | Ours | Decision | Why |
|---|---|---|---|---|
| Layout grid | full-bleed night photo, lit phone as brightest object, dark left, warm light strip upper right | same grid: dark left, warm lamp upper right, lit phone as bright anchor, ring hand added | KEEP | load-bearing (native "friend's post" read) |
| Focal flow | phone -> mug -> clutter -> light | lit ring display/hand -> mug -> lamp -> dark phone (problem object now dark at the edge, per chief note) | ADAPT | product must be visible (swipe weakness: MG1 miss) |
| Image style / production | native lo-fi phone photo, grain, blur, tilt | same, amateur phone snap, no studio polish | KEEP | load-bearing |
| Camera | above-left, tilted, phone wide lens | same, slightly closer so the ring display reads | KEEP/ADAPT | ring is small |
| Setting | messy kitchen counter, 1 AM | bedside nightstand at night (brief: lo-fi night bedside, ring glowing); kitchen counter = V-scene | ADAPT | brief visual concept |
| Props | mug, cable, dish rack | mug of tea, charging cable, glasses case, crumpled deep-green throw | KEEP types | |
| Text on image | none | none; the only digits are the ring's own display "5332" (UI_TEXT_1, product's own, not an overlay) | KEEP (no overlay) | approved copy: hook lives in the Meta headline/primary text, as in the swipe |
| Hook structure | "I [pious thing] for [years] without [gap]" | frame `I counted dhikr for [time] and never [gap]` - copywriter owns words | KEEP frame, SWAP words | |
| Palette | #0F0D0A / #C9B98A / #DCEBFF | #0F0D0A shadow / amber lamp #E8B76A / phone glow #DCEBFF / brand green #1F5A2E throw / ring black #0B0B0C + gold #D9B96A | SWAP by role | brand |
| Product | none | Al Rayan Dhikr Ring 2.0 black via PNG reference, worn on a hand | SWAP | |
| People | none | one hand only, no face, no identity | KEEP (no face) | |
| Proof / stats / persona name / charity | 60,000 users, "500 words = 75%", Bilal, meal to Palestine | none | NEVER | TRUTH-RISK |

Load-bearing kept: raw dark phone photo, lit phone as brightest object, no studio feel, no polished graphics, scene implies a private late-night moment.
Truth replacements: swipe's stats/persona/charity dropped; proof slot filled with a plain product-in-use shot (ring display lit). No stars, badges, review counts. No faith claim on the image.
Variations planned: V-layout (mirror), V-scene (kitchen counter), V-format (1:1). V-copy is dropped: the approved copy has no on-image hook (the hook is the Meta headline, as in the swipe), so there is nothing on the image to swap.

## Brand context
- Palette: shadow #0F0D0A, amber lamp #E8B76A, brand green #1F5A2E (throw/mug only), ring black #0B0B0C + gold #D9B96A + white digits #FFFFFF (product's own). Fonts: none rendered (no overlay text). Product: black smart ring (not a bottle): glossy black wide flat alloy band, rectangular black glass display with four white 7-segment digits "5332", rounded-square panel with gold heart-shaped logo. PNG: C:/Users/rayan/OneDrive/Desktop/ADS/ad-runs/2026-10-05-al-rayan-dhikr-ring/00-intake/product_black.png

## Slot table (image)
| slot | role | max words | max chars | font | hex | zone % | size |
|---|---|---|---|---|---|---|---|
| UI_TEXT_1 | the ring's own lit display digits, exactly "5332" (approved copy_final) | 1 | 4 | white 7-segment digits on black glass (product's own) | #FFFFFF | ring display, 46-60% height, 44-78% width | display cap height 2.8% |
| HEADLINE / CTA_BUTTON | none on image (copy_final) | 0 | 0 | - | - | - | - |

Copy mapping: copy_final UI_TEXT_1 "5332" -> slot UI_TEXT_1 (1:1). Phone is dark, face down, at the edge (chief note v2); no text on it.

## Prompts
### img_main — nano_banana_pro · 9:16 · 2k · refs: @product
```text
Scene: A candid late-night snapshot of a bedside nightstand seen from above-left at a slight tilt. A relaxed adult right hand (no face, only wrist and a plain dark grey cotton pyjama sleeve) rests palm-down on the nightstand edge in the right-center of the frame. Exactly one ring is worn on the ring finger of that hand, its small digital display lit and glowing: it is the brightest and most important object. At the far left edge a smartphone lies face down and dark, with a white charging cable trailing from it. Behind the hand stand one ceramic mug of tea and one closed glasses case, soft and out of focus, and a small lamp base blurred at the upper right. A bunched deep-green fabric throw sits at the left edge. No people besides the one hand.

Style: Authentic amateur phone photo, native lo-fi UGC look, not a studio ad. Low-light grain, slight motion blur on the background, imperfect tilted framing, natural clutter. No graphic design elements, no borders, no filters.

Lighting: One small warm bedside lamp at the upper right, about 2400K, amber glow falling softly across the nightstand and the back of the hand. The ring display adds a crisp white glow on the finger. Deep near-black shadows (#0F0D0A) fill the left and top of the frame. Quiet, private, late-night mood.

Camera: Handheld phone at about 45 degrees from above-left, 26mm wide lens, close enough that the ring display reads clearly, background soft, ring and hand in focus.

Composition: Vertical 9:16 (tall portrait). Top 0-14%: only dark wall and shadow. The hand rests at 38-64% of frame height, wrist entering from the right edge; the ring sits at about 46-60% of frame height and 44-78% of frame width and is about 14% of frame height, display window facing the camera. Dark phone at the far left edge, 52-68% height, 0-18% width, cropped by the frame edge. Mug at 34-46% height, 30-44% width, out of focus. Lamp glow upper right at 14-30%. Below 66%: dark nightstand surface and cable only, nothing important. Focal flow: ring display first, then hand, then lamp glow, then the dark phone.

Brand colors: Shadows #0F0D0A. Lamp light amber #E8B76A. Throw blanket deep green #1F5A2E, muted in the dark. Ring black #0B0B0C with gold logo #D9B96A and white digits #FFFFFF. Phone dark #1A1A1C. No other saturated colors.

Product: Match the attached product reference image exactly: shape, label, colors, logo. Do not redesign, re-letter, simplify or recolor the label. Do not invent label text. The product is a smart ring: a glossy black wide flat metal band with a rectangular black glass display window showing four white seven-segment digits, and a smaller rounded-square panel holding a gold heart-shaped logo mark to the left of the display. Exactly one ring, worn on the ring finger, display and logo panel facing the camera within 25 degrees, fully visible, sharp, not covered by any finger, the phone or the mug. The display digits read as in the reference.

Text: Render exactly one text element, and it is the ring's own display, not an overlay: the lit display window shows the four digits "5332" in white seven-segment digits (#FFFFFF) on black glass, centered in the display window, exactly as in the product reference image, display cap height about 2.8% of frame height. There is no other text anywhere in the image: no text on the phone, no captions, no headline, no labels.

Legibility: The digits are spelled five, three, three, two: "5332", in that order, each digit fully visible, evenly spaced, not cut off, with a soft white glow. The ring's gold logo is a symbol, not letters. Render only the four display digits and the ring's logo; do not render section labels or any other words from these instructions.

Avoid: any text, words, letters or numbers other than the four ring display digits "5332"; text or UI on the phone screen; a visible face; a second ring or extra jewellery; misspelled, warped or duplicated digits; notification banners or app logos; Quran pages, calligraphy, religious symbols or prayer beads; star ratings, review counts, badges, seals, "clinically proven" claims; watermarks; other brand names or logos; extra fingers, fused or bent fingers, distorted hand; plastic CGI skin; studio lighting or glossy ad polish; any text in the top 14% or bottom 28% of the frame.
```

### img_v1 — nano_banana_pro · 9:16 · 2k · refs: @product
```text
Scene: A candid late-night snapshot of a bedside nightstand seen from above-left at a slight tilt. A relaxed adult left hand (no face, only wrist and a plain dark grey cotton pyjama sleeve) rests palm-down on the nightstand edge in the left-center of the frame. Exactly one ring is worn on the ring finger of that left hand, its small digital display lit and glowing: it is the brightest and most important object. At the far right edge a smartphone lies face down and dark, with a white charging cable trailing from it. Behind the hand stand one ceramic mug of tea and one closed glasses case, soft and out of focus, and a small lamp base blurred at the upper left. A bunched deep-green fabric throw sits at the right edge. No people besides the one hand.

Style: Authentic amateur phone photo, native lo-fi UGC look, not a studio ad. Low-light grain, slight motion blur on the background, imperfect tilted framing, natural clutter. No graphic design elements, no borders, no filters.

Lighting: One small warm bedside lamp at the upper left, about 2400K, amber glow falling softly across the nightstand and the back of the hand. The ring display adds a crisp white glow on the finger. Deep near-black shadows (#0F0D0A) fill the right and top of the frame. Quiet, private, late-night mood.

Camera: Handheld phone at about 45 degrees from above-left, 26mm wide lens, close enough that the ring display reads clearly, background soft, ring and hand in focus.

Composition: Vertical 9:16 (tall portrait). Top 0-14%: only dark wall and shadow. The hand rests at 38-64% of frame height, wrist entering from the left edge; the ring sits at about 46-60% of frame height and 22-56% of frame width and is about 14% of frame height, display window facing the camera. Dark phone at the far right edge, 52-68% height, 82-100% width, cropped by the frame edge. Mug at 34-46% height, 56-70% width, out of focus. Lamp glow upper left at 14-30%. Below 66%: dark nightstand surface and cable only, nothing important. Focal flow: ring display first, then hand, then lamp glow, then the dark phone.

Brand colors: Shadows #0F0D0A. Lamp light amber #E8B76A. Throw blanket deep green #1F5A2E, muted in the dark. Ring black #0B0B0C with gold logo #D9B96A and white digits #FFFFFF. Phone dark #1A1A1C. No other saturated colors.

Product: Match the attached product reference image exactly: shape, label, colors, logo. Do not redesign, re-letter, simplify or recolor the label. Do not invent label text. The product is a smart ring: a glossy black wide flat metal band with a rectangular black glass display window showing four white seven-segment digits, and a smaller rounded-square panel holding a gold heart-shaped logo mark to the left of the display. Exactly one ring, worn on the ring finger, display and logo panel facing the camera within 25 degrees, fully visible, sharp, not covered by any finger, the phone or the mug. The display digits read as in the reference.

Text: Render exactly one text element, and it is the ring's own display, not an overlay: the lit display window shows the four digits "5332" in white seven-segment digits (#FFFFFF) on black glass, centered in the display window, exactly as in the product reference image, display cap height about 2.8% of frame height. There is no other text anywhere in the image: no text on the phone, no captions, no headline, no labels.

Legibility: The digits are spelled five, three, three, two: "5332", in that order, each digit fully visible, evenly spaced, not cut off, with a soft white glow. The ring's gold logo is a symbol, not letters. Render only the four display digits and the ring's logo; do not render section labels or any other words from these instructions.

Avoid: any text, words, letters or numbers other than the four ring display digits "5332"; text or UI on the phone screen; a visible face; a second ring or extra jewellery; misspelled, warped or duplicated digits; notification banners or app logos; Quran pages, calligraphy, religious symbols or prayer beads; star ratings, review counts, badges, seals, "clinically proven" claims; watermarks; other brand names or logos; extra fingers, fused or bent fingers, distorted hand; plastic CGI skin; studio lighting or glossy ad polish; any text in the top 14% or bottom 28% of the frame.
```

### img_v2 — nano_banana_pro · 9:16 · 2k · refs: @product
```text
Scene: A candid late-night snapshot of a narrow kitchen counter seen from above-left at a slight tilt. A relaxed adult right hand (no face, only wrist and a plain dark grey sleeve) wraps around one ceramic mug of tea in the right-center of the frame, the ring on its ring finger with the small digital display lit and glowing and turned toward the camera: it is the brightest and most important object. At the lower left a smartphone lies face down and dark, with a white charging cable. Behind them a dish rack, a kettle and a small bottle, all soft and out of focus, with a warm under-cabinet light strip at the upper right. The counter is slightly messy with a few crumbs. No people besides the one hand.

Style: Authentic amateur phone photo, native lo-fi UGC look, not a studio ad. Low-light grain, slight motion blur on the background, imperfect tilted framing, natural clutter. No graphic design elements, no borders, no filters.

Lighting: A warm under-cabinet light strip at the upper right, about 2700K, amber glow across the counter and the back of the hand. The ring display adds a crisp white glow. Deep near-black shadows (#0F0D0A) fill the left and top of the frame. Quiet, private, one-in-the-morning mood.

Camera: Handheld phone at about 45 degrees from above-left, 26mm wide lens, close enough that the ring display reads clearly, background soft, ring and hand in focus.

Composition: Vertical 9:16 (tall portrait). Top 0-14%: only dark cabinet and shadow. The hand and mug rest at 36-64% of frame height, wrist entering from the right edge; the ring sits at about 44-58% of frame height and 44-78% of frame width and is about 14% of frame height, display window facing the camera, not hidden by the mug. Dark phone at 56-70% height, 6-30% width. Light strip glow at 14-30% upper right. Below 70%: dark counter and cable only, nothing important. Focal flow: ring display first, then hand and mug, then light strip, then the dark phone.

Brand colors: Shadows #0F0D0A. Under-cabinet light amber #E8B76A. Mug deep green #1F5A2E. Ring black #0B0B0C with gold logo #D9B96A and white digits #FFFFFF. Phone dark #1A1A1C. No other saturated colors.

Product: Match the attached product reference image exactly: shape, label, colors, logo. Do not redesign, re-letter, simplify or recolor the label. Do not invent label text. The product is a smart ring: a glossy black wide flat metal band with a rectangular black glass display window showing four white seven-segment digits, and a smaller rounded-square panel holding a gold heart-shaped logo mark to the left of the display. Exactly one ring, worn on the ring finger, display and logo panel facing the camera within 25 degrees, fully visible, sharp, not covered by any finger, the phone or the mug. The display digits read as in the reference.

Text: Render exactly one text element, and it is the ring's own display, not an overlay: the lit display window shows the four digits "5332" in white seven-segment digits (#FFFFFF) on black glass, centered in the display window, exactly as in the product reference image, display cap height about 2.8% of frame height. There is no other text anywhere in the image: no text on the phone, no captions, no headline, no labels.

Legibility: The digits are spelled five, three, three, two: "5332", in that order, each digit fully visible, evenly spaced, not cut off, with a soft white glow. The ring's gold logo is a symbol, not letters. Render only the four display digits and the ring's logo; do not render section labels or any other words from these instructions.

Avoid: any text, words, letters or numbers other than the four ring display digits "5332"; text or UI on the phone screen; a visible face; a second ring or extra jewellery; misspelled, warped or duplicated digits; notification banners or app logos; Quran pages, calligraphy, religious symbols or prayer beads; star ratings, review counts, badges, seals, "clinically proven" claims; watermarks; other brand names or logos; extra fingers, fused or bent fingers, distorted hand; plastic CGI skin; studio lighting or glossy ad polish; any text in the top 14% or bottom 28% of the frame.
```

### img_v3 — nano_banana_pro · 1:1 · 2k · refs: @product
```text
Scene: A candid late-night snapshot of a bedside nightstand seen from above-left at a slight tilt. A relaxed adult right hand (no face, only wrist and a plain dark grey cotton pyjama sleeve) rests palm-down on the nightstand edge in the right-center of the frame. Exactly one ring is worn on the ring finger of that hand, its small digital display lit and glowing: it is the brightest and most important object. At the far left edge a smartphone lies face down and dark, with a white charging cable trailing from it. Behind the hand stand one ceramic mug of tea and one closed glasses case, soft and out of focus, and a small lamp base blurred at the upper right. A bunched deep-green fabric throw sits at the left edge. No people besides the one hand.

Style: Authentic amateur phone photo, native lo-fi UGC look, not a studio ad. Low-light grain, slight motion blur on the background, imperfect tilted framing, natural clutter. No graphic design elements, no borders, no filters.

Lighting: One small warm bedside lamp at the upper right, about 2400K, amber glow falling softly across the nightstand and the back of the hand. The ring display adds a crisp white glow on the finger. Deep near-black shadows (#0F0D0A) fill the left and top of the frame. Quiet, private, late-night mood.

Camera: Handheld phone at about 45 degrees from above-left, 26mm wide lens, close enough that the ring display reads clearly, background soft, ring and hand in focus.

Composition: Square 1:1. Keep a 5% margin on every side, nothing important in the outer 5%. The hand rests at 34-78% of frame height, wrist entering from the right edge; the ring sits at about 46-68% of frame height and 42-80% of frame width and is about 17% of frame height, display window facing the camera. Dark phone at the far left edge, 54-76% height, 0-16% width, cropped by the frame edge. Mug at 28-42% height, 28-44% width, out of focus. Lamp glow upper right at 8-28%. Below 82%: dark nightstand surface and cable only. Focal flow: ring display first, then hand, then lamp glow, then the dark phone.

Brand colors: Shadows #0F0D0A. Lamp light amber #E8B76A. Throw blanket deep green #1F5A2E, muted in the dark. Ring black #0B0B0C with gold logo #D9B96A and white digits #FFFFFF. Phone dark #1A1A1C. No other saturated colors.

Product: Match the attached product reference image exactly: shape, label, colors, logo. Do not redesign, re-letter, simplify or recolor the label. Do not invent label text. The product is a smart ring: a glossy black wide flat metal band with a rectangular black glass display window showing four white seven-segment digits, and a smaller rounded-square panel holding a gold heart-shaped logo mark to the left of the display. Exactly one ring, worn on the ring finger, display and logo panel facing the camera within 25 degrees, fully visible, sharp, not covered by any finger, the phone or the mug. The display digits read as in the reference.

Text: Render exactly one text element, and it is the ring's own display, not an overlay: the lit display window shows the four digits "5332" in white seven-segment digits (#FFFFFF) on black glass, centered in the display window, exactly as in the product reference image, display cap height about 2.8% of frame height. There is no other text anywhere in the image: no text on the phone, no captions, no headline, no labels.

Legibility: The digits are spelled five, three, three, two: "5332", in that order, each digit fully visible, evenly spaced, not cut off, with a soft white glow. The ring's gold logo is a symbol, not letters. Render only the four display digits and the ring's logo; do not render section labels or any other words from these instructions.

Avoid: any text, words, letters or numbers other than the four ring display digits "5332"; text or UI on the phone screen; a visible face; a second ring or extra jewellery; misspelled, warped or duplicated digits; notification banners or app logos; Quran pages, calligraphy, religious symbols or prayer beads; star ratings, review counts, badges, seals, "clinically proven" claims; watermarks; other brand names or logos; extra fingers, fused or bent fingers, distorted hand; plastic CGI skin; studio lighting or glossy ad polish; any text near the frame edges.
```

## Variations
- img_v1 · V-layout: Mirror composition: left hand wears the ring, wrist from the left, dark phone at the right edge, lamp glow upper left, throw on the right.
- img_v2 · V-scene: Kitchen counter at night closer to the swipe: ring hand wrapped around a mug, dark phone lower left, under-cabinet light strip upper right.
- img_v3 · V-format: 1:1 feed re-layout of the main scene, ring larger (about 17% of frame height), 5% margins; no on-image hook exists, so V-copy has nothing to swap (alt hooks H2-H5 are Meta headline/primary-text tests).

## Budget
img_main 1 x 2.0 = 2.0 credits (variations excluded; 2.0 each if rendered, all 3 = 6.0).

## Self-check
On-image string "5332" verbatim in quotes in all 4 prompts; @product first in references; no slot markers or double braces; Avoid blocks name truth items; no competitor refs. Note: img_v3 is 1:1 (aspect_ratio param "1:1").
