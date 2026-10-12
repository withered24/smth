# Scout log p2-gh-img (GetHookd, images)
- tabId: tab-4 | date 2026-10-05 | credit counter: NOT DISPLAYED anywhere on explore/ad pages in this layout (start/end unknown); no credit buttons clicked.
- Filters: Country = United States (no Language filter offered), performance winning+optimized, ads_per_brand_limit=2, ad-format=images. Final explore URL pattern: /explore?query=<q>&ad-format=images&location=US&performance_scores=winning%2Coptimized&run-time=14&ads_per_brand_limit=2
- Method: get-ads POST is multipart FormData (page, per_page, order_column, search, display_formats, days_active, location, performance_scores, ads_per_brand_limit, semantic_mode, ranking_method, personalize) with X-XSRF-TOKEN header; re-issued via fetch in-page. run-time (days_active) dropped for most queries (loosening step 1) because strict results were 0-2.

## Queries (query | params | results)
tasbih ring | strict US | 0 ; dhikr | strict | 2 (Nimah x2) ; islamic gift | strict, no run-time | 0 ; muslim | no run-time | 17 ; tasbih | no run-time | 2 ; tasbih ring | no run-time | 0 ; islamic | no run-time | 4 ; smart ring | no run-time / no perf | 0 / 0 ; prayer ring | no run-time | 0 ; ramadan | no run-time | 4 ; rosary | no run-time | 21 ; prayer | no run-time | 42 ; wearable | no run-time | 44 ; rosary ring | 0 ; jewelry gift | 0 ; habit tracker | 0 ; ring | no run-time | 54 ; mindfulness | 7 ; bracelet | 51 ; tracker | 40 ; quran | 12 ; eid | 0. (Multi-word queries mostly return 0: use single words.)

## Shortlist and pages opened (13 of 15)
Own niche: nimah-172387899, sajada-159582735, tayyib-beauty-175015416, hilalhaven-174215175, qurannest-161909756, yaqeen-books-126182379. Cross-niche: tulas-175871419, magnevaco-178051290, hallow-177222207, catholight-112275383, amen-artisan-150829118, hope-rings-177217013, dusq-by-innergize-172605956.

## Kept (6)
| id | format | dur | tier | days | taste | hook |
|---|---|---|---|---|---|---|
| yaqeen-books-126182379 | image 1638x2048 | - | optimized | 80 | 70 A | I recited the Quran for 20 years without understanding it |
| hope-rings-177217013 | image 2048x2560 | - | winning | 22 | 62 B (rework) | If your granddaughter is growing up too fast... |
| sajada-159582735 | image 1080x1440 | - | winning | 41 | 61 B (rework) | Finally pray without checking your phone every 30 seconds |
| tayyib-beauty-175015416 | image 1024x1024 | - | optimized | 69 | 60 B (rework) | No water for 16 hours. Wudu five times. |
| tulas-175871419 | image 1024x1024 | - | winning | 25 | 53 B (rework) | My mother slid a green ring onto my finger... this one goes first |
| nimah-172387899 | image 1080x1350 | - | optimized | 31 | 52 B (rework) | Share in her dhikr. |

## Rejects (7)
hilalhaven-174215175 (34, offer-led collage, adaptability floor) | magnevaco-178051290 (disease claims, immodest crop, avatar/adapt floors) | hallow-177222207 (celebrity-dependent) | catholight-112275383 (generic still life, avatar floor) | amen-artisan-150829118 (40, feature-led) | qurannest-161909756 (42, restock promo template) | dusq-by-innergize-172605956 (B 50, stat-led, avatar 5/adapt 6)

## Skips / failures
- None skipped. Credit counter not found on page (cannot compare start/end).
- Truth flags: Nimah (reward-to-giver faith claim), Tulas and Yaqeen (fabricated first-person testimonials, stats, protection lore, charity claim), Hope Rings (30,000+ customers), Sajada (unattributed quotes).
- Primary text for Tulas and Yaqeen is truncated in record.json (7.5k / 8.0k char long-form); beats summarised in the record.
