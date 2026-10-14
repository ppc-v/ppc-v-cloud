# Prompt playbook

Prompts that work well, by task. Copy one, change the initials and the PP number, send. New to this? Read the [quick start](quick-start.md) first.

**Tips that apply to everything**
- Give the PP number or ad account ID, the date range, and what you'll do with the answer ("for the client call", "for Salesforce"). Claude pitches the output to fit.
- Say how you want it back: a table, bullet points, a Google Sheet, a doc, a draft Slack message.
- Ask follow-ups in the same session; Claude keeps the context. Start a new session for a new task.
- When you approve a change, say "yes" or "go". Anything else and Claude will check with you again.

## Daily triage
```
SS: daily health check
JW: daily health check, red and orange
IA: daily health check for everyone, fast pass only, then I'll pick which to dig into
SS: why is PP4956 flagged NO_LEADS? Check WhatConverts too
JW: PP6236 says ACTIVE_NOT_SPENDING. What's stopping it?
SS: snooze SPEND_SWING on PP1654 until 31 Oct, client paused for a holiday
```

## Performance and reporting
```
JW: PP5416 last 30 days vs previous 30: spend, clicks, leads, CPL, by campaign
SS: which of my accounts had the biggest CPL increase this week?
IA: total spend and leads across all Active accounts last month, by owner, in USD
SC: write the bi-weekly Salesforce review for PP0519
JW: monthly report draft for PP5416. Check the notes for their format first
SS: compare Google and WhatConverts leads for PP4956 since 1 Oct
```
Uses the `campaign-review-summary` skill for Salesforce reviews.

## Search terms and keywords
```
JW: search terms for PP5416, last 14 days. Build negatives and preview them
SS: which search terms spent over $50 with no conversions across my accounts?
SC: suggest new keywords for PP3906 from converting search terms
JW: is broad match "dentist near me" on PP5416 matching junk?
```
Uses the `negative-keyword-builder` skill.

## Budgets and bids
```
SS: pacing for my accounts: month-to-date vs monthly budget, projected month end
JW: raise PP5416 to AUD 100/day. Show daily and monthly effect
IA: which accounts are losing over 50% of searches to budget?
SS: PP4956 is spending 195% of budget yesterday. Why?
JW: which of my accounts will run out of budget before the 31st, and what daily budget fixes it?
IA: pacing for everyone, only the accounts that need action
```
Uses the `budget-pacing` skill: budgets come from Salesforce (Paid Advertising Project), and "runs out early" means the monthly budget rule will pause the account before month end. Every budget or bid change gets a preview with the daily and monthly effect.

## Ads and creative
```
SS: 5 RSA headlines and 4 descriptions for PP4956's emergency dentist ad group
JW: refresh Meta creative for PP1654: newest ad is 98 days old. Draft 3 concepts, 1:1
SC: rewrite PP3906's disapproved ad to fix the policy issue
SS: landing page for PP4956's Invisalign offer
```
Uses the `google-ads-copy`, `meta-ads-copy`, `headline-copy`, `ppc-landing-page` and `ads-asset-review-canva` skills. Confirm sizes and formats each time.

## Tracking
```
IA: audit conversion tracking on PP0519: Google goals, GA4, GTM, WhatConverts
JW: which of my accounts count button clicks or page views as primary conversions?
SS: PP1654 pixel: is it firing, and what events?
IA: set up form-submit and call tracking for PP3906 in GTM. Workspace only, show me before publishing
SC: PP1654 says TRACKING_STOPPED. Run a tracking audit
JW: tracking audit sweep on my Google accounts, red and orange findings only
```
Uses the `tracking-audit` skill. Calls and leads are only ever reported as counts; patient details from WhatConverts never appear.

## Building and structure
```
SS: campaign structure for a new chiro client in Austin, $1,500/month, new patients
JW: build the search campaign we agreed for PP5416. Create it paused
IA: audience research for a dental implant campaign in Sydney
```
Uses the `campaign-structure-brainstorm` and `audience-market-research` skills.

## Bulk work across accounts
```
IA: list every Active account with no call conversion set up
SS: add these 20 negatives to all my dental accounts. One approval for the batch
JW: pause everything labelled Canceled that's still spending. Preview first
```
Claude asks whether you want one approval for the batch or one per account.

## Client memory
```
JW: add to PP5416 notes: client wants calls only, ignore booking clicks
SS: what do we know about PP4956? Notes, recent changes, open flags
IA: what changed on PP0519 in the last 30 days, and who did it?
```

## Housekeeping
```
SS: check connections
JW: show me today's change logs
SC: add my timezone to the team table: <timezone>
```
