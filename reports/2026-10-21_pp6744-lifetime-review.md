# PP6744 – Gavric Chiropractic Clinic: lifetime review and booking tracking options

Requested by: SS (Sara), 2026-10-21. Read-only review; nothing was changed.

Windows: Google Ads 2026-04-01 → 2026-10-20 in the account's timezone (America/Chicago). WhatConverts 2026-04-08 (first call) → 2026-10-21, UTC. No Meta account in the inventory.

## Summary
- **The Perfect Patients campaign has spent $7,311 since 14 Apr 2026.** That bought 633 clicks, 81 calls from ads (Google call reporting) and 104 recorded conversions, about $70 per conversion.
- **About 6 confirmed new-patient bookings came from Google Ads calls** (3 Jul, 6 Jul, 22 Jul, 15 Sep, 23 Sep, 9 Oct). That's roughly $1,200 spend per booked new patient. Up to 2–3 more may have come via the GBP-labelled number in Apr–Jul, which gives a range of 6–9 bookings ($810–$1,220 each). "Booked" means booked on the call, estimated from WhatConverts' AI call summaries using the same method as `2026-09_whatconverts-calls-bookings.md`. It doesn't show whether the patient turned up.
- **About half the "conversions" are existing patients.** Of 76 WhatConverts calls proven to come from ads, 38 were existing patients and 17 were new patients. 21 were missed: they hung up within 6–37 seconds, and only 1 of those callers got through within 7 days. Brand searches ("gavric chiropractic…") produced at least 28 conversions, which suggests existing patients searching the practice name.
- **CPCs have roughly tripled while volume fell.** CPC was $6.29 in April and $21.63 in September. The $60/day budget runs into a ~$1,500/month cap, the campaign loses 31–77% of searches to budget, and the ad schedule is Mon–Fri 8–5 only.
- **Security incident, 27–28 Apr 2026.** 98 campaigns not created by us ("NHV-ADS-A79-…", one "AKR-…") spent **$1,304** in two days on spam and gambling-style searches ("dewi11", "badak178"): 5,762 clicks, 0 real conversions. All are now removed. The account then didn't serve from 28 Apr to 18 Jun, probably suspended or under recovery. This $1,304 is in the lifetime total ($8,615) but isn't ours. **Check whether Google credited it** (billing isn't visible through the API).

## Monthly (Perfect Patients campaign)
| Month | Spend | Clicks | Avg CPC | Conversions (primary) | Calls from ads (Google) | Lost IS to budget | New-patient bookings (confirmed, ads numbers) |
|---|---|---|---|---|---|---|---|
| Apr (from 14th) | $812 | 129 | $6.29 | 15 | 16 | 34% | 0 (+1 on GBP number) |
| May | $0 | – | – | – | – | – | account not serving |
| Jun (from 18th) | $832 | 123 | $6.76 | 18 | 13 | 31% | 0 (+0–1 GBP number) |
| Jul | $1,510 | 149 | $10.13 | 31 | 15 | 62% | 3 (+1 GBP number) |
| Aug | $1,521 | 91 | $16.72 | 14 | 14 | 77% | 0 |
| Sep | $1,514 | 70 | $21.63 | 18 | 17 | 33% | 2 |
| Oct 1–20 | $1,122 | 71 | $15.80 | 8 | 6 | 35% | 1 |
| **Total** | **$7,311** | **633** | **$11.55** | **104** | **81** | | **6 (6–9 with GBP number)** |

Conversions in Jun–Jul include 11 from Google's own "Calls from ads" action on top of the WhatConverts imports (double counting; that action was later removed). Store visits (6) are secondary and not counted.

Campaign setup: Search only, Maximize Conversions (no target), $60/day, radii 1/2/4/6 mi (presence), Mon–Fri 8:00–17:00, 210 excluded countries. Call asset (414) 797-6621.

## How tracking works today
| Lead path | Tracked? | How |
|---|---|---|
| Calls from the call asset | ✅ | WhatConverts number (414) 797-6621 → "Calls From Ad Extensions" (call import, primary, counts every call) |
| Calls from the website after an ad click | ✅ | WhatConverts number swap (414) 775-3142, with GCLID → "Calls From Google Ads" (click import, primary, counts every call) |
| Website forms ("Book an Appointment", Contact) | ⚠️ | GA4 imports "Appointment Request (New Patient)" and "Contact Us Submission" are primary but have recorded **nothing since July** (2 in Jun, 2 in Jul). GA4 property and both GTM containers (GTM-NZ6BNM2N, GTM-PX3V6953) aren't shared with paidsearch@, so we can't see why. |
| Online booking | – | No booking engine: the site uses form fills only (`2026-10-19_active-ppc-booking-engines.xlsx`). |
| New patient vs existing | ❌ in Google Ads | WhatConverts knows (phone menu choice + AI label), but every call goes to Google Ads as a conversion, so bidding learns from existing-patient calls too. |

The practice appears to answer many calls with an AI receptionist that books appointments on the call. That matters for booking tracking (below).

## If they stay: tracking a third-party booking engine
Do this once they've chosen an engine. Order of preference:

1. **Confirmation event on our domain (best).** The engine is embedded on gavricchiropractic.com as a widget or iframe and sends a confirmation event (dataLayer push, `postMessage` or JS callback). GTM listens for it → GA4 key event `booking_confirmed` → Google Ads conversion "Online Booking – New Patient" (primary, count One). The button click stays secondary.
2. **Engine-hosted page with GA4/GTM support.** Add our GTM/GA4 ID in the engine's settings, fire on the confirmation step only, and set up cross-domain measurement so the ad click (GCLID) carries over.
3. **Redirect to a thank-you page.** If the engine can send people back to a URL after booking, use a /booking-confirmed/ page on the site as the trigger.
4. **No tracking support.** Track "booking started" as secondary only. Count real bookings through an **offline conversion import**: pass the GCLID into the booking (hidden field or URL parameter the engine stores), then upload booked new patients weekly or monthly with GCLID + time only.

For every option:
- **Only new patients as the primary goal**, if the engine shows appointment type: send a plain `new_patient: true/false`, never the reason for visit.
- **No patient data to Google** (team default until a HIPAA policy exists): no names, emails, phone numbers, conditions, treatments or practitioner/service names in event names, parameters or URLs. **Leave Enhanced Conversions off.** Strip query strings and path segments the engine adds.
- **Avoid double counting.** If the booking engine replaces the "Book an Appointment" form, retire the form goal. A booking and a call from the same person both count unless we dedupe; that's acceptable, but say so in reports.
- **Test it.** Make a test booking (then cancel it). Check GTM preview, GA4 DebugView, then Google Ads conversion diagnostics after 24–48 h.

Prerequisites for Gavric specifically:
1. **GTM Publish access** to GTM-NZ6BNM2N and GTM-PX3V6953 (find out whose each is; probably one is the Perfect Patients site and one is the client's) and **GA4 Editor**. Without these we can't build options 1–3.
2. **Fix or retire the silent form goals** before adding a booking goal, so bidding isn't counting a dead goal.
3. **Phone bookings:** most bookings here happen on calls. Two options:
   - Import only new-patient calls as their own primary goal, using the phone-menu "New Patient" choice. This depends on what WhatConverts' Google Ads integration can filter on: check in the UI, or mark leads quotable.
   - If the AI receptionist / PMS can export booked new patients, add them to the offline import. Upload GCLID + time only.

## Other things to raise (preview before any change)
- Call conversion actions count every call per click; switch to One (as done on PP6773) and add a minimum call length (e.g. 30s).
- Confirm with Google whether the April $1,304 was credited, and check the account's users and 2-step verification. Today the only direct user is a read-only Perfect Patients login.
- Budget: at $15–22 CPCs, ~$1,500/month buys ~70–90 clicks. Either raise the budget, or narrow to the best keywords/hours so the budget covers them. Think about the 9–10 am and Friday missed calls with the practice.
