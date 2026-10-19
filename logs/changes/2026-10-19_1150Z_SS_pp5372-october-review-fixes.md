# PP5372: October review fixes (keyword, ads, business name, location option, search partners)

- **When:** 2026-10-19 11:50 UTC (07:50 US Eastern, Sara's usual timezone)
- **Requested by:** SS
- **Approved by:** SS, approved items 1–8 of the review preview in chat ("go ahead with 1-8")
- **Platform:** Google Ads
- **Session:** https://claude.ai/code/session_01VgSYjWu1NiKzKt5EMX3TyQ

## Changes
| Account | Entity (type, name, ID) | Field | Before | After | Result |
|---|---|---|---|---|---|
| PP5372 - Mason Spine & Injury Center (796-011-4833) | Keyword "chiropractor near me" broad, ad group Chiropractor (113333303926~564075452) | Status | Enabled | Paused | ✅ applied |
| PP5372 (796-011-4833) | Call-only ad 712072234497, ad group Chiropractor | Status | Enabled | Paused | ✅ applied |
| PP5372 (796-011-4833) | Campaign "Perfect Patients" (11773819584), business name asset 424255983143 "Mason Spine&Injury Center" | Campaign asset link | Not linked (no business name on the campaign) | Linked (status Eligible) | ✅ applied |
| PP5372 (796-011-4833) | RSA 612949126771, ad group Chiropractor (ad strength Good) | Status | Paused | Enabled | ✅ applied |
| PP5372 (796-011-4833) | RSA 612948941659, ad group Chiropractor Near Me (ad strength Good) | Status | Paused | Enabled | ✅ applied |
| PP5372 (796-011-4833) | Campaign "Perfect Patients" (11773819584) | Location option | Presence or interest | Presence | ✅ applied |
| PP5372 (796-011-4833) | Campaign "Perfect Patients" (11773819584) | Search Partners | On | Off | ✅ applied |

API resource names returned: `adGroupCriteria/113333303926~564075452`, `adGroupAds/113333303926~712072234497`, `campaignAssets/11773819584~424255983143~BUSINESS_NAME`, `adGroupAds/113333303926~612949126771`, `adGroupAds/122823606198~612948941659`, `campaigns/11773819584`. All re-read and confirmed after applying.

## Failed or skipped
- Item 2 (negative keywords), the radius part of item 6 and item 8 (ad schedule) are not applied yet. They need specific values previewed and approved first.
- Item 4: the preview said "Mason Spine & Injury Center", but that is 27 characters and business names allow 25. Linked Sara's existing 23 Sep asset "Mason Spine&Injury Center" instead.
- Item 5: re-enabled the two "Good" ads rather than unpinning headlines on 484318240972, which stays as is.

## Notes
- Reason: October leads fell to 2 (from 14 in September). The broad keyword took 87% of October spend on condition and medication searches, and the call-only ad got about 28% of impressions with almost no clicks.
- Watch: the broad "Chiropractor near me" keyword in ad group Chiropractor Near Me ($8 bid) is still enabled and may now pick up the same searches.
