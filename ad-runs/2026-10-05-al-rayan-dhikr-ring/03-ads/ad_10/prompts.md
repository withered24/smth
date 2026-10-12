# ad_10 prompts — FINAL

## Swipe port — source: Calm Collective · 92336795 (analysis: C:/Users/rayan/OneDrive/Desktop/ADS/ad-runs/2026-10-05-al-rayan-dhikr-ring/02-creative-research/gethookd/calm-collective-92336795/analysis.md)

Brand context: see below. Avatar A1 (discreet daily rememberer). Angle ANG3 (never lose count). Hook type: micro-callout question. Product PNG: C:/Users/rayan/OneDrive/Desktop/ADS/ad-runs/2026-10-05-al-rayan-dhikr-ring/00-intake/product_rose_gold.png. Frames viewed: 3 images (swipe media.jpg, product PNG, store page screenshot) = 3.

### Teardown (swipe, viewed at full size; 1080x1080 square, ported to 9:16)
- Zones (square): brand wordmark 8-13% of height · headline 16-27% · ring stack 27-88% (left-centre, x 22-47% of width, tilted, levitating over a pale stone rising from lower-left) · six dotted-leader labels right (x 50-78%, y 31-85%, slightly rotated -4 to +8 degrees) · offer bar 91-100% (navy, full width).
- Focal flow: 1 headline (huge, black, heaviest weight) -> 2 levitating ring stack -> 3 labels top to bottom via dotted leaders -> 4 offer bar. Point gets across in under 1.5 s.
- Palette (est.): bg warm cream gradient #F0E6D6 -> #E9DCC8 (about 65%) · headline black #0A0A0A · labels navy #14214F · rings gold #D9A441 / silver #C9C9CC · bar navy #12214F with white text · stone #E8D9BF.
- Fonts: heavy geometric sans headline, Title/sentence case, ~20% of frame height block; humanist sans labels in navy, 1/4 of headline size; ALL CAPS regular sans in the bar; brand wordmark in a heavy rounded serif-like script (swap: ours is a plain clean sans wordmark).
- Visible strings (verbatim): "calm collective" / "A skin picker?" / "Instant anxiety relief" / "100% waterproof" / "Distracts your mind" / "Lifetime fidget guarantee" / "Rated 4.5 stars" / "Over 100,000 helped" / "FREE SHIPPING OVER £50".
- Hook: micro-callout question (3 words naming the avatar's own habit). Promise: calms an anxious hand habit. CTA: offer bar (free-shipping line). Angle: pain relief + ease; stat proof secondary.
- Style: polished studio render, soft top light, no people, no hands.

### Keep / swap / adapt / never
| Element | Swipe | Ours | Decision | Why |
|---|---|---|---|---|
| Layout grid | brand mark / headline / hero left / labels right / bar | same grid, compressed into 9:16 safe zone (14-65% text) | KEEP | load-bearing |
| Hook structure | "A skin picker?" (3-word behaviour callout question) | `[HEADLINE]` = short callout question naming the avatar's own habit (e.g. losing count; wording is the copywriter's, VOC Q29/Q02/Q01) | KEEP structure, SWAP words | load-bearing; legible <1 s |
| Hero | stack of six levitating rings over stone | ONE levitating rose-gold Al Rayan ring (display facing camera) over a pale stone | ADAPT | display fidelity is the known weak spot: one ring, large, front-on; a second ring is dropped on purpose |
| Annotation list | 6 dotted-leader labels | up to 5 dotted-leader labels, 2-3 words, allowed claims A-1..A-11 only | KEEP device, SWAP words | load-bearing |
| Proof slot | "Rated 4.5 stars" / "Over 100,000 helped" | removed; replaced by the real guarantee line in the bar | ADAPT | TRUTH-RISK |
| Claims "Instant anxiety relief" / "100% waterproof" | health / absolute claims | never; IP67 "wear it to wudu" fact only | NEVER | truth rules |
| Offer bar | navy, 91-100% (in the platform UI band) | deep green bar moved UP into the safe zone 60-66% | ADAPT | 9:16 safe zone |
| Palette | cream + navy + gold | cream #F3EBDD + black + deep green #1F5A2E (store accent) + rose gold ring | SWAP by role | brand |
| Brand wordmark | "calm collective" | fixed brand text "Al Rayan" (clean sans); NOT copy-slot text | SWAP | brand |
| Background / props | pale stone, beige gradient | pale limestone block, warm cream gradient | KEEP | native to look |
| Product | competitor rings | our ring via PNG reference | SWAP | |

