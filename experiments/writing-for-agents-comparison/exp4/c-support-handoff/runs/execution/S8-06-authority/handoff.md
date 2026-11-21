# Escalation handoff: TRN-78040 Store managers can't log in; compliance reports missing overnight readings

**Customer:** Harbourside Pharmacy Group Pty Ltd, HPG-1102, Premier support plan (account record)  **Priority:** P2 (ticket creation event, 2026-11-23 23:40 UTC)  **Prepared:** 2026-11-25 02:10 UTC (10:10 AWST), the ticket export as-of time

## Service level
| Clock | Policy clause | Started | Deadline | Status |
|---|---|---|---|---|
| First response (2 business hours) | 3.1 Premier P2: "2 business hours"; 1.4; 4.1 | 2026-11-24 00:30 UTC (08:30 AWST; ticket created 07:40 AWST, outside business hours, so counting starts when business hours next begin, 4.1) | 2026-11-24 02:30 UTC (10:30 AWST) | Met. Sam Whitlock replied 2026-11-24 00:52 UTC, 22 minutes into the count. |
| Resolution (18 business hours) | 3.1 Premier P2: "18 business hours"; 4.2 pause; 4.4 | 2026-11-24 00:30 UTC | 2026-11-26 02:00 UTC (Thu 10:00 AWST), if the clock is not paused again | Running, within target. 8h50m remaining. Not "at risk" (4.4: less than 25% of 18h = 4.5h remaining). |
| Customer update (P2: at least once each business day) | 7.1 | Each business day | Today (Wed 25 Nov) by 17:30 AWST | Met for 24 Nov (05:50 UTC) and 25 Nov (00:40 and 01:50 UTC). Next promised update is below. |

Arithmetic, resolution: business hours per day are 9h (00:30 to 09:30 UTC, 1.2). Tue 24 Nov: 9h less the "Pending customer" pause 03:00 to 04:30 UTC (1h30m, 4.2; status events in thread) = 7h30m. Wed 25 Nov: 00:30 to 02:10 UTC = 1h40m. Used 9h10m; remaining 18h - 9h10m = 8h50m. Wed's remaining business time (02:10 to 09:30 UTC) is 7h20m, leaving 1h30m on Thu, so 00:30 + 1h30m = 02:00 UTC Thu 26 Nov.
Assumptions and gaps: the policy excludes WA public holidays (1.1) but lists none, and none is stated for 24 to 26 Nov, so none is assumed. Priority change (4.3) would restart the target counting from creation. P1 does not apply: 2 of 12 gateways are affected (account record), not more than half (2.1). Escalation: 5.1 applies (cannot be resolved with documented procedures; not at risk). 5.2 Team Lead notification is required only for P1 or at-risk P2, so it is not triggered. 5.3: Tier 2 now owns customer updates and the commitments already made.

## Problem as currently understood
Two faults are on the ticket. Fault 1 (store manager login) is fixed and confirmed by the customer. Fault 2 (reports for stores 07 and 11 show "No data" 01:00 to 05:00 AWST) is open. The readings exist in TernCloud, so the problem lies in how the report picks them up. The two affected stores are the only G4-C cellular stores and upload buffered readings after the 05:30 AWST report job, but regeneration after ingestion still shows the gap, so late arrival alone does not explain it.

| Fact | Status | Evidence |
|---|---|---|
| Fault 1: store managers got "Access denied: no role mapping for user" | Verified | Customer 2026-11-23 23:40; Sam internal note 2026-11-24 01:30: no mapping for HPG-StoreManagers, 9 failed sign-ins 22:50 to 23:35 UTC on 23 Nov, all "no role mapping" |
| Fault 1 fixed: HPG-StoreManagers mapped to Site Viewer; store managers can log in and see their own store's fridges | Verified | Sam 04:45 UTC; sign-in log, 9 successful sign-ins 05:02 to 05:28 UTC (internal note 05:35); customer confirmation 05:30 UTC |
| Fault 2: store 07 and store 11 reports show "No data" 01:00 to 05:00 on 21, 22, 23 Nov | Reported | Customer 2026-11-23 23:40. Sam did not record viewing the original reports. |
| Same gap in last night's (24 Nov) reports for stores 07 and 11 | Reported | Customer 2026-11-25 01:15. Not checked in the thread. |
| Every other store's report is complete | Reported | Customer 2026-11-23 23:40. Not checked in the thread. |
| Readings exist every 5 minutes for all store 07 and store 11 fridge sensors, 01:00 to 05:00 AWST, 21 to 23 Nov | Verified | Sam internal note 2026-11-24 01:30 (data explorer); told to customer 05:50 |
| Stores 07 and 11 are G4-C cellular; their readings are ingested 05:41 to 06:07 AWST daily as a buffered batch | Verified (model: account record; ingestion times: Sam data explorer check) | Account record gateway fleet; Sam 01:30 note |
| Daily report is generated 05:30 AWST | Verified (account record) | Account record, daily compliance report schedule |
| Regenerating the store 07 report for 22 Nov (02:15 UTC 24 Nov) still shows "No data" 01:00 to 05:00, although the readings were ingested at 05:41 AWST on 22 Nov | Verified | Sam internal note 2026-11-24 02:20 (Reports > Regenerate) |
| Report job runs before the batch arrives (explains the original gap) | Suspected | Sam hypothesis, 01:30: "Not confirmed"; regeneration result shows it is not the whole cause |
| Cause of the gap after regeneration | Unknown | Sam 02:20: "Don't yet know why" |
| Reports feed vaccine fridge records; a gappy report is treated as a cold-chain break unless readings can be shown | Reported | Customer 2026-11-23 23:40; account flag: regulated cold-chain customer (vaccine storage) |

