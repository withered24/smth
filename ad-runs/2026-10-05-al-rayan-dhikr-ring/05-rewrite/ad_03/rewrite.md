# ad_03 copy - v2 rewrite (copywriter pass)

## Ad info
- Format: image (9:16)
- Concept: swipe:hope-rings-177217013 (gift callout + hero macro + reveal + reassurance + risk reversal), structure kept, words and emotion rebuilt
- Angle: ANG5 - a gift for someone learning the five daily prayers: a tasbih for the hand, not the shelf
- Avatar: A2 meaningful-gift buyer (friend, spouse, parent, sibling shopping before Ramadan, Eid, Umrah)
- Awareness: problem-aware (offer_brief) bridging to solution-aware (brief). The primary text names the category ("smart tasbih ring") in line 2.
- Sophistication: stage 3 (mechanism): own the beginner scene (the 33-33-34 after salah, prayer-time alerts) instead of the generic feature stack the other ten ads share.
- Framework: demo-first (ring in a box is the visual), callout in the first line, one recipient scene as the mechanism, fear answers (permission, size, risk) in short lines, one CTA.
- Argument spine: Someone shopping for a person who is learning the five daily prayers wants a gift that gets used, not shelved. After salah there is a count to hold (33, 33, 34); the ring keeps it with a tap, a small display and a gentle pulse at 33, 66 and 99, and buzzes at the five prayer times. Fingers stay the Sunnah, so there is no hesitation. The size is the gift buyer's worry, so 16-22 mm, a 60-day money-back guarantee and a 1-year warranty make it safe to guess. Tap Shop Now.
- Beliefs installed (in order): B4 (a ring can count quietly and keep my place) -> B3 (one line: fingers stay the Sunnah, the ring is a helper) -> B5 (it is safe to buy, even guessing the size) -> B6 (low risk to try)
- Faith line: none. No hadith or Quran used (none required). No reward claim, no Sadaqah Jariyah, no claim about what the ring earns.
- Length (video): n/a

## Hooks
| ID | Type (slug) | Hook (exact) | Where it runs |
|---|---|---|---|
| H1 | contrast / us-vs-them | A tasbih for the hand, not the shelf. | On-image headline (re-render) |
| H2 | situation-callout (product framing, no "you") | Gift idea for someone learning the five daily prayers. | Primary text line 1 |
| H3 | scene / pain | After salah comes the tasbih: 33, 33, 34. Easy to lose your place when it is all still new. | Alt primary opener |
| H4 | objection-answer | Guessing the size? You have 60 days to send it back. | Alt opener, or later line |
| H5 | mechanism curiosity | A gentle pulse at 33, 66 and 99. | Alt on-image headline / Meta headline |
| H6 | question (gift-search intent) | Stuck on a gift for someone who is learning to pray? | Alt opener (second tier: third-party religious practice, lower risk than "your husband is new to Islam", still prefer H2) |
Recommended: **H1 on the image, H2 as primary line 1.** Why: H1 stands alone (the picture shows a box, so "gift" is understood) and is a real contrast with a dhikr context, instead of a dangling ellipsis. It does not assert anyone's religion. H2 does different work from the image (it names the situation the buyer is in) rather than repeating it, and uses product/situation framing with no "you/your friend" + religious-status claim. Cut from v1: "If your husband is new to Islam..." (Meta personal-attribute risk).

## On-image copy
Decision: **RE-RENDER.** The current main image (`report_media/ad_03_main.jpg`) shows a garbled display (reads about "2655"), and the older variants stack the digits vertically, so the "5332" reveal fails. The headline also changes, so a re-render costs nothing extra.
| Slot | Exact text | Words | Placement / notes |
|---|---|---|---|
| HEADLINE | A tasbih for the hand, not the shelf. | 8 | top 20%, 2 lines ("A tasbih for the hand," / "not the shelf."), centred, one heavy grotesque sans used identically in every variant (v1 had four different type styles, which confounded testing). Cream on the deep-green satin of `ad_03_img_v3.jpg` (best contrast, most premium). |
| DISPLAY_TEXT | 5332 | 1 | the ring's own small display, one horizontal row of four seven-segment digits, clearly legible, no other glyphs. Re-render until it reads 5332. |
Total on-image words: 9. No SUBHEAD, BADGE, bullets or CTA button.
Render notes:
- Use the `ad_03_img_v3.jpg` composition (ring standing in a cushion box, three-quarter view). It reads as a ring; the `ad_03_main.jpg` flat wide band reads as a smart band.
- Box stays plain and unbranded (cream or green). No printed text on the box. Do not add a card or ribbon with words.
- Rose gold ring stays for the main version. Optional test variant: same composition with the black ring, for buyers shopping for a man. Never show a man wearing it, and never on the index finger.

## Primary text (final, ready to paste)
Gift idea for someone learning the five daily prayers: a smart tasbih ring.

After salah comes the tasbih. 33, 33, 34. Easy to lose your place when it is all still new.

Tap the ring to count. A small display shows the number, and a gentle pulse at 33, 66 and 99 helps them keep their place. It also buzzes for all five prayer times, set up in the app. [CONFIRM: prayer-time alerts are set up in the Al Rayan app, and the app is live in the stores]