Load-bearing kept: the callout question headline, one levitating hero over stone, dotted-leader labels, offer bar. Truth replacements: stars/counts -> none; "100% waterproof" -> "IP67" fact only (if copy uses it); bar -> real offer/guarantee from offer_brief. Variations planned: V-copy (alt approved hook), V-layout (ring right, labels left), V-scene (deep-green ground, cream text).

## Brand context
- Palette (store page + product PNG): background cream #F3EBDD (gradient to #EADFCB) · headline text black #111111 · label text + dotted leaders deep green #1F5A2E · offer bar fill #1F5A2E with white #FFFFFF text · stone #E8DCC6 · ring rose gold (from PNG, approx #D9A58F body, black inner sleeve, black display panel, gold #D9B15A logo glyph, white segments).
- Fonts (classes): headline = bold geometric sans-serif, black weight, sentence case; labels = clean humanist sans-serif, medium; bar = clean geometric sans-serif, bold, ALL CAPS only if the approved string is ALL CAPS (case must match the string); brand wordmark = clean geometric sans-serif, bold.
- Product: a **ring** (metal-alloy smart band ring, about 8 mm wide). From the PNG: rose-gold outer band, black inner sleeve visible inside. On the band face: ONE single horizontal rounded-rectangle black screen showing four white seven-segment digits "5332" in one row, and left of the screen a smaller black rounded square with a gold stylised heart-like looped Al Rayan logo glyph (the logo button). No other label words on the product. Product PNG: C:/Users/rayan/OneDrive/Desktop/ADS/ad-runs/2026-10-05-al-rayan-dhikr-ring/00-intake/product_rose_gold.png.

## Slot table (image) — FINAL mapping: copy_final slots BRAND_WORDMARK, HEADLINE, CALLOUT_1..4, BADGE map 1:1; CALLOUT_5 unused (4 labels spaced over y 36-57.5%)
Fixed (not copy slots): brand wordmark "Al Rayan" (2 words, 8 chars) — clean geometric sans bold, #111111, centred, zone y 14-18% / x 38-62%, cap height ≈2.6% of frame height. Treated as fixed brand text; the orchestrator should list it as `on_image_text` slot `BRAND` in Phase B.

| slot | role | max words | max chars | font class · weight · case | hex | zone (% of frame H / W) | size (cap height % of frame) |
|---|---|---|---|---|---|---|---|
| HEADLINE | callout question naming the avatar's habit (swipe: "A skin picker?") | 6 | 34 | bold geometric sans-serif · black · sentence case (as approved); 1-2 lines | #111111 | y 19-31% / x 6-94%, centred | ≥5.5% (line height ~8%) |
| CALLOUT_1 | dotted-leader label 1 | 3 | 20 | clean humanist sans · medium · sentence case | #1F5A2E | y 34-39% / x 56-94%, left-aligned, 4 dots leader from x 50% | ≥2.8% |
| CALLOUT_2 | label 2 | 3 | 20 | same | #1F5A2E | y 39.5-44.5% | ≥2.8% |
| CALLOUT_3 | label 3 | 3 | 20 | same | #1F5A2E | y 45-50% | ≥2.8% |
| CALLOUT_4 | label 4 | 3 | 20 | same | #1F5A2E | y 50.5-55.5% | ≥2.8% |
| CALLOUT_5 | label 5 (optional; slot unused if copy gives 4) | 3 | 20 | same | #1F5A2E | y 56-61% | ≥2.8% |
| BADGE | offer bar: real guarantee/shipping line (swipe: "FREE SHIPPING OVER £50") | 6 | 36 | clean geometric sans · bold · case as approved | white #FFFFFF on #1F5A2E | full-width bar x 0-100%, y 61.5-66.5% | ≥3.2% |

