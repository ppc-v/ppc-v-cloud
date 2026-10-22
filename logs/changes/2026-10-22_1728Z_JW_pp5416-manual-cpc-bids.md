# PP5416: switch Max Conversions back to Manual CPC, reset bids, tidy keywords and negatives

- **When:** 2026-10-22 17:28 UTC (12:28 US Central, John's time)
- **Requested by:** JW (John)
- **Approved by:** JW, approved the full preview in chat ("give your recommendations a shot"); "cost" negative not approved, left out
- **Platform:** Google Ads
- **Session:** https://claude.ai/code/session_01WHrYeQhLtw2HfkA9KYKMYd

## Changes
| Account | Entity (type, name, ID) | Field | Before | After | Result |
|---|---|---|---|---|---|
| PP5416 - St Leonards Square Dental Care (289-453-0350) | Campaign "Smile Marketing" (20538393484) | Bid strategy | Maximize Conversions (no target CPA) | Manual CPC, enhanced CPC off | ✅ applied |
| same | Ad group "Dentist" (156295523714) | Default max CPC | AUD 20.00 | AUD 13.00 | ✅ applied |
| same | Ad group "Emergency" (153498606859) | Default max CPC | AUD 20.00 | AUD 14.00 | ✅ applied |
| same | Keyword "st leonards dentist" phrase (310187016864) | Max CPC | AUD 17.00 | AUD 15.00 | ✅ applied |
| same | Keyword "dentist near me" phrase (10538286510) | Max CPC | ad group default (AUD 20) | AUD 13.00 | ✅ applied |
| same | Keyword "Dentist" phrase (42566390) | Max CPC | ad group default (AUD 20) | AUD 13.00 | ✅ applied |
| same | Keyword "dentist near me" broad (5732504843) | Status | Enabled (ad group default AUD 20) | Paused | ✅ applied |
| same | Keyword "dentist" broad (10191500) | Status / max CPC | Paused / AUD 17.00 | Enabled / AUD 11.00 | ✅ applied |
| same | Keyword "emergency dentist" broad (12540101) | Status | Enabled (AUD 24.00) | Paused | ✅ applied |
| same | Keyword "Emergency dentist" phrase (3549218802) | Max CPC | AUD 20.00 | AUD 14.00 | ✅ applied |
| same | Keyword "emergency dental" phrase (129040224) | Max CPC | AUD 20.00 | AUD 14.00 | ✅ applied |
| same | Negative list "Search Terms" (10785462206, used only by this campaign) | Add phrase negatives | — | nest dental, worldciti, smiles2go, millennium dentistry, smile restore, no more gaps, lennox dental, pensioners, screwless, naturally, symptoms, lenses, limpieza, false teeth, denture repairs | ✅ applied (15 added) |
| same | Negative list "Search Terms" (10785462206) | Remove phrase negatives | artarmon (297484551504), cammeray (298860988948) | removed | ✅ applied |

Unchanged: daily budget AUD 82.23 (~AUD 2,500/month, Salesforce budget AUD 2,500), Mon–Thu 9–6 schedule, mobile +15%, Mon/Tue +10%, dentist [exact] AUD 15, dentist st leonards (broad) AUD 15.

## Failed or skipped
- None failed. All four batches were validated with validate_only first, then applied, then read back (bid strategy MANUAL_CPC, eCPC off, all bids, statuses and negatives confirmed).
- The first two apply attempts were blocked by the session's permission check before reaching Google; nothing was sent. Applied on John's retry request.
- "cost" negative proposed but not approved; not added.

## Notes
- Why: Max Conversions (3–22 Oct) vs manual (3 Aug–1 Oct): avg CPC AUD 12.10 → 21.70, clicks/week 32 → 26, cost/conversion AUD 127 → 278; 6 conversions in 3 weeks, all Book Online button clicks. Broad "dentist near me" took most spend at ~AUD 24 CPC, matching competitor names. ~3 conversions/week is too little data for automated bidding.
- "artarmon" and "cammeray" were blocking target suburbs (both inside targeted postcodes 2064 / 2062).
- Monitor at 1 and 2 weeks: CPC back to AUD 12–15, ~10 clicks per ad day, WhatConverts website calls (pool 4316) and "Calls from ads" (call asset, reporting on since 15 Oct, nothing recorded yet; test call if still zero), broad "dentist" search terms, cost/conversion vs ~AUD 127.
