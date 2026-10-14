#!/usr/bin/env python3
"""Monthly budget pacing: live month-to-date spend (Google Ads, Meta) against each client's monthly budget in Salesforce.

Accounts come from the inventory sheet (Spend status Active, or client status Active). Spend and dates use each ad
account's own timezone; month to date runs from the 1st through yesterday, so a part day doesn't skew the pace.

Salesforce has no API key in this environment, so budgets are passed in as a file:
  1. python3 scripts/pacing.py --soql [--owner Sara]   # prints the SOQL to run with the Salesforce connector
  2. save the connector's JSON response (or just its "records" list) to a file
  3. python3 scripts/pacing.py --budgets <file> [--owner Sara] [--platform Google] [--account PP5416] [--json]
Without --budgets, pacing is judged against the current daily budgets × days in month ("implied" budget).

The Salesforce budget is the monthly cap the team's Google Ads "Bulk Actions" rule enforces (last month most accounts
spent within a few % of it), so over-pacing is reported as the date the budget runs out and the days left dark.
"""

import argparse
import calendar
import json
import os
import re
import sys
from concurrent.futures import ThreadPoolExecutor
from datetime import date, datetime, timedelta
from zoneinfo import ZoneInfo

import requests

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import inventory  # noqa: E402

TIMEOUT = 30
META_API = "https://graph.facebook.com/v26.0"
# Meta reports budgets in the currency's smallest unit; these currencies have no minor unit.
META_NO_MINOR_UNIT = {"CLP", "COP", "CRC", "HUF", "ISK", "IDR", "JPY", "KRW", "PYG", "TWD", "VND"}
UNDER = 0.90  # projected month end below this share of budget counts as under-pacing
# The team's "Bulk Actions" rule pauses a Google account once the month's budget is spent, so over-pacing shows up as
# days with no ads at the end of the month. Flag it from this many dark days.
DARK_DAYS = 2
SF_FIELDS = ("Account_Number__c, Name, Adwords_ID__c, Adwords_Monthly_Budget__c, Adword_Billing_Date__c, "
             "Facebook_Ad_Budget__c, Facebook_Billing_Date__c, Budget_Type__c, CurrencyIsoCode, "
             "Adwords_Cancellation_Date__c, Facebook_Cancellation_Date__c")


def pp_number(name):
    m = re.match(r"\s*(PP\d+)", name or "", re.I)
    return m.group(1).upper() if m else None


def digits(s):
    return re.sub(r"\D", "", s or "")


def in_scope(r, args):
    # Meta rows show the Google account's label, so for Meta only actual spend puts it in scope.
    live = r.get("Spend status") == "Active" or (r.get("Platform") == "Google" and r.get("Client status") == "Active")
    return (live
            and (not args.owner or r.get("Owner", "").lower() == args.owner.lower())
            and (not args.platform or r.get("Platform") == args.platform)
            and (not args.account or args.account.lower() in (r["Account"] + " " + r["Ad account ID"]).lower()
                 or digits(args.account) and digits(args.account) == digits(r["Ad account ID"])))


def load_budgets(path):
    data = json.load(open(path))
    records = data.get("records", data) if isinstance(data, dict) else data
    by_google, by_pp = {}, {}
    for rec in records:
        if digits(rec.get("Adwords_ID__c")):
            by_google.setdefault(digits(rec["Adwords_ID__c"]), []).append(rec)
        if rec.get("Account_Number__c"):
            by_pp.setdefault(pp_number(rec["Account_Number__c"]) or rec["Account_Number__c"].upper(), []).append(rec)
    return by_google, by_pp


def budget_for(row, by_google, by_pp):
    """Return (monthly budget, billing day, note) from Salesforce for an inventory row."""
    google = row["Platform"] == "Google"
    field, bill, cancel = (("Adwords_Monthly_Budget__c", "Adword_Billing_Date__c", "Adwords_Cancellation_Date__c") if google
                           else ("Facebook_Ad_Budget__c", "Facebook_Billing_Date__c", "Facebook_Cancellation_Date__c"))
    recs = (by_google.get(digits(row["Ad account ID"])) if google else None) or by_pp.get(pp_number(row["Account"]), [])
    recs = [r for r in recs if r.get(field)]
    if not recs:
        return None, "", "no budget in Salesforce"
    if len(recs) > 1:
        return None, "", f"{len(recs)} Salesforce projects with a budget: check which applies"
    rec, notes = recs[0], []
    if rec.get(cancel):
        notes.append(f"CANCELLED in Salesforce {rec[cancel]}")
    if rec.get("CurrencyIsoCode") and rec["CurrencyIsoCode"] != row.get("Currency"):
        notes.append(f"Salesforce budget is in {rec['CurrencyIsoCode']}, account in {row.get('Currency')}")
    if not google and rec.get("Budget_Type__c") == "Dates Specified":
        notes.append("Meta budget is for specified dates, not monthly")
    return float(rec[field]), rec.get(bill) or "", "; ".join(notes)


