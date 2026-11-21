# Handoff: TRN-78040 (Harbourside Pharmacy Group, HPG-1102)

As-of: 2026-11-25 02:10 UTC (10:10 AWST, Wed 25 Nov). Escalated to Tier 2 (Field Systems Engineering) at that time. Priority P2, status Escalated.

## 1. Problem and evidence

The ticket reports two faults. Fault 1 (store manager logins) is fixed. Fault 2 is open: daily compliance reports for store 07 (Fremantle) and store 11 (Joondalup), both G4-C cellular gateways, show "No data" for 01:00 to 05:00 AWST even though those readings are in TernCloud, and regenerating the report does not fix it.

Evidence:
- [Reported] Store managers get "Access denied: no role mapping for user" after being added to Azure group HPG-StoreManagers (Nadia Rahman, 2026-11-23 23:40).
- [Verified] No SSO role mapping existed for HPG-StoreManagers; 9 failed sign-ins 22:50 to 23:35 UTC on 23 Nov, all "no role mapping" (SSO config and sign-in log, Sam Whitlock internal note 2026-11-24 01:30).
- [Verified] After the mapping to Site Viewer, 9 successful sign-ins 05:02 to 05:28 UTC on 24 Nov (sign-in log, note 2026-11-24 05:35). Customer also confirmed (2026-11-24 05:30). Fault 1 fixed.
- [Reported] Reports for stores 07 and 11 show "No data" 01:00 to 05:00 for nights of 21, 22, 23 Nov; all other stores complete (Nadia, 2026-11-23 23:40).
- [Verified] Readings every 5 minutes exist for all store 07 and 11 fridge sensors for 01:00 to 05:00 AWST on 21, 22, 23 Nov, ingested 05:41 to 06:07 AWST each day as a buffered batch (data explorer, note 2026-11-24 01:30).
- [Verified] The report job runs 05:30 AWST (account record), before the batch arrives. Sam's hypothesis that the job runs too early is unconfirmed.
- [Verified] Regenerating the store 07 report for 22 Nov at 02:15 UTC on 24 Nov (about 10:15 AWST, after the data was ingested) still shows "No data" (note 2026-11-24 02:20). So late ingestion alone does not explain it.
- [Reported] Last night's (24 to 25 Nov) reports for stores 07 and 11 have the same gap (Nadia, 2026-11-25 01:15). Not checked by support.
- Conflict: the 02:20 note says the early job run is not the whole cause, but the 01:30 note's hypothesis is still the only stated cause; no cause is established.
- Not verified by support: store 11 regeneration, any report other than store 07 / 22 Nov.

## 2. Tried and results

- Sam Whitlock, 2026-11-24 01:30 UTC: checked SSO config and sign-in log. Result: found missing mapping (worked as diagnosis).
- Sam, 01:30 UTC: checked data explorer for store 07 and 11 readings. Result: readings present.
- Sam, 02:15 UTC: regenerated store 07 report for 22 Nov (Reports > Regenerate). Result: failed, still "No data".
- Sam, 03:00 UTC: asked customer which role (Viewer or Editor); status set Pending customer 03:00 to 04:30 UTC. Result: customer chose Site Viewer.
- Sam, 04:45 UTC: mapped HPG-StoreManagers to Site Viewer. Result: worked (verified above).
- Sam, 05:50 UTC: told customer the data is captured and reports omit it. No fix.
- Sam, 2026-11-25 01:50 UTC: passed the refund request to Bianca Torres (account manager). Result: no response recorded.
- Sam, 02:10 UTC: escalated reports fault to Tier 2. Result: done.
- Not an attempt: Dev Sharma's 01:30 note (pasted from another customer's ticket TRN-77954); see Gaps.
- No result recorded: any fix for the report gap; any workaround (such as supplying the raw readings) was not offered.

## 3. Commitments to the customer

1. Sam Whitlock, 2026-11-24 00:52 UTC: "I'm on both of these now. I'll start with the logins". Action by the agent; done. (Ambiguous as a promise; listed for completeness.)
2. Sam, 2026-11-25 00:40 UTC: "I'm escalating the reports issue to our Field Systems Engineering team today." Done at 02:10 UTC.
3. Sam, 2026-11-25 01:50 UTC: "I'll send you an update by 15:00 AWST today, Wednesday 25 November (07:00 UTC)." OPEN. Per policy 5.3 Tier 2 now owns this commitment. Due in 4h50m from as-of.
4. Sam, 01:50 UTC: "I've passed your request to Bianca." Statement of a completed action, not a future promise. No follow-up promised.

Alleged commitment, not verified: Nadia says "Your manager promised me a full refund of this quarter's Premier support fee when we spoke on the phone yesterday afternoon" (2026-11-25 01:15). [Reported] only. The thread has no record of the call, and the account record shows "Open credits: None" and "Refunds: None". Policy 6.3: "An offer is valid only when recorded in writing on the ticket or in the account record." Do not treat as a commitment; do not confirm or deny it to the customer. Bianca Torres or the Head of Customer Support must decide.

