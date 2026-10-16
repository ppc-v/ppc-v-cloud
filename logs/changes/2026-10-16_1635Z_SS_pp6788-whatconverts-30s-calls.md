# PP6788: WhatConverts sends only 30s+ calls to Google Ads

- **When:** 2026-10-16, reported in chat at about 16:35 UTC (12:35 US Eastern, Sara)
- **Requested by:** SS
- **Approved by:** SS, who made the change herself
- **Platform:** WhatConverts (Google Ads integration)
- **Session:** https://claude.ai/code/session_01LBMSMa2Rm2AJQJQHz4fbdu

## Changes
| Account | Entity (type, name, ID) | Field | Before | After | Result |
|---|---|---|---|---|---|
| PP6788 - Resolve Chiropractic and Wellness (WhatConverts profile) | Google Ads integration → "Calls From Ad Extensions" / "Calls From Google Ads" (Google Ads 7757609264 / 7757747947) | Call duration rule | All calls sent | Calls of 30s+ only | ✅ changed by SS in the WhatConverts UI (not verifiable through the API) |

## Failed or skipped
None.

## Notes
- Reason: in the first 30 days, 12 of 29 Google Ads calls were under 30s (hang-ups, IVR, misdials), and every one counted as a primary conversion for Max Conversions bidding.
- Expect fewer conversions from here, and a higher cost per lead in Google Ads, while lead quality stays the same. Note this in reports.
- Check: compare WhatConverts calls under 30s with the Google Ads imported call conversions over the next week.
