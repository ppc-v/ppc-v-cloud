# PP5372 - Mason Spine & Injury Center

- **Google Ads ID:** 796-011-4833 (America/New_York, USD). Brand label: Perfect Patients
- **Meta ad account ID:** none in the inventory
- **WhatConverts profile:** 125411 (account 83295). Tracking numbers seen on google/cpc calls: +1 513-298-6490 (with GCLID) and +1 513-342-8947 (the call asset, no GCLID).
- **GTM container / GA4 property:** GTM-58N3NPS on the site, not shared with paidsearch@. Google Ads tag AW-473513114 on the landing page. No GA4 property visible to paidsearch@.
- **Access:** normal
- **Usually worked on by:** Sara (Google label)

## Setup (as of 2026-10-19)
- One Search campaign, "Perfect Patients" (11773819584): manual CPC, $87/day, Mon–Thu 9:00–18:00 only, mobile +15%, desktop/tablet -50%, Search Partners on.
- Location: 2 mi and 5 mi radius around 969 Reading Rd, Mason OH 45040, set to "presence or interest", plus 372 excluded locations.
- An automated rule pauses the campaign when the monthly budget is reached and restarts it on the 1st (paused 28 Sep, restarted 1 Oct 2026).
- Landing page: https://www.masonsaic.com/chiropractor-mason-oh/

## Tracking
- Primary goals: Calls from Google Ads (WhatConverts click import), Calls from Ad Extensions (WhatConverts call import), Submitted Appointment Request (GA4). Both call actions count "every", not "one".
- Call asset (513) 342-8947 has Google call conversion reporting disabled; about half of paid calls arrive without a GCLID.

## History and decisions
- 2026-04: about 30 unfamiliar campaigns ("Mec-Oishi…", "Mec-Volvo-Zelo…", "MEC-camry…") spent about $1,078 in April and are now removed. Looks like an account compromise; no record here of how it was handled.
- 2026-09-23 SS: removed the "Mason Spine & Injury" business name asset and created "Mason Spine&Injury Center"; set the broad "chiropractor near me" bid to $25.80. As of 2026-10-19 no business name asset is linked to the campaign.
- 2026-10-19 SS asked for a performance review because October was slow. Findings: leads 14 in Sep → 2 in Oct 1–19 (WhatConverts agrees: last paid call 7 Oct), CTR 3.0% → 1.8%. Main causes: the broad "chiropractor near me" keyword matching condition and medication searches (87% of October spend), a call-only ad taking about 28% of impressions with almost no clicks, no business name on the ads, Poor ad strength on the main ad. No changes made yet.
- 2026-10-19 SS: paused the broad "chiropractor near me" keyword and the call-only ad, linked the "Mason Spine&Injury Center" business name, re-enabled two "Good" RSAs (612949126771, 612948941659), set location to presence only, turned Search Partners off. See `logs/changes/2026-10-19_1150Z_SS_pp5372-october-review-fixes.md`. Still to do: negatives, radius, ad schedule. Check results around 2026-11-02.
- Business names are limited to 25 characters, so "Mason Spine & Injury Center" doesn't fit. "Mason Spine&Injury Center" is used.
