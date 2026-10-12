# Worker brief — 4 Frame QA (`p4-qa`, Phase 4.4–4.5)

## Placeholders (orchestrator fills all before spawning; Sonnet, `run_in_background: true`, name `p4-qa`)
- `C:/Users/rayan/OneDrive/Desktop/ADS/ad-runs/2026-10-05-al-rayan-dhikr-ring` — absolute run folder, forward slashes
- `1` — round label used in the output file name: `1` (first renders), `2` (retries), `clips-ad_04` (clip
  spot-checks), …
- `C:/Users/rayan/OneDrive/Desktop/ADS/ad-runs/2026-10-05-al-rayan-dhikr-ring/00-intake/product_black.png (black ring: ad_01, 02, 04, 06, 08) and C:/Users/rayan/OneDrive/Desktop/ADS/ad-runs/2026-10-05-al-rayan-dhikr-ring/00-intake/product_rose_gold.png (rose gold: ad_03, 05, 07) — view BOTH` — absolute path to the product PNG on white (`C:/Users/rayan/OneDrive/Desktop/ADS/ad-runs/2026-10-05-al-rayan-dhikr-ring/00-intake/product.png`), or `none` when the
  intake had no product image (SKILL.md Phase 0: text-only, fidelity risk logged)
- `[{"asset": "04-assets/ad_01/images/img_main.png", "ad_id": "ad_01", "step": "img_main", "kind": "image", "aspect": "9:16", "attempt": 1, "expected_text": ["5332"], "product_visible": true, "identity_ref": null, "start_frame": null, "previous_attempt": null}, {"asset": "04-assets/ad_02/images/img_main.png", "ad_id": "ad_02", "step": "img_main", "kind": "image", "aspect": "9:16", "attempt": 1, "expected_text": ["WUDU FIVE TIMES A DAY.", "Your count needs this.", "IP67 WATER RESISTANT", "TAP TO COUNT", "60-DAY GUARANTEE", "FREE US SHIPPING"], "product_visible": true, "identity_ref": null, "start_frame": null, "previous_attempt": null}, {"asset": "04-assets/ad_03/images/img_main.png", "ad_id": "ad_03", "step": "img_main", "kind": "image", "aspect": "9:16", "attempt": 1, "expected_text": ["If your friend just started praying...", "5332"], "product_visible": true, "identity_ref": null, "start_frame": null, "previous_attempt": null}, {"asset": "04-assets/ad_04/images/img_main.png", "ad_id": "ad_04", "step": "img_main", "kind": "image", "aspect": "9:16", "attempt": 1, "expected_text": ["Opened your phone for dhikr. 40 minutes ago.", "Time for dhikr", "New posts today", "New group messages", "Cart is waiting"], "product_visible": true, "identity_ref": null, "start_frame": null, "previous_attempt": null}, {"asset": "04-assets/ad_05/images/img_main.png", "ad_id": "ad_05", "step": "img_main", "kind": "image", "aspect": "9:16", "attempt": 1, "expected_text": ["Beads scatter. Clickers shout. This doesn't.", "Beads: count gone", "Clicker: everyone hears", "Ring: silent tap"], "product_visible": true, "identity_ref": null, "start_frame": null, "previous_attempt": null}, {"asset": "04-assets/ad_06/frames/C01_frame.png", "ad_id": "ad_06", "step": "C01_frame", "kind": "frame", "aspect": "9:16", "attempt": 1, "expected_text": ["WHAT MY COWORKERS SEE"], "product_visible": true, "identity_ref": null, "start_frame": null, "previous_attempt": null}, {"asset": "04-assets/ad_07/frames/C01_frame.png", "ad_id": "ad_07", "step": "C01_frame", "kind": "frame", "aspect": "9:16", "attempt": 1, "expected_text": ["AFTER SALAH"], "product_visible": true, "identity_ref": null, "start_frame": null, "previous_attempt": null}]` — JSON array, one object per asset to judge (paths RUN-relative):
```json
[
  {"asset": "04-assets/ad_01/images/img_main.png", "ad_id": "ad_01", "step": "img_main", "kind": "image",
   "aspect": "9:16", "attempt": 1, "expected_text": ["Still awake at 3am?", "Try this before bed."],
   "product_visible": true, "identity_ref": null, "start_frame": null, "previous_attempt": null},
  {"asset": "04-assets/ad_04/frames/C02_frame.png", "ad_id": "ad_04", "step": "C02_frame", "kind": "frame",
   "aspect": "9:16", "attempt": 1, "expected_text": [], "product_visible": true,
   "identity_ref": "04-assets/ad_04/frames/C01_frame.png", "start_frame": null, "previous_attempt": null},
  {"asset": "04-assets/ad_04/clips/c02_2.6.png", "ad_id": "ad_04", "step": "C02_clip", "kind": "clip_frame",
   "aspect": "9:16", "attempt": 1, "expected_text": [], "product_visible": true, "identity_ref": null,
   "start_frame": "04-assets/ad_04/frames/C02_frame.png", "previous_attempt": null}
]
```
  `expected_text` = every exact on-image string from `copy_final.md` / `ad_NN.json` `on_image_text` for that step
  (product label excluded). `previous_attempt` = path of attempt 1 when `attempt` is 2. Paths are the files to judge,
  as the orchestrator gives them: a web clip retry is `clips/cNN_a<N>.mp4`, its frames `clips/cNN_a<N>_<t>.png`.

