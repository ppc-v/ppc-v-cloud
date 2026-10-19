# PP0117: revert Google call conversion tracking (calls come from WhatConverts)

- **When:** 2026-10-19 16:53 UTC (12:53 EDT for Sara)
- **Requested by:** SS
- **Approved by:** SS, approved the revert preview in chat ("yes please")
- **Platform:** Google Ads
- **Session:** https://claude.ai/code/session_01BwBaixcA8hEbMDfkToMWq1

## Changes
Account: PP0117 - Funnell Chiropractic (470-953-8470). Undoes items 15–16 of `2026-10-19_1643Z_SS_pp0117-october-review-fixes.md`.

| Entity (type, name, ID) | Field | Before | After | Result |
|---|---|---|---|---|
| Call asset (08) 6830 1993 (48187391158) | Call conversion reporting | Resource-level action 7856876390 | Disabled | ✅ applied |
| Conversion action "Calls from ads (call extension, 60s+)" (7856876390) | Status | Enabled, primary | Removed | ✅ applied |
| Conversion action "Calls From Ad Extensions" (6802290174) | Primary | Secondary | Primary | ✅ applied |

## Failed or skipped
None.

## Notes
- Sara: Google's "Calls from ads" was removed earlier on purpose, because calls are imported from WhatConverts and a Google call action would double count them.
- Both WhatConverts call actions keep counting "one" (changed earlier today).
- The new action was live for about 10 minutes and recorded no conversions.
- Open question: "Calls From Ad Extensions" has recorded 0 conversions in 90 days, and the one paid call WhatConverts logged on the call asset number had no GCLID. The call-asset import may not be working.
