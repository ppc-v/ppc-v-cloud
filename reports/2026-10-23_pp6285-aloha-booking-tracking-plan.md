# PP6285 – Tracking Aloha (ReviewWave) online bookings

Requested by SS, 2026-10-23. This is a read-only plan: nothing was changed.

## What's on the site today (checked 2026-10-23)
- **https://www.lifestylechiromn.com/book-online/** runs the Aloha "New Patient Scheduler" (ReviewWave embed `23362a1b3c4b74ca4f3eaf92d45a39fb1e83`, script `cdn.reviewwave.com/js/reviewwave.js`). The steps are patient info, then service, then date and time. When a booking succeeds it shows "Thank You! Your appointment is scheduled for…". It's built into the page (not an iframe) on our own domain, so GTM can see it and the GCLID cookie is available.
- The widget fires a browser event, **`RWEmbedJS.appt_scheduled`**, and sets `window._rw_sched_config.schedule_status` to `"scheduled"` or `"error"`. It only does this if the page has already defined `window._rw_sched_config`. Our GTM tag will define it.
- The "existing patient" portal (theschedulingapp.com/LifestyleChiropracticandWellness, linked from /contact-us/) is a separate site, and those bookings are current patients. We leave it out.
- GTM container **GTM-TMMG5BN8** is on the site but not shared with paidsearch@. Also on the site: GA4 G-6SMSLQ3FYK, the Google Ads tag AW-16627031643 and WhatConverts 128417.
- **Neither the ad landing page (/chiropractor-mendota-heights/) nor the homepage links to /book-online/.** Ad visitors can't reach the booking form from the page the ad sends them to, so tracking alone won't produce booking conversions until a "Book Online" button is added.
- The current primary goal "Book Online Page View" counts a page view, not a booking.

## Step by step

### 1. Get access (send the client message below)
- GTM-TMMG5BN8: add `paidsearch@vortala.com` with **Publish** permission. The site is a Vortala childsite, so first check internally (web team) whether Vortala already owns this GTM account. If it does, no client email is needed for this.
- Aloha / ReviewWave: a user login, or a staff member who can check the appointment list, so we can confirm test bookings and cancel them.
- Optional: GA4 G-6SMSLQ3FYK with Editor access for paidsearch@, so we can mark a GA4 key event.
- The client's OK to make 1–2 test bookings, which we cancel straight away.

### 2. Website change (Vortala web team)
- Add a "Book Online" / "Schedule Your $99 Visit" button on /chiropractor-mendota-heights/ linking to /book-online/. Optionally add the same button to the main nav.

### 3. Build in GTM (in a workspace; publishing is a separate approval)
1. **Custom HTML tag "Aloha – booking listener"**, firing on the Initialization trigger for Page Path contains `/book-online` (or on all pages, if the widget gets added elsewhere later):
   ```html
   <script>
   (function () {
     window._rw_sched_config = window._rw_sched_config || {};
     if (window._rwListenerOn) return; window._rwListenerOn = true;
     document.addEventListener('RWEmbedJS.appt_scheduled', function () {
       if (window._rw_sched_config.schedule_status === 'scheduled') {
         window.dataLayer = window.dataLayer || [];
         window.dataLayer.push({ event: 'aloha_booking' });
       }
     });
   })();
   </script>
   ```
   Push only the event name. **Don't** push the patient's name, email, phone, the service chosen or the appointment date or time. All of these sit in the widget or `_rw_sched_config`, and they're patient and health data.
2. **Trigger:** Custom Event `aloha_booking`.
3. **Tags on that trigger:**
   - Google Ads conversion: a new action "Online Booking – Aloha" (category Book appointment, count **one**, value per Sara). Make sure the Conversion Linker tag exists.
   - GA4 event `aloha_booking`, marked as a key event (if we get GA4 access).
   - Meta: only if Sara wants it. A plain `Schedule` event with no parameters.
4. **Fallback** if the event doesn't fire in testing: an Element Visibility trigger on `.rw-thanks-message` / `.rw-completed-checkmark` (check this in Preview mode against a real confirmation screen).

### 4. Test
- In GTM Preview, make a test booking on /book-online/ and check that `aloha_booking` fires once, and only on the "Thank You" screen (not on errors).
- Check the Google Ads tag fired (Tag Assistant), then have the client or Aloha cancel the test appointment.
- Show Sara the workspace changes and publish after she approves.

### 5. Google Ads goals (part of the pending item 3 cleanup on this account)
- Make "Online Booking – Aloha" primary and move "Book Online Page View" to secondary.
- Separately fix the call double counting: "Calls from ads" and "Calls from Ad Extensions" both counted the same calls on Oct 2 and Oct 5.
- Cross-check monthly: the widget asks "How did you hear about us?" with a "Google Ad" option. Compare Aloha's bookings with source = google_ad against Google Ads conversions.

## Compliance notes
- US client (Minnesota). GDPR-style consent isn't required, but Minnesota's consumer data privacy law treats health data as sensitive. Sending only a bare "booking happened" event, with no service or patient details, keeps us within the team's current default.
- Aloha's own privacy notice already sits in the form. Nothing for us to add.

## Message to send the client (draft, sent by Sara)

> Subject: Quick access request so we can track online bookings
>
> Hi [Name],
>
> We'd like to start tracking how many people book through the online scheduler on your website (your Aloha / ReviewWave "Schedule an Appointment" form) after clicking your Google ads. That way we can see which ads and keywords bring in booked new patients and put more of your budget behind them. We only record that a booking happened, never any patient details.
>
> To set this up, could you help with the following:
>
> 1. **Google Tag Manager:** please add **paidsearch@vortala.com** as a user on your Tag Manager account (container GTM-TMMG5BN8) with **Publish** permission. In Tag Manager: Admin → User Management → + → Add users. If someone else manages your website or tracking, feel free to forward this to them.
> 2. **Google Analytics (optional):** add **paidsearch@vortala.com** as an **Editor** on your Google Analytics property. In Analytics: Admin → Property access management → +.
> 3. **Test bookings:** we'll make one or two test appointments through the online scheduler, marked "TEST – Vortala, please cancel", to make sure the tracking works. Is that OK? We'll let you know when they're in, so your team can cancel them in Aloha (or tell us if you'd rather we cancel them).
> 4. **A quick question:** do you want online bookings to be the main goal we optimise your ads for, alongside phone calls?
>
> We'll also add a "Book Online" button to your ad landing page so visitors from the ads can book straight away.
>
> Thanks!
> Sara
