# ad_06 prompts — FINAL

## Swipe port — source: ErgoSalah · 71735717 (analysis: C:/Users/rayan/OneDrive/Desktop/ADS/ad-runs/2026-10-05-al-rayan-dhikr-ring/02-creative-research/gethookd/ergosalah-71735717/analysis.md)

Brand context: see next section. Frames viewed: 18 swipe frames (10 hook frames 0.0-4.5 s, 5.0, 6.0, 7.23 cut, 8.0, 9.0, 10.13 cut, 11.0, 12.0) + hook sheet + product PNG + store page screenshot.

Swipe teardown (12.1 s, 720x1280, native UGC phone footage, no speech, caption-led):
| t (s) | Beat | On screen (verbatim caption) | Visual |
|---|---|---|---|
| 0.0-2.2 | hook (wrong assumption) | "What muslim think i sell:" + sick/skull emoji, caption block at ~28-35% height | high-angle handheld, hand tosses a pillow onto a green prayer rug, woman in black hijab / grey abaya kneeling at left; motion from 0.5 s |
| 2.2-3.4 | contrast | "Vs..." | same shot, pillows beside kneeling woman |
| 3.5-6.9 | reveal | "What i actually sell.." + 3 soft emoji | whip-blur transition, new room, woman presses a beige plush mat |
| 7.0-10.1 | mechanism (feature) | "Padded prayer mat with memory foam and cushion in the knee area." | locked high-angle macro of plush mat |
| 10.1-12.1 | real use + offer | "Shop With 40% Off this Ramadan" (lower third) | woman lowers into sujood on the mat |
Palette: cream floor #F2EEE8, beige mat #D9BC96, green rug #3F6B2A, black hijab #1B1B1B, white caption. Type: bold rounded sans, sentence case, white with soft shadow, centred, no backing shape. Watermark brand logo mid-right (never ported). Hook = callout/pattern-inversion meme; psychology = in-group joke, benefit inferred in 3 s, real-use proof.

| Element | Swipe | Ours | Decision | Why |
|---|---|---|---|---|
| Beat order | wrong assumption / Vs... / reveal / feature / real use + offer | same order, 3 clips: assumption (C01) / Vs + reveal (C02) / real use + offer cue (C03) | KEEP | load-bearing |
| Hook frame | caption on frame 1 over "wrong" action | OVERLAY_1 meme caption in frame 0 of C01, motion in first second | KEEP structure, SWAP words | load-bearing; copy by copywriter |
| Wrong-vs-right in same room | pillow on rug vs plush mat, same living room | ordinary-looking black band on a hand in a meeting vs the same ring tapped silently, same conference room and persona | ADAPT | our "wrong" is what coworkers assume (plain ring), not a bad product |
| Persona | woman, black hijab, grey abaya | new persona P1: woman ~29, cream hijab, charcoal blazer, office | SWAP (modest, same avatar world) | never reuse likeness |
| Production level | native lo-fi phone footage | phone-camera realism, handheld micro-sway | KEEP | |
| Whip-blur transition | hard swish between rooms | plain cut at the edit (clips are separate) | DROP | incidental, Kling-unsafe |
| Caption style | white bold rounded sans, soft shadow, no box | white bold sans on deep-green #1F5A2E pill (video-prompting needs a backing), in start frame top band | SWAP (brand) | |
| Emojis | skull / sick / soft emoji | none (text rendering risk; Avoid) | DROP | incidental |
| Product | plush prayer mat | ring via @product reference | SWAP | |
| Feature caption | mat foam | spoken line only (pulse at 33/66/99 allowed A-2) | ADAPT | copywriter |
| Real use | sujood on mat | thumb tap under the table edge while the meeting goes on, display count visible | ADAPT | |
| Offer line | "Shop With 40% Off this Ramadan" | real offer only: $49.99, free US shipping, 60-day money-back; OVERLAY_3 = CTA cue | SWAP | TRUTH-RISK removed |
| Watermark brand logo | ErgoSalah | none | NEVER | |

