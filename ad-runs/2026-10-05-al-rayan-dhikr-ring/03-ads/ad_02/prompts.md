# ad_02 prompts - FINAL

## Swipe port - source: Tayyib Beauty - 175015416 (analysis: C:/Users/rayan/OneDrive/Desktop/ADS/ad-runs/2026-10-05-al-rayan-dhikr-ring/02-creative-research/gethookd/tayyib-beauty-175015416/analysis.md)

Viewed (Read tool): swipe media.jpg (1024x1024), product_black.png, product_rose_gold.png, store_product_page.png. frames_viewed = 4 (image ad, no video frames).

### Teardown (swipe, brand-agnostic)
- Format: 1:1 static, polished AI-rendered studio look (not native). Zones (height): top headline band 0-22%; split macro/product 22-77% (two 50% columns divided by a thin gold vertical line, thin gold rule above and below); badge row 77-100% (four items). Focal flow: gold "Your lips need this." (largest) -> black caps ritual line -> lips macro -> product -> badges. Read time under 1.5 s. Cream bg est. #F5F0E6, black caps #111111, gold #B8860B.
- Fonts: high-contrast serif; line 1 bold ALL CAPS black; line 2 larger gold sentence case; badges small caps sans with gold check/droplet icons.
- Strings (verbatim): "NO WATER FOR 16 HOURS. WUDU FIVE TIMES." / "Your lips need this." / "HALAL CERTIFIED" / "SAFE TO INGEST" / "SEALS OVERNIGHT" / "ABSORBS IN MINUTES" / product label "Tayyib HALAL TALLOW LIP BALM".
- Hook: two ritual facts only Muslims recognise, then the symptom; type callout; visual device split_contrast. Promise: the product is relief for a ritual-specific problem. CTA: Meta button only (no on-image CTA). Angle: pain relief + identity. Proof elements: none (their halal certified / safe to ingest claims are not ours).

### Keep / swap / adapt / never
| Element | Swipe | Ours | Decision | Why |
|---|---|---|---|---|
| Layout grid | headline band / split / badge row | same order, re-zoned for 9:16 safe zones (headline 14-32%, split 33-60%, badge row 61-66%) | KEEP (re-zone) | load-bearing |
| Hook structure | "X. Y five times. Your ___ needs this." | frame: [ritual fact]. [ritual fact x five]. Your [hand/tool] needs this. Words from the copywriter | KEEP frame / SWAP words | load-bearing; assigned type callout |
| Split contrast | problem macro vs product | wudu water on a hand wearing the ring vs ring hero | ADAPT | problem = water on the hand, our answer = IP67 ring that stays on |
| Palette | cream / black / gold | cream #F5F0E6 / black #111111 / deep green #1F5A2E (store accent) | SWAP | gold becomes store green; ring keeps its own gold logo |
| Fonts | high-contrast serif both lines | line 1 bold condensed sans caps (store headline style), line 2 editorial serif bold in green | ADAPT | keeps two-tier contrast, store-true |
| Image style | polished studio | polished studio macro + product render | KEEP | designed register |
| Badge row | 4 claims with icons | 3 truthful offer badges (copy decides; allowed: free US shipping, 60-day money-back guarantee, 1-year tech warranty, IP67) | ADAPT | their claims are TRUTH-RISK |
| Product | tube | our ring via product PNG ref (black) | SWAP | |
| Proof slot | halal certified | none; offer terms in badges | ADAPT | truth |
| Brand marks / people | none / lips close-up | none / one hand and wrist only, no face | SWAP | |

Load-bearing kept: two-tier ritual callout banner, split_contrast, badge row, cream light field. Truth replacements: no waterproof/shower/swim (IP67 only, splash not submersion); no stars/counts/stats; no halal or ingestion claims; no faith reward claims in the image.
Variations planned: V-copy (alt approved hook, same layout), V-layout (panels swapped), V-scene (deep green background).

