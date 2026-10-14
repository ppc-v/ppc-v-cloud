#!/usr/bin/env python3
"""Collect conversion-tracking facts for one client across Google Ads, the website, GTM, GA4, Meta and WhatConverts.

  python3 scripts/tracking_audit.py PP5416            # markdown summary with automatic findings
  python3 scripts/tracking_audit.py PP5416 --json     # everything collected, for deeper digging
  python3 scripts/tracking_audit.py PP5416 --url https://example.com/offer   # also check this page
  python3 scripts/tracking_audit.py PP5416 --refresh-gtm   # after a client shares a new GTM container

Ad accounts come from the inventory sheet (match on PP number); add --google-id / --meta-id for accounts not in it.
Read-only. WhatConverts leads are reduced to counts: no names, numbers, recordings, transcripts or call summaries.
"""

import argparse
import json
import os
import re
import sys
import time
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from datetime import date, timedelta

import requests

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import inventory  # noqa: E402

TIMEOUT = 30
META_API = "https://graph.facebook.com/v26.0"
WC_API = "https://app.whatconverts.com/api/v1"
LEAD_CATEGORIES = {"PHONE_CALL_LEAD", "SUBMIT_LEAD_FORM", "BOOK_APPOINTMENT", "CONTACT", "IMPORTED_LEAD",
                   "QUALIFIED_LEAD", "CONVERTED_LEAD", "REQUEST_QUOTE", "SIGNUP", "PURCHASE", "STORE_SALE"}
WEAK_CATEGORIES = {"PAGE_VIEW", "ENGAGEMENT", "GET_DIRECTIONS", "STORE_VISIT", "OUTBOUND_CLICK", "ADD_TO_CART",
                   "BEGIN_CHECKOUT", "DOWNLOAD"}
# Same idea as the inventory sheet: these names describe interest, not a confirmed lead.
WEAK_NAME = re.compile(r"page ?view|visit|reached|button|click|scroll|engag|direction|time on", re.I)
META_LEAD_GOALS = {"LEAD_GENERATION", "OFFSITE_CONVERSIONS", "QUALITY_LEAD", "QUALITY_CALL", "CONVERSATIONS"}
# Where privacy/consent rules most likely apply (inventory "Country" column).
CONSENT_COUNTRIES = {"CA", "AU", "NZ", "GB", "UK", "IE"} | {
    "AT", "BE", "BG", "HR", "CY", "CZ", "DK", "EE", "FI", "FR", "DE", "GR", "HU", "IT", "LV", "LT", "LU", "MT", "NL",
    "PL", "PT", "RO", "SK", "SI", "ES", "SE", "NO", "IS", "LI", "CH"}
CONSENT_TOOLS = {"Cookiebot": "cookiebot", "OneTrust": "onetrust", "CookieYes": "cookieyes", "Termly": "termly",
                 "iubenda": "iubenda", "Complianz": "complianz", "Usercentrics": "usercentrics",
                 "Osano": "osano", "Google consent mode": "gtag('consent'"}
GTM_INDEX = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "config", "gtm_containers.json")
HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; VortalaTrackingAudit/1.0)"}


def digits(s):
    return re.sub(r"\D", "", str(s or ""))


def country_from_tz(tz):
    """Best guess when the inventory has no country (Meta rows)."""
    tz = tz or ""
    if re.match(r"America/(Toronto|Vancouver|Edmonton|St_Johns|Winnipeg|Halifax|Regina|Moncton|Montreal)", tz):
        return "CA"
    return ("US" if tz.startswith("America/") else "AU" if tz.startswith("Australia/") else
            "NZ" if tz == "Pacific/Auckland" else "GB" if tz == "Europe/London" else "")


def google_token():
    return inventory.access_token()


def gget(token, url, **params):
    for wait in (5, 15, 30, 60, None):  # Tag Manager's per-minute quota is small; back off on 429
        r = requests.get(url, headers={"Authorization": f"Bearer {token}"}, params=params, timeout=TIMEOUT)
        if r.status_code != 429 or wait is None:
            break
        time.sleep(wait)
    r.raise_for_status()
    return r.json()


