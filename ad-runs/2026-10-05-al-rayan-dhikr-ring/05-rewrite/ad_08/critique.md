# ad_08 critique (video, POV overthinking walk, "Mind racing on your walk to work? Make it istighfar.")

Role: copy critic, not a rewrite. Reviewed: CONTEXT.md; intake; user market research; avatar sheet; master avatar research; necessary beliefs; offer brief; `03-ads/ad_08/brief.md`, `copy_final.md`, `chief_notes_v1.md`, `_assign.json` and `concept_slate.md` entries; `04-assets/ad_08/script_display.txt`, `clip_args.txt`, `prompts/*`, `audio/vo_words.json` (real Whisper timings), `captions.ass`; every start frame; a 1 fps contact sheet of the actual `final.mp4` (13.6 s); the swipe analysis; the other 10 ads' `copy_final.md`; the rebuilt store pages.

**Verdict in one line:** the concept (a racing mind on a city walk, turned into istighfar) is a good A1 scene and the structure is clean. But the hook asserts a mental state about the viewer, the Quran line is placed so it reads as "tap the ring and your heart is at ease", the ring is never named aloud, B1 and B4 are not actually installed by any spoken line, and the picture does not show what the words say (no tap, no walking, no ticking count, two women in one coat). Faith wording and metrics are mostly clean. Most of the fixes are VO, caption and primary-text changes; three are clip changes, flagged below.

---

## 0. What actually shipped (anchor for everything below)

Final = 4 clips, 13.6 s, VO 13.28 s. Clip windows come from `clip_args.txt`: C01 0-3.5, C02 3.5-6.6, C03 (a2) 6.6-9.7, C04 (a2) 9.7-13.6.

| Clip / window | VO as spoken (Whisper) | Burned caption (editable ASS) | Baked-in pill (in the start frame, NOT editable without a clip change) | What the picture shows (from the frames and the contact sheet) |
|---|---|---|---|---|
| C01 0-3.5 | "Mind racing on your walk to work?" 0.00-1.72, gap, "Make it istighfar." 2.16-3.28 | Mind racing on / your walk to work? / Make it istighfar | POV: your thoughts won't slow down | A POV arm in a camel coat reaches a palm toward the back of a second woman in a sage hijab and an identical camel coat, walking away. White scribbles circle the hand. The ring (5332) is on the hand. The arm swings and the ring hand drops back. No tap happens. |
| C02 3.5-6.6 | "Tap." 3.62, "Keep walking." 4.32-4.92, "The count keeps up." 5.38-6.30 | Tap / Keep walking / The count keeps up | none | Close-up of a raised hand, finger pointing up, ring at the base of what looks like the index finger, thumb below. The hand stays raised and nearly still. The display reads 5332 and never changes. No visible tap, no visible dissolve of scribbles, no walking motion except background blur. |
| C03 6.6-9.7 | "By the remembrance of Allah," 6.84-8.00, "hearts are assured." 8.44-9.30 | By the remembrance / of Allah / hearts are assured | QURAN 13:28 | A different woman from C01/C02: different face, blue-grey hijab, no bag. She stands facing camera, palm raised with scribbles fading beside her, then eyes closed and mouth slightly open at ~8 s (it reads as if she is reciting), then hand lowered. She is standing, not walking. |
| C04 9.7-13.6 | "Sixty-day money-back guarantee." 10.02-11.58, "Tap Shop Now." 12.20-13.06 | Sixty-day / money-back guarantee / Tap Shop Now | AL RAYAN DHIKR RING 2.0 (small, caps) | Profile of the same woman, open palm held up like a "stop" or wave, ring on the third finger, display too small to read. The hand does not tap. The background changes (a different street with parked cars) across the clip. |

Words per second per line (VO): L1 10 words in 3.3 s = 3.0 w/s (the hook sentence itself is 7 words in 1.7 s); L2 7 words in 2.7 s = 2.6; L3 8 words in 2.5 s = 3.2 (fastest line, and it is a Quran verse); L4 8 words in 3.0 s = 2.6. Overall 33 words in 13.3 s = 2.5, but unevenly distributed, with a 0.7 s pause before the CTA.

---

## 1. Hook strength and ranking

**First second as shipped.** VO starts at 0.0 ("Mind racing on your walk to work?"), caption "Mind racing on" at 0.0, a green pill "POV: your thoughts won't slow down" on screen, and a hand with a ring reaching toward the back of a woman. Text arrives immediately and the scene is real, which is good. The problems:

