# Scout log p2-gh-vid
- tabId: tab-5 | start 2026-10-05 (local) | formats: videos | max opened 15 | max video 30s | download consent: yes
- Preflight: logged in (no login wall). Credit counter: NOT visible on /explore text ("N left" not found in body text; mobile layout) -> recheck on ad page.
- Tools check: ffprobe 9.0.2 ok; faster_whisper ok; frames.py, transcribe.py ok.
- Filters panel opened with real click: options = Country, EU transparency, Estimated spend, Performance, Ad Rank, Limit ads per brand, Ad format, CTA Type, Static ad style, Status, Niche, Page Type, Technology, Run time. NO Language option. Country/Niche left unset (own-niche queries return 0-10 results anyway; English verified per ad). Ad Rank not applied (performance_scores=winning,optimized covers tier).
- Ad list source: get-ads POST (FormData: page, per_page=12, order_column=relevance, search, display_formats=videos, days_active=14, performance_scores=winning,optimized, ads_per_brand_limit=2, semantic_mode=hybrid, ranking_method=impressions, personalize=0), replayed via fetch in JS.
- Note: URL param ad-format=videos maps to body display_formats=videos; run-time=14 -> days_active=14.

## Searches (videos, winning+optimized, run-time 14, brand limit 2)
| query | result count | note |
|---|---|---|
| tasbih ring | 0 | |
| dhikr | 4 | Nimah x2 (tasbih bracelet gift), The Shop Korner 49s, Urban Rugs 34s |
| islamic gift | 0 | |
| muslim | 90 | fashion/abaya/shorts mostly; ErgoSalah, Mommy Yasmin (gift), Deen Intl |
| smart ring | 0 | |
| prayer ring | 0 | |
| smart ring (loosen: drop run-time) | 0 | |
| smart ring (loosen: drop run-time + tier) | 10,392 | weak evidence (no tier); QALO, Kogan, Oura, LoopTrack |
| prayer ring (drop run-time) | 0 | |
| smart ring (run-time 7) | 0 | |
| tasbih | 10 | Nimah, CuvaLife (Hinglish), ZikerZone (Urdu), Kitabisa/Shopping culture (Indonesian) |
| zikr counter | (call timed out; not captured) | |
| rosary (adjacent: faith) | 35 | many 6-30s wearable/prayer rosaries |
| christian prayer | 56 | Spiral Bible, FaithGateway, Holy Land Prayer |
| bible | 226 | |
| wearable ring / mantra ring / gift for her ring | 0 | |
| habit tracker (adjacent) | 62 | planners, WHOOP |
| mindfulness | 47 | Poeak (Dutch), Saged |

Additional searches (videos, winning+optimized, 14d): fidget ring 0 | anxiety ring 0 | meaningful gift 0 | bracelet 1,093 (off-niche) | habit 484 (off-niche) | rosary ring 0 | prayer beads 214 (Blessedbangles, HilalHaven, Amen Artisan, Solace Beads) | counter 402 (off-niche).
Loosening used: dropped run-time, then dropped tier for "smart ring" only (QALO taken, no tier = weak evidence).

## Shortlist (opened in this order; 14 ad pages opened of 15)
nimah-149804170, nimah-160687594, crushcovet-141919376, spiral-bible-104491118, ergosalah-71735717, mommy-yasmin-175600855, blessedbangles-163936452, catholic-woodworker-149531283, ghirelli-156707359, qalo-17730240, whoop-107141009, hilalhaven-132665673, deen-international-173775613, fithbyrahim-175606348.
Pre-skipped from JSON (no page opened): The Shop Korner 49s and Urban Rugs 34s (too_long), Muslim Lane/Noor Qalb/Jamal Al Muslim (too_long), CuvaLife (Hinglish, non_english from get-ads body), ZikerZone/Kitabisa/Vevo/Shopping culture (non-English), LoopTrack (German), ErgoSalah sibling 178567261 (same concept as kept 71735717).

## Kept
| id | format | duration | tier | days running | taste total | hook |
|---|---|---|---|---|---|---|
| ergosalah-71735717 | video | 12.1 s | winning | 271 | 53 (B, 7/8/8) | What muslim think i sell: / Vs... / What i actually sell.. |
| deen-international-173775613 | video | 29.9 s | winning | 28 | 55 (B, 7/8/8) | Everybody asks the same three questions about our shorts. |

## Rejects
| id | reason |
|---|---|
| nimah-149804170 | total 29: soft opening, no mechanism/CTA |
| nimah-160687594 | total 21: still image slogan, unverifiable shared-reward faith claim |
| crushcovet-141919376 | avatar floor: chest-focused framing, Catholic iconography |
| spiral-bible-104491118 | total 46: Christian older-woman Bible book, avatar 5/adaptability 5 |
| mommy-yasmin-175600855 | non_english (Arabic recitation audio) + avatar floor (kids' toy) |
| blessedbangles-163936452 | non_english (Arabic speech); us-vs-them only in primary text |
| catholic-woodworker-149531283 | avatar floor: Catholic friar testimonial |
| ghirelli-156707359 | adaptability floor: celebrity (Jonathan Roumie), polished brand intro |
| qalo-17730240 | total 27: no hook/mechanism/CTA; no GetHookd tier, ended |
| whoop-107141009 | total 33: polished 3D spot, health claims |
| hilalhaven-132665673 | non_english (Urdu audio), catalog promo-code ad |
| fithbyrahim-175606348 | total 23: polished apparel montage |

## Failures / notes
- frames.py failed on most clips ("ffmpeg cut pass failed", non-full-range YUV); fell back to ffmpeg with -strict unofficial (hook_NN.jpg / body_NNN.jpg naming), contact sheets used to view frames (frames/_sheet_*.jpg).
- Credit counter text ("N left") was not present in page text anywhere on /explore or ad pages; could not read start/end value. No credit-spending control was clicked.
- Another worker's scratch files overwrote my helper rec.py once; rebuilt in a private folder; no effect on outputs.
- Kept count 2 of target 6: Muslim niche has almost no winning video ads; faith/jewelry/smart-ring candidates mostly failed avatar or adaptability floors.
- 1 ad-page budget unused.
