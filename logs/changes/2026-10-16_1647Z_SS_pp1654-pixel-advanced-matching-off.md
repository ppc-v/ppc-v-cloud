# PP1654: automatic advanced matching turned off on the Meta pixel

- **When:** 2026-10-16 16:47 UTC (12:47 US Eastern, Sara)
- **Requested by:** SS
- **Approved by:** SS, in chat ("if advanced matching isn't recommended then please turn it off")
- **Platform:** Meta
- **Session:** https://claude.ai/code/session_01L7HCWStozQv2YmJHW1GfSp

## Changes
| Account | Entity (type, name, ID) | Field | Before | After | Result |
|---|---|---|---|---|---|
| PP1654 - Goffstown Chiropractic Care (act_3615153821950382) | Pixel "PP1654 - Goffstown Chiropractic Care Pixel" (654754024942013) | enable_automatic_matching | true (fields em, fn, ln, ph, ge, zp, ct, st) | false | ✅ applied, confirmed by re-read |

## Failed or skipped
None.

## Notes
- Reason: the team's default rule (CLAUDE.md, until a HIPAA policy is set) is not to send patient identifiers to ad platforms; automatic matching hashed form fields from a healthcare site and sent them to Meta.
- The site's own pixel code (`fbq('init', '654754024942013')`) passes no manual matching data.
- Expect slightly lower event match quality and possibly fewer attributed conversions.