Load-bearing kept: caption-first callout at 0.0 s, wrong-vs-right in one room, modest realistic person, real-use shot.
Truth replacements: "world's first", 40% off, knee-pain claims not ported; offer = intake only; no reward/iman claim; no "completely silent" (use silent tracking / quiet tap); no stats, no stars.
Q40 is persona-voice material only, never an attributed review.

## Brand context
- Palette (store_product_page.png: deep-green banners/buttons, white/cream, black text; product black or rose gold with gold logo, white 7-segment digits): background cream #F5EFE6 / white #FFFFFF · text black #111111 · accent deep green #1F5A2E (overlay pill backing, text white #FFFFFF) · product black #0B0B0B, gold logo #E6C77A, display digits white #FFFFFF.
- Font classes: caption overlays = bold clean geometric sans-serif (store: clean modern sans, bold headlines), sentence case or as approved, white on #1F5A2E pill.
- Product: Al Rayan Dhikr Ring 2.0, black variant. Packaging noun: none, the product is a ring (no pouch/box in these shots). Wide matte-black metal band with glossy inner edge; on its outer face a rectangular black display window with 4 white seven-segment digits (reference reads "5332") and, left of it, a small rectangular window with a gold heart/flame-shaped Al Rayan logo. Only legible words: the digits. Product PNG: C:/Users/rayan/OneDrive/Desktop/ADS/ad-runs/2026-10-05-al-rayan-dhikr-ring/00-intake/product_black.png (@product).
- Claims allowed (concept_slate A-1..A-13): tap to count, gentle vibrations at 33/66/99, silent tracking (brand-stated, never "100% silent"), looks like a ring, $49.99, free US shipping, 60-day money-back, 1-year tech warranty, Tirmidhi 3375 "keep your tongue moist" if copy uses it (exact wording + citation). Finger counting never knocked.

## Slot table (image)
n/a (video). In-frame overlay slots (rendered in start frames, copywriter fills the Overlay column of the script):
| slot | step | role | max words | max chars | font | color | zone | size |
|---|---|---|---|---|---|---|---|---|
| OVERLAY_1 | C01_frame | meme caption: what coworkers assume | 6 | 36 | bold clean geometric sans, sentence case as approved | white #FFFFFF on pill #1F5A2E | top band 15-27% height, 8-92% width, centered | cap height ~3.2% of frame |
| OVERLAY_2 | C02_frame | "Vs... / what it actually is" reveal caption | 6 | 36 | same | same | same | same |
| OVERLAY_3 | C03_frame | CTA cue (e.g. shop cue) | 4 | 24 | same | same | same | same |
Overlays must not repeat the spoken line; if the copy has fewer overlays the frame carries none and the Avoid line adds "any text".

## Video port + storyboard
Video port table (swipe 12.1 s; ours 10.2 s planned, within -20%):
| Swipe beat (t) | Our beat | Our line (copy_final ref) | Clip type | Target s |
|---|---|---|---|---|
| hook 0.0-2.2 + Vs 2.2-3.4 | assumption: "coworkers" see a normal ring in a meeting (hook payload by 3 s) | L1 pending | b-roll (scroll stopper) | 3.4 |
| reveal 3.5-6.9 | what it actually is: thumb tap, display, gentle pulse, silent | L2 pending | product-in-action | 3.4 |
| mechanism 7.0-10.1 + real use/offer 10.1-12.1 | real use in the meeting, quiet smile, single CTA | L3 pending | b-roll / product-in-action | 3.4 |

