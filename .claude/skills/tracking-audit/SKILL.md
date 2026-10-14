---
name: tracking-audit
description: Conversion tracking audit for a client across Google Ads goals, the landing pages, GTM, GA4, Meta pixel / custom conversions and WhatConverts call tracking. Finds broken or missing lead tracking, weak goals used for bidding, double counting, calls that never reach Google Ads (no GCLID), consent gaps and anything sending patient or health data to ad platforms, then proposes fixes as a preview. Use when someone asks to audit or check tracking, conversions, goals, the pixel, GTM or GA4 for an account; asks why leads/conversions look wrong or stopped; or follows up an inventory flag like TRACKING_STOPPED, GOAL_NEVER_FIRES, NO_LEAD_TRACKING, WEAK_GOALS, ONLY_PAGE_VISITS or PIXEL_STALE.
---

# Tracking audit

A lead is a call, form, booking, registration, purchase or messaging conversation. Page views, "reached … page", booking-button clicks, directions and engagement are **not** leads (same definition as the inventory sheet, `config/accounts.md`). Bidding should optimise on real leads only.

## 1. Collect the facts

```bash
python3 scripts/tracking_audit.py PP5416                  # summary + automatic findings
python3 scripts/tracking_audit.py PP5416 --json           # everything, for digging
python3 scripts/tracking_audit.py PP5416 --url <page>     # also scan a page (e.g. the booking page, a new landing page)
python3 scripts/tracking_audit.py PP5416 --google-id 123-456-7890 --meta-id 1234567890   # accounts not in the inventory
```

The script is read-only and takes about 15 seconds; longer if the GTM index needs rebuilding (`config/gtm_containers.json`, about 2 minutes, at most daily, or `--refresh-gtm` after a client shares a container). It collects:

- **Google Ads:** auto-tagging, account call reporting, enabled conversion actions (type, category, primary, counting, conversions and last date over 90 days), call assets, top final URLs.
- **Pages:** the top landing pages' HTML: GTM, GA4, AW- and Meta pixel IDs; WhatConverts/CallRail; consent tools; URL parameters.
- **GTM:** the live version of each container found on the site: tags, IDs, conversion labels, event names, consent settings.
- **GA4:** the property by measurement ID or Google Ads link: key events, event counts over 30 days, Ads links.
- **Meta:** pixels (last fired, events over 7 days), custom conversions (rules, type, last fired), what active ad sets optimise for, ad landing URLs.
- **WhatConverts:** lead **counts only**, by type and source, google/cpc leads with and without a GCLID, by tracking number, new vs existing.

Start from the client's `accounts/<pp>-<slug>/notes.md`: it may already explain quirks (e.g. PP5416's three tracking numbers).

## 2. Judge it

The automatic findings are a starting list, not the answer. Work through:

1. **Is every real lead path tracked?** Calls from ads (call asset reporting, or WhatConverts import with GCLID), website calls (WhatConverts number swap, GA4/Ads click events), forms (thank-you page or submit event), online booking (confirmation, not the button click). Name any path that isn't tracked.
2. **Is bidding on the right thing?** Primary goals should be real leads. Weak actions (page views, button clicks) should be secondary. A "Calls from ads" action with 0 conversions while WhatConverts shows paid calls means a reporting gap, not a lack of calls.
3. **Double counting:** the same lead counted by both a GA4 import and a Google tag, or by both a call asset and a WhatConverts import; MANY_PER_CLICK on lead actions.
4. **Does it fire?** Compare the Google/Meta counts with WhatConverts and GA4 for the same period. Big gaps mean broken tracking or untracked paths. Check the inventory sheet's numbers too (`python3 scripts/inventory.py --account <PP> --json`).
5. **Meta:** pixel alive? Lead events or URL-based custom conversions? Custom conversions typed OTHER instead of LEAD? Ad sets optimising for landing page views or link clicks instead of leads?
6. **Consent:** for CA, AU, NZ, UK and EU clients, is there a consent banner and does it gate the tags (consent mode, or tag consent settings in GTM)? Say what's required; never design tracking to avoid a consent requirement.
7. **Health and patient data (CLAUDE.md):** look for health conditions, treatments or identifiers in event names, custom conversion names and rules, URL parameters, GTM custom HTML (the script flags tags that mention email/phone), GA4 event parameters and Meta audience names. Treatment-specific page URLs in rules (e.g. `/sciatica-treatment/`) are worth flagging as a policy question for the team, not as a breach. Flag; don't fix silently.
8. **Access gaps:** a GTM container or GA4 property that paidsearch@ can't see limits the audit. List what access to request (GTM Publish, GA4 Editor).

## 3. Report

```
## Tracking audit: PP0000 - Client (date, windows: Google/WhatConverts 90d, GA4 30d, Meta pixel 7d)
Verdict: one line (e.g. "Calls are under-reported in Google Ads by ~half; bidding optimises on button clicks").

| # | Severity | Finding | Evidence | Fix |
|---|---|---|---|---|
| 1 | 🔴 | ... | numbers, dates, IDs | what to change, where |

Lead paths: calls from ads ✅/❌ · website calls ✅/❌ · forms ✅/❌ · bookings ✅/❌ · Meta leads ✅/❌
Access needed: ...
Compliance notes: consent / health data
```

🔴 means leads are missing, wrong or sending patient data. 🟠 means bidding or reporting is distorted. 🟡 means hygiene. Keep the evidence factual and short.

## 4. Fixes (preview, approval, apply, log)

Confirm with the requester which conversion actions to track before building any (CLAUDE.md). Then for each fix show account, entity, current → new, and wait for approval:

- **Google Ads:** primary/secondary changes, counting type, category, call asset call-conversion reporting, enabling call reporting. Changing primary goals changes what Smart Bidding optimises for; say so, and suggest doing it early in the week.
- **GTM:** build in a new workspace, show the diff (tags, triggers, variables), and publish only after a separate approval.
- **GA4:** key event changes are live changes: preview first.
- **Meta:** custom conversion type (LEAD) can't be edited after creation, so a new one is needed; ad set optimisation event changes reset learning: mention it.
- **WhatConverts:** settings changes are made by a person in the UI; give exact steps.

Log every applied change in `logs/changes/` and push to `main`. Add a dated summary of the audit (verdict, what was fixed, what's pending) to the client's `notes.md`. Don't paste WhatConverts lead details anywhere: counts only.

## Several accounts

For a sweep (e.g. "audit tracking on all of John's accounts"), run the script per account in the background, then show one table of 🔴/🟠 findings per account and ask which to dig into. Use `inventory.py --owner John --platform Google` for the account list. Expect about 15–30 seconds per account.
