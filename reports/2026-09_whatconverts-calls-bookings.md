# September 2026: WhatConverts calls, new patients and bookings (all clients + Google Ads)

Requested by: SS (Sara), 2026-10-21. Builds on Arif's `reports/2026-09_phone-call-performance.md`.

**Google Sheet:** https://docs.google.com/spreadsheets/d/16pgSXiWArj7QjpNfhTmVP2LfBl98SNFzhqFXJAO-gOU/edit (tabs: Read me · All clients · Google Ads calls · By source · Call list). The call list holds no caller names, numbers, recordings or summaries. Use the WhatConverts lead ID to open a call.

CSV copies of the summary tabs: `2026-09_whatconverts-calls-{all-clients,google-ads,by-source}.csv`.

## What's new compared with Arif's report
- **Phone-menu "New Patient" field.** 94 WhatConverts profiles record the caller's IVR choice (New / Existing patient), so we know intent even for **missed** calls. It flags 3,200 new-patient calls vs 1,038 from the AI label alone. The two agree on 90% of calls where both exist. "New-patient call" = menu says new OR AI says New Customer (3,345 calls).
- **Booking outcome (estimated).** WhatConverts stores no booking result, so the AI summary of each of the 5,571 answered, summarised calls was labelled Booked / Enquired, not booked / Existing appt change / Other. Spot checks agreed with the summary wording 90–100% of the time. It shows a booking made on the call, not whether the patient turned up.
- **Call-backs.** For each missed call: did the same number reach the same practice within 7 days? This was matched in memory and no numbers are stored.
- **Owner / ads status** from the inventory, or from the Sara/John Google Ads labels for accounts outside the active book.

## Which calls count as Google Ads (final, 2026-10-21)
Sara asked for Google Ads calls only, with no organic calls. A call counts only with evidence it came from our ads:
- **Number is a Google Ads call asset** (333): the WhatConverts tracking number is attached (not removed) as a call asset in the client's Google Ads account, checked through the API on 2026-10-21.
- **Call has a Google Ads click ID** (414).
- **Visitor came from an ad** (109): WhatConverts' website number pool, google / cpc.
- **Number named for Google Ads** (18): e.g. "Google Ads Calls", with no other evidence.

**GBP numbers named "Ads Extension" or tagged cpc count only if Google Ads proves it.** That's 25 of 487 calls: PP3899 and PP6313 use their GBP number as a call asset, and 9 calls had a click ID. The other 462 are on numbers not used anywhere in Google Ads, so they're counted as Google Business Profile (organic). Example: PP6773's GBP number …6449 took 138 calls, only 21% were answered, and it went to 0 in October. Worth checking for robocalls or a routing fault.

Result: **874 Google Ads calls** (67 accounts). The first version of this report used google / cpc only (1,038), which included 217 organic GBP-number calls tagged google / cpc and missed some call-asset calls with other tags. 64 of the 874 come from 5 clients not in our MCC (PP4073, PP4570, PP5089, PP5676, PP6645): paid Google clicks, but not from our campaigns.

## Headlines
| | All clients | Google Ads only |
|---|---|---|
| Calls (accounts) | 9,141 (105) | 874 (67) |
| Answered | 84% | 78% |
| New-patient calls | 3,345 (37%) | 592 (68%) |
| …booked on the call | 751 | 154 |
| …enquired, not booked | 421 | 112 |
| …missed / voicemail | 1,317 | 219 |
| …missed and never got through within 7 days | 1,157 | 199 |
| New-patient booking rate | 30% | 32% |
| Booking rate, answered appointment calls | 75% | 60% |

- **Missed calls are the biggest leak.** Arif's report saw 6.6% of new-patient calls missed because the AI label is mostly blank for unanswered calls. The phone menu shows the real figure is 39%, and 88% of those callers never got through on a tracked number within a week. Practices that call back from their own lines wouldn't show here, so this is the worst case.
- Google Ads' new-patient booking rate (32%) is similar to organic (39%), referral (36%) and GBP (28%). Its value is the share of new-patient callers (68%), not a higher close rate.
- Answered Google Ads appointment calls book less often than average (60% vs 75%): paid callers shop on price, insurance and availability.

## Gaps
- WhatConverts holds phone calls only for September (no forms, chats or bookings).
- Actual new patients won need practice-side data (PMS / online booking) or practices marking outcomes in WhatConverts.
- Dates are UTC. Small accounts swing a lot.
