# PP4094 - Palmetto Smiles of Charleston

- **Google Ads ID:** 505-760-9128 (US Eastern, USD). Brand label: Smile Marketing
- **Meta ad account ID:** 320969308719059 (paused by Sara 4 Aug 2026; Salesforce Meta budget $900)
- **WhatConverts profile:** 125372 (account 83256). (843) 256-3614 = Google Ads call asset (since Aug 2026); (843) 256-3615 "Google My Business Ads" = Business Profile number, also used in Maps ads (was the main ad-call number before the breach); 256-3026 / 256-3031 / 256-2996 = website number pool.
- **GTM container / GA4 property:** GTM-P4VKDWZ ("added by SEO"), not shared with paidsearch@. No GA4 property visible. Access requested from the SEO team (Sara, by 2026-10-23); waiting.
- **Website:** www.palmettosmilesofcharleston.com, 3188 W Montague Ave, North Charleston SC. Hours: Mon & Wed 7:30–4:30, Tue & Thu 7:30–2:30, Fri by appointment. Contact: Amy.
- **Salesforce:** $2,500/month Google budget, billing day 24.
- **Access:** normal
- **Usually worked on by:** Sara (Google label)

## Setup (as of 2026-10-22)
- One Search campaign, "Smile Marketing" (338034390), manual CPC, $144.25/day, Mon & Wed 7:30–16:30, Tue & Thu 7:30–14:30 (since 2026-10-22; was Mon–Thu 6:00–16:15). 3 and 5 mile radius. Mobile +15%, desktop/tablet −30%. Live ad groups: General Dentistry, Charleston Dentist, Emergency Dental, Dentist Near; Holistic, Mercury Removal, Sedation, Invisalign, Children's, insurance groups paused.
- Offers: $189 new patient special; Dental Wellness Plan $348/year (page /dental-wellness-plan/), not yet advertised.

## Tracking
- Primary: Calls from Ad Extensions (WhatConverts call import) and Calls from Google Ads (WhatConverts click import), both counting one per click since 2026-10-22; GA4 imports Appointment Request (New Patient), Online Appointment Request Submission, Contact Us Submission. Appointment Request (Current Patient) is secondary since 2026-10-22.
- Site has an opt-in cookie banner: GA4 loads only after "Accept", so GA4 form conversions undercount. Calls unaffected.
- Before the breach Google's own "Calls From Ads" action was also primary, double counting calls (now gone).

## History and decisions
- 2026-04-28: account compromised; 15 unauthorised campaigns spent ≈$230. Account didn't serve May–June, restarted July. Call asset rebuilt with (843) 256-3614 in Aug.
- 2026-10-22 SS: account review for Amy's concerns (read-only). Calls from ads −63% and Maps ad clicks −56% (Jan–Mar vs Jul–Sep 2026) at the same spend and clicks; main converting phrase keywords now carry little spend, broad "dentist" takes 40% of budget. Organic rankings also down (SEO, not the breach). Recommended: restore phrase keywords, cut broad, office-hours schedule, Dental Wellness Plan test campaign (~$500/mo), holistic ad group test, Consent Mode + per-page forms. See `reports/2026-10-22_pp4094-account-review.md`.
- 2026-10-22 SS: applied review fixes:
  - Keywords: "dentist" phrase enabled at $19; "dentist" broad paused; "dentist charleston" phrase $10 → $20.
  - Added 14 phrase negatives to "Negative Search Terms".
  - Ad schedule moved to office hours: Mon/Wed 7:30–16:30, Tue/Thu 7:30–14:30.
  - Emergency ad typo fixed; 4 new RSAs added, with the old ones kept live.
  - Call actions count one per click; Current Patient appointment is now secondary.
  - See `logs/changes/2026-10-22_1628Z_SS_pp4094-review-fixes.md`.
  - Next: Wellness Plan campaign and holistic test once Amy approves; review results around 2026-11-05.
- Ad copy rule: Google rejects phone numbers in ad text (PHONE_NUMBER_IN_AD_TEXT); use the call asset instead.