Note: bar text must stay inside the 65% safe line for the label; the bar band is y 61.5-66.5%. Labels therefore stop at y 59%. If the copy has 4 callouts, space them evenly over y 34-58%. Total on-image words target ≤25 (headline ≤6 + callouts ≤15 + bar ≤6 = 27 max; copywriter must hold total ≤25 including brand 2 -> keep callouts to 2-3 words, bar ≤5 words, headline ≤5). CTA_BUTTON not used (the Meta button is the CTA; the bar carries the offer line).

## Prompts
### img_main — nano_banana_pro · 9:16 · 2k · refs: @product
```text
Scene: A clean studio product advertisement. Exactly one rose-gold smart ring floats in mid-air, levitating about one ring-height above a pale cream limestone #E8DCC6 stone block that rises from the lower-left of the frame. The ring is turned so its flat outer face with the black display screen points to the camera, tilted about 12 degrees, with a soft contact shadow on the stone below it. No people, no hands, no other products. Thin dotted leader lines run from the ring sideways, each ending next to a short text label.

Style: Polished premium DTC studio render, soft and airy, with a flat graphic text overlay on top; calm, minimal, uncluttered. Not a lifestyle photo.

Lighting: Soft diffused top light from the upper left, warm 3500K, gentle highlights on the rose-gold edges, smooth warm cream gradient background, soft natural shadow beside the stone.

Camera: Eye-level, straight-on, 85mm product lens, the ring and its display perfectly sharp.

Composition: Vertical 9:16 frame. The top 0-14% is empty background. Brand wordmark centred at 14-18% of frame height. Headline band 19-31% of height, centred, spanning 6-94% of width. The ring hero occupies 33-58% of frame height and about 52% of frame width, centred at x 31% (left-centre), its display fully visible. The stone occupies 54-72% of height at the lower-left, the ring floating above it. Four dotted-leader labels are stacked between 36% and 57.5% of height, left-aligned from x 56% to 94%, evenly spaced, each with a four-dot dotted leader starting at x 50% and running a short straight line toward the ring. A solid bar spans the full width of the frame at 61.5-66.5% of height. Below 67% only calm background and the soft shadow of the stone, no text.

Brand colors: Background warm cream #F3EBDD blending to #EADFCB. Headline and brand wordmark near-black #111111. Labels and dotted leaders deep green #1F5A2E. Bar fill deep green #1F5A2E with white #FFFFFF text. Stone pale cream limestone #E8DCC6. The ring keeps its own colors.

Product: Match the attached product reference image exactly: shape, label, colors, logo. Do not redesign, re-letter, simplify or recolor the label. Do not invent label text. Exactly one rose-gold ring with a black inner sleeve, a flat wide band about 8 mm wide, floating, its flat outer face turned toward the camera. The display is ONE single horizontal row of four white seven-segment digits reading 5-3-3-2 on a black screen, with the gold Al Rayan logo button (a small black rounded square with a gold looped glyph) beside it on the left, exactly as in the product PNG; never digits running along the band, never a second row, no other digits. Ring height about 26% of frame height, the display clearly readable, no hand or object covering it. Use a single hero ring only; no second ring.

Text: Render exactly seven text elements (brand wordmark, headline, four labels, bar):
1) "Al Rayan" — clean geometric sans-serif, bold, #111111, centred, y 14-18%, cap height about 2.6% of frame height.
2) "Lost your dhikr count?" on one line — bold geometric sans-serif, black weight, sentence case, #111111, centred in the headline band 19-31%, cap height at least 5.5% of frame height.
3) "Tap to count" — clean humanist sans-serif, medium weight, #1F5A2E, left-aligned, y 36-41%, cap height about 2.8% of frame height, very slightly rotated (about 2 degrees clockwise).
4) "Pulse at 33-66-99" — clean humanist sans-serif, medium weight, #1F5A2E, left-aligned, y 41.5-46.5%, cap height about 2.8% of frame height, very slightly rotated (about 2 degrees clockwise).
5) "IP67 for wudu" — clean humanist sans-serif, medium weight, #1F5A2E, left-aligned, y 47-52%, cap height about 2.8% of frame height, very slightly rotated (about 2 degrees clockwise).
6) "App sync" — clean humanist sans-serif, medium weight, #1F5A2E, left-aligned, y 52.5-57.5%, cap height about 2.8% of frame height, very slightly rotated (about 2 degrees clockwise).
7) "60-DAY MONEY-BACK GUARANTEE" — clean geometric sans-serif, bold, ALL CAPS exactly as written, white #FFFFFF, centred inside the bar, one line, cap height about 3.2% of frame height.

Legibility: Spell every word exactly as written, letter for letter, with exact capitalisation, hyphens and punctuation. The brand wordmark "Al Rayan" is spelled A-L space R-A-Y-A-N. The word "dhikr" in the headline (if present) is spelled D-H-I-K-R. The label "Pulse at 33-66-99" has the numbers 33, 66 and 99 joined by two hyphens, no spaces around the hyphens. High contrast on every element; the headline is the largest and heaviest element and is readable at thumbnail size. All text fully inside the frame with 6% side margins, nothing cut off, no text overlapping the ring or the leader lines. Render only these seven quoted strings and the product's own display digits and logo; do not render section labels or any other words from these instructions.

Avoid: any other text, words or numbers; star ratings, review counts, "helped" counts, badges, seals, press logos, "clinically proven", "100% waterproof" or any health or anxiety claims; digits running along the band or digits on the side of the band; a second ring; extra rings or a ring stack; an altered or invented logo glyph; hands, people, faces; water, bubbles or splashes; reflections hiding the display; watermarks; other brand names; text in the top 14% or below 67% of the frame; blank placeholder text on objects.
```

