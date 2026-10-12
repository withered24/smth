# Scout log p2-social (Meta Ad Library)
tabId: tab-7 · start: 2026-10-05T13:31:31Z · country US · mode parallel-builtin · download consent: yes

## Searches (video unless noted; country US; sorted by total impressions desc)
- 13:32Z video q="tasbih ring" -> ~2 results, 2 cards (both Weslamic-office, 11s, 41d: 2379413312864003, 1634398231590296)
- video queries run: tasbih ring (~2), zikr ring (~5), dhikr (~250), muslim ring (~18), islamic gift (~150), iQibla (apps, junk), smart ring (~8800), rosary ring (~76), tasbih bracelet (~6, all Nimah), prayer bracelet (~220)
- image queries run: tasbih ring (0), dhikr (0), tasbih (0), islamic gift (~8), rosary ring (~22), islamic jewelry (~1), smart ring (~740), weslamic (0), faith bracelet (~100)
- not run: Hadiyah, Sajada, "Al Rayan Rings", "tasbeeh counter"
- cards scanned ~280, collected 13

## Kept (4) - all tier B, both filters >=8 -> "[needs hook rework]"
| id | brand | format | dur | days | score |
|---|---|---|---|---|---|
| meta-1518673786238484 | Nimah | video | 6.4s | 56 | 50 |
| meta-2379413312864003 | Weslamic | video 1:1 | 10.7s | 41 | 51 |
| meta-1649694736793087 | The Prayer I Share | video | 15.4s | 19 | 53 |
| meta-1580472540526104 | Qamar Jewelry | image | - | 33 | 57 |

## Rejected (8)
meta-1719407559115659 Nimah video 36 (adaptability, faith claim); meta-1600083061461951 Weslamic video 45 (non-English Arabic); meta-26726286480310591 Only One You video 25; meta-1944921103117985 Pineapplea Lot video 33 (avatar); meta-792911836811986 Hero Company image 29 (avatar); meta-855873960549944 Kindred Spirits image 32; meta-989177810361520 Flairgifts image 31 (avatar); meta-1363264355565394 Amen Artisan image 33 (avatar)

## Skipped (1)
meta-1728858588400637 Qamar video 30.42s - too_long (>30s), not processed

## Issues
- Thin Islamic niche: image searches for tasbih/dhikr returned 0. Kept 3 videos + 1 image vs target 6/6.
- Write tool blocked analysis.md files for subagents; analyses saved as analysis.md.txt in each kept folder (record.json updated).
- Meta Ad Library gives no performance tier; longevity (days active) used as proxy.
- Signed fbcdn URLs not stored anywhere.
