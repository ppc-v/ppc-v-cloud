# PP4094 – Palmetto Smiles of Charleston: account review and plan

Requested by: SS (Sara), 2026-10-22, ahead of a call with Amy (client) about falling rankings, calls and bookings after the April Google Ads breach. Read-only review; nothing was changed.

Sources: Google Ads 505-760-9128 (account timezone, US Eastern), WhatConverts profile 125372 (UTC), Search Console (palmettosmilesofcharleston.com, through 20 Oct), the website (checked 22 Oct), Salesforce ($2,500/month Google budget; $900 Meta, paused since 4 Aug).

"Before" = Jan–Mar 2026 (last full quarter before the breach). "Now" = Jul–Sep 2026 (first full quarter after the account came back). October to date is in line with "now".

## The short version
1. **Paid traffic didn't fall; paid *calls* did.** Spend and clicks are the same as before (≈$2,500 and ≈140 clicks a month), but calls from the ads fell by about 60% and Google Maps ad clicks by about 55%. The clicks moved from calls and Maps to website visits on broader, lower-intent searches (dental implants, insurance, "cheap" dentist).
2. **The main cause is how the campaign was rebuilt after the breach.** The keywords that drove most calls before ("dentist" and "dentist charleston" as phrase match) carry little or no spend now. A broad-match "dentist" keyword takes 40% of the budget at about $185 per conversion. With more searches lost to budget (45–57% vs 27–44%), the ads appear less often in the local/Maps results, which is where calls came from.
3. **Organic rankings did drop, but that's SEO, not the breach.** A Google Ads hack can't affect organic rankings. Search Console shows organic clicks down about a third year on year. Positions slipped on their niche terms ("holistic dentist charleston sc" 1.9 → 5.0) and on "dentist north charleston sc" (4.7 → 12.3). This needs the SEO team.
4. **Reporting understates and overstated at different times.** Before the breach, Google Ads counted calls twice (its own call action plus the WhatConverts import), so old "conversions" look higher than they really were. Since the site's cookie banner went in, form conversions only record for visitors who click "Accept", so forms now look lower than they really are.
5. **There's clear demand for the Dental Wellness Plan.** About a quarter of current search spend already goes to "no insurance", "cheap", "affordable" and payment-plan searches, but those people land on the general page with no mention of the $348/year plan.

## Before vs now
| | Jan–Mar 2026 | Jul–Sep 2026 | Change |
|---|---|---|---|
| Spend | $7,896 | $7,105 | −10% |
| Clicks (all types) | 406 | 427 | +5% |
| Calls from ads (Google call reporting, answered) | 86 | 32 (+13 missed) | **−63%** |
| Clicks on the ad in Google Maps / local results | 167 | 73 | **−56%** |
| Website clicks | 109 | 266 | +144% |
| Online "Appointment Request (New Patient)" (GA4) | ≈17 | 4 | −76% (partly the cookie banner, see 4) |
| Share of possible searches shown | 42–52% | 25–31% | down |
| Searches lost to budget | 27–42% | 45–54% | up |
| Avg cost per click | $18–21 | $15–18 | similar |

The account was hacked on 28 Apr (15 unauthorised campaigns spent about $230), then didn't run in May and June. It restarted in July.

## Answers to the six questions

### 1. Audience targeting
- **Today:** one Search campaign, manual CPC, 3- and 5-mile radius around 3188 W Montague Ave, Mon–Thu 6am–4pm. Mobile +15%, desktop and tablet −30%. Four ad groups are live: General Dentistry, Charleston Dentist, Emergency Dental and Dentist Near. Fourteen others are paused, including Holistic Dentistry, Mercury Removal, Sedation, Invisalign, Children's and the insurance groups.
- **Where it converts:** North Charleston users cost $106 per conversion; Charleston (city) users cost $335 per conversion on similar spend ($3,682, 11 conversions since July). Hanahan converts well on small volume.
- **Opportunities:**
  - **Holistic / biological dentistry.** This is their organic strength and differentiator, and there's local search for it ("holistic dentist charleston sc", "biological dentist charleston sc", "holistic dentist summerville sc"). It's a small, cheap, high-intent test, and it needs a slightly wider radius, since people travel for it.
  - **Affordable care / no insurance** (see the Dental Wellness Plan section).
  - **Spanish speakers.** "Se habla Español" is already in the ads; a Spanish ad group is worth testing if the office can handle the calls.
  - Lower bids for Charleston city users, or narrow the 5-mile ring, so the budget goes to North Charleston and Hanahan.
  - **Audiences** (observation only, to learn): in-market for dental services, recent movers to Charleston County.