def google_spend(client, cid, start, today):
    svc = client.get_service("GoogleAdsService")
    rows = svc.search(customer_id=cid, query=(
        "SELECT segments.date, metrics.cost_micros FROM customer "
        f"WHERE segments.date BETWEEN '{start}' AND '{today}'"))
    daily = {r.segments.date: r.metrics.cost_micros / 1e6 for r in rows}
    budgets = {}
    for r in svc.search(customer_id=cid, query=(
            "SELECT campaign_budget.resource_name, campaign_budget.amount_micros FROM campaign "
            "WHERE campaign.status = 'ENABLED' AND campaign.serving_status != 'ENDED'")):
        budgets[r.campaign_budget.resource_name] = r.campaign_budget.amount_micros / 1e6  # shared budgets count once
    return daily, sum(budgets.values()), ""


def meta_get(path, **params):
    resp = requests.get(f"{META_API}/{path}", params={"access_token": os.environ["META_ACCESS_TOKEN"], **params},
                        timeout=TIMEOUT)
    resp.raise_for_status()
    return resp.json()


def meta_spend(act, start, today, currency):
    ins = meta_get(f"act_{act}/insights", fields="spend", time_increment=1, limit=100,
                   time_range=json.dumps({"since": str(start), "until": str(today)}))
    daily = {d["date_start"]: float(d["spend"]) for d in ins.get("data", [])}
    unit = 1 if currency in META_NO_MINOR_UNIT else 100
    total, lifetime = 0.0, 0
    camps = meta_get(f"act_{act}/campaigns", fields="daily_budget,lifetime_budget", limit=200,
                     effective_status='["ACTIVE"]').get("data", [])
    for c in camps:
        if c.get("daily_budget"):
            total += int(c["daily_budget"]) / unit
        elif c.get("lifetime_budget"):
            lifetime += 1
    if any(not c.get("daily_budget") and not c.get("lifetime_budget") for c in camps):  # ad set budgets
        for s in meta_get(f"act_{act}/adsets", fields="daily_budget,lifetime_budget", limit=500,
                          effective_status='["ACTIVE"]').get("data", []):
            if s.get("daily_budget"):
                total += int(s["daily_budget"]) / unit
            elif s.get("lifetime_budget"):
                lifetime += 1
    return daily, total, f"{lifetime} lifetime budget(s) not counted in daily budget" if lifetime else ""