## Variations (img_v1–img_v3 · NOT rendered this round; full prompts)
### img_v1 — V-copy — Same layout; HEADLINE swapped to approved hook H2 "Kids interrupted. Count gone." on two lines.
```text
Scene: A clean studio product advertisement. Exactly one rose-gold smart ring floats in mid-air, levitating about one ring-height above a pale cream limestone #E8DCC6 stone block that rises from the lower-left of the frame. The ring is turned so its flat outer face with the black display screen points to the camera, tilted about 12 degrees, with a soft contact shadow on the stone below it. No people, no hands, no other products. Thin dotted leader lines run from the ring sideways, each ending next to a short text label.

Style: Polished premium DTC studio render, soft and airy, with a flat graphic text overlay on top; calm, minimal, uncluttered. Not a lifestyle photo.

Lighting: Soft diffused top light from the upper left, warm 3500K, gentle highlights on the rose-gold edges, smooth warm cream gradient background, soft natural shadow beside the stone.

Camera: Eye-level, straight-on, 85mm product lens, the ring and its display perfectly sharp.

Composition: Vertical 9:16 frame. The top 0-14% is empty background. Brand wordmark centred at 14-18% of frame height. Headline band 19-31% of height, centred, spanning 6-94% of width. The ring hero occupies 33-58% of frame height and about 52% of frame width, centred at x 31% (left-centre), its display fully visible. The stone occupies 54-72% of height at the lower-left, the ring floating above it. Four dotted-leader labels are stacked between 36% and 57.5% of height, left-aligned from x 56% to 94%, evenly spaced, each with a four-dot dotted leader starting at x 50% and running a short straight line toward the ring. A solid bar spans the full width of the frame at 61.5-66.5% of height. Below 67% only calm background and the soft shadow of the stone, no text.

Brand colors: Background warm cream #F3EBDD blending to #EADFCB. Headline and brand wordmark near-black #111111. Labels and dotted leaders deep green #1F5A2E. Bar fill deep green #1F5A2E with white #FFFFFF text. Stone pale cream limestone #E8DCC6. The ring keeps its own colors.

Product: Match the attached product reference image exactly: shape, label, colors, logo. Do not redesign, re-letter, simplify or recolor the label. Do not invent label text. Exactly one rose-gold ring with a black inner sleeve, a flat wide band about 8 mm wide, floating, its flat outer face turned toward the camera. The display is ONE single horizontal row of four white seven-segment digits reading 5-3-3-2 on a black screen, with the gold Al Rayan logo button (a small black rounded square with a gold looped glyph) beside it on the left, exactly as in the product PNG; never digits running along the band, never a second row, no other digits. Ring height about 26% of frame height, the display clearly readable, no hand or object covering it. Use a single hero ring only; no second ring.

Text: Render exactly seven text elements (brand wordmark, headline, four labels, bar):
1) "Al Rayan" — clean geometric sans-serif, bold, #111111, centred, y 14-18%, cap height about 2.6% of frame height.
2) "Kids interrupted. Count gone." on two lines: line 1 "Kids interrupted.", line 2 "Count gone." — bold geometric sans-serif, black weight, sentence case, #111111, centred in the headline band 19-31%, cap height at least 5.5% of frame height.
3) "Tap to count" — clean humanist sans-serif, medium weight, #1F5A2E, left-aligned, y 36-41%, cap height about 2.8% of frame height, very slightly rotated (about 2 degrees clockwise).
4) "Pulse at 33-66-99" — clean humanist sans-serif, medium weight, #1F5A2E, left-aligned, y 41.5-46.5%, cap height about 2.8% of frame height, very slightly rotated (about 2 degrees clockwise).
5) "IP67 for wudu" — clean humanist sans-serif, medium weight, #1F5A2E, left-aligned, y 47-52%, cap height about 2.8% of frame height, very slightly rotated (about 2 degrees clockwise).
6) "App sync" — clean humanist sans-serif, medium weight, #1F5A2E, left-aligned, y 52.5-57.5%, cap height about 2.8% of frame height, very slightly rotated (about 2 degrees clockwise).
7) "60-DAY MONEY-BACK GUARANTEE" — clean geometric sans-serif, bold, ALL CAPS exactly as written, white #FFFFFF, centred inside the bar, one line, cap height about 3.2% of frame height.

Legibility: Spell every word exactly as written, letter for letter, with exact capitalisation, hyphens and punctuation. The brand wordmark "Al Rayan" is spelled A-L space R-A-Y-A-N. The word "dhikr" in the headline (if present) is spelled D-H-I-K-R. The label "Pulse at 33-66-99" has the numbers 33, 66 and 99 joined by two hyphens, no spaces around the hyphens. High contrast on every element; the headline is the largest and heaviest element and is readable at thumbnail size. All text fully inside the frame with 6% side margins, nothing cut off, no text overlapping the ring or the leader lines. Render only these seven quoted strings and the product's own display digits and logo; do not render section labels or any other words from these instructions.

Avoid: any other text, words or numbers; star ratings, review counts, "helped" counts, badges, seals, press logos, "clinically proven", "100% waterproof" or any health or anxiety claims; digits running along the band or digits on the side of the band; a second ring; extra rings or a ring stack; an altered or invented logo glyph; hands, people, faces; water, bubbles or splashes; reflections hiding the display; watermarks; other brand names; text in the top 14% or below 67% of the frame; blank placeholder text on objects.
```

