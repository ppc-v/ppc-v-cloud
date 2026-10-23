# PP6742: WhatConverts sends only 45s+ calls to Google Ads

- **When:** 2026-10-23, reported in chat at about 12:14 UTC (08:14 US Eastern for Sara and the account)
- **Requested by:** SS
- **Approved by:** SS, who made the change herself
- **Platform:** WhatConverts (Google Ads integration)
- **Session:** https://claude.ai/code/session_01EiVWQEthbRXB2zN1t6GazV

## Changes
| Account | Entity | Field | Before | After | Result |
|---|---|---|---|---|---|
| PP6742 - Touch Light Chiropractic (WhatConverts profile 171730) | Google Ads integration: "Calls From Ad Extensions" (7693839803) / "Calls From Google Ads" (7693840052), Google Ads 288-398-9795 | Call duration rule | All calls sent | Calls of 45s+ only | ✅ changed by SS in the WhatConverts UI (not verifiable through the API) |

## Failed or skipped
None.

## Notes
- On the 50 ad calls since late July, the rule would have dropped 20 (under 45s: greeting/menu hang-ups and missed calls) and kept all 8 quotable new-patient calls.
- Expect fewer imported conversions in Google Ads; note this in reports.
- SS is telling the client about missed calls / voicemail during ad hours.