Storyboard skeleton (route web, Omni 5 s clips trimmed; 3 clips; ~7 words per line = 3.4 s):
| line | clip | type | dur / trim | start-frame description | motion / camera | audio | on-screen |
|---|---|---|---|---|---|---|---|
| L1 | C01 | surreal-scroll-stopper style b-roll (meme "wrong" beat) | 5 / 3.4 | P1 at conference table, left hand on notebook, ring looks like a plain black band; out-of-focus colleague opposite | colleague's eyes flick to her hand and give a small approving nod; her fingers tap the pen once; slow push-in <=5% | VO pending line L1 | in-frame OVERLAY_1 |
| L2 | C02 | product-in-action | 5 / 3.4 | macro of the same hand resting on her lap under the table edge, ring display "5332" visible, thumb touching the band | thumb taps twice, soft pulse ripple of light on the band; locked camera | VO pending line L2 | in-frame OVERLAY_2 |
| L3 | C03 | b-roll real use + CTA | 5 / 3.4 | P1 medium close-up, attentive to the meeting, left hand with ring at the table edge, mouth closed | thumb taps once, she gives a tiny private smile, hand stays; push-in <=5% | VO pending line L3 | in-frame OVERLAY_3 |

## Voice mode
`tts_narrator`: swipe has no speech, the meme is caption-led; one dry, amused creator voice-over over silent clips (nobody lip-syncs), cheaper (5 cr per clip) and consistent. Voice description (= `voice.description`): a young woman in her late 20s, General American accent, warm, low-key and dry-funny, conversational pace, like a quiet in-on-the-joke TikTok voice-over. Each clip carries one line (3 lines, ~7 words each, ~21 words total).

## Consistency blocks
```
PERSONA P1: a 29-year-old woman with warm light-brown skin, a neatly pinned cream crepe hijab covering hair and neck, warm brown eyes, natural skin texture, no visible makeup, small gold stud earrings partly visible, wearing a charcoal blazer over a white blouse; a wide matte-black smart ring on the ring finger of her left hand.
SETTING S1: a modern US office conference room: long light-oak table, open silver laptop, a black notebook and a pen, a white paper coffee cup, glass wall behind with soft out-of-focus colleagues, one colleague (man in a blue shirt, out of focus) seated across the table.
LIGHT L1: soft neutral 4500K overhead office light with daylight from a window at frame left, gentle shadows, phone-camera realism, slight grain.
```

## Scroll-stopper concepts
Ranked (reads in one frame / motion in 1 s / ties to hook & VOC / Kling-feasible):
1. **"Nice ring" nod** (chosen): meeting table, a colleague's eyes flick to her ring hand and he gives a small approving nod while she calmly taps a pen; reads as "they think it is just jewellery". Ties to Q40 ("passes as a regular ring"), Q22. Motion at 0.3 s (glance), one subject, feasible.
2. **Clicker turns heads (inverted wrong-beat)**: a red plastic clicker clicks and three colleagues turn their heads; whip to the silent ring. Ties to Q21 but multi-face, riskier; kept as alternate hook visual only.
3. **Pulse in the meeting**: macro of the ring hand under the table, a soft ripple on the band at the pulse while the table above stays still. Ties to A-2; better as C02 than a hook.
Retention-beat concept: C02 reveal cut (hard cut to macro, thumb tap + ripple) at ~3.4 s; copy may add "keep watching".

## Prompts
No competitor media is referenced.

