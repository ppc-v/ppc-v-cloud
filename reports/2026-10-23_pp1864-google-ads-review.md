# PP1864 Memorial Drive Chiropractic and Massage: Google Ads review (2026-10-23)

Requested by: SS. Read-only; nothing changed. Google Ads 474-357-1274 (account timezone America/Vancouver; the practice is in Calgary, Mountain time), data through 22 Oct. Budget: CAD 1,920/month (Salesforce). WhatConverts profile 142918.

## Snapshot
| Month | Spend | Clicks | Avg CPC | Google conversions |
|---|---|---|---|---|
| Apr | 1,655 | 124 | 13.34 | 20 |
| Jun | 1,802 | 161 | 11.19 | 16 |
| Jul | 1,974 | 164 | 12.03 | 9 |
| Aug | 1,949 | 95 | 20.51 | 11 |
| Sep | 1,983 | 96 | 20.66 | 5 |
| Oct 1-15 | 2,233 | 95 | 23.51 | 16 (3 are double-counted calls) |

CPC has almost doubled since July, and clicks fell by about 40%.

## WhatConverts calls, 24 Jul - 23 Oct (38 calls tagged google / cpc)
| Type | Calls |
|---|---|
| New patient, booked or strong enquiry (quotable Yes, or proposed Yes) | 11 |
| Existing patient: reschedule, cancel, receipt, refund, running late | 11 |
| Missed / hung up during greeting (under 25s) | 10 |
| Not a lead: job applicant, X-ray film buyer, wrong number, caller in Winnipeg, language mix-ups | 6 |

Every new-patient call lasted 149s or more. Google Ads counted 28 of these calls as conversions (plus 3 from Google's own call tracking), so about 1 in 3 imported calls is a real new patient.

## Findings
1. **Dark half of every month, and over budget.** CAD 150/day, but Maximize conversions spends 2x (about CAD 300) on each of the roughly 13 scheduled days (Mon/Wed/Thu). The budget runs out mid-month (16 Sep; 15 Oct). The rule fires after a full day's spend, so October ended up CAD 313 over budget.
2. **Double-counted calls.** Google's own "Calls from ads" is primary alongside the WhatConverts call imports.
3. **Bidding on junk.** All imported calls count, including 10 short or missed calls and 11 existing-patient calls. Max Conversions is learning from the wrong signal and has pushed CPC from about 12 to 23.
4. **Broad match leaks spend.** About CAD 1,500 over 90 days went on searches like hip and knee clinic (about 410), "mass muscle" (179), other clinics and brands (Primaris, Synapse, One8t, Wells Health, Connecta, Telus Health, Shepard Health, Beaconhill, Revolve, Gehrke), products (mattress, back brace, posture corrector, pain patch) and other specialties (podiatrist, orthopedist, orthotics, SoftWave, Scenar, Discseel). The best keyword, "chiropractor calgary", is **paused**; that search still matches through the broad keywords.
5. **One ad, every headline pinned.** Average strength. It promotes a $49 exam; on a 14 Oct call the front desk quoted "$99 for the first visit". Check the current offer.
6. **Overlapping radii** (2/4/6/8/10 km); effectively 10 km.
7. **Form tracking silent.** "PPC Appt Request Form" was last recorded in Aug; "Custom Form Appt Request" has been silent since June. There's no GTM access to check it.
8. **April hack** (CAD 17, two Vietnamese campaigns, removed).

## Recommendations (each needs approval before it's applied)
1. Daily budget CAD 150 → CAD 74. At about 2x on roughly 13 scheduled days that's about CAD 1,920/month, spread to month end.
2. Make "Calls from ads" (Google call tracking) secondary. In WhatConverts' Google Ads integration, send only 60s+ calls (or quotable only).
3. Manual CPC instead of Max Conversions, with CPC caps of about CAD 18-20.
4. Keywords: re-enable "chiropractor calgary" (phrase); add "chiropractor near me" phrase + exact and "chiropractor" phrase; pause the broad "chiropractor near me", "chiropractor" and "neck pain chiropractor".
5. Add negatives for the categories above.
6. Confirm the new-patient offer ($49 vs $99), then add an unpinned RSA.
7. Keep only the 10 km radius.
8. Get GTM access and run a tracking audit on the forms.
