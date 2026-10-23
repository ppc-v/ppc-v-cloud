# John's Google Ads reviews: how JW likes them done

From JW's review session on 2026-10-23. Use this for any Google Ads review on John's accounts.

## Scope and history
- Review **active and paused campaigns only**. Never review removed campaigns, including those left from the April 2026 breach.
- Read the historic notes on the "Google AdWords Review" case first. It may hang off the client's **Account** rather than the Paid Advertising Project (e.g. PP5347 case 00553324), so search the Account's cases if the project has none.
- Work one account at a time; don't make sweeping changes. Flag bigger changes (bid strategy, budget) as a recommendation and let JW decide.

## Report layout (JW's format)
Budget (limited? Google's recommendation vs our daily budget), impressions/clicks up or down, CTR + % change, conversions (30 days) + % change, conversions by action, CPC + % change, CPL + % change, notes on the data, what was done this review, last-30-day call tracking breakdown, call notes. Say which calls still need scoring.
After approval and applying: a Salesforce-ready summary for JW to post, with a **KEEP TABS** line. **Highlight any budget change and its reasoning** (e.g. `*** BUDGET CHANGE ... ***`). Post case comments only when JW asks.

## Negative keywords
- Default to **phrase** match; exact only for bare generic searches like [doctor] or [clinic]. No broad-match negatives.
- Business names: a **single distinctive name** ("baker", "kettering") catches every variant, because negatives don't match close variants. Names made of common words ("joint chiropractic", "relief wellness", "elite chiropractic") stay as **two-word phrases** so they don't block good searches.
- Leave out searches that converted (competitors included), unless the "conversion" was clearly not a lead.
- Before adding, **check the existing lists for conflicts** and show JW the list to approve:
  - state/province abbreviations that are also words, e.g. "IN" and "OR" in stock lists (they blocked "chiropractor in greer" on PP5347); "ME" would block "near me"
  - nearby suburbs/towns inside the radius (be mindful: unblock close ones, keep edge ones with their own providers)
  - services the practice offers (check the website) and offer wording in the ads (e.g. "free" vs a free consultation)
  - the office's own street or area names
- Intentional negatives to keep: e.g. PP6304 "invisalign" (expensive, research-based).

## Other preferences
- Ads keep running during office closures unless the client asks to pause.
- The "Enable Campaign 1st" rule is active on JW's accounts.
- When Max Conversions has very few leads (about 2-9 a month) and CPCs climb, suggest Manual CPC (applied on PP5347; noted as next step on PP6304).
- Apply changes with each step run once; verify with read-only queries rather than re-running an apply script.