### C01_frame — nano_banana_pro · 9:16 · 2k · refs: @product
```text
Scene: P1 sits at the conference table in a quiet team meeting, seen from across the table at a slight angle. Her left hand rests on a black notebook in the foreground, a pen between her fingers; on her ring finger sits exactly one wide matte-black ring, worn with its display window turned toward her palm side so that only the plain polished black band is visible from the top, looking like an ordinary fashionable ring. Her face is turned slightly toward the speaker out of frame, attentive, mouth closed. Behind the table, out of focus, the colleague in the blue shirt is looking toward her hand.
PERSONA P1: a 29-year-old woman with warm light-brown skin, a neatly pinned cream crepe hijab covering hair and neck, warm brown eyes, natural skin texture, no visible makeup, small gold stud earrings partly visible, wearing a charcoal blazer over a white blouse.
SETTING S1: a modern US office conference room: long light-oak table, open silver laptop, a black notebook and a pen, a white paper coffee cup, glass wall behind with soft out-of-focus colleagues.
LIGHT L1: soft neutral 4500K overhead office light with daylight from a window at frame left, gentle shadows, phone-camera realism, slight grain.
Style: Authentic amateur phone video still, native UGC meme look, not a studio ad.
Camera: eye-level from across the table, handheld phone, 26mm wide lens, hand and ring in sharp focus, background softly blurred.
Composition: Vertical 9:16. The top band 15% to 27% holds the caption pill; her face at 32% to 46% of frame height, left of center; her left hand with the ring in the foreground at 46% to 54% of frame height, ring about 4% of frame height; the colleague blurred at the right at 34% to 48%; the band from 58% to 100% shows only the table surface and laptop edge.
Brand colors: Caption pill deep green #1F5A2E with white #FFFFFF text; cream hijab #F5EFE6; matte black ring #0B0B0B.
Product: Match the attached product reference image exactly: shape, label, colors, logo. Do not redesign, re-letter, simplify or recolor the label. Do not invent label text. Exactly one ring, worn on the ring finger, band width and glossy edges as in the reference; display window hidden on the palm side in this shot.
Text: Render exactly one text element: "WHAT MY COWORKERS SEE" in ALL CAPS in bold clean geometric sans-serif, white #FFFFFF, centered inside a solid deep-green #1F5A2E rounded pill, top band 15% to 27% of frame height, 8% to 92% of frame width, cap height about 3.2% of frame height.
Legibility: Spell the quoted string exactly, letter for letter (W-H-A-T M-Y C-O-W-O-R-K-E-R-S S-E-E), with its capitalization and punctuation. High contrast, fully inside the frame with 6% side margins. Render only that string; do not render section labels or any other words.
Avoid: any text other than the quoted overlay; emojis; logos, brand names or watermarks; a second ring; extra fingers or fused hands; distorted face; stars, badges, doctors or lab coats; faces or hands in the bottom 40% of the frame.
```

### C01_clip — kling3_omni_web · 720p · 9:16 · 5 s (trim 3.4) · sound off · fallback kling3_0 std 4 s sound off
```text
The colleague across the table glances at the woman's ringed hand and gives a small approving nod. 0-1s: his eyes flick to her hand while she taps her pen once against the notebook. 1-2.4s: he nods slightly and looks back toward the speaker; she keeps her calm, attentive look. 2.4-5s: both hold still. Vertical 9:16, one continuous shot, no cuts, starting exactly from the start frame. Camera: very slow push-in of about 4 percent. Her expression stays calm and attentive. Nobody speaks; mouths stay closed. Ambient only: no sound. Keep the ring exactly as in the start frame, a plain black band, and keep her face, hair and clothing identical to the start frame. All text in the start frame stays exactly as it is, unchanged and still. Do not add any text, captions, subtitles, logos or watermarks.
```