## Brand context
- Palette roles: background cream #F5F0E6 (fade #EDE6D8); text black #111111; accent deep green #1F5A2E (store buttons/banners; payoff line, rules, icons); dark-variant gold #D9B65A for V-scene only. Ring: black metal body, white 7-segment digits on black display, gold logo button.
- Font classes: bold condensed sans-serif (store headline style) ALL CAPS; editorial serif bold; clean geometric sans-serif.
- Product: black metal smart ring (a band ring; not a pouch/tub/bottle), flat top with two inset black panels: the display reading "5332" in white segment digits and a small panel with the gold logo. No other label words. PNG: C:/Users/rayan/OneDrive/Desktop/ADS/ad-runs/2026-10-05-al-rayan-dhikr-ring/00-intake/product_black.png (on white). Rose gold variant exists, not used.
- Claims: offer_brief.md / concept_slate A-1..A-13 only; IP67 only.

## Slot table (image)
Approved copy slots (copy_final.md) mapped 1:1: HEADLINE_L1 = text 1 (top line), HEADLINE_L2 = text 2 (payoff line), BADGE_1..4 = badge grid (2x2). No CTA_BUTTON (Meta button only, as in the swipe). Fonts per swipe-analysis ADAPT (store sans caps + editorial serif); the copy file names serif/gold, rendered in brand green instead per the brand palette decision. HEADLINE is 9 words: accepted; headline wraps to 2 lines at cap height 5% (spec minimum), no word cut.
| slot | role | words | chars | font class + weight + case | hex | zone (height / width) | size (cap height % frame) |
|---|---|---|---|---|---|---|---|
| HEADLINE_L1 | ritual fact, hook line 1 | 5 | 22 | bold condensed sans-serif, black, ALL CAPS | #111111 | 14-28% / 6-94% centered, up to 2 lines | 5% |
| HEADLINE_L2 | payoff, hook line 2 | 4 | 22 | editorial serif, bold, sentence case | #1F5A2E | 28.5-35% / centered, 1 line | 5.5% |
| BADGE_1 | IP67 tag, droplet icon | 3 | 20 | clean geometric sans, medium, ALL CAPS | #111111 | 59-62.5% / 6-48% | 2.6% |
| BADGE_2 | tap to count, check icon | 3 | 12 | same | #111111 | 59-62.5% / 52-94% | 2.6% |
| BADGE_3 | guarantee, check icon | 2 | 16 | same | #111111 | 62.5-66% / 6-48% | 2.6% |
| BADGE_4 | shipping, check icon | 3 | 16 | same | #111111 | 62.5-66% / 52-94% | 2.6% |
Copy mapping notes: copy_final.md names the badge row as 4 badges (swipe also 4); layout changed from my Phase A 3-column row to a 2x2 grid. V-copy uses H5 "Wear it to wudu. Keep your count." split on the sentence break: line 1 "Wear it to wudu." (sentence case, because approved casing is kept) and line 2 "Keep your count.".

## Prompts

