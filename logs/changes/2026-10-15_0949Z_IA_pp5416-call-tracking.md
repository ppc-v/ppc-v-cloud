# PP5416: turn on call-asset call reporting and fix call conversion goals

- **When:** 2026-10-15 09:49 UTC (17:49 Kuala Lumpur, Arif's time)
- **Requested by:** IA (Arif)
- **Approved by:** IA, approved preview A–D in chat; button-click goal kept primary on IA's instruction
- **Platform:** Google Ads
- **Session:** https://claude.ai/code/session_01WoSzo6g4kT9YTbm3NX4DEF

## Changes
| Account | Entity (type, name, ID) | Field | Before | After | Result |
|---|---|---|---|---|---|
| PP5416 - St Leonards Square Dental Care (289-453-0350) | Call asset (02) 7202 4320 (99627838724) | Call conversion reporting | DISABLED (action 179) | USE_RESOURCE_LEVEL_CALL_CONVERSION_ACTION → "Calls from ads" (6685891089) | ✅ applied |
| same | Conversion action "Calls from ads" (6685891089) | Counting | MANY_PER_CLICK | ONE_PER_CLICK | ✅ applied (stays primary) |
| same | Conversion action "Calls from Ad Extensions" (6812202193) | Counting / primary | MANY_PER_CLICK / primary | ONE_PER_CLICK / secondary | ✅ applied (primary change needed a second call, see notes) |
| same | Conversion action "Calls from Google Ads" (6812303445) | Counting | MANY_PER_CLICK | ONE_PER_CLICK | ✅ applied (stays primary) |

## Failed or skipped
- First update batch set counting on all three actions but did not change "Calls from Ad Extensions" to secondary, because the automatic field mask dropped `primary_for_goal = false` (default value). Re-applied with an explicit mask; verified secondary.
- "Book Online Button Clicks" (6644078394) left primary on IA's instruction.

## Notes
- The preview said the asset would use the account-level call action. The account-level action is 179, which does not appear in the conversion action list (probably an old system default), so the asset now points straight at the visible "Calls from ads" action instead. The intent is the same.
- Calls from ads count after 60 seconds (existing threshold). The ad now shows a Google forwarding number that forwards to 4320, so WhatConverts still logs these calls.
- Follow-ups: confirm whether 4319 is on the Google Business Profile (if so, change its WhatConverts source to google/organic). Revisit moving the button-click goal to secondary once calls are being counted. Request GA4 Editor access to G-GNHSPLVJH1. Raise the consent gap (AU).
