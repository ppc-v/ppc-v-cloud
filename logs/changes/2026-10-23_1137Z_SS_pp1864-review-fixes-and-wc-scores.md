# PP1864: Google Ads review fixes + WhatConverts call scores

- **When:** WhatConverts 2026-10-23 11:37 UTC; Google Ads 11:42 UTC (07:37 / 07:42 US Eastern for Sara; 05:37 / 05:42 Calgary)
- **Requested by:** SS
- **Approved by:** SS: "apply the scores above" (WhatConverts preview) and "approve all" (Google Ads preview), in chat
- **Platform:** WhatConverts, Google Ads
- **Session:** https://claude.ai/code/session_01EiVWQEthbRXB2zN1t6GazV

## Changes
### WhatConverts (profile 142918)
| Lead ID | Field | Before | After | Result |
|---|---|---|---|---|
| 263525961 (14 Oct, 218s, new patient booked) | Quotable | Not Set | Yes | ✅ read back |
| 263562174 (14 Oct, 8s, hung up during greeting) | Quotable | Not Set | No | ✅ read back |
| 258033626 (14 Sep, 149s, new patient accepted an appointment) | Quotable | Pending | Yes | ✅ read back |

### Google Ads: PP1864 (474-357-1274), campaign "Perfect Patients" (22378360978), ad group "Chiropractor Calgary" (183813770344)
The campaign is paused by the monthly budget rule until 1 Nov.

| Entity | Field | Before | After | Result |
|---|---|---|---|---|
| Budget 14431528302 | Daily | CAD 150 | CAD 85 (expected about CAD 85-170 per scheduled day, about CAD 1,920/month) | ✅ |
| Conversion action "Calls from ads" (7091289085) | Primary | Primary | Secondary (stops double counting with the WhatConverts call imports) | ✅ read back |
| Campaign | Bid strategy | Maximize conversions | Manual CPC (no eCPC) | ✅ |
| "chiropractor calgary" phrase (300108680850) | Status / max CPC | Paused | Enabled, CAD 20 | ✅ |
| "chiropractor" exact (70618091) | Max CPC | - | CAD 18 | ✅ |
| "sciatica chiropractor" exact (177138236), "back pain chiropractor" phrase (677899681) + exact (752947702), "chiropractor downtown calgary" exact (295514774082) | Max CPC | - | CAD 16 | ✅ |
| "chiropractor near me" broad (564075452), "chiropractor" broad (12457821), "neck pain chiropractor" broad (851898006) | Status | Enabled | Paused | ✅ |
| New: "chiropractor near me" phrase (24314362356) + exact (24315031836) | Created | - | Enabled, CAD 20 | ✅ under review |
| New: "chiropractor" phrase (20640151), "neck pain chiropractor" phrase (2971518580) | Created | - | Enabled, CAD 16 | ✅ under review |
| Shared list "Search Queries" (11529285089) | Added 31 phrase negatives | - | hip and knee · knee clinic · hip clinic · primaris · synapse · one8t · wells health · connecta · shepard health · beaconhill · revolve chiropractic · gehrke · takahashi · lethbridge · south calgary family chiropractic · active steps · mendable · smooth spine · tania carreon · ccst · feet it · mass muscle · corrector · salonpas · back brace · podiatrist · orthopedist · orthopedics · scenar · discseel · bodyworker | ✅ |
| Proximity targets 2460446298949 (2 km), 2460446299109 (4 km), 2460446299149 (6 km), 2410504760864 (8 km) | Removed | 2/4/6/8/10 km | 10 km only | ✅ |

## Failed or skipped
- The first validation of "chiropractor near me" (phrase and exact) failed with the policy HEALTH_IN_PERSONALIZED_ADS (exemptible). I resubmitted with an exemption request: the keyword can't be used for personalised/audience ads, but normal search serving is unaffected (the old broad version ran the same way).
- The preview said "30" negatives; the actual list is 31 (it included "back brace").
- Not done: new RSA (offer confirmed as $49 by SS; draft sent for approval); the 60s+ call rule in WhatConverts' Google Ads integration (SS does this in the WhatConverts UI); form tracking audit (needs GTM access).

## Notes
- Check pacing after the first week of November (Manual CPC may not spend 2x a day the way Max Conv did).
- On a 14 Oct call the front desk quoted "$99 for the first visit" while the ads offer a $49 exam. Worth raising with the client.
