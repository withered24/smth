# Scout log - p2-gh-nm (EXTENSION ROUND, images, non-Muslim brands only)
- tabId: seed (built-in browser, parallel-builtin). Start 2026-10-05 ~19:50Z. Resumed once after an API-limit interruption.
- Credit counter: not shown in header text (regex found none); no credit buttons clicked, so unchanged. Start/end: n/a.
- Tools OK: ffprobe 9.0.2, faster_whisper (not needed, images only).

## Searches (images, winning+optimized, run-time 30, ads_per_brand_limit 2)
Ad lists via a re-issued get-ads POST (FormData: search, display_formats[], days_active=30, performance_scores[], ads_per_brand_limit, semantic_mode=hybrid, X-XSRF-TOKEN). No Language filter used; English verified on ad pages.
- "smart ring" (URL form) 0 results; single word "smartring" 22; rosary 25; habit tracker 48; ring 50; wearable 43; mindfulness 21-23; journal 47; engraved 47; bracelet 47; habit 43; necklace 51; tracker 38; fidget 19; stress 47; calm 46; locket 24; pendant 48; keepsake 40; clicker 2; counter 44.
- 0 results (multi-word or sparse): oura ring, fidget ring, anxiety ring, sleep tracker, health tracker, prayer beads.
Muslim/Islamic brands and the ids listed in the brief were skipped. Thumbnails of ~28 candidates were previewed from get-ads (not counted as page opens), then ranked by tier, days running, ads using the creative, structure.

## Ad pages opened: 12 of 12
1 honest-hands 133996335: quick reject (tier "growing", 1 use), no folder.
2 tinker-stone-165455430 reject 43. 3 pulserive-98463189 reject 45. 4 try-halo-149270677 reject 49. 5 element-ring-co-132515960 reject 33. 6 plaud-171642547 reject 46. 7 neosapien-168014911 reject (B 54, avatar 4).
8 HAALE 120340388: quick reject (Swedish primary text, non_english), no folder.
9 calm-collective-92336795 KEPT A 70. 10 cloud-nine-133765605 KEPT A 71. 11 vincero-collective-169130877 reject (B 59, avatar 6). 12 ellie-grace-97725879 reject 46.

## Kept
| id | fmt | duration | tier | days running | taste | hook |
|---|---|---|---|---|---|---|
| calm-collective-92336795 | image 1080x1080 | n/a | winning | 175 | 70 (A) | A skin picker? |
| cloud-nine-133765605 | image 1080x1350 | n/a | optimized | 77 | 71 (A) | Hoodie with hidden anxiety tools |

## Rejects / skips
| id | reason |
|---|---|
| honest-hands-133996335 | tier growing, 1 use (quick reject, no folder) |
| haale-120340388 | non_english (Swedish), no folder |
| tinker-stone-165455430 | avatar: zodiac/astrology imagery |
| pulserive-98463189 | adaptability: FDA/blood-pressure claims, cluttered grid |
| try-halo-149270677 | avatar: price-first health tracker (total 49) |
| element-ring-co-132515960 | avatar: wedding romance, no headline |
| plaud-171642547 | avatar: AI recorder; giant-number visual device is harvestable |
| neosapien-168014911 | avatar: subscription pain; duplicates our 3-panel comparison |
| vincero-collective-169130877 | B 59, avatar 6 (skull imagery); blueprint-sketch device harvestable |
| ellie-grace-97725879 | overlaps our gift-box hero; anxiety-cure claim |

## Failures / notes
- Multi-word queries return 0 or time out via the API; single words worked. Run-time 30 + winning/optimized is narrow, so the S bar (long-running + several uses + new structure) yielded 2 of the 5 targeted. Page-open budget (12) exhausted.
- Harvestable devices in the reject taste JSONs: Plaud giant-number spec hero, Vincero hand-drawn blueprint annotation page, Halo price-on-macro hero.
