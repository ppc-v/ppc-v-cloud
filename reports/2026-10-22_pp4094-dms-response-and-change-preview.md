# PP4094 – Palmetto Smiles of Charleston: response to DMS and change preview

Requested by: SS (Sara), 2026-10-22. Builds on `2026-10-22_pp4094-account-review.md`. **Nothing has been changed yet**: part B is a preview awaiting Sara's approval.

---

## A. Response to the DMS (draft for Sara to send)

Hi,

Thanks for flagging Amy's concerns. I've reviewed the account in detail, and here's where things stand and what we're proposing.

**What's behind the decline**
- **Ad traffic hasn't dropped, but calls from the ads have.** Comparing Jan–Mar 2026 (before the breach) with Jul–Sep 2026, spend and clicks are about the same (~$2,500 and ~140 clicks a month). Over the same period, answered calls from the ads fell from 86 to 32, and clicks on our ad in Google Maps fell from 167 to 73.
- **Why:** when the account was restored after the breach, the keywords that drove most calls ("dentist" and "dentist charleston", phrase match) ended up with little or no spend. A broad-match "dentist" keyword now takes about 40% of the budget and attracts lower-intent searches (dental implants for seniors, insurance questions, "cheap" dentist). Because more searches are now lost to budget (45–54%, up from 27–42%), the ads also show less often in Google Maps, which is where most calls used to come from.
- **Organic rankings have dropped, but that isn't related to the Google Ads breach.** Paid ads and organic rankings are separate systems. Search Console shows organic clicks down about a third year on year. Positions on their key terms slipped: "holistic dentist charleston sc" from 1.9 to 5.0, and "dentist north charleston sc" from 4.7 to 12.3. I'd recommend the SEO team reviews this alongside us.
- **Reporting:** before the breach, Google Ads counted each call twice, so older conversion numbers look higher than they really were. Since a cookie banner was added to the website, online form submissions are only counted for visitors who accept cookies, so forms now look lower than they really are.

**1. Audience targeting**
- **Current setup:** 3–5 mile radius around the office, Mon–Thu, mostly mobile.
- **North Charleston vs Charleston:** North Charleston users convert at about a third of the cost of Charleston city users, so we'll focus spend there.
- **New audiences worth testing:**
  - People looking for a dentist without insurance (see the Dental Wellness Plan below).
  - Holistic/biological dentistry. This is a real differentiator and something they already rank for organically.
  - Spanish-speaking patients, since the office speaks Spanish.

**2. Budget recommendations**
- Google's "recommended budget" is recalculated automatically from week to week, which is why it keeps moving. It isn't a sign that anything has changed.
- The current $2,500/month is spent in full each month (ads run Mon–Thu, during office hours), but not efficiently:
  - The broad "dentist" keyword costs about $185 per lead, compared with $55 for "dentist near me".
  - About 13% of spend runs before the office opens at 7:30am.
- We'll reallocate first, before asking for any increase.

**3. Local opportunities**
- The biggest opportunity is getting back into Google Maps ad placements, which drove most calls before the breach.
- Search terms show people comparing local practices on price and insurance, which supports promoting the Dental Wellness Plan.

**4. Tracking and cookies**
- Yes, the website's opt-in cookie banner is reducing the number of form submissions we can record. Calls are unaffected.
- We'll set up Google's Consent Mode correctly (which respects visitors' choices and lets Google estimate the conversions it can't see) and add form tracking through our call-tracking platform.
- We'll also ask the practice for a monthly count of new patients from Google, so we can show real results.

**5. Dedicated landing page forms**
- Agreed. We'll give each landing page its own form and conversion (general, emergency, wellness plan), so we can show which campaign each enquiry came from.
- We need access to the site's Google Tag Manager and Analytics to set this up.

**6. Campaign performance**
- **What we're changing now:**
  - Restoring the keywords that performed well before the breach.
  - Pausing the broad "dentist" keyword and blocking irrelevant searches.
  - Matching the ad schedule to office hours (no ads before 7:30, or after 2:30 on Tue/Thu).
  - Fixing an ad typo and adding a second, refreshed ad to every ad group.
  - Cleaning up how calls are counted so reporting is accurate.

**Dental Wellness Plan ($348/year)**
- **Worth testing.** Since July, people searching for a dentist without insurance, "affordable" dentists and payment plans have already cost about $1,570 of the budget. Those clicks currently land on the general page, which doesn't mention the plan.
- **What we propose:**
  - A dedicated "No Insurance? No Problem" campaign, sending people to the existing Dental Wellness Plan page.
  - Ads highlighting "Exams & X-Rays Included", "10% Off All Treatment" and "No Deductibles or Waiting Periods".
  - Its own tracking number and enquiry form, so we can report plan enquiries separately.
