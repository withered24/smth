# Rewrite round — shared context for every agent

Run folder (all paths below are relative to it): `ad-runs/2026-10-05-al-rayan-dhikr-ring/`
Product: **Al Rayan Dhikr Ring 2.0** (smart tasbih ring), store https://alrayanrings.net. Name is fixed, never renamed.

This round rewrites the **copy** of 11 existing ads (8 image, 3 video). Images and video clips are already rendered.
For image ads we rewrite everything text-based: hooks, primary text, Meta headlines, Meta description, CTA line, and
the on-image text (on-image changes need a re-render, so only change on-image text when it is clearly worth it and say so).
For video ads (06, 07, 08) we rewrite the **script**: spoken lines (VO / on-cam), overlay text, captions, plus the
primary text, headlines and hooks. Keep each line mapped to the existing clips and their timings (see
`04-assets/ad_XX/clip_args.txt`, `04-assets/ad_XX/prompts/`, `04-assets/ad_XX/frames/`) so only the voice-over needs
re-recording. If a clip itself must change, say so explicitly as a "clip change" note — don't silently assume it.

## Read these in full before working (required)
1. `00-intake/intake.md` — product facts, offer, user constraints.
2. `00-intake/user_market_research.md` — the user's full market research (VOC table, competitors, fiqh notes).
3. `01-research/avatar_sheet.md`, `01-research/master_avatar_research.md`, `01-research/necessary_beliefs.md`,
   `01-research/offer_brief.md` (incl. "Verified Islamic sources", "Claims we CAN/CANNOT say").
4. For your ad: `03-ads/ad_XX/brief.md`, `03-ads/ad_XX/copy_final.md` (the copy being rewritten),
   `03-ads/ad_XX/chief_notes_v*.md`, and the ad's entry in `03-ads/_assign.json` and `03-ads/concept_slate.md`.
5. Look at the creative: image ads → `report_media/ad_XX_main.jpg` and any `report_media/ad_XX_img_v*.jpg`;
   video ads → `report_media/ad_XX_poster.jpg`, `04-assets/ad_XX/frames/*.png`, `04-assets/ad_XX/script_display.txt`,
   `04-assets/ad_XX/prompts/*.txt`. Copy must match what is actually in the picture.
6. Optional but useful: the swipe the ad was built from, under `02-creative-research/` (folder named in `_assign.json` `src`).
7. The user's rebuilt store pages (unpublished, newer than the research): `../../alrayan-rebuild/html/product.html`
   and `index.html` (FAQ, specs, guarantee). Use them to check what the landing page will say.

## Hard rules (from the user + an independent review of the first round)
**Faith**
- Only Quran verses and hadith from offer_brief.md "Verified Islamic sources" (rows 1–13). Never Tirmidhi 3583 or Muslim 783.
  Quote wording exactly as in that table. Say what the dhikr earns, never what the ring earns. Never claim the ring raises
  iman, gives khushu', or earns reward. Never position the ring above Sunnah finger counting.
- Attribute correctly. Bukhari 6464 is the Prophet's ﷺ saying narrated by Aisha — write e.g. "The Prophet ﷺ said
  (narrated by Aisha): ..." not "Narrated by Aisha: '...'" which reads as her own words.
- Sahih Muslim 596a is 33 + 33 + 34 = 100. The ring pulses at 33, 66 and 99 — don't imply it marks the 100th.
- Wudu: fiqh guidance generally says move/adjust a ring so water reaches the skin beneath (some scholars say required
  if tight). Do NOT say "never take it off" or imply wudu is complete with the ring untouched. "IP67 water resistant,
  so wudu splashes are fine" / "it can stay on through wudu splashes" style is OK. Expect a comment-section audience
  that knows fiqh.
- Riya': don't make counts a brag ("I hit 2,400 today"). Dhikr is private.
- Men: a narration in Sahih Muslim is commonly cited against men wearing rings on the index/middle finger. Copy must not
  direct men to wear it on the index finger; flag any visual that shows a man doing so.
- "Rose gold" is a colour/tone of an alloy, not gold — never imply real gold (matters for men).

**Meta ad policy**
- Personal attributes: never assert or imply the viewer's religion (or other personal attributes). "Muslim at work?",
  "As a Muslim, you...", "Are you a revert?" are violations. Second-person + religious practice ("If you count after
  salah...", "If your husband is new to Islam...") is borderline — prefer situation/product framing ("Lost your dhikr
  count?", "After salah, the count stays on your finger") or first-person brand voice.
- No before/after body or "you" + negative self-perception framing.

**Truth / FTC**
- No fabricated testimonials. A first-person story ("I did a big dhikr week...", "Now I tap") voiced by an AI person or
  written in primary text reads as a customer endorsement; there are no verified Al Rayan customer quotes. Either
  (a) write it in the brand's own voice ("We hear this a lot: ..."), (b) make it clearly a relatable scenario in
  second person ("You do a big dhikr week. Then nothing."), or (c) frame it as the founder's own experience ONLY using the
  brand-stated founder line ("Built by a young Muslim woman who learned to navigate life with resilience and faith") — no
  invented founder details. VOC quotes from the research are paraphrase-risk: use as the avatar's language, never in
  quote marks attributed to a customer.
- No store metrics: no "85% consistency", "4.2x", "92%", "8,200+", star ratings, review counts.
- No superlatives ("world's most discreet"), no competitor names/prices/specs attacks.

## Allowed product claims
- $49.99 · free US shipping · 60-day money-back guarantee · 1-year tech warranty (product page + rebuilt store).
- Tap to count; small display shows the count; gentle vibrations at 33, 66 and 99; prayer-time alerts for five daily
  prayers; syncs with the Al Rayan app (history / habit tracking); IP67 water resistance; colours black and rose gold;
  sizes 16–22 mm; gold Al Rayan logo button on the ring (visible on product images); "silent tracking" (brand wording —
  never "completely silent").
- Do NOT quote a sale price or % off (unconfirmed). Do NOT state delivery speed, weight, IP68, "waterproof".

## Claims to use only with a [CONFIRM] tag (rebuilt store says them, owner hasn't confirmed)
- Works without your phone (ring counts on its own; app is optional).
- Free size exchanges.
- Battery 3–5 days of frequent use.
- That the "Al Rayan app" is a real branded app in the stores (if a line leans hard on the app, tag it).
If you use one, append ` [CONFIRM: <claim>]` right after it so the owner can check before running.

## Craft bar
- Hook lands in the first line / first second; specific scenes (meeting room, sink, car, bedside) beat abstractions.
- Every ad must stay clearly different from the other 10 (angle, hook, scene). Don't converge on the same "blame your
  tools" lines everywhere — use it at most where it is the angle.
- Plain, warm, tribe-correct vocabulary (dhikr, tasbih, istighfar, SubhanAllah, salah, wudu). No guilt or shame.
- Primary text: tight. Short lines. One CTA. Meta headline ≤ 40 chars. Video VO ~2.3–2.6 words/second; keep each
  line within its clip's duration.
- Keep the angle, avatar and swipe structure of the ad unless the critique shows the angle itself is the problem.
