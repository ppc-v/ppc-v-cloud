---
name: daily-health-check
description: Daily triage of the team's ad accounts. Reads the Vortala Ad Account Inventory sheet's flags, checks the urgent accounts live in Google Ads / Meta, and returns a ranked to-do list with a diagnosis and a proposed fix (preview only) for each. Use when someone asks for their daily check, morning check, health check, "what needs attention", "what's on fire", "triage my accounts", "go through my red/orange flags", or to investigate a specific inventory flag (NO_LEADS, TRACKING_STOPPED, NOTHING_DELIVERING, BILLING and the rest) on one account.
---

# Daily health check

The inventory sheet already flags problems every day at 06:00 GMT+8 (see `config/accounts.md`), and the Account Monitor Slack bot already DMs each owner a list. This skill does the next step: **work out why** each urgent account is flagged, using live data, and propose the fix. It never applies anything on its own.

## 1. Scope

- **Whose accounts:** the requester's (Sara, John or Arif) unless they name someone else, "unassigned" or "everyone". Owners come from the sheet's Owner column. Stella has no accounts in the sheet yet: ask whose book she's covering.
- **Depth:** 🔴 only by default. Add 🟠 if asked, or if there are fewer than 3 🔴 accounts. On Mondays, offer 🟠 as well (the Slack bot sends the full list then).
- **One account:** if they name an account or a flag, skip to step 3 for that account.

## 2. Pull the list

```bash
python3 scripts/inventory.py --owner <Name> --level red             # accounts, most urgent first
python3 scripts/inventory.py --issues --owner <Name> --level orange # one row per problem, with days open
python3 scripts/inventory.py --account <PP number or ID> --json     # every column for one account
```

- Check the banner first. If the last refresh is more than ~26 hours old, or it reports accounts that "failed to load", tell the requester before going on. A stale sheet means stale flags.
- Snoozed issues are hidden by default; that's intended (someone already decided). Use `--include-snoozed` only if asked.
- Treat "Client status" Paused/Canceled with care: the flag may be about spend that shouldn't be happening.

## 3. Investigate each account (live data)

For each account, in order of urgency:

1. Read `accounts/<pp>-<slug>/notes.md` if it exists. Respect **Access: read only / do not touch**: still diagnose, but propose nothing that changes the account. Check `logs/changes/` for recent changes to it (`grep -l <PP number> logs/changes/*`).
2. Run the checks for its flag codes from the table below. Use the account's own timezone for every date range and say so.
3. Decide on a **cause** (confirmed / likely / unknown) and a **next step**. Don't stop at restating the flag: "no leads in 15 days" is the flag; "the call import only counts calls with a GCLID, and the 3 recent calls came through the call asset" is a diagnosis.

### Checks by flag

Google Ads queries use `GoogleAdsService.search` with `customer_id` = the account ID without dashes (`GOOGLE_ADS_LOGIN_CUSTOMER_ID` is already the MCC). Meta calls go to `https://graph.facebook.com/v26.0/act_<id>/...` with `META_ACCESS_TOKEN`. WhatConverts uses `https://app.whatconverts.com/api/v1/` with the token and secret as basic auth.

| Flag | What to check |
|---|---|
| NO_LEADS, LEADS_DROP, CPL_UP | Conversions by action for the last 30 days (Q2) vs goal setup (Q3): did a lead action stop, or did traffic change? Daily spend, clicks and conversions (Q8). Recent changes (Q5). Search terms (Q7) for drift. For call-tracked clients, compare WhatConverts leads in the same period: calls may be happening but not reaching the platform. |
| TRACKING_STOPPED, GOAL_NEVER_FIRES, PIXEL_STALE | Google: Q2 and Q3, and whether the landing page still loads and has the tag (fetch the final URL and look for `gtag`/`GTM-`). Meta: `adspixels?fields=name,last_fired_time`, and the ad sets' `optimization_goal`/`promoted_object`. If the client has a GTM container, check the live version's tags. |
| NOTHING_DELIVERING, SOME_NOT_DELIVERING, ACTIVE_NOT_SPENDING, STOPPED | Q1 (`primary_status`, `primary_status_reasons`), Q4 (disapprovals), Q6 (billing), Q5 (who paused what). Meta: account `account_status`/`disable_reason`, ads' `effective_status` and `issues_info`. |
| BILLING, RUNNING_OUT | Google Q6. Meta: `account_status` (1 active, 2 disabled, 3 unsettled, 9 grace period), `spend_cap` vs `amount_spent`, `funding_source_details`. Billing fixes are done by a person in the UI: say what's needed. |
| DISAPPROVED | Q4, with the policy topic. Propose replacement copy that fixes the policy issue. |
| BUDGET_LIMITED, UNDER_DELIVERY, OVER_DELIVERY, SPEND_SWING | Q1 (budget, lost IS), Q8 (daily trend), Q5 (budget edits). Express any budget suggestion as a daily and monthly figure (×30.4). |
| CANCELED_SPENDING, META_ON_GOOGLE_OFF, BUDGET_RULE_STUCK | Q1 and Q5 to see what is live and who changed it last. This usually needs a person to confirm the client status, so ask rather than diagnose. |
| CTR_DROP, CPC_UP, WEAK_GOALS, NO_LEAD_TRACKING, ONLY_PAGE_VISITS | Q3 for goals; Q7 and Q1 for auction and match-type drift. Usually a 🟠/🟡 recommendation, not an urgent fix. |
| FREQUENCY, CREATIVE_OLD, LEARNING_LIMITED | Meta `insights` (frequency, last 7 days), `ads?fields=created_time,effective_status`, `adsets?fields=learning_stage_info,optimization_goal`. |
| OWNER_MISMATCH, UNASSIGNED, NEGLECT | No live check needed: say who should look and offer to note it. |

