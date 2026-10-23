# Inventory sheet: dated reminders in the Account Monitor Slack messages

- **When:** 2026-10-23 17:47 UTC (12:47 US Central, John's time)
- **Requested by:** JW (John): wanted the PP5825 Max Clicks → Max Conversions review to appear in his daily Slack heads-up on the right day
- **Approved by:** JW, approved the preview in chat ("Yes, go ahead … as long as it doesn't mess with any of the current logic or flows")
- **Platform:** Apps Script bound to the Vortala Ad Account Inventory sheet (script `1eatKDsUVvuawzBCdi5h-vYKZUSoAZ13Z3UrHq2g4ylBxmF9j82S6Lrvp`)
- **Session:** https://claude.ai/code/session_01RaxPZsTsPJiRg7UR4UL5vR

## Changes
| Where | Change | Before | After | Result |
|---|---|---|---|---|
| Script `Code` file | Saved a version as a rollback point | none | **Version 1**: "Before Owners & Notes reminders (JW, 2026-10-23)" | ✅ |
| `NOTE_COLS` | Two new ✎ columns after Note | Platform … Note ✎, Current owner (auto), Open flag codes (auto) (9 cols) | … Note ✎, **Remind on ✎**, **Reminder ✎**, Current owner (auto), Open flag codes (auto) (11 cols) | ✅ code saved |
| `readNotes_` | Reads A:I; finds the reminder columns by header name, so the current 9-column tab gives no reminders and isn't misread | A:G by position | A:I; owner/snooze/note still by position (unchanged), reminders by header | ✅ code saved |
| `notesTab_` | Writes/format the new columns (date format and date validation on Remind on; ✎ background D:I; grey auto columns J:K); intro text mentions reminders | | | ✅ code saved |
| `buildBook_` | Carries `remind_on` / `reminder` onto each account row | | | ✅ code saved |
| `digestText_` | New "⏰ Reminders" section under the header of the daily and Monday messages: the owner's accounts whose Remind on date ≤ today, until the cells are cleared (Arif's all-accounts message shows all) | | | ✅ code saved |

Pending (scheduled check-in after the 24 Oct 06:00 GMT+8 refresh, trigger `trig_01BAoUKX3dV8J1CroscQAHhL`): confirm the tab layout, then set PP5825 (464-210-2599) Remind on 2026-11-06, Reminder "Review Max Clicks data (CPC, conversions); switch to Max Conversions if there are enough data points".

## Failed or skipped
- None. Manifest (`appsscript`) unchanged. Read-back confirmed the live code matches the edited file.

## Notes
- Checked before applying: nothing else reads Owners & Notes by position (other references use the tab's sheet ID only). There's no data beyond column I, and the 5 rows with manual entries are carried over. The basic filter is rebuilt to the new width by the same refresh.
- Tested locally: syntax check passed, and `readNotes_` was tested against both the old and the new layout.
- Rollback: restore script version 1 (Apps Script editor → Project history, or the API).
- Arif maintains this script and the bot; John to give him a heads-up.