- Three layers say the same thing in the first 3.5 s: the pill ("your thoughts won't slow down"), the VO ("Mind racing"), and the caption ("Mind racing on"). The viewer learns nothing from the pill that the VO has not said. One of them should carry a different beat.
- The "POV" label is false. A POV shot would be the speaker's eyes. Here the POV arm reaches toward another woman's back, as if about to tap a stranger on the shoulder. It reads as "someone is following her", not "my thoughts are racing". The scribbles around the hand are an abstract thought-loop, but the framing gives the eye a different story first.
- Would an A1/A2 stop? A1 (a practising Muslim, 20-40, in a walking commute): probably a pause on "istighfar" at 2.2-3.3 s, because that is the in-group word, but it lands after the first two seconds. "Mind racing on your walk to work?" alone could be any meditation or ADHD ad. A2 (gift buyer): no signal at all; but this ad is A1, so that is fine.
- Policy risk in the hook itself (see 3): "Mind racing?" plus "your thoughts won't slow down" asserts or implies a mental-health state about the viewer, and it is second-person negative framing.

**Ranking of the six existing hooks** (as spoken or overlay hooks for this clip set):

1. **H1 "Mind racing on your walk to work? Make it istighfar."** Best of the six as built, because it names a scene and a turn in one line and "istighfar" is the tribe word. Weaknesses: mental-health-adjacent, "to work" narrows the scene (students, school run, lunch walk), and "Make it istighfar" is an imperative at the viewer's religious practice.
2. **H2 "My mind races the whole walk to work. So I tap."** The strongest structure (confession plus action, 11 words) and the closest to the swipe's "I started wearing this because I would think a lot". But as first-person it reads as a customer or creator endorsement from an AI persona, and there are no verified Al Rayan customer quotes. It needs reframing into brand voice ("We hear this a lot: ...") or a clear second-person scenario.
3. **H5 "What if every racing thought became a chance for istighfar?"** Good idea, but 11 words, "racing thought" again, and a question that asks the viewer to imagine rather than see.
4. **H6 "A steady rhythm of istighfar, even on the walk to work."** Calm, on-brief (echoes Q39), but flat. It does not interrupt anything.
5. **H4 "Watch this walk: one tap, one istighfar, keep going."** "Watch this walk" is empty, and the clips do not show one tap per istighfar (no tap is shown at all).
6. **H3 "You open your dhikr app and get pulled into social media."** Wrong ad. This is ad_04's whole angle (phone trap, Q30). Drop it.

---

## 2. Angle and avatar fit; awareness and sophistication; belief order

- **Angle fit: sound.** The A1 desire for "dhikr in dead moments" (avatar sheet, Short-Term Goals) and the commute-istighfar evidence (Q18, Q39, Q20) support this. Caveat: the VOC is a drive ("quiet drive between cities", "45-minute highway drive"), not a walk. The brief swapped to walking to avoid AI driving shots. That is fine for production, but the copy should not borrow the "1,000 in 20 minutes" claim. It correctly does not.
- **Distinct from the other 10 ads?** Yes on scene and angle: this is the only walk and the only istighfar-led ad. The overlap is in the closing lines (see 5).
- **Awareness and sophistication.** Problem-aware, stage 3. At stage 3 the lead should be the specific moment plus a usage mechanism. The ad has the moment but the mechanism is only "Tap. Keep walking. The count keeps up." The ring is never named or described aloud. At 13.6 s the viewer cannot tell what is being tapped.
- **Beliefs in order (B1 then B4): neither is actually installed by the script.**
  - B1 = "steady dhikr through my day matters, and a small constant habit beats a big rare one." The chief notes say it is "installed by the callout premise (reader already values istighfar) and L3 (Quran 13:28)". That is not installation. Quran 13:28 is about tranquility, not about steadiness or smallness. There is no Bukhari 6464 or Tirmidhi 3375 line anywhere in the script.
  - B4 = "a ring can count silently, without a phone, noise or a look at a screen." The VO says nothing about silent, phone-free, or screen-free. "The count keeps up" is about keeping pace, not silence. The only B4 content is visual, and the visual does not show a tap or the count changing.
  - What the script actually installs is a third promise, "tap, and your heart is at ease", which is not on the belief list and is the riskiest of the three (see 3).