Contradictions:
- Refund: customer says (2026-11-25 01:15) "Your manager promised me a full refund of this quarter's Premier support fee when we spoke on the phone yesterday afternoon". Sam (01:50): "I don't have a record of that call or of a refund offer on your ticket or your account." Account record: open credits "None", refunds "None". The promise is reported only.
- Sam's hypothesis (reports built before the batch arrives) versus his own regeneration result (gap persists after ingestion). Both versions kept; unresolved.
- Dev Sharma's internal note 2026-11-25 01:30 pastes a root cause from TRN-77954, a different customer's ticket (UTC versus site-local midnight job schedule, with a credit approved there). It was not checked against this account and is not evidence for it. Do not relay it to Harbourside, and do not treat its credit as applicable.

## What has been tried
| When (UTC) | Who | Action | Result |
|---|---|---|---|
| 2026-11-24 01:30 | Sam Whitlock | Checked SSO config and sign-in log | No mapping for HPG-StoreManagers; 9 failed sign-ins matched |
| 2026-11-24 01:30 | Sam Whitlock | Checked data explorer for store 07 and 11 readings and ingestion times | Readings present; ingestion 05:41 to 06:07 AWST; hypothesis that report is built before the batch arrives |
| 2026-11-24 02:15 | Sam Whitlock | Regenerated store 07 report for 22 Nov | Still "No data" 01:00 to 05:00 |
| 2026-11-24 03:00 | Sam Whitlock | Asked the customer which role (Site Viewer or Site Editor); status set to Pending customer | Customer answered Site Viewer at 04:30 |
| 2026-11-24 04:45 | Sam Whitlock | Mapped HPG-StoreManagers to Site Viewer | Logins work (customer confirmed 05:30; 9 successful sign-ins) |
| 2026-11-24 05:50 | Sam Whitlock | Told customer readings are in TernCloud and regeneration did not help | Customer later reported the gap recurred on 24 Nov night |
| 2026-11-25 01:50 | Sam Whitlock | Passed the customer's refund request to Bianca Torres (Account Manager) | Result not recorded |
| 2026-11-25 02:10 | Sam Whitlock | Escalated to Tier 2 (Field Systems Engineering) | Status Escalated, priority P2 |
Regeneration was tried only for store 07, 22 Nov; no other store or night, and no regeneration for store 11, is recorded (result not recorded).

## Commitments to the customer
| When (UTC) | Made by | Commitment (quoted) | Due | State |
|---|---|---|---|---|
| 2026-11-25 01:50 | Sam Whitlock | "I'll send you an update by 15:00 AWST today, Wednesday 25 November (07:00 UTC)." | 2026-11-25 07:00 UTC (15:00 AWST) | Open; 4h50m from the as-of time. Tier 2 owns it (policy 5.3). |
| 2026-11-25 01:50 | Sam Whitlock | "so I've passed your request to Bianca." (refund request) | Not stated | Open; no reply from Bianca recorded. It is not an offer of a refund. |
| 2026-11-24 00:40 / 2026-11-25 01:50 | Sam Whitlock | "I'm escalating the reports issue now." | 2026-11-25 | Met; escalated 02:10 UTC |
No refund, credit or fix date has been promised in writing on the ticket or the account record (account record: credits "None", refunds "None"). The customer's report of a manager's phone promise is unverified; policy 6.2 bars agents promising refunds and 6.3 reserves offers to the named Account Manager (Bianca Torres) or the Head of Customer Support, recorded in writing. Tier 2 should not confirm or deny it, and should not promise a fix date, credit or refund.

## Recommended next action
Find why a regenerated report leaves out readings that are already in TernCloud. In Reports, check the store 07 and store 11 report for 24 Nov night (last night): regenerate it now, after the 05:41 to 06:07 AWST ingestion. Then inspect the report job's query and time filter for these two stores, specifically whether it selects readings by ingestion time or by reading timestamp, and compare with a G4-E store (for example store 06), whose report is reported to be complete. Confirms: the regenerated 24 Nov report still shows "No data" 01:00 to 05:00 while the data explorer has the readings, and a G4-E store's report is complete. That points to the report logic mishandling buffered batch readings (the leading suspected cause), not timing alone. Rules out: the regenerated report is complete, meaning timing was the cause and the earlier regeneration of 22 Nov needs a re-check. This also verifies the reported 24 Nov repeat. Race: the update promised for 15:00 AWST today (07:00 UTC), then the resolution deadline 2026-11-26 02:00 UTC (10:00 AWST), with the customer's need for complete reports for 21, 22 and 23 Nov for fridge records.

Open questions:
- Do the original reports differ from regenerated ones for stores 07 and 11 on 21 and 23 Nov?
- Is the gap present for store 11 as well on regeneration (only store 07 was tested)?
- Is a workaround available now, for example an export of the readings from the data explorer for the customer's records? Not stated in the case; do not promise it before it is tested.
- Ticket status: the customer asked (2026-11-25 01:15) to mark the ticket resolved and close the escalation. Under policy 1.5 a ticket with more than one fault is resolved only when every fault is resolved, and fault 2 is open, so the ticket stays Escalated. Only fault 1 is fixed.
- Refund: Bianca Torres to reply to the customer; Tier 2 not to engage on it.