### C02_frame — nano_banana_pro · 9:16 · 2k · refs: @product, C01_frame (identity)
```text
Scene: Close-up of P1's left hand resting on her charcoal-blazer lap just under the edge of the conference table, her thumb touching the matte-black ring on her ring finger; the ring's display window faces the camera and shows four white seven-segment digits and the small gold logo window beside it. The table edge and a sliver of the laptop are visible above, softly blurred; no face in frame except the lower edge of her cream hijab at the top right, blurred.
Attached image 1 is the product reference. Attached image 2 is the identity reference for the woman: same skin tone, hijab, blazer and outfit.
PERSONA P1: a 29-year-old woman with warm light-brown skin, a neatly pinned cream crepe hijab, wearing a charcoal blazer over a white blouse.
SETTING S1: a modern US office conference room: long light-oak table edge, open silver laptop above, glass wall behind with soft out-of-focus colleagues.
LIGHT L1: soft neutral 4500K overhead office light with daylight from a window at frame left, gentle shadows, phone-camera realism, slight grain.
Style: Authentic amateur phone macro still, native UGC, not a studio ad.
Camera: low close-up from the side at lap height, handheld phone, 35mm lens, ring and thumb in sharp focus, background softly blurred.
Composition: Vertical 9:16. The top band 15% to 27% holds the caption pill; the hand and ring occupy 30% to 52% of frame height, centered slightly left; the ring about 18% of frame height with its display fully visible and facing the camera; table edge at 14% to 20% at the very top, blurred; the band from 58% to 100% shows only blazer fabric and floor, blurred.
Brand colors: Caption pill deep green #1F5A2E with white #FFFFFF text; ring matte black #0B0B0B, gold logo #E6C77A, digits white #FFFFFF.
Product: Match the attached product reference image exactly: shape, label, colors, logo. Do not redesign, re-letter, simplify or recolor the label. Do not invent label text. Exactly one ring, display window readable and facing the camera within 20 degrees, digits identical to the reference, thumb beside the display not covering it, ring height about 18% of frame height.
Text: Render exactly one text element: "VS... WHAT IT ACTUALLY IS" in ALL CAPS in bold clean geometric sans-serif, white #FFFFFF, centered inside a solid deep-green #1F5A2E rounded pill, top band 15% to 27% of frame height, 8% to 92% of frame width, cap height about 3.2% of frame height.
Legibility: Spell the quoted string exactly, letter for letter (V-S, three dots, W-H-A-T I-T A-C-T-U-A-L-L-Y I-S), with its capitalization and punctuation. High contrast, fully inside the frame with 6% side margins. Render only that string and the ring's own display digits; do not render section labels or any other words.
Avoid: any text other than the quoted overlay and the ring's own digits; emojis; logos, brand names or watermarks; a second ring; extra fingers or fused hands; changed digits; stars, badges, doctors or lab coats.
```

### C02_clip — kling3_omni_web · 720p · 9:16 · 5 s (trim 3.4) · sound off · fallback kling3_0 std 4 s sound off
```text
Her thumb taps the black ring twice under the table edge while a soft pulse of light ripples across the band. 0-1s: the thumb presses the ring once. 1-2s: it presses a second time and a gentle ripple of faint white light spreads over the band, as a quiet vibration. 2-5s: the hand settles and stays still. Vertical 9:16, one continuous shot, no cuts, starting exactly from the start frame. Camera locked off. Nobody speaks; mouths stay closed. Ambient only: no sound. Keep the ring, its display and its logo exactly as in the start frame; the display digits stay sharp and unchanged; the ring does not rotate. Keep her hand, sleeve and clothing identical to the start frame. All text in the start frame stays exactly as it is, unchanged and still. Do not add any text, captions, subtitles, logos or watermarks.
```

### C03_frame — nano_banana_pro · 9:16 · 2k · refs: @product, C01_frame (identity)
```text
Scene: P1 in medium close-up at the conference table, attentive to the meeting, her gaze toward the speaker out of frame, mouth closed. Her left hand rests at the table edge in the lower foreground with the matte-black ring on the ring finger, thumb resting on the band. The white paper coffee cup and notebook sit nearby. The colleague in the blue shirt is blurred in the background.
Attached image 1 is the product reference. Attached image 2 is the identity reference for the woman: same face, hair covering, skin and outfit.
PERSONA P1: a 29-year-old woman with warm light-brown skin, a neatly pinned cream crepe hijab covering hair and neck, warm brown eyes, natural skin texture, no visible makeup, small gold stud earrings partly visible, wearing a charcoal blazer over a white blouse.
SETTING S1: a modern US office conference room: long light-oak table, a black notebook, a white paper coffee cup, glass wall behind with soft out-of-focus colleagues.
LIGHT L1: soft neutral 4500K overhead office light with daylight from a window at frame left, gentle shadows, phone-camera realism, slight grain.
Style: Authentic amateur phone video still, native UGC, not a studio ad.
Camera: eye-level, slightly from the side, handheld phone, 30mm lens, face and hand in focus, background softly blurred.
Composition: Vertical 9:16. The top band 15% to 27% holds the caption pill; her face at 30% to 44% of frame height, center-left; her hand with the ring at 46% to 54% of frame height, ring about 5% of frame height with display turned toward the camera; the band from 58% to 100% shows only table surface and blazer.
Brand colors: Caption pill deep green #1F5A2E with white #FFFFFF text; cream hijab #F5EFE6; ring matte black #0B0B0B.
Product: Match the attached product reference image exactly: shape, label, colors, logo. Do not redesign, re-letter, simplify or recolor the label. Do not invent label text. Exactly one ring on the ring finger.
Text: Render exactly one text element: "FREE US SHIPPING" in ALL CAPS in bold clean geometric sans-serif, white #FFFFFF, centered inside a solid deep-green #1F5A2E rounded pill, top band 15% to 27% of frame height, 8% to 92% of frame width, cap height about 3.2% of frame height.
Legibility: Spell the quoted string exactly, letter for letter (F-R-E-E U-S S-H-I-P-P-I-N-G), with its capitalization and punctuation. High contrast, fully inside the frame with 6% side margins. Render only that string and the ring's own digits; do not render section labels or any other words.
Avoid: any text other than the quoted overlay and the ring's own digits; emojis; logos, brand names or watermarks; a second ring; extra fingers or fused hands; distorted face; stars, badges, doctors or lab coats.
```

