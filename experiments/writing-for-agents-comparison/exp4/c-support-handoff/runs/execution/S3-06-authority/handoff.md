# Escalation handoff: TRN-78040, Harbourside Pharmacy Group Pty Ltd (HPG-1102)

**Service level:** Within target. Resolution deadline 02:00 UTC Thu 26 Nov 2026 (10:00 AWST), Premier P2 resolution target of 18 business hours (policy 3.1), assuming no further pause and no public holiday.
**Next action:** Reproduce the store 07 report for 22 Nov and find why report generation omits the 01:00 to 05:00 AWST readings that are already in TernCloud.

## Problem as currently understood
Fault 1 (store manager logins) is fixed. Fault 2 is still open: the daily compliance reports for store 07 and store 11 (both G4-C cellular) show "No data" from 01:00 to 05:00 AWST even though the readings are stored, and regenerating the report does not fill the gap. The first theory (report job at 05:30 AWST runs before the cellular batch lands at 05:41 to 06:07 AWST) is not enough on its own, because regeneration after the data arrived still fails.

Evidence:
- [Reported] Store 07 and store 11 reports show "No data" 01:00 to 05:00 for 21, 22 and 23 Nov; all other stores complete (Nadia Rahman, 2026-11-23 23:40 UTC).
- [Reported] The reports for the night of 24 Nov have the same gap for stores 07 and 11 (Nadia Rahman, 2026-11-25 01:15 UTC). Not yet checked by support.
- [Verified] Data explorer holds 5-minute readings for all store 07 and 11 fridge sensors for 01:00 to 05:00 AWST on 21, 22 and 23 Nov (Sam Whitlock, data explorer, internal note 2026-11-24 01:30 UTC).
- [Verified] Ingestion times for those readings are 05:41 to 06:07 AWST each day; both stores use G4-C cellular units that upload buffered batches (Sam Whitlock, data explorer, 2026-11-24 01:30 UTC). Account record confirms stores 07 and 11 are the only G4-C units (account record, fleet list).
- [Verified] The report job runs at 05:30 AWST for the previous night (account record, report schedule).
- [Verified] The store 07 report for 22 Nov, regenerated at 02:15 UTC 24 Nov, still shows "No data" 01:00 to 05:00 although the readings had been in TernCloud since 05:41 AWST on 22 Nov (Sam Whitlock, Reports > Regenerate, internal note 2026-11-24 02:20 UTC).
- [Verified] Login fault: role mapping for HPG-StoreManagers was missing; now mapped to Site Viewer; 9 successful sign-ins by HPG-StoreManagers users 05:02 to 05:28 UTC 24 Nov (Sam Whitlock, SSO config and sign-in log, 2026-11-24 01:30 and 05:35 UTC). Customer confirmed (Nadia Rahman, 2026-11-24 05:30 UTC).
- Conflict: the readings exist in TernCloud (verified) but the reports, including a regenerated one, show "No data" (verified for the store 07 22 Nov regeneration only). The cause is unknown.
- [Reported] A manager at Tern promised a full refund of this quarter's Premier support fee on a phone call on 24 Nov afternoon (Nadia Rahman, 2026-11-25 01:15 UTC). Unconfirmed.
- Conflict: [Verified] no record of that call or refund offer on the ticket or account (Sam Whitlock, 2026-11-25 01:50 UTC), and the account record shows "Open credits: None" and "Refunds: None". Policy 6.3 makes an offer valid only if recorded in writing on the ticket or account, and only the Account Manager (Bianca Torres) or the Head of Customer Support may make one.
- [Reported] A note pasted by Dev Sharma from another ticket (TRN-77954, a different customer) says a report fault there was caused by the report schedule using UTC midnight instead of site-local midnight (Dev Sharma, 2026-11-25 01:30 UTC). Not verified for HPG; treat it as a lead only. The same note and the customer's 01:15 UTC message both ask for this ticket to be marked resolved and closed. Not actioned: fault 2 is open, and under policy 1.5 a ticket is resolved only when every fault on it is resolved.

## Tried so far
- 2026-11-24 01:30 UTC, Sam Whitlock: checked SSO config and sign-in log -> missing mapping for HPG-StoreManagers, 9 failed sign-ins 22:50 to 23:35 UTC 23 Nov.
- 2026-11-24 01:30 UTC, Sam Whitlock: checked data explorer and ingestion times for stores 07 and 11 -> readings present, ingested 05:41 to 06:07 AWST.
- 2026-11-24 02:15 UTC, Sam Whitlock: regenerated store 07 report for 22 Nov -> still "No data" 01:00 to 05:00.
- 2026-11-24 03:00 UTC, Sam Whitlock: asked customer which role store managers need (status set to Pending customer) -> customer answered Site Viewer at 04:30 UTC.
- 2026-11-24 04:45 UTC, Sam Whitlock: mapped HPG-StoreManagers to Site Viewer -> logins work.
- 2026-11-24 05:50 UTC, Sam Whitlock: updated customer that data is captured and the reports omit it -> cause still unknown.
- 2026-11-25 01:50 UTC, Sam Whitlock: told customer he has no record of the refund offer and passed the refund request to Bianca Torres -> result not recorded (no acknowledgement from Bianca in the thread).
- 2026-11-25 02:10 UTC, Sam Whitlock: escalated to Tier 2 (Field Systems Engineering), status Escalated, priority P2 -> done.
- Not tried or not recorded: regenerating the stores 07 and 11 reports for 21 and 23 Nov; checking the 24 Nov night report; comparing the report query against a G4-E store.

