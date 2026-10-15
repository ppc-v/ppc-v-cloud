# PP6481 ChiroPro: lower budget, pause broad keywords, add negatives, reset device bids, demote page-view goal

- **When:** 2026-10-15 19:08 UTC (15:08 US Eastern, Sara)
- **Requested by:** SS
- **Approved by:** SS, approved the full preview in chat ("approve all")
- **Platform:** Google Ads
- **Session:** https://claude.ai/code/session_01KLi6n12BmMTkGN7niN9tsm

## Changes
| Account | Entity (type, name, ID) | Field | Before | After | Result |
|---|---|---|---|---|---|
| PP6481 - ChiroPro (143-377-9401) | Campaign budget for "Perfect Patients" (budget 15383092929, campaign 23580321327) | Daily budget | USD 405.00 | USD 150.00 | ✅ applied |
| PP6481 - ChiroPro (143-377-9401) | Keyword `chiropractor` (broad), ad group "Chiropractor" (195987951320~12457821) | Status | Enabled | Paused | ✅ applied |
| PP6481 - ChiroPro (143-377-9401) | Keyword `chiropractic adjustment near me` (broad), ad group "Chiropractor Near Me" (195987951480~296440987624) | Status | Enabled | Paused | ✅ applied |
| PP6481 - ChiroPro (143-377-9401) | Shared negative list "Account Level Negative Keywords" (11464716827) | Phrase negatives | 2,177 entries | 2,233 entries (+56, listed below) | ✅ applied, no partial failures |
| PP6481 - ChiroPro (143-377-9401) | Campaign "Perfect Patients" device criterion Mobile (23580321327~30001) | Bid adjustment | +15% (1.15) | 0% (1.00) | ✅ applied |
| PP6481 - ChiroPro (143-377-9401) | Campaign "Perfect Patients" device criterion Desktop (23580321327~30000) | Bid adjustment | −15% (0.85) | 0% (1.00) | ✅ applied |
| PP6481 - ChiroPro (143-377-9401) | Conversion action "Book Appointment Page Views" (6984945262) | Primary for goal | Primary | Secondary | ✅ applied |

Negatives added (phrase match):
- Products: halsten, bodylever, relivez, theraworx, pso rite, tryfascial, back pod, posture corrector, shoulder straightener, pstrelab, back braces, tablets
- Other clinics, providers and people: park place chiropractor, health source chiropractic, fidel chiropractic, dawn chiropractic, hollander chiropractor, yarger chiropractic, proactive chiropractic, schopp nutrition, rajneesh kant, leslie jacobi, swing care, osf rehabilitation, st charles ortho
- Conditions and procedures outside chiropractic: plantar fasciitis, carpal tunnel, rheumatoid arthritis, psoriatic arthritis, erosive arthritis, spondyloarthritis, ankylosing spondylitis, arthroscopy, nerve ablation, interbody fusion, cervical fusion, rotator cuff, labral tear, osteoporosis, cauda equina, compression fracture, bone spurs, golfer's elbow, achilles, bursitis, synovial fluid, heel pain, leg cramps, muscle cramp
- Spanish exercise searches: ejercicio, ejercicios, ciática
- Informational: healthline, are chiropractors safe, hasfit, boho beautiful

## Failed or skipped
None. Each value was re-read before the change and confirmed after it.

## Notes
- **Budget:** daily effect is a maximum of about USD 300 on any one day (2× daily), down from about USD 810. Monthly effect: October was projected at about USD 10,400 against the USD 7,200 Salesforce budget, with the cap reached around 22 Oct and about 9 dark days. At USD 150/day with 12 weekdays left, October should finish close to USD 7,200. The calendar month was used; Salesforce shows billing on the 27th.
- **Keywords:** `chiropractor` phrase and `chiropractic adjustment near me` exact remain enabled.
- **Negatives:** these searches cost about USD 2,500 over 17 Aug–14 Oct with no conversions. Left off on purpose: "oak street health" (3 odd conversions, check in WhatConverts), services ChiroPro may offer (neuropathy, softwave/shockwave, decompression, scoliosis, upper cervical, Webster), and "optum"/insurance searches.
- **Bidding:** the campaign uses manual CPC, so demoting the page-view goal changes reporting, not bidding.
- **Follow-ups:**
  - Recheck pacing and leads around 22 Oct.
  - Confirm in the UI why Search Partners still shows spend when the API reports it off.
  - Preview the split by office with matching landing pages.