- **Missing proof beat.** At stage 3 with a mechanism claim, one concrete fact would earn belief: the pulse at 33/66/99 (A-2), or "no click" (Q21). Neither is spoken.

---

## 3. Rule violations (quote the line)

### 3a. Faith accuracy and attribution

- **L3 VO "By the remembrance of Allah, hearts are assured."** The verified wording (offer_brief row 1) is "...Unquestionably, by the remembrance of Allah hearts are assured". The VO drops "Unquestionably" and begins with a capital "By", so it is a clipped fragment. A fragment is acceptable only if it does not change the meaning. Here the meaning does shift, because the full verse is addressed to "those who have believed", and the clipped version is placed straight after "Tap. Keep walking. The count keeps up." That sequence plus the visual (her shoulders drop, her eyes close, scribbles vanish) reads as: tap the ring, then hearts are assured. CONTEXT.md: "Say what the dhikr earns, never what the ring earns." The sequencing breaks the spirit of that rule even though the words are the Quran's. Treat this as a MUST FIX.
- **No spoken attribution.** The VO never says "Quran" or "Allah says"; only the baked-in pill "QURAN 13:28" does. A viewer with sound on and eyes elsewhere hears an unattributed quote. The pill itself is a bare citation; it shows no verse text, so the on-screen and spoken versions do not match each other (VO is the verse, pill is the reference, captions are a third chunking of the VO).
- **Primary text** repeats the clipped line: "By the remembrance of Allah hearts are assured. (Quran 13:28)". Same issue; quote the full verified clause and place it away from the "tap" sentence.
- **Better fit available in the verified table:** Quran 62:10 ("...disperse within the land... and remember Allah often that you may succeed") is literally about walking out into the day and remembering, and Quran 3:191 ("standing or sitting...") fits a walk. Muslim 2702 (the Prophet seeking forgiveness a hundred times a day) is the istighfar hadith that the angle is built on and the brief lists as an option, but the copy ignored it. Caution on 2702: it is 100, and the ring pulses at 33/66/99, so never imply the ring marks the 100th.
- **Never above finger counting / ring earns:** not violated in words. "Make it istighfar" attributes the dhikr to the viewer, not the ring. OK.

### 3b. Meta personal-attributes policy (religion, health)

- **L1 "Mind racing on your walk to work?" and pill "POV: your thoughts won't slow down".** Both describe a mental state of the viewer ("your thoughts"), in second person, in a negative-self-perception frame. Meta's personal-attributes rule covers implied mental-health conditions. "Mind racing / thoughts won't slow down" is anxiety-adjacent, and L3 then offers a Quran line that "assures hearts". The brief itself warned: "Avoid mental-health/anxiety cure claims". The shipped sequence (racing thoughts, tap, verse, shoulders drop) is exactly an anxiety-relief arc. MUST FIX. A situation-first hook ("the walk to work", "twelve quiet minutes", "the stretch between the train and the desk") avoids asserting anything about the viewer.
- **"Make it istighfar."** Second-person imperative about the viewer's religious practice. CONTEXT.md calls this borderline and says prefer situation or product framing, or first-person brand voice. SHOULD FIX (or reframe to "Some walks are istighfar walks" style situation framing).
- **H2 "My mind races the whole walk to work. So I tap." (alternate hook, not shipped in the VO).** If used, first-person plus an AI persona reads as a customer testimonial. There is no verified Al Rayan customer. Do not carry it into the rewrite without brand-voice or second-person reframing.

### 3c. Wudu fiqh, riya', men's finger, rose gold

- Wudu: not mentioned. Fine.
- Riya': no counts bragged. Fine. The ring shows 5332 on screen, which is the product image number, not a boast.
- **Men's finger / ring finger:** the ad is about a woman, so there is no direct violation. But C02 shows the ring at the base of what looks like the index finger of the raised hand (prompt said ring finger). If a male viewer or a later male edit copies this visual, it models the index-finger wear the Muslim narration cautions against. Flag for a regenerate or a check on any reuse. The ring finger shot in C03 and C04 is fine.
- Rose gold: not mentioned; black ring only. Fine.

### 3d. Fabricated testimonial risk

- Shipped VO and on-image copy are second person; no first-person claim. Good.
- Primary text: second person plus product description. Good.
- Hook H2 (see 3b) is the only risk, and it is not in the render.
- The persona is an AI-generated woman in photoreal UGC style. Beyond the copy, expect Meta's AI-content labelling. Not a copy fix, but do not write lines that imply she is a real customer ("I", "my").