### 2. Budget: why the "recommended budget" keeps changing
- Google's budget recommendation is recalculated automatically from recent lost impressions and competition, so it moves week to week. That isn't a signal that something changed in the account.
- Our setup also makes it look odd. The daily budget is $144, ads only run Mon–Thu, and the team's monthly rule pauses the account once the $2,500 Salesforce budget is reached, then restarts it on the 1st. Google sees a "limited" campaign and keeps recommending more.
- **Is the $2,500 spent well?** Not yet:
  - Broad "dentist" took $3,692 of $9,129 since July for 20 conversions ($185 each).
  - "Dentist near me" exact cost $55 per conversion; "emergency dentist" broad cost $90.
  - Searches about implants, Cigna, seniors, SSI and the like took about $700 with almost no conversions.
  - The 6–7:30am slot (before the office opens at 7:30) took $1,188 (13%) for 3 conversions.
  - Tuesday and Thursday ads run until 4pm, but the office closes at 2:30.

### 3. Local opportunities
- **Maps / local results are the biggest loss.** Clicks there fell from about 55 a month to about 24. The Business Profile is still linked to Google Ads, so the drop comes down to competitiveness (budget and bids), not a broken link. Getting the ads back into Maps is the fastest route back to calls.
- **Competitors and searches:** search terms show people looking for other practices (Palmetto Family Dentistry, Sheldon Dental, Gentle Family Dentistry, Charleston Periodontics) and comparing on price and insurance. Auction Insights in the Google Ads interface will show which competitors overlap most (not available through the API).
- **Organic (for the SEO team):** organic clicks are down from about 250 to about 165 a month (Jul–Sep 2025 vs 2026). Positions slipped on "holistic dentist charleston sc", "biological dentist charleston sc", "dentist north charleston sc" and "dentist charleston". The homepage and /holistic-dentistry/ bring most organic visits.

### 4. Tracking and cookies
- The site has an **opt-in cookie banner**: "We require your active consent". Google Analytics only loads after a visitor clicks Accept, and "Reject" also switches Google's consent signals off.
- **Every form conversion in Google Ads comes from Analytics,** so forms are only counted for people who accept. That's likely why "Contact Us Page" stopped recording after February and online appointment requests dropped.
- **Calls are not affected:** call-button calls are counted by Google directly, and WhatConverts tracks website calls.
- **Options** (consent must be respected; a team decision, since the banner is on Perfect Patients sites generally):
  - Turn on Google Consent Mode properly (a "denied" default, then update on choice), so Google can model conversions from people who decline. It records nothing about them.
  - Track form submissions in WhatConverts as well, under the same consent rules.
  - Report the practice's own new-patient-by-source numbers alongside Google's.
- **Hygiene:**
  - Two call conversion actions count every call per click; they should count once.
  - Three Analytics goals have no category.
  - "Appointment Request (Current Patient)" is a primary goal, which it shouldn't be.
  - The Meta pixel "Default Offline Event Set For Vortala" has never fired.
  - The GTM container (GTM-P4VKDWZ, "added by SEO") isn't shared with us, and there's no Analytics property we can see.

### 5. Dedicated forms per landing page
- **Yes, worth doing.** Give each landing page its own form (or a hidden "source page" field) and send each as its own conversion: "New Patient – General", "Emergency", "Wellness Plan enquiry". Then we can see which campaign produces bookings, and the practice can see the source on each enquiry.
- With the cookie banner, Analytics alone will undercount. Pair it with WhatConverts form tracking and Consent Mode (above).
- Never put treatment or health details in the conversion names or URLs. "Wellness plan" is fine; specific conditions aren't (team default until a HIPAA policy exists).

