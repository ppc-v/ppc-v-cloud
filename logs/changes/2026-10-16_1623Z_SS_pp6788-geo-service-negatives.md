# PP6788: negatives for McKinney, Frisco, softwave and laser

- **When:** 2026-10-16 16:23 UTC (12:23 US Eastern, Sara)
- **Requested by:** SS
- **Approved by:** SS, direct instruction in chat ("block mckinney", "block Frisco if further than 12mi", "no softwave or laser")
- **Platform:** Google Ads
- **Session:** https://claude.ai/code/session_01LBMSMa2Rm2AJQJQHz4fbdu

## Changes
| Account | Entity (type, name, ID) | Field | Before | After | Result |
|---|---|---|---|---|---|
| PP6788 - Resolve Chiropractic and Wellness (238-150-2203) | Shared negative list "Search Queries" (12255104966) | Members | 234 | 239: + mckinney, frisco, softwave, soft wave, laser (phrase) | ✅ applied, 5/5 |

## Failed or skipped
- WhatConverts: SS asked for only 30s+ calls to go to Google Ads. Not done: the WhatConverts API has no endpoint for integration settings, so it has to be changed in the WhatConverts UI.

## Notes
- Distances from the practice (1061 N Preston Rd, Celina): McKinney center 12.1 mi, Frisco center 13.0 mi. North Frisco (around US 380) is about 8 mi away, so the Frisco negative also blocks searchers near the edge of the 8 mi radius. SS's rule: block if over 12 mi.
- Shockwave is offered, so it stays unblocked. Softwave and laser aren't offered.
