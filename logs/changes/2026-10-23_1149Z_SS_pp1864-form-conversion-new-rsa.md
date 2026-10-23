# PP1864 Google Ads: single form conversion + new $49 RSA

- **When:** 2026-10-23 11:49 UTC (07:49 US Eastern for Sara; 05:49 Calgary)
- **Requested by:** SS
- **Approved by:** SS, "approve" on the preview in chat
- **Platform:** Google Ads
- **Session:** https://claude.ai/code/session_01EiVWQEthbRXB2zN1t6GazV

## Changes
PP1864 (474-357-1274), campaign "Perfect Patients" (22378360978), ad group "Chiropractor Calgary" (183813770344).

| Entity | Field | Before | After | Result |
|---|---|---|---|---|
| Conversion action "PPC Appt Request Form" (7530250936; GA4 `PPC_Appt_Request` = /thank-you-appointment-request-ad/, no hits since Aug) | Primary | Primary | Secondary | ✅ read back |
| Conversion action "Custom Form Appt Request" (7085978622; GA4 `custom_form_appointment_request` = /thank-you-appointment-request/) | - | Primary | Primary (unchanged): now the only primary form conversion, per SS | - |
| New RSA 829431185750 | Created | - | Enabled, 15 unpinned headlines, 4 descriptions ($49 new patient exam), path chiropractor/calgary, same final URL as RSA 741530451102 (unchanged) | ✅ in review |

Primary conversions now: Custom Form Appt Request + WhatConverts "Calls from Ad Extension" and "Calls from Google Ads". Secondary: "Calls from ads", "PPC Appt Request Form".

## Failed or skipped
- GA4 unwanted referral for `forms.vortala.com` (needed so ad-driven form fills keep google / cpc credit). It can't be set through the API; SS to do it in GA4 Admin → Data streams → Website-PP1864 → Configure tag settings → List unwanted referrals.

## Notes
- GA4 records about 20 `custom_form_appointment_request` events a month, about a third attributed to "forms.vortala.com / referral" (the embedded form, forms.vortala.com/embed/6938892.js). Google Ads recorded 0 in 120 days.
- After the GA4 fix, check in mid-November that "Custom Form Appt Request" starts recording in Google Ads.
