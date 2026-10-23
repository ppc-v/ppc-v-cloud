# PP1654: Audience Network removed from both lead ad sets

- **When:** 2026-10-23 13:02 UTC (09:02 US Eastern, Sara)
- **Requested by:** SS
- **Approved by:** SS, approved preview in chat
- **Platform:** Meta
- **Session:** https://claude.ai/code/session_01L7HCWStozQv2YmJHW1GfSp

## Changes
| Account | Entity (type, name, ID) | Field | Before | After | Result |
|---|---|---|---|---|---|
| PP1654 - Goffstown Chiropractic Care (act_3615153821950382) | Ad set "Sports Ads Set - Lead" (120252876845190220) | targeting.publisher_platforms | not set (Advantage+ placements, all platforms incl. Audience Network) | facebook, instagram, messenger, threads (all positions) | ✅ applied, confirmed by re-read |
| same | Ad set "Pediatric AdSet - Form Fills" (120252912927790220) | targeting.publisher_platforms | not set (Advantage+ placements, all platforms incl. Audience Network) | facebook, instagram, messenger, threads (all positions) | ✅ applied, confirmed by re-read |

## Failed or skipped
None. WhatsApp Status is also no longer included (it had $0.04 of spend); add it back if wanted.

## Notes
- Why: 14–22 Oct, Audience Network took $19.09 of $100.83 lead-campaign spend for 37 of 84 link clicks but 4 landing page views.
- Bigger issue: "Appt Form Submission" hasn't fired since SS's test on Oct 12 (site-wide), so both ad sets optimise for an event with no data. Clicks fell from ~25/day to 4–8/day and landing page views to ~0 from Oct 15.
- Revisit on 2026-11-01: if still no form fills, rebuild with a higher-volume goal (landing page views, or one combined ad set). SS agreed.
- Ad sets went back to IN_PROCESS (review) after the edit; budget unchanged at $10/day (campaign level).
