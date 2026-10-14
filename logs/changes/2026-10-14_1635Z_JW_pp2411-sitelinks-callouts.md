# Campaign-level sitelinks and callouts for PP2411 - Universal Chiropractic

- **When:** 2026-10-14 16:35 UTC (11:35 US Central)
- **Requested by:** John Wylie (JW)
- **Approved by:** JW, "approved" on the preview in chat
- **Platform:** Google Ads
- **Session:** https://claude.ai/code/session_013dj8bHtuu5r6yWsX6NxYLc

One atomic mutate (36 operations: 18 assets + 18 campaign links), dry-run with validate_only first. Copy and URLs taken from universalchiro.ca; every URL returned 200.

## Changes
| Account | Entity (type, name, ID) | Field | Before | After | Result |
|---|---|---|---|---|---|
| PP2411 - Universal Chiropractic (990-954-7723) | Campaign "Perfect Patients" (24354926627) | Sitelinks (campaign level) | none | 8 sitelinks, below | ✅ applied |
| same | Campaign "Perfect Patients" (24354926627) | Callouts (campaign level) | none | 10 callouts, below | ✅ applied |

Sitelinks (asset ID: text / description 1 / description 2 / URL):
- 429887898605: New Patients / Your 45-minute first visit / Exam, history & posture check / /new-patients/
- 429887888102: Request an Appointment / Same-day visits available / Early, evening & Sat hours / /contact-us/
- 430074371166: Meet Our Chiropractors / Four chiropractors on site / Serving Mississauga since 2003 / /meet-the-doctors/
- 430074393714: Our Services / Chiropractic, massage & more / Naturopathic care on site / /our-services/
- 430074377937: Spinal Decompression / Non-surgical spinal decompression / Ask about it at your first visit / /spinal-decompression/
- 430074393768: Pregnancy Chiropractic / Chiropractic care for moms-to-be / Gentle, prenatal-focused care / /pregnancy-chiropractic/
- 429887898926: Pediatric Chiropractic / Care for infants and children / Family care for every age / /pediatric-chiropractic/
- 429887888117: Massage Therapy / Registered massage therapist / Book alongside your adjustment / /massage-therapy/

Callouts (asset IDs 429989149372, 429989165158, 429887888120, 430074392163, 429887898989, 429989167306, 429887899013, 429887899019, 429887892866, 430074371202): Since 2003 in Mississauga; Same-Day Appointments; New Patients Welcome; Early & Evening Hours; Saturday Hours; 4 Chiropractors On Site; Posture-Focused Care; Infant to Senior Care; Massage & Naturopathy; Book Appointments Online.

## Failed or skipped
- None. Call asset still pending (practice number vs WhatConverts tracking number).

## Notes
- Read back after applying: all 18 campaign assets ENABLED on campaign 24354926627 (campaign itself still paused).