### 3e. Unconfirmed or banned claims; store metrics

- No store metrics. No stars, no 85% or 4.2x. Clean.
- No weight, battery, IP68, "waterproof", "completely silent", "works without your phone", size exchange. Clean.
- "The count keeps up" is vague but not a claim of automatic counting. Clean. If the rewrite says "the phone stays in your pocket", it needs `[CONFIRM: works without your phone]`.
- Primary text: "no loud clicker and no beads in your pocket" is fine as product framing, but it drifts into ad_05 and ad_09 territory (see 5).
- Meta description "60-day money-back guarantee": fine.
- No sale price: correct.

---

## 4. Copy-to-creative mismatch (what the picture shows vs what the words say)

| Line | What it says | What the picture shows at that moment | Mismatch |
|---|---|---|---|
| L1 "Mind racing on your walk to work?" | A walk to work, a racing mind | A hand reaching toward another woman's back on a sidewalk; scribbles around the hand; no visible commute cues (no bag strap for work, no building entry, no train). The "POV" pill is not a POV of the speaker. | The scene reads as "following a stranger", not "my own thoughts". Two women in identical coats is confusing. |
| L2 "Tap." | A tap | A raised hand, ring up, still. No thumb tap. | Medium to high. The one verb in the ad's mechanism is not shown. |
| L2 "Keep walking." | Walking | A raised hand held still with a blurred street. | Medium. Motion is minimal. |
| L2 "The count keeps up." | The count climbing | Display reads 5332 the entire time. | High. This is the retention beat of the ad and the digits never change. |
| L2 (prompt) "each tap makes one scribble loop dissolve" | Scribbles dissolve | Scribbles stay thin and faint; no obvious dissolve | The visual metaphor (tap resolves the thought-loop) is lost. |
| L3 "By the remembrance of Allah, hearts are assured." | Calm | A different woman; eyes closed, mouth slightly open as if reciting, then standing still | Identity drift between C02 and C03 (different face, different hijab shade, no bag). The "shoulders drop" beat is not visible. She is standing, not on a walk. |
| L4 "Sixty-day money-back guarantee. Tap Shop Now." | Offer and CTA | A raised palm like a "stop" gesture; the ring face is too small to read; the street changes. Pill "AL RAYAN DHIKR RING 2.0" is tiny caps. | The product is not named in the VO and barely legible on screen. The gesture reads "stop" or "hi", not "tap". |

On-image text quality:

- **Pill 1 "POV: your thoughts won't slow down":** clean render and legible. Content issues in 3b. It sits over the first 3.5 s only.
- **Pill 2 "QURAN 13:28":** clean render. Gives only a reference, not the verse text. Looks like a verified citation but gives the viewer nothing to read.
- **Pill 3 "AL RAYAN DHIKR RING 2.0":** correct spelling, but it is the first and only time the product is named, in the last 3.9 s, at about 55% of the size of the other pills. Weak brand impression for a cold audience. This is the main reason the ring has to be named in VO.
- **Captions (ASS):** word-group captions at about 65% of the frame height. Legible. They sit over the hand and ring in C02, and over her coat in C03/C04. They are editable.

---

## 5. Clarity, rhythm, flab, clichés, repetition, overlap with the other 10 ads