### img_main - nano_banana_pro - 9:16 - 2k - refs: @product
```text
Scene: A split-screen vertical ad image divided exactly in half by a thin vertical green line. LEFT panel: an extreme close-up of one right hand and wrist over a white ceramic bathroom sink, fingers cupped under a thin stream of clear tap water, water splashing and beading on the back of the hand and wrist, wet skin with natural droplets. The hand wears exactly one black metal smart ring on the ring finger with a small illuminated four-digit display; the ring is small in this panel and stays on the hand, splashed with water, not submerged. RIGHT panel: exactly one black smart ring floating upright at a slight three-quarter angle on a clean warm cream seamless backdrop, display facing the camera, soft shadow below. Two rings in total in the whole image.

Style: Polished, designed static ad with a clean editorial look: sharp macro photography on the left, crisp studio product render on the right, flat graphic text bands. Premium, calm, not cluttered.

Lighting: Left panel: soft bright window light from upper left, 5500K, crisp water droplets with small specular highlights. Right panel: soft diffused studio key light from upper left, warm cream gradient background, gentle ground shadow.

Camera: Left panel: macro, slightly above the hand, 85mm lens, shallow depth of field, hand sharp. Right panel: eye-level product shot, 85mm lens, ring fully sharp.

Composition: Vertical 9:16. Cream background #F5F0E6 across the whole frame. Text 1 spans 6% to 94% of width, from 14% to 28% of frame height, centered, on up to two balanced lines, broken at a natural word break. Text 2 sits directly below, from 28.5% to 35% of height, centered. A thin green #1F5A2E horizontal rule at 35.5% of height. Split panels occupy 36% to 58% of height, full width, each panel 50% of the width, divided by a 0.4% wide green #1F5A2E vertical line. Badge block on the cream strip from 59% to 66% of height: a 2 by 2 grid of four badges (two rows, two equal columns inside 6% side margins), row 1 at 59% to 62.5%, row 2 at 62.5% to 66%. Below 67% only cream background that gently fades to #EDE6D8, no elements. Focal flow: text 2 (green, largest weight) then text 1, then the hand, then the right ring, then the four badges.

Brand colors: Background cream #F5F0E6 (fading to #EDE6D8 at the bottom). Text 1 black #111111. Text 2 deep green #1F5A2E. Divider lines and badge check icons deep green #1F5A2E. Badge text black #111111. The ring keeps its own black and gold logo colors.

Product: Match the attached product reference image exactly: shape, label, colors, logo. Do not redesign, re-letter, simplify or recolor the label. Do not invent label text. Exactly one ring in the right panel, black version, upright, display facing the camera within 15 degrees, ring height about 22% of frame height, fully sharp, display digits and the gold logo button clearly visible. In the left panel one more copy of the same ring is worn on the ring finger, about 5% of frame height, display may be soft and need not be legible.

Text: Render exactly six text elements:
1) "WUDU FIVE TIMES A DAY." - bold condensed sans-serif, black weight, ALL CAPS, #111111, centered, top band 14% to 28% of frame height, on two balanced lines if the string does not fit one line at this size (never shrink below the stated size), cap height about 5% of frame height.
2) "Your count needs this." - editorial serif, bold, sentence case, deep green #1F5A2E, centered directly below text 1, 28.5% to 35% of frame height, one line, the largest text in the image, cap height about 5.5% of frame height.
3) "IP67 WATER RESISTANT" - clean geometric sans-serif, medium weight, ALL CAPS, #111111, top-left of the badge grid, one line, preceded by a small deep green #1F5A2E water-droplet icon, cap height about 2.6% of frame height.
4) "TAP TO COUNT" - same style as text 3, top-right of the badge grid, preceded by a small deep green #1F5A2E check-in-circle icon.
5) "60-DAY GUARANTEE" - same style as text 3, bottom-left of the badge grid, preceded by a small deep green #1F5A2E check-in-circle icon.
6) "FREE US SHIPPING" - same style as text 3, bottom-right of the badge grid, preceded by a small deep green #1F5A2E check-in-circle icon.
No other text is allowed other than the ring's own display and gold logo; do not render a CTA button.

Legibility: Spell every word exactly as written, letter for letter, with the exact punctuation and case of each quoted string. High contrast on every element, all text fully inside 6% side margins, nothing touching the split line or the frame edge. Render only the six quoted strings plus the ring's own display and logo; do not render section labels or any other words from these instructions.

Avoid: any text, words, letters or numbers other than the quoted strings above and the ring's own display and logo; misspelled, warped, mirrored, duplicated or cut-off letters; section labels from this prompt; more than the two rings described; altered or invented ring label or logo; watermarks; other brand names or logos; star ratings, review counts, seals, awards, 'clinically proven', press logos, the word waterproof; showers, swimming, submerged hands, pools, bathtubs; prayer beads, mosque interiors, faces, people other than the one hand and wrist; extra fingers, fused hands, distorted anatomy; plastic CGI skin; cluttered background; text in the top 14% or below 67% of the frame.
```

