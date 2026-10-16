# PP5368 - Triad Family Chiropractic

- **Google Ads ID:** 558-007-2284 (America/New_York, USD). Brand label: Perfect Patients
- **Meta ad account ID:** not checked yet
- **WhatConverts profile:** not checked yet (no WhatConverts script on the landing page)
- **GTM container / GA4 property:** GTM-T2ZW66 is on the site. The Google Ads tag AW-598318905 is also loaded directly on the landing page.
- **Access:** normal
- **Usually worked on by:** Sara (Google label)

## Goals and preferences
- **No number swapping (Sara, 2026-10-16):** the client doesn't want the phone numbers on the landing page to swap, so no Google forwarding numbers or WhatConverts number pools on the site. Track as much as possible without swapping.

## Tracking
- **Landing page:** https://www.triadfamilychiropractic.com/5-star-family-chiropractor-in-kernersville/. 6 tel: links, all to the practice number (336) 904-0752.
- **Primary goals:**
  - Appointment Request New Patient and Current Patient (GA4)
  - Contact Us Submission (GA4)
  - Calls from ads (practice number) (call asset)
  - Landing Page Phone Tap (7849561377), which needs the click listener on the page to fire. See `logs/changes/2026-10-16_1154Z_SS_pp5368-phone-tap-conversion.md`.
- **"Calls from Website" (7683627117):** older tap action, never fired, made secondary 2026-10-16.

## History and decisions
- 2026-10-16 SS: removed "LP Phone Tap" (7849571497) and created "Landing Page Phone Tap" (7849561377, send_to `AW-598318905/k2jVCKGa-54dELm-pp0C`). Waiting for the snippet to be added to the landing page.
