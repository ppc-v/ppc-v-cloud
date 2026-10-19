# PP0117 - Funnell Chiropractic

- **Google Ads ID:** 470-953-8470 (Australia/Perth, AUD). Brand label: Perfect Patients
- **Meta ad account ID:** none in the inventory
- **WhatConverts profile:** 125335 (account 83219). Tracking numbers seen on google/cpc calls: +61 8 6830 1982 (website swap, with GCLID) and +61 8 6830 1993 (the call asset, no GCLID).
- **GTM container / GA4 property:** GTM-NC3TPB5 on the site, not shared with paidsearch@. GA4 property 258186108 (G-13X5BRXDZT), linked to the Ads account. Google Ads tag AW-1046081343.
- **Online booking:** eVisit scheduler in an iframe on /book-online/ (evisit.com.au, clinic cis0068). Completed bookings aren't tracked.
- **Access:** normal
- **Usually worked on by:** Sara (Google label)

## Setup (after the 2026-10-19 changes)
- One active Search campaign, "Perfect Patients" (395701357): Maximize Clicks with max CPC AUD 12, AUD 23/day, Search Partners and Display off, location presence only.
- Locations: five WA postcodes (6167–6172, Rockingham area).
- Ad schedule (Perth time, matches clinic hours): Mon/Wed/Fri 8:30–11:00 and 13:00–17:30, Tue/Thu 8:00–12:30, Sat 8:00–11:00.
- One enabled ad group, "Rockingham Chiropractor", with two RSAs: the old fully pinned one (Average) and an unpinned one added 2026-10-19. Final URL: /chiropractor-rockingham/ with utm_source=v_adwords.
- Enabled keywords: chiropractor, back pain chiropractor, chiropractor near me, chiropractor rockingham [exact]; phrase: chiropractor rockingham, rockingham chiropractor, chiro rockingham, chiropractic rockingham, chiropractor near rockingham, chiro near me, chiropractic near me. No broad match: broad "back pain chiropractor" (AUD 279 in 30 days, mostly condition searches) and broad "chiropractor rockingham" are paused.

## Tracking
- Calls are tracked through WhatConverts only. Google's own call conversion actions are deliberately not used, to avoid double counting (Sara, 2026-10-19), so Google's own call action is secondary only. From 2026-10-19 the call asset reports to the secondary action "Google call extension calls (observe only)" (7857040504), which keeps Google forwarding numbers on so the WhatConverts call import can match.
- Primary goals: Calls From Google Ads (WhatConverts click import, working, count one), Calls From Ad Extensions (WhatConverts call import, count one: had never received an upload before the 2026-10-19 fix), Reached Online Booking Page (GA4, which is just a page view of /book-online/, counts every).
- GA4 key event contact_submissions (form) isn't imported into Google Ads.
- Dead GA4 key events: purchase, appointments__new_patient_, appointments__current_patient_or_returni, ga4_google_ads_appointment_request_submi.

## History and decisions
- 2026-10-19 SS asked for an account and tracking review because October had only 1 lead. Verdict: tracking for calls is working (WhatConverts and Google Ads agree: 2 paid calls since 30 Sep, the last on 2 Oct). The lead drop is real and comes from low volume (19 clicks Oct 1–19 at about AUD 20 CPC) and wasted spend on condition searches. September's 8.8 "conversions" were 1 call plus 7.8 booking-page views. No changes made yet; recommendations given to Sara.
- 2026-10-19 SS: switched to Maximize Clicks (max CPC AUD 12, budget unchanged at AUD 23/day), presence only, paused broad "chiropractor rockingham" and enabled phrase variants plus "chiro near me" / "chiropractic near me", added 47 negatives, extended the ad schedule to the clinic's hours (including Sat 8–11), added an unpinned RSA (828510025650), set both call actions to count "one", made "Calls From Ad Extensions" secondary and created "Calls from ads (call extension, 60s+)" (7856876390) on the call asset, and changed the callout to "Over 45 Years Experience". See `logs/changes/2026-10-19_1643Z_SS_pp0117-october-review-fixes.md`. Review around 2026-11-02.
- Still open: "Reached Online Booking Page" stays primary until the team decides how to track bookings (Sara: "we need to figure out tracking first"). Its counting is still "every" because the API can't change it. The contact form (GA4 contact_submissions) still needs importing in the UI. GTM access is still needed.
- 2026-10-19 SS: reverted the Google call tracking added earlier today. The call asset's reporting is disabled again, "Calls from ads (call extension, 60s+)" (7856876390) is removed, and "Calls From Ad Extensions" is primary again. See `logs/changes/2026-10-19_1653Z_SS_pp0117-revert-google-call-tracking.md`.
- 2026-10-19 SS asked why Calls From Ad Extensions records nothing. Findings: over the last 12 months WhatConverts logged 19 google/cpc calls on the call-extension number (08) 6830 1993, against 18 on the website number. Google Ads recorded 0 phone calls and has no call records (call_view) for the whole period, despite about 4,800 phone impressions. Google's upload summary has no uploads at all for Calls From Ad Extensions. So Google forwarding numbers aren't being used on the call asset, and WhatConverts' caller-ID import has nothing to match against. About half of paid calls have been invisible to Google Ads. No changes made yet; options given to Sara.
- 2026-10-19 SS: created the secondary "Google call extension calls (observe only)" (7857040504) and pointed the call asset's call conversion reporting at it, so calls go through a Google forwarding number again. See `logs/changes/2026-10-19_1701Z_SS_pp0117-call-extension-forwarding.md`. Check on 2026-10-27: Google call records, and uploads to Calls From Ad Extensions. If uploads are still missing, check the WhatConverts Google Ads integration.