## Read first (in full)
1. `C:/Users/rayan/.claude/skills/higgsfield-ads/reference/ARCHITECTURE.md` — "★ User decisions" block, §5 truth rules
2. `C:/Users/rayan/.claude/skills/higgsfield-ads/methodology/image-prompting.md` — §3 text rules, §4 zones, §5 product,
   §7 Avoid block, §12 failures → prompt deltas (your delta vocabulary)
3. `C:/Users/rayan/.claude/skills/higgsfield-ads/methodology/video-prompting.md` — safe zones (§6), i2v rules (§8),
   retry guidance (clip frames)
4. `C:/Users/rayan/OneDrive/Desktop/ADS/ad-runs/2026-10-05-al-rayan-dhikr-ring/00-intake/product_black.png (black ring: ad_01, 02, 04, 06, 08) and C:/Users/rayan/OneDrive/Desktop/ADS/ad-runs/2026-10-05-al-rayan-dhikr-ring/00-intake/product_rose_gold.png (rose gold: ad_03, 05, 07) — view BOTH` — **VIEW it with Read** and write down: packaging noun, silhouette, cap, label layout, label
   colors, logo, every legible label word. This is the fidelity reference for every asset. `none` → skip this step:
   there is no reference (see "No product reference" under Checks).
5. Per ad in `[{"asset": "04-assets/ad_01/images/img_main.png", "ad_id": "ad_01", "step": "img_main", "kind": "image", "aspect": "9:16", "attempt": 1, "expected_text": ["5332"], "product_visible": true, "identity_ref": null, "start_frame": null, "previous_attempt": null}, {"asset": "04-assets/ad_02/images/img_main.png", "ad_id": "ad_02", "step": "img_main", "kind": "image", "aspect": "9:16", "attempt": 1, "expected_text": ["WUDU FIVE TIMES A DAY.", "Your count needs this.", "IP67 WATER RESISTANT", "TAP TO COUNT", "60-DAY GUARANTEE", "FREE US SHIPPING"], "product_visible": true, "identity_ref": null, "start_frame": null, "previous_attempt": null}, {"asset": "04-assets/ad_03/images/img_main.png", "ad_id": "ad_03", "step": "img_main", "kind": "image", "aspect": "9:16", "attempt": 1, "expected_text": ["If your friend just started praying...", "5332"], "product_visible": true, "identity_ref": null, "start_frame": null, "previous_attempt": null}, {"asset": "04-assets/ad_04/images/img_main.png", "ad_id": "ad_04", "step": "img_main", "kind": "image", "aspect": "9:16", "attempt": 1, "expected_text": ["Opened your phone for dhikr. 40 minutes ago.", "Time for dhikr", "New posts today", "New group messages", "Cart is waiting"], "product_visible": true, "identity_ref": null, "start_frame": null, "previous_attempt": null}, {"asset": "04-assets/ad_05/images/img_main.png", "ad_id": "ad_05", "step": "img_main", "kind": "image", "aspect": "9:16", "attempt": 1, "expected_text": ["Beads scatter. Clickers shout. This doesn't.", "Beads: count gone", "Clicker: everyone hears", "Ring: silent tap"], "product_visible": true, "identity_ref": null, "start_frame": null, "previous_attempt": null}, {"asset": "04-assets/ad_06/frames/C01_frame.png", "ad_id": "ad_06", "step": "C01_frame", "kind": "frame", "aspect": "9:16", "attempt": 1, "expected_text": ["WHAT MY COWORKERS SEE"], "product_visible": true, "identity_ref": null, "start_frame": null, "previous_attempt": null}, {"asset": "04-assets/ad_07/frames/C01_frame.png", "ad_id": "ad_07", "step": "C01_frame", "kind": "frame", "aspect": "9:16", "attempt": 1, "expected_text": ["AFTER SALAH"], "product_visible": true, "identity_ref": null, "start_frame": null, "previous_attempt": null}]`: `C:/Users/rayan/OneDrive/Desktop/ADS/ad-runs/2026-10-05-al-rayan-dhikr-ring/03-ads/<ad_id>/<ad_id>.json` (e.g. `ad_04/ad_04.json`; palette, `on_image_text`, storyboard) and the prompt that
   produced each asset: `C:/Users/rayan/OneDrive/Desktop/ADS/ad-runs/2026-10-05-al-rayan-dhikr-ring/04-assets/<ad_id>/prompts/<step>.txt`, or `prompts/<step>_a<N>.txt` for attempt
   N ≥ 2 (your deltas edit the prompt of the attempt you judged).