### img_v2 — V-layout — Mirrored composition: ring right-of-centre over a lower-right stone, labels right-aligned on the left; headline and bar unchanged.
```text
Scene: A clean studio product advertisement. Exactly one rose-gold smart ring floats in mid-air, levitating about one ring-height above a pale cream limestone #E8DCC6 stone block that rises from the lower-right of the frame. The ring is turned so its flat outer face with the black display screen points to the camera, tilted about 12 degrees, with a soft contact shadow on the stone below it. No people, no hands, no other products. Thin dotted leader lines run from the ring sideways, each ending next to a short text label.

Style: Polished premium DTC studio render, soft and airy, with a flat graphic text overlay on top; calm, minimal, uncluttered. Not a lifestyle photo.

Lighting: Soft diffused top light from the upper left, warm 3500K, gentle highlights on the rose-gold edges, smooth warm cream gradient background, soft natural shadow beside the stone.

Camera: Eye-level, straight-on, 85mm product lens, the ring and its display perfectly sharp.

Composition: Vertical 9:16 frame. The top 0-14% is empty background. Brand wordmark centred at 14-18% of frame height. Headline band 19-31% of height, centred, spanning 6-94% of width. The ring hero occupies 33-58% of frame height and about 52% of frame width, centred at x 69% (right-centre), its display fully visible. The stone occupies 54-72% of height at the lower-right, the ring floating above it. Four dotted-leader labels are stacked between 36% and 57.5% of height, right-aligned, ending at x 44% and starting no further left than x 6%, evenly spaced, each with a four-dot dotted leader starting at x 50% and running a short straight line toward the ring. A solid bar spans the full width of the frame at 61.5-66.5% of height. Below 67% only calm background and the soft shadow of the stone, no text.

Brand colors: Background warm cream #F3EBDD blending to #EADFCB. Headline and brand wordmark near-black #111111. Labels and dotted leaders deep green #1F5A2E. Bar fill deep green #1F5A2E with white #FFFFFF text. Stone pale cream limestone #E8DCC6. The ring keeps its own colors.

Product: Match the attached product reference image exactly: shape, label, colors, logo. Do not redesign, re-letter, simplify or recolor the label. Do not invent label text. Exactly one rose-gold ring with a black inner sleeve, a flat wide band about 8 mm wide, floating, its flat outer face turned toward the camera. The display is ONE single horizontal row of four white seven-segment digits reading 5-3-3-2 on a black screen, with the gold Al Rayan logo button (a small black rounded square with a gold looped glyph) beside it on the left, exactly as in the product PNG; never digits running along the band, never a second row, no other digits. Ring height about 26% of frame height, the display clearly readable, no hand or object covering it. Use a single hero ring only; no second ring.

Text: Render exactly seven text elements (brand wordmark, headline, four labels, bar):
1) "Al Rayan" — clean geometric sans-serif, bold, #111111, centred, y 14-18%, cap height about 2.6% of frame height.
2) "Lost your dhikr count?" on one line — bold geometric sans-serif, black weight, sentence case, #111111, centred in the headline band 19-31%, cap height at least 5.5% of frame height.
3) "Tap to count" — clean humanist sans-serif, medium weight, #1F5A2E, right-aligned, y 36-41%, cap height about 2.8% of frame height, very slightly rotated (about 2 degrees counter-clockwise).
4) "Pulse at 33-66-99" — clean humanist sans-serif, medium weight, #1F5A2E, right-aligned, y 41.5-46.5%, cap height about 2.8% of frame height, very slightly rotated (about 2 degrees counter-clockwise).
5) "IP67 for wudu" — clean humanist sans-serif, medium weight, #1F5A2E, right-aligned, y 47-52%, cap height about 2.8% of frame height, very slightly rotated (about 2 degrees counter-clockwise).
6) "App sync" — clean humanist sans-serif, medium weight, #1F5A2E, right-aligned, y 52.5-57.5%, cap height about 2.8% of frame height, very slightly rotated (about 2 degrees counter-clockwise).
7) "60-DAY MONEY-BACK GUARANTEE" — clean geometric sans-serif, bold, ALL CAPS exactly as written, white #FFFFFF, centred inside the bar, one line, cap height about 3.2% of frame height.

Legibility: Spell every word exactly as written, letter for letter, with exact capitalisation, hyphens and punctuation. The brand wordmark "Al Rayan" is spelled A-L space R-A-Y-A-N. The word "dhikr" in the headline (if present) is spelled D-H-I-K-R. The label "Pulse at 33-66-99" has the numbers 33, 66 and 99 joined by two hyphens, no spaces around the hyphens. High contrast on every element; the headline is the largest and heaviest element and is readable at thumbnail size. All text fully inside the frame with 6% side margins, nothing cut off, no text overlapping the ring or the leader lines. Render only these seven quoted strings and the product's own display digits and logo; do not render section labels or any other words from these instructions.

Avoid: any other text, words or numbers; star ratings, review counts, "helped" counts, badges, seals, press logos, "clinically proven", "100% waterproof" or any health or anxiety claims; digits running along the band or digits on the side of the band; a second ring; extra rings or a ring stack; an altered or invented logo glyph; hands, people, faces; water, bubbles or splashes; reflections hiding the display; watermarks; other brand names; text in the top 14% or below 67% of the frame; blank placeholder text on objects.
```

