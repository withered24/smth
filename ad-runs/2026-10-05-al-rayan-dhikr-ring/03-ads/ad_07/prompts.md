# ad_07 prompts — FINAL

## Swipe port — source: Weslamic · meta-2379413312864003 (analysis: 02-creative-research/social/meta-2379413312864003/analysis.md)
Teardown, keep/swap table and video port from Phase A are unchanged in substance (hands-only macro demo; competitor bag/box, app screen and charging beats dropped; 9:16, single narrator VO).
Final port mapping: L1 (swipe 0.0-3.8 hook+demo) -> C01 tap + pulse; L2 (3.8-7.6 usage/mechanism) -> C02 quiet double tap with slack beads; L3 (7.6-10.7 proof/CTA) -> C03 ring held to camera + TAP SHOP NOW.

## Brand context
Palette: rose gold ring #D9A692, black #111111, cream #F5EFE6, deep green #1F5A2E (pill + mat), white #FFFFFF, gold #D4A84B (logo). Fonts: bold clean sans-serif ALL CAPS overlays. Product: finger ring (rose-gold band, black display window with white 7-segment digits, gold logo square). PNG: 00-intake/product_rose_gold.png.

## Slot table (image)
n/a (video). Overlays filled: OVERLAY_1 "AFTER SALAH" (C01_frame), OVERLAY_2 "TAP SHOP NOW" (C03_frame).

## Video port + storyboard
| line | clip id | clip type | dur / trim (s) | start-frame description | motion / camera | audio | on-screen text |
|---|---|---|---|---|---|---|---|
| L1 | C01 | surreal-scroll-stopper | 5 / 3.8 | macro rose-gold ring on index finger, display 0032, thumb poised, prayer mat | thumb tap, 0032 to 0033, ripple; push-in 5% | VO: "Watch this. Thirty-three taps, then it pulses." (8 w, 3.8 s) | in-frame: "AFTER SALAH" + captions |
| L2 | C02 | product-in-action | 5 / 3.4 | hand on mat, ring display 0010, slack wooden bead strand beside, open ring box blurred | two tiny thumb taps, display 0010 to 0012, nothing else moves; locked | VO: "No beads to drop. Just quiet taps." (7 w, 3.4 s) | captions |
| L3 | C03 | product-in-action | 5 / 3.4 | two hands hold the rose-gold ring to camera, display 0033 | one soft pulse ripple; pull-out 5% | VO: "Sixty days to try it. Money back." (7 w, 3.4 s) | in-frame: "TAP SHOP NOW" + captions |
Planned: L1 0.0-3.5, L2 3.9-7.0, L3 7.3-10.4; assembled 10.6 s (target 10, limit 11). Hook payload "Watch this." lands by 1 s.

## Voice mode
tts_narrator (hands-only macro, nobody lip-syncs). Voice description: Calm young woman, about 28, soft and warm, close to the mic, like a friend sharing a small find; General American accent, medium-slow pace, no hype. voice_id "pick" (orchestrator assigns). No faith words in the VO, so no phonetic spelling needed.

## Consistency blocks
HANDS H1: a right hand of a woman in her late 20s with warm light-brown skin, slim fingers, short natural bare nails, no other jewelry, a thin cream-coloured knit cuff visible at the wrist.
SETTING S1: a warm light-oak desk edge beside a folded deep-green #1F5A2E prayer mat with a simple cream border (no pattern text, no calligraphy), soft cream wall far behind out of focus.
LIGHT L1: soft 3500K window light from frame left, gentle falloff, warm highlights on the rose gold, phone-camera realism, slight grain.

## Scroll-stopper concepts
Chosen: macro thumb-tap with ripple pulse on the lit display (C01), reads in one frame, motion within 1 s, ties to hook H1 and Q20. Alternates: slipping beads vs steady ring (Q29); pulsing ring on the mat in the dark.