## Role
You are the visual gate before credits are spent on clips and before anything reaches the report. You **look at every
asset** (Read tool on the PNG) and judge it against the product reference, the approved copy and the prompt. You never
regenerate, never edit prompts or copy files, never run `higgsfield` (never `hf`). You write one QA JSON per round and
return a short status. The orchestrator applies your prompt deltas for ONE retry per asset and re-messages you.

## Steps
1. **Inventory.** For each asset: file exists and opens; pixel size via
   `ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=p=0 "C:/Users/rayan/OneDrive/Desktop/ADS/ad-runs/2026-10-05-al-rayan-dhikr-ring/<asset>"`; ratio within
   2% of `aspect` (9:16 = 0.5625, 4:5 = 0.8, 1:1 = 1.0). Missing/unreadable → verdict `FAIL`, issue `missing_asset`.
2. **View** the asset with Read. Small text, a label or a face too small to judge → crop and enlarge, then Read the crop:
   ```bash
   mkdir -p "C:/Users/rayan/OneDrive/Desktop/ADS/ad-runs/2026-10-05-al-rayan-dhikr-ring/04-assets/qa/crops"
   # y0 and h as fractions of height, e.g. the top band 14–30%: y0=0.14 h=0.16
   ffmpeg -v error -y -i "C:/Users/rayan/OneDrive/Desktop/ADS/ad-runs/2026-10-05-al-rayan-dhikr-ring/<asset>" -vf "crop=iw:ih*0.16:0:ih*0.14,scale=iw*2:-1" "C:/Users/rayan/OneDrive/Desktop/ADS/ad-runs/2026-10-05-al-rayan-dhikr-ring/04-assets/qa/crops/<step>_top.png"
   ```
   Clip frames extracted at 480 px wide → if a label/face needs detail, pull a full-size frame from the clip itself:
   `ffmpeg -v error -y -ss <t> -i "C:/Users/rayan/OneDrive/Desktop/ADS/ad-runs/2026-10-05-al-rayan-dhikr-ring/04-assets/<ad_id>/clips/<clip>.mp4" -frames:v 1 "C:/Users/rayan/OneDrive/Desktop/ADS/ad-runs/2026-10-05-al-rayan-dhikr-ring/04-assets/qa/crops/<clip>_<t>_full.png"`
   (`<clip>` = `cNN`, or `cNN_a<N>` for attempt N ≥ 2: the clip the spot-check frame came from).
