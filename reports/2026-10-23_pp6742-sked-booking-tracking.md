# PP6742 – Touch Light Chiropractic: SKED booking tracking

Requested by SS, 2026-10-23. Goal: count **completed** new-patient bookings made through SKED as a Google Ads conversion, in place of the "New Patient Book Now Page View" goal, which only counts people who opened /book-now/.

## How it works (background for Sara)

- The SKED scheduler is embedded as an iframe on https://www.touchlightchiro.com/book-now/ (`portal.sked.life/new-patient?key=…`). GTM-MBGVZFCG runs on the parent page. All the CTAs on the ad landing page (/huntersville-chiropractor/) go to /book-now/.
- **Vortala manages the website** (SS, 23 Oct): /book-now/, the landing page and any CTA changes are ours. The client only controls SKED itself.
- I read SKED's portal code (23 Oct 2026). When a booking saves, the scheduler sends a message to the page it's embedded in: `parent.postMessage('{"actionType":"confirm", …}', "*")`. **SKED already does this. The client doesn't need to switch anything on.** A small GTM listener on the website can catch that message and fire the conversion.
- The message also contains the patient's **name, email, phone and appointment time**. Our listener must throw these away and pass on only "a booking happened". No patient details go to Google (CLAUDE.md healthcare rule). Don't turn on enhanced conversions for this action.
- SKED's "redirect after booking" setting only works when the scheduler is opened as a full page, **not when it's embedded**. In the code, if a redirect URL is set and the scheduler is embedded, the page stays on a loading spinner after booking (the booking still saves). So we want that setting blank. One patient's voicemail said online booking for the $199 special "failed", which could be this. Not confirmed.
- New and returning patients: the new-patient scheduler links to a "Returning Patients Here" flow. In the code, the second booking path sends a placeholder email (`example@ex.com`) instead of the patient's. That probably means a returning patient, but it needs confirming in testing. The listener tags each booking `new` or `returning` from this, so only new ones count.

---

## A. Message for the DMS to send to the client (draft)

