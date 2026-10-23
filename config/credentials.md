# Credentials

Keys are stored **only** in the cloud environment's settings (the environment menu in a session's title bar → Edit → environment variables). Never commit them or paste them into chat. A session picks up new values only when it starts, so start a fresh session after adding any.

Check what works with `python3 scripts/check_connections.py`.

## Google (Ads, Tag Manager, GA4, Merchant Center, Search Console, Drive, Sheets, Docs, Slides)
One OAuth app and one sign-in as `paidsearch@vortala.com` covers all of them.

| Variable | Where it comes from |
|---|---|
| `GOOGLE_ADS_DEVELOPER_TOKEN` | MCC → Tools → API Center → "View token". The token has Basic Access. |
| `GOOGLE_ADS_CLIENT_ID` | Google Cloud project → APIs & Services → Credentials → OAuth client (type: Web application) |
| `GOOGLE_ADS_CLIENT_SECRET` | Same OAuth client |
| `GOOGLE_ADS_REFRESH_TOKEN` | OAuth Playground, signed in as paidsearch@vortala.com (steps below) |
| `GOOGLE_ADS_LOGIN_CUSTOMER_ID` | `6241281836` |

Setup steps:
1. In the Google Cloud project, enable: Google Ads API, Tag Manager API, Google Analytics Admin API, Google Analytics Data API, Merchant API, Google Search Console API, Google Drive API, Google Sheets API, Google Docs API, Google Slides API, Apps Script API. Also, signed in as paidsearch@, switch on "Google Apps Script API" at https://script.google.com/home/usersettings.
2. OAuth consent screen: **Internal** (Workspace). If External, publish it to "In production"; in "Testing" the refresh token expires after 7 days.
3. Create an OAuth client of type Web application, with authorised redirect URI `https://developers.google.com/oauthplayground`.
4. At https://developers.google.com/oauthplayground: gear icon → "Use your own OAuth credentials" → enter the client ID and secret. Paste these scopes (one line, space separated), authorise as paidsearch@vortala.com, then "Exchange authorization code for tokens" and copy the refresh token:
   ```
   https://www.googleapis.com/auth/adwords https://www.googleapis.com/auth/tagmanager.edit.containers https://www.googleapis.com/auth/tagmanager.edit.containerversions https://www.googleapis.com/auth/tagmanager.publish https://www.googleapis.com/auth/analytics.edit https://www.googleapis.com/auth/analytics.readonly https://www.googleapis.com/auth/content https://www.googleapis.com/auth/webmasters https://www.googleapis.com/auth/drive https://www.googleapis.com/auth/spreadsheets https://www.googleapis.com/auth/documents https://www.googleapis.com/auth/presentations https://www.googleapis.com/auth/script.projects
   ```
5. paidsearch@vortala.com needs access in each product: a user on the MCC, a user on each GTM account (Publish permission), an Editor on each GA4 account, and a user in Merchant Center and Search Console where relevant.

Notes:
- The Google Cloud project has its **own** Google Ads API access level, separate from the token's: Cloud console → project `vortala-ppc-claude` → APIs & Services → Google Ads API → Access levels → Manage. It was Test until 2026-10-14 (error `CLOUD_PROJECT_NOT_APPROVED_FOR_PRODUCTION`). Arif verified and published the project's OAuth branding and upgraded it to **Basic** the same day: 15,000 operations a day on real accounts, all API features. Standard (unlimited) needs a separate application, about 10–15 business days' review.
- The developer token's "Intended use" says Reporting. Update it in the API Center to include campaign management before making changes through the API.
- The token's API contact is timo@vortala.com, who receives Google's notices about it.

## Meta (ads, Pixel / Conversions API, Instagram, Lead Ads)
| Variable | Where it comes from |
|---|---|
| `META_ACCESS_TOKEN` | Business Settings → Users → System users → Generate token (never expires) |
| `META_APP_SECRET` | Optional. The Meta app's secret, used to sign API calls |

Setup steps (needs a Business portfolio admin):
1. Create a business app at https://developers.facebook.com/apps, linked to portfolio 1517895191848391, with the Marketing API product added.
2. Business Settings → System users → add an **Admin** system user.
3. Assign the system user the ad accounts (full control), Pages, Instagram accounts and pixels/datasets.
4. Generate a token for the app with these permissions: `ads_management`, `ads_read`, `business_management`, `pages_show_list`, `pages_read_engagement`, `pages_manage_ads`, `leads_retrieval`, `instagram_basic`, `catalog_management`.

Status (2026-10-14): done. **Known limit (2026-10-22):** the Meta app was in Development mode, which blocked new ad creatives (error 1885183). It was switched to Live by 2026-10-23 04:39 UTC, and new creatives work now. When creating creatives, don't send the old `standard_enhancements` bundle in `degrees_of_freedom_spec` (error 3858504); opt in or out per feature instead. The system user also needs access to each client's Facebook Page to create ads or read lead forms. `META_ACCESS_TOKEN` is a system-user token for "Claude PPC" (ID `122100097821508769`) that never expires, and it sees the portfolio's ad accounts.

The token was granted more than the list above. Beyond those it also has `read_insights`, `publish_video`, `threads_business_basic`, `ads_mcp_management`, `pages_messaging`, `pages_manage_metadata`, `pages_read_user_content`, `pages_manage_posts`, `pages_manage_engagement`, `pages_utility_messaging`, `instagram_manage_comments`, `instagram_manage_insights`, `instagram_content_publish`, `instagram_manage_messages`, `instagram_manage_contents`, `instagram_shopping_tag_products`, `instagram_branded_content_brand`, `instagram_branded_content_ads_brand`, `facebook_branded_content_ads_brand`, `whatsapp_business_management`, `whatsapp_business_messaging`, `whatsapp_business_manage_events`, `paid_marketing_messages` and `manage_app_solution`. Page posting, Instagram publishing and WhatsApp/Messenger messaging are outbound actions: the "no outbound messages unless asked" rule in `CLAUDE.md` applies to them, and they need the same preview and approval as any other live change.

## WhatConverts
| Variable | Where it comes from |
|---|---|
| `WHATCONVERTS_API_TOKEN` | WhatConverts agency account → Integrations → API keys (create an agency/master key) |
| `WHATCONVERTS_API_SECRET` | Same key |

## claude.ai connectors (not relied on)
The team prefers direct API access over claude.ai connectors; use the APIs above for Google Drive, Sheets, Docs and Slides. Slack and Salesforce are currently connected as claude.ai connectors.
