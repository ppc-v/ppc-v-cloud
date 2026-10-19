# PP5449: more negatives, callout cleanup, RSA copy and pinning

- **When:** 2026-10-19 17:19 UTC (13:19 US Eastern, Sara's usual timezone)
- **Requested by:** SS
- **Approved by:** SS. Approved the preview in chat ("approve"), then confirmed the trimmed version ("approve google ads changes") after two items were dropped.
- **Platform:** Google Ads
- **Session:** https://claude.ai/code/session_01SRANjNvhovjur1KiBgBKZp

## Changes
| Account | Entity (type, name, ID) | Field | Before | After | Result |
|---|---|---|---|---|---|
| PP5449 - Midwest Sport & Spine (756-376-8919) | Campaigns Noblesville (11560827514) and Greenwood (22208313305) | Campaign negative keywords, PHRASE (10 per campaign) | — | foxworthy, balanced chiropractic, graceful health, i u health, family health chiropractic, medscape, limiflex, cvs, name three, icd | ✅ applied |
| PP5449 | Campaigns Noblesville and Greenwood | Campaign negative keywords, EXACT (2 per campaign) | — | [health], [do near me] | ✅ applied |
| PP5449 | Callout "Open Evenings" (asset 23330420185) | Linked to Noblesville and Greenwood | Linked | Unlinked (asset kept in library) | ✅ applied |
| PP5449 | Callout "Free Consultations" (asset 201099821019) | Linked to Greenwood | Linked | Unlinked (asset kept in library) | ✅ applied |
| PP5449 | New callout "$49 New Patient Special" (asset 431578509961) | Linked to Noblesville and Greenwood | — | Linked | ✅ applied |
| PP5449 | New callout "On-Site Parking" (asset 431578512367) | Linked to Noblesville and Greenwood | — | Linked | ✅ applied |
| PP5449 | RSA 554378155105, Noblesville › Chiropractor Noblesville | Headline | "Free Consultations" (pinned 2) | "Exam & Treatment For $49" (unpinned) | ✅ applied |
| PP5449 | RSA 700320794076, Noblesville › Chiropractor Near Me | Headline | "Free Consultations" (pinned 2) | "Exam & Treatment For $49" (unpinned) | ✅ applied |
| PP5449 | RSA 700320794076 | Description | "Convenient, Affordable Chiropractor. Ins Accepted. Same-Day/Evening Appts - Call Now!" | "Convenient, Affordable Chiropractor. Ins Accepted. Same-Day Appts Available - Call Now!" | ✅ applied |
| PP5449 | RSA 732104525707, Greenwood › Chiropractor Near Me | Description | Same "Same-Day/Evening Appts" text | Same "Same-Day Appts Available" text | ✅ applied |
| PP5449 | RSA 732104525707 | Headlines | 9 | 15. Added "Trusted Greenwood Chiropractor" (pin 1), "Chiropractor In Greenwood" (pin 1), "Exam & Treatment For $49", "Same Day Appointment Available", "Insurance Accepted", "Flexible Hours" | ✅ applied |
| PP5449 | RSA 732104525710, Greenwood › Chiropractor | Headlines | 11, including "Free Consultations" and "Complimentary Consultations" | 15. Removed both consultation headlines. Added "Exam & Treatment For $49", "Top Greenwood Chiropractor" (pin 1), "Get Started For Just $49", "Same Day Appointment Available", "Insurance Accepted", "Sports & Family Chiropractic" | ✅ applied |
| PP5449 | All 4 RSAs above | Pinning | Every headline pinned to position 1, 2 or 3, and every description pinned to 1 or 2 | Location and keyword headlines stay pinned to position 1. All other headlines and all descriptions unpinned. | ✅ applied |

All other headline and description text is unchanged. After the update, all four ads are ENABLED, review PENDING, and approval still APPROVED.

## Failed or skipped
- Removed from the batch before applying, after a check of the client's website:
  - Negative "dryer": the Greenwood office was formerly Dyer Chiropractic, so "dryer chiropractor" is probably a misspelled brand search.
  - Noblesville description "In-Network W/ All Indiana Ins Companies…" left as is: the homepage says "in-network with all insurance providers in Indiana".
- No API errors. The batch was validated (validate_only) before it was applied.

## Notes
- Negatives come from 90 days of search terms with zero conversions. Condition searches (sciatica, stenosis, plantar fasciitis, lower back pain) were left running because the practice treats them, and "treatment for lower back pain in females" produced a lead.
- Old callout assets are unlinked, not deleted.
- Expect ad strength to rise from "Average" now that more headlines are unpinned. Check it after review.
- Landing page refresh (not yet published) is in `accounts/pp5449-midwest-sport-and-spine/landing-pages/`.
- Open follow-ups:
  - Greenwood ad schedule has no Friday, but the office is open Fri 6:30–2.
  - Reset the daily budgets on 1 Nov.
  - Someone needs to remove the hidden UA goal in the Google Ads UI.
  - paidsearch@ needs GTM and GA4 access.