> **Subject: Quick setup so we can track online bookings from your ads**
>
> Hi Dr. Gross and team,
>
> At the moment we can see when someone from your Google Ads opens your Book Now page, but not whether they actually finish booking an appointment in SKED. We'd like to fix that, so the ads are judged on real new-patient bookings rather than page visits. Most of the work is on our side. We need three things from you:
>
> 1. **Check one SKED setting.** In your SKED online scheduling (new patient portal) settings, if there's a **"redirect URL" or "thank-you page"** after booking, please leave it **blank** or tell us what it's set to. Your scheduler is built into your website's Book Now page, and a redirect can stop patients seeing the confirmation screen. If you're not sure where this is, SKED support can check it for you.
>
> 2. **Allow one test booking.** Once tracking is set up, we'll make one test appointment through the website. It'll be named **"TEST Vortala – please delete"**, at a time you choose (ideally a slot you don't expect to fill). Please let us know a good day and time, and delete the appointment afterwards. While you're at it, it's worth making a test booking yourselves on your phone. One caller recently told us online booking for the $199 special didn't work for them.
>
> 3. **Let us know if your SKED online booking changes.** We look after the Book Now page on your website, so you don't need to change anything there. But if your SKED new-patient booking link changes, online booking is switched off, or you move to different scheduling software, please tell us first so tracking (and the Book Now page) keeps working.
>
> One quick question: do returning patients ever book through the same Book Now page, or only new patients?
>
> And for the first month, it would help if you could tell us how many **new-patient online bookings** SKED shows, so we can check our numbers match yours.
>
> No patient names, emails, phone numbers or appointment details are sent to Google. We only record that a booking happened.
>
> Thanks!

*(Internal: Vortala already has access to the GTM container, so the client doesn't need to do anything in GTM. Sara still needs to be added internally (23 Oct). The message can go before that. Optional extra, only if GTM shows a GA4 tag (G-…) and you want the GA4 event: ask the client to add paidsearch@vortala.com as an **Editor** on that Google Analytics property (Admin → Property access management → +).)*

---

## B. Sara's steps

### 1. Before building
- [ ] GTM access to GTM-MBGVZFCG for you. Vortala already has the container, so this is an **internal** ask: get whoever manages it at Vortala to add you (or paidsearch@) with **Publish** permission. The client doesn't need to do anything.
- [ ] Optional: if GTM has a GA4 tag (G-…), ask for GA4 Editor access so you can mark the booking as a key event.
- [ ] The client has confirmed SKED's redirect URL is blank.
- [ ] Decide the conversion **value**: none, or a fixed value (e.g. 199 for the new-patient special). Tell me which.
- [ ] Check in GTM whether a **Conversion Linker** tag fires on All Pages and whether a Google Ads tag (AW-…) already exists. The page HTML has no AW- tag, so anything there is inside GTM.

### 1b. Website (ours to manage): no page change needed
The tracking runs entirely in GTM, so /book-now/ stays as it is. Going forward:
- **Keep the SKED scheduler embedded** on /book-now/ (`<iframe id="sked-portal" src="https://portal.sked.life/new-patient?key=…">`, existing `sandbox` attribute included). Don't replace it with a button or link that opens sked.life in a new tab or a pop-up. The booking signal only reaches a page the scheduler is embedded in, so a booking made on sked.life itself wouldn't be tracked.
- **All booking CTAs go to /book-now/**, never straight to sked.life. That's true now: all 6 booking links on /huntersville-chiropractor/ point to /book-now/. Do the same on any new landing pages or ad variants.
- **After any edit to /book-now/**, open it on a phone and check the scheduler loads and scrolls properly.
- **Plan B, only if the test in step 4 doesn't pick up the booking:** since we own the site, we could create a thank-you page (e.g. /booking-confirmed/, noindex), link CTAs to the full-page SKED scheduler, and ask the client to set that page as SKED's redirect URL. We'd then track the thank-you page. It's worse for patients (they leave the site to book) and needs a client change in SKED, so it's a fallback only.

### 2. Create the Google Ads conversion action (288-398-9795)
Goals → Conversions → Summary → **+ New conversion action** → Website → enter touchlightchiro.com → **Add a conversion action manually**:
- Category: **Book appointment**
- Name: **SKED New Patient Booking**
- Value: your choice from step 1
- Count: **One**
- Click-through window 30 days, engaged-view 3 days, view-through 1 day; attribution data-driven
- Enhanced conversions: **off** (patient details)
- Set it as a **secondary** action while testing.
- Save → choose **Use Google Tag Manager** → copy the **Conversion ID** and **Conversion label**.

(I can create this through the API instead. I'll show you a preview first.)

### 3. Build in GTM (in a new workspace, e.g. "SKED booking tracking")
**a. Listener tag:** Tags → New → **Custom HTML**, name `SKED – booking listener`. Trigger: **All Pages** (it only reacts to messages from portal.sked.life, so it's safe site-wide and covers future embeds).

```html
<script>
(function () {
  if (window.__skedListener) return;
  window.__skedListener = true;
  var sent = false;
  window.addEventListener('message', function (e) {
    if (e.origin !== 'https://portal.sked.life') return;
    var msg;
    try { msg = typeof e.data === 'string' ? JSON.parse(e.data) : e.data; } catch (err) { return; }
    if (!msg || msg.actionType !== 'confirm' || sent) return;
    sent = true;
    // Only the booking type leaves this function. Name, email, phone and time are discarded.
    var returning = !!(msg.payload && msg.payload.email === 'example@ex.com');
    window.dataLayer = window.dataLayer || [];
    window.dataLayer.push({ event: 'sked_booking_confirmed', sked_patient_type: returning ? 'returning' : 'new' });
  });
})();
</script>
```

**b. Variable:** Variables → New → **Data Layer Variable**, name `DLV – sked_patient_type`, variable name `sked_patient_type`.

**c. Trigger:** Triggers → New → **Custom Event**, name `SKED – new patient booking`, event name `sked_booking_confirmed`, fires on **Some Custom Events**: `DLV – sked_patient_type` equals `new`.

**d. Google Ads tag:** Tags → New → **Google Ads Conversion Tracking**, name `Google Ads – SKED New Patient Booking`. Paste the Conversion ID and label, leave value blank unless you chose one, no enhanced conversions. Trigger: `SKED – new patient booking`.

**e. Conversion Linker:** if there isn't one, add a **Conversion Linker** tag on All Pages.

**f. GA4 (optional, if they have GA4):** Tags → New → **Google Analytics: GA4 Event**, event name `sked_booking`, parameter `patient_type` = `{{DLV – sked_patient_type}}`, trigger `SKED – new patient booking`. Mark `sked_booking` as a key event in GA4, but **don't import it into Google Ads** (it would count twice with the tag above).

### 4. Test (GTM Preview, before publishing)
1. Click **Preview**, enter `https://www.touchlightchiro.com/book-now/?gclid=test123`, and make the agreed test booking ("TEST Vortala – please delete").
2. In Tag Assistant, check that `sked_booking_confirmed` appears **once**, `sked_patient_type` = `new`, and the Google Ads tag fired.
3. Check the dataLayer has **no** name, email or phone in it.
4. If the client allows it, also test the "Returning Patients Here" path and check it shows `returning` and the Ads tag **doesn't** fire. If it shows `new`, tell me and I'll change the check.
5. Ask the client to delete the test appointment.

### 5. Publish and switch over
- [ ] Show me the workspace changes. I'll put them in a preview before you publish (publishing is its own approval).
- [ ] Publish the GTM version with the name "SKED booking tracking".
- [ ] After 1–2 weeks, once real bookings appear and roughly match SKED's own count: set **SKED New Patient Booking → Primary** and **New Patient Book Now Page View → Secondary**. Don't leave both primary, or every booking counts twice (page view + booking).
- [ ] Log the changes in `logs/changes/` and update `accounts/pp6742-touch-light-chiropractic/notes.md` (I'll do both).

**Timing:** the campaign is paused by the budget rule until 1 Nov, so setting this up before then means November starts with clean booking data.

---

## C. Salesforce case comment for the DMS (draft, SS to post)

Hi [DMS name],

PPC request for Touch Light Chiropractic (PP6742), from Sara Stuka.

What we're doing: setting up tracking for completed online bookings made through SKED from Google Ads. Right now Google Ads only counts people who open the Book Now page, not people who actually book. Once this is live, the ads will be measured and optimised on real new-patient bookings. We'd like it in place before the campaign restarts on 1 Nov.

How: SKED already sends a "booking confirmed" signal to the website's Book Now page, where the scheduler is embedded. We'll pick that up in Google Tag Manager and send it to Google Ads as a conversion. No patient names, emails, phone numbers or appointment details go to Google. Vortala manages the website and GTM, so nothing changes on the site and the client doesn't need to touch GTM.

What we need from you: please send the client the message below and pass their replies back on this case. The main things we need back are the answer on the SKED redirect setting, a day and time for the test booking, and whether returning patients use the Book Now page.

----- Message to client -----

Subject: Quick setup so we can track online bookings from your ads

Hi Dr. Gross and team,

At the moment we can see when someone from your Google Ads opens your Book Now page, but not whether they actually finish booking an appointment in SKED. We'd like to fix that, so the ads are judged on real new-patient bookings rather than page visits. Most of the work is on our side. We need three things from you:

1. Check one SKED setting. In your SKED online scheduling (new patient portal) settings, if there's a "redirect URL" or "thank-you page" after booking, please leave it blank or tell us what it's set to. Your scheduler is built into your website's Book Now page, and a redirect can stop patients seeing the confirmation screen. If you're not sure where this is, SKED support can check it for you.

2. Allow one test booking. Next week we'll make one test appointment through your website, named "TEST Vortala – please delete". Please tell us a day and time between Wed 28 and Fri 30 Oct that suits you (ideally a slot you don't expect to fill), and delete the appointment afterwards. It's also worth making a test booking yourselves on your phone. One caller recently told us online booking for the $199 special didn't work for them.

3. Let us know if your SKED online booking changes. We look after the Book Now page on your website, so you don't need to change anything there. But if your SKED new-patient booking link changes, online booking is switched off, or you move to different scheduling software, please tell us first so tracking keeps working.

One quick question: do returning patients ever book through the same Book Now page, or only new patients?

For the first month, it would help if you could tell us how many new-patient online bookings SKED shows, so we can check our numbers match yours.

No patient names, emails, phone numbers or appointment details are sent to Google. We only record that a booking happened.

Thank you!

----- End of message -----

Thanks,
Sara

---

## D. Phase 2: track show-ups and started care in Google Ads (SS wants this, 23 Oct)

Goal: tell Google Ads which ad bookings actually **showed** and which **started care**, so it can be measured on real new patients rather than bookings.

### The problem to solve
Google Ads can only credit a later outcome to an ad click if each booking has an ID that we can find again later. SKED doesn't store a Google click ID with the appointment (its booking link only carries `key` / `from`), and WhatConverts can't see inside a third-party iframe without its script inside SKED's page, which we can't add.

### Recommended method: opaque booking ID + conversion adjustments
1. **At booking (phase 1 tag, small addition):** the GTM listener builds a booking ID from the **appointment date and time** in SKED's message, hashed with a secret salt (SHA-256). The ID goes to Google Ads as the conversion's `transaction_id`. Google gets an unreadable string, not the time or any patient details.
2. **Weekly, from the client:** a list of the **appointment dates and times** of online new-patient bookings that showed, and of those that started care. Times only, no names.
3. **Our side:** hash those times the same way to find the matching booking IDs, then upload **conversion adjustments** to Google Ads:
   - no-show → **retract** the booking conversion, so it only counts bookings that showed; or
   - **restate the value**, e.g. booked 0 → showed 1 → started care 10 (values to agree).
   No new conversion data or identifiers go to Google, just adjustments to the bookings it already has, keyed by the opaque ID.
4. Google only accepts adjustments within a limited window after the conversion (about 55 days; confirm before building), so the weekly cadence matters.

Why this one: no patient names, phones or emails leave the site, no new tool or server, and it builds on the phase 1 tag. Put the booking ID in the tag **from day one**, so bookings made before the policy is signed off can still be adjusted later, within the window.

Alternative (not recommended for now): send each booking into WhatConverts as a lead with the click ID (needs a small server relay holding the WhatConverts API key), have the front desk mark show / started care in WhatConverts, and let WhatConverts import those to Google Ads. It's a smoother daily workflow, but patient names and contact details pass through more systems. WhatConverts says it signs BAAs (https://www.whatconverts.com/security/whatconverts-and-hipaa/), but the relay would need one too.

### Gate: needs a policy decision before anything is uploaded
CLAUDE.md: until the team sets a HIPAA / patient-data policy, nothing about patients goes to ad platforms. Telling Google "this ad click became a patient" is patient-related information even without names, and Google doesn't sign BAAs for Google Ads. Before phase 2 uploads start:
- [ ] Vortala sign-off on a policy covering this (Jacob as CEO, ideally with legal advice).
- [ ] The client's written OK (they're the HIPAA covered entity), and confirmation that a BAA between Vortala and the practice covers us receiving appointment times.
- [ ] The website privacy policy mentions ad conversion measurement (we manage the site).

Building the phase 1 booking tag, with the opaque ID, can go ahead now. It sends no patient data.

### What the client sends us first (before anything goes back to Google)
Send once Vortala has decided its own position (Jacob), so the agreement wording comes from Vortala, ideally reviewed by legal. Draft for the DMS:

> **Subject: Your OK to measure which ads bring in new patients**
>
> Hi Dr. Gross and team,
>
> Once your online booking tracking is live, we'd like to go one step further and measure which ad bookings actually come in and start care. That lets Google put your budget behind the ads that bring real new patients, not just bookings. Because this involves your patients' appointments, we need a few things from you before we start:
>
> 1. **Your written OK.** Please reply confirming you're happy for Vortala to receive a weekly list of online new-patient appointment dates and times (no names or contact details), marked showed / started care. Also confirm you're happy for us to use it to send Google Ads an anonymous signal, a scrambled booking reference plus "showed" or "started care", with no patient details. *(Vortala to attach or link its standard authorization here if it has one.)*
> 2. **Our business associate agreement.** Please confirm whether you have a signed Business Associate Agreement (BAA) with Vortala. If you're not sure or don't have one, let us know and we'll send one over.
> 3. **Privacy policy.** We'll add a short line to your website's privacy policy explaining that we measure ad results, and send it to you to approve. If your practice's HIPAA Notice of Privacy Practices says anything about marketing or sharing information with vendors, please send us a copy or check it with whoever looks after your compliance.
> 4. **Who sends the weekly list.** The name and email of the person at the practice who'll send it each Monday, and the easiest way for them to pull it from SKED.
> 5. **What "started care" means for you.** For example, they accepted a care plan, or came back for a second visit.
> 6. **Roughly what a new patient is worth** to the practice (e.g. average first-year value), so we can tell Google how much more a patient who starts care is worth than a booking. A rough figure is fine.
>
> Nothing is sent to Google until we have these. Thank you!

Internal checklist before the first upload:
- [ ] Vortala policy decision (Jacob), ideally with legal review of the wording in item 1.
- [ ] Items 1–2 received in writing; saved where the team keeps client agreements (not in this repo).
- [ ] Privacy policy line added to touchlightchiro.com and approved by the client.
- [ ] Values agreed (items 5–6) and the adjustment window confirmed.

### Extra ask for the client (send only once the policy is signed off)
> **Subject: One weekly update so we can see which ads bring in real patients**
>
> Hi Dr. Gross and team,
>
> Online booking tracking is now live. Next, we'd like to see which bookings from your ads turn into patients who come in and start care, so we can put more of your budget behind the ads that bring in real new patients.
>
> **Each Monday**, please send us a short list of the **online new-patient bookings** for appointments in the previous week (Monday to Sunday). For each one, we just need:
>
> | Appointment date | Appointment time | Showed? | Started care? |
> |---|---|---|---|
> | e.g. Wed 4 Nov | 5:45 pm | Yes | Yes |
> | e.g. Thu 5 Nov | 12:30 pm | No | – |
> | e.g. Thu 5 Nov | 3:15 pm | Yes | Not yet |
>
> A few notes:
> - **Online bookings only**: appointments the patient booked themselves through the Book Now page on your website (SKED shows these as online / new patient portal bookings). Please leave out phone and walk-in bookings.
> - **Use the original appointment time.** If a patient rescheduled, use the time they first booked and put "Rescheduled" in the Showed column, plus the new date if you have it.
> - **"Started care"** means they accepted a care plan, or came back for a second visit, whichever you usually count as a new patient. "Not yet" is fine; just update it on a later list.
> - **Please don't include names, phone numbers, emails or anything about their condition or treatment.** We only need the date, the time and the two answers.
> - If there were no online bookings that week, a quick "none this week" is perfect.
>
> We match these times to the online bookings our tracking recorded. Google only receives a scrambled booking reference, never the time or any patient details. This list is what lets us tell Google which ads are bringing in real patients, so it really helps if it arrives every week.
>
> Thank you!