# ---------- Google Ads ----------

def google_ads(cid, days):
    from google.ads.googleads.client import GoogleAdsClient
    os.environ.setdefault("GOOGLE_ADS_USE_PROTO_PLUS", "true")
    svc = GoogleAdsClient.load_from_env().get_service("GoogleAdsService")
    q = lambda query: list(svc.search(customer_id=cid, query=query))  # noqa: E731
    out = {"customer_id": cid}
    c = q("SELECT customer.descriptive_name, customer.auto_tagging_enabled, customer.time_zone, "
          "customer.call_reporting_setting.call_reporting_enabled, "
          "customer.call_reporting_setting.call_conversion_reporting_enabled FROM customer")[0].customer
    out.update(name=c.descriptive_name, auto_tagging=c.auto_tagging_enabled, time_zone=c.time_zone,
               call_reporting=c.call_reporting_setting.call_reporting_enabled,
               call_conversion_reporting=c.call_reporting_setting.call_conversion_reporting_enabled)
    actions = {}
    for r in q("SELECT conversion_action.id, conversion_action.name, conversion_action.type, conversion_action.category, "
               "conversion_action.status, conversion_action.primary_for_goal, conversion_action.counting_type, "
               "conversion_action.origin FROM conversion_action WHERE conversion_action.status = 'ENABLED'"):
        a = r.conversion_action
        actions[a.name] = {"id": a.id, "type": a.type_.name, "category": a.category.name, "primary": a.primary_for_goal,
                           "counting": a.counting_type.name, "origin": a.origin.name,
                           "conversions": 0.0, "last_date": None}
    end, start = date.today(), date.today() - timedelta(days=days)
    for r in q("SELECT segments.date, segments.conversion_action_name, metrics.all_conversions FROM customer "
               f"WHERE segments.date BETWEEN '{start}' AND '{end}' AND metrics.all_conversions > 0"):
        a = actions.setdefault(r.segments.conversion_action_name, {"conversions": 0.0, "last_date": None,
                                                                   "note": "not an enabled action"})
        a["conversions"] += r.metrics.all_conversions
        a["last_date"] = max(a["last_date"] or "", r.segments.date)
    out["conversion_actions"] = actions
    out["call_assets"] = [
        {"phone": r.asset.call_asset.phone_number,
         "call_conversion_reporting": r.asset.call_asset.call_conversion_reporting_state.name}
        for r in q("SELECT asset.call_asset.phone_number, asset.call_asset.call_conversion_reporting_state "
                   "FROM customer_asset WHERE customer_asset.status = 'ENABLED' AND asset.type = 'CALL'")
        + q("SELECT asset.call_asset.phone_number, asset.call_asset.call_conversion_reporting_state, campaign.status "
            "FROM campaign_asset WHERE campaign_asset.status = 'ENABLED' AND asset.type = 'CALL' "
            "AND campaign.status = 'ENABLED'")]
    clicks = Counter()
    for r in q("SELECT ad_group_ad.ad.final_urls, metrics.clicks FROM ad_group_ad "
               "WHERE segments.date DURING LAST_30_DAYS AND metrics.clicks > 0"):
        for u in r.ad_group_ad.ad.final_urls:
            clicks[u] += r.metrics.clicks
    for r in q("SELECT asset_group.final_urls, asset_group.status, campaign.status FROM asset_group WHERE asset_group.status = 'ENABLED' "
               "AND campaign.status = 'ENABLED'"):
        for u in r.asset_group.final_urls:
            clicks[u] += 0
    out["final_urls"] = [u for u, _ in clicks.most_common(5)]
    return out


# ---------- Website ----------

