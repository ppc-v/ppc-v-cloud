# PP3074 - Doster Chiropractic

- **Google Ads ID:** 437-163-4545 (US Eastern, USD)
- **Meta ad account ID:** none in the inventory
- **WhatConverts profile:** yes (calls imported as "Calls from Google Ads" and "Calls from Ad Extensions")
- **GTM container / GA4 property:** GTM-5ZHJGTP (paidsearch@ has no GTM access yet, see `reports/2026-10-21_gtm-access-gaps.md`)
- **Website:** https://www.dosterchiropractic.com (ads land on /chiropractor-asheville/)
- **Office:** 388 Merrimon Ave, Asheville NC 28801; hours Mon-Fri 9am-12pm and 2-6pm; (828) 236-2200
- **Access:** normal
- **Usually worked on by:** Sara

## Goals and preferences
- Salesforce Google budget: USD 1,000/month (billing date 11). The team's monthly rule pauses the account when it reaches the budget.

## Setup (as of 2026-10-23)
- Live campaign "Perfect Patients" (Search; Maximize conversions; USD 46/day; Mon-Fri 9am-6pm; radius 3/6/8 mi around 388 Merrimon Ave, "presence or interest"; mobile +10%, desktop -15%). One live ad group, "Chiropractor Asheville", with 3 keywords: chiropractor asheville (phrase), chiropractor near me (exact), chiropractor (phrase). One RSA, with all 15 headlines pinned.
- "Perfect Patients Near Me" (manual CPC) has been paused since April with no spend.
- The shared negative list "Negatives - Search Terms" (3,244 terms) includes "doster" / "dr doster" (brand excluded) and "family chiropractic" (phrase).

## Tracking
- Primary conversions: Appointment Request (New Patient) and (Current Patient) from GA4, plus the two WhatConverts call imports. Current-patient requests count as conversions, which inflates leads.

## History and decisions
- 2026-04: account hacked. 20 rogue "CBH-NC-..." campaigns (gambling-style names) spent USD 2,291 in April; all removed. No spend May-July; restarted in August.
- 2026-10-22: paused by the monthly budget rule at USD 1,042, so dark 23-31 Oct.
- 2026-10-23 SS: asked for a performance review. See `reports/2026-10-23_pp3074-google-ads-review.md`.