- **Rhythm.** The short lines (L2 "Tap. Keep walking. The count keeps up.") are the best rhythm in the ad. L1 is rushed (hook sentence in 1.7 s). L3 is 8 words in 2.5 s: an eight-word verse fragment read at 3.2 w/s with a pause before "hearts" is too fast for a Quran line, and it is the emotional peak.
- **Flab and redundancy.** "Mind racing... thoughts won't slow down" is said twice in 3.5 s. The caption repeats the VO and the pill repeats both. L4 "Sixty-day money-back guarantee. Tap Shop Now." is serviceable, but "Tap" is now both the product verb (L2) and the button verb (L4). The word is overloaded.
- **Cliché.** "POV: ..." is the swipe's device and is fine for a UGC walk, but "Mind racing" is the category cliché of meditation and ADHD ads. In an Islamic ad the freshest thing is the specific dhikr word (istighfar), which currently lands late.
- **Missing.** No product name aloud, no price, no free shipping, no pulse, no "silent". The viewer finishes the ad not knowing what the object is, how much, or why it is better than the beads in their pocket.
- **Overlap with other ads:**
  - Closing line: ad_06 "Sixty days, money back. Tap Shop Now.", ad_07 "Sixty days to try it. Money back." (overlay TAP SHOP NOW), ad_08 "Sixty-day money-back guarantee. Tap Shop Now." Three video ads end on near-identical CTAs. Differentiate or at least vary the offer beat.
  - "Tap. ... Tap." phrasing appears in ad_01, ad_04, ad_05, ad_06, ad_07, ad_09, ad_10 as "Tap to count". Fine as product language, but here it is also the VO's second sentence and the CTA's first word.
  - Primary text line "no loud clicker and no beads in your pocket" overlaps ad_05 and ad_09 ("Beads scatter. Clickers shout.", "Retire the loud clicker"). Cut it; this ad does not need the us-vs-them.
  - Quran 13:28 and istighfar are used in no other ad. Good, keep them exclusive to ad_08. Quran 2:152 is ad_04's; Tirmidhi 3375 is ad_06 and ad_11; Bukhari 6464 is ad_01 and ad_07; Muslim 596a is ad_07. So the unused verified lines available to ad_08 without overlap are 13:28, 62:10, 3:191, 33:41 and Muslim 2702.
  - "The walk" and "commute" are unique to this ad (only ad_10 mentions walking, in passing).

---

## 6. Script timing (words per line vs clip durations)

| Line | VO window | Clip window | Words / seconds / w/s | Fit |
|---|---|---|---|---|
| L1 | 0.00-3.28 | C01 0-3.5 | 10 / 3.3 / 3.0 | Fits but rushed; "Mind racing on your walk to work?" is 1.7 s |
| L2 | 3.62-6.30 | C02 3.5-6.6 | 7 / 2.7 / 2.6 | Good. The best-paced line |
| L3 | 6.84-9.30 | C03 6.6-9.7 | 8 / 2.5 / 3.2 | Too fast for a verse; ends 0.4 s before the clip ends and is followed by 0.7 s of dead air |
| L4 | 10.02-13.06 | C04 9.7-13.6 | 8 / 3.0 / 2.6 | OK. Starts 0.3 s into the clip; no space to name the ring |

- **Total** 33 words in 13.28 s vs the 15 s target and the 13.6 s render: the ad is 1.4 s shorter than the brief, so there is no timing pressure to squeeze words. There is room for a slightly fuller L4 and a slower L3.
- **Overlay text** is only on-image in three baked pills (not editable) and the captions (editable). The Meta-spec "overlay ≤6 words" is met by the pills (5, 2, 5 words), but see the redundancy in 4.
- **Line to clip match.** The structure maps well: hook, tap, release, CTA. The mismatch is inside each clip (no tap, no count change, standing instead of walking), not the timing.
- **Practical limits for a VO-only rewrite** (at 2.3-2.5 w/s, VO starts at 0.0 and must end by ~13.2 s): C01 about 7-8 words, C02 about 6-7, C03 about 6-7 (slower, for the verse), C04 about 8-9. Total about 30-32.

---

## MUST FIX

1. **Remove the mental-state assertion.** Replace "Mind racing on your walk to work?" (VO + caption) and keep the baked pill "POV: your thoughts won't slow down" from carrying meaning alone. The pill cannot change without a **clip change** (C01 start frame), so either (a) write a VO that does not repeat it and lets the pill be a visual label, or (b) re-render C01 with a new pill. Situation framing ("the walk to work", "the stretch between the train and the desk") or a brand-voice line, not "your mind / your thoughts".
2. **Decouple the verse from the tap.** As built, "Tap. Keep walking. The count keeps up. By the remembrance of Allah, hearts are assured." plus the relieved visual says "the ring brings tranquility". Put the verse in a position and phrasing that credits the dhikr (e.g. "Allah's own words on remembrance"), use the full verified clause with "Unquestionably", say who said it, or swap to Quran 62:10 / 3:191 / 33:41, which fit a walk and do not promise a feeling. Also slow it to at most 6-7 words in ~3 s.
3. **Name the ring aloud, and say what it does.** Right now the product is never in the VO. One concrete mechanism line (tap, count on your finger, gentle pulse at 33, 66, 99) must be spoken, not only captioned. This also installs B4 for real.
4. **Install B1 for real or drop it from the brief.** One sentence of small-and-steady (Bukhari 6464, attributed correctly as "The Prophet ﷺ said (narrated by Aisha)", or Muslim 2702) is better than an unlinked verse. If 13:28 stays, B1 is not installed and the brief should say the ad carries B4 and a faith anchor only.
5. **Match the words to the picture for L2.** "Tap." and "The count keeps up." have no visible support. Either (a) **clip change**: re-render C02 with a visible thumb tap and digits ticking (e.g. 0033 rolling toward the pulse), or (b) rewrite L2 to describe what C02 does show (a ring on a raised hand, a still display) and not promise motion.
6. **Fix the first-frame story.** The hand reaching toward another woman's back reads as "touching a stranger". **Clip change** (C01): single woman, wrist-first POV from her own eyes, hand at hip, one tap. If no re-render is possible, write the opening VO so it does not say "POV" or "your" and treat the figure ahead as "the walk".

