# September 2026: phone call performance (WhatConverts)

Requested by: IA (Arif), 2026-10-21. Goal: assess how well phone calls bring new patients to clients.

**Source:** WhatConverts agency account, every profile, lead type "Phone Call", 1–30 Sep 2026. WhatConverts returns timestamps in UTC, so the month boundary is UTC rather than each client's local time, and a few calls at either end may fall in a neighbouring day locally. No calls were flagged spam or duplicate. Counts only: no caller details or transcript text are stored here.

**Method:**
1. WhatConverts' AI call analysis labels each answered call New Customer, Existing Customer or Other. 1,038 calls were labelled New Customer ("new-patient calls").
2. For those 1,038 calls, Claude read the AI summary and the transcript and recorded the outcome of the call: **booked** (an appointment was scheduled or confirmed on the call), **follow-up pending** (voicemail, callback promised, caller will call back or book online, office checking insurance), **not booked** (ended with no booking and no next step), or **not actually a new patient**. 16 calls (1.5%) fell in the last group and are excluded below.
3. A spot check of a random sample against the summaries agreed on 15 of 16. The one miss was a booking labelled as follow-up, so the booked numbers are if anything slightly low.

"Booked" means booked on the call. It doesn't capture bookings made later from a callback, or no-shows. Calls the AI labelled Other or didn't score (mostly unanswered) weren't read, so some new-patient bookings among them are missing.

## Headline
- **9,141 calls** across 105 client accounts. **1,022 were genuine new-patient enquiries, and 634 of them (62%) booked an appointment on the call.** Another 230 (23%) ended with a follow-up pending and 158 (15%) didn't book.
- Once a new patient gets through, the booking rate is about the same whatever the source (60–66%). **What differs is how many new patients each source brings in.**
- **Google Ads: 179 bookings from 1,038 calls, or 17 new-patient bookings per 100 calls.** That's 2–4× the other sources: Google Business Profile 4.8, organic 8.3, direct 7.3.
- Google Ads produced **28% of all new-patient bookings by phone from 11% of the calls.**

## By source
| Source | Calls | Answered | New-patient calls | Booked on call | Booked % of new-patient calls | Follow-up pending | Not booked | **Bookings per 100 calls** |
|---|---|---|---|---|---|---|---|---|
| **Google Ads** (google / cpc) | 1,038 | 81.5% | 281 | **179** | 64% | 53 | 49 | **17.2** |
| Google Business Profile | 5,488 | 86.2% | 432 | 263 | 61% | 100 | 69 | 4.8 |
| GBP tagged "cpc" | 247 | 46.6% | 12 | 8 | 67% | 2 | 2 | 3.2 |
| Organic search | 1,073 | 89.9% | 135 | 89 | 66% | 27 | 19 | 8.3 |
| Direct / offline / legacy numbers | 1,048 | 78.1% | 129 | 77 | 60% | 39 | 13 | 7.3 |
| Referral | 197 | 83.2% | 26 | 14 | 54% | 8 | 4 | 7.1 |
| Meta | 19 | 73.7% | 2 | 1 | 50% | 1 | 0 | 5.3 |
| Other | 31 | 71.0% | 5 | 3 | 60% | 0 | 2 | 9.7 |
| **Total** | **9,141** | **83.9%** | **1,022** | **634** | **62%** | **230** | **158** | **6.9** |

New-patient calls here exclude the 16 that turned out not to be new patients. The rest of the calls are existing patients (54% of scored calls), "Other" (vendors, wrong numbers, spam-like sales calls) or unscored.

## Why new-patient calls didn't book
| Reason | Follow-up pending | Not booked | Of which Google Ads (pending / not booked) |
|---|---|---|---|
| Caller will decide / call back | 92 | 7 | 26 / 3 |
| Voicemail or unanswered | 55 | 5 | 12 / 1 |
| No suitable appointment time | 26 | 47 | 4 / 14 |
| Price | 17 | 26 | 6 / 15 |
| Insurance not accepted / unclear | 15 | 30 | 2 / 5 |
| Service not offered | 0 | 16 | 0 / 8 |
| Information only | 0 | 14 | 0 / 1 |
| Other | 25 | 13 | 3 / 2 |