### C03_clip — kling3_omni_web · 720p · 9:16 · 5 s (trim 3.4) · sound off · fallback kling3_0 std 4 s sound off
```text
The woman gives one quiet thumb tap on her ring and a tiny private smile while the meeting carries on. 0-1.2s: her thumb presses the ring once. 1.2-2.6s: the corners of her mouth lift in a small closed-mouth smile and her eyes stay on the speaker. 2.6-5s: she settles, hand still on the table edge. Vertical 9:16, one continuous shot, no cuts, starting exactly from the start frame. Camera: very slow push-in of about 4 percent. Nobody speaks; mouths stay closed. Ambient only: no sound. Keep the ring exactly as in the start frame and keep her face, hair and clothing identical to the start frame. All text in the start frame stays exactly as it is, unchanged and still. Do not add any text, captions, subtitles, logos or watermarks.
```

### vo — text2speech_v2 · elevenlabs · voice_id pick
```text
Coworkers think I'm fidgeting with a ring. It's my tas-beeh. Silent tracking, gentle vibration. Sixty days, money back. Tap Shop Now.
```

## Variations
n/a for video.

## Budget
3 start frames x 2.0 = 6.0 · 3 Omni 5 s sound-off clips x 5.0 = 15.0 · vo 0.6 x ceil(~130 chars / 160) = 0.6 → est 21.6 credits.

## Self-check
Phase A only. Open: copy fit (3 overlays, 3 ~7-word lines); display digits cannot count up in Kling (digits stay "5332"); display-hidden ring in C01 may render with the window visible, QA must check; copywriter chooses meme wording; no competitor name or media referenced.

## Final script mapping (copy_final.md, approved round 1)
| L | line | words | clip | dur / trim | planned t | overlay (in start frame) |
|---|---|---|---|---|---|---|
| L1 | Coworkers think I'm fidgeting with a ring. | 7 | C01 | 5 / 3.4 | 0.0-2.8 | "WHAT MY COWORKERS SEE" |
| L2 | It's my tasbih. Silent tracking, gentle vibration. (spoken: tas-beeh) | 7 | C02 | 5 / 3.4 | 3.4-6.2 | "VS... WHAT IT ACTUALLY IS" |
| L3 | Sixty days, money back. Tap Shop Now. | 7 | C03 | 5 / 3.4 | 6.8-9.6 | "FREE US SHIPPING" |
Total 10.2 s planned. All lines are VO (tts_narrator, nobody lip-syncs; copy's ON-CAM tag on L1 becomes VO). Fallback clips: kling3_0 std, 4 s, sound off.
Mapping notes: copy_final's persona note says black hijab; P1 keeps the cream hijab to avoid resemblance to the swipe. Copy's "display count climbs / pulse at 33" cannot be rendered by Kling: digits stay as in the reference, a soft ripple shows the pulse. The whip-pan is a plain cut at assembly. C01 shows one colleague instead of three.
