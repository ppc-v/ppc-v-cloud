# PP1654: attempt to fix Pediatric AdSet conversion goal (not applied)

- **When:** 2026-10-16 16:38 UTC (12:38 US Eastern, Sara)
- **Requested by:** SS
- **Approved by:** SS, approved preview in chat
- **Platform:** Meta
- **Session:** https://claude.ai/code/session_01L7HCWStozQv2YmJHW1GfSp

## Changes
| Account | Entity (type, name, ID) | Field | Before | After | Result |
|---|---|---|---|---|---|
| PP1654 - Goffstown Chiropractic Care (act_3615153821950382) | Ad set "Pediatric AdSet" (120252802707410220), campaign "PP1654 - Lead Gen Campaign" (120252802465590220) | promoted_object (conversion event) | Custom conversion "Appt Requests" (2025667461473803, archived, LEAD) | Custom conversion "Appt Form Submission" (1107897131731829, OTHER) | ❌ rejected by Meta, nothing changed |

## Failed or skipped
- Attempt 1 (promoted_object without pixel_rule): error 100 / subcode 1885014 "Promoted Object Invalid".
- Attempt 2 (with the conversion's pixel_rule): error 100 / subcode 3260011 "Can't make edits to published ad set": Meta doesn't allow the pixel, conversion event, custom conversion or optimisation to change once an ad set is published. Re-read afterwards: the ad set is unchanged and still active.

## Notes
- Why: "Appt Requests" ANDs two URL conditions (`/info/new-patient-thank-you/` and `/info/current-patient-thank-you/`), so it can never fire, and it's archived. The ad set was optimising for an event Meta will never see.
- Fix needs a new ad set with the right goal (proposed to SS as a separate preview).
