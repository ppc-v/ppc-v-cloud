# Booking response time test: form pages (21 Oct 2026)

Requested by JW (task from Jacob Froats). Working sheet: [Booking Response Time Test – Oct 2026 (JW)](https://docs.google.com/spreadsheets/d/1jXj7lwp2P-qtv2-v_PHO67rBsw2iq9Tlp-GJFj9nseM/edit) in the paidsearch@ Drive. Form links and details also in `2026-10-21_booking-response-test-forms.csv`.

## How the links were checked
- Website taken from each account's Google Ads final URLs, then every contact page loaded in a browser on 21 Oct 2026. All 26 links return HTTP 200 and show an appointment request form.
- 23 practices use the standard /contact-us/ page with an "Appointments" / "Appointment Request" form (plus a general contact form).
- Exceptions: PP2230, PP5596 and PP6481 have several locations, so /contact-us/ there only lists them and the forms are on each location's page (the sheet uses the main location and lists the others). PP3906 is on a different website platform and its form is at /contact-us.htm. PP3159 has separate New and Current Patient forms (use New).
- Practice timezone comes from the office address, not the ad account. These don't match for PP1864 (account Vancouver, practice Calgary), PP5596 (account Denver, practice Missouri) and PP4094 (account Indiana/Vevay, practice Eastern).
- For all 25 clients that have WhatConverts, it shows only phone calls in the last 90 days (no web forms). PP5368 has no WhatConverts account.

## Site issues found
- PP5372: the Contact Us office hours table shows only Thursday 9–12.
- PP5596: the Osage Beach contact page shows "Call Today: (000) 000-0000".