### img_v3 — V-scene — Deep green gradient ground with a dark stone, cream headline, labels and leaders, cream bar with deep green text; ring unchanged rose gold.
```text
Scene: A clean studio product advertisement. Exactly one rose-gold smart ring floats in mid-air, levitating about one ring-height above a dark green-grey stone #2E4A35 stone block that rises from the lower-left of the frame. The ring is turned so its flat outer face with the black display screen points to the camera, tilted about 12 degrees, with a soft contact shadow on the stone below it. No people, no hands, no other products. Thin dotted leader lines run from the ring sideways, each ending next to a short text label.

Style: Polished premium DTC studio render, soft and airy, with a flat graphic text overlay on top; calm, minimal, uncluttered. Not a lifestyle photo.

Lighting: Soft diffused top light from the upper left, warm 3500K, gentle highlights on the rose-gold edges, smooth deep green gradient background, soft natural shadow beside the stone.

Camera: Eye-level, straight-on, 85mm product lens, the ring and its display perfectly sharp.

Composition: Vertical 9:16 frame. The top 0-14% is empty background. Brand wordmark centred at 14-18% of frame height. Headline band 19-31% of height, centred, spanning 6-94% of width. The ring hero occupies 33-58% of frame height and about 52% of frame width, centred at x 31% (left-centre), its display fully visible. The stone occupies 54-72% of height at the lower-left, the ring floating above it. Four dotted-leader labels are stacked between 36% and 57.5% of height, left-aligned from x 56% to 94%, evenly spaced, each with a four-dot dotted leader starting at x 50% and running a short straight line toward the ring. A solid bar spans the full width of the frame at 61.5-66.5% of height. Below 67% only calm background and the soft shadow of the stone, no text.

Brand colors: Background deep green #1F5A2E blending to darker green #14401F at the bottom. Headline and brand wordmark warm cream #F3EBDD. Labels and dotted leaders warm cream #F3EBDD. Bar fill warm cream #F3EBDD with deep green #1F5A2E text. Stone dark green-grey stone #2E4A35. The ring keeps its own colors.

Product: Match the attached product reference image exactly: shape, label, colors, logo. Do not redesign, re-letter, simplify or recolor the label. Do not invent label text. Exactly one rose-gold ring with a black inner sleeve, a flat wide band about 8 mm wide, floating, its flat outer face turned toward the camera. The display is ONE single horizontal row of four white seven-segment digits reading 5-3-3-2 on a black screen, with the gold Al Rayan logo button (a small black rounded square with a gold looped glyph) beside it on the left, exactly as in the product PNG; never digits running along the band, never a second row, no other digits. Ring height about 26% of frame height, the display clearly readable, no hand or object covering it. Use a single hero ring only; no second ring.

Text: Render exactly seven text elements (brand wordmark, headline, four labels, bar):
1) "Al Rayan" — clean geometric sans-serif, bold, #F3EBDD, centred, y 14-18%, cap height about 2.6% of frame height.
2) "Lost your dhikr count?" on one line — bold geometric sans-serif, black weight, sentence case, #F3EBDD, centred in the headline band 19-31%, cap height at least 5.5% of frame height.
3) "Tap to count" — clean humanist sans-serif, medium weight, #F3EBDD, left-aligned, y 36-41%, cap height about 2.8% of frame height, very slightly rotated (about 2 degrees clockwise).
4) "Pulse at 33-66-99" — clean humanist sans-serif, medium weight, #F3EBDD, left-aligned, y 41.5-46.5%, cap height about 2.8% of frame height, very slightly rotated (about 2 degrees clockwise).
5) "IP67 for wudu" — clean humanist sans-serif, medium weight, #F3EBDD, left-aligned, y 47-52%, cap height about 2.8% of frame height, very slightly rotated (about 2 degrees clockwise).
6) "App sync" — clean humanist sans-serif, medium weight, #F3EBDD, left-aligned, y 52.5-57.5%, cap height about 2.8% of frame height, very slightly rotated (about 2 degrees clockwise).
7) "60-DAY MONEY-BACK GUARANTEE" — clean geometric sans-serif, bold, ALL CAPS exactly as written, deep green #1F5A2E, centred inside the bar, one line, cap height about 3.2% of frame height.

Legibility: Spell every word exactly as written, letter for letter, with exact capitalisation, hyphens and punctuation. The brand wordmark "Al Rayan" is spelled A-L space R-A-Y-A-N. The word "dhikr" in the headline (if present) is spelled D-H-I-K-R. The label "Pulse at 33-66-99" has the numbers 33, 66 and 99 joined by two hyphens, no spaces around the hyphens. High contrast on every element; the headline is the largest and heaviest element and is readable at thumbnail size. All text fully inside the frame with 6% side margins, nothing cut off, no text overlapping the ring or the leader lines. Render only these seven quoted strings and the product's own display digits and logo; do not render section labels or any other words from these instructions.

Avoid: any other text, words or numbers; star ratings, review counts, "helped" counts, badges, seals, press logos, "clinically proven", "100% waterproof" or any health or anxiety claims; digits running along the band or digits on the side of the band; a second ring; extra rings or a ring stack; an altered or invented logo glyph; hands, people, faces; water, bubbles or splashes; reflections hiding the display; watermarks; other brand names; text in the top 14% or below 67% of the frame; blank placeholder text on objects.
```

## Budget
img_main 1 x 2.0 cr = 2.0 cr (variations excluded; 2.0 each if rendered).

## Self-check
- [x] Every on-image string verbatim and quoted in its prompt (Al Rayan; Lost your dhikr count?; Tap to count; Pulse at 33-66-99; IP67 for wudu; App sync; 60-DAY MONEY-BACK GUARANTEE; img_v1 headline Kids interrupted. Count gone.)
- [x] @product first in references; no competitor media or names; single hero ring; display = one row 5-3-3-2 + gold logo button, never along the band.
- [x] Bar at 61.5-66.5% of height (inside the 9:16 safe zone); text within 14-67%.
- [x] No slot marker or double brace left.
- Mapping notes: copy slot BRAND_WORDMARK used as given; BADGE = bottom bar; 4 callouts (CALLOUT_5 dropped). On-image words 18.
- chief_verdict_v1.json says REVISE (round 1); the orchestrator accepted the chiefed v1 as final, so chief.final_verdict is "APPROVE".
