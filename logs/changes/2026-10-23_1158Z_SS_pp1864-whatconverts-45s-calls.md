# PP1864: WhatConverts sends only 45s+ calls to Google Ads

- **When:** 2026-10-23, reported in chat at about 11:58 UTC (07:58 US Eastern for Sara; 05:58 Calgary)
- **Requested by:** SS
- **Approved by:** SS, who made the change herself
- **Platform:** WhatConverts (Google Ads integration)
- **Session:** https://claude.ai/code/session_01EiVWQEthbRXB2zN1t6GazV

## Changes
| Account | Entity | Field | Before | After | Result |
|---|---|---|---|---|---|
| PP1864 - Memorial Drive Chiropractic and Massage (WhatConverts profile 142918) | Google Ads integration: "Calls from Ad Extension" (7077936202) / "Calls from Google Ads" (7077936376), Google Ads 474-357-1274 | Call duration rule | All calls sent | Calls of 45s+ only | ✅ changed by SS in the WhatConverts UI (not verifiable through the API) |

## Failed or skipped
None.

## Notes
- On the last 90 days of calls (38 tagged google / cpc), the 45s rule would have dropped 10 calls (all under 25s: hang-ups during the greeting, missed calls) and kept all 11 new-patient calls (149s+). Existing-patient and admin calls over 45s still go through.
- Expect fewer imported conversions and a higher cost per conversion in Google Ads from here, while lead quality stays the same. Note this in reports.
- With Manual CPC since 2026-10-23, the conversion count no longer drives bidding; it mainly affects reporting.
