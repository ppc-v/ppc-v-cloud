# PP6788 - Resolve Chiropractic and Wellness

- **Google Ads ID:** 238-150-2203 (one Search campaign "Perfect Patients", Max Conversions, $85/day, launched 2026-09-09)
- **Meta ad account ID:** none in the inventory
- **WhatConverts profile:** PP6788 - Resolve Chiropractic and Wellness
- **GTM container / GA4 property:** not checked yet
- **Access:** normal
- **Ad schedule:** Mon–Fri 8am–6pm (account time). Weekends are dark by design.
- **Usually worked on by:** Sara (owner). John has also made changes.
- Location: Celina, TX area. 5 proximity radii (1–8 mi). Timezone America/Chicago, USD.

## Goals and preferences
- Offer: $37 New Patient Special. Offers shockwave; no SoftWave or laser. No Spanish-speaking service, so Spanish searches are blocked (SS, 2026-10-16). Same-day and walk-in appointments, insurance accepted.
- Reporting: the 30-day review is internal. Sara writes the DMS update herself. No client email drafts needed.

## Tracking
- Primary conversions: WhatConverts call imports ("Calls From Ad Extensions", "Calls From Google Ads"), GA4 forms (New Patient appt, Current Patient appt, Contact Us).
- From 2026-10-16, WhatConverts sends only calls of 30s+ to Google Ads (set by SS). Existing-patient calls still count. The Current Patient form is secondary, and the New Patient form counts one per click.
- Only 8 of 29 google/cpc WhatConverts calls carry a GCLID (normal for call-extension calls).

## History and decisions
- 2026-09-29 SS: brand negatives added (resolve, dr, Mistry, practice name).
- 2026-10-14 SS: sitelinks, callouts, structured snippet and image assets added.
- 2026-10-16 SS: first 30-day review (review-2026-10-16.md). ~22% of spend went to competitor and PT/ortho searches; 38% of ad calls went unanswered.
- 2026-10-16 SS: 172 phrase negatives added to the Competitor and Search Queries shared lists, "chiropractor" broad paused, Current Patient form set to secondary (log: logs/changes/2026-10-16_1616Z_SS_pp6788-negatives-goals.md). New Patient form counting could not be set through the API; SS changed it to One per click herself (confirmed). 
- 2026-10-16 SS: blocked McKinney and Frisco (over 12 mi from the practice; SS's geo rule for this account), plus softwave and laser. Asked WhatConverts to send only 30s+ calls to Google Ads; this has to be set in the WhatConverts UI.
- 2026-10-16 SS: 16 Spanish-language phrase negatives added to the Search Queries list.
- 2026-10-16 SS: WhatConverts call import limited to 30s+ calls. Conversion counts from this date aren't comparable to the first 30 days.
- 2026-10-23 one-week check (19–22 Oct): $359, 5 conversions ($72 CPL, now counting 30s+ calls only), impression share 47% (was 39%), budget-lost share down to 11% (was 30%). The 7s call wasn't imported, so the 30s filter looks to be working. 24 new negatives proposed (not applied).
