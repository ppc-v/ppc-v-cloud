# PP5449: stop double-counted calls, call assets reporting on, headline typo fix

- **When:** 2026-10-16 14:36 UTC (10:36 US Eastern, Sara's usual timezone)
- **Requested by:** SS
- **Approved by:** SS, "apply all recommended changes" after the tracking audit preview in chat
- **Platform:** Google Ads
- **Session:** https://claude.ai/code/session_018VvLTAjnHXZw3XAeRaMuPL

## Changes
| Account | Entity (type, name, ID) | Field | Before | After | Result |
|---|---|---|---|---|---|
| PP5449 - Midwest Sport & Spine (756-376-8919) | Conversion action "Calls from ads" (810422319, AD_CALL) | Counting | Every (MANY_PER_CLICK) | One (ONE_PER_CLICK) | ✅ applied |
| PP5449 | Conversion action "Calls from ads" (810422319) | Call length to count | 1 s | 60 s | ✅ applied |
| PP5449 | Conversion action "Calls from Google Ads" (6812210609, WhatConverts UPLOAD_CLICKS) | Counting | Every | One | ✅ applied |
| PP5449 | Conversion action "Calls from Ad Extensions" (6812210621, WhatConverts UPLOAD_CALLS) | Primary / Counting | Primary, Every | Secondary, One | ✅ applied |
| PP5449 | Conversion action "Calls from Website" (480464571, WEBSITE_CALL) | Primary / Counting | Primary, Every | Secondary, One | ✅ applied |
| PP5449 | Call asset (317) 296-8308 (asset 49444305112) | Call conversion reporting | Disabled | On, using "Calls from ads" (810422319) | ✅ applied |
| PP5449 | Call asset (317) 279-5966 (asset 201133400377) | Call conversion reporting | Disabled | On, using "Calls from ads" (810422319) | ✅ applied |
| PP5449 | RSA 732104525710, Greenwood › Chiropractor | Headline (pinned position 1) | "Greenwood Family Chiroprator" | "Trusted Greenwood Chiropractor" | ✅ applied (other headlines and pins unchanged; ad goes back through review) |

## Failed or skipped
- Conversion action "Contact Us Page view (All Web Site Data)" (486341499, hidden Universal Analytics goal): primary → secondary was **refused** by the API ("Mutates are not allowed for the requested resource"). Its category (page view) isn't biddable at account level and UA no longer sends data, so it has no effect on reporting or bidding. A person needs to remove it in the Google Ads UI to clear the inventory's weak-goal flag.
- "Open Evenings" callout left as is until SS confirms the practice's hours.

## Notes
- Result: calls from ads are counted once, by Google's call tracking (60 s minimum). Website calls are counted once, by WhatConverts' click-ID upload ("Calls from Google Ads"). Forms are counted by "Appointment Request Submission" (GA4). The account uses manual CPC, so this changes reporting, not bidding.
- Expect slightly fewer, more accurate conversions from now on: duplicates and calls under 60 s are no longer counted. Compare CPL to the period before 16 Oct with that in mind.
- A call asset with a Brazilian-format number, (19) 3722-0601 (asset 354925386057), is still in the asset library from the April 2026 hijack. Its account-level link is already removed, so nothing serves it.
- Still to do: get GTM-P6CX8J5 Publish access and GA4 Editor access for paidsearch@. Optionally, filter the WhatConverts Google Ads upload to 60 s+ calls (WhatConverts UI, profile 125418).