def scan_page(url):
    try:
        r = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
        html = r.text
    except Exception as e:  # noqa: BLE001
        return {"url": url, "error": str(e)[:150]}
    low = html.lower()
    return {
        "url": url, "status": r.status_code, "final_url": r.url,
        "gtm": sorted(set(re.findall(r"GTM-[A-Z0-9]{4,9}", html))),
        "ga4": sorted(set(re.findall(r"\bG-[A-Z0-9]{6,12}\b", html))),
        "google_ads": sorted(set(re.findall(r"\bAW-\d{6,12}\b", html))),
        "meta_pixel": sorted(set(re.findall(r"fbq\(\s*['\"]init['\"]\s*,\s*['\"](\d{10,20})", html))),
        "whatconverts": "whatconverts" in low or "ksrndkehqnwntyxlhgto" in low,
        "callrail": "callrail" in low,
        "consent_tools": [n for n, k in CONSENT_TOOLS.items() if k in low],
        "query_params": sorted(set(re.findall(r"[?&]([a-zA-Z_]+)=", url))),
    }


# ---------- GTM ----------

def gtm_index(token, refresh=False):
    """Map GTM public ID → container, cached in the repo because listing every account is slow under the API quota."""
    if not refresh and os.path.exists(GTM_INDEX):
        return json.load(open(GTM_INDEX))
    index = {}
    for a in gget(token, "https://tagmanager.googleapis.com/tagmanager/v2/accounts").get("account", []):
        try:
            cs = gget(token, f"https://tagmanager.googleapis.com/tagmanager/v2/{a['path']}/containers").get("container", [])
        except requests.HTTPError:
            continue
        for c in cs:
            index[c["publicId"]] = {"path": c["path"], "name": c.get("name"), "account": a.get("name")}
    with open(GTM_INDEX, "w") as fh:
        json.dump(dict(sorted(index.items())), fh, indent=1, ensure_ascii=False)
        fh.write("\n")
    return index


def gtm_containers(token, public_ids):
    if not public_ids:
        return []
    index = gtm_index(token)
    age_hours = (time.time() - os.path.getmtime(GTM_INDEX)) / 3600 if os.path.exists(GTM_INDEX) else 999
    if public_ids - set(index) and age_hours > 24:  # maybe shared since the index was built; rebuild at most daily
        index = gtm_index(token, refresh=True)
    found = [{"publicId": pid, **index[pid]} for pid in sorted(public_ids) if pid in index]
    out = []
    for c in found:
        info = {"public_id": c["publicId"], "name": c.get("name"), "path": c["path"]}
        try:
            live = gget(token, f"https://tagmanager.googleapis.com/tagmanager/v2/{c['path']}/versions:live")
        except requests.HTTPError as e:
            info["error"] = f"live version: HTTP {e.response.status_code}"
            out.append(info)
            continue
        info["live_version"] = live.get("containerVersionId")
        tags = []
        for t in live.get("tag", []):
            params = {p.get("key"): p.get("value") for p in t.get("parameter", []) if "value" in p}
            html = params.get("html", "") or ""
            tags.append({
                "name": t.get("name"), "type": t.get("type"), "paused": bool(t.get("paused")),
                "ids": sorted(set(re.findall(r"\b(?:G-[A-Z0-9]{6,12}|AW-\d{6,12})\b", json.dumps(t)))
                              | set(filter(None, [params.get("conversionId"), params.get("measurementIdOverride"),
                                                  params.get("tagId")]))),
                "conversion_label": params.get("conversionLabel"),
                "event_name": params.get("eventName"),
                "meta_pixel": sorted(set(re.findall(r"fbq\(\s*['\"]init['\"]\s*,\s*['\"](\d{10,20})", html))),
                "custom_html_mentions": [k for k in ("fbq", "whatconverts", "gtag", "dataLayer", "email", "phone")
                                         if k in html.lower()],
                "consent": (t.get("consentSettings") or {}).get("consentStatus"),
                "triggers": len(t.get("firingTriggerId", [])),
            })
        info["tags"] = tags
        out.append(info)
    return out


# ---------- GA4 ----------