### 6. Campaign performance and ads
- **One ad per ad group, all "Average" strength.** Three of the four send people to /north-charleston-dentist/. There's a typo, "Insurance Accpeted", in the Emergency ad.
- **Quality Score:** "emergency dentist" 3/10 and "dentist near me" 4/10. These mean higher costs per click; a dedicated emergency page and tighter ad copy would help.
- **What to change:**
  - Bring back phrase "dentist" and "dentist charleston" (strong before the breach).
  - Cut broad "dentist" spend sharply and add negatives for implants-for-seniors, SSI, Cigna-type and "cheap" searches; send the affordability searches to the plan instead.
  - Add a second ad per group.
  - Move the schedule to 7:30–4:30 Mon/Wed and 7:30–2:30 Tue/Thu.
  - **Consider Maximize Conversions** once tracking is fixed. Manual CPC is struggling to win Maps placements.

## Dental Wellness Plan ($348/year: 2 exams, X-rays, screenings, iTero scan, 10% off treatment)
- **Fit:** strong. Searches like "how much is it to get teeth cleaned without insurance", "dental no insurance near me", "affordable dentist near me", "dentist that has payment plans" and "i need my teeth fixed but have no money" already cost about $1,570 since July. Today they land on a page about the $189 new-patient special.
- **Structure:** a separate "Affordable Dental Care / No Insurance" campaign, so it has its own budget and we can report on it cleanly. Keywords around no-insurance dentist, affordable dentist, dental membership/savings plan and dental cleaning without insurance, plus the existing affordability terms moved out of the main campaign.
- **Budget:** start at **$500/month**, either from reallocation (cutting broad "dentist" and the pre-opening hours frees about $700/month) or as a $500 increase if Amy wants to keep the core campaign intact. Review after 6–8 weeks; at current costs, expect 25–35 clicks a month.
- **Landing page:** use /dental-wellness-plan/ (already good) with a short form, "Join the plan / Book your first visit", a clear price-per-month framing ($29/month equivalent), what's included, the $189 special compared, the click-to-call number and reviews.
- **Ad messaging:** "No Insurance? No Problem", "$348/Year Dental Wellness Plan", "Exams, X-Rays & Screenings Included", "10% Off All Treatment", "No Deductibles or Waiting Periods". Add a sitelink and callout for the plan in the main campaign too.
- **Conversions:** calls via a dedicated WhatConverts number on that campaign, and a "Wellness Plan enquiry" form conversion. Ask the practice to tell us monthly how many plan sign-ups came from Google.
- Needs Amy's approval of the offer wording and pricing in ads.

## Recommended plan for the conversation with Amy
**Immediate (this week, with approval):**
1. Restore phrase "dentist" and "dentist charleston"; cut broad "dentist" and add the low-intent negatives.
2. Fix the schedule to office hours.
3. Fix the Emergency ad typo and add a second ad per group.
4. Count calls once per click; make "Current Patient" secondary.

**Next 2–4 weeks:**
1. Launch the Dental Wellness Plan campaign (start paused, switched on after Amy approves).
2. Test the Holistic/Biological ad group.
3. Request GTM and Analytics access; set up Consent Mode properly and per-page form conversions.

**Measurement:** report monthly on calls from ads (Google), Maps clicks, form enquiries and the practice's own count of new patients from Google. Today's starting point: about 11 answered ad calls a month, about 24 Maps clicks a month and about 1–2 online requests a month. The target is to get back towards Jan–Mar levels (about 29 calls and about 55 Maps clicks a month).

**Budget:** $2,500 is enough for the core campaign if it's reallocated as above. Add $500/month only if Amy wants the wellness-plan test without trimming the core campaign. Increasing the core budget would mainly recover lost Maps visibility, at about $18 a click.

**Organic rankings:** refer to the SEO team with the Search Console numbers above. They're separate from the ads, and the Google Ads breach didn't cause them.