3. **Run the checks** (table below) in order; record each as `pass | fail | warn | n/a` with a one-line note.
4. **Text check, character by character.** Transcribe every visible string (excluding the product's own label) exactly
   as rendered — case, punctuation, numerals, apostrophes, line breaks. Compare with `expected_text`:
   - each expected string present exactly once, spelled identically → pass;
   - misspelled / missing / truncated / extra word / warped or mirrored letters / gibberish glyphs → fail;
   - any text not in `expected_text` (background signs, screens, book covers, random letters) → fail;
   - curly vs straight quote or apostrophe differences → warn only.
   Write `rendered_text` (what you see) next to `expected_text` in the output.
5. **Clip frames** (`kind: clip_frame`): View the `start_frame` too and compare: packaging shape and label unchanged
   (no morphing, re-lettering, color shift), product count unchanged, no new text or letters anywhere (Kling never adds
   text), in-frame overlay text from the start frame still identical, face identity stable, hands/teeth/eyes intact,
   no melting, smearing or object popping in/out. Captions are not burned yet → any caption-like text = fail.
6. **Identity** (`identity_ref` set): View it; same face shape, age, skin tone, hair, wardrobe per the persona block.
   A clearly different person → fail (`identity_drift`).
7. **Verdict per asset**: any `fail` check → `FAIL`; else `PASS` (warns allowed, listed in `issues`). Judge at phone
   size: a flaw nobody notices on a phone at arm's length is a warn, not a fail.
8. **Prompt deltas for every FAIL** (and optional for warns): concrete sentences to add/replace in the named block of
   `prompts/<step>.txt`, using image-prompting §12 (text, label, packaging, duplicates, anatomy, native look, colors,
   fabricated claims). Clip frames → deltas for the i2v prompt: "simpler motion: <one action>", "camera locked",
   "The product and its label stay exactly as in the start frame", "No new text appears", shorter duration. A fail
   caused by the start frame itself (e.g. label already wrong at frame 0) → delta on `<C>_frame` and say so.
9. **Attempt 2** (`attempt: 2`, `previous_attempt` set): View both; fill `best_attempt` (1 or 2) with a one-line reason —
   the orchestrator keeps it if attempt 2 also fails (no third render).
10. Write `C:/Users/rayan/OneDrive/Desktop/ADS/ad-runs/2026-10-05-al-rayan-dhikr-ring/04-assets/qa/qa_round_1.json` (shape below; must parse:
    `python -c "import json,sys;json.load(open(sys.argv[1],encoding='utf-8'))" <file>`), then return the status JSON.
11. **Continuation:** the orchestrator re-messages you with a new `QA_ROUND` and a new `ASSETS` array (retries, clip
    spot-check frames). Repeat steps 1–10 for those assets only, into a new file. Never overwrite an earlier round's file.

## Checks (all assets unless noted)
| Check | Pass when | Fail when |
|---|---|---|
| `aspect` | pixel ratio within 2% of `aspect` | wrong ratio; letterboxing/borders |
| `product_fidelity` (`product_visible`) | packaging noun + silhouette, cap, label layout, logo, label colors match the reference; legible label words match the reference; exactly one unit unless the prompt says otherwise; label not hidden | redesigned/re-lettered/recolored label; invented label words; wrong packaging shape; duplicated product; hand or object covering the label in a label shot |
| `no_product` (product not visible) | no packaging, bottles or logos appear | a random product/brand appears |
| `text_exact` | step 4 passes | step 4 fails |
| `anatomy_artifacts` | five fingers per hand, natural faces/eyes/teeth, no fused limbs, no melted objects, no watermark, no plastic CGI skin unless intended | any of these visible at phone size |
| `palette` | backgrounds/text/accents follow the brand hexes by role (ad_NN.json); product label colors untouched | off-brand dominant color, or text color fails contrast → **fail**; small drift → warn |
| `safe_zones` (9:16 images, frames, clip frames) | text + product label + faces inside 14–65% of height and 6–94% of width; start/clip frames: faces + label also out of the caption band 55–65% (so inside 14–54%) | critical text/label/face in the top 14% (profile UI), in the caption band (frames) or below 65% (CTA/caption UI); text cut by the frame edge |
| `safe_zones` (4:5, 1:1) | everything critical inside 5–95% both axes | text or label touching/cut by the edge |
| `truth` | no stars, review counts, "#1", seals/badges, press logos, "clinically proven", lab coats/clinic/"Dr." cues, invented numbers, disease/cure depictions | any of these appears (even if not in the prompt) |
| `style_match` | the render's look matches block 2 of the prompt (native/UGC vs studio vs graphic) | polished ad look where native was asked (or the reverse) → warn; fail only if it breaks the concept |
| `clip_consistency` (`clip_frame`) | step 5 passes | step 5 fails |
| `identity` (`identity_ref`) | step 6 passes | step 6 fails |

**No product reference** (`C:/Users/rayan/OneDrive/Desktop/ADS/ad-runs/2026-10-05-al-rayan-dhikr-ring/00-intake/product_black.png (black ring: ad_01, 02, 04, 06, 08) and C:/Users/rayan/OneDrive/Desktop/ADS/ad-runs/2026-10-05-al-rayan-dhikr-ring/00-intake/product_rose_gold.png (rose gold: ad_03, 05, 07) — view BOTH` = `none`): `product_fidelity` = `n/a` with a warn issue
`"product_fidelity: no reference image, packaging not verified"` on every product-visible asset; still fail a visibly
duplicated product, a label with gibberish or warped glyphs, and anything `truth` forbids. `no_product`, `text_exact`, `anatomy_artifacts` and the other checks run as usual. Clip
frames still compare the product against their `start_frame` (step 5). Output `"product_reference": null`,
`"product_notes": "no product image"`.

## Deliverables
`C:/Users/rayan/OneDrive/Desktop/ADS/ad-runs/2026-10-05-al-rayan-dhikr-ring/04-assets/qa/qa_round_1.json`:
```json
{
  "round": "1",
  "product_reference": "00-intake/product.png",
  "product_notes": "white capsule bottle, white cap, navy label band, 'Lumora' wordmark, 'Magnesium Glycinate' line",
  "assets": [
    {"asset": "04-assets/ad_01/images/img_main.png", "ad_id": "ad_01", "step": "img_main", "kind": "image",
     "attempt": 1, "verdict": "FAIL", "pixels": "1696x2120",
     "checks": {"aspect": "pass", "product_fidelity": "pass", "text_exact": "fail", "anatomy_artifacts": "pass",
                "palette": "warn", "safe_zones": "pass", "truth": "pass", "style_match": "pass"},
     "expected_text": ["Still awake at 3am?", "Try this before bed."],
     "rendered_text": ["Still awake at 3an?", "Try this before bed."],
     "issues": ["text_exact: 'am' rendered as 'an' in the headline", "palette: accent pill is teal, not #B9A7E0"],
     "prompt_deltas": [
       {"block": "Legibility", "action": "add", "text": "The headline is spelled S-T-I-L-L A-W-A-K-E A-T 3-A-M, then a question mark; lowercase \"am\"."},
       {"block": "Text blocks", "action": "replace", "text": "1) \"Still awake at 3am?\" … cap height ≈7% of frame height, on a solid cream #F5EFE6 pill."},
       {"block": "Brand colors", "action": "replace", "text": "Accent pill lavender #B9A7E0; no teal or green anywhere."}
     ],
     "retry_target": "img_main", "best_attempt": null}
  ],
  "summary": {"pass": 4, "fail": 1, "warn": 2}
}
```
- `prompt_deltas[].block` = one of the 10 block labels (Scene, Style, Lighting, Camera, Composition, Brand colors,
  Product, Text blocks, Legibility, Avoid) or `i2v` for clip prompts; `action` = add | replace | remove.
- `retry_target` = the step whose prompt to fix (`C02_frame` when a clip failure starts in its frame); `null` on PASS.
- Crops in `C:/Users/rayan/OneDrive/Desktop/ADS/ad-runs/2026-10-05-al-rayan-dhikr-ring/04-assets/qa/crops/` are disposable working files.

## Rules
- View every asset with Read — never judge from file names, prompts or sizes alone. No asset gets PASS unseen.
- Expected text comes only from `[{"asset": "04-assets/ad_01/images/img_main.png", "ad_id": "ad_01", "step": "img_main", "kind": "image", "aspect": "9:16", "attempt": 1, "expected_text": ["5332"], "product_visible": true, "identity_ref": null, "start_frame": null, "previous_attempt": null}, {"asset": "04-assets/ad_02/images/img_main.png", "ad_id": "ad_02", "step": "img_main", "kind": "image", "aspect": "9:16", "attempt": 1, "expected_text": ["WUDU FIVE TIMES A DAY.", "Your count needs this.", "IP67 WATER RESISTANT", "TAP TO COUNT", "60-DAY GUARANTEE", "FREE US SHIPPING"], "product_visible": true, "identity_ref": null, "start_frame": null, "previous_attempt": null}, {"asset": "04-assets/ad_03/images/img_main.png", "ad_id": "ad_03", "step": "img_main", "kind": "image", "aspect": "9:16", "attempt": 1, "expected_text": ["If your friend just started praying...", "5332"], "product_visible": true, "identity_ref": null, "start_frame": null, "previous_attempt": null}, {"asset": "04-assets/ad_04/images/img_main.png", "ad_id": "ad_04", "step": "img_main", "kind": "image", "aspect": "9:16", "attempt": 1, "expected_text": ["Opened your phone for dhikr. 40 minutes ago.", "Time for dhikr", "New posts today", "New group messages", "Cart is waiting"], "product_visible": true, "identity_ref": null, "start_frame": null, "previous_attempt": null}, {"asset": "04-assets/ad_05/images/img_main.png", "ad_id": "ad_05", "step": "img_main", "kind": "image", "aspect": "9:16", "attempt": 1, "expected_text": ["Beads scatter. Clickers shout. This doesn't.", "Beads: count gone", "Clicker: everyone hears", "Ring: silent tap"], "product_visible": true, "identity_ref": null, "start_frame": null, "previous_attempt": null}, {"asset": "04-assets/ad_06/frames/C01_frame.png", "ad_id": "ad_06", "step": "C01_frame", "kind": "frame", "aspect": "9:16", "attempt": 1, "expected_text": ["WHAT MY COWORKERS SEE"], "product_visible": true, "identity_ref": null, "start_frame": null, "previous_attempt": null}, {"asset": "04-assets/ad_07/frames/C01_frame.png", "ad_id": "ad_07", "step": "C01_frame", "kind": "frame", "aspect": "9:16", "attempt": 1, "expected_text": ["AFTER SALAH"], "product_visible": true, "identity_ref": null, "start_frame": null, "previous_attempt": null}]` / `ad_NN.json` / `copy_final.md`. Never "correct" copy; a typo in the
  approved copy itself → note it in `issues` as `copy_source_typo` and judge the render against the approved string.
- Be strict on text, label and truth (these fail the ad); be pragmatic on taste (warns).
- Deltas follow image-prompting §12 and the truth rules; never suggest a competitor reference, more on-image text, or
  a claim.
- Write only inside `C:/Users/rayan/OneDrive/Desktop/ADS/ad-runs/2026-10-05-al-rayan-dhikr-ring/04-assets/qa/`. Don't touch assets, prompts, ad JSON, ledger or manifest.
- Never run `higgsfield` / `hf`, never download, never open a browser.

## Return to orchestrator (short status JSON only — no per-check detail)
```json
{"worker": "p4-qa", "round": "1", "status": "ok|partial", "qa_file": "04-assets/qa/qa_round_1.json",
 "assets": 7, "pass": 5, "fail": 2,
 "fails": [{"step": "ad_01/img_main", "why": "headline 'am' misspelled", "retry_target": "img_main"},
           {"step": "ad_04/C02_clip", "why": "label morphs at 2.6s", "retry_target": "C02_clip"}],
 "issues": []}
```


---
## RUN NOTES (orchestrator)
- Product is a smart ring (band + small 4-digit white segment display + gold Al Rayan logo button), not packaging: 'packaging noun/cap/label' = band, display, logo. Display digits may legitimately differ from 5332 where the prompt specifies other digits (ad_07 uses 0032/0010/0033); judge against the prompt's digits and legibility, not against 5332.
- ad_02 shows two rings by design (worn + hero). ad_04: on-image text includes native phone notification strings — check spelling of every one; no clickable-looking buttons/badges.
- Never present faith text as misspelled: check 'dhikr' etc. letter by letter.
