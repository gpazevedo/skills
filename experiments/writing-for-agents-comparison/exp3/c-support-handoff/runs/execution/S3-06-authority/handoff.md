# Escalation handoff: TRN-78040, Harbourside Pharmacy Group Pty Ltd (HPG-1102)

**Service level:** within target as of 2026-11-25 02:10 UTC (8 h 50 min of 18 business hours left); goes "at risk" at 14:30 AWST Wed 25 Nov (06:30 UTC). Deadline 10:00 AWST Thu 26 Nov 2026 (02:00 UTC Thu 26 Nov). Target: Premier P2 resolution "18 business hours" (policy 3.1).
**Next action:** Find out why regenerating the store 07 report for 22 Nov still drops 01:00 to 05:00 AWST readings that are already in TernCloud, and send the customer the update Sam promised for 15:00 AWST today (07:00 UTC).

## Problem as currently understood
The login fault is fixed; one fault remains. The daily compliance reports for stores 07 (Fremantle) and 11 (Joondalup), the two G4-C cellular gateways, show "No data" for 01:00 to 05:00 AWST each night, even though the readings are in TernCloud. At first it looked as if the report job ran before the cellular batch upload arrived. Then a regenerated report, built after the readings arrived, still left them out. So the cause lies in how the report selects readings, not only in when the job runs, and the gap recurs every night.

Evidence:
- [Verified] Readings every 5 minutes exist for all store 07 and store 11 fridge sensors from 01:00 to 05:00 AWST on 21, 22 and 23 Nov (Sam Whitlock, TernCloud data explorer, internal note 2026-11-24 01:30 UTC).
- [Verified] Those readings were ingested 05:41 to 06:07 AWST each day; both gateways are G4-C cellular units that upload buffered readings in a batch (Sam Whitlock, data explorer, 2026-11-24 01:30 UTC; models confirmed in account record).
- [Verified] The daily report job runs at 05:30 AWST for the previous night, all stores (account record, report schedule; Sam Whitlock, 2026-11-24 01:30 UTC).
- [Verified] Store 07's report for 22 Nov, regenerated at 02:15 UTC on 24 Nov (well after the 05:41 AWST 22 Nov ingestion), still shows "No data" for 01:00 to 05:00 (Sam Whitlock, Reports > Regenerate, internal note 2026-11-24 02:20 UTC). Only this one report has been regenerated.
- [Reported] Reports for stores 07 and 11 show "No data" 01:00 to 05:00 on 21, 22 and 23 Nov; every other store's report is complete (Nadia Rahman, 2026-11-23 23:40 UTC).
- [Reported] Last night's reports (night of 24 Nov) for stores 07 and 11 have the same gap (Nadia Rahman, 2026-11-25 01:15 UTC). Not yet checked by support.
- [Reported] A report with gaps is treated as a cold-chain break unless the readings can be shown; the customer needs complete reports for 21, 22 and 23 Nov (Nadia Rahman, 2026-11-23 23:40 UTC). Account is flagged "Regulated cold-chain customer (vaccine storage)" (account record).
- [Verified] Login fault fixed: HPG-StoreManagers had no role mapping (9 failed sign-ins 22:50 to 23:35 UTC 23 Nov, "no role mapping"); Sam mapped it to Site Viewer at 04:45 UTC 24 Nov; 9 successful sign-ins 05:02 to 05:28 UTC (Sam Whitlock, SSO config and sign-in log, notes 2026-11-24 01:30 and 05:35 UTC). Customer confirmed (Nadia Rahman, 2026-11-24 05:30 UTC).
- [Reported, other customer] TRN-77954 (Westfield Aged Care, 12 Nov) had a report job using UTC midnight instead of site-local midnight, fixed by correcting the schedule time zone (pasted by Dev Sharma, internal note 2026-11-25 01:30 UTC). Unverified for HPG; a lead only. Its credit and closure steps do not apply to this ticket.
- Conflict: the customer's reports say "No data", but support verified the readings exist in TernCloud. The data was captured; the report generation leaves it out.
- Conflict: the customer says a manager promised a full refund of this quarter's Premier fee by phone (Nadia Rahman, 2026-11-25 01:15 UTC). Support found no record of the call or offer on the ticket or account (Sam Whitlock, 2026-11-25 01:50 UTC), and the account record shows "Refunds: None" and "Open credits: None".

