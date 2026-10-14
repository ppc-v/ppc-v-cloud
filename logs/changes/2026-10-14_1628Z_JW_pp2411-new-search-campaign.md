# New Search campaign "Perfect Patients" for PP2411 - Universal Chiropractic

- **When:** 2026-10-14 16:28 UTC (11:28 US Central)
- **Requested by:** John Wylie (JW)
- **Approved by:** JW, approved the preview in chat (bid strategy changed to Maximize Conversions; keywords and ad copy approved)
- **Platform:** Google Ads
- **Session:** https://claude.ai/code/session_013dj8bHtuu5r6yWsX6NxYLc

All entities were created in one atomic mutate request (254 operations), dry-run with validate_only first.

## Changes
| Account | Entity (type, name, ID) | Field | Before | After | Result |
|---|---|---|---|---|---|
| PP2411 - Universal Chiropractic (990-954-7723) | Budget "Perfect Patients Budget" (15942374858) | Daily budget | none | CAD 39.47/day (about CAD 1,200/month), standard delivery | ✅ applied |
| same | Campaign "Perfect Patients" (24354926627) | Created | none | Search, **PAUSED**, Maximize Conversions (no tCPA), Google Search only (partners and Display off), Presence targeting, English | ✅ applied |
| same | Campaign 24354926627 | Proximity targets | none | 15, 10, 5, 3, 2, 1 km around 1900 Minnesota Ct #110, Mississauga ON L5N 3C9 (43.603296, -79.741502) | ✅ applied |
| same | Campaign 24354926627 | Negative locations | none | 218 countries (all except Canada) + AB, BC, MB, NB, NL, NS, NT, NU, PE, QC, SK, YT (230 total) | ✅ applied |
| same | Ad group "Chiropractor" (204840146367) | Created | none | PAUSED; keywords [chiropractor], "chiropractor", chiropractor; 1 RSA (827985481569) | ✅ applied |
| same | Ad group "Chiropractor Near Me" (204950460870) | Created | none | PAUSED; keywords [chiropractor near me], "chiropractor near me", chiropractor near me; 1 RSA (827985449724) | ✅ applied |
| same | Ad group "Chiropractor Mississauga" (200777236709) | Created | none | PAUSED; keywords [chiropractor mississauga], "chiropractor mississauga", chiropractor mississauga; 1 RSA (827985468669) | ✅ applied |

RSA (same in all three ad groups). Final URL https://www.universalchiro.ca/chiropractor-in-mississauga/, paths Chiropractor / Mississauga.
Headlines: Chiropractor in Mississauga; Mississauga Chiropractor; Chiropractor Near You; Universal Chiropractic; New Patients Welcome; Same-Day Appointments; Serving Mississauga Since 2003; Four Chiropractors On Site; Early, Evening & Sat Hours; Book Your First Visit; Corrective Chiropractic Care; Posture-Focused Chiropractic; Thorough 45-Min First Visit; Care for Infants to Seniors; Request an Appointment Online.
Descriptions: Corrective chiropractic care in Mississauga since 2003. New patients welcome. Book today. / Your first visit includes a health history, exam and posture analysis. Request online. / Four chiropractors under one roof. Early morning, evening and Saturday hours available. / We see patients with sciatica, headaches, neck and lower back pain. Same-day visits.

## Failed or skipped
- First validate_only attempt was rejected: keywords hit the exemptible HEALTH_IN_PERSONALIZED_ADS policy. Re-sent with an exemption request (same as "submit anyway" in the UI); validated and applied. Keywords and ads are under review.
- Call asset not created: waiting for John to decide between the practice number and a WhatConverts tracking number.

## Notes
- Campaign and ad groups are paused; enable both to launch.
- Before launch: billing setup is PENDING; the "Contact" conversion tag is not installed on the site, so Maximize Conversions has no signal until tracking (GA4 import and/or WhatConverts calls) works.
