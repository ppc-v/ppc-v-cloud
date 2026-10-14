#!/usr/bin/env python3
"""Report which API connections work. Never prints secret values."""

import os

import requests

TIMEOUT = 30
# Tag Manager, GA4 and Search Console need only the OAuth trio; Google Ads also needs these.
GOOGLE_VARS = ["GOOGLE_ADS_CLIENT_ID", "GOOGLE_ADS_CLIENT_SECRET", "GOOGLE_ADS_REFRESH_TOKEN"]
GOOGLE_ADS_VARS = ["GOOGLE_ADS_DEVELOPER_TOKEN", "GOOGLE_ADS_LOGIN_CUSTOMER_ID"]
META_BUSINESS_ID = "1517895191848391"
# Meta rejects unversioned calls once the app's default version is deprecated; bump when Meta deprecates this one.
META_API_VERSION = "v26.0"


def report(name, ok, detail):
    print(f"{'✅' if ok else '❌'} {name}: {detail}")


def missing(names):
    return [n for n in names if not os.environ.get(n)]


def google_access_token():
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


def get_json(url, token, key):
    resp = requests.get(url, headers={"Authorization": f"Bearer {token}"}, timeout=TIMEOUT)
    if resp.status_code != 200:
        return False, f"HTTP {resp.status_code}: {resp.text[:200]}"
    return True, f"{len(resp.json().get(key, []))} found"


def check_google():
    gaps = missing(GOOGLE_VARS)
    if gaps:
        report("Google", False, "not set: " + ", ".join(gaps))
        return
    try:
        token = google_access_token()
    except Exception as e:  # noqa: BLE001
        report("Google sign-in", False, str(e)[:200])
        return
    report("Google sign-in", True, "refresh token works")

    ads_gaps = missing(GOOGLE_ADS_VARS)
    if ads_gaps:
        report("Google Ads", False, "not set: " + ", ".join(ads_gaps))
    else:
        try:
            from google.ads.googleads.client import GoogleAdsClient

            os.environ.setdefault("GOOGLE_ADS_USE_PROTO_PLUS", "true")
            client = GoogleAdsClient.load_from_env()
            # Listing accessible customers works even with a test-only developer token, so also query the MCC.
            rows = client.get_service("GoogleAdsService").search(
                customer_id=os.environ["GOOGLE_ADS_LOGIN_CUSTOMER_ID"],
                query="SELECT customer_client.id FROM customer_client WHERE customer_client.manager = FALSE",
            )
            report("Google Ads", True, f"{sum(1 for _ in rows)} client accounts under the MCC")
        except Exception as e:  # noqa: BLE001
            failure = getattr(e, "failure", None)
            detail = "; ".join(err.message for err in failure.errors) if failure else str(e)
            report("Google Ads", False, detail[:300])

    for name, url, key in [
        ("Tag Manager", "https://tagmanager.googleapis.com/tagmanager/v2/accounts", "account"),
        ("GA4", "https://analyticsadmin.googleapis.com/v1beta/accountSummaries", "accountSummaries"),
        ("Search Console", "https://www.googleapis.com/webmasters/v3/sites", "siteEntry"),
        ("Drive", "https://www.googleapis.com/drive/v3/files?pageSize=100", "files"),
    ]:
        ok, detail = get_json(url, token, key)
        report(name, ok, detail)


def check_meta():
    token = os.environ.get("META_ACCESS_TOKEN")
    if not token:
        report("Meta", False, "not set: META_ACCESS_TOKEN")
        return
    params = {"access_token": token, "fields": "id,name", "limit": 500}
    resp = requests.get(
        f"https://graph.facebook.com/{META_API_VERSION}/{META_BUSINESS_ID}/owned_ad_accounts", params=params, timeout=TIMEOUT
    )
    if resp.status_code != 200:
        report("Meta", False, f"HTTP {resp.status_code}: {resp.text[:200]}")
        return
    report("Meta", True, f"{len(resp.json().get('data', []))} ad accounts visible (first page)")


def check_whatconverts():
    gaps = missing(["WHATCONVERTS_API_TOKEN", "WHATCONVERTS_API_SECRET"])
    if gaps:
        report("WhatConverts", False, "not set: " + ", ".join(gaps))
        return
    resp = requests.get(
        "https://app.whatconverts.com/api/v1/accounts",
        auth=(os.environ["WHATCONVERTS_API_TOKEN"], os.environ["WHATCONVERTS_API_SECRET"]),
        timeout=TIMEOUT,
    )
    if resp.status_code != 200:
        report("WhatConverts", False, f"HTTP {resp.status_code}: {resp.text[:200]}")
        return
    report("WhatConverts", True, "API key works")


if __name__ == "__main__":
    check_google()
    check_meta()
    check_whatconverts()