## Variations (rendered only per the render policy)
- img_v1 V-copy: same layout, headline/subhead from approved hook H5 (benefit-statement) (H5, approved).
- img_v2 V-layout: panels swapped (ring hero left, wudu hand right); text zones unchanged.
- img_v3 V-scene: deep green #1F5A2E background, cream and gold text, dark slate sink; same layout and words as main.

### img_v1 - nano_banana_pro - 9:16 - 2k - refs: @product
```text
Scene: A split-screen vertical ad image divided exactly in half by a thin vertical green line. LEFT panel: an extreme close-up of one right hand and wrist over a white ceramic bathroom sink, fingers cupped under a thin stream of clear tap water, water splashing and beading on the back of the hand and wrist, wet skin with natural droplets. The hand wears exactly one black metal smart ring on the ring finger with a small illuminated four-digit display; the ring is small in this panel and stays on the hand, splashed with water, not submerged. RIGHT panel: exactly one black smart ring floating upright at a slight three-quarter angle on a clean warm cream seamless backdrop, display facing the camera, soft shadow below. Two rings in total in the whole image.

Style: Polished, designed static ad with a clean editorial look: sharp macro photography on the left, crisp studio product render on the right, flat graphic text bands. Premium, calm, not cluttered.

Lighting: Left panel: soft bright window light from upper left, 5500K, crisp water droplets with small specular highlights. Right panel: soft diffused studio key light from upper left, warm cream gradient background, gentle ground shadow.

Camera: Left panel: macro, slightly above the hand, 85mm lens, shallow depth of field, hand sharp. Right panel: eye-level product shot, 85mm lens, ring fully sharp.

Composition: Vertical 9:16. Cream background #F5F0E6 across the whole frame. Text 1 spans 6% to 94% of width, from 14% to 28% of frame height, centered, on up to two balanced lines, broken at a natural word break. Text 2 sits directly below, from 28.5% to 35% of height, centered. A thin green #1F5A2E horizontal rule at 35.5% of height. Split panels occupy 36% to 58% of height, full width, each panel 50% of the width, divided by a 0.4% wide green #1F5A2E vertical line. Badge block on the cream strip from 59% to 66% of height: a 2 by 2 grid of four badges (two rows, two equal columns inside 6% side margins), row 1 at 59% to 62.5%, row 2 at 62.5% to 66%. Below 67% only cream background that gently fades to #EDE6D8, no elements. Focal flow: text 2 (green, largest weight) then text 1, then the hand, then the right ring, then the four badges.

Brand colors: Background cream #F5F0E6 (fading to #EDE6D8 at the bottom). Text 1 black #111111. Text 2 deep green #1F5A2E. Divider lines and badge check icons deep green #1F5A2E. Badge text black #111111. The ring keeps its own black and gold logo colors.

Product: Match the attached product reference image exactly: shape, label, colors, logo. Do not redesign, re-letter, simplify or recolor the label. Do not invent label text. Exactly one ring in the right panel, black version, upright, display facing the camera within 15 degrees, ring height about 22% of frame height, fully sharp, display digits and the gold logo button clearly visible. In the left panel one more copy of the same ring is worn on the ring finger, about 5% of frame height, display may be soft and need not be legible.

Text: Render exactly six text elements:
1) "Wear it to wudu." - bold condensed sans-serif, black weight, sentence case, #111111, centered, top band 14% to 28% of frame height, on two balanced lines if the string does not fit one line at this size (never shrink below the stated size), cap height about 5% of frame height.
2) "Keep your count." - editorial serif, bold, sentence case, deep green #1F5A2E, centered directly below text 1, 28.5% to 35% of frame height, one line, the largest text in the image, cap height about 5.5% of frame height.
3) "IP67 WATER RESISTANT" - clean geometric sans-serif, medium weight, ALL CAPS, #111111, top-left of the badge grid, one line, preceded by a small deep green #1F5A2E water-droplet icon, cap height about 2.6% of frame height.
4) "TAP TO COUNT" - same style as text 3, top-right of the badge grid, preceded by a small deep green #1F5A2E check-in-circle icon.
5) "60-DAY GUARANTEE" - same style as text 3, bottom-left of the badge grid, preceded by a small deep green #1F5A2E check-in-circle icon.
6) "FREE US SHIPPING" - same style as text 3, bottom-right of the badge grid, preceded by a small deep green #1F5A2E check-in-circle icon.
No other text is allowed other than the ring's own display and gold logo; do not render a CTA button.

Legibility: Spell every word exactly as written, letter for letter, with the exact punctuation and case of each quoted string. High contrast on every element, all text fully inside 6% side margins, nothing touching the split line or the frame edge. Render only the six quoted strings plus the ring's own display and logo; do not render section labels or any other words from these instructions.

Avoid: any text, words, letters or numbers other than the quoted strings above and the ring's own display and logo; misspelled, warped, mirrored, duplicated or cut-off letters; section labels from this prompt; more than the two rings described; altered or invented ring label or logo; watermarks; other brand names or logos; star ratings, review counts, seals, awards, 'clinically proven', press logos, the word waterproof; showers, swimming, submerged hands, pools, bathtubs; prayer beads, mosque interiors, faces, people other than the one hand and wrist; extra fingers, fused hands, distorted anatomy; plastic CGI skin; cluttered background; text in the top 14% or below 67% of the frame.
```

