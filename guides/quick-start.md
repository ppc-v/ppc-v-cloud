# Quick start: working with Claude

One page to get going. The full rules are in [`CLAUDE.md`](../CLAUDE.md); example prompts are in the [prompt playbook](prompt-playbook.md).

## Start a session
1. Go to claude.ai/code (shared paidsearch@ login) and start a new session on **ppc-v/ppc-v-cloud**.
2. Start your first message with your initials: `JW:`, `SS:`, `SC:`, `IA:`, `JF:`.
3. Name the account by PP number (`PP5416`) or ad account ID. Claude looks it up in the inventory sheet and reads the client's notes.

One task per session works best. Start a new session for an unrelated job; sessions run in parallel without getting in each other's way.

## What you can ask for
| You want | Say something like |
|---|---|
| Your daily to-do list | `SS: daily health check` |
| Why an account is flagged | `JW: why is PP5416 showing no leads?` |
| Numbers | `SC: last 30 days vs previous 30 for PP4956, leads and CPL` |
| A change | `JW: raise the budget on PP5416 to AUD 100/day` |
| Creative or copy | `SS: 5 Meta primary texts for PP1654's sports injury ad set, 1:1` |
| Tracking | `IA: audit conversion tracking on PP0519` |

## How changes work
1. **Claude previews first:** account, what changes, current value → new value. Budget and bid changes show the daily and monthly effect.
2. **You approve** ("yes", "go", "approved"). Nothing live changes without it.
3. **Claude applies it, logs it** in `logs/changes/` and pushes the log to `main`.

Good to know:
- New campaigns, ad sets, ad groups and asset groups are created **paused**. You switch them on.
- For changes across several accounts, Claude asks whether you want one approval for the batch or one per account.
- GTM changes go into a workspace; publishing is a separate approval.
- Claude doesn't send Slack messages or emails unless you ask for that specific message, and never sends anything to clients.

## Make Claude better at your clients
When you learn something about a client (they hate broad match, the owner wants reports on Mondays, the booking widget breaks tracking), say **"add that to the notes"**. It goes in `accounts/<pp>-<client>/notes.md`, and every future session reads it, whoever is asking.

## Things Claude won't do
- Send health conditions, treatment details or patient identifiers to ad platforms, or store them in the repo.
- Build tracking that avoids a consent requirement (Canada, EU, Australia/NZ privacy rules).
- Guess your timezone. Performance dates use each ad account's own timezone.

## If something breaks
- Say `check connections`. Claude runs `scripts/check_connections.py` and tells you what's down.
- A conflict message when pushing: let Claude resolve it. Several people push at once; that's expected.
- An answer looks wrong: ask "how did you get that number?" Claude shows its query and date range.
