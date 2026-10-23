# PP6285 - Lifestyle Chiropractic & Wellness

- **Google Ads ID:** 889-106-4862 (America/Denver, USD). Brand label: Perfect Patients
- **Meta ad account ID:** none in the inventory
- **WhatConverts profile:** 128417 (account 85838). Tracking numbers seen on google/cpc calls: +1 651-448-2853 (with GCLID), +1 651-448-2894 (the call asset, no GCLID), +1 651-448-2907 (no GCLID).
- **GTM container / GA4 property:** GTM-TMMG5BN8 on the site. Vortala owns it, but it isn't shared with paidsearch@ yet; Sara is getting access (2026-10-23). Vortala also manages GA4. GA4 G-6SMSLQ3FYK, Google Ads tag AW-16627031643, Meta pixel 2530064823884699 on the landing page.
- **Access:** normal
- **Usually worked on by:** Sara (Google label)
- **Salesforce:** $2,500/month Google budget, billing day 4.

## Setup (as of 2026-10-19)
- One live Search campaign, "Perfect Patients" (21416541072): manual CPC, $150/day, Search Partners and Display off. Location: 5 mi radius around 750 S Plaza Dr, Mendota Heights MN 55120, **presence or interest**, plus about 350 excluded countries/regions.
- Ad schedule: Mon & Wed 8–17, Tue & Thu 14–18, Fri 8–12 (no weekends). Mobile +30%.
- One live ad group, "Mendota Heights Chiropractor": broad + exact "chiropractor" (QS 2, bid $22), exact "mendota heights chiropractor" (QS 7), phrase/exact "back pain chiropractor". One RSA (704213498545, Average strength).
- "Massage Therapy" campaign ($40/day) is paused, and so are the Chiropractor, Massage and Chiropractor Near ad groups.
- Shared negative lists: Competitor (69), Stock (175), Search Queries (2,037), plus 1,113 campaign negatives.
- Landing page: https://www.lifestylechiromn.com/chiropractor-mendota-heights/ ($99 new patient special).
- The monthly budget rule pauses the campaign at the cap and restarts it on the 1st.

## Tracking
- Primary goals: Book Online Page View (GA4 page view, not a lead), Call from Google Ads (WhatConverts click import), Calls from Ad Extensions (WhatConverts call import), Calls from ads (Google call asset AD_CALL). All three call actions count "every".
- Calls from ads and Calls from Ad Extensions both recorded the same calls on 2 and 5 Oct 2026 (double counting).
- Call asset (651) 448-2894 has call conversion reporting disabled. Most paid calls arrive without a GCLID.
- No form or booking confirmation is tracked as a lead.
- Online booking is the **Aloha (ReviewWave) New Patient Scheduler** on /book-online/ (embed 23362a1b…). It's built into the page, not an iframe, and fires `RWEmbedJS.appt_scheduled` when `window._rw_sched_config` is defined. The landing page's three "BOOK AN APPOINTMENT »" buttons go to /book-online/. The header button goes to /contact-us/. Existing patients book at theschedulingapp.com (don't track it). Plan and client access request: `reports/2026-10-23_pp6285-aloha-booking-tracking-plan.md` (2026-10-23 SS, not built yet).

## History and decisions
- 2026-04: the account was compromised. Five campaigns (DR-JR-SHA, DR-JR-Murong, DR-JR-VAN, DR-E300-ADAM-LD-Meme, DR-E300-ADAM-LD-Meme #2) ran Indonesian gambling ads and fake Mexican passport ads and spent about $2,660 in April. They are now removed, though their ad groups and ads remain under the removed campaigns. This is the same pattern and month as PP5372. No record here of how it was handled (credit, access review).
- 2026-10-19 SS: applied the review fixes. Location set to presence only. Broad "chiropractor" paused; phrase "chiropractor" and exact "chiropractor near me" added ($22); phrase "mendota heights chiropractor" re-enabled. 89 campaign negatives added. Daily budget $150 → $29 so October's $2,500 lasts to Oct 30. Business name "Lifestyle Chiropractic" re-linked, but Google shows the asset as disapproved (check the reason in the UI). Duplicate sitelinks removed. New RSA 828570674638 is live. Sara pre-approved $119/day for November; a check-in is set for 2026-11-01 (trigger trig_01HLfUCtniXo79tjZKpwsTz3). See `logs/changes/2026-10-19_2118Z_SS_pp6285-review-fixes.md`. Check results around 2026-11-02. Not done yet: conversion goal cleanup (item 3).
- 2026-10-19 SS: performance review, no changes made. Real paid leads per WhatConverts: Aug 6, Sep 4, Oct 4 calls (about $420–$625 per lead). Findings: broad "chiropractor" takes 87% of spend and matches conditions, orthopedics, PT, competitors and Spanish searches; about 59% of last-30-day spend came from people outside the targeted radius (presence or interest; Minneapolis alone was $627); 43% of searches were lost to budget and the $2,500 cap will be hit around 21 Oct; Book Online Page View and duplicated call actions inflate conversions; landing page experience is Below average on every keyword.
