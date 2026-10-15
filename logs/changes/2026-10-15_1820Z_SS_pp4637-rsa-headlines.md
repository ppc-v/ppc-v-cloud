# PP4637: add 3 headlines and replace Treaty 6 description in the main RSA

- **When:** 2026-10-15 18:20 UTC (14:20 US Eastern, Sara)
- **Requested by:** SS
- **Approved by:** SS, approved the preview in chat ("sounds good! update the ads")
- **Platform:** Google Ads (API, AdService.MutateAds update)
- **Session:** https://claude.ai/code/session_016Up6We52M96cWUPBKbVTNr

## Changes
| Account | Entity (type, name, ID) | Field | Before | After | Result |
|---|---|---|---|---|---|
| PP4637 - Action Chiropractic (893-398-8418) | RSA 400135192233, ad group "Chiropractor Edmonton" (43343186356), campaign "Perfect Patients" (849188617) | Headline 13 | (empty) | Serving Edmonton Since 1998 | ✅ applied |
| same | same | Headline 14 | (empty) | Book Your Visit Today | ✅ applied |
| same | same | Headline 15 | (empty) | Chiropractor in Edmonton | ✅ applied |
| same | same | Description 3 | Proudly Rooted in Treaty 6 Territory, Serving Families Across Our Community | Serving Edmonton Since 1998. Hands-On Care For Back & Neck Pain. Book Your Visit Today. | ✅ applied |

API response: `customers/8933988418/ads/400135192233`. Verified afterwards: 15 headlines, 4 descriptions, ad ENABLED, policy APPROVED. Headlines 1–12, descriptions 1/2/4, final URL and paths unchanged.

## Failed or skipped
None. The copy of this RSA in ad group "Chiropractor Near" (43342995316, 0 impressions in 90 days) was left unchanged on purpose.

## Notes
- This is part of the Quality Score work (QS 1–2). SS is replacing the body of the /chiropractor-in-edmonton/ landing page with the draft in `accounts/pp4637-action-chiropractic/landing-page-chiropractor-in-edmonton-v2.html`. The URL stays the same, so no final URL change is needed.
- Follow-up: once the page is live, check it and watch QS, expected CTR and landing page ratings over 2–4 weeks before lowering the $23 ad group bid.
