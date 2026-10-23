# PP1864 - DZ 1-Memorial Drive Chiropractic and Massage

- **Google Ads ID:** 474-357-1274 (CAD). Account timezone is America/Vancouver, but the practice is in Calgary (Mountain, 1 hour ahead). Ad schedule hours are in Pacific time.
- **Meta ad account ID:** none in the inventory
- **WhatConverts profile:** 142918 (account 95543). Phone names: "Google Ads" (website pool), "Google Ad Extensions" (call asset (587) 209-0007), "GBP Ad Extensions".
- **GTM container / GA4 property:** GTM-TMT4P3B (paidsearch@ has no GTM access yet, see `reports/2026-10-21_gtm-access-gaps.md`)
- **Website:** https://www.mycalgarychiropractor.ca (ads land on /chiropractor-calgary/)
- **Office:** 5271 Memorial Drive SE, Calgary AB; (403) 273-0203. Hours (per the booking test sheet): Mon 8:30-6:30, Tue 8:30-12:30, Wed 2-6:30, Thu 8:30-6:30, Fri 8:30-12, Sat 9-12. Wednesday-morning calls do get answered.
- **Access:** normal
- **Usually worked on by:** Sara

## Goals and preferences
- Salesforce Google budget: CAD 1,920/month (billing date 15). The monthly budget rule pauses the account at the cap.

## Setup (as of 2026-10-23)
- One Search campaign, "Perfect Patients" (22378360978): Maximize conversions, CAD 150/day, Mon/Wed/Thu 8:30-17:00 account time, radii 2/4/6/8/10 km around 5271 Memorial Dr SE (presence only), mobile +15%, desktop -15%.
- One live ad group, "Chiropractor Calgary", mostly broad match. "chiropractor calgary" broad and phrase are **paused**. One RSA (741530451102, Average, every headline pinned) with a $49 new-patient exam offer.
- Paused ad groups: Chiropractor, Branded, Massage, Chiropractor Near.

## Tracking
- **Since 2026-10-23, primary:** WhatConverts "Calls from Ad Extension" + "Calls from Google Ads", and **"Custom Form Appt Request" (GA4 `custom_form_appointment_request` = page view of /thank-you-appointment-request/: the correct form conversion, per SS)**. Secondary: Google's "Calls from ads" and "PPC Appt Request Form" (/thank-you-appointment-request-ad/, unused since Aug).
- The form is embedded from forms.vortala.com (embed 6938892). GA4 attributes many thank-you views to "forms.vortala.com / referral", so Google Ads sees almost none. Fix: add forms.vortala.com to GA4 unwanted referrals (UI only).
- GA4 property 327914033 (G-TKLTYM44SJ) is also linked to another Google Ads account, 7638907768.
- No consent banner found in the landing page HTML (Canada: consent rules likely apply). It may load via GTM, which isn't shared with paidsearch@.
- WhatConverts quotable scoring: someone scores calls about 2 weeks after they happen. Yes = a new patient who booked or a strong new-patient enquiry; No = existing patients, admin, short/missed calls, irrelevant callers.

## History and decisions
- 2026-04: account hacked. Two Vietnamese "SANI - WOLF Thái" campaigns spent about CAD 17, now removed. Didn't run in May.
- Sep 2026 spent CAD 1,983; Oct 2026 spent CAD 2,233 (CAD 313 over budget), paused by the rule on 15 Oct.
- 2026-10-23 SS: asked for a review and recommendations plus WhatConverts call scoring. See `reports/2026-10-23_pp1864-google-ads-review.md`.
- 2026-10-23 SS: WhatConverts scores set for 3 calls. Google Ads: budget CAD 150 → 85, "Calls from ads" secondary, Manual CPC (calgary/near me $20, chiropractor exact $18, others $16), broad keywords paused and phrase/exact added, 31 negatives, 10 km radius only. Log `logs/changes/2026-10-23_1137Z_SS_pp1864-review-fixes-and-wc-scores.md`. **Current offer: $49 new patient exam** (SS confirmed). Check pacing around 8 Nov. To do: 60s+ call rule in WhatConverts (SS), new RSA, GTM access + form audit.
- 2026-10-23 SS: "PPC Appt Request Form" set to secondary; new $49 RSA 829431185750 added (log `logs/changes/2026-10-23_1149Z_SS_pp1864-form-conversion-new-rsa.md`). SS to add the forms.vortala.com unwanted referral in GA4.
- 2026-10-23 SS: added forms.vortala.com as an unwanted referral in GA4 (UI; the API can't read the setting back). Oct data already shows no forms.vortala.com referral sessions. Check-in set for 2026-11-09 14:07 UTC (trigger trig_01NcUxc6Juvn5DLEi66Wc6aD): form conversion recording, referral gone, pacing, RSA comparison.
