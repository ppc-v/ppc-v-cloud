# September 2026: WhatConverts calls, new patients and bookings (all clients + Google Ads)

Requested by: SS (Sara), 2026-10-21. Builds on Arif's `reports/2026-09_phone-call-performance.md`.

**Google Sheet:** https://docs.google.com/spreadsheets/d/16pgSXiWArj7QjpNfhTmVP2LfBl98SNFzhqFXJAO-gOU/edit (tabs: Read me · All clients · Google Ads calls · GBP numbers tagged paid · Google Ads + GBP combined · By source · Call list). The call list holds no caller names, numbers, recordings or summaries. Use the WhatConverts lead ID to open a call.

CSV copies of the summary tabs: `2026-09_whatconverts-calls-{all-clients,google-ads,gbp-numbers-tagged-paid,google-ads-plus-gbp,by-source}.csv`.

## What's new compared with Arif's report
- **Phone-menu "New Patient" field.** 94 WhatConverts profiles record the caller's IVR choice (New / Existing patient), so we know intent even for **missed** calls. It flags 3,200 new-patient calls vs 1,038 from the AI label alone. The two agree on 90% of calls where both exist. "New-patient call" = menu says new OR AI says New Customer (3,345 calls).
- **Booking outcome (estimated).** WhatConverts stores no booking result, so the AI summary of each of the 5,571 answered, summarised calls was labelled Booked / Enquired, not booked / Existing appt change / Other. Spot checks agreed with the summary wording 90–100% of the time. It shows a booking made on the call, not whether the patient turned up.
- **Call-backs.** For each missed call: did the same number reach the same practice within 7 days? This was matched in memory and no numbers are stored.
- **Owner / ads status** from the inventory, or from the Sara/John Google Ads labels for accounts outside the active book.

## Which calls count as Google Ads (updated 2026-10-21 after Sara's question)
Calls are grouped by **tracking number**, not only by WhatConverts' source tag, so that no paid number is missed:
- **Google Ads numbers** (849 calls, 67 accounts): the dynamic "All Traffic" pool when the visitor came from an ad (google / cpc), plus numbers named for Google Ads ("Google Ads Extension" call assets, "Google Ads Calls", "Google Ads – <location>"), whatever source they were tagged with.
- **GBP numbers tagged paid** (487 calls, 49 accounts): Business Profile numbers named or tagged as paid ("GBP Ads Extension", "Google Business Profile Ads Extension", "Google My Business Ads", "GMB Ad Extension"). They're probably on the Business Profile itself, so they likely take organic Maps calls too. Only 2% have a GCLID. PP6773's (…6449) took 138 calls in September vs about 13 on its Ads numbers. Only 21% were answered, 87% were first-time callers, and it went to 0 in October, which looks like robocalls or a routing fault. Treat this group as "possibly paid".
- **Combined** (1,336 calls): the upper bound. The earlier version of this report used google / cpc only (1,038), which mixed in 239 GBP-number calls and missed 298 calls on Ads-named numbers.

## Headlines
| | All clients | Google Ads numbers | GBP numbers tagged paid | Combined |
|---|---|---|---|---|
| Calls (accounts) | 9,141 (105) | 849 (67) | 487 (49) | 1,336 (71) |
| Answered | 84% | 78% | 66% | 73% |
| New-patient calls | 3,345 (37%) | 582 (69%) | 297 (61%) | 879 (66%) |
| …booked on the call | 751 | 149 | 53 | 202 |
| …enquired, not booked | 421 | 111 | 24 | 135 |
| …missed / voicemail | 1,317 | 218 | 166 | 384 |
| …missed and never got through within 7 days | 1,157 | 199 | 160 | 359 |
| New-patient booking rate | 30% | 31% | 22% | 28% |

- **Missed calls are the biggest leak.** Arif's report saw 6.6% of new-patient calls missed because the AI label is mostly blank for unanswered calls. The phone menu shows the real figure is 39%, and 88% of those callers never got through on a tracked number within a week. Practices that call back from their own lines wouldn't show here, so this is the worst case.
- Google Ads' new-patient booking rate (31%) is similar to organic (39%), referral (36%) and GBP (30%). Its value is the share of new-patient callers (69%), not a higher close rate.
- Answered Google Ads appointment calls book less often than average (59% vs 75%): paid callers shop on price, insurance and availability.
- 5 clients with "google / cpc" calls aren't in our MCC (PP4073, PP4570, PP5089, PP5676, PP6645). That includes PP5676 120 Chiropractic, which Arif flagged, so those calls aren't from our campaigns.

## Gaps
- WhatConverts holds phone calls only for September (no forms, chats or bookings).
- Actual new patients won need practice-side data (PMS / online booking) or practices marking outcomes in WhatConverts.
- Dates are UTC. Small accounts swing a lot.
