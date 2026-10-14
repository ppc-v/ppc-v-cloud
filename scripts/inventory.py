#!/usr/bin/env python3
"""Read the Vortala Ad Account Inventory sheet (config/accounts.md) and print accounts or issues as a table or JSON.

Examples:
  python3 scripts/inventory.py                              # every account in the active book, most urgent first
  python3 scripts/inventory.py --owner John --level orange  # John's 🔴 and 🟠 accounts
  python3 scripts/inventory.py --issues --owner Sara        # Sara's open (not snoozed) issues, one row per problem
  python3 scripts/inventory.py --account PP5416 --json      # every column for one account
"""

import argparse
import json
import os
import sys

import requests

SHEET_ID = "1PHkhNJ6GHoAoKRtB-XyeaJFqnJbs00OzGZpNlMF6GwQ"
TIMEOUT = 30
# Header row and first data row of each tab (rows above are the refresh banner and column help).
TABS = {"Accounts": 4, "Issues": 2}
LEVELS = {"red": ["🔴"], "orange": ["🔴", "🟠"], "yellow": ["🔴", "🟠", "🟡"], "all": ["🔴", "🟠", "🟡", "🟢"]}
ACCOUNT_COLS = ["Health", "Account", "Top issue", "Owner", "Platform", "Client status", "Spend this month",
                "Leads (7d)", "Days since last lead", "Last touched", "Ad account ID", "Timezone"]
ISSUE_COLS = ["Level", "Owner", "Account", "Platform", "Issue", "Suggested next step", "Days open", "Status", "Flag code"]


def access_token():
    resp = requests.post(
        "https://oauth2.googleapis.com/token",
        data={
            "client_id": os.environ["GOOGLE_ADS_CLIENT_ID"],
            "client_secret": os.environ["GOOGLE_ADS_CLIENT_SECRET"],
            "refresh_token": os.environ["GOOGLE_ADS_REFRESH_TOKEN"],
            "grant_type": "refresh_token",
        },
        timeout=TIMEOUT,
    )
    resp.raise_for_status()
    return resp.json()["access_token"]


def read_tab(token, tab):
    resp = requests.get(
        f"https://sheets.googleapis.com/v4/spreadsheets/{SHEET_ID}/values/'{tab}'!A1:BZ2000",
        headers={"Authorization": f"Bearer {token}"},
        timeout=TIMEOUT,
    )
    resp.raise_for_status()
    rows = resp.json().get("values", [])
    header_row = TABS[tab]
    banner = rows[0][0] if rows and rows[0] else ""
    header = rows[header_row - 1]
    records = [dict(zip(header, r + [""] * (len(header) - len(r)))) for r in rows[header_row:] if any(r)]
    return banner, records


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--issues", action="store_true", help="read the Issues tab instead of Accounts")
    p.add_argument("--owner", help="Sara, John, Arif or Unassigned")
    p.add_argument("--level", choices=LEVELS, default="all", help="red = 🔴 only, orange = 🔴+🟠, yellow = 🔴+🟠+🟡")
    p.add_argument("--account", help="PP number, ad account ID or part of the name")
    p.add_argument("--platform", choices=["Google", "Meta"])
    p.add_argument("--include-snoozed", action="store_true", help="with --issues, also show snoozed issues")
    p.add_argument("--json", action="store_true", help="every column, as JSON")
    args = p.parse_args()

    tab = "Issues" if args.issues else "Accounts"
    banner, records = read_tab(access_token(), tab)
    level_col = "Level" if args.issues else "Health"
    wanted = LEVELS[args.level]

    def keep(r):
        if not any(r.get(level_col, "").startswith(e) for e in wanted):
            return False
        if args.owner and r.get("Owner", "").lower() != args.owner.lower():
            return False
        if args.issues and not args.include_snoozed and r.get("Status", "").startswith("Snoozed"):
            return False
        if args.platform and r.get("Platform") != args.platform:
            return False
        if args.account:
            needle = args.account.lower()
            hay = (r.get("Account", "") + " " + r.get("Ad account ID", "")).lower()
            if needle not in hay and needle.replace("-", "") not in hay.replace("-", ""):
                return False
        return True

    records = [r for r in records if keep(r)]
    if args.json:
        json.dump({"refreshed": banner, "rows": records}, sys.stdout, ensure_ascii=False, indent=1)
        print()
        return
    cols = ISSUE_COLS if args.issues else ACCOUNT_COLS
    print(banner)
    print(f"{len(records)} {tab.lower()} matched\n")
    print("| " + " | ".join(cols) + " |")
    print("|" + "---|" * len(cols))
    for r in records:
        print("| " + " | ".join(r.get(c, "").replace("\n", " / ").replace("|", "/") for c in cols) + " |")


if __name__ == "__main__":
    main()
