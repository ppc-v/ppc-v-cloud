# PP6744 - Gavric Chiropractic Clinic

- **Google Ads ID:** 969-838-9009 (America/Chicago, USD). Brand label: Perfect Patients
- **Meta ad account ID:** none in the inventory
- **WhatConverts profile:** 165760 (account 112852). Numbers: (414) 797-6621 "Google Ads Extension" (the call asset), (414) 775-3142 "All Traffic" (website number swap), (414) 742-7394 "Google Business Profile Ads Extension" (not a current Google Ads call asset).
- **GTM container / GA4 property:** GTM-NZ6BNM2N and GTM-PX3V6953 both on the site, neither shared with paidsearch@. No GA4 property visible to paidsearch@.
- **Website:** www.gavricchiropractic.com (Oak Creek, WI). Form fills only, no booking engine (2026-10-19).
- **Access:** normal
- **Usually worked on by:** Sara (Google label)

## Setup (as of 2026-10-21)
- One Search campaign, "Perfect Patients" (23712983933), first spend 2026-04-14. Maximize Conversions (no target), $60/day, ~$1,500/month cap via the monthly budget rule. Radii 1/2/4/6 mi, presence only. Mon–Fri 8:00–17:00.

## Tracking
- Primary: Calls From Ad Extensions (WhatConverts call import), Calls From Google Ads (WhatConverts click import), both count every call. Also primary: Appointment Request (New Patient) and Contact Us Submission (GA4 imports), silent since July. Appointment Request (Current Patient) is secondary.
- Site also has an **Aloha webchat (ReviewWave)** widget, added by the client (`cdn.reviewwave.com/js/chat_embed.js`, key 4b30f1fe76e484): visitors leave name, phone and message and get a text back. Not tracked anywhere today. It runs on the page (not an iframe) and shows `#rws-message-sent-view` after a successful send, so GTM can catch it once we have access. Send only the event, never the form fields.
- About half the ad calls are existing patients. The practice seems to use an AI receptionist that books on the call.
- The client may move to a third-party booking engine; options are in `reports/2026-10-21_pp6744-lifetime-review.md`.

## History and decisions
- 2026-04-27/28: account compromised. 98 unauthorised campaigns ("NHV-ADS-A79-…", "AKR-…") spent $1,304 on spam searches, then were removed. The account didn't serve until 2026-06-18. Whether Google credited the spend is unknown (raised with Sara 2026-10-21).
- 2026-10-21 SS: lifetime review (read-only). $7,311 on our campaign, 81 calls from ads, ~6 confirmed new-patient bookings on calls (6–9 counting the GBP number in Apr–Jul). CPC up from $6 to $16–22, 31–77% of searches lost to budget. See `reports/2026-10-21_pp6744-lifetime-review.md`.
