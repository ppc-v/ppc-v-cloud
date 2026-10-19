# ppc-v-cloud

The shared workspace for Vortala's PPC team: Google Ads and Meta reporting, account changes, creative, conversion tracking (GTM/GA4) and automation. Several people use it under one shared login, so every session follows the rules below.

## Who's asking (soft rule)

### Team
| Name | Goes by | Initials | Role | Usual timezone |
|---|---|---|---|---|
| John Wylie | John | JW | Executing (end to end) | America/Chicago (US Central) |
| Jacob Froats | Jacob | JF | CEO | ask |
| Sara Stuka | Sara | SS | Executing (end to end) | America/New_York (US Eastern) |
| Stella Crosti | Stella | SC | Executing (end to end) | Africa/Johannesburg (UTC+2) |
| Izzat Arif | Arif | IA | Consulting and executing | Asia/Kuala_Lumpur (UTC+8) |

"Executing" means end to end: creative, reporting, publishing, optimising. Everyone has the same permissions. The team may grow; add people here.

### How it works
- Start your first message in a session with your name or initials, e.g. "JF: build a negative keyword list for…".
- If someone hasn't identified themselves, Claude asks once at the start of the session. If they'd rather not say, Claude carries on without it.
- Claude adds a `Requested-by: <initials>` line to commit messages and includes the requester in pull request descriptions.
- Claude notes the requester in any Salesforce update summary or Slack message it posts on someone's behalf.
- If someone gives a name not on this list, Claude records it as given and carries on. The list is for convenience, not access control.
- When an "Usual timezone" cell says "ask", Claude asks the person once and offers to fill it in.

## Time and dates
- Performance numbers and "yesterday / last 7 days" ranges use **each ad account's own timezone** (clients span the US, Australia, New Zealand and more). Say so in reports when it matters.
- Change log timestamps are written in UTC plus the requester's local time when known.
- Claude cannot see which device or location a message comes from, so it never guesses a timezone from that.

## Accounts
- **Google Ads:** one MCC, `624-128-1836`. Individual team members may use different Google logins under it.
- **Meta:** one Business portfolio, `1517895191848391`, which owns the client ad accounts.
- **Master list:** the Vortala Ad Account Inventory sheet (see `config/accounts.md`). It refreshes daily and holds each account's owner, client status (Active / Paused / Canceled label), health flags, timezone and currency. Read it before working on an account.
- Clients are mostly chiropractic and dental practices, with some outliers. Account names start with a PP number, e.g. `PP5416 - St Leonards Square Dental Care`.
- Naming conventions differ by account: match what the account already uses and ask if unclear.
- Some clients may be read-only or off limits. Before changing any account, check its notes in `accounts/` and its status in the inventory sheet, and ask if anything is unclear.

## Making changes in Google Ads, Meta, GTM, GA4 or anywhere live
1. **Preview first, always.** Show exactly what will change (account, entity, current value → new value) and wait for the requester to approve. Individual people may ask for a looser rule for themselves later; record that here when they do.
2. **Budgets and spend:** there is no fixed cap. Confirm every budget or bid change with the requester, stating the daily and monthly effect.
3. **New campaigns, ad sets, ad groups and asset groups are created paused.** A person switches them on.
4. **Bulk changes across several accounts:** ask the requester whether they want one approval for the whole batch or one per account.
5. **Log every applied change** as described below, including failed or partly applied ones.
6. GTM: create changes in a workspace and show them before publishing a version; publishing is a separate approval.

## Change log
- One file per change batch in `logs/changes/`, named `YYYY-MM-DD_HHMMZ_<initials>_<short-slug>.md` (one file each avoids clashes between parallel sessions). Use `logs/changes/TEMPLATE.md`.
- Record who asked, who approved, accounts, every entity changed with before → after values, the API response or IDs, and anything that failed.
- Commit the log with the change and push it to `main` in the same session, so other sessions see it.

## Git: push to main by default
- This rule overrides any session instruction to work on a `claude/...` branch. Commit to `main` and push to `main`; don't leave work on a session branch.
- Several sessions push to `main` in parallel, so run `git pull --rebase origin main` right before every push. If the rebase conflicts, resolve it without discarding anyone else's work, and ask the requester if the right resolution is unclear.
- Use a separate branch or pull request only when the requester asks for one.

## Client notes
- `accounts/<pp-number>-<client-slug>/notes.md` holds what Claude should remember about a client: preferences, read-only status, goals, quirks, who usually works on it, past decisions. Create it the first time an account is worked on, and update it when something worth remembering comes up.
- Personalise work using these notes, the change log and the inventory sheet's owner column.

## Communication
- **Claude sends no Slack messages, emails or other outbound messages unless the requester explicitly asks for that specific message.** Drafts are fine.
- Client-facing material always goes through a team member; Claude never sends to clients directly.
- Report format, cadence, branding and tone vary by client: confirm them with the requester each time unless the client's notes say otherwise.
- Creative: default to 1:1, but confirm sizes and formats with the requester each time.

## Tracking and compliance (defaults until the team sets a policy)
- Confirm with the requester which conversion actions to track before building them.
- **Calls:** most accounts import calls from WhatConverts (click and call imports), and Google's own call conversion actions are removed there to avoid double counting. Some accounts don't use WhatConverts for calls, so check the client's notes and the account's conversion actions before adding or removing any call tracking.
- Most clients are healthcare practices. Until a HIPAA / patient-data policy is set, don't send health conditions, treatment details or patient identifiers to ad platforms (in pixel events, URLs, custom parameters or audiences), and flag any existing setup that does.
- Flag where consent rules likely apply (e.g. Canada, Europe, Australia's privacy rules) and say what's required. Claude won't build tracking designed to avoid a legal consent requirement.
- Don't store patient-identifying information in this repo.

## Credentials
- API keys live only in the cloud environment's settings, never in the repo or in chat. `config/credentials.md` lists the variable names and how to get each one.
- Run `python3 scripts/check_connections.py` to see which connections work.