Counting on the fingers stays the Sunnah. The ring is a helper, not a replacement.

Not a lecture. Not another book on the shelf. Just something small on the hand.

Guessing the size? It comes in 16-22 mm, and you have a 60-day money-back guarantee. Free size exchanges. [CONFIRM: free size exchanges]

Black or rose gold. IP67 water resistant. 1-year tech warranty. Free US shipping.

$49.99.

Tap Shop Now to choose their size and colour.

## Meta headlines (<= 40 chars)
1. Sizes 16-22 mm, 60-Day Money-Back (33) <- recommended
2. A Gentle Pulse at 33, 66 and 99 (31)
3. Smart Tasbih Ring Gift Idea (27)
Why #1: it answers the gift buyer's top fear (guessing the size) and adds nothing the image already says. #3 is the fallback if a cold audience needs the category word in the headline.

## Meta description
Smart tasbih ring. Free US shipping. (36)

## CTA
- Button: Shop Now
- Line: "Tap Shop Now to choose their size and colour."
- Offer: "$49.99 · free US shipping · 60-day money-back guarantee · 1-year tech warranty". No sale price, no % off.
- Risk reversal: 60-day money-back guarantee (sits next to the size line so it works as size insurance)

## Changes vs v1
- Image headline "If your friend just started praying..." -> "A tasbih for the hand, not the shelf." [Critique 1 (ellipsis hook waits on the primary text, no emotional charge); Section 3 #4 (second-person + religious practice, "just started praying" can read as shaming a returner); Should-fix 7; Direction 3. Keeps the H3 rhythm the critique praised.] Re-render needed.
- Display reveal: re-render so "5332" is legible and horizontal. [MUST FIX 3 / Section 4: current main image shows garbage digits.] Also locks one font across variants [Should-fix 8].
- Primary line 1 no longer repeats the headline; it now names the buying situation in product framing. [MUST FIX 4; Should-fix 4 of section 3]
- H5 "If your husband is new to Islam..." deleted, and "A Meaningful Gift for a New Muslim" headline deleted; no copy asserts a recipient's religion. [MUST FIX 2; Section 3 #3]
- "IP67 water resistance: wear it to wudu" removed; IP67 kept as a plain fact next to the warranty, no wudu line (ad_02 owns wudu). [MUST FIX 1; Section 5 overlap]
- Feature stack of bullets replaced by one recipient scene: the 33-33-34 after salah, the pulse at 33, 66 and 99 (no claim it marks the 100th), and prayer-time alerts as the beginner-specific benefit. [MUST FIX 6; Direction 1; Section 2 "best-fit feature buried"]
- Added size answer: "16-22 mm", 60-day money-back, free exchange tagged. [MUST FIX 5; Direction 2]
- Added B3 line: fingers stay the Sunnah, ring is a helper. [Should-fix 2; necessary_beliefs gift outline]
- Dropped "It looks like a ring, not a gadget" (contradicted by the flat-band image; shared with ad_05, 06, 11). [Should-fix 1; Section 3 #6]
- Dropped "A meaningful gift, made for daily use." and "one easy habit"; replaced with "Not a lecture. Not another book on the shelf. Just something small on the hand." (quiet-support emotion, no guilt, no durability implication). [Should-fix 3; Section 3 #7; Section 2 emotional layer]
- Warranty and IP67 moved together in one line so B5 is stated as facts together. [Should-fix 4]
- Dropped "Silent tracking" and the copy-pasted mechanism sentence shared with the other ten ads. [Direction 4; Section 5 overlap]
- Meta headlines rewritten: no price repeat of the image, no "New Muslim", no "Gift ... Dhikr". [Should-fix 5; Section 3 #3, #5]
- Meta description no longer repeats the guarantee line. [Should-fix 5; Section 5 redundancy]
- Box: copy says nothing about packaging; image box stays unbranded. [Should-fix 6; Section 3 #8]
- Closing CTA now ties to the size choice instead of "get them one". [Section 5 flab]
- Kept: the gift-buyer / learning-to-pray recipient angle, callout-style situation opener, 5332 reveal, single CTA, offer line, "Sunnah" respect, no metrics, no hadith.

## Owner to confirm
- [CONFIRM: free size exchanges] - the rebuilt store says free size exchanges within 60 days; the research/product page does not state it. Delete that line if not confirmed.
- [CONFIRM: prayer-time alerts are set up in the Al Rayan app, and the app is live in the stores] - the rebuilt page says alerts are set in the app. If the app is not live, change to "prayer-time alerts for all five daily prayers" and drop "set up in the app".
- Size range: copy says 16-22 mm (product page). The rebuilt store lists only 18, 20 and 22 mm. Make the store and the ad agree before running.
- Packaging: the image shows a plain box, but there is no confirmed Al Rayan gift box. Keep the image box unbranded; do not add "gift-ready" or "arrives boxed" copy without confirming.
- Landing-page warning (outside this ad's scope, but it receives this traffic): the rebuilt pages still carry testimonials, "Voices from the community" quotes, and an index-finger recommendation. A gift ad for men lands on advice that conflicts with the Sahih Muslim narration the page itself cites. Remove or change before sending traffic.