def ga4_properties(token, measurement_ids, ads_cid):
    summaries = gget(token, "https://analyticsadmin.googleapis.com/v1beta/accountSummaries", pageSize=200)
    props = [p for a in summaries.get("accountSummaries", []) for p in a.get("propertySummaries", [])]

    def streams(p):
        try:
            s = gget(token, f"https://analyticsadmin.googleapis.com/v1beta/{p['property']}/dataStreams").get("dataStreams", [])
        except requests.HTTPError:
            s = []
        try:
            links = gget(token, f"https://analyticsadmin.googleapis.com/v1beta/{p['property']}/googleAdsLinks").get("googleAdsLinks", [])
        except requests.HTTPError:
            links = []
        return p, s, links

    with ThreadPoolExecutor(8) as ex:
        scanned = list(ex.map(streams, props))
    out = []
    for p, s, links in scanned:
        mids = [x.get("webStreamData", {}).get("measurementId") for x in s]
        linked = [digits(lk.get("customerId")) for lk in links]
        if not (set(mids) & set(measurement_ids) or (ads_cid and ads_cid in linked)):
            continue
        info = {"property": p["property"], "name": p.get("displayName"), "measurement_ids": mids,
                "google_ads_links": linked,
                "stream_urls": [x.get("webStreamData", {}).get("defaultUri") for x in s]}
        try:
            info["key_events"] = [k["eventName"] for k in gget(
                token, f"https://analyticsadmin.googleapis.com/v1beta/{p['property']}/keyEvents").get("keyEvents", [])]
        except requests.HTTPError as e:
            info["key_events_error"] = f"HTTP {e.response.status_code}"
        try:
            r = requests.post(f"https://analyticsdata.googleapis.com/v1beta/{p['property']}:runReport",
                              headers={"Authorization": f"Bearer {token}"}, timeout=TIMEOUT,
                              json={"dateRanges": [{"startDate": "30daysAgo", "endDate": "yesterday"}],
                                    "dimensions": [{"name": "eventName"}], "metrics": [{"name": "eventCount"}],
                                    "limit": 50})
            r.raise_for_status()
            info["events_30d"] = {row["dimensionValues"][0]["value"]: int(row["metricValues"][0]["value"])
                                  for row in r.json().get("rows", [])}
        except requests.HTTPError as e:
            info["events_error"] = f"HTTP {e.response.status_code}"
        out.append(info)
    return out


# ---------- Meta ----------

def meta(act):
    tok = os.environ["META_ACCESS_TOKEN"]
    get = lambda path, **p: requests.get(f"{META_API}/{path}", params={"access_token": tok, **p},  # noqa: E731
                                         timeout=TIMEOUT).json()
    out = {"ad_account": act}
    pixels = get(f"act_{act}/adspixels", fields="id,name,last_fired_time,is_unavailable").get("data", [])
    since = int(time.time()) - 7 * 86400
    for px in pixels:
        stats = get(f"{px['id']}/stats", aggregation="event", start_time=since)
        counts = Counter()
        for bucket in stats.get("data", []):
            for d in bucket.get("data", []):
                counts[d.get("value")] += int(d.get("count", 0))
        px["events_7d"] = dict(counts)
    out["pixels"] = pixels
    out["custom_conversions"] = [
        {k: c.get(k) for k in ("id", "name", "custom_event_type", "rule", "last_fired_time", "is_archived")}
        for c in get(f"act_{act}/customconversions", fields="id,name,custom_event_type,rule,last_fired_time,is_archived",
                     limit=100).get("data", []) if not c.get("is_archived")]
    out["active_ad_sets"] = [
        {"name": s.get("name"), "optimization_goal": s.get("optimization_goal"), "promoted_object": s.get("promoted_object")}
        for s in get(f"act_{act}/adsets", fields="name,optimization_goal,promoted_object", limit=200,
                     effective_status='["ACTIVE"]').get("data", [])]
    links = Counter()
    for ad in get(f"act_{act}/ads", fields="creative{object_story_spec,asset_feed_spec}", limit=50,
                  effective_status='["ACTIVE"]').get("data", []):
        for u in re.findall(r"https?://[^\s\"'\\]+", json.dumps(ad.get("creative", {}))):
            if not re.search(r"facebook\.com|fbcdn|instagram\.com|fb\.me", u):
                links[u] += 1
    out["landing_urls"] = [u for u, _ in links.most_common(3)]
    return out


