# PP0117: bidding, keywords, negatives, schedule, new RSA, call tracking, callout

- **When:** 2026-10-19 16:43 UTC (12:43 EDT for Sara)
- **Requested by:** SS
- **Approved by:** SS, approved the preview in chat ("do everything aside from changing the reached online booking page to secondary"); the callout change was approved separately
- **Platform:** Google Ads
- **Session:** https://claude.ai/code/session_01BwBaixcA8hEbMDfkToMWq1

## Changes
Account: PP0117 - Funnell Chiropractic (470-953-8470), campaign "Perfect Patients" (395701357), ad group "Rockingham Chiropractor" (52436055548).

| Entity (type, name, ID) | Field | Before | After | Result |
|---|---|---|---|---|
| Campaign 395701357 | Bid strategy | Maximize Conversions, no target CPA | Maximize Clicks, max CPC AUD 12.00 | ✅ applied |
| Campaign 395701357 | Daily budget | AUD 23.00 | AUD 23.00 (unchanged; about AUD 700/month) | n/a |
| Campaign 395701357 | Location option | Presence or interest | Presence | ✅ applied |
| Keyword "chiropractor rockingham" broad (14387138612) | Status | Enabled | Paused | ✅ applied |
| Keyword "chiropractor rockingham" phrase (330811894307) | Status | Paused | Enabled | ✅ applied |
| Keyword "rockingham chiropractor" phrase (330811894467) | Status | Paused | Enabled | ✅ applied |
| Keyword "chiro rockingham" phrase (331740201019) | Status | Paused | Enabled | ✅ applied |
| Keyword "chiropractic rockingham" phrase (469189360315) | Status | Paused | Enabled | ✅ applied |
| Keyword "chiropractor near rockingham" phrase (330811894267) | Status | Paused | Enabled | ✅ applied |
| Keyword "chiro near me" phrase (87650539880) | New | none | Enabled | ✅ applied |
| Keyword "chiropractic near me" phrase (294891648136) | New | none | Enabled | ✅ applied |
| Campaign negatives | New | 9 campaign negatives | 56: added 46 phrase and 1 exact (list below) | ✅ applied |
| Ad schedule Mon afternoon (305270) | Hours | 13:00–17:00 | 13:00–17:30 | ✅ applied (removed and recreated) |
| Ad schedule Wed afternoon (325270) | Hours | 13:00–17:00, modifier 1.0 | 13:00–17:30, modifier 1.0 | ✅ applied (removed and recreated) |
| Ad schedule Fri afternoon (345270) | Hours | 13:00–17:00, modifier 1.0 | 13:00–17:30, modifier 1.0 | ✅ applied (removed and recreated) |
| Ad schedule Tue (313444 → 313250) | Hours | 8–11 | 8:00–12:30 | ✅ applied (removed and recreated) |
| Ad schedule Thu (333444 → 333250) | Hours | 8–11 | 8:00–12:30 | ✅ applied (removed and recreated) |
| Ad schedule Sat (353244) | New | not scheduled | 8:00–11:00 | ✅ applied |
| RSA 828510025650 | New | none | Enabled, no pins, path /new-patients, 15 headlines + 4 descriptions (see the preview in session) | ✅ applied, policy review in progress |
| Conversion action "Calls From Google Ads" (6802245026) | Counting | Every | One | ✅ applied |
| Conversion action "Calls From Ad Extensions" (6802290174) | Counting | Every | One | ✅ applied |
| Conversion action "Calls From Ad Extensions" (6802290174) | Primary | Primary | Secondary | ✅ applied |
| Conversion action "Calls from ads (call extension, 60s+)" (7856876390) | New | none | AD_CALL, Phone call lead, primary, count one, 60 s, no value | ✅ applied |
| Call asset (08) 6830 1993 (48187391158) | Call conversion reporting | Disabled | Use resource-level action 7856876390 | ✅ applied |
| Callout "Over 37 Years Experience" (23107636156) | Campaign link | Linked | Removed from campaign | ✅ applied |
| Callout "Over 45 Years Experience" (431574926812) | New | none | Linked to campaign | ✅ applied |

Negatives added (phrase): painkillers, pills, ibuprofen, advil, medi rub, patch, patches, peptides, palmitoylethanolamide, hydrafil, deep heat, tens machine, posture corrector, brace, theragun, heating pad, stimulator, inverter, decompression machine, orthopaedic, orthopaedics, rheumatologist, pain specialist, injections, laminectomy, surgeon, massage, massages, acupuncture, acupuncturist, naturopath, pilates, reflexology, hydrotherapy, tcm, osteopath, symptoms, causes, what causes, bike riding, exercises, unwind chiropractic, thorpe street health, cove chiropractic, in sync chiropractic, my body chiro. Exact: [appointment].

## Failed or skipped
- "Reached Online Booking Page" (6523430333): counting Every → One was rejected by the API (IMMUTABLE_FIELD on a GA4 import). Not applied; it can be changed in the Google Ads UI.
- "Reached Online Booking Page" stays primary: Sara wants to sort out tracking first.

## Notes
- New ad schedule matches the clinic's hours on the website (Mon/Wed/Fri 8:30–11:00 and 13:00–17:30, Tue/Thu 8:00–12:30, Sat 8:30–10:45). The Mon/Wed/Fri morning slots (8:30–11:00) were not changed.
- Under Maximize Clicks, keyword-level max CPCs and the +10% schedule modifiers are ignored.
- A Google "Calls from ads" action (231909324) and a GA4 "Contact Us Submission" import (6523430324) had been removed in the past; reason unknown.
- Review around 2026-11-02: clicks per day, CPC, search terms, calls in WhatConverts.