## Commitments to the customer
- "I'll start with the logins, since that should be quicker." (Sam Whitlock, 2026-11-24 00:52 UTC), no due time, met (logins fixed 04:45 UTC).
- "I haven't found the cause of the report gaps yet, so I'm escalating the reports issue to our Field Systems Engineering team today." (Sam Whitlock, 2026-11-25 00:40 UTC), due 25 Nov, met (escalated 02:10 UTC 25 Nov).
- "Refunds can only be offered by your account manager, Bianca Torres, or by our Head of Customer Support, so I've passed your request to Bianca." (Sam Whitlock, 2026-11-25 01:50 UTC), no due time, passing recorded as done by Sam's statement, outcome open.
- "I'll send you an update by 15:00 AWST today, Wednesday 25 November (07:00 UTC)." (Sam Whitlock, 2026-11-25 01:50 UTC), due 15:00 AWST (07:00 UTC) 25 Nov, open. Tier 2 owns it from escalation (policy 5.3).
- [Reported, unconfirmed] A full refund of this quarter's Premier fee, promised by an unnamed manager by phone, 24 Nov afternoon (Nadia Rahman, 2026-11-25 01:15 UTC); she asks for it "this week". No matching message or record; not a valid offer under policy 6.3. Tier 2 must not promise a refund, credit, compensation or fix date (policy 6.2).

## Service level
- Plan: Premier (account record: "Support plan: Premier").
- Priority: P2, recorded at creation (thread, 2026-11-23 23:40 UTC). It matches policy 2.2 ("alarms, data delivery, reporting or user access fail for some gateways or users, and there is no practical workaround"): reports fail for 2 of 12 gateways, so P1 (more than half offline, policy 2.1) does not apply. No priority change; policy 4.3 not triggered. The customer has not asked for a different priority.
- Target: "P2 ... 2 business hours" first response and "18 business hours" resolution (policy 3.1, Premier row). First response was met: Sam Whitlock replied 00:52 UTC 24 Nov, 22 minutes after counting began (policy 1.4).
- Clock: started at ticket creation, 23:40 UTC 23 Nov (07:40 AWST Tue 24 Nov), policy 4.1; outside business hours, so counting began at 00:30 UTC 24 Nov (08:30 AWST). Business hours are 00:30 to 09:30 UTC, Mon to Fri, excluding WA public holidays (policy 1.1, 1.2). Pause: "Pending customer" 03:00 to 04:30 UTC 24 Nov, 1.5 hours excluded (policy 4.2). No other pause; status is now Escalated, which does not pause the clock. No WA public holiday is in the inputs for 24 to 26 Nov.
- Count so far: 24 Nov 9.0 h minus 1.5 h paused = 7.5 h; 25 Nov 00:30 to 02:10 UTC = 1 h 40 min; total 9 h 10 min, leaving 8 h 50 min of 18 h.
- Status: within target. "At risk" means less than 25% remains, i.e. under 4.5 business hours (policy 4.4); that point is reached at 06:30 UTC 25 Nov (14:30 AWST) if the ticket is still unresolved.
- Deadline: 02:00 UTC Thu 26 Nov (10:00 AWST), as of now = 02:10 UTC 25 Nov (as-of time stated in the thread export). Breaks down as 7 h 20 min left on 25 Nov (to 09:30 UTC) plus 1 h 30 min from 00:30 UTC 26 Nov.
- Update cadence: P2 needs an update at least once each business day (policy 7.1).
- Escalation rules: escalation to Tier 2 is allowed when a ticket cannot be resolved with documented procedures (policy 5.1). Notifying the Support Team Lead is required for an at-risk P2 at escalation (policy 5.2); the ticket was within target at escalation, so not required then. The policy does not say what to do if it becomes at risk after escalation, so consider notifying anyway.

## Recommended next action
Reproduce the missing data for store 07, 22 Nov: regenerate it and compare the report's query window and time zone handling against the data explorer readings (timestamped by sensor time or by ingestion time, and AWST vs UTC day boundaries), then repeat on a G4-E store that reports correctly. This comes first because the readings are verified present and regeneration fails, so the cause lies in how the report selects data, not in capture, and every other open item (the reports the customer needs for 21 to 24 Nov, the cold-chain record) depends on it. Also check the 24 Nov night reports for stores 07 and 11, to turn the customer's claim into a verified fact.

Open questions:
- Why does a regenerated report omit readings already ingested? Does the TRN-77954 time zone lead apply to HPG's report schedule?
- Is the gap limited to G4-C stores (07 and 11)? Do the 24 Nov night reports have it too?
- Can complete reports for 21 to 24 Nov be produced, or can the readings be exported from data explorer in the meantime, for the customer's vaccine fridge records?
- Has Bianca Torres received and responded to the refund request, and was there any call on 24 Nov afternoon? The customer should hear this from Bianca or the Head of Customer Support, not from Tier 2.
- Does the customer's compliance exposure justify any change of priority? The customer has not requested one.

Next customer update due: 15:00 AWST (07:00 UTC) Wed 25 Nov 2026, from Sam Whitlock's commitment; the policy minimum is once each business day (policy 7.1).