# ---------- WhatConverts ----------

def whatconverts(pp, days):
    auth = (os.environ["WHATCONVERTS_API_TOKEN"], os.environ["WHATCONVERTS_API_SECRET"])
    num = digits(pp)
    accounts = requests.get(f"{WC_API}/accounts", auth=auth, params={"accounts_per_page": 250}, timeout=TIMEOUT).json()
    match = [a for a in accounts.get("accounts", []) if re.match(rf"\s*(PP)?\s*0*{int(num)}\b", a["account_name"], re.I)]
    if not match:
        return {"error": f"no WhatConverts account named like {pp}"}
    out = []
    start, end = date.today() - timedelta(days=days), date.today()
    for a in match:
        for prof in a.get("profiles", []):
            leads, page = [], 1
            while True:
                r = requests.get(f"{WC_API}/leads", auth=auth, timeout=TIMEOUT, params={
                    "account_id": a["account_id"], "profile_id": prof["profile_id"], "start_date": str(start),
                    "end_date": str(end), "leads_per_page": 250, "page_number": page}).json()
                leads += r.get("leads", [])
                if page >= int(r.get("total_pages") or 1) or page >= 8:
                    break
                page += 1
            real = [x for x in leads if not x.get("spam") and not x.get("duplicate")]
            paid = [x for x in real if (x.get("lead_source"), x.get("lead_medium")) == ("google", "cpc")]
            meta_leads = [x for x in real if x.get("lead_source") in ("facebook", "fb", "instagram", "ig", "meta")]
            analysis = lambda x, k: (x.get("lead_analysis") or {}).get(k) if isinstance(x.get("lead_analysis"), dict) else None  # noqa: E731
            out.append({
                "account": a["account_name"], "account_id": a["account_id"], "profile_id": prof["profile_id"],
                "days": days, "leads": len(leads), "spam_or_duplicate": len(leads) - len(real),
                "by_type": dict(Counter(x.get("lead_type") for x in real)),
                "by_source": dict(Counter(f"{x.get('lead_source')}/{x.get('lead_medium')}" for x in real).most_common(8)),
                "google_cpc": len(paid),
                "google_cpc_with_gclid": sum(1 for x in paid if x.get("gclid")),
                "google_cpc_by_tracking_number": dict(Counter(x.get("tracking_number") for x in paid
                                                              if x.get("lead_type") == "Phone Call")),
                "google_cpc_customer_type": dict(Counter(analysis(x, "Customer Type") for x in paid)),
                "meta": len(meta_leads),
                "last_google_cpc": max((x.get("date_created", "") for x in paid), default=None),
            })
    return out


# ---------- Findings ----------

