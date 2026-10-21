# September 2026: WhatConverts calls, new patients and bookings (all clients + Google Ads)

Requested by: SS (Sara), 2026-10-21. Builds on Arif's `reports/2026-09_phone-call-performance.md`.

**Google Sheet:** https://docs.google.com/spreadsheets/d/16pgSXiWArj7QjpNfhTmVP2LfBl98SNFzhqFXJAO-gOU/edit (tabs: Read me · All clients · Google Ads calls · By source · Call list). The call list holds no caller names, numbers, recordings or summaries. Use the WhatConverts lead ID to open a call.

CSV copies of the summary tabs: `2026-09_whatconverts-calls-all-clients.csv`, `2026-09_whatconverts-calls-google-ads.csv`, `2026-09_whatconverts-calls-by-source.csv`.

## What's new compared with Arif's report
- **Phone-menu "New Patient" field.** 94 WhatConverts profiles record the caller's IVR choice (New / Existing patient), so we know intent even for **missed** calls. It flags 3,200 new-patient calls vs 1,038 from the AI label alone. The two agree on 90% of calls where both exist. "New-patient call" = menu says new OR AI says New Customer (3,345 calls).
- **Booking outcome (estimated).** WhatConverts stores no booking result, so the AI summary of each of the 5,571 answered, summarised calls was labelled Booked / Enquired, not booked / Existing appt change / Other. Spot checks agreed with the summary wording 90–100% of the time. It shows a booking made on the call, not whether the patient turned up.
- **Call-backs.** For each missed call: did the same number reach the same practice within 7 days? This was matched in memory and no numbers are stored.
- **Owner / ads status** from the inventory, or from the Sara/John Google Ads labels for accounts outside the active book.

## Headlines
| | All clients | Google Ads only |
|---|---|---|
| Calls (accounts) | 9,141 (105) | 1,038 (70) |
| New-patient calls | 3,345 (37% of calls) | 674 (65% of calls) |
| …booked on the call | 751 | 193 |
| …enquired, not booked | 421 | 129 |
| …missed / voicemail | 1,317 (39%) | 221 (33%) |
| …missed and never got through within 7 days | 1,157 | 197 |
| New-patient booking rate (booked ÷ booked + not booked + missed) | 30% | 36% |
| Booking rate, answered appointment calls (all callers) | 75% | 62% |

- **Missed calls are the biggest leak.** Arif's report saw 6.6% of new-patient calls missed because the AI label is mostly blank for unanswered calls. The phone menu shows the real figure is 39%, and 88% of those callers never got through on a tracked number within a week. Practices that call back from their own lines wouldn't show here, so this is the worst case.
- Google Ads' new-patient booking rate (36%) is in line with organic (39%) and referral (36%) and above GBP (30%). Its value is the share of new-patient callers, not a higher close rate.
- Answered Google Ads appointment calls book less often than average (62% vs 75%): paid callers shop on price, insurance and availability.
- "GBP tagged cpc" (247 calls): 47% answered and 7 bookings from 166 new-patient calls. Worth checking which numbers these are.
- 67 "google / cpc" calls come from 5 clients **not in our MCC** (PP4073, PP4570, PP5089, PP5676, PP6645). That includes PP5676 120 Chiropractic, which Arif flagged, so those calls aren't from our campaigns.

## Gaps
- WhatConverts holds phone calls only for September (no forms, chats or bookings).
- Actual new patients won need practice-side data (PMS / online booking) or practices marking outcomes in WhatConverts.
- Dates are UTC. Small accounts swing a lot.