- **Budget:** about $500/month. This can be funded from the savings above (cutting the broad keyword and pre-opening hours frees around $700/month), or added on top if Amy prefers to keep the main campaign at its full level.
- **Needs Amy's approval** of the offer wording first. We'd also ask her to tell us monthly how many plan sign-ups mention Google.

**Proposed plan for the conversation with Amy**
1. **This week:** keyword, schedule and ad fixes (already prepared).
2. **Next 2–4 weeks:** launch the Dental Wellness Plan test (once Amy approves), test a holistic dentistry ad group, and fix form tracking (we need website tracking access).
3. **Monthly reporting:** calls from ads, Google Maps clicks, form enquiries, and the practice's own new-patient count from Google.
   - Starting point: about 11 answered ad calls a month.
   - Target: back towards 29 a month, the level before the breach.
4. **Budget:** keep $2,500 and reallocate; add $500/month only if Amy wants the Wellness Plan test without trimming the main campaign.
5. **Rankings:** SEO team to review organic positions separately.

Happy to talk any of this through before the call.

Thanks,
Sara

---

## B. Change preview: Google Ads 505-760-9128, campaign "Smile Marketing" (338034390)

**Budget effect:** none. The daily budget stays $144.25, and the monthly cap stays $2,500 (Salesforce budget, enforced by the team's monthly rule). The changes move the same spend onto better-performing keywords and hours. The keyword bid changes are listed with their per-click effect.

### B1. Keywords and bids
| # | Ad group | Keyword | Current | New | Why |
|---|---|---|---|---|---|
| 1 | General Dentistry | `dentist` PHRASE (22037152) | Paused (would use ad group bid $19.00) | **Enabled**, $19.00 | Top performer Jan–Mar: $2,335, 31.8 conv |
| 2 | General Dentistry | `dentist` BROAD (10191500) | Enabled, $28.00 bid | **Paused** | $3,692 since Jul for 20 conv ($185 each); low-intent matches |
| 3 | Charleston Dentist | `dentist charleston` PHRASE (297457473305) | Enabled, $10.00 bid | **$20.00** | Top performer Jan–Mar at ~$19.38 CPC; at $10 it gets almost no traffic ($71 since Jul) |

Max CPC effect: #1 adds a keyword at up to $19/click; #3 doubles the ceiling from $10 to $20 per click. Total spend can't exceed the $2,500 cap.

### B2. Negative keywords: add to shared list "Negative Search Terms" (10925853225), phrase match
`ssi` · `veterans` · `disabled` · `oral specialist` · `periodontist` · `charleston periodontics` · `clear choice` · `best life` · `temporary dental insurance` · `financing pre approval` · `no money` · `sheldon dental` · `palmetto family dentistry` · `gentle family dentistry`

None of these is already in the account's negative lists. Deliberately **not** blocked: implants (they offer them), Cigna/BCBS/Tricare (check which plans they're in network with), and "affordable"/"no insurance" (these move to the Wellness Plan campaign later).

### B3. Ad schedule (remove and recreate; the schedule can't be edited in place)
| Day | Current | New (office hours) |
|---|---|---|
| Monday (302465) | 6:00–16:15 | **7:30–16:30** |
| Tuesday (312465) | 6:00–16:15 | **7:30–14:30** |
| Wednesday (322465) | 6:00–16:15 | **7:30–16:30** |
| Thursday (332465) | 6:00–16:15 | **7:30–14:30** |

Fri–Sun stay off ("Fri by appt"). Ad schedule times use the account's timezone (US Eastern, which matches Charleston).

### B4. Ads
**Fix typo** in the Emergency Dental RSA (653846618131): headline "Insurance Accpeted" → **"Insurance Accepted"** (pin position 2 kept). Everything else stays the same.

**Add one new RSA per ad group** (the current ads stay live, so we can compare them):

| Ad group | Final URL |
|---|---|
| General Dentistry | /north-charleston-dentist/ |
| Charleston Dentist | /north-charleston-dentist/ |
| Emergency Dental | /emergency-dentist-in-charleston/ |
| Dentist Near | /north-charleston-dentist/ |

Each keeps the current UTM tags and has 12 headlines and 4 descriptions. Only the brand/offer headline is pinned to position 1, to give Google more combinations than the fully pinned current ads.

