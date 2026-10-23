# PP3159 Google Ads: longer ad schedule, Sciatica ad group live

- **When:** 2026-10-23 20:52 UTC (15:52 US Central; 16:52 Toronto, the account's timezone)
- **Requested by:** JW
- **Approved by:** JW, "Let's do 4 and 5" on the options preview in chat
- **Platform:** Google Ads
- **Session:** https://claude.ai/code/session_01LcRb8DvrKpT3HL8f9bhwTj

## Changes
PP3159 - Herron Family Chiropractic (681-623-5254), campaign "Perfect Patients" (10157736635).

| Entity | Field | Before | After | Result |
|---|---|---|---|---|
| Ad schedule (campaign criteria 303270, 313270, 323270, 333270 → 302484, 312484, 322484, 332484) | Mon-Thu hours | 8:00-17:00 | 6:00-21:00 | ✅ replaced in one atomic request |
| Ad group "Sciatica" (106123650631) | Status | Paused | Enabled | ✅ |
| Keyword "sciatica relief" phrase (16011460) | Status | Paused | Enabled | ✅ |
| Keyword "sciatica treatment" phrase (23338183) | Status | Paused | Enabled | ✅ |
| Keyword "sciatica" broad (11038541) | Status | Enabled | Paused | ✅ |
| Keyword "sciatica" phrase (69305271) | Status | Enabled | Paused | ✅ (so only the treatment/relief phrases run, per the proposal) |

## Failed or skipped
- None failed. Read back: Mon-Thu 6-21; Sciatica ad group enabled with only "sciatica relief" and "sciatica treatment" (phrase) live. Its ad 518093087211 is approved and lands on /sciatica-treatment-in-cobourg/ (HTTP 200).
- Not approved this time (options 1-3, 6): turning the "1st of month" rule back on (UI only), 20 km radius, removing the "port hope"/"northumberland" negatives and enabling the Port Hope ad group, pausing for the office closure (26-30 Oct). The campaign will run during the closure week.

## Notes
- Why: the campaign had zero impressions 25 Aug - 20 Oct (no eligible auctions; card on file is fine per JW) and resumed 21-22 Oct after a campaign + budget change on 22 Oct (who/what not visible through the API; check Change History in the UI). When live in August it converted well (CAD 441, 23 clicks, 10 conversions); the limit is reach (about 25 eligible searches a day), not budget (CAD 120/day).
- Calls after 17:00 go to voicemail; watch for missed calls from the new evening hours.
- Correction (JW): the "Enable Campaign 1st" rule is active, so it wasn't the cause of the dark period; ads run during the closure week (client didn't ask to pause).
- Case note posted on Salesforce case 00553324 (internal comment 00aN100000dcu7ZIAQ).
