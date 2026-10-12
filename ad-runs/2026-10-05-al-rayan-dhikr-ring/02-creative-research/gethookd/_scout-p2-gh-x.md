# Scout log — p2-gh-x (GetHookd cross-niche, images+videos)
- tabId: tab-6 (built-in browser, parallel-builtin) · start 2026-10-05T13:31Z
- Credit counter at start: "50 left" (read from nav menu text)
- Preflight: logged in, no login wall. Tools OK (ffprobe 9.0.2, faster_whisper, frames.py, transcribe.py).

## Searches
Filters panel opened with real click; Country = United States (URL: https://app.gethookd.ai/explore?query=smart+ring&ad-format=videos&location=US&performance_scores=winning%2Coptimized&run-time=14&ads_per_brand_limit=2). Language filter not offered; Niche left unset (own niche reached via queries muslim/islamic/tasbih). Ad Rank filter not used (performance_scores already winning,optimized).
Ad lists came from the get-ads POST (FormData body: search, display_formats, days_active, location, performance_scores, ads_per_brand_limit, semantic_mode=hybrid...), re-issued from JS fetch with the page cookies + XSRF header (the observed request body was FormData, not JSON). run-time = days_active=14; per_page 30.
| fmt | query | step -> result count |
|---|---|---|
| videos | smart ring | page-own request: 0 results (winning+optimized+14d, US). My re-issue later: base/no-runtime/no-loc all timed out (15 s) |
| videos | rosary | base 0? -> no-runtime 27 (base step not logged separately; no-runtime step returned 27) |
| videos | prayer | base 50 |
| videos | faith jewelry | base/no-runtime/no-loc all timeout |
| videos | habit tracker | base timeout, no-runtime timeout, no-rt+no-loc 41 |
| videos | meditation | base 41 |
| videos | tasbih (own niche) | base 2 |
| videos | muslim (own niche) | base 26 |
| videos | islamic (own niche) | base 18 |
| images | smart ring | timeout x3 (base/no-runtime/no-loc) |
| images | rosary | base 21 |
| images | prayer | base 42 |
| images | faith jewelry | timeout x3 |
| images | habit tracker | base timeout, no-runtime timeout, no-rt+no-loc 48 |
| images | meditation | base 41 |
| images | tasbih / muslim / islamic | 2 / 17 / 4 |
Note: result counts of base queries exceed per_page because get-ads returns grouped cards; ids deduped before shortlisting. Multi-word queries ("smart ring", "faith jewelry") repeatedly timed out from JS fetch (server slow with concurrent in-flight requests) — logged as failures.

Later queries (same method): tasbih, muslim, islamic, rosary, prayer, meditation, habit tracker and others returned lists; see table above. Shortlist drawn from cross-niche (faith jewelry, reminders, gift rings).

## Page opens (15 of 15 used)
1 nimah-149804170 (WASTED: taken by p2-gh-vid; my collect step overwrote media/poster/frames/transcript in their folder; record.json and taste are theirs)
2-9 ra-optics, moki, habitaware, my-saint-my-hero, kailash-energy, pixie-wing, wishhouse, sajada (all rejected)
10 yappy-apparel-178309829 (KEPT, B 54)
11 hope-doves-132737005 (KEPT, B 51, image)
12 alabaster-co-179532582 (reject 38; faith claim 'God stopped you here')
13 lilli-paris-175960512 (reject 32; cocktail in frame, alcohol skip)
14 support-mental-health-174287440 (reject 40; charity mechanism)
15 rextus-174570757 (reject 48; avatar 6; faith claim 'strength comes from God')

## Kept
| id | fmt | total | tier |
|---|---|---|---|
| yappy-apparel-178309829 | video 20.2 s | 54 | B [needs hook rework] |
| hope-doves-132737005 | image | 51 | B [needs hook rework] |

## Failures / notes
- Multi-word queries timed out; Language filter absent; "smart ring" 0 results with winning filter.
- One read-only javascript_tool call ran on the wrong tab (tab-2, a higgsfield page) because tabId was omitted; nothing modified.
- Under target: 1 video and 1 image kept vs 4 and 4.
