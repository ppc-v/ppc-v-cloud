# PP6773 - Mind and Spine Chiropractic

- **Google Ads ID:** 375-946-4446 (America/Chicago, USD). Brand label: Perfect Patients
- **Meta ad account ID:** none in the inventory
- **WhatConverts profile:** 174065 (account 119615). Paid call tracking numbers: +1 629-284-6196 (the call asset, most paid calls, no GCLID), +1 423-589-1080, +1 615-915-2413. GBP number +1 423-564-6449.
- **GTM container / GA4 property:** GTM-PDQ4R3PW on the site, not shared with paidsearch@. No GA4 property visible to paidsearch@.
- **Access:** normal
- **Usually worked on by:** Sara (Google label); John has also made changes
- **Salesforce:** $1,500/month Google budget, billing day 8.

## Setup (as of 2026-10-20)
- New account: one Search campaign, "Perfect Patients" (24182598704), started 2026-08-26. Maximize Conversions (no target), $40/day (from 2026-10-20; $71/day pre-approved for November), **Search Partners on**, Display off.
- Location: presence only, layered radii 1/2/4/6/8 mi around 139 Maple Row Blvd, Hendersonville TN 37075 (4 mi has +15%, which Maximize Conversions ignores). Mobile +15%.
- Ad schedule: Mon & Wed 8–18, Tue & Fri 8–15, Thu 10–18 (no weekends).
- Ad groups: Chiropractor (broad/phrase/exact "chiropractor", "back pain chiropractor"), Chiropractor Hendersonville (broad/phrase/exact), Chiropractor Near (broad/phrase/exact "chiropractor near me").
- One RSA per ad group, nearly identical, every headline pinned, Average strength. All go to /chiropractor-hendersonville/ ($40 new patient special).
- Shared negative lists: Competitor (108), Stock (175), Search Queries (272), plus 7 campaign negatives (brand and Dr. Dotson's name are excluded on purpose).
- **Negatives preference (SS):** add every negative to a shared list, never as a campaign negative: competitor and other-practice names go to "Competitor Negative Keywords", everything else to "Search Queries".
- Ads offer: **$40 new patient special** (consultation, exam, X-rays if needed); Sara confirmed. The site header and New Patients page still say $60.

## Tracking
- Primary goals: Calls From Ad Extensions (WhatConverts call import), Calls From Google Ads (WhatConverts click import), both counting one per click since 2026-10-20; Appointment Request (New Patient) and Contact Us Submission (GA4). Appointment Request (Current Patient) is secondary. WhatConverts should send only calls of 30s or longer (Sara to set in the UI).
- Call asset (629) 284-6196 has Google call conversion reporting off (calls come in through the WhatConverts import instead).

## History and decisions
- 2026-10-20 SS: performance review, no changes made. Findings: about two thirds of visible search-term spend (about $1,175 of $1,764 since late July) went to searches for other providers' names (TOA, AOS, Integrity Pain, Brentwood Bone & Joint, other chiropractors and pain clinics), and those searches produced most of the recorded conversions, so Maximize Conversions is learning from them. WhatConverts: 26 paid calls since launch, 18 unanswered and under 30 seconds, about 2 new-patient calls. Search Partners $121, 0 conversions. 36% of searches lost to budget (last 30 days). October will hit the $1,500 cap around 26–27 Oct at the current pace. GBP calls in WhatConverts stopped after September (138 in Sep, 0 in Oct).
- 2026-10-20 SS: daily budget $60 → $40 so October's $1,500 lasts to Oct 30 (MTD was $1,161.30). Sara pre-approved $71/day for November; check-in set for 2026-11-01 (trigger trig_01EDxYKyaaNdXar9hBKFLXxW). See `logs/changes/2026-10-20_1436Z_SS_pp6773-daily-budget.md`.
- 2026-10-20 SS: applied the review fixes. Call actions now count one per click; Current Patient appointment is secondary; 30s minimum for WhatConverts call imports (Sara, in the WhatConverts UI). 50 competitor negatives added to the Competitor list and 54 to Search Queries (Sara had already added many to Search Queries that morning). Broad "chiropractor hendersonville" and "chiropractor near me" paused. Search Partners off. New RSAs 828708489758 / 828708489761 / 828708489764 with the old ones kept live for comparison. See `logs/changes/2026-10-20_1423Z_SS_pp6773-review-fixes.md`. Check results around 2026-11-03; consider pausing the old RSAs then.
