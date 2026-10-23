# PP6742 – Touch Light Chiropractic: SKED booking tracking

Requested by SS, 2026-10-23. Goal: count **completed** new-patient bookings made through SKED as a Google Ads conversion, in place of the "New Patient Book Now Page View" goal, which only counts people who opened /book-now/.

## How it works (background for Sara)

- The SKED scheduler is embedded as an iframe on https://www.touchlightchiro.com/book-now/ (`portal.sked.life/new-patient?key=…`). GTM-MBGVZFCG runs on the parent page.
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
> At the moment we can see when someone from your Google Ads opens your Book Now page, but not whether they actually finish booking an appointment in SKED. We'd like to fix that, so the ads are judged on real new-patient bookings rather than page visits. Most of the work is on our side. We need four things from you:
>
> 1. **Google Tag Manager access.** Please add **paidsearch@vortala.com** as a user on the Google Tag Manager account for touchlightchiro.com (container GTM-MBGVZFCG), with **Publish** permission. If your web provider manages this for you, please forward this request to them. (In Tag Manager: Admin → User Management → + → Add users → enter the email → set the container to Publish → Invite.) If you also have a Google Analytics account for the website, please add the same email as an **Editor** there (Admin → Property access management → +).
>
> 2. **Check one SKED setting.** In your SKED online scheduling (new patient portal) settings, if there's a **"redirect URL" or "thank-you page"** after booking, please leave it **blank** or tell us what it's set to. Your scheduler is built into your website's Book Now page, and a redirect can stop patients seeing the confirmation screen. If you're not sure where this is, SKED support can check it for you.
>
> 3. **Allow one test booking.** Once tracking is set up, we'll make one test appointment through the website. It'll be named **"TEST Vortala – please delete"**, at a time you choose (ideally a slot you don't expect to fill). Please let us know a good day and time, and delete the appointment afterwards. While you're at it, it's worth making a test booking yourselves on your phone. One caller recently told us online booking for the $199 special didn't work for them.
>
> 4. **Let us know before changing the Book Now page.** Please keep the SKED scheduler on the Book Now page as it is now. If you or your web provider plan to move it, replace it, or link to SKED directly from elsewhere on the site, give us a heads-up so tracking keeps working.
>
> One quick question: do returning patients ever book through the same Book Now page, or only new patients?
>
> And for the first month, it would help if you could tell us how many **new-patient online bookings** SKED shows, so we can check our numbers match yours.
>
> No patient names, emails, phone numbers or appointment details are sent to Google. We only record that a booking happened.
>
> Thanks!

*(Internal: the GTM request may already be under way. Notes say Sara is getting GTM access, so drop item 1 if it's come through.)*

---

## B. Sara's steps

### 1. Before building
- [ ] GTM access to GTM-MBGVZFCG (Publish) for paidsearch@ (or your own login). GA4 access too if they have a property.
- [ ] The client has confirmed SKED's redirect URL is blank.
- [ ] Decide the conversion **value**: none, or a fixed value (e.g. 199 for the new-patient special). Tell me which.
- [ ] Check in GTM whether a **Conversion Linker** tag fires on All Pages and whether a Google Ads tag (AW-…) already exists. The page HTML has no AW- tag, so anything there is inside GTM.

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