### img_v2 - nano_banana_pro - 9:16 - 2k - refs: @product
```text
Scene: A split-screen vertical ad image divided exactly in half by a thin vertical green line. RIGHT panel: an extreme close-up of one right hand and wrist over a white ceramic bathroom sink, fingers cupped under a thin stream of clear tap water, water splashing and beading on the back of the hand and wrist, wet skin with natural droplets. The hand wears exactly one black metal smart ring on the ring finger with a small illuminated four-digit display; the ring is small in this panel and stays on the hand, splashed with water, not submerged. LEFT panel: exactly one black smart ring floating upright at a slight three-quarter angle on a clean warm cream seamless backdrop, display facing the camera, soft shadow below. Two rings in total in the whole image.

Style: Polished, designed static ad with a clean editorial look: sharp macro photography on the left, crisp studio product render on the right, flat graphic text bands. Premium, calm, not cluttered.

Lighting: Right panel: soft bright window light from upper left, 5500K, crisp water droplets with small specular highlights. Left panel: soft diffused studio key light from upper left, warm cream gradient background, gentle ground shadow.

Camera: Right panel: macro, slightly above the hand, 85mm lens, shallow depth of field, hand sharp. Left panel: eye-level product shot, 85mm lens, ring fully sharp.

Composition: Vertical 9:16. Cream background #F5F0E6 across the whole frame. Text 1 spans 6% to 94% of width, from 14% to 28% of frame height, centered, on up to two balanced lines, broken at a natural word break. Text 2 sits directly below, from 28.5% to 35% of height, centered. A thin green #1F5A2E horizontal rule at 35.5% of height. Split panels occupy 36% to 58% of height, full width, each panel 50% of the width, divided by a 0.4% wide green #1F5A2E vertical line. Badge block on the cream strip from 59% to 66% of height: a 2 by 2 grid of four badges (two rows, two equal columns inside 6% side margins), row 1 at 59% to 62.5%, row 2 at 62.5% to 66%. Below 67% only cream background that gently fades to #EDE6D8, no elements. Focal flow: text 2 (green, largest weight) then text 1, then the left ring, then the hand, then the four badges.

Brand colors: Background cream #F5F0E6 (fading to #EDE6D8 at the bottom). Text 1 black #111111. Text 2 deep green #1F5A2E. Divider lines and badge check icons deep green #1F5A2E. Badge text black #111111. The ring keeps its own black and gold logo colors.

Product: Match the attached product reference image exactly: shape, label, colors, logo. Do not redesign, re-letter, simplify or recolor the label. Do not invent label text. Exactly one ring in the left panel, black version, upright, display facing the camera within 15 degrees, ring height about 22% of frame height, fully sharp, display digits and the gold logo button clearly visible. In the right panel one more copy of the same ring is worn on the ring finger, about 5% of frame height, display may be soft and need not be legible.

Text: Render exactly six text elements:
1) "WUDU FIVE TIMES A DAY." - bold condensed sans-serif, black weight, ALL CAPS, #111111, centered, top band 14% to 28% of frame height, on two balanced lines if the string does not fit one line at this size (never shrink below the stated size), cap height about 5% of frame height.
2) "Your count needs this." - editorial serif, bold, sentence case, deep green #1F5A2E, centered directly below text 1, 28.5% to 35% of frame height, one line, the largest text in the image, cap height about 5.5% of frame height.
3) "IP67 WATER RESISTANT" - clean geometric sans-serif, medium weight, ALL CAPS, #111111, top-left of the badge grid, one line, preceded by a small deep green #1F5A2E water-droplet icon, cap height about 2.6% of frame height.
4) "TAP TO COUNT" - same style as text 3, top-right of the badge grid, preceded by a small deep green #1F5A2E check-in-circle icon.
5) "60-DAY GUARANTEE" - same style as text 3, bottom-left of the badge grid, preceded by a small deep green #1F5A2E check-in-circle icon.
6) "FREE US SHIPPING" - same style as text 3, bottom-right of the badge grid, preceded by a small deep green #1F5A2E check-in-circle icon.
No other text is allowed other than the ring's own display and gold logo; do not render a CTA button.

Legibility: Spell every word exactly as written, letter for letter, with the exact punctuation and case of each quoted string. High contrast on every element, all text fully inside 6% side margins, nothing touching the split line or the frame edge. Render only the six quoted strings plus the ring's own display and logo; do not render section labels or any other words from these instructions.

Avoid: any text, words, letters or numbers other than the quoted strings above and the ring's own display and logo; misspelled, warped, mirrored, duplicated or cut-off letters; section labels from this prompt; more than the two rings described; altered or invented ring label or logo; watermarks; other brand names or logos; star ratings, review counts, seals, awards, 'clinically proven', press logos, the word waterproof; showers, swimming, submerged hands, pools, bathtubs; prayer beads, mosque interiors, faces, people other than the one hand and wrist; extra fingers, fused hands, distorted anatomy; plastic CGI skin; cluttered background; text in the top 14% or below 67% of the frame.
```