def pace(row, budget, bill_day, sf_note, client):
    tz_note = ""
    try:
        tz = ZoneInfo(row.get("Timezone") or "UTC")
    except Exception:  # noqa: BLE001
        tz, tz_note = ZoneInfo("UTC"), f"unknown timezone {row.get('Timezone')!r}: dates in UTC"
    today = datetime.now(tz).date()
    month_start, dim = today.replace(day=1), calendar.monthrange(today.year, today.month)[1]
    yesterday = today - timedelta(days=1)
    start = min(month_start, today - timedelta(days=7))
    out = {"Account": row["Account"], "Owner": row["Owner"], "Platform": row["Platform"],
           "Ad account ID": row["Ad account ID"], "Currency": row.get("Currency", ""),
           "Timezone": row.get("Timezone", ""), "Billing day": bill_day, "Notes": [n for n in [sf_note, tz_note] if n]}
    try:
        if row["Platform"] == "Google":
            daily, daily_budget, note = google_spend(client, digits(row["Ad account ID"]), start, today)
        else:
            daily, daily_budget, note = meta_spend(row["Ad account ID"], start, today, row.get("Currency"))
    except Exception as e:  # noqa: BLE001
        failure = getattr(e, "failure", None)
        out["Status"] = "Error"
        out["Notes"].append(("; ".join(x.message for x in failure.errors) if failure else str(e))[:200])
        return out
    if note:
        out["Notes"].append(note)

    elapsed = (yesterday - month_start).days + 1 if today.day > 1 else 0  # full days so far this month
    remaining = dim - elapsed  # includes today
    mtd = sum(v for d, v in daily.items() if month_start <= date.fromisoformat(d) <= yesterday)
    last7 = sum(v for d, v in daily.items() if today - timedelta(days=7) <= date.fromisoformat(d) <= yesterday) / 7
    implied = budget is None
    if implied:
        budget = daily_budget * dim
        out["Notes"].append("no Salesforce budget: judged against daily budgets × days in month")
    projected = mtd + last7 * remaining
    out.update({
        "Monthly budget": round(budget, 2), "Budget source": "implied" if implied else "Salesforce",
        "Spend MTD": round(mtd, 2), "Today so far": round(daily.get(str(today), 0.0), 2),
        "Expected MTD": round(budget * elapsed / dim, 2), "Avg daily (7d)": round(last7, 2),
        "Daily budget now": round(daily_budget, 2), "Projected month end": round(projected, 2),
        "Needed per day": round(max(budget - mtd, 0) / remaining, 2) if remaining else 0,
        "Days left": remaining, "As of": f"{today} (through {yesterday})",
    })
    share = projected / budget if budget else None
    out["Projected % of budget"] = round(share * 100) if share is not None else None
    dark = 0
    if budget and last7 > 0 and mtd < budget:
        days_to_cap = (budget - mtd) / last7  # counted from the start of today
        if days_to_cap < remaining:
            dark = round(remaining - days_to_cap)
            out["Runs out on"] = str(today + timedelta(days=int(days_to_cap)))
    out["Dark days"] = dark
    if any(n.startswith("CANCELLED") for n in out["Notes"]):
        out["Status"] = "Spending after cancellation" if mtd or out["Today so far"] else "Cancelled"
    elif not budget:
        out["Status"] = "No budget"
    elif mtd >= budget:
        out["Status"] = "Budget reached"
        if out["Today so far"]:
            out["Notes"].append("still spending today: check the budget rule paused it")
    elif elapsed == 0:
        out["Status"] = "Month just started"
    elif dark >= DARK_DAYS:
        out["Status"] = "Runs out early"
    elif share < UNDER:
        out["Status"] = "Under"
    else:
        out["Status"] = "On track"
    return out


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--soql", action="store_true", help="print the Salesforce query for the accounts in scope, then exit")
    p.add_argument("--budgets", help="Salesforce JSON (connector response or list of records)")
    p.add_argument("--owner")
    p.add_argument("--platform", choices=["Google", "Meta"])
    p.add_argument("--account", help="PP number, ad account ID or part of the name")
    p.add_argument("--json", action="store_true")
    args = p.parse_args()

    banner, rows = inventory.read_tab(inventory.access_token(), "Accounts")
    rows = [r for r in rows if in_scope(r, args)]
    if args.soql:
        pps = sorted({pp_number(r["Account"]) for r in rows} - {None})
        print(f"SELECT {SF_FIELDS} FROM Paid_Advertising_Project__c "
              f"WHERE Account_Number__c IN ({', '.join(repr(x) for x in pps)})")
        return
    by_google, by_pp = load_budgets(args.budgets) if args.budgets else ({}, {})

    client = None
    if any(r["Platform"] == "Google" for r in rows):
        from google.ads.googleads.client import GoogleAdsClient
        os.environ.setdefault("GOOGLE_ADS_USE_PROTO_PLUS", "true")
        client = GoogleAdsClient.load_from_env()

    def one(r):
        budget, bill, note = budget_for(r, by_google, by_pp) if args.budgets else (None, "", "")
        return pace(r, budget, bill, note, client)

    with ThreadPoolExecutor(8) as ex:
        results = list(ex.map(one, rows))
    order = {"Error": 0, "Spending after cancellation": 0, "Runs out early": 1, "Budget reached": 2, "Under": 3, "No budget": 4, "Month just started": 5, "On track": 6, "Cancelled": 7}
    results.sort(key=lambda x: (order.get(x["Status"], 9), -x.get("Dark days", 0),
                                -abs((x.get("Projected % of budget") or 100) - 100)))

    if args.json:
        json.dump({"inventory": banner, "accounts": results}, sys.stdout, ensure_ascii=False, indent=1)
        print()
        return
    cols = ["Status", "Account", "Owner", "Platform", "Currency", "Monthly budget", "Budget source", "Spend MTD",
            "Expected MTD", "Projected month end", "Projected % of budget", "Runs out on", "Dark days", "Avg daily (7d)",
            "Daily budget now",
            "Needed per day", "Days left", "Billing day", "Notes"]
    print(f"{len(results)} accounts. Spend through yesterday in each account's timezone. Inventory: {banner}\n")
    print("| " + " | ".join(cols) + " |")
    print("|" + "---|" * len(cols))
    for x in results:
        cells = [("; ".join(x[c]) if isinstance(x.get(c), list) else "" if x.get(c) is None else str(x.get(c, "")))
                 for c in cols]
        print("| " + " | ".join(s.replace("|", "/") for s in cells) + " |")


if __name__ == "__main__":
    main()
