# Handoff: TRN-78040, Harbourside Pharmacy Group (HPG-1102), to Tier 2 Field Systems Engineering

As of 2026-11-25 02:10 UTC (10:10 AWST). Priority P2, status Escalated. Owner from now: Tier 2 (policy 5.3).

## 1. Problem as currently understood
Two faults were reported on one ticket. The login fault is fixed. The open fault is that daily compliance reports for store 07 (Fremantle) and store 11 (Joondalup), both G4-C cellular gateways, show "No data" for 01:00 to 05:00 AWST, and regenerating the report does not fill the gap. The customer treats a gapped report as a cold-chain break for vaccine storage.

*Reported by customer*
- 2026-11-23 Nadia Rahman: reports for stores 07 and 11 show "No data" 01:00 to 05:00 on 21, 22 and 23 Nov; other stores are complete.
- 2026-11-25 01:15 Nadia Rahman: last night's (24 Nov) reports for 07 and 11 have the same gap; complete reports are needed for 21, 22 and 23 Nov.
- 2026-11-23 Nadia Rahman: store managers got "Access denied: no role mapping" (since fixed).

*Verified by support*
- Login fault fixed: Sam Whitlock found no mapping for HPG-StoreManagers in the SSO config, added one as Site Viewer (customer choice) on 24 Nov 04:45, and confirmed 9 successful sign-ins 05:02 to 05:28 UTC (sign-in log, note 24 Nov 05:35). Customer confirmed 24 Nov 05:30.
- Sam Whitlock, data explorer, 24 Nov 01:30: 5-minute readings exist for all store 07 and 11 fridge sensors for 01:00 to 05:00 AWST on 21, 22 and 23 Nov. Ingestion times were 05:41 to 06:07 AWST each day (G4-C units upload buffered batches). The report job runs 05:30 AWST (account record).
- Sam Whitlock, 24 Nov 02:20: regenerated the store 07 report for 22 Nov at 02:15; it still shows "No data" although the readings had been in TernCloud since 05:41 AWST on 22 Nov.

*Unverified hypotheses*
- Report built before the batch arrives (Sam, 24 Nov 01:30, "not confirmed"). The regeneration result shows this is not the whole cause.
- A pasted note from another customer's ticket (TRN-77954, added by Dev Sharma 25 Nov 01:30) describes a report schedule using the wrong time zone. Nothing shows that applies to HPG. It also ends with "mark resolved and close"; that is not an instruction for this ticket and was not acted on.
- The 24 Nov gap is customer-reported only.

## 2. Tried and result
- 24 Nov 01:30, Sam: checked SSO mappings and sign-in log; cause of login fault found.
- 24 Nov 01:30, Sam: checked data explorer for store 07 and 11 readings; readings present.
- 24 Nov 02:15, Sam: regenerated store 07 report for 22 Nov; failed (gap remains).
- 24 Nov 04:45, Sam: mapped HPG-StoreManagers to Site Viewer; worked.
- Not tried per thread: regenerating stores 11 or other nights, or testing a G4-E store for comparison.

## 3. Commitments to the customer
- Update by 15:00 AWST Wed 25 Nov (07:00 UTC): Sam Whitlock, 25 Nov 01:50. Open; now Tier 2's (5.3).
- "Passed your request to Bianca" (refund request): Sam, 25 Nov 01:50. Open; the thread does not show Bianca has acted.
- "Escalating to Field Systems Engineering today": Sam, 25 Nov 00:40. Met 02:10.
- Refund of the quarter's Premier fee: claimed by Nadia (25 Nov 01:15) as promised by "your manager" by phone on 24 Nov. No such statement by a named person is on the ticket, and the account record shows Credits: None, Refunds: None. Not a commitment. Policy 6.2 forbids agents promising it; 6.3 limits offers to Bianca Torres or the Head of Customer Support, in writing on the ticket or account.

## 4. Service-level status and deadline
- Tier: Premier (account record). Priority P2, recorded at creation. Policy 3.1: Premier P2, first response "2 business hours", resolution "18 business hours". Business hours 08:30 to 17:30 AWST Mon to Fri = 00:30 to 09:30 UTC (1.1, 1.2).
- First response: met. Ticket created 23 Nov 23:40 UTC (07:40 AWST Tue), outside business hours, so counting starts 24 Nov 00:30 UTC (4.1). Sam replied 00:52 UTC, 22 minutes in.
- Resolution clock: starts 24 Nov 00:30 UTC. Paused only while Pending customer (4.2): 24 Nov 03:00 to 04:30 UTC = 1.5 h, all inside business hours.
  - 24 Nov: 00:30 to 09:30 = 9.0 h, minus 1.5 h = 7.5 h.
  - 25 Nov: 00:30 to 02:10 = 1 h 40 min.
  - Used 9 h 10 min; remaining 8 h 50 min.
- Deadline: 7 h 20 min left on 25 Nov (to 09:30 UTC), then 1 h 30 min on 26 Nov: **02:00 UTC Thu 26 Nov = 10:00 AWST Thu 26 Nov**, assuming no further pause and no WA public holiday on 25 or 26 Nov (not checked against a holiday list).
- Status: within target. At risk (4.4) when under 4.5 h remains, i.e. 13.5 h used, at about 06:30 UTC 25 Nov (14:30 AWST).
- Resolution needs every fault on the ticket resolved (1.5). The login fault is fixed, but the ticket is not resolvable until reports are fixed.
- P2 update rule (7.1): at least once each business day; met on 24 and 25 Nov.

## 5. Recommended next action (support's judgement, not a commitment)
1. Tier 2 engineer to find why a regenerated report omits readings that are present, starting with the report window or time basis and whether it uses reading time or ingestion time for G4-C stores, comparing a G4-E store and checking the 24 Nov night. Send the customer the 15:00 AWST update (07:00 UTC) today, which Sam promised, saying what has been checked even if no cause is found.
2. Alternative: while the cause is open, offer the customer an export of the raw 01:00 to 05:00 readings for stores 07 and 11 for 21 to 24 Nov from the data explorer, as evidence for their fridge records. Reason: the data is verified present and the customer's need is proof of readings. Do not promise a fix date.
3. Alternative: if no cause by about 06:30 UTC (at-risk point), tell the Support Team Lead (5.2 strictly applies at escalation, but the ticket reaches at-risk hours later).
Owner: Tier 2 engineer. Do not mark resolved or close the escalation, despite the customer's request in her 25 Nov message. The fault is not fixed. Refund: leave to Bianca Torres.

## 6. Open questions
- Why does regeneration still exclude the readings?
- Did the 24 Nov night gap occur (customer claim)? Does it also affect other nights for these stores?
- Did a phone call on 24 Nov take place, and did anyone offer a refund? Ask Bianca Torres and check call records; the record shows nothing.
- Has Bianca received the refund request?
- Are 25 and 26 Nov WA public holidays? Check.
- Conflict: the customer says a manager promised a refund; the thread and account record show no offer.
