# Accounts reference

These IDs aren't secret. API keys go in `credentials.md` (names only).

| What | Value |
|---|---|
| Google Ads MCC | `624-128-1836` (API form: `6241281836`) |
| Meta Business portfolio | `1517895191848391` (owns the client ad accounts) |
| WhatConverts | One agency account containing every client profile |
| Google service login | `paidsearch@vortala.com` (for Google Ads, GTM, GA4, Merchant Center, Search Console API access) |

## Vortala Ad Account Inventory (master client list)
- Sheet: https://docs.google.com/spreadsheets/d/1PHkhNJ6GHoAoKRtB-XyeaJFqnJbs00OzGZpNlMF6GwQ/edit
- Refreshes daily at 06:00 GMT+8 from the MCC and the Meta portfolio.
- Tabs: a "how to use" front tab with the flag catalogue, **Accounts** (one row per active ad account: health, top issue, owner, platform, client status, spend, budgets, leads, timezone, currency, IDs, notes), **Issues**, **Owners & Notes** (owner overrides and flag snoozes) and an Archive.
- Ownership: Sara/John labels in Google Ads are the official assignment. Meta accounts take the owner of the same client's Google account, matched by PP number. Shared Google logins: `ppcmcc1@` = Sara, `ppcmcc2@` / `ppcmcc3@` = John.
- Client status (Active / Paused / Canceled) is the team's own Google Ads label.
- Lead definition used by the sheet: a call, form, booking, registration, purchase or messaging conversation. Page views, booking-page visits, directions and engagement are **not** leads. Use the same definition in reports unless the requester says otherwise.
- Read it through the Google Sheets API with the paidsearch@ credentials (spreadsheet ID `1PHkhNJ6GHoAoKRtB-XyeaJFqnJbs00OzGZpNlMF6GwQ`). Don't rely on the public CSV export link: the sheet may be restricted to Vortala.
- Updated by an Apps Script bound to the sheet (Extensions → Apps Script). Script ID: `1eatKDsUVvuawzBCdi5h-vYKZUSoAZ13Z3UrHq2g4ylBxmF9j82S6Lrvp`. Read it with the Apps Script API (`GET https://script.googleapis.com/v1/projects/<id>/content`). Any edits to it are live changes: preview first, as with any other change.
- The sheet is owned by `arif@tincityimpact.com`, not a Vortala account; paidsearch@ has edit access.
