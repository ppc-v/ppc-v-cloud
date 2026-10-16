# PP6788: 172 negatives, pause broad "chiropractor", Current Patient goal to secondary

- **When:** 2026-10-16 16:16 UTC (12:16 US Eastern, Sara)
- **Requested by:** SS
- **Approved by:** SS, approved preview in chat
- **Platform:** Google Ads
- **Session:** https://claude.ai/code/session_01LBMSMa2Rm2AJQJQHz4fbdu

## Changes
| Account | Entity (type, name, ID) | Field | Before | After | Result |
|---|---|---|---|---|---|
| PP6788 - Resolve Chiropractic and Wellness (238-150-2203) | Shared negative list "Competitor Negative Keywords" (12231635375) | Members | 116 | 228 (+112 phrase) | ✅ applied, 112/112 |
| PP6788 (238-150-2203) | Shared negative list "Search Queries" (12255104966) | Members | 174 | 234 (+60 phrase) | ✅ applied, 60/60 |
| PP6788 (238-150-2203) | Keyword "chiropractor" [broad], ad group "Chiropractor" (203779783887~12457821) | Status | Enabled | Paused | ✅ applied |
| PP6788 (238-150-2203) | Conversion action "Appointment Request (Current Patient)" (7757753937) | Goal | Primary | Secondary | ✅ applied |

Both lists are attached to campaign "Perfect Patients" (24227912106). All operations ran validate-only first, then applied with no errors. Each change was read back from the API afterwards.

### Added to Competitor Negative Keywords (phrase)
alive and well; doans; austin chiropractic; walk off wellness; whole body chiropractic; ortho texas; orthotexas; athletico; north texas sport and spine; therapy fit; star orthopedics; global chiropractic; mckinney health and wellness; texas pain relief group; texas neck and back; texas healthcare neck and back; c3 wellness; ortholazer; ortho lazer; omni spine; epic chiropractic; t3 chiropractic; accident centers of texas; elliot spine; farrar; farrer; happy health; healthsource; health source; jensen chiropractic; premise health; solutions in pain; arora; craft chiropractic; flow chiropractic; flow chiropractor; palmer chiropractic; tribe wellness; first light chiropractic; limitless chiropractic; origin chiropractic; revolution chiropractic; revolution chiropractor; one chiropractic; anchor point; bullitt; denito; illuminate chiropractor; illumin8; orion ortho; our well house; pro sports performance; texas spine consultants; the treatment room; chiroworx; elder chiropractic; family tree chiro; nortex; prime care chiropractic; we care chiropractic; subherban; aligned clinic; inside out chiropractic; max chiropractic; nicklas chiropractic; optimal spine; premier chiropractic; ring chiropractic; thrive chiropractic; upright health; barefoot rehabilitation; clearway pain; inspire chiropractic; paragon pain; principle spine; quantum pain; restore chiropractic; network spinal; injury relief chiropractic; mondragon; centennial medical; baylor; bsw; methodist; specialty wellness; speciality wellness; mckinney injury rehab; frisco pain and spine; performance orthopedics; plano sports; pain and spine physicians; brock pain; texas muscle activation; elements frisco; neubie; sole hao; custom chiropractic; village chiropractor; gonstead; nucca; yalamanchili; ognenovski; deana hicks; gonzalo gonzales; alexander satin; jon c thompson; rajnikant; slabisak; bosita; aritosi; independent chiropractor; complete chiropractor

### Added to Search Queries (phrase)
orthopedic; orthopedics; orthopaedic; orthopedist; ortho; rheumatology; rheumatologist; traumatologist; physical medicine; urgent care; sports medicine; sportsmedicine; epidural; steroid injection; steroid injections; trigger point injections; injection; injections; surgery; reflexology; pilates; yoga; gyrotonic; tcm; eastern medicine; posture corrector; support belt; muscle relaxer; foam roller; remedies; diy; machine; chair; india; online; test; x ray; what is; what kind of doctor; what type of doctor; what to do; what should you do; how many days; how i cured; is chiropractic safe; ways to help; symptoms; meant by; ejercicios; porque; por que; que tomar; qué es; cómo; dallas; plano; carrollton; allen; haslet; windhaven

## Failed or skipped
- "Appointment Request (New Patient)" (7757753940): change counting from Every to One per click. Skipped because the API returned `IMMUTABLE_FIELD`: the action is imported from GA4, so GA4 controls counting. Not retried.
- Follow-up: SS changed it to One per click herself. Read back from the API on 2026-10-16: `ONE_PER_CLICK`, still primary.

## Notes
- Reason: about 22% of the first 30 days' spend went to competitor, orthopedic/PT and off-topic searches. Run against all 779 search terms since launch, the new negatives would have blocked 266 terms, $758 of spend and 5 conversions (all competitor-name searches). They don't block any active keyword.
- Broad "chiropractor": $683 for 5.3 conversions (~$129 CPL). Phrase/exact "chiropractor" and broad "chiropractor near me" are still on.
- Not changed: budget ($85/day), Frisco/McKinney geo, Spanish searches, shockwave/softwave/laser searches. Open questions for SS.
- Follow-up: WhatConverts imports every call as a primary conversion. Consider importing only quotable or 60s+ calls.

