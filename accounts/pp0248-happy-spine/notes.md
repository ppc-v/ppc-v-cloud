# PP0248 - Happy Spine

- **Google Ads ID:** 170-705-2450 / 1707052450 (NZD), cancelled 2018. Meta only now.
- **Meta ad account ID:** 607986248191762 (Pacific/Auckland, bills in AUD). Pixel 1997515890557818. A third-party pixel 1852619532352403 is also on the site (added 14 Dec 2025).
- **WhatConverts profile:** none
- **GTM container / GA4 property:** GTM-MJFZ3QX (not shared with paidsearch@); no GA4 property visible.
- **Website:** happyspine.co.nz, Christchurch (164 Clarence St, Riccarton), 03 348 3536. Booking: happyspine1.apollo.practicehub.io (external, untracked).
- **Budgets (Salesforce):** Meta NZD 375/month, but the ad account is in AUD and spends about AUD 375. Confirm which is right.
- **Access:** normal
- **Usually worked on by:** John (manual owner in the inventory sheet; note there: "Working on new META Ad creative and tracking.")

## Goals and preferences
(Not recorded yet.) Offer: $199 new patient assessment with same-day adjustment, page /199-new-patient-assessment/.

## Tracking
- The "Meta Pixel Code ADDED BY PPC" snippet fires fbq('track','Lead') on every page load. Remove it before any lead-optimised campaign.
- The third-party pixel snippet sets fbq('consent','revoke'); consent is granted only when a visitor accepts all cookies. That gates our pixel too. Keep it (NZ privacy).
- Custom conversion "$199 NPS Page View" (OTHER) = page view of the offer page.

## History and decisions
- 2023: "Perfect Patients" instant-form campaign got 20 leads for AUD 701 (about AUD 35 each).
- 2026-04-17: "Perfect Patients - 2026 New" ad set "2026 New" launched, optimising LINK_CLICKS. AUD 1,941 to Oct with no leads; 72% of 90-day spend on Audience Network; weekly frequency 4–13.
- 2026-10-14 JW: conversion audit. Doc: https://claude.ai/code/artifact/c0f04199-360c-42cf-921f-5454a49bbe98. Recommended: new Leads campaign with an instant form, Audience Network excluded, new creative; remove the page-load Lead event. Nothing changed yet.