### Google Ads queries

```sql
-- Q1 delivery and budget (enabled campaigns, last 7 days)
SELECT campaign.name, campaign.status, campaign.primary_status, campaign.primary_status_reasons,
       campaign.bidding_strategy_type, campaign_budget.amount_micros, metrics.impressions,
       metrics.clicks, metrics.cost_micros, metrics.search_budget_lost_impression_share
FROM campaign WHERE campaign.status = 'ENABLED' AND segments.date DURING LAST_7_DAYS

-- Q2 conversions by action (last 30 days)
SELECT segments.conversion_action_name, segments.conversion_action_category,
       metrics.all_conversions, metrics.conversions
FROM campaign WHERE segments.date DURING LAST_30_DAYS AND metrics.all_conversions > 0

-- Q3 goal setup
SELECT conversion_action.name, conversion_action.type, conversion_action.category,
       conversion_action.primary_for_goal
FROM conversion_action WHERE conversion_action.status = 'ENABLED'

-- Q4 disapproved ads in live campaigns
SELECT campaign.name, ad_group.name, ad_group_ad.ad.id, ad_group_ad.policy_summary.policy_topic_entries
FROM ad_group_ad
WHERE ad_group_ad.policy_summary.approval_status = 'DISAPPROVED' AND campaign.status = 'ENABLED'
  AND ad_group.status = 'ENABLED' AND ad_group_ad.status = 'ENABLED'

-- Q5 recent changes (the API keeps 30 days; needs a date filter and a LIMIT)
SELECT change_event.change_date_time, change_event.user_email, change_event.change_resource_type,
       change_event.resource_change_operation, change_event.changed_fields, campaign.name
FROM change_event WHERE change_event.change_date_time DURING LAST_14_DAYS
ORDER BY change_event.change_date_time DESC LIMIT 50

-- Q6 billing / budget orders
SELECT account_budget.status, account_budget.approved_end_date_time,
       account_budget.approved_spending_limit_micros, account_budget.amount_served_micros
FROM account_budget

-- Q7 top search terms by cost (last 14 days)
SELECT search_term_view.search_term, segments.search_term_match_type, metrics.clicks,
       metrics.cost_micros, metrics.conversions
FROM search_term_view WHERE segments.date DURING LAST_14_DAYS
ORDER BY metrics.cost_micros DESC LIMIT 50

-- Q8 daily trend (days with no activity are omitted)
SELECT segments.date, metrics.cost_micros, metrics.clicks, metrics.conversions
FROM customer WHERE segments.date DURING LAST_30_DAYS
```

Money fields are micros: divide by 1,000,000 and show the account currency.

## 4. Report

Lead with a summary line ("Sara: 2 🔴, 22 🟠. Sheet refreshed 14 Oct 07:29 GMT+8."), then one block per account, most urgent first:

```
### 🔴 PP4956 - Lightwood Dental (Google 316-641-4805, Australia/Sydney, AUD)
Flag: NO_LEADS, 27 days, AUD 791 spent since (open 12 days)
Cause (likely): ...evidence with numbers and dates...
Proposed next step: ...
Proposed change (not applied): Campaign "X" (123) · field · before → after · daily/monthly effect
Needs a person: ...anything Claude can't do (billing, asking the clinic, UI-only settings)
```

Keep each block short. Put long evidence (search term lists, change histories) underneath or offer it on request.

End with a short to-do list by urgency, and offer to: apply any proposed change (after approval, following CLAUDE.md), add findings to the client's notes, or snooze a flag on the sheet's Owners & Notes tab (an edit to a live sheet: preview first).

## Rules that apply here

- **Nothing is changed during the check.** Proposed changes follow the normal CLAUDE.md flow: preview, approval, apply, log in `logs/changes/`, push to `main`.
- **No Slack or email.** The bot already sends the daily list. Draft a message only if asked.
- **Write down what you learn.** If the diagnosis is new and worth remembering (a tracking quirk, a decision, why a flag is expected), offer to add a dated line to the client's `notes.md`, creating it from `accounts/README.md` if missing. That's how tomorrow's check gets faster.
- **No patient data** in notes, logs or output. WhatConverts lead details can include names and call content: summarise by count, date, source and outcome only.
- **Big books:** with more than ~10 accounts to investigate, do a fast pass (sheet data plus Q1/Q2 or the Meta account status) on all of them first, show the list, and ask which to dig into.
