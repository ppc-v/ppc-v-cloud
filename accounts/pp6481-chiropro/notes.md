# PP6481 - ChiroPro

- **Google Ads ID:** 143-377-9401 (America/Chicago, USD). Brand label: Perfect Patients
- **Meta ad account ID:** not checked yet
- **WhatConverts profile:** not checked yet
- **GTM container / GA4 property:** GA4 conversion actions imported (Book Appointment Page Views, Custom Form Submission)
- **Access:** normal
- **Usually worked on by:** Sara (Google label; changes made as sara.stuka@vortala.com)
- **Salesforce:** Google Ads budget USD 7,200/month, billing date 27

## Goals and preferences
- Services (Sara, 2026-10-15): offers shockwave therapy, so don't block it; does **not** offer softwave therapy (`softwave` and `soft wave` are negatives). Neuropathy, spinal decompression and scoliosis not confirmed yet.

## Structure (as of 2026-10-15)
- One live campaign, "Perfect Patients" (Search, manual CPC, USD 405/day, Mon–Fri business hours, Search Partners on). Five 8-mile radii: St Charles/Cottleville MO, Troy IL, Highland IL, Shiloh IL, Columbia IL.
- Seven older per-office campaigns are paused (Shiloh, Troy, Columbia, Highland, Lake St Louis, Eureka, St Charles).
- The "Chiropractor" and "Chiropractor Near Me" ad groups (about 80% of spend) send every click to /st-charles-chiropractor/, including the Illinois searchers.
- Shared negative lists: Stock (137), Competitors (30), St Charles (27), Account Level (2,177).

## Tracking
- Primary goals: Calls from Google Ads (click import), Calls from Ad Extensions (call upload), Calls from ads, Custom Form Submission (GA4), Book Appointment Page Views (GA4, weak goal per the inventory sheet). "Contact ... Pageview" actions also counted 6 conversions between 17 Aug and 14 Oct.

## History and decisions
- 2026-04-27/28: account hijacked. 12 spam Search campaigns ("SANI-...", "Roy-..."; URLs such as juno-pack.com, pakar-seo.com, bluevillasmallorca.com, typeform) spent about USD 1,072. All are removed, but their ad groups and ads remain. The same April window as the PP5416 hijack.
- 2026-09-21 SS: campaign renamed, ECPC toggled, keyword bids raised, the five radius targets replaced, ad schedule edited, keywords added. 2026-10-01 SS: one keyword status change and one campaign negative ("cigna").
- 2026-10-15 SS: performance review (CPL_UP flag). Over 17 Aug–14 Oct: USD 14.3k for 39 conversions, about 30 of them real leads. Broad "chiropractor" cost USD 5.9k for 8 conversions; broad "chiropractic adjustment near me" cost USD 2.0k for 0. Broad match is pulling in symptom, product and competitor searches at about USD 35 a click. Missouri suburbs outside St Charles (Cottleville, St Peters, St Louis and others) cost about USD 5.2k for 4 conversions. Pacing: about USD 10.4k projected against the USD 7.2k budget, running out around 22 Oct. Recommendations given; nothing changed yet.
- 2026-10-15 SS: applied (log `logs/changes/2026-10-15_1908Z_SS_pp6481-budget-keywords-negatives.md`). Daily budget cut from USD 405 to USD 150. Broad `chiropractor` and broad `chiropractic adjustment near me` paused. 56 phrase negatives added to Account Level Negative Keywords. Mobile and desktop bid adjustments reset to 0%. Book Appointment Page Views made secondary. Still open:
  - Check "oak street health" conversions in WhatConverts.
  - Confirm which services the client offers (neuropathy, decompression, scoliosis). Softwave and shockwave answered 2026-10-15.
  - Check the Search Partners setting.
  - Split the campaign by office with matching landing pages.
  - Recheck pacing around 22 Oct.
