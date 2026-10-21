# September 2026: phone call performance (WhatConverts)

Requested by: IA (Arif), 2026-10-21. Goal: assess how well phone calls bring new patients to clients.

**Source:** WhatConverts agency account, every profile, lead type "Phone Call", 1–30 Sep 2026. WhatConverts returns timestamps in UTC, so the month boundary is UTC rather than each client's local time, and a few calls at either end may fall in a neighbouring day locally. No calls were flagged spam or duplicate. Counts only: no caller details are stored here.

**What "new patient" means here:** WhatConverts' AI call analysis labels each answered call as New Customer, Existing Customer or Other. That shows the caller was a *prospective* new patient, not that an appointment was booked. WhatConverts has no booking outcome for these calls: sales values are empty and "quotable" is mostly unset. So the numbers below show new-patient *opportunities* by phone, not patients won.

## Headline
- **9,141 calls** across 105 client accounts; 3,926 from first-time numbers ("Unique").
- **1,038 calls (14% of AI-scored calls) were prospective new patients.** 54% were existing patients and 32% were "other" (vendors, spam-like sales calls, wrong numbers).
- **Google Ads calls are by far the most new-patient-heavy: 36.6% of scored calls**, compared with 9.7% for Google Business Profile and about 15% for organic and direct.
- Google Ads produced **285 new-patient calls from 1,038 calls (27% of the total), across 70 accounts**, close to as many as Google Business Profile (438) from one fifth of the volume.
- 84% of all calls were answered. Of the new-patient calls the AI could score, 6.6% ended in voicemail or a hang-up. That understates the real loss, because unanswered calls are mostly not scored (below).

## By source
| Source | Calls | Answered | Scored by AI | New-patient calls | New-patient % of scored | Existing % | New-patient calls missed / voicemail | Median length |
|---|---|---|---|---|---|---|---|---|
| **Google Ads** (google / cpc) | 1,038 | 81.5% | 779 | **285** | **36.6%** | 34.9% | 13 | 87s |
| Google Business Profile | 5,488 | 86.2% | 4,520 | 438 | 9.7% | 59.0% | 33 | 75s |
| GBP tagged "cpc" | 247 | 46.6% | 161 | 12 | 7.5% | 17.4% | 0 | 60s |
| Organic search | 1,073 | 89.9% | 904 | 137 | 15.2% | 53.1% | 13 | 90s |
| Direct / offline / legacy numbers | 1,048 | 78.1% | 836 | 132 | 15.8% | 53.2% | 9 | 81s |
| Referral | 197 | 83.2% | 151 | 27 | 17.9% | 45.0% | 1 | 86s |
| Meta | 19 | 73.7% | 17 | 2 | 11.8% | 47.1% | 0 | 90s |
| Other | 31 | 71.0% | 23 | 5 | 21.7% | 52.2% | 0 | 69s |
| **Total** | **9,141** | **83.9%** | **7,391** | **1,038** | **14.0%** | **53.8%** | **69** | **78s** |

## What this says about calls and new patients
1. **Paid search calls are mostly new-patient enquiries.** About 1 in 3 scored Google Ads calls is a prospective new patient, against about 1 in 10 for GBP. Most GBP calls are existing patients rescheduling or asking questions. Judge paid calls on their own rate, not the practice's overall call volume.
2. **They are real conversations.** Of the 285 Google Ads new-patient calls, 227 lasted over 2 minutes and 255 were classed as "Sales" calls. 268 reached a live person.
3. **Missed calls are the biggest leak.** 192 of 1,038 Google Ads calls (18.5%) were not answered. WhatConverts doesn't score most unanswered calls (259 Google Ads calls are unscored), so their intent is unknown. If they match the answered mix, that's roughly **70 more prospective new patients from Google Ads alone who didn't reach anyone**. Accounts where answering is weakest: PP2122 Adelphia (31% answered), PP5063 Essential Dental Care (47%), PP3599 Martindale (53%), PP5353 Aurora Dental (65%).
4. **Some accounts' paid calls bring in few new patients.** PP6236 Pullen Dental (15 Google Ads calls, 0 new patients) and PP5676 120 Chiropractic (10 calls, 0 new patients) are worth a look at search terms, call assets and whether existing patients are clicking the ads.
5. **Strong paid-call accounts** (new-patient share of Google Ads calls): PP5596 Align Chiropractic 87% (13/15), PP5372 Mason Spine 77% (10/13), PP5080 Blockhouse Bay Dental 54% (19/35), PP5353 Aurora Dental 53%, PP4348 Vision Dental 53%, PP4906 Back & Body 49% (29/59, the largest paid-call volume).
6. **"GBP tagged cpc" (247 calls) behaves differently:** only 47% answered and few new patients. It's probably calls from Google Maps / location assets on Ads, or mis-tagged numbers. Worth checking which numbers these are before counting them as paid.
7. **Meta drives almost no phone calls** (19 in the month). Meta's value is in forms and messages, not calls.

## Gaps in the data
- **Booked appointments aren't recorded anywhere we can read.** To measure "calls that became patients" we need either practices marking outcomes in WhatConverts (quotable / sales value) or booking data from the practice management system or online booking. 88 Google Ads calls are marked "quotable: Yes", which suggests a few profiles do this. That's too few to use.
- **Only 42.7% of Google Ads calls carry a GCLID**, so most can't be matched back to a campaign or keyword in Google Ads. Calls from call assets on the ad itself have no landing-page GCLID, which explains part of it.
- AI labels are an estimate and individual calls can be mislabelled. Use the per-account numbers as indicators where volume is low.

Per-account detail: `reports/2026-09_phone-calls-by-account.csv`.