### img_v3 - nano_banana_pro - 9:16 - 2k - refs: @product
```text
Scene: A split-screen vertical ad image divided exactly in half by a thin vertical cream line. LEFT panel: an extreme close-up of one right hand and wrist over a dark grey slate bathroom sink, fingers cupped under a thin stream of clear tap water, water splashing and beading on the back of the hand and wrist, wet skin with natural droplets. The hand wears exactly one black metal smart ring on the ring finger with a small illuminated four-digit display; the ring is small in this panel and stays on the hand, splashed with water, not submerged. RIGHT panel: exactly one black smart ring floating upright at a slight three-quarter angle on a clean deep green #1F5A2E seamless backdrop with a soft cream rim light, display facing the camera, soft shadow below. Two rings in total in the whole image.

Style: Polished, designed static ad with a clean editorial look: sharp macro photography on the left, crisp studio product render on the right, flat graphic text bands. Premium, calm, not cluttered.

Lighting: Left panel: soft bright window light from upper left, 5500K, crisp water droplets with small specular highlights. Right panel: soft diffused studio key light from upper left, deep green gradient background, gentle ground shadow.

Camera: Left panel: macro, slightly above the hand, 85mm lens, shallow depth of field, hand sharp. Right panel: eye-level product shot, 85mm lens, ring fully sharp.

Composition: Vertical 9:16. Deep green background #1F5A2E across the whole frame. Text 1 spans 6% to 94% of width, from 14% to 28% of frame height, centered, on up to two balanced lines, broken at a natural word break. Text 2 sits directly below, from 28.5% to 35% of height, centered. A thin cream #F5F0E6 horizontal rule at 35.5% of height. Split panels occupy 36% to 58% of height, full width, each panel 50% of the width, divided by a 0.4% wide cream #F5F0E6 vertical line. Badge block on the cream strip from 59% to 66% of height: a 2 by 2 grid of four badges (two rows, two equal columns inside 6% side margins), row 1 at 59% to 62.5%, row 2 at 62.5% to 66%. Below 67% only deep green background that gently fades to #174421, no elements. Focal flow: text 2 (gold, largest weight) then text 1, then the hand, then the right ring, then the four badges.

Brand colors: Background deep green #1F5A2E (fading to #174421 at the bottom). Headline text 1 cream #F5F0E6. Text 2 warm gold #D9B65A. Divider lines and badge check icons cream #F5F0E6. Badge text cream #F5F0E6. The ring keeps its own black and gold logo colors.

Product: Match the attached product reference image exactly: shape, label, colors, logo. Do not redesign, re-letter, simplify or recolor the label. Do not invent label text. Exactly one ring in the right panel, black version, upright, display facing the camera within 15 degrees, ring height about 22% of frame height, fully sharp, display digits and the gold logo button clearly visible. In the left panel one more copy of the same ring is worn on the ring finger, about 5% of frame height, display may be soft and need not be legible.

Text: Render exactly six text elements:
1) "WUDU FIVE TIMES A DAY." - bold condensed sans-serif, black weight, ALL CAPS, cream #F5F0E6, centered, top band 14% to 28% of frame height, on two balanced lines if the string does not fit one line at this size (never shrink below the stated size), cap height about 5% of frame height.
2) "Your count needs this." - editorial serif, bold, sentence case, warm gold #D9B65A, centered directly below text 1, 28.5% to 35% of frame height, one line, the largest text in the image, cap height about 5.5% of frame height.
3) "IP67 WATER RESISTANT" - clean geometric sans-serif, medium weight, ALL CAPS, cream #F5F0E6, top-left of the badge grid, one line, preceded by a small cream #F5F0E6 water-droplet icon, cap height about 2.6% of frame height.
4) "TAP TO COUNT" - same style as text 3, top-right of the badge grid, preceded by a small cream #F5F0E6 check-in-circle icon.
5) "60-DAY GUARANTEE" - same style as text 3, bottom-left of the badge grid, preceded by a small cream #F5F0E6 check-in-circle icon.
6) "FREE US SHIPPING" - same style as text 3, bottom-right of the badge grid, preceded by a small cream #F5F0E6 check-in-circle icon.
No other text is allowed other than the ring's own display and gold logo; do not render a CTA button.

Legibility: Spell every word exactly as written, letter for letter, with the exact punctuation and case of each quoted string. High contrast on every element, all text fully inside 6% side margins, nothing touching the split line or the frame edge. Render only the six quoted strings plus the ring's own display and logo; do not render section labels or any other words from these instructions.

Avoid: any text, words, letters or numbers other than the quoted strings above and the ring's own display and logo; misspelled, warped, mirrored, duplicated or cut-off letters; section labels from this prompt; more than the two rings described; altered or invented ring label or logo; watermarks; other brand names or logos; star ratings, review counts, seals, awards, 'clinically proven', press logos, the word waterproof; showers, swimming, submerged hands, pools, bathtubs; prayer beads, mosque interiors, faces, people other than the one hand and wrist; extra fingers, fused hands, distorted anatomy; plastic CGI skin; cluttered background; text in the top 14% or below 67% of the frame.
```

## Budget
img_main 1 x 2.0 = 2.0 credits (est_credits). Variations excluded (3 x 2.0 = 6.0 if rendered).

## Self-check
Final: slot table written before the full prompt; 10 blocks in order; product fidelity sentence present; 9:16 stated in words; Avoid names truth risks (waterproof, showers, swimming, stars, badges). No slot marker or double brace remains. Hook type assigned: callout; angle ANG11, IP67 only.