- **General Dentistry** (path: dentist / charleston)
  - **Headlines:** Palmetto Smiles of Charleston [pin 1] · North Charleston Dentist · $189 New Patient Special · Same-Day Appointments · Gentle Family Dentistry · Complimentary Nitrous Oxide · Mercury-Free Dentistry · Se Habla Español · Most Insurance Accepted · Payment Plans Available · 5-Star Rated Local Dentist · Book Your Visit Today
  - **Descriptions:** New Patients: $189 Exam, X-Rays, Cleaning, Photos & Fluoride. Call Or Request Online. · Gentle Family Dentistry On W Montague Ave. Sedation Options For Anxious Patients. · In Network With Many Insurance Plans. CareCredit & Cherry Financing Available. · Same-Day Appointments Available. Friendly Team, Modern Care. Call (843) 554-3300.
- **Charleston Dentist** (path: dentist / charleston)
  - **Headlines:** Dentist In North Charleston [pin 1] · Palmetto Smiles of Charleston · $189 New Patient Special · Same-Day Appointments · Serving Charleston & Hanahan · Mercury-Free Dentistry · Complimentary Nitrous Oxide · Most Insurance Accepted · Payment Plans Available · 5-Star Charleston Dentist · Se Habla Español · Book Your Visit Today
  - **Descriptions:** New Patients: $189 Exam, X-Rays, Cleaning, Photos & Fluoride. Call Or Request Online. · Trusted Charleston-Area Dentist For The Whole Family. Gentle, Comfortable Care. · In Network With Many Insurance Plans. CareCredit & Cherry Financing Available. · Same-Day Appointments Available. Friendly Team, Modern Care. Call Today!
- **Emergency Dental** (path: emergency / dentist)
  - **Headlines:** Emergency Dentist Charleston [pin 1] · Same-Day Emergency Visits · Toothache? Call Us Now · Palmetto Smiles of Charleston · Broken Or Chipped Tooth? · Get Out Of Pain Today · Gentle, Calming Care · Sedation Options Available · Most Insurance Accepted · Financing Available · $189 New Patient Special · Call (843) 554-3300
  - **Descriptions:** Tooth Pain, Swelling Or A Broken Tooth? Call Now For A Same-Day Emergency Visit. · Gentle Emergency Care In North Charleston. Nitrous Oxide Available For Comfort. · In Network With Many Insurance Plans. CareCredit & Cherry Financing Available. · Don't Wait In Pain. Our Team Will Get You Seen Fast. Call (843) 554-3300 Today.
- **Dentist Near** (path: northcharleston / dentist)
  - **Headlines:** Dentist Near You [pin 1] · Palmetto Smiles of Charleston · $189 New Patient Special · Same-Day Appointments · Accepting New Patients · Gentle Family Dentistry · Mercury-Free Dentistry · Complimentary Nitrous Oxide · Most Insurance Accepted · Payment Plans Available · Se Habla Español · 5-Star Rated Local Dentist
  - **Descriptions:** New Patients: $189 Exam, X-Rays, Cleaning, Photos & Fluoride. Call Or Request Online. · Your Local North Charleston Dentist. Gentle Care For Kids, Adults & Seniors. · In Network With Many Insurance Plans. CareCredit & Cherry Financing Available. · Same-Day Appointments Available. Friendly Team, Modern Care. Call (843) 554-3300.

All headlines are 30 characters or fewer and all descriptions 90 or fewer. Every claim comes from the website or the existing ads/callouts ($189 special, same-day appointments, complimentary nitrous, mercury-free, Se habla español, insurance, CareCredit/Cherry).

### B5. Conversion settings
| Conversion action | Current | New |
|---|---|---|
| Calls from Ad Extensions (6807311652) | Every call counted | **One per click** |
| Calls from Google Ads (6807204373) | Every call counted | **One per click** |
| Appointment Request (Current Patient) (6522332335) | Primary | **Secondary** (existing patients shouldn't steer bidding) |

Manual CPC bidding doesn't optimise on conversions, so this changes reporting only, not delivery.

### B6. Held for Amy's approval / access (not part of this batch)
- **Dental Wellness Plan campaign:**
  - Search, created **paused**, ≈$29/day on the same Mon–Thu schedule (≈$500/month).
  - Keywords for no-insurance / affordable / membership-plan searches; final URL /dental-wellness-plan/.
  - Its own WhatConverts number and a "Wellness Plan enquiry" form conversion.
  - Plus a Wellness Plan sitelink in the main campaign.
- **Holistic / Biological Dentistry ad group** test (the paused group can be refreshed).
- **Consent Mode setup and per-page form conversions:** need GTM-P4VKDWZ Publish access and GA4 Editor access.
