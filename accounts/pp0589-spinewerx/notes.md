# PP0589 - SpineWerX

- **Google Ads ID:** 791-140-6240 (America/Toronto, CAD)
- **Meta ad account ID:** none in the inventory
- **WhatConverts profile:** 125343 (imports "Calls From Ad Extensions" and "Calls From Google Ads"; all call lengths are sent)
- **Website:** https://www.spinewerx.ca (ads land on /lindsay-chiropractor/)
- **Office:** 245 Kent St W, Lindsay ON (City of Kawartha Lakes); Dr. Phillip Croutch, in Lindsay since 1984. Services on the site: chiropractic, spinal decompression, Spinal Stenosis Boot Camp, ScoliBrace, orthotics, acupuncture, shockwave, weight loss. No massage or physio. Free consultation is the new-patient offer.
- **Access:** normal
- **Usually worked on by:** John
- **Salesforce:** review case 00206360 "Google Adwords Account Review". Budget CAD 750/month, billing date 5.

## Goals and preferences
- JW 2026-10-23: keep the daily budget as is for now and keep tabs on spend vs the CAD 750 budget in the review case.
- JW 2026-10-23: leave competitor searches alone if they converted.

## Setup (as of 2026-10-23)
- Live campaign "Perfect Patients" (Search, Maximize conversions, CAD 32.89/day, Mon-Wed 9-18, Thu 9-20; Lindsay city + 2/4/6/10 km radii, presence or interest; mobile +15%). Max Conversions works here (CPL about CAD 52), so bidding was left alone.
- Ad groups: "Chiropractor" (chiropractor broad/phrase/exact) and "Lindsay Chiropractor" (chiropractor lindsay / lindsay chiropractor phrase, chiropractor near me exact).
- Shared negatives: "Negative Search Terms" and "Stock Negative Keywords". Brand terms (spinewerx, croutch) excluded at campaign level on purpose.
- Paused: "Campaign #1", "Campaign #2", and the client's own Smart campaign "Chiropractic Therapy Treatment" (created by the client on 8 May 2026).

## Tracking
- Primary: WhatConverts call imports, "Appointment Request (New Patient)" (GA4), "Contact Us" (codeless). "Appointment Request (Current Patient)" secondary since 2026-10-23.
- The 4 Smart campaign conversion actions are still primary (the API can't change them; 0 conversions since April). Set them secondary in the UI when convenient.

## History and decisions
- 2026-07: account relaunched after a Google credit (bad spend) was processed.
- 2026-09-28 JW: negatives added; broad "chiropractor" drives most conversions.
- 2026-10-23 JW: review. 110 negatives added; removed "kawartha", "kent", "st" and "free" negatives (they blocked local / free-consultation searches); Current Patient secondary; RSA typo "Linsday" fixed (new RSA 829334816388, old 405611333965 paused). Budget left at CAD 32.89 by JW's choice although spend runs 15-50% over CAD 750. Calls show the clinic turning new patients away (no availability) while ads promise same-day appointments: open question. Log `logs/changes/2026-10-23_2007Z_JW_pp0589-review-fixes.md`.
