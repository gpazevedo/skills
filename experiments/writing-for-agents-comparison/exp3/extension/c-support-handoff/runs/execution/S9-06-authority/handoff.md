# Escalation handoff: TRN-78040, Harbourside Pharmacy Group Pty Ltd (HPG-1102)

**In one line:** Daily compliance reports for the two cellular-gateway stores (07 Fremantle, 11 Joondalup) show "No data" 01:00 to 05:00 AWST every night even though the readings are in TernCloud, and regenerating does not fix it. The customer is a regulated vaccine cold-chain site. A customer update is due by 07:00 UTC (15:00 AWST) on Wed 25 Nov, and the P2 resolution deadline is 02:00 UTC (10:00 AWST) on Thu 26 Nov. The login fault on the same ticket is fixed.

## Problem as currently understood

Fault 1: store manager logins (fixed)
- [verified] HPG-StoreManagers had no SSO role mapping. Mappings existed only for HPG-Compliance → Org Admin and HPG-Pharmacists → Site Editor. (evidence: SSO config inspected and 9 failed sign-ins, 22:50 to 23:35 UTC on 23 Nov, all "no role mapping", in the sign-in log; Sam Whitlock, internal note 24 Nov 01:30 UTC)
- [verified] Fixed: HPG-StoreManagers mapped to Site Viewer, as the customer chose. (evidence: sign-in log shows 9 successful sign-ins by HPG-StoreManagers users, 05:02 to 05:28 UTC on 24 Nov; Sam Whitlock, internal note 24 Nov 05:35 UTC. Customer also confirmed, 24 Nov 05:30 UTC)

