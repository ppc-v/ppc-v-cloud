---
name: budget-pacing
description: Monthly budget pacing across the team's Google Ads and Meta accounts. Compares live month-to-date spend (each account's own timezone) with the client's monthly budget in Salesforce, projects month end, flags accounts that will hit their cap early and go dark (the team's budget rule pauses them) or will underspend, and proposes daily budget changes as a preview. Use when someone asks about pacing, budget pacing, spend vs budget, month-to-date spend, "will we hit budget", "who's overspending/underspending", projected month end, or what daily budget an account needs.
---

# Budget pacing

## How budgets work at Vortala (read first)

- **The monthly budget lives in Salesforce:** `Paid_Advertising_Project__c.Adwords_Monthly_Budget__c` (Google) and `Facebook_Ad_Budget__c` (Meta), keyed by `Account_Number__c` (the PP number) and `Adwords_ID__c`.
- **The team's Google Ads "Bulk Actions" automated rule pauses an account once the month's budget is spent** and restarts it on the 1st. Last month most accounts spent within a few percent of their Salesforce budget, so treat that figure as the cap. Overspending therefore rarely means going over budget; it means the **budget runs out early and the ads go dark** for the rest of the month. The inventory sheet shows rule-paused accounts as "ℹ️ Monthly budget reached".
- The rule isn't readable through the API, so if the rule's threshold and Salesforce disagree, Salesforce can be wrong. Spend last month far from the Salesforce budget is a hint.
- Pacing runs on the **calendar month** (the rule resets on the 1st). Salesforce's "billing day" is shown for reference only. If a requester wants billing-cycle pacing for a client, do it by hand and note it in the client's notes.
- Meta has no budget rule. Meta accounts may use spend caps or lifetime budgets; the script notes lifetime budgets it can't count.

## 1. Get the budgets from Salesforce

There is no Salesforce API key in the environment, so use the Salesforce connector (`soqlQuery`):

```bash
python3 scripts/pacing.py --soql --owner <Name>   # prints the SOQL for the accounts in scope (drop --owner for everyone)
```

Run that query with the connector. Save the records to a scratch file as a JSON list, keeping only these keys (drop `attributes` and null fields to keep it short): `Account_Number__c, Adwords_ID__c, Adwords_Monthly_Budget__c, Adword_Billing_Date__c, Facebook_Ad_Budget__c, Facebook_Billing_Date__c, Budget_Type__c, CurrencyIsoCode, Adwords_Cancellation_Date__c, Facebook_Cancellation_Date__c`. Use the session's scratchpad directory, not the repo.

Never read or output `Google_Password__c` or `Google_Username__c` from that object.

## 2. Run the pacing

```bash
python3 scripts/pacing.py --budgets <file> [--owner Sara] [--platform Google|Meta] [--account PP5416] [--json]
```

It takes about 20 seconds for the whole book. Spend is through **yesterday** in each account's own timezone; "Today so far" is separate.

| Status | Meaning | Usual action |
|---|---|---|
| Spending after cancellation | Salesforce has a cancellation date but the account spent this month | Confirm with the requester: wrong Salesforce record, or ads that should be off? |
| Runs out early | At the 7-day run rate the budget is gone before month end ("Runs out on", "Dark days") | Lower daily budgets to "Needed per day", or confirm front-loading is intended |
| Budget reached | Month-to-date spend ≥ budget | Check the rule paused it (a note appears if it's still spending today) |
| Under | Projected month end < 90% of budget | Find out why (budget-limited? low search volume? disapprovals? paused campaigns?) before raising budgets |
| On track | Neither | Nothing |
| No budget / implied | No Salesforce budget; judged against daily budgets × days in month | Ask the owner for the budget; offer to note it in the client's notes |
| Error | API error for that account | Report it; `check_connections.py` if many |

Notes flag currency mismatches (Salesforce budget in a different currency from the ad account), Meta "Dates Specified" budgets, lifetime budgets and duplicate Salesforce projects. Don't pace across a currency mismatch: ask which figure is right.

## 3. Report

Lead with one line per status count and the date basis, then a table of the accounts that need action, worst first:

| Account | Owner | Budget | MTD | Projected | Runs out | Dark days | Avg/day (7d) | Daily budget now | Needed/day |
|---|---|---|---|---|---|---|---|---|---|

All money is in the account's currency (say which). Mention the timezone when it matters. For "Under" accounts, check `Searches lost to budget (7d)`, `Not delivering` and the flags in the inventory sheet (`python3 scripts/inventory.py --account <PP> --json`) so you don't recommend raising budgets on an account that is under-delivering for another reason.

## 4. Proposed changes (preview only)

When the requester wants to fix pacing, build the preview from the live campaign budgets:

```sql
SELECT campaign.id, campaign.name, campaign.status, campaign_budget.id, campaign_budget.name,
       campaign_budget.amount_micros, campaign_budget.explicitly_shared, metrics.cost_micros
FROM campaign
WHERE campaign.status = 'ENABLED' AND segments.date DURING LAST_7_DAYS
```

- Split the new account-level daily figure across campaigns in proportion to their recent spend, unless the requester or the client notes say otherwise. Shared budgets count once.
- Show account, campaign, budget name and ID, current daily → new daily, and the **daily and monthly effect** (×30.4, and to month end: new daily × days left).
- Meta: change at the level the budget sits (campaign for CBO, otherwise ad set). Amounts in the API are in cents for most currencies.
- For many accounts, ask whether the requester wants one approval for the batch or one per account (CLAUDE.md).
- After approval: apply, verify by reading the budgets back, log in `logs/changes/` (before → after per budget), push to `main`.

Never change the Bulk Actions rule or Salesforce budgets from this skill. If Salesforce looks wrong, say so and let a person fix it, or draft the correction for their approval.
