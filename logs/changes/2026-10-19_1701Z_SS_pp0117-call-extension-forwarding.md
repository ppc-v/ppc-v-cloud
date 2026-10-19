# PP0117: turn on Google call reporting on the call extension (secondary action) so WhatConverts call imports can match

- **When:** 2026-10-19 17:01 UTC (13:01 EDT for Sara)
- **Requested by:** SS
- **Approved by:** SS, approved the preview in chat ("do what you need to do to get calls to come through")
- **Platform:** Google Ads
- **Session:** https://claude.ai/code/session_01BwBaixcA8hEbMDfkToMWq1

## Changes
Account: PP0117 - Funnell Chiropractic (470-953-8470).

| Entity (type, name, ID) | Field | Before | After | Result |
|---|---|---|---|---|
| Conversion action "Google call extension calls (observe only)" (7857040504) | New | none | AD_CALL, Phone call lead, **secondary**, count one, 60 s, no value | ✅ applied |
| Call asset (08) 6830 1993 (48187391158) | Call conversion reporting | Disabled | Resource-level action 7857040504 | ✅ applied |

Primary goals are unchanged: Calls From Google Ads, Calls From Ad Extensions (WhatConverts imports) and Reached Online Booking Page.

## Failed or skipped
None.

## Notes
- Why: in the last 12 months WhatConverts logged 19 google/cpc calls on the call-extension number, while Google Ads recorded 0 phone calls and has no call_view records, and "Calls From Ad Extensions" has never received an upload. Google forwarding numbers weren't being used, so WhatConverts' caller-ID import had nothing to match. Turning call conversion reporting on for the asset should make Google use a forwarding number again.
- The new action is secondary, so it isn't counted in Conversions or used for bidding; the WhatConverts import stays the counted source (CLAUDE.md calls rule).
- To check around 2026-10-27: call_view / phone_calls in Google Ads, and uploads to "Calls From Ad Extensions" in the offline upload summary. If Google sees calls but uploads don't arrive, check the WhatConverts Google Ads integration (call-extension import on, mapped to "Calls From Ad Extensions").
