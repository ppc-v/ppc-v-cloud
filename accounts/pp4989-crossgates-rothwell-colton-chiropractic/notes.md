# PP4989 - Crossgates, Rothwell, and Colton Chiropractic Clinics

- **Google Ads ID:** 735-054-6707 (Etc/GMT, GBP). Account name "PP4989 - Crossgates, Rothwell, and Colton Chiropractic"
- **Meta:** none known
- **Country:** United Kingdom (Leeds / Wakefield area). Contact: Derek Mould. DMS: Stacy Gustafson
- **Salesforce:** setup case 00837698 (https://vortala.my.salesforce.com/500N100000bAlwW). £750/month Google budget, £188 management fee
- **Landing page:** https://www.crossgatesclinic.co.uk/chiropractor-in-leeds/
- **Access:** normal
- **Usually worked on by:** John

## Setup (as of 2026-10-23, read-only check)
- One Search campaign, "Perfect Patients" (23211235880), paused, £37.50/day budget.
- Billing: setup 8037914655 on payments profile "Rothwell Health Hub Limited" (1051-8671-0269), payments account 9597-4189-4208-0222. **Ended 2026-04-27**, so there's no active billing. The client removed it after the April breach notice. paidsearch@ can't see any payments account for this customer through the API.
- Identity verification status can't be read until billing is active again (API error NO_EFFECTIVE_BILLING).
- Conversions: many primary goals, including GA4 page views (online_booking_page_view, contact page views) and Google's own "Calls from ads" alongside the WhatConverts call imports. This likely double counts calls and inflates conversions (Jan 2026: 174 conversions from 305 clicks). Fix the goals before relaunch.
- UK client: UK GDPR / PECR consent applies. Check Consent Mode v2 on the site before relaunch.

## History and decisions
- 2025-11: set up by John. The card needed extra bank security (3-D Secure) before Google accepted it. Launched 2026-01-03 with a £60 new patient special and a code.
- Spend: Jan 2026 £733.67, Feb £745.12, Mar £482.43. Last spend was 2026-03-18. No unauthorised campaigns or spend from the April 2026 breach were found in this account.
- 2026-06-02: cancelled.
- 2026-10-21/22: client wants to restart at the original £750 budget. No new setup fee because it's been under 6 months (John). They proposed a £50 "autumn offer" for November first appointments, code GADD50 at reception.
- 2026-10-23 JW: blocked on reconnecting billing and on Google's advertiser verification.