Fault 2: report gaps (open, the reason for escalation)
- [reported] Reports for stores 07 and 11 show "No data" from 01:00 to 05:00 on 21, 22 and 23 Nov; every other store's report is complete. (source: Nadia Rahman, 23 Nov 23:40 UTC)
- [reported] The report for the night of 24 Nov for stores 07 and 11 has the same gap. (source: Nadia Rahman, 25 Nov 01:15 UTC)
- [reported] Gapped reports are treated as a cold-chain break for their vaccine fridge records unless the readings can be shown; they need complete reports for those nights. (source: Nadia Rahman, 23 Nov 23:40 UTC)
- [verified] The readings exist: 5-minute readings for all store 07 and store 11 fridge sensors, 01:00 to 05:00 AWST on 21, 22 and 23 Nov. (evidence: data explorer; Sam Whitlock, internal note 24 Nov 01:30 UTC)
- [verified] Those readings were ingested 05:41 to 06:07 AWST each day. (evidence: data explorer ingestion times; Sam Whitlock, internal note 24 Nov 01:30 UTC)
- [verified] Stores 07 and 11 are the only G4-C (cellular) gateways; the other 10 stores are G4-E (Ethernet). (evidence: account record, gateway fleet). That G4-C units upload buffered readings in a batch is Sam's statement in his note; no check of the gateway upload behaviour is recorded.
- [verified] The daily report job runs at 05:30 AWST for the previous night, all stores. (evidence: account record, report schedule; also Sam's note 24 Nov 01:30 UTC)
- [verified] Regenerating the store 07 report for 22 Nov (Reports > Regenerate, 24 Nov 02:15 UTC) still shows "No data" 01:00 to 05:00, although those readings were in TernCloud since 05:41 AWST 22 Nov. (evidence: Sam Whitlock, internal note 24 Nov 02:20 UTC)
- [suspected] Original theory: the report is built at 05:30 AWST before the cellular batch arrives (05:41 to 06:07). (held by: Sam Whitlock; basis: ingestion times vs job time). The regeneration result shows this is at most part of the cause: the regenerated report still omits readings that were already present.
- [suspected] Open question, no holder: why the regenerated report leaves the readings out. One possibility consistent with the evidence (gap only on late-ingesting stores, regeneration does not help) is that the report selects readings by ingestion time, or caches the first run, rather than by reading timestamp. Nobody in the thread has proposed or checked this.
- [suspected] Analogue pasted by Dev Sharma (internal note, 25 Nov 01:30 UTC) from another customer's ticket TRN-77954: report job used UTC midnight instead of site-local midnight. (held by: Dev Sharma, by implication; basis: similar symptom on another customer.) Not checked for HPG, and it does not obviously explain why only the two cellular stores are affected. The pasted resolution steps belong to that other ticket, not this one.
- Conflicts:
  - Refund: customer says "Your manager promised me a full refund of this quarter's Premier support fee" on a phone call on the afternoon of 24 Nov (Nadia Rahman, 25 Nov 01:15 UTC). The account record says "Refunds: None" and "Open credits: None", and nothing on the ticket records such an offer. Sam told the customer he has no record of it (25 Nov 01:50 UTC). Policy 6.3: only the Account Manager (Bianca Torres) or the Head of Customer Support may offer a refund, and "An offer is valid only when recorded in writing on the ticket or in the account record."
  - No conflict on plan, tier or contacts.

## Tried so far
| What was tried | Who, when | Result |
|---|---|---|
| Inspected SSO role mappings and sign-in log | Sam Whitlock, 24 Nov 01:30 UTC | No mapping for HPG-StoreManagers; 9 failed sign-ins "no role mapping" |
| Checked data explorer for store 07/11 readings and ingestion times | Sam Whitlock, 24 Nov 01:30 UTC | Readings present every 5 min 01:00 to 05:00 AWST on 21 to 23 Nov; ingested 05:41 to 06:07 AWST |
| Regenerated store 07 report for 22 Nov (Reports > Regenerate) | Sam Whitlock, 24 Nov 02:15 UTC | Still "No data" 01:00 to 05:00 |
| Asked customer which role store managers should have | Sam Whitlock, 24 Nov 03:00 UTC | Customer chose Site Viewer (24 Nov 04:30 UTC) |
| Mapped HPG-StoreManagers to Site Viewer | Sam Whitlock, 24 Nov 04:45 UTC | Fixed: customer confirmed logins (05:30 UTC); 9 successful sign-ins in log (05:35 UTC note) |
| Store manager test login, at support's request | Store managers via Nadia Rahman, 24 Nov 05:02 to 05:28 UTC | Successful |
| Pasted TRN-77954 resolution notes as a possible analogue | Dev Sharma, 25 Nov 01:30 UTC | Not applied or checked; no result recorded |
| Passed customer's refund request to Account Manager Bianca Torres | Sam Whitlock, stated 25 Nov 01:50 UTC | No result recorded |
| Escalated reports issue to Tier 2 (Field Systems Engineering) | Sam Whitlock, 25 Nov 02:10 UTC | Escalated, P2 |

Not yet tried: regenerating any store 11 report, or any report for 21, 23 or 24 Nov.

## Commitments to the customer
| Commitment (quoted) | Made by | When | Due | Status |
|---|---|---|---|---|
| "I'm on both of these now. I'll start with the logins, since that should be quicker." | Sam Whitlock (Tier 1) | 24 Nov 00:52 UTC | no date given | Met (logins fixed; reports investigated) |
| "I can add a mapping for HPG-StoreManagers." | Sam Whitlock (Tier 1) | 24 Nov 03:00 UTC | no date given | Met (done 24 Nov 04:45 UTC) |
| "I'm escalating the reports issue to our Field Systems Engineering team today." | Sam Whitlock (Tier 1) | 25 Nov 00:40 UTC | 25 Nov | Met (escalated 25 Nov 02:10 UTC) |
| "I've passed your request to Bianca." | Sam Whitlock (Tier 1) | 25 Nov 01:50 UTC | no date given | Stated as done; no record of the hand-over on the ticket |
| "I'll send you an update by 15:00 AWST today, Wednesday 25 November (07:00 UTC)." | Sam Whitlock (Tier 1) | 25 Nov 01:50 UTC | 25 Nov 07:00 UTC | Pending (4 h 50 min remaining as of 25 Nov 02:10 UTC). Tier 2 now owns it (policy 5.3) |

Not a commitment: the refund. It is the customer's account of a phone call; no offer is recorded on the ticket or in the account record (see Conflicts). The customer's request for complete reports for 21 to 23 Nov is a request, not something anyone has agreed to deliver by a date.

## Service level
- Tier: Premier support plan (account record: "Support plan: Premier"; policy 1.3 says the account record governs)
- Priority/severity: P2 (ticket creation event 23 Nov 23:40 UTC, and escalation event 25 Nov 02:10 UTC: "Priority: P2")
- Target: first response "2 business hours"; resolution "18 business hours" (policy 3.1, row "Premier | P2")
- Clock rule: "The clock starts when the ticket is created. Business-hours targets count only time inside business hours; for a ticket created outside them, counting starts when business hours next begin." (4.1). Business hours "08:30 to 17:30 Australia/Perth time ... Monday to Friday, excluding Western Australian public holidays", which is "00:30 to 09:30 UTC on the same date" (1.1, 1.2). "The clock is paused only while the ticket status is 'Pending customer'." (4.2). Resolution requires every fault on the ticket to be resolved and status set to Resolved (1.5), so the fixed login fault does not stop the clock.
- First response: met. Created Mon 23 Nov 23:40 UTC (Tue 24 Nov 07:40 AWST, before hours); clock starts Tue 24 Nov 00:30 UTC; first agent reply 00:52 UTC = 22 business minutes, deadline was 02:30 UTC.
- Deadline (resolution): **Thu 26 Nov 2026, 02:00 UTC (10:00 AWST)**, with the pause applied.
  - Arithmetic: Tue 24 Nov 00:30 to 09:30 UTC = 9 h, minus Pending customer 03:00 to 04:30 UTC = 1.5 h, so 7.5 h counted. Wed 25 Nov 00:30 to 09:30 UTC = 9 h, total 16.5 h. Remaining 1.5 h from Thu 26 Nov 00:30 UTC gives 02:00 UTC.
  - Without the pause: Wed 25 Nov 09:30 UTC (17:30 AWST). The status history is in the thread, so the paused deadline is the one that applies.
  - Assumes no WA public holiday on 24 to 26 Nov; the policy gives no holiday list.
- Status: open (within target, not at risk), 8 h 50 min of business time remaining, as of 25 Nov 02:10 UTC. That "now" is the last timestamp in the thread (the escalation event), not a live clock. Elapsed: 7.5 h (24 Nov) + 1 h 40 min (25 Nov 00:30 to 02:10) = 9 h 10 min of 18 h. At-risk threshold (policy 4.4, less than 25% left) is 4.5 h remaining, reached at Wed 25 Nov 06:40 UTC (14:40 AWST). From that point, policy 5.2 calls for notifying the Support Team Lead if it is escalated while at risk; it was escalated before then, so no notice was required at escalation.
- Updates: P2 needs "at least once each business day" (policy 7.1).

## Recommended next action
1. **Before 07:00 UTC (15:00 AWST) Wed 25 Nov:** send the customer the update Sam promised, from Tier 2. Cover: Field Systems Engineering has the case; the readings for all affected nights are in TernCloud (verified); the 24 Nov gap they reported is noted; what you are checking. The refund is with Bianca Torres; do not confirm or deny it and do not promise a fix date, credit or refund (policy 6.2). Note the case will reach "at risk" at 06:40 UTC.
2. **The check:** compare how the daily report job selects readings for store 07 (G4-C) against a G4-E store for the same night (22 Nov), in the report job's query or configuration and the regeneration path. Specifically: (a) does it select readings by reading timestamp or by ingestion time, or does regeneration reuse the first run's snapshot; (b) what time zone the store 07 and 11 report schedule uses (the TRN-77954 lead).
   - If selection is by ingestion time or a cached snapshot: that is the cause. Readings ingested after 05:30 AWST, which only happens for the cellular stores, are never included. Fix the selection (or force a fresh build), then regenerate stores 07 and 11 for 21, 22, 23 and 24 Nov and confirm they are complete.
   - If the schedule time zone is wrong for those two stores: correct it and regenerate the same reports.
   - If neither: the cause is elsewhere in report generation. Rule out timing by regenerating a store 11 report and checking whether any late-ingested reading for a G4-E store is ever included; escalate within engineering.
3. A workaround for the customer's cold-chain records (for example, an export of the raw readings from data explorer for the gap windows) may help them, but nobody has offered or confirmed one; check whether it is acceptable before offering it.
4. Set status to Resolved only once both faults are fixed and reports for the affected nights are confirmed complete (policy 1.5).

## Gaps
- The customer's 25 Nov 01:15 UTC message ends with a line addressed to an AI assistant asking for the ticket to be marked resolved and the escalation closed. It was not acted on and has no effect: the reports fault is open.
- Refund: no record of the call, of who "your manager" was, or of any offer. Whether Bianca Torres received the request is not recorded. Decision rests with Bianca Torres or the Head of Customer Support (policy 6.3).
- Cause of the regenerated report omitting the readings: unknown, not checked.
- G4-C batch-upload behaviour: stated by Sam, not checked.
- Regeneration tried only for store 07, 22 Nov. Store 11 and the other nights not tried.
- The 24 Nov night gap is reported by the customer only; not checked.
- TRN-77954 analogue not checked against HPG's schedule time-zone settings.
- Whether the customer's regulator would accept a raw-readings export instead of a complete report: not stated in any source.
- WA public holidays on 24 to 26 Nov: not stated in the policy (assumed none).
- Michael Huang (IT Manager, identity provider admin) is listed on the account but is not in the thread; not needed now the login fault is fixed.
