# PP5347 - Community Chiropractic Center

- **Google Ads ID:** 444-653-5801 (US Eastern, USD)
- **Meta ad account ID:** none in the inventory
- **WhatConverts profile:** 125409 (calls imported as "Calls from Google Ads" and "Calls from Ad Extensions")
- **Website:** https://www.communitychirosc.com (ads land on /chiropractor-greer-sc/)
- **Office:** 812 N Main St, Greer SC; Dr. Joel Cox. Services on the site: general chiropractic, pregnancy/prenatal (Webster technique), pediatric (newborns up), auto accident care, athletes. No massage or decompression listed.
- **Access:** normal
- **Usually worked on by:** John
- **Salesforce:** review case 00553316 "Google Adwords Account Review" (on the Account, not the Paid Advertising Project). Budget USD 1,000/month ("PPC Lite"), billing date 20, management fee USD 250/month.

## Goals and preferences
- Calls are the lead. The landing page's booking button was removed in Dec 2025, so the GA4 form goals record nothing.
- Prenatal/pregnancy and pediatric searches are wanted (JW 2026-10-23); don't add them as negatives.

## Setup (as of 2026-10-23)
- One live campaign, "Perfect Patients" (Search, **Manual CPC since 2026-10-23**, **USD 65/day**; Mon/Tue 6am-6pm, Thu 6am-5pm; 5 mi (+10%) and 8 mi radius around 812 N Main St, presence only; mobile +15%, desktop -35%, tablet -25%).
- Keyword max CPCs: chiropractor greer (phrase) $15, chiropractor near me (exact) $15, chiropractor near me (phrase/broad) $12, chiropractor (exact/phrase) $12. "chiropractor greer" broad and "chiropractor" broad are paused (too expensive, no conversions).
- Shared negative lists: Competitors, Stock Negatives (every state except SC), Search Queries. Brand terms (community chiropractic, dr, joel) are excluded on purpose.

## Tracking
- Primary: WhatConverts imports "Calls from Google Ads" (6812221097) and "Calls from Ad Extensions" (6812220392). Google's own "Calls from ads" is **secondary since 2026-10-23** (it double counted). Two older WhatConverts actions with the same names but different capitalisation (6810529106, 6810600600) record nothing.

## History and decisions
- 2026-04: account hacked; about 15 removed "TT - ..." campaigns of gambling keywords. USD 1,354.92 bad spend was credited by Google (case 00907625, Oct 2026); USD 1,192 credit left on the account.
- 2026-07: relaunched after billing was updated.
- 2026-09-28 JW: paused broad "chiropractor" ($859 on 10 clicks, 0 conversions).
- 2026-10-23 JW: review. Max Conversions was spending 2x the daily budget at USD 68 CPC and burned the month's budget in 5 days. Switched to Manual CPC, USD 125 → 65/day, paused broad "chiropractor greer", enabled 2 lightly pinned RSAs, made "Calls from ads" secondary. Log `logs/changes/2026-10-23_1956Z_JW_pp5347-review-fixes.md`.