- **Availability is the biggest fixable reason a call is lost outright** (47 not booked, 26 more pending). The practice had no time that suited the caller.
- **Price is the top reason Google Ads callers walk away** (15 not booked). Paid search attracts more price-shoppers than other sources.
- **8 Google Ads new-patient calls asked for a service the practice doesn't offer**, which points to keyword or ad-copy mismatches.
- **92 callers said they'd decide and call back.** Practices that follow these up quickly should recover some of them.

## Accounts
Google Ads new-patient calls and bookings on the call (accounts with 5 or more):

| Account | GA new-patient calls | Booked | Booked % |
|---|---|---|---|
| PP4906 Back & Body Wellness Centre | 29 | 21 | 72% |
| PP5080 Blockhouse Bay Dental Centre | 19 | 9 | 47% |
| PP5006 Kinross Drive Dental | 15 | 12 | 80% |
| PP5596 Align Chiropractic Clinic | 13 | 10 | 77% |
| PP4960 The Tooth Affair | 11 | 10 | 91% |
| PP5449 Midwest Sport and Spine | 10 | 4 | 40% |
| PP5372 Mason Spine & Injury Center | 10 | 7 | 70% |
| PP4348 Vision Dental | 9 | 5 | 56% |
| PP5353 Aurora Dental | 9 | 4 | 44% |
| PP4773 Restoring Life Chiropractic | 8 | 3 | 38% |
| PP6724 Lakeside Align Chiropractic | 8 | 3 | 38% |
| PP0315 Marstellar Family Chiropractic | 8 | 6 | 75% |
| PP5813 Shenton Park Village Dental | 7 | 5 | 71% |
| PP5154 TC Smiles | 6 | 1 | 17% |
| PP6645 Optimal Align Chiropractic | 6 | 1 | 17% |
| PP5999 Hervey Bay Dental | 6 | 5 | 83% |
| PP6066 Morley Chiropractic | 6 | 6 | 100% |
| PP4956 Lightwood Dental | 6 | 6 | 100% |
| PP6481 ChiroPro | 6 | 3 | 50% |
| PP6282 Dentist in Hervey Bay | 5 | 4 | 80% |
| PP6596 Peak Performance Sport & Spine | 5 | 4 | 80% |
| PP0573 Chaparral Chiropractic | 5 | 3 | 60% |
| PP3899 Lindenwoods Chiropractic | 5 | 5 | 100% |

**Front desks converting the fewest new-patient callers** (all sources, 8 or more new-patient calls): PP4537 Shows Chiropractic 2 of 10, PP1935 Beacon Hill Chiropractic 11 of 35, PP6645 Optimal Align 4 of 12, PP5449 Midwest Sport and Spine 4 of 10, PP0500 Alexander Chiropractic 35 of 85, PP4610 Westheights 5 of 12. Most of these lose callers to "will call back" and availability rather than to the ads, so they're worth raising with the client as a front-desk conversation.

**Paid calls bringing in no new patients:** PP6236 Pullen Dental (15 Google Ads calls) and PP5676 120 Chiropractic (10) had no new-patient calls at all. Check search terms, call assets, and whether existing patients are clicking the ads.

## Missed calls
192 of 1,038 Google Ads calls (18.5%) weren't answered, and WhatConverts mostly doesn't score or transcribe those. If they follow the answered mix, that's roughly 70 prospective new patients and about 45 lost bookings from Google Ads alone. Accounts answering least: PP2122 Adelphia (31% answered), PP5063 Essential Dental Care (47%), PP3599 Martindale (53%), PP5353 Aurora Dental (65%).

## Other notes
- **"GBP tagged cpc" (247 calls)** has only 47% answered and few new patients. These are probably Maps / location-asset calls or mis-tagged numbers. Check them before counting them as paid.
- **Meta drives almost no phone calls** (19 in the month).
- **Only 42.7% of Google Ads calls carry a GCLID**, so most can't be tied to a campaign or keyword. Calls from call assets on the ad have no GCLID, which explains part of it.
- Small per-account numbers swing a lot. Treat accounts with fewer than about 10 new-patient calls as indicators only.

Per-account detail: `reports/2026-09_phone-calls-by-account.csv`.
