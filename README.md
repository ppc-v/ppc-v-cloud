# ppc-v-cloud

Vortala PPC team's shared Claude workspace for Google Ads, Meta, GTM/GA4, WhatConverts, reporting and creative. The full working rules are in [`CLAUDE.md`](CLAUDE.md); Claude reads them at the start of every session.

## Getting started
1. Start a new session on this repository at claude.ai/code (shared paidsearch@ login).
2. Begin your first message with your name or initials, e.g. `SS: pull last 7 days of leads for PP5416`. Claude tags commits and change logs with them.
3. Ask in plain English. Mention the PP number or account name so Claude can find the right account.

## What to expect
- **Nothing changes without your approval.** Claude shows a preview (account, entity, before → after) and waits for a yes. Budget and bid changes include the daily and monthly effect. Batches across several accounts: you choose one approval or one per account.
- **New campaigns, ad sets, ad groups and asset groups are created paused.** You switch them on.
- **GTM:** changes go into a workspace first; publishing a version is a separate approval.
- **No outbound messages** (Slack, email, Page posts, client messages) unless you ask for that specific message. Drafts are fine.
- **Healthcare data:** no health conditions, treatment details or patient identifiers go to ad platforms or into this repo.
- Performance dates use each ad account's own timezone.

## Where things live
| Path | What |
|---|---|
| `CLAUDE.md` | Team rules, team list, change process |
| `config/accounts.md` | MCC, Meta portfolio, and the Ad Account Inventory sheet (master client list) |
| `config/credentials.md` | Which API keys exist and how to renew them (names only, never values) |
| `accounts/<pp-number>-<client>/notes.md` | What Claude remembers about each client: access level, preferences, history |
| `logs/changes/` | One log per applied change batch: who asked, who approved, before → after |

## If something isn't working
Ask Claude to run `python3 scripts/check_connections.py`. It reports which connections (Google Ads, GTM, GA4, Search Console, Drive, the inventory sheet, Meta, WhatConverts) work, without printing any secrets. Keys live in the cloud environment's settings; after changing one, start a fresh session.

Several people push to `main` at the same time, so Claude pulls before every push. If you see a conflict message, let Claude resolve it.
