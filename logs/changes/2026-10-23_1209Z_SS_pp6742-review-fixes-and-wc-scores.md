# PP6742: Google Ads review fixes + WhatConverts call scores

- **When:** WhatConverts 2026-10-23 12:09 UTC; Google Ads 12:10 UTC (08:09 / 08:10 US Eastern, which is also the account's timezone)
- **Requested by:** SS
- **Approved by:** SS, in chat: "keep New Patient Book Now Page View as primary but switch the other to secondary. Approve all others."
- **Platform:** WhatConverts, Google Ads
- **Session:** https://claude.ai/code/session_01EiVWQEthbRXB2zN1t6GazV

## Changes
### WhatConverts (profile 171730): quotable
| Lead ID | Before | After | Reason |
|---|---|---|---|
| 258412043 | No | Yes | New patient booking (next-day consult offered) |
| 261243128 | No | Yes | New patient confirming 5:45pm booking (voicemail) |
| 252141431 | No | Yes | Prospective patient, cost/insurance enquiry |
| 261846172 | No | Yes | Voicemail enquiry about care for husband |
| 255023143 | Pending | Yes | Voicemail: referred, appointment for wife |
| 258747094 | Pending | Yes | Voicemail: referred by trainer, wants appointment |
| 263427131 | Not Set | Yes | Voicemail: acute pain, asks for availability |
| 263433277 | Not Set | Yes | Voicemail: online booking for $199 special failed |
| 263661742 | Not Set | No | Duplicate of 263433277 (same number, next day) |
| 258286612 | Pending | No | Asked for children's physicals (not offered) |
| 263452713 | Not Set | No | Menu + voicemail, no message |
| 263731615 | Not Set | No | 6s hang-up |
All read back ✅.

### Google Ads: PP6742 (288-398-9795), campaign "Perfect Patients" (24043812427), paused by the budget rule until 1 Nov
| Entity | Field | Before | After | Result |
|---|---|---|---|---|
| Conversion action "Calls from ads" (7708209586) | Primary | Primary | Secondary | ✅ read back |
| Conversion action "New Patient Book Now Page View" (7691500922) | - | Primary | Primary (kept, per SS) | - |
| Campaign | Bid strategy | Maximize conversions | Manual CPC (no eCPC) | ✅ |
| Budget | Daily | USD 90 | USD 90 (unchanged) | - |
| Chiropractor Huntersville (198736472095): chiropractor huntersville phrase (306597887936) + exact (363237084154), huntersville chiropractor exact (363237087554) | Max CPC | - | USD 20 | ✅ |
| Chiropractor Near (198875873976): chiropractor near me phrase (24314362356) + exact (24315031836) | Max CPC | - | USD 20 | ✅ |
| Chiropractor (193686081770): chiropractor exact (70618091) | Max CPC | - | USD 18 | ✅ |
| Chiropractor: chiropractor phrase (20640151), back pain chiropractor phrase (677899681) + exact (752947702), network spinal exact (335309128467), network spinal near me phrase (846351157338) + exact (1638404188450) | Max CPC | - | USD 16 | ✅ |
| Broad: chiropractor (12457821), back pain chiropractor (490534244), network spinal (384286292567), network spinal near me (1692172268767), chiropractor huntersville (373138165190), chiropractor near me (564075452) | Status | Enabled | Paused | ✅ |
| New keyword "huntersville chiropractor" phrase (306597893456), Chiropractor Huntersville | Created | - | Enabled, USD 20 (HEALTH_IN_PERSONALIZED_ADS exemption requested) | ✅ |
| Shared list "Search Queries" (12186248133) | Added 23 phrase negatives | - | orthopedic · orthopedics · neurosurgery · pain center · dry needling · prolotherapy · shock wave · spinal decompression machine · cauda equina · ear infection · medicaid · twins chiropractic · harmony chiropractic · atkinson chiropractic · cook chiropractic · shook family chiropractic · nucca · renoja · innovation health · adam fields · nevin markel · atlas orthogonal · upper cervical | ✅ |
| New unpinned RSAs (same headlines/descriptions/paths/URLs as the pinned ones, which are unchanged): 829431853151 (Chiropractor, copy of 817139155867), 829431838232 (Chiropractor Near, copy of 817243080429), 829308669003 (Chiropractor Huntersville, copy of 817349698997) | Created | - | Enabled | ✅ in review |

## Failed or skipped
- First validation of "huntersville chiropractor" (phrase) hit HEALTH_IN_PERSONALIZED_ADS (exemptible); resubmitted with the exemption.
- Not done (SS's side): WhatConverts 45s+ call rule; phone/IVR and voicemail follow-up with the client; GA4/GTM access (SS working on GTM).

## Notes
- 6 of the 8 quotable new-patient calls since late July reached voicemail during ad hours; one caller said online booking for the $199 special failed.
- Check pacing after the first week of November.
