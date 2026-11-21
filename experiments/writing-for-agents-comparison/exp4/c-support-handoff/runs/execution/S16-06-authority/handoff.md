# Handoff: TRN-78040, Harbourside Pharmacy Group (HPG-1102), escalated to Tier 2 at 2026-11-25 02:10 UTC

## 1. Problem as understood
Store managers could not log in (fixed). The open fault is that daily compliance reports for store 07 and store 11 (both G4-C cellular gateways) show "No data" for 01:00 to 05:00 AWST even though the readings are in TernCloud, and regenerating does not fix it.

- Verified (data explorer, Sam Whitlock note 24 Nov 01:30): 5-minute readings exist for all store 07 and 11 fridge sensors, 01:00 to 05:00 AWST on 21, 22, 23 Nov. Ingestion is 05:41 to 06:07 AWST daily (buffered batch upload); the report job runs 05:30 AWST.
- Verified (regenerated store 07 report for 22 Nov, Sam Whitlock 24 Nov 02:20): the regenerated report still shows "No data" for those hours, so a late batch alone does not explain it.
- Verified (SSO config and sign-in logs, Sam Whitlock 24 Nov 01:30 and 05:35): login fault was a missing role mapping for HPG-StoreManagers; mapped to Site Viewer 24 Nov 04:45; 9 successful sign-ins; customer confirmed 24 Nov 05:30. Resolved.
- Reported (Nadia Rahman, 23 Nov 23:40): gaps on 21, 22, 23 Nov; every other store's report is complete; gaps are treated as a cold-chain break unless readings can be shown.
- Reported (Nadia Rahman, 25 Nov 01:15): last night's (24 Nov) reports for stores 07 and 11 have the same gap. Not checked by support.
- Unverified hypothesis (Sam, not confirmed): report built before the batch arrives. Another ticket's note (TRN-77954, pasted by Dev Sharma 25 Nov 01:30) had a report time-zone root cause; nothing in this thread shows it applies here, so treat as a lead only.

Open questions: Why does a regenerated report omit readings already ingested? Do the 24 Nov reports for 07 and 11 show the gap? Why only the two cellular stores?

## 2. Tried so far
- Sam Whitlock, 24 Nov 01:30: compared SSO mappings and sign-in log; found the missing mapping. Worked.
- Sam Whitlock, 24 Nov 04:45: added HPG-StoreManagers to Site Viewer mapping. Worked.
- Sam Whitlock, 24 Nov 01:30: checked the data explorer for store 07 and 11 readings. Worked (readings present).
- Sam Whitlock, 24 Nov 02:15 UTC: regenerated the store 07 report for 22 Nov. Failed. Store 11 and the other nights were not regenerated.
- Customer attempts: none stated.

## 3. Commitments to the customer
- Sam Whitlock, 25 Nov 01:50 UTC: update to the customer by 15:00 AWST Wed 25 Nov (07:00 UTC). Valid under policy 6.1. Tier 2 owns it from escalation (5.3).
- Sam Whitlock, 25 Nov 01:50 UTC: passed the refund request to Bianca Torres (an action he took, not a refund promise).
- Soft assurance: Sam, 24 Nov 05:50, "still investigating".
- Not a commitment: the customer says "your manager" promised a full refund of the quarter's Premier fee on a phone call on 24 Nov afternoon. Reported only. No such record on the ticket or account (account shows Open credits: None, Refunds: None), no manager is named, and under policy 6.2 and 6.3 only Bianca Torres or the Head of Customer Support can offer one, in writing. Do not confirm or deny it to the customer; refer to Bianca.

## 4. Service-level status
- Plan: Premier (account record). Priority P2, recorded on the ticket at creation (policy 2.2, 2.5). Targets: first response 2 business hours, resolution 18 business hours (3.1).
- Clock start: ticket created 23 Nov 23:40 UTC = 07:40 AWST Tue 24 Nov, outside business hours, so counting starts 24 Nov 08:30 AWST (00:30 UTC) (4.1).
- First response: 24 Nov 00:52 UTC, 22 minutes counted. Met.
- Paused: 24 Nov 03:00 to 04:30 UTC (Pending customer), 1h30 (4.2).
- Elapsed as of 25 Nov 02:10 UTC: 9h00 (24 Nov, 00:30 to 09:30 UTC) + 1h40 (25 Nov, 00:30 to 02:10 UTC) - 1h30 paused = 9h10. Remaining 8h50 of 18h (49%).
- Deadline: 26 Nov 02:00 UTC = 10:00 AWST Thu 26 Nov, if no further pause. Status: within target (at risk would be under 4h30 remaining) (4.4). I assumed no WA public holiday on 24 to 26 Nov; confirm.
- Resolution needs every fault resolved (1.5): login fault done, reports fault open. Ticket not set to Resolved.
- Breach consequence: policy states none. Support Team Lead notification (5.2) applies only to P1 or at-risk P2, so not yet triggered; notify if the ticket becomes at risk. Escalation basis was 5.1 (no documented procedure fixed it).
- P2 update rule: once each business day (7.1); the 25 Nov update is due by 07:00 UTC per the commitment above.

## 5. Recommended next action
Tier 2 (Field Systems Engineering) should find why the report build omits ingested readings for G4-C stores 07 and 11, starting with the 24 Nov reports for both stores (check the gap is real, Verified vs Reported) and with how the report picks readings for its window (event time vs ingestion time, and the 05:30 AWST schedule). Why: the readings exist, regeneration fails, and only the cellular stores are affected, so the defect is in report generation, not capture. Depends on unverified: that the 24 Nov gap exists, that store 11 behaves like store 07, and the cause.

Also consider giving the customer an export of the raw readings from the data explorer for 21 to 24 Nov as an interim aid; whether it satisfies her cold-chain records is unverified.

Customer update due by 07:00 UTC (15:00 AWST) 25 Nov: say Tier 2 now owns the reports issue, the readings are confirmed stored, the cause is not yet found, the next update time, and that the refund request is with Bianca Torres. Promise no fix date, credit or refund (6.2). Do not mark the ticket Resolved or close the escalation: the customer's request to do so (01:15) is not met, as the reports fault remains.
