# PP5449 - Midwest Sport & Spine

- **Google Ads ID:** 756-376-8919 (America/New_York, USD)
- **Meta ad account ID:** none in the inventory
- **WhatConverts profile:** yes (call uploads "Calls from Google Ads" / "Calls from Ad Extensions")
- **GTM container / GA4 property:** GA4 "PP5449 - Midwest Sport and Spine-GA4 (web)"
- **Access:** normal
- **Usually worked on by:** Sara (Google label)
- **Salesforce budget:** USD 5,000/month, on-going, billing day 27. The Bulk Actions monthly budget rule pauses both campaigns when the cap is hit.

## Account setup
- Two Search campaigns, one per location: Noblesville (220 Lakeview Dr, 8-mile radius, call (317) 296-8308) and Greenwood (33 E County Line Rd, 8-mile radius, call (317) 279-5966).
- Manual CPC. Ad schedule: Noblesville Mon–Thu 7–18, Fri 8–13; Greenwood Mon–Thu 8–17 (Wed from 6), no Friday.
- Offer in ads: $49 new patient special (chiro); the physical therapy ads say $20. Confirm the current offer before writing copy.

## Tracking
- Primary conversions: Calls from Website, Calls from ads (Google call tracking), Calls from Google Ads + Calls from Ad Extensions (WhatConverts uploads), Appointment Request Submission (GA4). Google and WhatConverts call actions are both primary, so calls may be double counted (flagged 2026-10-16, not yet resolved).
- Hidden legacy UA goal "Contact Us Page view (All Web Site Data)" is still set as primary (inventory WEAK_GOALS flag).
- Call assets (317) 296-8308 and (317) 279-5966 are also WhatConverts tracking numbers. Their call conversion reporting is DISABLED (Google "Calls from ads" last counted 14 Sep).
- WhatConverts uploads every call, including 5–7 second hang-ups (e.g. 16 Sep: 4 uploaded, 2 of them 5 s). Google's own call tracking only counts calls that pass its duration threshold.
- No access: GTM-P6CX8J5 isn't shared with paidsearch@, and no GA4 property is visible. Ask for GTM Publish and GA4 Editor.
- Website offer: $49 new patient special, "not valid for Medicare, Medicaid, state or federal insurance plans, or auto/PI". So Medicaid searches aren't necessarily wrong; left running.

## History and decisions
- 2026-04-27/28: account was hijacked. 44 fraudulent Search campaigns ("Mec-…", "MEC-…") were created and spent about USD 5,400 before being removed. All are now removed.
- 2026-09-23/24: monthly budget rule paused both campaigns until 1 Oct (cap reached early).
- 2026-10-16 SS: performance review requested (leads -62%, CPL +151% flag). Recommendations given; nothing changed yet.
- 2026-10-16 SS: applied budgets $388 → $215/day (paced to the $5,000 cap), search partners off, lower broad bids, new Greenwood keywords, 15 phrase negatives per campaign. See logs/changes/2026-10-16_1432Z_SS_pp5449-budgets-partners-keywords-negatives.md.
- 2026-10-16 SS tracking audit: verdict "calls double counted". Every Google-tracked call from Jul to Sep also came in as a WhatConverts upload on the same day: about 13 duplicates in 90 days, none since 21 Sep. WhatConverts saw 73 google/cpc calls in 90 days (about 30 tagged new patient, 11 existing). Fix (primary/secondary and counting) previewed, waiting on SS.
