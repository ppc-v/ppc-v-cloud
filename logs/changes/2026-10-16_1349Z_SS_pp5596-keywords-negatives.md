# PP5596: tighten Jefferson City keywords and add 13 negatives

- **When:** 2026-10-16 13:49 UTC (09:49 US Eastern)
- **Requested by:** SS
- **Approved by:** SS, approved preview in chat ("yes please")
- **Platform:** Google Ads
- **Session:** https://claude.ai/code/session_01USjya2G6ufP63tzHwMt22C

## Changes
| Account | Entity (type, name, ID) | Field | Before | After | Result |
|---|---|---|---|---|---|
| PP5596 - Align Chiropractic Clinic (128-340-8501) | Keyword `chiropractor` broad, ad group "Chiropractor" (152319217133~12457821), campaign "Chiropractor - Jefferson City" | Status | Enabled | Paused | ✅ applied |
| PP5596 (128-340-8501) | Keyword `chiropractor jefferson city` broad, ad group "Chiropractor Jefferson City" (152319217333~821938106111) | Status | Enabled | Paused | ✅ applied |
| PP5596 (128-340-8501) | Keyword `chiropractor jefferson city` exact (152319217333~339591057571) | Status / max CPC | Paused / USD 16.00 | Enabled / USD 27.00 | ✅ applied |
| PP5596 (128-340-8501) | Keyword `chiropractor jefferson city` phrase (152319217333~1931294707431) | Status / max CPC | Paused / none (ad group USD 28.00) | Enabled / USD 24.00 | ✅ applied |
| PP5596 (128-340-8501) | Shared negative list "Search Queries" (10720596569), used by all 3 campaigns | Phrase negatives added | 1,127 members | 1,140 members | ✅ applied |

Negatives added (phrase): kieser, we chiro, dudum, 100 chiropractic, sport and spine, comc, eicgo, dubuque, litchfield, decompression machine, decompression device, walgreens, cervicalgia.

Budget effect: none (Jefferson City capped at USD 50/day since 13:46 UTC today).

## Failed or skipped
None. Deliberately not added: `medicare` (would block Medicare-accepting searches), `sports doctor` and `3d neck scan` (pending SS confirming whether the clinic offers these).

## Notes
- Reason: 90 days to 15 Oct, `chiropractor` broad cost USD 1,645 for 9 leads (USD 183/lead) at a USD 29 bid; `chiropractor jefferson city` broad USD 497 for 1 lead. The exact `jefferson city chiropractor` converts at ~USD 61/lead; top search term "chiropractor jefferson city mo" (9 leads) is now covered by the phrase keyword.
- Check in 2–3 weeks: Jefferson City lead volume and CPL; whether impression share on the exact/phrase terms improves.
