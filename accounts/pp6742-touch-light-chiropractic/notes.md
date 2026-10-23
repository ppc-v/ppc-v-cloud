# PP6742 - Touch Light Chiropractic

- **Google Ads ID:** 288-398-9795 (US Eastern, USD)
- **Meta ad account ID:** none in the inventory
- **WhatConverts profile:** 171730 (phone names "Google Ads Extension" = call asset (704) 312-2331, "Google Ads" = website pool)
- **GTM container / GA4 property:** GTM-MBGVZFCG (not shared with paidsearch@); GA4 not visible to paidsearch@ either
- **Website:** https://www.touchlightchiro.com (ads land on /huntersville-chiropractor/)
- **Office:** 16405 Northcross Dr, Huntersville NC. Positioning: brain-based / nervous-system chiropractic, NetworkSpinal, Webster certified, $199 new patient special, Dr. Ginni Gross
- **Access:** normal
- **Usually worked on by:** Sara

## Goals and preferences
- Salesforce Google budget: USD 2,500/month (billing date 24). The monthly budget rule pauses the campaign at the cap and restarts it on the 1st.

## Setup (as of 2026-10-23)
- One Search campaign, "Perfect Patients" (24043812427), first spend Jul 2026. Maximize conversions; budget USD 90/day (SS lowered it from 144.25 on 16 Oct); schedule Mon 12-7pm, Tue 8am-3pm, Wed 8am-1pm, Thu 12-7pm; 8 mi radius around 16405 Northcross Dr, presence only; mobile +15%.
- Ad groups: Chiropractor, Chiropractor Huntersville, Chiropractor Near. Broad "chiropractor", "chiropractor huntersville" and "chiropractor near me" take about 89% of spend; QS 3-4. Three RSAs, every headline pinned.

## Tracking
- Primary: WhatConverts "Calls From Ad Extensions" and "Calls From Google Ads" (one per click), and GA4 "New Patient Book Now Page View" (a page view, many per click; **SS chose to keep it primary**, 2026-10-23). Google's own "Calls from ads" set to secondary 2026-10-23.
- Calls: about a third of ad calls never reach a person; most genuine new-patient callers reach voicemail ("off hours or assisting others") during ad hours. Raise with the client.

## History and decisions
- 2026-10-15: paused by the monthly budget rule at USD 2,512 (on a USD 144.25 budget, Max Conv spent about USD 290/day).
- 2026-10-23 SS: asked for a review. See `reports/2026-10-23_pp6742-google-ads-review.md`.
- 2026-10-23 SS: rescored 12 WhatConverts calls (8 quotable new-patient calls since late July). Google Ads: Manual CPC (Huntersville/near me $20, chiropractor exact $18, others $16), 6 broad keywords paused, "huntersville chiropractor" phrase added, 23 negatives, unpinned copies of the 3 RSAs, "Calls from ads" secondary; budget kept at $90. Log `logs/changes/2026-10-23_1209Z_SS_pp6742-review-fixes-and-wc-scores.md`. SS is getting GTM access. Check pacing about 8 Nov.
- 2026-10-23 SS: WhatConverts now sends only 45s+ calls to Google Ads (log `logs/changes/2026-10-23_1214Z_SS_pp6742-whatconverts-45s-calls.md`). SS is raising the missed-call / voicemail issue with the client.
