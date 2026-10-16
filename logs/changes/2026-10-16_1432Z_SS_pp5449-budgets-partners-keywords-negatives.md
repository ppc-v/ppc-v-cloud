# PP5449: pace budgets to the monthly cap, search partners off, keyword and negative cleanup

- **When:** 2026-10-16 14:32 UTC (10:32 US Eastern, Sara's usual timezone)
- **Requested by:** SS
- **Approved by:** SS, approved the previewed changes #1–5 in chat ("make any changes you think will help")
- **Platform:** Google Ads
- **Session:** https://claude.ai/code/session_018VvLTAjnHXZw3XAeRaMuPL

## Changes
| Account | Entity (type, name, ID) | Field | Before | After | Result |
|---|---|---|---|---|---|
| PP5449 - Midwest Sport & Spine (756-376-8919) | Budget of campaign "Perfect Patients - Greenwood" (budget 14308776661) | Daily budget | USD 188.00 | USD 125.00 | ✅ applied |
| PP5449 | Budget of campaign "Perfect Patients - Noblesville" (budget 7554124556) | Daily budget | USD 200.00 | USD 90.00 | ✅ applied |
| PP5449 | Campaign "Perfect Patients - Noblesville" (11560827514) | Search partners | On | Off | ✅ applied |
| PP5449 | Campaign "Perfect Patients - Greenwood" (22208313305) | Search partners | On | Off | ✅ applied |
| PP5449 | Keyword `chiropractor` BROAD, Greenwood › Chiropractor (175299730515~12457821) | Max CPC | USD 30.00 | USD 20.00 | ✅ applied |
| PP5449 | Keyword `back pain chiropractor` BROAD, Noblesville › Chiropractor Noblesville (115090293280~490534244) | Max CPC | USD 25.00 | USD 18.00 | ✅ applied |
| PP5449 | Greenwood › Chiropractor (175299730515) | New keyword | — | [chiropractor greenwood] EXACT, USD 20.00 (~340362937431) | ✅ applied |
| PP5449 | Greenwood › Chiropractor (175299730515) | New keyword | — | "chiropractor greenwood" PHRASE, USD 18.00 (~338274197668) | ✅ applied |
| PP5449 | Greenwood › Chiropractor Near Me (175299730275) | New keyword | — | "chiropractors near me" PHRASE, USD 16.00 (~18785721652) | ✅ applied |
| PP5449 | Campaigns Noblesville (11560827514) and Greenwood (22208313305) | Campaign negative keywords, PHRASE (15 per campaign, 30 total) | — | icd 10, cauda equina, fracture, ablation, emg test, cramps in the feet, perimenopause, sciatica belt, self hip adjustment, massagebook, body n motion, lc chiropractic, greenwood family chiropractic, family care chiropractic, net chiropractic technique | ✅ applied |

Daily and monthly effect of the budget change: combined daily budget USD 388 → USD 215 (−USD 173/day). Salesforce monthly budget is USD 5,000; USD 2,901.58 was spent 1–15 Oct, leaving about USD 2,098. At USD 215/day across the remaining scheduled days, October lands at about USD 4,800–5,000 instead of hitting the cap around 22–26 Oct and going dark for the rest of the month (as it did 23/24 Sep–1 Oct).

## Failed or skipped
None. All operations were validated (validate_only) and then applied with no errors.

## Notes
- Spanish ("quiropráctico") and Medicaid searches were not excluded: Sara found nothing about either on the website and isn't certain, so they're left running until confirmed with the client.
- Search partners in the last 30 days: USD 679, 1 conversion.
- Follow-ups: call tracking audit (Google call tracking vs WhatConverts uploads, which may double count calls) is in progress. Primary-goal cleanup and ad copy fixes (typo "Greenwood Family Chiroprator", reversed "Midwest Spine & Sport", USD 49 vs USD 20 offer, "Open Evenings" callout) will be previewed separately.
- Reset the daily budgets on 1 Nov so November lands at about USD 5,000.