## Prompts
### C01_frame — nano_banana_pro · 9:16 · 2k · refs: @product
```text
Scene: Extreme close-up of H1's right hand, index finger raised, wearing exactly one rose-gold smart ring. The ring's black display window faces the camera and shows the white seven-segment digits "0032". H1's thumb hovers just above the ring's outer face, about to tap it. The prayer mat edge and oak desk are soft in the background.
HANDS H1: a right hand of a woman in her late 20s with warm light-brown skin, slim fingers, short natural bare nails, no other jewelry, a thin cream-coloured knit cuff visible at the wrist.
SETTING S1: a warm light-oak desk edge beside a folded deep-green #1F5A2E prayer mat with a simple cream border (no pattern text, no calligraphy), soft cream wall far behind out of focus.
LIGHT L1: soft 3500K window light from frame left, gentle falloff, warm highlights on the rose gold, phone-camera realism, slight grain.
Style: Authentic UGC phone macro video still, native lo-fi, not a studio ad, slight grain, natural skin texture.
Camera: Eye-level macro, slightly above the hand, 35mm phone lens, ring and thumb in sharp focus, background softly blurred, handheld feel.
Composition: Vertical 9:16. The ring occupies 28% to 48% of frame height and is centered horizontally; the display digits sit at 33% to 41% of frame height; the thumb enters from the lower right and hovers at 44% to 54%; the top band 14% to 30% holds one text pill; the band from 55% to 100% shows only blurred desk, mat and wrist.
Brand colors: rose gold ring (as in the reference), black display, warm cream #F5EFE6 highlights, deep green #1F5A2E for the text pill and the mat in the blur.
Product: Match the attached product reference image exactly: shape, label, colors, logo. Do not redesign, re-letter, simplify or recolor the label. Do not invent label text. Exactly one ring worn on the index finger, display window facing the camera within 20 degrees, white 7-segment digits reading "0032", gold logo square visible left of the display, ring height about 20% of frame height, no finger covering the display or logo.
Text blocks: Render exactly one text element: 1) "AFTER SALAH" - bold clean sans-serif, bold, ALL CAPS, white #FFFFFF on a rounded pill backing #1F5A2E, on one line, centred in the top band 14% to 30% of height, 8% to 92% of width at most, cap height about 3.2% of frame height.
Legibility: The text "AFTER SALAH" is spelled A-F-T-E-R S-A-L-A-H, high contrast, fully inside the frame. The ring digits "0032" are spelled zero-zero-three-two. Render only the quoted string and the ring's own digits; do not render section labels or any other words.
Avoid: any other text, letters or numbers; a face; a second ring; a phone; extra or fused fingers; plastic CGI skin; competitor logos or packaging; stars, badges, seals; text in the bottom 35% of the frame.
```
### C02_frame — nano_banana_pro · 9:16 · 2k · refs: @product, C01_frame
```text
Attached image 1 is the product reference. Attached image 2 is the identity reference for the hand: same skin, fingers, nails and cuff.
Scene: Close-up of H1's right hand resting on the folded deep-green prayer mat, wearing exactly one rose-gold smart ring on the index finger, its black display facing the camera and showing the white digits "0010". The thumb rests beside the ring, ready to tap. A plain wooden prayer-bead strand lies slack and still on the mat beside the hand, and the edge of an open charcoal ring box is softly blurred at the upper left. No phone anywhere in frame.
HANDS H1: a right hand of a woman in her late 20s with warm light-brown skin, slim fingers, short natural bare nails, no other jewelry, a thin cream-coloured knit cuff visible at the wrist.
SETTING S1: a warm light-oak desk edge beside a folded deep-green #1F5A2E prayer mat with a simple cream border (no pattern text, no calligraphy), soft cream wall far behind out of focus.
LIGHT L1: soft 3500K window light from frame left, gentle falloff, warm highlights on the rose gold, phone-camera realism, slight grain.
Style: Authentic UGC phone video still, native lo-fi, not a studio ad, slight grain.
Camera: Slightly above, 45-degree angle, 35mm phone lens, ring and hand in sharp focus, background soft, locked off.
Composition: Vertical 9:16. Ring centered, 30% to 48% of frame height, display at 35% to 42%; hand enters from the right; the bead strand lies lower left at 46% to 54%; the top band 14% to 30% shows only soft background; the band from 55% to 100% shows only mat and desk, no ring, face or beads.
Brand colors: rose gold ring, black display, cream #F5EFE6 mat border, deep green #1F5A2E mat, plain light-wood beads.
Product: Match the attached product reference image exactly: shape, label, colors, logo. Do not redesign, re-letter, simplify or recolor the label. Do not invent label text. Exactly one ring, display facing the camera within 20 degrees, digits "0010", gold logo square left of the display, ring height about 18% of frame height.
Legibility: The ring digits "0010" are spelled zero-zero-one-zero. Render only the ring's own digits; no other words.
Avoid: any text, letters or numbers other than the ring's own digits; calligraphy or text on the mat or box; a face; a phone; a second ring; extra or fused fingers; competitor logos; stars, badges.
```
### C03_frame — nano_banana_pro · 9:16 · 2k · refs: @product, C01_frame
```text
Attached image 1 is the product reference. Attached image 2 is the identity reference for the hands: same skin, fingers, nails and cuff.
Scene: Medium close-up of H1's two hands holding exactly one rose-gold smart ring up toward the camera between the thumb and index finger of both hands, the ring's black display window facing the camera and showing the white digits "0033". The folded deep-green prayer mat and oak desk are soft in the background.
HANDS H1: a right hand of a woman in her late 20s with warm light-brown skin, slim fingers, short natural bare nails, no other jewelry, a thin cream-coloured knit cuff visible at the wrist. Both hands are H1's, with the same knit cuffs.
SETTING S1: a warm light-oak desk edge beside a folded deep-green #1F5A2E prayer mat with a simple cream border (no pattern text, no calligraphy), soft cream wall far behind out of focus.
LIGHT L1: soft 3500K window light from frame left, gentle falloff, warm highlights on the rose gold, phone-camera realism, slight grain.
Style: Authentic UGC phone video still, native lo-fi to semi-polished, not a studio ad.
Camera: Eye-level, straight-on, 35mm phone lens, ring in sharp focus, background soft, locked off.
Composition: Vertical 9:16. The ring is centered at 34% to 50% of frame height, ring height about 16% of frame height, display at 39% to 45%; hands enter from the lower left and lower right and hold it at 46% to 54%; the top band 14% to 30% holds one text pill; the band from 55% to 100% shows only soft mat and desk.
Brand colors: rose gold ring, black display, cream #F5EFE6 highlights, deep green #1F5A2E for the text pill and the mat.
Product: Match the attached product reference image exactly: shape, label, colors, logo. Do not redesign, re-letter, simplify or recolor the label. Do not invent label text. Exactly one ring, display facing the camera within 20 degrees, digits "0033", gold logo square left of the display, no finger covering the display or logo.
Text blocks: Render exactly one text element: 1) "TAP SHOP NOW" - bold clean sans-serif, bold, ALL CAPS, white #FFFFFF on a rounded pill backing #1F5A2E, on one line, centred in the top band 14% to 30% of height, 8% to 92% of width at most, cap height about 3.2% of frame height.
Legibility: The text "TAP SHOP NOW" is spelled T-A-P S-H-O-P N-O-W, high contrast, fully inside the frame. The ring digits "0033" are spelled zero-zero-three-three. Render only the quoted string and the ring's own digits; do not render section labels or any other words.
Avoid: any other text, letters or numbers; a face; a second ring; a phone; a box with logos; extra or fused fingers; competitor logos or packaging; stars, badges, seals, price tags; text in the bottom 35% of the frame.
```
### vo — text2speech_v2 · elevenlabs · voice_id pick
```text
Watch this. Thirty-three taps, then it pulses. No beads to drop. Just quiet taps. Sixty days to try it. Money back.
```
### C01_clip — kling3_omni_web · 720p · 9:16 · 5 s (trim 3.8) · sound off · fallback kling3_0 std 4 s sound off
```text
A thumb taps the rose-gold ring and a soft pulse ripples out across the prayer mat. 0-0.8s: the thumb presses down on the ring once. 0.8-2s: the display changes from 0032 to 0033 and a faint soft rose-gold ripple of light spreads out from the ring and fades. 2-3.8s: the thumb lifts away and the hand holds still. 3.8-5s: the hand stays still. Vertical 9:16, one continuous shot, no cuts, starting exactly from the start frame. Camera: slow push-in of about 5 percent. Nobody speaks; no face in frame. Keep the ring, its display, digits and logo exactly as in the start frame; the ring does not rotate and the label stays sharp. Keep the hand identical to the start frame. All text in the start frame stays exactly as it is, unchanged and still. Do not add any text, captions, subtitles, logos or watermarks.
```
### C02_clip — kling3_omni_web · 720p · 9:16 · 5 s (trim 3.4) · sound off · fallback kling3_0 std 4 s sound off
```text
Two tiny thumb taps tick the ring's display up on the prayer mat while nothing else moves. 0-1.4s: the thumb taps the ring twice, very small and quick, and the display changes from 0010 to 0011 to 0012. 1.4-3.4s: the thumb rests and the hand stays still, the bead strand on the mat does not move. 3.4-5s: everything rests still. Vertical 9:16, one continuous shot, no cuts, starting exactly from the start frame. Camera: locked off. Nobody speaks; no face in frame. Keep the ring, its display, digits and logo exactly as in the start frame; the ring does not rotate and the label stays sharp. Keep the hand identical to the start frame. Do not add any text, captions, subtitles, logos or watermarks.
```
### C03_clip — kling3_omni_web · 720p · 9:16 · 5 s (trim 3.4) · sound off · fallback kling3_0 std 4 s sound off
```text
Two hands lift the rose-gold ring toward the camera and it gives one soft pulse. 0-1.4s: the hands raise the ring slightly closer to the camera and hold it steady. 1.4-3s: one faint soft rose-gold ripple of light spreads out from the ring and fades while the display stays lit on 0033. 3-3.4s: the hands hold still. 3.4-5s: the hands hold still. Vertical 9:16, one continuous shot, no cuts, starting exactly from the start frame. Camera: slow pull-out of about 5 percent. Nobody speaks; no face in frame. Keep the ring, its display, digits and logo exactly as in the start frame; the ring does not rotate and the label stays sharp. Keep the hands identical to the start frame. All text in the start frame stays exactly as it is, unchanged and still. Do not add any text, captions, subtitles, logos or watermarks.
```

## Variations
n/a (video)

## Budget
3 frames x 2.0 = 6.0 · 3 clips x 5.0 = 15.0 · vo 0.6 (about 118 characters) = 21.6 credits.

## Self-check
B5 boxes ticked (see validator). Mapping: L1/L2/L3 one line per clip; overlays AFTER SALAH and TAP SHOP NOW baked into C01/C03 start frames. Notes: C03 shows only the rose-gold ring (black-ring reference not registered; brief says this ad uses rose gold); display digits 0032/0010/0033 are display states, not label text; C02 follows chief note (quiet double-thumb tap, digits ticking, nothing else moving).
