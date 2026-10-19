# PP0117 - Funnell Chiropractic

- **Google Ads ID:** 470-953-8470 (Australia/Perth, AUD). Brand label: Perfect Patients
- **Meta ad account ID:** none in the inventory
- **WhatConverts profile:** 125335 (account 83219). Tracking numbers seen on google/cpc calls: +61 8 6830 1982 (website swap, with GCLID) and +61 8 6830 1993 (the call asset, no GCLID).
- **GTM container / GA4 property:** GTM-NC3TPB5 on the site, not shared with paidsearch@. GA4 property 258186108 (G-13X5BRXDZT), linked to the Ads account. Google Ads tag AW-1046081343.
- **Online booking:** eVisit scheduler in an iframe on /book-online/ (evisit.com.au, clinic cis0068). Completed bookings aren't tracked.
- **Access:** normal
- **Usually worked on by:** Sara (Google label)

## Setup (as of 2026-10-19)
- One active Search campaign, "Perfect Patients" (395701357): Maximize Conversions with no CPC cap, AUD 23/day, Search Partners and Display off, location "presence or interest".
- Locations: five WA postcodes (6167–6172, Rockingham area).
- Ad schedule: Mon–Fri 8:00–11:00, plus Mon/Wed/Fri 13:00–17:00. No Tue/Thu afternoons or weekends.
- One enabled ad group, "Rockingham Chiropractor", with one RSA (ad strength Average). Final URL: /chiropractor-rockingham/ with utm_source=v_adwords.
- Enabled keywords: chiropractor [exact], back pain chiropractor [exact], chiropractor rockingham (broad + exact), chiropractor near me [exact]. Broad "back pain chiropractor" is paused (it spent AUD 279 in the 30 days to 19 Oct, mostly on condition searches).

## Tracking
- Primary goals: Calls From Google Ads (WhatConverts click import, working), Calls From Ad Extensions (WhatConverts call import, 0 in 90 days), Reached Online Booking Page (GA4, which is just a page view of /book-online/). All three count "every".
- GA4 key event contact_submissions (form) isn't imported into Google Ads.
- Call asset (08) 6830 1993 has Google call conversion reporting disabled.
- Dead GA4 key events: purchase, appointments__new_patient_, appointments__current_patient_or_returni, ga4_google_ads_appointment_request_submi.

## History and decisions
- 2026-10-19 SS asked for an account and tracking review because October had only 1 lead. Verdict: tracking for calls is working (WhatConverts and Google Ads agree: 2 paid calls since 30 Sep, the last on 2 Oct). The lead drop is real and comes from low volume (19 clicks Oct 1–19 at about AUD 20 CPC) and wasted spend on condition searches. September's 8.8 "conversions" were 1 call plus 7.8 booking-page views. No changes made yet; recommendations given to Sara.
