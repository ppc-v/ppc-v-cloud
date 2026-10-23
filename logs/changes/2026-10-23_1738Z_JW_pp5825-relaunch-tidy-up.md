# PP5825: relaunch tidy-up (schedule, callouts, typo, location, goals, Max Clicks)

- **When:** 2026-10-23 17:38 UTC (12:38 US Central, John's time)
- **Requested by:** JW (John)
- **Approved by:** JW, approved the full preview in chat ("Those changes and ideas look good to me. Go ahead."), then agreed the NZD 15 max CPC ("CPC max makes sense")
- **Platform:** Google Ads
- **Session:** https://claude.ai/code/session_01RaxPZsTsPJiRg7UR4UL5vR

## Changes
| Account | Entity (type, name, ID) | Field | Before | After | Result |
|---|---|---|---|---|---|
| PP5825 - Be Vital Chiropractic (464-210-2599) | Campaign "Perfect Patients" (20578631432) | Ad schedule (Pacific/Auckland) | Mon 07:30–17:00 (303068), Wed 07:30–17:30 (323070), Thu 07:30–17:30 (333070), Fri 08:00–11:30 (343246); no Tue | Mon 07:00–18:00 (302872), Tue 14:00–17:45 (315671), Wed 07:00–18:00 (322872), Thu 08:00–18:00 (333272), Fri 07:00–12:00 (342848) | ✅ applied |
| same | Campaign callout | Asset link | "$65 New Client Special" (284628577341) | Unlinked; new callout "$68 New Client Special" (432658910393) linked | ✅ applied |
| same | Campaign callout | Asset link | "Convienient Location" (102310002331) | Unlinked; new callout "Convenient Location" (432762293371) linked | ✅ applied |
| same | RSA 674920828757 (ad group "Chiropractor") | Headline 15 (pinned H3) | Convienient Bethlehem Location | Convenient Bethlehem Location (pin kept) | ✅ applied |
| same | RSA 694964855715 (ad group "Chiropractor Tauranga") | Headline 15 (pinned H3) | Convienient Tauranga Location | Convenient Tauranga Location (pin kept) | ✅ applied |
| same | RSA 674829354360 (ad group "Bethlehem", paused) | Headline 15 | Convienient Bethlehem Location | Convenient Bethlehem Location | ✅ applied |
| same | Campaign "Perfect Patients" | Location option (include) | Presence or interest | Presence | ✅ applied |
| same | Campaign "Perfect Patients" | Bid strategy | Maximize Conversions (no target CPA) | Maximize Clicks, max CPC NZD 15.00 | ✅ applied |
| same | Conversion actions: Calls From Google Ads (6810811146), Calls From Ad Extensions (6810723814), Calls from Ad Extensions (6812195233), Call Tracking Lead (6652483898), Phone Number Only Call Tracking (6652484063) | Primary for goal | Primary | Secondary | ✅ applied |

Unchanged: daily budget NZD 39.47 (≈ NZD 1,200/month, matches Salesforce), 6-mile radius around 16 Bethlehem Road, device adjustments (desktop −10%, mobile +15%, tablet none), "Calls from Google Ads" (6812195227, WhatConverts import) and the booking page view goal stay primary.

## Failed or skipped
- None failed. Every batch was validated with validate_only first, then applied, then read back (schedule, callout links, headlines and pins, TARGET_SPEND with a NZD 15 ceiling, PRESENCE, conversion action primary flags all confirmed). The script reported an error on the callout batch, but only in its own result printing after the API calls had succeeded; the read-back confirmed the links.
- RSAs came back APPROVED / REVIEWED on read-back.

## Notes
- Why: the account has been dormant since 28 Apr 2026 (hijacked that day; the team is handling that separately). The schedule now matches the clinic's office hours from the website. The new client offer is $68 on the landing page and in the ads. Max Clicks gives the account a few weeks to gather fresh data after 6 months off. NZD 15 is about the 90th percentile of historic CPC (median NZD 9.71; desktop NZD 14–15; "Tauranga Chiropractor" broad NZD 12.25).
- Follow-up in about 2 weeks (around 6 Nov 2026): check CPCs and conversions. If there are enough data points, switch back to Maximize Conversions (separate approval).
- Still open: booking submission goal (7249030073) has never fired, and the booking page view (7080886943) is the main primary goal. Fix submission tracking before relying on Max Conversions.
