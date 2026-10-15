# PP6481 ChiroPro: 5 per-office Search campaigns built (paused), in-radius towns removed from office negative lists

- **When:** 2026-10-15 19:38 UTC (15:38 US Eastern, Sara)
- **Requested by:** SS
- **Approved by:** SS, approved the full preview in chat ("approve"), including the town removals and the 1 Nov budget change
- **Platform:** Google Ads
- **Session:** https://claude.ai/code/session_01KLi6n12BmMTkGN7niN9tsm

## Changes
| Account | Entity (type, name, ID) | Field | Before | After | Result |
|---|---|---|---|---|---|
| PP6481 - ChiroPro (143-377-9401) | Campaign "Perfect Patients - St Charles - Search 2026" (24365678317), budget 15945307349 | New campaign | – | **Paused**, USD 45/day | ✅ created |
| PP6481 - ChiroPro (143-377-9401) | Campaign "Perfect Patients - Shiloh - Search 2026" (24365678062), budget 15950552631 | New campaign | – | **Paused**, USD 45/day | ✅ created |
| PP6481 - ChiroPro (143-377-9401) | Campaign "Perfect Patients - Columbia - Search 2026" (24354624228), budget 15945306848 | New campaign | – | **Paused**, USD 25/day | ✅ created |
| PP6481 - ChiroPro (143-377-9401) | Campaign "Perfect Patients - Troy - Search 2026" (24365679790), budget 15945308528 | New campaign | – | **Paused**, USD 20/day | ✅ created |
| PP6481 - ChiroPro (143-377-9401) | Campaign "Perfect Patients - Highland - Search 2026" (24365678077), budget 15945308564 | New campaign | – | **Paused**, USD 15/day | ✅ created |
| PP6481 - ChiroPro (143-377-9401) | Shared lists: St Charles, Shiloh, Troy and Columbia Negative Keywords | Phrase negatives inside the office radius | Present | Removed (16, listed below) | ✅ applied |

**Each campaign**
- **Settings:** Search, manual CPC (no ECPC), Google Search only (Search Partners and Display off), English, presence only.
- **Location:** an 8-mile radius around the office: 3711 Mexico Rd St Charles MO; 1231 Thouvenot Ln Shiloh IL; 1005 S Main St Columbia IL; 220 US-40 Troy IL; 208 Flax Dr Highland IL.
- **Ad schedule (as on the old campaign):** Mon 8–18, Tue 9–18, Wed 8–18, Thu 9–18, Fri 7–11.
- **Negatives:** campaign phrase negatives for the other offices' town names. Shared lists attached: Stock, Competitors, Account Level, plus that office's own list.
- **Assets:**
  - Call asset with the office's WhatConverts "Google Ad Extension" number: St Charles (636) 434-2607 (193509167446), Shiloh (618) 356-2436 (193509021283), Columbia (618) 342-7613 (193491841362), Troy (618) 668-0812 (193493555061), Highland (618) 681-4675 (193467140981).
  - The 5 existing sitelinks, 11 callouts ("7 Convenient Locations" left off) and 1 structured snippet.
- **Ad groups (both enabled; the campaign itself is paused):**
  - "Chiropractor [Office]", USD 25 default bid: city keywords in phrase and exact, plus the saint charles variants for St Charles.
  - "Chiropractor Near Me [Office]", USD 27 default bid: 9 near-me and generic keywords.
- **Ads:** 2 RSAs per ad group, 20 in total. Final URL is the current office page, e.g. `https://www.chiropro.com/shiloh-chiropractor/?utm_source=v_adwords&utm_medium=search&utm_campaign=chiropractor_shiloh`. Full copy matches the approved preview.
- **Totals:** 10 ad groups, 111 keywords, 20 ads. All ads were "review in progress" at build time.
- **Policy exemption:** 21 keyword texts were flagged with Google's exemptible HEALTH_IN_PERSONALIZED_ADS policy, the same as the account's existing chiropractic keywords. They were submitted with an exemption request. This only restricts personalized-audience use of health terms.

**Towns removed from office negative lists** (each within 8 miles of that office)
- **St Charles Negative Keywords:** st peters, saint peters, 63301, cottleville, o fallon
- **Shiloh Negative Keywords:** 62269, o fallon, fairview heights, swansea, belleville, collinsville
- **Troy Negative Keywords:** maryville, glen carbon, collinsville, edwardsville
- **Columbia Negative Keywords:** waterloo
- **Highland:** none within the radius.
- **Kept on purpose, just outside the St Charles radius:** 63366 (8.7 mi), maryland heights (8.9 mi).

## Failed or skipped
- None.
- The first dry run was rejected over the healthcare keyword policy. Nothing was created; the build went through once the exemptions were added.

## Notes
- **Budget:** the new budgets total USD 150/day, the same as the current "Perfect Patients" campaign, so no change in spend while they're paused.
- **Switch-over:** when Sara enables the new campaigns, pause "Perfect Patients" (23580321327) at the same time. That's agreed, but still needs her go-ahead on the day.
- **1 Nov:** a one-off reminder (trig_01L5Q4pghAiyUaBzAPyKe1ZS) is scheduled to set the November budgets: St Charles 70, Shiloh 70, Columbia 40, Troy 30, Highland 25 = USD 235/day, about USD 7,144 a month against the USD 7,200 Salesforce budget. If only the old campaign is live then, set it to USD 235/day instead.
- **Call reporting:** left off on the call assets on purpose. Calls come in through WhatConverts, which avoids double counting (Sara).
- **Landing pages:** new per-office pages are coming. Swap the final URLs when they're ready.
