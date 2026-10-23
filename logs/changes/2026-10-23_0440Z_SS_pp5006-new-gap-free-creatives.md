# PP5006 Meta: new Gap Free + doctor creative ads (paused)

- **When:** 2026-10-23 04:40 UTC (00:40 US Eastern for Sara; 12:40 in the account's Perth time)
- **Requested by:** SS
- **Approved by:** SS, approved the recommendations and creative direction in chat on 2026-10-22 and asked for the ads to be created paused for her review. Created by a scheduled retry once the Meta app was switched to Live.
- **Platform:** Meta
- **Session:** https://claude.ai/code/session_01EiVWQEthbRXB2zN1t6GazV

## Changes
| Account | Entity (type, name, ID) | Field | Before | After | Result |
|---|---|---|---|---|---|
| PP5006 - Kinross Drive Dental (act_161921765664666) | Ad "Gap Free + Dr Tisa - Oct 2026" (120252558859100105), creative 2532923500537524, ad set Doc/Emergency Ads - Lead Gen (120233567021590105) | Created | - | **Paused**. Image pp5006_gapfree_tisa_1x1 on Feed, pp5006_gapfree_tisa_9x16 on Stories/Reels; form 896201482847065 "No Gap NPS"; CTA Get Offer; headline "Gap Free New Patient Visit" | ✅ created, in processing, no issues |
| same | Ad "Gap Free + Dr Brigitte - Oct 2026" (120252558859840105), creative 29289616133989982, same ad set | Created | - | **Paused**. Same setup with the Brigitte images | ✅ created, in processing, no issues |

Preview links: Tisa https://fb.me/1WUNXTBeA1wjTCD, Brigitte https://fb.me/25moMXaZev96MuJ

## Failed or skipped
- Attempts at 21:35, 22:36 and 00:38 UTC failed with error 1885183 (Meta app in Development mode). After the switch to Live, the first try failed with 3858504 ("Creative should not include standard enhancements"): the `standard_enhancements` bundle is no longer accepted. Fixed by opting out per feature instead (advantage_plus_creative, text_optimizations, enhance_cta, ads_with_benefits all OPT_OUT).

## Notes
- Primary text and creative files: `accounts/pp5006-kinross-drive-dental/creative/2026-10-gap-free-doctors/`.
- SS switches them on after review. Budget unchanged (AUD 23/day campaign).