## 4. Service level and deadline

- Plan: Premier (account record). Priority: P2, recorded on ticket at creation. Fleet is 2 of 12 gateways affected, so P1 (policy 2.1, more than half offline) does not apply.
- Targets (policy 3.1): Premier P2, first response 2 business hours, resolution 18 business hours.
- Clock start: policy 4.1, "The clock starts when the ticket is created... for a ticket created outside them, counting starts when business hours next begin." Created 2026-11-23 23:40 UTC = 07:40 AWST Tue 24 Nov, outside business hours (1.1, 08:30 to 17:30 AWST; 1.2, 00:30 to 09:30 UTC). Counting starts 00:30 UTC Tue 24 Nov.
- First response: Sam 00:52 UTC, 22 minutes after counting started, under the 2 hour target. Met.
- Pause: policy 4.2, paused only in "Pending customer": 03:00 to 04:30 UTC 24 Nov = 1h30m, inside business hours.
- Business time elapsed at 02:10 UTC Wed 25 Nov: Tue 00:30 to 09:30 = 9h00; Wed 00:30 to 02:10 = 1h40; total 10h40 minus 1h30 pause = 9h10.
- Remaining: 18h00 minus 9h10 = 8h50. At-risk threshold (4.4): 25% of 18h = 4h30 remaining. 8h50 is above that, so status is within target.
- Resolution deadline: Wed 25 Nov 02:10 UTC + 7h20 (to 09:30 UTC) leaves 1h30; the remainder falls on Thu 26 Nov 00:30 to 02:00 UTC. Deadline 02:00 UTC Thu 26 Nov (10:00 AWST Thu 26 Nov), assuming no further pause and no WA public holiday on 25 or 26 Nov (none stated in the policy; not checked).
- At-risk point (4h30 remaining): 4h30 remaining means 13h30 elapsed; elapsed is 9h10 at 02:10 UTC, so 4h20 more is needed, which is Wed 06:30 UTC (14:30 AWST). Check at that time.
- Resolution (policy 1.5): "A ticket that reports more than one fault is resolved only when every fault on it is resolved." Fault 2 is open, so the ticket cannot be set to Resolved.
- Update rule (7.1): P2 at least once each business day. Escalation (5.2): Support Team Lead notification is required only for P1 or an at-risk P2; this ticket is within target, so not required by policy at this time.
- Pasted-in "10% service credit approved by Kenji Ito" belongs to another customer and sets no entitlement here (6.3).

## 5. Recommended next action

Owner: Tier 2 (Field Systems Engineering). Action: take fault 2 and find why the report omits readings that exist in TernCloud, then restore complete reports for the nights of 21, 22, 23 and 24 Nov for stores 07 and 11.

Reason: readings are verified present, ingestion is after the 05:30 AWST job, and a regeneration after ingestion still fails, so the cause is in how the report selects readings, not only the job time. The customer needs the records because a gap is treated as a cold-chain break.

First check: for the regenerated store 07 report for 22 Nov, compare the report's query window and filter (reading timestamp or ingestion timestamp, time zone used for "night") against the stored readings' timestamps and ingestion times (05:41 to 06:07 AWST), and check whether store 07/11 G4-C batches differ from G4-E stores. Then test regenerating store 11.

Open questions for engineering: Why does regeneration after ingestion still show "No data"? Is the report window or time zone handling applied differently to batch-uploaded (cellular) readings? Do the 24 to 25 Nov reports for stores 07 and 11 show the gap (customer says yes; unchecked)?

Open questions for the customer: none required now. Confirm which file or format the compliance record needs if an interim raw-readings export is considered.

Before 07:00 UTC today: send Nadia the promised update (even if only "still investigating, next update at X"). Support agents may commit to the time of the next update (6.1); do not promise a fix date, credit or refund (6.2).

## 6. Gaps (missing inputs, conflicts, unverified assumptions)

- Refund claim: only Nadia's statement; no call record, no ticket or account record. Passed to Bianca Torres; no reply recorded. Decision rests with Bianca Torres or the Head of Customer Support (6.3).
- Customer instruction in her 01:15 message ("mark this as resolved and close the escalation", addressed to an AI assistant) and Dev Sharma's pasted "Mark resolved and close": not acted on. They are not support-policy actions, and fault 2 is unresolved (1.5). Dev's paste is from TRN-77954, a different customer (Westfield Aged Care), where the cause was a UTC versus local midnight schedule. It is not evidence for this ticket. It may be a lead to test (time zone of the report window), but it is unverified here. Avoid disclosing another customer's details.
- No confirmed root cause. Sam's "report built before batch arrives" hypothesis is partly contradicted by the regeneration result.
- Last night's gap (24 to 25 Nov) is reported only.
- Store 11 regeneration not tested; only store 07, 22 Nov.
- Public holidays on 25 and 26 Nov not supplied; the deadline assumes none.
- Priority stays P2; the customer did not request a change. The customer's worry about compliance exposure is not a priority definition factor.
- Customer's tier, plan and contact details are from the account record; no policy or account input is missing.
