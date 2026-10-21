# GTM access gaps: PPC clients paidsearch@vortala.com can't open

Checked 2026-10-21 (requested by SS). Read-only, nothing was changed.

**Method:** took every client in the Vortala Ad Account Inventory sheet, found the website its live ads point to (Google Ads final URLs, Meta ad links), read the GTM container ID(s) loaded on that site, and compared them with the 85 containers paidsearch@ can currently see in GTM (index refreshed today, `config/gtm_containers.json`).

**Summary**
- 15 clients already have their container shared with paidsearch@ (e.g. PP5416, PP5813, PP6066, PP3953, PP5063, PP6147, PP5999, PP4956, PP0764, PP1820, PP5825, PP6349).
- **57 Active clients still need access** (list below; CSV with every row: `reports/2026-10-21_gtm-access-gaps.csv`).
- A few clients are Paused, Canceled, unlabelled or have no GTM on their site (further down).

To fix: in each container's GTM account → Admin → User Management → add `paidsearch@vortala.com` with **Publish** permission on the container. Someone who already has admin access to that GTM account (or the client) has to do this.

## Active clients without access (57)

| Owner | Client | Website | GTM container(s) to share |
|---|---|---|---|
| John | PP0519 - Fitchett Chiropractic | www.fitchettchiropractic.com | GTM-K442VGQ |
| John | PP0573 -Cr 1- Chaparral Chiropractic Wellness Centre | www.familywellnesscentre.com | GTM-556WP9P |
| John | PP0589 - SpineWerX | www.spinewerx.ca | GTM-PR7MRQW |
| John | PP1989 - Rauch Chiropractic & Rehab | www.thehamiltonchiropractor.com | GTM-MSP4M35M |
| John | PP2122 - Adelphia Chiropractic Health Centre | www.adelphiachiropractic.com | GTM-KGRVZ57 |
| John | PP2411 – Universal Chiropractic | www.universalchiro.ca | GTM-TZL2C4XW |
| John | PP3159 - Herron Family Chiropractic | www.herronchiropractic.com | GTM-TBSD5X9 |
| John | PP3899 - Lindenwoods Chiropractic | www.lindenwoodschiropractic.com | GTM-MN7G29B |
| John | PP4291 - Senopati Therapy Center (NEW) | www.senopatitherapy.com | GTM-PWQ65RR |
| John | PP4410 - HM Dental | www.dentistperth.com | GTM-NRMFXLT |
| John | PP4745 - Wavescape Orthodontics | www.wavescapeortho.com.au | GTM-K27JR5K, GTM-KWXN3RX |
| John | PP4773 - Restoring Life Chiropractic | www.restoringlifechiropractic.com | GTM-K936XBD |
| John | PP4906-Back & Body Wellness Centre | www.backandbody.ca | GTM-MVPGHBL9, GTM-WF6DNJ2 |
| John | PP4960 - The Tooth Affair | www.thetoothaffair.com.au | GTM-N6PWXKB |
| John | PP5152 - Active Health Chiropractic | www.activehealthchiro.ca | GTM-TSZK63X |
| John | PP5154 - TC Smiles | www.tcsmiles.com.au | GTM-WMC8QRP |
| John | PP5178 - Central Avenue Health Centre | www.cahc.ca | GTM-MC9RNJK |
| John | PP5347 - Community Chiropractic Center | www.communitychirosc.com | GTM-T93LFWH |
| John | PP5353 - Aurora Dental | www.auroradentalsmiles.com | GTM-55HB48Q |
| John | PP5405 - Melody Dental Care | www.melodydentalcare.com | GTM-KZXCZXL |
| John | PP5470 - Optimal Health Chiropractic | www.optimalhealthchiropracticsc.com | GTM-TMC278N |
| John | PP5555 - Essential Chiropractic Inc | www.essentialchiro.ca | GTM-KS2SZJT |
| John | PP5871 - Better Health Chiropractic | www.getbhc.com | GTM-KZ4V7K9 |
| John | PP6236 - Pullen Dental | www.pullendental.com.au | GTM-M7J952QZ |
| John | PP6293 - Ponsonby Chiropractic | www.ponsonbychiropractic.co.nz | GTM-W5KKD5L |
| John | PP6304 - Alkimos Beach Dental Centre | www.alkimosbeachdental.net.au | GTM-MQ8ZQK6N |
| John | PP6414 - McAfee Chiropractic | www.mcafeechiro.com | GTM-TKGVGT7S |
| John | PP6416 - Advanced Chiropractic | www.mylondonchiropractor.com | GTM-NTB23THW |
| John | PP6596 - Peak Performance Sport & Spine | www.peakperformss.com | GTM-5VVQSW2R |
| Sara | PP0117 - Funnell Chiropractic | www.funnell.com.au | GTM-NC3TPB5 |
| Sara | PP1184 – MM-Fayetteville Family Chiropractic | www.fayettevillechiropractic.com | GTM-T8J72J4 |
| Sara | PP1375 - The Chirohealth Clinic | www.chirohealth.co.uk | GTM-NXL36KZ |
| Sara | PP1864 - DZ 1-Memorial Drive Chiropractic and Massage | www.mycalgarychiropractor.ca | GTM-TMT4P3B |
| Sara | PP2230 - Croydon Sports Injury Clinic Ltd | www.croydonsportsinjuryclinic.co.uk | GTM-NWKSQ6D |
| Sara | PP3074 - Doster Chiropractic | www.dosterchiropractic.com | GTM-5ZHJGTP |
| Sara | PP3599 - Martindale Chiropractic & Wellness Centre | www.martindalechiropractic.com | GTM-5FGPCRZ |
| Sara | PP3678 - Advanced Care Chiropractic and Wellness Center | www.advancedcareva.com | GTM-M2NRJDK |
| Sara | PP4094 - Palmetto Smiles of Charleston | www.palmettosmilesofcharleston.com | GTM-P4VKDWZ |
| Sara | PP4348 - Vision Dental | www.visiondental.com.au | GTM-N2W4K5W |
| Sara | PP4637 - Action Chiropractic | www.myedmontonchiropractor.ca | GTM-T69B2W7 |
| Sara | PP4690 - Shine Dentists** | www.shinedentists.com.au | GTM-NX8DJJM |
| Sara | PP5080 - Blockhouse Bay Dental | www.bhbdental.co.nz | GTM-KSZDKX9 |
| Sara | PP5117 - Whale Family Chiropractic | www.whalefamilychiropractic.ca | GTM-TB9LN5J |
| Sara | PP5368 - Triad Family Chiropractic | www.triadfamilychiropractic.com | GTM-T2ZW66 |
| Sara | PP5372 - Mason Spine & Injury Center | www.masonsaic.com | GTM-58N3NPS |
| Sara | PP5449 - Midwest Sport & Spine | www.midwestsportandspinecenter.com | GTM-P6CX8J5 |
| Sara | PP6282 - Dentist in Hervey Bay | www.dentistinherveybay.com.au | GTM-NRQV8WLM |
| Sara | PP6285  - Lifestyle Chiropractic & Wellness | www.lifestylechiromn.com | GTM-TMMG5BN8 |
| Sara | PP6313 - RiverTowne Family Chiropractic | www.rivertownechiro.com | GTM-TZ68C5BR |
| Sara | PP6330 - Life Chiropractic Centre | www.lifechiropractic.com.au | GTM-T8BRCGBG |
| Sara | PP6481 - ChiroPro | www.chiropro.com | GTM-WTJG5FNK |
| Sara | PP6724 - Lakeside Align Chiropractic | www.lakesidealign.com | GTM-NP7XQ9JH |
| Sara | PP6742 - Touch Light Chiropractic | www.touchlightchiro.com | GTM-MBGVZFCG |
| Sara | PP6744 – Gavric Chiropractic Clinic | www.gavricchiropractic.com | GTM-NZ6BNM2N, GTM-PX3V6953 |
| Sara | PP6773 - Mind and Spine Chiropractic | www.mindandspinechiro.com | GTM-PDQ4R3PW |
| Sara | PP6788 - Resolve Chiropractic and Wellness | www.bobcatchiro.com | GTM-PBJ36LQF |
| Sara | PP6799 - Hershey Family Chiropractic | www.hersheyfamilychiropractic.com | GTM-MM8FV2LT |

