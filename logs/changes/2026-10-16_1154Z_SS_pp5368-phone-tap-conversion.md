# PP5368 Triad Family Chiropractic: rebuild the landing page phone-tap conversion

- **When:** 2026-10-16 11:54–11:56 UTC (07:54 US Eastern, Sara)
- **Requested by:** SS
- **Approved by:** SS, approved the preview in chat; approved the new name "Landing Page Phone Tap" after the first name was refused
- **Platform:** Google Ads
- **Session:** https://claude.ai/code/session_01KLi6n12BmMTkGN7niN9tsm

## Changes
| Account | Entity (type, name, ID) | Field | Before | After | Result |
|---|---|---|---|---|---|
| PP5368 - Triad Family Chiropractic (558-007-2284) | Conversion action "LP Phone Tap" (7849571497) | Status | Enabled, primary, 0 conversions | Removed | ✅ applied |
| PP5368 - Triad Family Chiropractic (558-007-2284) | Conversion action "Landing Page Phone Tap" (7849561377) | New | – | Website phone-number tap (CLICK_TO_CALL), Phone call lead, primary, one per click, USD 1 default value, 30-day click window, data-driven attribution. Tag: `AW-598318905/k2jVCKGa-54dELm-pp0C` | ✅ created |
| PP5368 - Triad Family Chiropractic (558-007-2284) | Conversion action "Calls from Website" (7683627117) | Primary for goal | Primary | Secondary | ✅ applied |

## Failed or skipped
- The first attempt to create the new action as "LP Phone Tap" failed with DUPLICATE_NAME, because Google Ads keeps the names of removed actions reserved. Nothing was created on that attempt. Sara approved "Landing Page Phone Tap" instead.

## Notes
- **Why taps, not calls:** the client doesn't want the landing page number to swap, so Google's website call tracking (forwarding numbers) and WhatConverts number pools aren't options. Taps on the practice number are tracked instead.
- **No GTM:** the landing page (`/5-star-family-chiropractor-in-kernersville/`) loads the Google Ads tag AW-598318905 directly. It has 6 tel: links, all to (336) 904-0752.
- **Firing:** the new action records nothing until the click listener below is added to the landing page or site footer. It only sends the conversion event, with no patient data.

```html
<script>
document.addEventListener('click', function (e) {
  var link = e.target.closest && e.target.closest('a[href^="tel:"]');
  if (!link || typeof gtag !== 'function') return;
  gtag('event', 'conversion', {
    'send_to': 'AW-598318905/k2jVCKGa-54dELm-pp0C',
    'value': 1.0,
    'currency': 'USD'
  });
});
</script>
```
- **Follow-up:** once the script is live, check it fires on a test tap, then check the action records conversions.