def findings(d, country):
    f = []
    add = lambda level, text: f.append((level, text))  # noqa: E731
    g = d.get("google")
    if isinstance(g, dict) and "error" not in g:
        if not g["auto_tagging"]:
            add("🔴", "Google Ads auto-tagging is OFF: no GCLID, so WhatConverts/offline call imports can't match")
        acts = g["conversion_actions"]
        primary = {n: a for n, a in acts.items() if a.get("primary")}
        lead_primary = {n: a for n, a in primary.items() if a.get("category") in LEAD_CATEGORIES}
        if not lead_primary:
            add("🔴", "No primary conversion action in a lead category (call, form, booking, contact, imported lead)")
        for n, a in primary.items():
            if a.get("category") in WEAK_CATEGORIES:
                add("🟠", f"Primary goal '{n}' is a weak action ({a['category']}): bidding optimises towards it")
            elif WEAK_NAME.search(n) and a.get("category") not in LEAD_CATEGORIES - {"CONTACT"}:
                add("🟠", f"Primary goal '{n}' looks like a page view or click by its name, not a confirmed lead")
            elif a.get("category") == "DEFAULT":
                add("🟡", f"Primary goal '{n}' has no category (DEFAULT): check whether it is a real lead")
            if not a.get("conversions"):
                add("🟠", f"Primary goal '{n}' recorded nothing in the window")
            if a.get("counting") == "MANY_PER_CLICK" and a.get("category") in LEAD_CATEGORIES:
                add("🟡", f"'{n}' counts every conversion per click: leads usually count One")
        ga4_primary = [n for n, a in primary.items() if str(a.get("type", "")).startswith("GOOGLE_ANALYTICS_4")]
        tag_primary = [n for n, a in primary.items() if a.get("type") in ("WEBPAGE", "WEBPAGE_CODELESS")]
        if ga4_primary and tag_primary:
            add("🟡", f"Both GA4 imports {ga4_primary} and Google tag actions {tag_primary} are primary: "
                     "check they don't count the same lead twice")
        if not g["call_reporting"] or not g["call_conversion_reporting"]:
            add("🟠", "Account-level call reporting or call conversion reporting is off: calls from ads aren't counted by Google")
        for ca in g["call_assets"]:
            if ca["call_conversion_reporting"] == "DISABLED":
                add("🟠", f"Call asset {ca['phone']} has call conversion reporting DISABLED")
    no_consent = []
    for p in d.get("pages", []):
        if p.get("error") or p.get("status", 200) >= 400:
            add("🔴", f"Landing page {p['url']} failed to load ({p.get('error') or p.get('status')})")
            continue
        if not (p["gtm"] or p["ga4"] or p["google_ads"]):
            add("🔴", f"No GTM, GA4 or Google Ads tag found in the HTML of {p['url']}")
        if not p["consent_tools"]:
            no_consent.append(p["url"].split("?")[0])
        risky = [q for q in p["query_params"] if not q.lower().startswith(("utm_", "gclid", "gbraid", "wbraid", "fbclid"))]
        if risky:
            add("🟡", f"Final URL carries non-standard parameters {risky}: make sure none hold health or patient data")
    if country in CONSENT_COUNTRIES:
        if no_consent:
            add("🟠", f"{country} client: no consent banner or consent mode found in the page HTML of {no_consent} "
                     "(it may load through GTM: check the container). Consent rules likely apply (CLAUDE.md)")
        else:
            add("ℹ️", f"{country} client: consent rules likely apply (CLAUDE.md); a consent tool was found, check it gates the tags")
    site_gtm = {x for pg in d.get("pages", []) for x in pg.get("gtm", [])}
    seen_gtm = {c["public_id"] for c in d["gtm"]} if isinstance(d.get("gtm"), list) else set(site_gtm)
    if site_gtm - seen_gtm:
        add("🟠", f"GTM container(s) {sorted(site_gtm - seen_gtm)} on the site are not shared with paidsearch@: "
                 "can't see what fires (ask for Publish access)")
    site_ga4 = sorted({x for pg in d.get("pages", []) for x in pg.get("ga4", [])} | {
        i for c in (d["gtm"] if isinstance(d.get("gtm"), list) else []) for t in c.get("tags", []) for i in t["ids"]
        if i.startswith("G-")})
    if not d.get("ga4") and (d.get("pages") or g):
        add("🟡", f"GA4 {site_ga4} is on the site but not shared with paidsearch@" if site_ga4 else
            "No GA4 property found that paidsearch@ can see (by measurement ID on the site/GTM or by Google Ads link)")
    for c in d.get("gtm") if isinstance(d.get("gtm"), list) else []:
        live = [t for t in c.get("tags", []) if not t["paused"]]
        types = Counter(t["type"] for t in live)
        if country in CONSENT_COUNTRIES and live and all(t.get("consent") in (None, "notSet") for t in live):
            add("🟠", f"GTM {c['public_id']}: no tag has consent settings ({country} client): check for consent mode")
        if types.get("awct") and not types.get("gclidw"):
            add("🟠", f"GTM {c['public_id']}: Google Ads conversion tags but no Conversion Linker")
        if any(t.get("custom_html_mentions") and {"email", "phone"} & set(t["custom_html_mentions"]) for t in live):
            add("🟡", f"GTM {c['public_id']}: custom HTML mentions email/phone: check nothing personal is sent to ad platforms")
    for p in d.get("ga4") if isinstance(d.get("ga4"), list) else []:
        if not p.get("key_events"):
            add("🟠", f"GA4 {p['name']}: no key events set")
        else:
            dead = [k for k in p["key_events"] if not p.get("events_30d", {}).get(k)]
            if dead:
                add("🟡", f"GA4 {p['name']}: key events with no hits in 30 days: {dead}")
        if g and isinstance(g, dict) and g.get("customer_id") and g["customer_id"] not in p.get("google_ads_links", []):
            add("🟡", f"GA4 {p['name']} is not linked to Google Ads {g['customer_id']}")
    m = d.get("meta")
    if isinstance(m, dict) and "error" not in m:
        if not m["pixels"]:
            add("🔴", "Meta ad account has no pixel/dataset")
        recent = str(date.today() - timedelta(days=14))
        cc_live = [c for c in m["custom_conversions"] if (c.get("last_fired_time") or "")[:10] >= recent]
        for px in m["pixels"]:
            last = px.get("last_fired_time")
            if not last or last[:10] < str(date.today() - timedelta(days=3)):
                add("🔴", f"Meta pixel {px['name']} last fired {last or 'never'}")
            elif not set(px.get("events_7d", {})) - {"PageView"}:
                if cc_live:
                    add("🟡", f"Meta pixel {px['name']} sends only PageView; leads are tracked by URL-based custom "
                             f"conversions {[c['name'] for c in cc_live]}. Check their type (LEAD vs OTHER) and that "
                             "ad sets optimise for them")
                else:
                    add("🟠", f"Meta pixel {px['name']} only records PageView and no custom conversion fired in 14 days: "
                             "no lead tracking")
        for c in m["custom_conversions"]:
            if c.get("custom_event_type") == "OTHER" and (c.get("last_fired_time") or "")[:10] >= recent:
                add("🟡", f"Custom conversion '{c['name']}' is typed OTHER: reports and the inventory sheet may not count it as a lead")
        weak = [s["name"] for s in m["active_ad_sets"] if s.get("optimization_goal") not in META_LEAD_GOALS]
        if weak:
            add("🟡", f"Meta ad sets not optimising for leads/conversions: {weak[:5]}")
    wc = d.get("whatconverts")
    if isinstance(wc, dict) and wc.get("error"):
        add("ℹ️", f"WhatConverts: {wc['error']} (no call tracking there, or the account is named differently)")
    for w in wc if isinstance(wc, list) else []:
        if isinstance(w, dict) and w.get("google_cpc"):
            miss = w["google_cpc"] - w["google_cpc_with_gclid"]
            if miss:
                add("🟡", f"WhatConverts: {miss} of {w['google_cpc']} google/cpc leads have no GCLID, so they can't "
                         "be imported to Google Ads (call-asset or static-number calls)")
    return f


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("pp", help="PP number, e.g. PP5416")
    p.add_argument("--google-id", action="append", default=[])
    p.add_argument("--meta-id", action="append", default=[])
    p.add_argument("--url", action="append", default=[], help="extra page to scan (repeatable)")
    p.add_argument("--days", type=int, default=90, help="conversion / lead window (default 90)")
    p.add_argument("--refresh-gtm", action="store_true",
                   help="rebuild config/gtm_containers.json first (after a client shares a new container; takes ~2 min)")
    p.add_argument("--json", action="store_true")
    args = p.parse_args()

    token = google_token()
    if args.refresh_gtm:
        gtm_index(token, refresh=True)
    _, rows = inventory.read_tab(token, "Accounts")
    num = digits(args.pp)
    rows = [r for r in rows if digits((re.match(r"\s*PP\s*(\d+)", r["Account"], re.I) or [None, ""])[1]) == num]
    gids = [digits(x) for x in args.google_id] or [digits(r["Ad account ID"]) for r in rows if r["Platform"] == "Google"]
    mids = [digits(x) for x in args.meta_id] or [digits(r["Ad account ID"]) for r in rows if r["Platform"] == "Meta"]
    country = next((r.get("Country") for r in rows if r.get("Country")), "") or next(
        (country_from_tz(r.get("Timezone")) for r in rows if country_from_tz(r.get("Timezone"))), "")
    d = {"pp": args.pp.upper(), "inventory_rows": [r["Account"] + " / " + r["Platform"] for r in rows],
         "country": country, "window_days": args.days}

    def safe(fn, *a):
        try:
            return fn(*a)
        except Exception as e:  # noqa: BLE001
            failure = getattr(e, "failure", None)
            return {"error": ("; ".join(x.message for x in failure.errors) if failure else str(e))[:300]}

    d["google"] = safe(google_ads, gids[0], args.days) if gids else None
    if len(gids) > 1:
        d["other_google_ids"] = gids[1:]
    d["meta"] = safe(meta, mids[0]) if mids else None
    urls = list(dict.fromkeys(
        args.url + ((d["google"] or {}).get("final_urls", [])[:3] if isinstance(d["google"], dict) else [])
        + ((d["meta"] or {}).get("landing_urls", [])[:2] if isinstance(d["meta"], dict) else [])))
    d["pages"] = [scan_page(u) for u in urls]
    gtm_ids = {x for pg in d["pages"] for x in pg.get("gtm", [])}
    d["gtm"] = safe(gtm_containers, token, gtm_ids)
    ga4_ids = {x for pg in d["pages"] for x in pg.get("ga4", [])} | {
        i for c in (d["gtm"] if isinstance(d["gtm"], list) else []) for t in c.get("tags", []) for i in t["ids"]
        if i.startswith("G-")}
    d["ga4"] = safe(ga4_properties, token, ga4_ids, gids[0] if gids else None)
    d["whatconverts"] = safe(whatconverts, args.pp, args.days)
    d["findings"] = findings(d, country)

    if args.json:
        json.dump(d, sys.stdout, ensure_ascii=False, indent=1, default=str)
        print()
        return
    print(f"# Tracking facts: {d['pp']} ({', '.join(d['inventory_rows']) or 'not in inventory'}; country {country or '?'})\n")
    print("## Automatic findings")
    for level, text in d["findings"] or [("🟢", "nothing flagged by the automatic checks")]:
        print(f"- {level} {text}")
    g = d["google"]
    if isinstance(g, dict) and "error" not in g:
        print(f"\n## Google Ads {g['customer_id']} ({g['name']}, {g['time_zone']})")
        print(f"auto-tagging {g['auto_tagging']}, call reporting {g['call_reporting']}, "
              f"call conversion reporting {g['call_conversion_reporting']}\n")
        print(f"| Action | Type | Category | Primary | Counting | Conv ({args.days}d) | Last |\n|---|---|---|---|---|---|---|")
        for n, a in sorted(g["conversion_actions"].items(), key=lambda x: (not x[1].get("primary"), x[0])):
            print(f"| {n} | {a.get('type', '')} | {a.get('category', '')} | {a.get('primary', '')} | {a.get('counting', '')} "
                  f"| {round(a['conversions'], 1)} | {a['last_date'] or ''} |")
        print("\nCall assets: " + (", ".join(f"{c['phone']} ({c['call_conversion_reporting']})" for c in g["call_assets"]) or "none"))
    elif g:
        print(f"\n## Google Ads: {g}")
    for section in ("pages", "gtm", "ga4", "meta", "whatconverts"):
        print(f"\n## {section}\n```json\n{json.dumps(d[section], ensure_ascii=False, indent=1, default=str)[:4000]}\n```")


if __name__ == "__main__":
    main()