Notes:
- PP6293 Ponsonby Chiropractic: paidsearch@ has GTM-PJW5BJ4Z, but the site also loads GTM-W5KKD5L, which isn't shared.
- PP4745, PP4906 and PP6744 sites load two containers each; both are listed.

## Active clients with no GTM container on the site
| Owner | Client | Website |
|---|---|---|
| John | PP3906 - Bilan Chiropractic | www.bilanchiropractic.com |
| Sara | PP5596 - Align Chiropractic Clinic | www.alignchiroclinicmo.com |

These may use gtag.js directly or another tag manager; nothing to share in GTM unless one is set up.

## Paused / Canceled / no client-status label
| Owner | Client | Platforms | Website | GTM container(s) to share |
|---|---|---|---|---|
| Sara | PP0315 - Marsteller | Google+Meta | www.mfamilychiro.com | GTM-KGWDW85 |
| Sara | PP4604 - The Joint Chiropractically | Google | www.thejoint.com.au | GTM-T8Q9NXZ |
| Sara | PP5949 - EvoHealth - Kansas Functional Medicine | Google | www.functionalmedicine.evohealthkansas.com |  |
| Sara | PP6782 – Germantown Premier Chiropractic | Google | www.chirogermantown.com |  |
| Arif | Perfect Patients Marketing | Meta | www.perfectpatients.com | GTM-PV4NQGT4 |
| John | PP0248 - Happy Spine** | Meta | www.happyspine.co.nz | GTM-MJFZ3QX |
| Sara | PP1654 - Goffstown Chiropractic Care | Meta | www.goffstownchirocare.com | GTM-MXWHJHK |
| Sara | PP5375 - Freedom Chiropractic | Meta | www.freedomchiro.com | GTM-52S9ZV7 |
| Unassigned | PP3228 - RCI Injury Treatment Center | Google+Meta | www.recoverychiro.com | GTM-WFXTW5X |
| Unassigned | Perfect Patients | Google | www.perfectpatients.com | GTM-PV4NQGT4 |
| Sara | PP1686 - Nardone Family Chiropractic | Meta |  |  |
| Sara | PP4482: Structural Chiropractic | Meta |  |  |
| Sara | PP5545 - Shenton Park Family Dental | Meta |  |  |
| Sara | PP6269 - Family Chiropractic Bundaberg | Meta |  |  |
| Sara | PP6677 - Brunswick Road Dental | Meta |  |  |
| Unassigned | PP1263 - Birmingham Chiropractic Clinic | Google |  |  |
| Unassigned | PP5116 - Client Self Run Account | Google |  |  |
| Unassigned | The Wellness Connection 2021 | Meta | go.thewellnessconnection.com |  |

"No client-status label" rows are mostly Meta-only accounts (their status comes from the Google Ads label) and in-house accounts. Blank website = the ads only link to Meta lead forms, so no site was found to check.

## Caveats
- The container is read from the live site's HTML. A container added only by a plugin after page load, or one on a different landing-page domain, could be missed.
- Matching is on the container ID; paidsearch@ may have access to an old container under a different ID that the site no longer uses.