## SHOULD FIX

7. Change "Make it istighfar" from imperative at the viewer's practice to situation or product framing.
8. Different CTA from ad_06 and ad_07: vary the offer beat (add $49.99 and free US shipping; "sixty days to try it" is ad_07's line).
9. Pace: hook sentence under 2.5 w/s; verse under 2.5 w/s; use the 1.4 s of spare runtime and the 0.7 s dead air before L4.
10. Primary text: cut "no loud clicker and no beads in your pocket" (ad_05/09 territory), put the verse in full with correct attribution and not directly after "Tap the ring", and keep one CTA. Currently 6 short paragraphs; trim to 4.
11. Pill/caption redundancy in the first 3.5 s: give the captions different words than the pill, or kill the caption in C01.
12. C03/C04 identity drift (different woman, no bag, hijab shade) and the "stop-hand" gesture in C04. Flag for a clip change if budget allows; otherwise accept and avoid copy that depends on continuity ("she", "my").
13. Check the ring finger in C02 (looks like index). For any reuse, avoid it.
14. If a first-person hook is wanted (H2), reframe as brand voice ("We hear this a lot"). Do not voice "I" from the AI persona.

## KEEP (what works)

- The scene: a short city walk, morning light, the ring on the hand. Real, specific, and unique among the 11 ads.
- Istighfar as the dhikr: unique to this ad and the right word for the tribe.
- L2's rhythm ("Tap. Keep walking. The count keeps up.") as a pattern: three short beats, 2.6 w/s.
- Structure of the swipe (hook, mechanism, release, CTA) mapping cleanly to four clips at the right durations; VO-to-clip timing is actually well aligned.
- Single CTA, no store metrics, no sale price, no weight or battery claims, no competitor jabs.
- Quran 13:28 as an exclusive faith anchor for this ad (no other ad uses it), if reframed per MUST FIX 2.
- Word-by-word captions in a legible bold style (editable).

---

## Directions for the rewrite (3-5)

1. **Situation hook, not state hook.** Lead with the scene and the word istighfar inside the first 1.5 s, with no "you" + mental state. For example "The walk to work. Twelve minutes of istighfar waiting to happen." (check "twelve minutes" reads as a scenario, not a claim; or "Between the train and the desk, there's a dhikr in every step."). Keep it at most 7-8 words for C01.
2. **Give the ring a name and a verb in the middle.** C02 window (3.1 s, ~6-7 words): the product and the mechanism in one breath, e.g. "Al Rayan Dhikr Ring. One tap, one count." If the tap is not visible, either re-render C02 or phrase it as what the picture shows ("Your count, on your finger").
3. **Faith line that earns, then credits.** Use Quran 62:10 (disperse in the land, remember Allah often) or 33:41 for the walk, or Muslim 2702 with correct attribution. Say who said it, keep it to a slow ~6 words in ~3 s, and do not place it directly after "tap". If 13:28 stays, say "Allah says" / use "Unquestionably", and make the visual calm come from the walk, not from the tap.
4. **Make the close different from ad_06 and ad_07.** C04 has 3.9 s: "Al Rayan Dhikr Ring 2.0. $49.99. Sixty days to try it." or a variant with free US shipping, with the CTA word "Shop Now" only in the caption and button, not "Tap Shop Now" again.
5. **Install B1 once, in primary text if not in VO.** Primary text can carry "small and steady" with Bukhari 6464 properly attributed, and one line on counting on fingers remaining the Sunnah. This keeps the VO short and the faith framing complete without crowding a 13.6 s video.
