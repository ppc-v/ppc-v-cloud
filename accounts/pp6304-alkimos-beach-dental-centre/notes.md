# PP6304 - Alkimos Beach Dental Centre

- **Google Ads ID:** 691-400-6772 (Australia/Perth, AUD)
- **Meta ad account ID:** none in the inventory
- **WhatConverts profile:** 147662 (calls imported as "Call from Google Ads" and "Calls from Ad Extensions")
- **GTM container / GA4 property:** GTM-MQ8ZQK6N / GA4 properties/437924569 (G-FVWPQJB5E7)
- **Website:** https://www.alkimosbeachdental.net.au (ads land on /alkimos-dentist/)
- **Office:** 8/15 Graceful Blvd, Alkimos WA 6038. Full-scope practice: general, same-day emergency, children's, cosmetic/whitening, Invisalign, implants, wisdom teeth and oral surgery, crowns/bridges, root canal, dentures (prosthodontist on staff), gum care. New patient special AUD 230 (was 199 until June 2026).
- **Access:** normal
- **Usually worked on by:** John
- **Salesforce:** review case 00815199 "Google Adwords Acct Review". Budget AUD 1,500/month (PPC Lite: runs at a full daily budget until the monthly limit, then the rule pauses it), billing date 15.

## Goals and preferences
- JW: "invisalign" is an intentional negative (expensive, research-based searches).
- JW 2026-10-23: be mindful of suburb negatives; suburbs near Alkimos inside the radius should not be blocked.
- JW 2026-10-23: next review, if there's no good movement, try Manual CPC.

## Setup (as of 2026-10-23)
- One campaign, "Smile Marketing" (Search, Maximize conversions, AUD 150/day, Mon-Fri 8-18, 10 km radius, presence only, mobile +15%). Ad groups "Dentist" (dentist exact; dentist near me exact/phrase/broad; broad "dentist" paused 2026-10-23) and "Dentist Alkimos" (dentist alkimos phrase/broad).
- Six shared negative lists (about 15,100 terms): Competitors 1-3, Stock Negatives, Aus Towns/Villages/Cities, Search Terms. The client's own name "alkimos beach dental" is in Competitors 3 (brand excluded).
- Suburbs unblocked 2026-10-23: Shorehaven, Eglinton, Jindalee, Butler, Brighton, Merriwa. Still blocked (edge of radius, own dentists): Yanchep, Quinns Rocks, Mindarie, Clarkson.

## Tracking
- Primary: WhatConverts call imports, Appointment Request New Patient, Contact Us Submission (GA4). Current Patient secondary since 2026-10-23.

## History and decisions
- 2026-04-28: account hacked ("CBH-GAU-..." campaigns, removed). The hackers' "hopbx" Purchase conversion action was removed 2026-10-23. Don't review removed breach campaigns.
- 2026-06-30 JW: new patient special 199 → 230; ads and landing page updated (the old $199 callout was missed until 2026-10-23).
- 2026-09-28 JW: paused high-spend keywords, opened broad/exact tests.
- 2026-10-01 JW: account suspended for "circumventing systems: cloaking"; appealed. It served 1-12 Oct. Landing page checked 2026-10-23: same page for users and Google's crawler, no redirects.
- 2026-10-23 JW: review. Paused broad "dentist" (AUD 938 for 2 conversions), removed hopbx, Current Patient secondary, $230 callout, 76 negatives added, "canal"/"surgery" and 6 nearby suburb negatives removed. Log `logs/changes/2026-10-23_2024Z_JW_pp6304-review-fixes.md`.