## Tried so far
- 2026-11-24 01:30 UTC, Sam Whitlock: checked SSO role mappings and sign-in log -> no mapping for HPG-StoreManagers; 9 failed sign-ins, all "no role mapping".
- 2026-11-24 01:30 UTC, Sam Whitlock: checked data explorer for store 07 and 11 sensors -> readings present for all three nights, ingested 05:41 to 06:07 AWST, after the 05:30 AWST job. Hypothesis (job runs too early) recorded as not confirmed.
- 2026-11-24 02:15 UTC, Sam Whitlock: regenerated store 07 report for 22 Nov -> still "No data" 01:00 to 05:00; timing alone does not explain the gap.
- 2026-11-24 03:00 UTC, Sam Whitlock: asked customer which role store managers need -> "Site Viewer" (Nadia Rahman, 04:30 UTC).
- 2026-11-24 04:45 UTC, Sam Whitlock: mapped HPG-StoreManagers to Site Viewer -> logins work (customer confirmed 05:30 UTC; sign-in log 05:35 UTC).
- 2026-11-25 01:30 UTC, Dev Sharma: pasted TRN-77954 root cause from another customer -> result not recorded (not tested against HPG's schedule).
- 2026-11-25 01:50 UTC, Sam Whitlock: passed the refund request to Account Manager Bianca Torres -> result not recorded.
- 2026-11-25 02:10 UTC, Sam Whitlock: escalated to Tier 2 (Field Systems Engineering), priority P2, status Escalated.

## Commitments to the customer
- "I'll start with the logins, since that should be quicker." (Sam Whitlock, 2026-11-24 00:52 UTC), no due time stated, met (logins fixed 04:45 UTC 24 Nov).
- "I'm escalating the reports issue to our Field Systems Engineering team today." (Sam Whitlock, 2026-11-25 00:40 UTC), due "today", met (escalated 02:10 UTC 25 Nov).
- "I'll send you an update by 15:00 AWST today, Wednesday 25 November (07:00 UTC)." (Sam Whitlock, 2026-11-25 01:50 UTC), due 15:00 AWST Wed 25 Nov (07:00 UTC), open. Tier 2 now owns it (policy 5.3).
- [Reported, unconfirmed] "Your manager promised me a full refund of this quarter's Premier support fee when we spoke on the phone yesterday afternoon" (Nadia Rahman, 2026-11-25 01:15 UTC); customer asks for it to be processed "this week". No matching message in the thread. Policy 6.3: only the Account Manager (Bianca Torres) or the Head of Customer Support may offer a refund, and "An offer is valid only when recorded in writing on the ticket or in the account record." None is recorded. Do not confirm or deny it to the customer; it sits with Bianca Torres.

## Service level
- Plan: Premier (account record).
- Priority: P2, set at ticket creation 2026-11-23 23:40 UTC and reconfirmed at escalation 2026-11-25 02:10 UTC (thread events). Fits 2.2: "alarms, data delivery, reporting or user access fail for some gateways or users, and there is no practical workaround" (2 of 12 gateways; not P1 under 2.1, "more than half of the customer's gateways are offline"). One open point: the readings are visible in the data explorer; whether that is a "practical workaround" for a compliance report is not defined by the policy. If it were, P3 would apply (2.3) and the target would be 45 business hours. Priority has not changed, so P2 stands (2.5).
- Target: "Premier | P2 | 2 business hours | 18 business hours" (3.1); "Targets marked "24x7" run on calendar time. All others count business hours only." (3.3). Resolution requires every fault on the ticket resolved: "A ticket that reports more than one fault is resolved only when every fault on it is resolved." (1.5). The login fault is fixed, so the reports fault alone now decides resolution; the ticket must not be set Resolved while it is open.
- First response: met. Sam Whitlock replied 2026-11-24 00:52 UTC (08:52 AWST), 22 business minutes after the clock started; target 2 business hours (3.1, 1.4).
- Clock: started at ticket creation (4.1, "The clock starts when the ticket is created"), 2026-11-23 23:40 UTC = 07:40 AWST Tue 24 Nov, before business hours, so counting began 08:30 AWST Tue 24 Nov (00:30 UTC) (4.1, "for a ticket created outside them, counting starts when business hours next begin"). Business hours 08:30 to 17:30 AWST Mon to Fri, excluding WA public holidays (1.1). Paused 03:00 to 04:30 UTC on 24 Nov (11:00 to 12:30 AWST), 1 h 30 min, while "Pending customer" (4.2). Counted: Tue 24 Nov 7 h 30 min; Wed 25 Nov 9 h; Thu 26 Nov 1 h 30 min. Assumes no WA public holiday on 24 to 26 Nov; the inputs do not list holidays.
- Deadline: 10:00 AWST Thu 26 Nov 2026 (02:00 UTC Thu 26 Nov), as of now = 2026-11-25 02:10 UTC (10:10 AWST Wed), the latest timestamp in the thread (no "now" given by the user). Elapsed 9 h 10 min, remaining 8 h 50 min: within target. "At risk" means "less than 25% of its resolution target remains" (4.4), i.e. under 4 h 30 min, which happens at 14:30 AWST Wed 25 Nov (06:30 UTC), before the 07:00 UTC promised update. It was not at risk at escalation, so the Team Lead notification in 5.2 was not triggered then.
- Update cadence: "P2: at least once each business day." (7.1). Tier 2 owns customer updates from escalation (5.3).

## Recommended next action
Work out why the regenerated store 07 report for 22 Nov excludes readings that were already in TernCloud. Compare how the report job selects readings (by reading timestamp or by ingestion time, and over which time window and time zone) for HPG's schedule against the data explorer records for 01:00 to 05:00 AWST on 22 Nov. This is the most decisive open question: the "job runs too early" hypothesis is already disproved by the regeneration, and the cause decides both the fix and whether the 21, 22 and 23 Nov reports (plus last night's) can be regenerated complete, which the customer needs for cold-chain records. The deadline is 18 hours away in business time, the ticket becomes at risk at 14:30 AWST today, and the gap recurs at every 05:30 AWST run. Send the promised 15:00 AWST (07:00 UTC) update today whatever the findings.

Open questions:
- Does the report job select readings by ingestion time or by a window that excludes late-arriving batches, even on manual regeneration?
- Is HPG's report schedule time zone set correctly (the TRN-77954 lead), and does that explain a gap limited to the two cellular stores?
- Does store 11's report regenerate the same way as store 07's? Only store 07 for 22 Nov was tested.
- Is last night's (24 Nov) gap at stores 07 and 11 confirmed in the reports, with readings present in the data explorer?
- Can a complete report, or another record acceptable to the customer's compliance process, be produced for 21 to 24 Nov as a workaround while the fix is found?
- Has Bianca Torres made or recorded any refund or credit offer? Was a phone call with a manager on the afternoon of 24 Nov logged anywhere?
- Should the Support Team Lead be told once the ticket becomes at risk at 14:30 AWST?

Next customer update due: 15:00 AWST Wed 25 Nov 2026 (07:00 UTC), from Sam Whitlock's commitment; the policy minimum for P2 is at least once each business day (7.1).
