# PP5006 - Kinross Drive Dental

- **Google Ads ID:** (Google side labelled Canceled in the inventory)
- **Meta ad account ID:** act_161921765664666 (AUD, Australia/Perth, brand: Smile Marketing)
- **Facebook Page:** 801344560257145. SS gave the Claude system user Page access on 2026-10-22: it can create ads from existing creatives and read the lead forms (with a Page token). New creatives fail until the Meta app is switched from Development to Live (error 1885183).
- **WhatConverts profile:**
- **GTM container / GA4 property:**
- **Access:** normal
- **Usually worked on by:** Sara

## Goals and preferences
- Leads on a limited budget (AUD 23/day campaign budget, about AUD 700/month).
- **The client wants ads running for every dentist** (SS, 2026-10-23). Don't pause a doctor's only ad for performance reasons; keep at least one live ad per doctor.

## Setup (as of 2026-10-22)
- One campaign, `PP5006 - Lead Gen` (Leads objective, Advantage campaign budget AUD 23/day, lowest cost).
- Two active ad sets with identical targeting (10 mi radius around 59 Kinross Dr, age 20-65+, Advantage+ audience, Advantage+ placements, instant forms, 1-day click):
  - `Doc/Emergency Ads - Lead Gen`: "meet the dentist" ads, form 4210232982583203.
  - `Gap Free NPS - Lead Gen`: gap-free new patient offer, form 896201482847065. Learning Limited. **Paused 2026-10-22; its ads now run in Doc/Emergency.**
- Archived 2026-10-22: Mouthguard Promo, Father's Day Whitening Offer, Gap Free/Use It Or Lose It (Nov 2025: AUD 300, 4 leads, CPL AUD 75), Gap Free NPS.

## Creative
- The client supplies the doctor photos. The house style is a navy background, logo top left, white dot grid, framed photo on the right, and kddental.com.au bottom right.
- 2026-10-22: drafted gap free + doctor creatives (1:1 and 9:16) in `creative/2026-10-gap-free-doctors/`. SS is fine with offer creative that resembles the doctor ads.

## Tracking
- Lead forms (all "Higher intent", first name / last name / phone / email only): 896201482847065 "No Gap NPS" (offer ads), 4210232982583203 "No Gap NPS-copy" (doctor ads).
- Leads are Meta instant forms (on-Facebook), so the pixel isn't used for leads ("Pixel never fired" in the inventory is expected).

## History and decisions
- 2026-10-22 SS: asked for recommendations to get more leads on the limited budget. Review: `reports/2026-10-22_pp5006-meta-review.md`.
- 2026-10-22: every ad in Doc/Emergency shows "Update required", error 3858385 ("Please authenticate your account"). Ads keep running, but nothing can be created or edited until someone authenticates in Ads Manager.
- 2026-10-22 SS: approved all review recommendations. Applied: Doc/Emergency placements set to FB feed + stories + reels only (log `2026-10-22_2048Z_SS_pp5006-placements.md`). Still to do (needs Page access or a person in Ads Manager): merge the Gap Free ads into Doc/Emergency and pause Gap Free NPS, publish the new creatives, switch the lead forms to Higher intent and add a private health cover question. Then confirm with the client that Meta should keep running while Google is canceled.
- 2026-10-22 SS: merged Gap Free ads 2 and 4 into Doc/Emergency and paused the Gap Free NPS ad set (log `2026-10-22_2055Z_SS_pp5006-merge-adsets.md`). The new creative images are in the ad account's image library, but no ads use them yet.
- 2026-10-22 ~21:15 UTC: the authentication block (3858385) has cleared. All Doc/Emergency doctor and emergency ads now show the HARD_ERROR "Missing lead form" (3390001), although their creatives point to form 4210232982583203. Fix in Ads Manager: re-select the instant form on each ad and publish. The Gap Free 2 and 4 ads are unaffected.
- 2026-10-22 21:30 UTC SS: fixed the missing lead form on the live ads in Ads Manager (all clear now). Archived the paused ad sets (Father's Day, Mouthguard, Use It Or Lose It, Gap Free NPS) and the old holiday/general ads. Kept Dr Jieun Kim and Dr Anvitha (paused) for future use; re-select the form before switching them on. Log `2026-10-22_2130Z_SS_pp5006-archive-cleanup.md`.
- 2026-10-23 04:40 UTC: created "Gap Free + Dr Tisa - Oct 2026" and "Gap Free + Dr Brigitte - Oct 2026" **paused** in Doc/Emergency for SS to review (log `2026-10-23_0440Z_SS_pp5006-new-gap-free-creatives.md`).
