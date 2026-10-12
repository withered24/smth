# Worker brief — 3 Prompt Engineer (`adNN-pe`, Phase 3 triad)

## Placeholders (orchestrator fills all before spawning; Sonnet, `run_in_background: true`, name `ad10-pe`)
- `C:/Users/rayan/OneDrive/Desktop/ADS/ad-runs/2026-10-05-al-rayan-dhikr-ring` — absolute run folder, forward slashes, e.g. `C:/Users/rayan/OneDrive/Desktop/ADS/ad-runs/2026-10-04-nmn-powder`
- `ad_10` — e.g. `ad_03` (files live in `C:/Users/rayan/OneDrive/Desktop/ADS/ad-runs/2026-10-05-al-rayan-dhikr-ring/03-ads/ad_10/`)
- `ad10-pe` — e.g. `ad03-pe`
- `image` — `image` | `video`
- `swipe` — `swipe` | `new_concept` (the deliverable's creative route)
- `9:16` — images: from the brief (intake default `9:16`); video: always `9:16`
- `n/a` — video: `web` (Kling 3.0 Omni in the Higgsfield web UI; `preflight.omni_web` true) | `cli`
  (`kling3_0` std via the CLI from the start; `omni_web` false); image: `n/a`
- `C:/Users/rayan/OneDrive/Desktop/ADS/ad-runs/2026-10-05-al-rayan-dhikr-ring/03-ads/ad_10/brief.md` — `C:/Users/rayan/OneDrive/Desktop/ADS/ad-runs/2026-10-05-al-rayan-dhikr-ring/03-ads/ad_10/brief.md`
- `C:/Users/rayan/OneDrive/Desktop/ADS/ad-runs/2026-10-05-al-rayan-dhikr-ring/02-creative-research/gethookd/calm-collective-92336795/record.json` — absolute path to the swipe's `record.json`, or `none` (new concept)
- `C:/Users/rayan/OneDrive/Desktop/ADS/ad-runs/2026-10-05-al-rayan-dhikr-ring/02-creative-research/gethookd/calm-collective-92336795/media.jpg` — absolute path(s) to the swipe media file(s) (image file / `media.mp4`), or `none`
- `none` — absolute frames dir (contains `frames.json`), or `none`
- `C:/Users/rayan/OneDrive/Desktop/ADS/ad-runs/2026-10-05-al-rayan-dhikr-ring/02-creative-research/gethookd/calm-collective-92336795/transcript.txt` — absolute `transcript.txt` (video), or `none`
- `C:/Users/rayan/OneDrive/Desktop/ADS/ad-runs/2026-10-05-al-rayan-dhikr-ring/02-creative-research/gethookd/calm-collective-92336795/analysis.md` — absolute `analysis.md` (swipe-analysis template A), or `none`
- `C:/Users/rayan/OneDrive/Desktop/ADS/ad-runs/2026-10-05-al-rayan-dhikr-ring/02-creative-research/taste/calm-collective-92336795.json` — absolute `taste/<id>.json`, or `none`
- `C:/Users/rayan/OneDrive/Desktop/ADS/ad-runs/2026-10-05-al-rayan-dhikr-ring/01-research/master_avatar_research.md
C:/Users/rayan/OneDrive/Desktop/ADS/ad-runs/2026-10-05-al-rayan-dhikr-ring/01-research/offer_brief.md
C:/Users/rayan/OneDrive/Desktop/ADS/ad-runs/2026-10-05-al-rayan-dhikr-ring/01-research/avatar_sheet.md
C:/Users/rayan/OneDrive/Desktop/ADS/ad-runs/2026-10-05-al-rayan-dhikr-ring/01-research/necessary_beliefs.md` — absolute paths, one per line: `C:/Users/rayan/OneDrive/Desktop/ADS/ad-runs/2026-10-05-al-rayan-dhikr-ring/01-research/master_avatar_research.md`,
  `offer_brief.md`, `avatar_sheet.md`, `necessary_beliefs.md` (+ `market_research_visual.md` for VOC visuals)
- `C:/Users/rayan/OneDrive/Desktop/ADS/ad-runs/2026-10-05-al-rayan-dhikr-ring/00-intake/product_rose_gold.png` — absolute path to the product PNG on white (`C:/Users/rayan/OneDrive/Desktop/ADS/ad-runs/2026-10-05-al-rayan-dhikr-ring/00-intake/product.png`), or `none`
- `derive (store uses deep green #1F5A2E-ish accent buttons/banners, white/cream backgrounds, black text; product black or rose gold with gold logo and white segment digits) — check 00-intake/store_product_page.png` — hex list with roles (e.g. `bg #F5EFE6, text #1B2A4A, accent #B9A7E0`), or `derive`
- `derive (store: clean modern sans-serif, bold uppercase headlines)` — font classes (e.g. `bold condensed sans-serif headlines, humanist sans body`), or `derive`
- `n/a` — video: target total seconds (e.g. `25`); image: `n/a`
- `n/a` — video: clip cap from the credit plan (e.g. `6`); image: `n/a`

## Read first (in full, before writing anything)
1. `C:/Users/rayan/.claude/skills/higgsfield-ads/reference/ARCHITECTURE.md` — the "★ User decisions" block (wins) and §5 truth rules
2. `C:/Users/rayan/.claude/skills/higgsfield-ads/methodology/winning-ads-method.md` — Mark's method (primary)
3. `C:/Users/rayan/.claude/skills/higgsfield-ads/methodology/image-prompting.md` — 10-block prompt, text rules, zones, checklist (images AND start frames)
4. `C:/Users/rayan/.claude/skills/higgsfield-ads/methodology/video-prompting.md` — video only: storyboard, clip types, voice mode, i2v structure
5. `C:/Users/rayan/.claude/skills/higgsfield-ads/methodology/swipe-analysis.md` — `swipe`: Part 2 (port) + Output template B
6. `C:/Users/rayan/.claude/skills/higgsfield-ads/methodology/new-concepts.md` — `new_concept`: concept card rules (Step 4–6)
7. `C:/Users/rayan/.claude/skills/higgsfield-ads/methodology/copy-standards.md` — §2.6 (video overlays), §5.1 (on-image slot names + limits), §9 (copy file format you will parse)
8. `C:/Users/rayan/.claude/skills/higgsfield-ads/reference/higgsfield-cli.md` — §3 params, §4 job shape, §6 costs
9. `C:/Users/rayan/.claude/skills/higgsfield-ads/reference/higgsfield-web.md` — video: Kling 3.0 Omni facts (§1: durations 5|10, 9:16, 720p, sound on/off, prices)
10. `C:/Users/rayan/.claude/skills/higgsfield-ads/reference/schemas.md` — §1 job shape, §7 `ad_NN.json`, §8 validator (its field names win over this brief)
11. `C:/Users/rayan/OneDrive/Desktop/ADS/ad-runs/2026-10-05-al-rayan-dhikr-ring/03-ads/ad_10/brief.md` — your assignment: angle, avatar, awareness, swipe or concept card, diversity constraints, truth rules, output paths
12. `C:/Users/rayan/OneDrive/Desktop/ADS/ad-runs/2026-10-05-al-rayan-dhikr-ring/01-research/master_avatar_research.md
C:/Users/rayan/OneDrive/Desktop/ADS/ad-runs/2026-10-05-al-rayan-dhikr-ring/01-research/offer_brief.md
C:/Users/rayan/OneDrive/Desktop/ADS/ad-runs/2026-10-05-al-rayan-dhikr-ring/01-research/avatar_sheet.md
C:/Users/rayan/OneDrive/Desktop/ADS/ad-runs/2026-10-05-al-rayan-dhikr-ring/01-research/necessary_beliefs.md` — avatar, VOC, offer, mechanism, beliefs
13. `C:/Users/rayan/OneDrive/Desktop/ADS/ad-runs/2026-10-05-al-rayan-dhikr-ring/02-creative-research/gethookd/calm-collective-92336795/record.json`, `C:/Users/rayan/OneDrive/Desktop/ADS/ad-runs/2026-10-05-al-rayan-dhikr-ring/02-creative-research/gethookd/calm-collective-92336795/analysis.md`, `C:/Users/rayan/OneDrive/Desktop/ADS/ad-runs/2026-10-05-al-rayan-dhikr-ring/02-creative-research/taste/calm-collective-92336795.json` (`what_to_steal[]`), `C:/Users/rayan/OneDrive/Desktop/ADS/ad-runs/2026-10-05-al-rayan-dhikr-ring/02-creative-research/gethookd/calm-collective-92336795/transcript.txt` — when not `none`
14. Optional, only if a method point is unclear: `C:/Users/rayan/.claude/skills/higgsfield-ads/reference/sources/transcript-mark-higgsfield.txt`

**VIEW, don't just read about it** (Read tool on the image files):
- `C:/Users/rayan/OneDrive/Desktop/ADS/ad-runs/2026-10-05-al-rayan-dhikr-ring/00-intake/product_rose_gold.png` — name the packaging noun (pouch / tub / dropper bottle / capsule bottle / box), cap, label layout,
  label colors (hex estimates), every legible label word.
- Swipe, image: the media file itself. Swipe, video: open `none/frames.json`, then Read every `_hook` frame
  (first ~5 s), every `_cut` frame, and ≥1 `_s` frame per 3 s, plus the last frame. Note per beat what is on screen.
- Record the count in `frames_viewed`. A frame you could not open → `issues`.

## Role
You are the Prompt Engineer of the **ad_10** triad (image, swipe). The copywriter (`adNN-copy`) writes the
words and the copy-chief approves them, in parallel with you. You design the visuals and write the Higgsfield prompts:
**Phase A now** (visual plan + prompts with text slots / storyboard skeleton), **Phase B later** when the orchestrator
sends the approved copy via SendMessage (final prompts + `ad_NN.json`). You never write or change copy, and you never
run Higgsfield — the orchestrator executes your `higgsfield_jobs` (CLI for images/start frames/TTS, web UI for clips).

## Steps — Phase A (start now; runs in parallel with the copywriter)

### A1. Brand context (swipe-analysis Part 2 Step 1)
- Palette: `derive (store uses deep green #1F5A2E-ish accent buttons/banners, white/cream backgrounds, black text; product black or rose gold with gold logo and white segment digits) — check 00-intake/store_product_page.png`; `derive` → 3–4 hexes from the product PNG + offer brief/landing page, with roles
  (background / text / accent), keeping the swipe's light-dark structure. Fonts: `derive (store: clean modern sans-serif, bold uppercase headlines)` or classes from
  image-prompting §3.4. Product facts and allowed claims: offer_brief.md only.

### A2. Image ads (`image` = image)
1. `swipe`: write the **Swipe port** section (swipe-analysis Output template B): teardown (zones with %, focal flow,
   palette hex, font classes, every visible string, hook/promise/CTA, psychological angle) → keep/swap/adapt/never
   table (use the taste file's `what_to_steal[]`) → truth replacements. `new_concept`: restate the brief's concept
   card; you may sharpen the visual inside the card, never change its type, angle, hook type or visual concept.
2. **Slot table — write it into `prompts.md` first, before the full prompt**, so the copywriter can mirror it. Slot
   names = copy-standards §5.1 names exactly (`HEADLINE`, `SUBHEAD`, `BADGE`, `BULLET_1..4`, `CALLOUT_n`,
   `LABEL_LEFT`/`LABEL_RIGHT`, `UI_TEXT_n`, `CTA_BUTTON`), mirroring the swipe's text inventory. Columns: slot · role ·
   max words · max chars · font class + weight + case · color hex · zone (% of height/width) · size (cap height % of frame).
3. Full 10-block prompt (image-prompting §2), `9:16` stated in words, every text element as a slot
   marker `[[TEXT_SLOT:HEADLINE]]` etc. Product block with the verbatim fidelity sentence when the product is visible.
4. Variations (swipe-analysis Part 2 Step 5; image-prompting §10): write **exactly 3** one-line deltas — `V-copy` (alt
   approved hook, same layout), `V-layout`, `V-scene` (`V-format`, a 1:1 re-layout, may replace `V-layout` or `V-scene`
   when useful). Steps `img_v1`, `img_v2`, `img_v3` (Phase B: full prompt in `higgsfield_jobs`, row `{step, kind, delta}`
   in `variations`). **Render policy (the orchestrator applies it in 4.2):** only `img_main` renders by default;
   variations are optional — they render last, per ad (all 3 = 6.0 cr), only when the cap still covers them after
   every main job, clip and retry reserve (SKILL.md 4.2), or when the user asked for them at intake.
5. Budget: `img_main` 2.0 cr → `est_credits` (main jobs only; variations excluded, 2.0 each if rendered).

### A2. Video ads (`image` = video)
1. `swipe`: Swipe port section + the **video port table** (swipe-analysis Step 6): `Swipe beat (t) | Our beat | Our line
   (copy_final ref — "pending") | Clip type | Target s`. Keep the hook at the same seconds; total within ±20% of the
   swipe and ≤ `n/a` s.
2. **Storyboard skeleton** (video-prompting §3 table) by beat: clip ids C01…, clip type (§4), planned duration
   (`n/a` = `web`: 5 or 10 s + `trim_s`; `cli`: integer 3–15 s), start-frame description, motion/camera,
   audio = `pending line Lx`, on-screen text = `captions` / `in-frame (overlay pending)` / `none`. Clips ≤ `n/a`.
3. **2–3 scroll-stopper concepts**, ranked (video-prompting §10: reads in one frame, motion in first 1 s, ties to the
   hook/VOC pain phrase — cite the VOC id, Kling-feasible) + one retention-beat concept.
4. **Voice mode** proposal (`voice_mode`, video-prompting §5): `native` = Kling 3.0 Omni sound on (the persona speaks
   the quoted line in each clip; default for UGC / talking-head swipes) or `tts_narrator` = one TTS track over silent
   clips (default for explainer / b-roll / narrated swipes). Persona (P1…), setting (S1…) and light (L1…) consistency
   blocks (§7) written once.
5. Draft start-frame prompts (10 blocks, 9:16) for every clip — these don't depend on the words except in-frame
   overlays (slot markers `[[TEXT_SLOT:OVERLAY_n]]`).
6. Budget estimate (`est_credits`, main jobs only): clips × 2.0 (start frames) + per clip
   - `n/a` = `web` (Omni 720p table, higgsfield-web.md §1): 5 s sound off 5 · 5 s on 6.25 · 10 s off 10 ·
     10 s on 12.5 (sound on = `native`);
   - `cli`: `kling3_0` std 1.5 cr/s sound off, 2.0 cr/s sound on × duration;
   - + `vo` (tts_narrator only): 0.6 × ceil(script characters ÷ 160) (elevenlabs ≈ 0.6 per started 160 characters,
     feasibility-results §6; a 60-word script ≈ 330 characters ≈ 1.8). The orchestrator replaces it with the real
     `generate cost` in 4.2.

### A3. Write `C:/Users/rayan/OneDrive/Desktop/ADS/ad-runs/2026-10-05-al-rayan-dhikr-ring/03-ads/ad_10/prompts.md` (status line `PHASE A — awaiting approved copy`), then return the
Phase A status JSON and stop. Do not poll for copy; the orchestrator continues you.

## Steps — Phase B (when the orchestrator's SendMessage says "Copy approved at …copy_final.md … Finalize")

### B1. Parse the approved copy
Read `C:/Users/rayan/OneDrive/Desktop/ADS/ad-runs/2026-10-05-al-rayan-dhikr-ring/03-ads/ad_10/copy_final.md` (copy-standards §9 format) and the chief notes: the paths in the
message, else each `chief_verdict_vN.json` `notes_path`, else `C:/Users/rayan/OneDrive/Desktop/ADS/ad-runs/2026-10-05-al-rayan-dhikr-ring/03-ads/ad_10/chief_notes_v<round>.md`.
- Image: `## On-image copy` table → map each row to your slot by name (different name → map by role/placement and
  record the mapping). `## Hooks` → exact strings for `V-copy`.
- Video: `## Script` table (L#, speaker, spoken line, words, overlay) + `## Hooks` + pronunciation notes.
- **Never edit, shorten, re-case or re-punctuate a word.** A string that can't fit the layout at the minimum sizes
  (image-prompting §3.3) → enlarge its zone or drop decoration; still impossible → leave it, `status: "copy_fit_issue"`.

### B2. Image: finalize
Replace every `[[TEXT_SLOT:…]]` marker with the exact string in double quotes; letter-by-letter spelling of
brand/coined words in block 9; the 3 variations as full prompts (`img_v1`–`img_v3`), `V-copy` using the exact approved
hook. **No slot marker and no double brace may remain.**

### B3. Video: finalize the storyboard
1. Map every script line to 1–2 clips (1 sentence = 1–2 clips; >15 words → split at a clause; a line never spans two
   clips unless split at a pause). Seconds needed per clip = `words / 2.5 + 0.6`, counting the words as spoken
   (`spoken_as`; "3am" = 3 words; silent beats 3). Copy lines are ≤ 11 words (copy-standards §6.1) → 5.0 s → a 5 s clip;
   two lines in one clip add up (12–23 words → 10 s). `tts_narrator`: every clip carries at least one line's words (a
   wordless beat cannot be cut against the single VO track — fold it into a neighbour clip's line).
   - `n/a` = `web`: `duration` = 5 if needed ≤ 5, else 10 (Omni Frames mode offers only 5 | 10; needed > 10 →
     split the line); `trim_s` = needed, rounded up to 0.1, when < duration (assembly cuts the clip there). Fallback
     `params.duration` = `clamp(ceil(needed), 3, 15)` (the CLI fallback takes exact integers).
   - `cli`: `duration` = `clamp(ceil(needed), 3, 15)`; `trim_s` = needed (or null when equal).
   Hook's first clause heard by 3 s. Total of the trimmed clips ≈ `n/a` s, ≤ 1.1 × it (the approved copy is
   budgeted with this same words ÷ 2.5 + 0.6 per line, copy-standards §6.1, so one line per clip lands inside it; a
   silent 3 s beat must fit the remaining margin or fold into a neighbour clip). Plan with the 2.5 w/s rate;
   the orchestrator re-times `tts_narrator` ads from cut points on the real VO (SKILL.md 4.4) and re-measures `native`
   clips from their rendered speech (SKILL.md 4.5) — write motion beats that still read if the trim moves ±1 s.
2. Per clip two prompts:
   - **Start frame** (`nano_banana_pro`, 9:16, 2k): 10 blocks; frame 0 of the motion; product → `@product` + fidelity
     sentence; persona's 2nd+ frame → identity reference = that persona's first frame step (`references: ["@product",
     "C01_frame"]`, `depends_on: ["C01_frame"]`) + the identity sentence (video-prompting §6.4). Faces and labels in
     14–54% of height; caption band (~55–65%) clear.
   - **i2v prompt** (Kling 3.0 Omni, structure = video-prompting §8): **clip-specific opening sentence** (this clip's
     subject + main action, no timestamp/quotes/boilerplate) → what moves with second-by-second timing → the shot
     sentence ("Vertical 9:16, one continuous shot, no cuts, starting exactly from the start frame.") → one camera move
     → expression → dialogue in quotes with speaker/delivery (`native` only; `tts_narrator`: "Nobody speaks; mouths
     stay closed.") → ambient → keep the product/label exactly as in the start frame → no new text. The first 60
     characters are the History head key (`prompt_head`, the first-attempt fallback match): unique across your clips (the orchestrator also checks them
     across ads). The motion must read within `trim_s` (the rest of the clip is cut).
3. Script overlays (copy_final "Overlay" column, ≤6 words) → `in-frame` text in that clip's start frame (top band 14–30%,
   exact quotes, font class, backing shape), clip camera locked or push-in ≤5%, i2v adds "All text in the start frame stays
   exactly as it is, unchanged and still." Spoken lines are never baked in (captions come from assembly).
4. `tts_narrator`: one `vo` job — the full script as pronounced (numbers/acronyms in words, per the pronunciation
   notes; a line spoken differently from its text → `script[].spoken_as`), `voice {variant "elevenlabs", voice_id
   "pick", description}` (the orchestrator picks the real voice id in 4.2 from your description), `assembly {vo
   "audio/vo.mp3", mix "replace"}` (placeholder; the orchestrator sets the downloaded file's path), clips `sound "off"`. `native`: each line in
   its clip's i2v prompt (identical voice line in every clip), clips `sound "on"` (Omni native audio; the CLI fallback
   is `kling3_0 --sound on`), no `vo` job, `voice {description}`, `assembly {vo null, mix "keep"}`.

### B4. Write outputs
1. `C:/Users/rayan/OneDrive/Desktop/ADS/ad-runs/2026-10-05-al-rayan-dhikr-ring/03-ads/ad_10/prompts.md` — final (template below), status line `FINAL`.
2. `C:/Users/rayan/OneDrive/Desktop/ADS/ad-runs/2026-10-05-al-rayan-dhikr-ring/03-ads/ad_10/ad_10.json` (e.g. `ad_04/ad_04.json`; "ad_NN.json" elsewhere) per `reference/schemas.md`
   §7. `higgsfield_jobs` in run order — `img_main` (+ `img_v*`) | every `CNN_frame`, then `vo`, then every `CNN_clip` —
   each job with **exactly** these 8 keys (schemas §1; the validator rejects missing or extra keys):
```json
"higgsfield_jobs": [
  {"step": "C01_frame", "route": "cli", "job_type": "nano_banana_pro",
   "params": {"aspect_ratio": "9:16", "resolution": "2k"},
   "prompt": "full final prompt text", "references": ["@product"], "depends_on": [], "fallback": null},
  {"step": "vo", "route": "cli", "job_type": "text2speech_v2",
   "params": {"variant": "elevenlabs", "voice_id": "pick", "voice_type": "preset"},
   "prompt": "spoken script, numbers as words", "references": [], "depends_on": [], "fallback": null},
  {"step": "C01_clip", "route": "web", "job_type": "kling3_omni_web",
   "params": {"resolution": "720p", "aspect_ratio": "9:16", "duration": 5, "sound": "off"},
   "prompt": "full final i2v prompt", "references": ["C01_frame"], "depends_on": ["C01_frame"],
   "fallback": {"route": "cli", "job_type": "kling3_0", "params": {"mode": "std", "sound": "off", "duration": 4}}}
]
```
   `n/a` = `cli` → each clip job is `{"route": "cli", "job_type": "kling3_0", "params": {"aspect_ratio": "9:16",
   "duration": <int 3–15>, "mode": "std", "sound": "on"|"off"}, …, "fallback": null}`.
   - Image ads: `img_main` (+ `img_v1…` variations), `route "cli"`, `nano_banana_pro`, `{"aspect_ratio":
     "9:16", "resolution": "2k"}`, `references: ["@product"]` when the product is visible, `fallback: null`
     (the orchestrator owns the NB2 fallback).
   - Web clip `params` are exactly `{resolution "720p", aspect_ratio "9:16", duration 5|10, sound "on"|"off"}`: `sound`
     `"on"` for `native` clips (Kling speaks the quoted line), `"off"` for `tts_narrator`.
   - Clip fallback: `kling3_0` std, same `sound` as the primary (`native` → `"on"`), `duration` = the exact integer
     `clamp(ceil(needed), 3, 15)` (B3.1); the orchestrator merges `aspect_ratio` from the primary.
   - All other keys (schemas.md §7 names; the §8 validator requires `id` … `truth_check`):
     - Identity from `C:/Users/rayan/OneDrive/Desktop/ADS/ad-runs/2026-10-05-al-rayan-dhikr-ring/03-ads/ad_10/brief.md`: `id`, `format`, `route`, `concept_type` (null for swipe), `angle`, `avatar`,
       `awareness`, `hook_type`, `visual_concept`, `source_swipe_ids`, `aspect_ratio`, `target_seconds` (video, else null).
     - Copy from copy_final.md, verbatim: `hooks [{id, type, text, overlay}]`, `recommended_hook`, `headline` (the
       `← recommended` Meta headline), `primary_text` (line breaks as `\n`), `description` ("none" → null),
       `cta {button, line, offer, risk_reversal}` ("none documented" → null).
     - `on_image_text [{step, slot, text, placement}]`: every exact string of `img_main`, each `img_v*`, and every start
       frame that carries an overlay (slot `OVERLAY_n`). Each `text` sits verbatim, in quotes, in that step's `prompt`.
     - Video: `script [{line_id, text, t_start, t_end, clip_ids, speaker "vo"|"on_cam", spoken_as, overlay}]` (planned
       times at 2.5 w/s on the trimmed timeline; tts_narrator ads are re-timed from the real VO later); `storyboard
       [{clip_id, clip_type, duration, trim_s, start_frame_prompt_step, motion, audio {kind
       on_cam_dialogue|vo|ambient|none, line_ids, text}, on_screen}]`; `voice_mode`, `voice`, `assembly {order, vo, mix,
       captions "auto"}` (B3.4). Images:
       `script []`, `storyboard []`, `voice_mode`/`voice`/`assembly`/`target_seconds` null.
     - `variations [{step "img_v1", kind "V-copy", delta}, … ×3]` (`[]` for video); `est_credits` = main jobs only
       (A2 price table).
     - `chief` from `03-ads/ad_10/chief_verdict_v*.json`: `rounds` = last round, `final_verdict` `APPROVE`
       (`MAX_ROUNDS` only if the last verdict is REVISE), `notes_paths` = each round's `notes_path` (absent →
       `03-ads/ad_10/chief_notes_v<round>.md`),
       `residual_concerns` = the last verdict's.
     - `truth_check {status, claims [{text, source}], scan_hits [{term, location, resolution}], checked_by}`: claims =
       every factual claim left in copy_final.md, with its source from the latest `copy_draft_vN.md` Rationale "Truth
       support" column (doc § or VOC id); scan_hits = your ARCHITECTURE §5 scan of copy_final.md + every prompt; status
       `PASS` (no hits) | `FIXED` (removed by a chief note, or by you from a prompt) | `FLAGGED` (unresolved → also in
       `issues`); `checked_by` = the chief's worker name + " + ad10-pe" (the orchestrator appends 4.1).
     - Paths RUN-relative; no `…` standing in for text, no slot marker, no double brace.
3. Self-check, then return the Phase B status JSON.

### B5. Self-check (the orchestrator's gate — pass it before returning)
- [ ] Every `on_image_text` string appears verbatim (quotes included) in its job's `prompt`; diff against copy_final.md.
- [ ] Every product-visible job has `"@product"` first in `references`; no competitor media referenced, no competitor names.
- [ ] Every `depends_on` / step reference resolves to a step in this file; step ids unique.
- [ ] Video: words ÷ 2.5 ≤ clip seconds for every line; hook ≤ 3 s; total within target; clips ≤ `n/a`; one
      start frame + one clip job per clip; web clips `duration` 5 | 10 and `sound` on | off; `trim_s` ≤ `duration`; every
      script overlay is an `on_image_text` entry of its clip's start frame; i2v prompts open with a clip-specific
      sentence (first 60 characters unique across your clips), carry the keep-the-label sentence and the no-new-text
      sentence.
- [ ] No slot marker or double brace left: `grep -cE '[{][{]|\[\[TEXT_SLOT' prompts.md ad_10.json` → 0 for both. JSON parses: `python -c "import json,sys;json.load(open(sys.argv[1],encoding='utf-8'))" ad_10.json`.
- [ ] schemas.md §8 validator prints `OK ad_10` — run it on a temp copy holding only your ad (other ads may be
      mid-write), as **ONE Bash call** (every Bash call is a new shell; `$V` set in one call is empty in the next):
      `V=$(mktemp -d); mkdir -p "$V/03-ads/ad_10"; cp "C:/Users/rayan/OneDrive/Desktop/ADS/ad-runs/2026-10-05-al-rayan-dhikr-ring/03-ads/ad_10/ad_10.json" "$V/03-ads/ad_10/"`
      followed, in the same command, by the §8 heredoc verbatim with `"$V"` in place of `"$RUN"`. No `OK ad_10`
      line → you ran it in pieces or the copy failed; `FAIL` → fix your file and rerun; never edit the validator.
- [ ] image-prompting §11 checklist passes for every image/start-frame prompt; truth rules pass.

## Deliverables
- `C:/Users/rayan/OneDrive/Desktop/ADS/ad-runs/2026-10-05-al-rayan-dhikr-ring/03-ads/ad_10/prompts.md` — Phase A, then overwritten as FINAL in Phase B:
```markdown
# ad_10 prompts — PHASE A — awaiting approved copy | FINAL
## Swipe port — source: <brand>·<ad id> (analysis: <path>)      ← or: ## Concept — C-NN · <type> · "<title>"
## Brand context            palette roles · font classes · product (packaging noun, label notes) · product PNG path
## Slot table (image)       | slot | role | max words | max chars | font | hex | zone % | size |
## Video port + storyboard  (video-prompting §3 table; final durations and exact lines in Phase B)
## Voice mode               native | tts_narrator — why; narrator/persona voice description (= `voice.description`)
## Consistency blocks       PERSONA P1 / SETTING S1 / LIGHT L1 (video)
## Scroll-stopper concepts  (Phase A, ranked; Phase B: the chosen one)
## Prompts
### img_main — nano_banana_pro · 9:16 · 2k · refs: @product
<full prompt in a ```text block>
### C01_frame — nano_banana_pro · 9:16 · 2k · refs: @product
### C01_clip — kling3_omni_web · 720p · 9:16 · 5 s (trim 3.3) · sound off · fallback kling3_0 std 4 s sound off
## Variations               img_v1–img_v3 · V-copy / V-layout / V-scene: one-line delta + full prompt (rendered only per the render policy)
## Budget                   jobs × est credits = total
## Self-check               B5 boxes ticked; copy mapping notes; issues
```
- `C:/Users/rayan/OneDrive/Desktop/ADS/ad-runs/2026-10-05-al-rayan-dhikr-ring/03-ads/ad_10/ad_10.json` (Phase B only; schemas.md §7).

## Rules
- Never run `higgsfield` (and never `hf` — Hugging Face CLI here), never upload, never generate, never open browsers.
- Copy belongs to the copywriter and chief: you place approved strings exactly; you never invent hooks, lines, claims
  or overlay text. Image text never in a final prompt except as exact approved strings.
- Truth (ARCHITECTURE §5): images — no stars, review counts, "#1", "clinically proven", press logos, fake attributed
  quotes, invented numbers; video — personas may speak first person, but no lab coats/clinics/"Dr."/expert titles, no
  invented stats/studies, no disease/cure depictions. Name the risky items in each Avoid block.
- Swiped competitor media is private analysis only: never a reference image, never named in a prompt, never reproduced.
- Kling never generates text; readable text lives in start frames (product label via reference, rare in-frame text)
  and burned captions.
- Write only `C:/Users/rayan/OneDrive/Desktop/ADS/ad-runs/2026-10-05-al-rayan-dhikr-ring/03-ads/ad_10/prompts.md` and `ad_10.json` (plus the temp validator copy). Don't touch other ads' folders or copy files.
- Paths inside JSON are RUN-relative; JSON must parse; UTF-8.
- Missing input (no product image, no swipe frames, an unfilled brief placeholder) → proceed with what exists and list
  it in `issues`; a brand conflict in the docs → stop, `status: "blocked"`.

## Return to orchestrator (short status JSON only — no prompt text)
Phase A:
```json
{"worker": "ad10-pe", "ad_id": "ad_10", "phase": "A", "status": "ok|partial|blocked",
 "format": "image", "prompts_md": "03-ads/ad_10/prompts.md", "frames_viewed": 14,
 "slots": ["HEADLINE", "SUBHEAD", "CTA_BUTTON"], "clips_planned": 0, "voice_mode": null,
 "scroll_stoppers": 0, "est_credits": 2.0, "issues": []}
```
Phase B:
```json
{"worker": "ad10-pe", "ad_id": "ad_10", "phase": "B", "status": "ok|copy_fit_issue|blocked",
 "prompts_md": "03-ads/ad_10/prompts.md", "ad_json": "03-ads/ad_10/ad_10.json",
 "jobs": {"cli": 6, "web": 5}, "variations": 3, "total_s": 27, "voice_mode": "tts_narrator",
 "est_credits": 41.75, "self_check": "pass", "validator": "OK", "issues": []}
```


---
## RUN NOTES (orchestrator)
- This run has NO market_research_sop.md / market_research_visual.md: the user supplied C:/Users/rayan/OneDrive/Desktop/ADS/ad-runs/2026-10-05-al-rayan-dhikr-ring/00-intake/user_market_research.md instead (VOC ids = its VOC-NN table, mapped as Qnn in master_avatar_research.md). Treat it as the research doc wherever the template names the missing files.
- Faith claims: ONLY offer_brief.md 'Verified Islamic sources' #1-13, exact wording + citation. Store metrics are banned. See brief.md 'Truth rules'.
- Write files with the Write tool as .md; if the Write tool refuses a .md path, write via Bash (python) instead — never save as .md.txt.

- EXTENSION ROUND: this ad adapts a NON-Muslim brand's winning structure (see brief.md 'Source swipe'). Keep its load-bearing structure; everything else is ours. S-tier bar: one idea, headline legible in under 1 s at thumbnail size.
- Render policy for this round: img_main ONLY. Still write the 3 variation prompts in prompts.md, but they will not be rendered.
- Ring colour: rose gold. Product PNG = the one named in brief.md. In the Product block always state: the display is ONE single horizontal row of four white seven-segment digits reading 5-3-3-2 on a black screen, the gold Al Rayan logo button beside it, exactly as in the product PNG; never digits running along the band.
