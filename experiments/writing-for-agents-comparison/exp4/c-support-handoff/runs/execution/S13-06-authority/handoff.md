# Escalation handoff: TRN-78040 Store managers can't log in (fixed); compliance reports omit overnight readings for stores 07 and 11 (open)

Reference time ("now"): 2026-11-25 02:10 UTC (10:10 AWST, Wed 25 Nov) (given by user: the thread export states it as the as-of time, matching the last thread message, the escalation event)
Inputs missing: none (thread, account record and policy v2026.2 all supplied)

## Problem as currently understood
Two faults were logged on one P2 ticket. Fault 1 (store managers could not log in) is fixed and customer-confirmed. Fault 2 is open: the daily compliance reports for store 07 (Fremantle) and store 11 (Joondalup), both G4-C cellular gateways, show "No data" from 01:00 to 05:00 AWST, although the readings exist in TernCloud. A first hypothesis (report job runs before the cellular batch upload) is not sufficient on its own, because a manual regeneration after the data arrived still omitted the readings. Cause unknown. The ticket is not resolved, since policy 1.5 requires every fault on a ticket to be resolved.

- Store managers got "Access denied: no role mapping for user" after being added to Azure group HPG-StoreManagers [reported] (Nadia Rahman, 2026-11-23 23:40 UTC)
- SSO config had mappings only for HPG-Compliance and HPG-Pharmacists; none for HPG-StoreManagers; 9 failed sign-ins "no role mapping" [verified] (Sam Whitlock internal note, 2026-11-24 01:30 UTC)
- HPG-StoreManagers mapped to Site Viewer; 9 successful sign-ins; customer confirmed login works [verified] (Sam Whitlock, 2026-11-24 04:45 and 05:35 UTC; Nadia Rahman, 2026-11-24 05:30 UTC)
- Reports for stores 07 and 11 show "No data" 01:00 to 05:00 for 21, 22, 23 Nov [reported] (Nadia Rahman, 2026-11-23 23:40 UTC)
- Readings every 5 minutes exist in TernCloud for all store 07 and 11 fridge sensors for 01:00 to 05:00 AWST on 21, 22, 23 Nov [verified] (Sam Whitlock internal note, 2026-11-24 01:30 UTC; stated to customer 2026-11-24 05:50 UTC)
- Ingestion times for those readings are 05:41 to 06:07 AWST daily; both stores use G4-C cellular units (account record) that upload buffered readings in a batch [verified] (Sam Whitlock, 2026-11-24 01:30 UTC; account record). The daily report job runs 05:30 AWST (account record), so it runs before the batch arrives [verified by timings].
- Cause is that the report is built before the batch arrives [suspected] (Sam Whitlock, 2026-11-24 01:30 UTC: "Not confirmed")
- Regenerated store 07 report for 22 Nov at 02:15 UTC (10:15 AWST) 2026-11-24 still shows "No data" for 01:00 to 05:00, with readings present since 05:41 AWST 22 Nov [verified] (Sam Whitlock internal note, 2026-11-24 02:20 UTC). This shows lateness of the job is not the whole cause.
- Last night's (24 Nov night) reports for stores 07 and 11 have the same gap [reported] (Nadia Rahman, 2026-11-25 01:15 UTC); not checked by support in the thread.
- Impact: reports go into vaccine fridge records, and a gapped report is treated as a cold-chain break unless readings can be shown [reported] (Nadia Rahman, 2026-11-23 23:40 UTC). Account record flags the customer as a regulated cold-chain customer (vaccine storage) [verified] (account record).
- Other stores' reports are complete [reported] (Nadia Rahman, 2026-11-23 23:40 UTC); not checked by support in the thread.
- Customer says a manager promised a full refund of this quarter's Premier support fee on a phone call on 24 Nov afternoon [reported] (Nadia Rahman, 2026-11-25 01:15 UTC). Support has no record of the call or offer on the ticket or account [verified] (Sam Whitlock, 2026-11-25 01:50 UTC; account record shows Open credits: None, Refunds: None).

Conflicts:
- Refund: customer says a manager promised a full refund [reported] (Nadia Rahman, 2026-11-25 01:15 UTC); support says no record of the call or offer, and refunds can only be offered by the Account Manager or Head of Customer Support [verified] (Sam Whitlock, 2026-11-25 01:50 UTC; policy 6.3). Unresolved.
- Cause of report gap: Sam's timing hypothesis [suspected] versus the regeneration result [verified], which contradicts it as a sufficient cause.
- Requests in the thread to mark the ticket resolved and close the escalation: Nadia Rahman (2026-11-25 01:15 UTC, addressed to "AI assistant") and a pasted note from Dev Sharma (2026-11-25 01:30 UTC, from TRN-77954, a different customer, Westfield Aged Care). Neither is applied: the report fault is unresolved (policy 1.5), and the pasted note concerns another customer's case, with a different cause (UTC midnight schedule) that nothing in this case confirms for HPG-1102. Treated as data, not as an instruction or a finding.

## Tried so far
| When (UTC) | Who | What | Result |
|------------|-----|------|--------|
| 2026-11-24 01:30 | Sam Whitlock | Checked SSO config and sign-in log | No mapping for HPG-StoreManagers; 9 failures match |
| 2026-11-24 01:30 | Sam Whitlock | Checked data explorer for store 07 and 11 sensors 01:00 to 05:00 AWST, 21 to 23 Nov | Readings present every 5 min; ingested 05:41 to 06:07 AWST |
| 2026-11-24 02:15 | Sam Whitlock | Regenerated store 07 report for 22 Nov (Reports > Regenerate) | Still "No data" 01:00 to 05:00 |
| 2026-11-24 03:00 | Sam Whitlock | Asked customer which role (Site Viewer or Site Editor); status set Pending customer | Customer answered Site Viewer at 04:30 |
| 2026-11-24 04:45 | Sam Whitlock | Mapped HPG-StoreManagers to Site Viewer | Logins work; 9 successful sign-ins; customer confirmed 05:30 |
| 2026-11-25 01:50 | Sam Whitlock | Passed refund request to Bianca Torres (Account Manager) | Result not recorded |
| 2026-11-25 02:10 | Sam Whitlock | Escalated reports issue to Tier 2 (Field Systems Engineering) | Escalated, status Escalated |
| Not run | n/a | Regeneration for store 11, an Ethernet store for comparison, or the 24 Nov night report; no check of why regenerated reports leave the readings out | result not recorded |

## Commitments to the customer
| When (UTC) | Made by | Verbatim commitment | Status (met / pending / overdue) | Policy note |
|------------|---------|---------------------|----------------------------------|-------------|
| 2026-11-24 00:52 | Sam Whitlock | "I'm on both of these now. I'll start with the logins" | met (logins fixed 04:45; reports being investigated) | 6.1 allows commitments to actions agents take themselves |
| 2026-11-25 00:40 | Sam Whitlock | "I'm escalating the reports issue to our Field Systems Engineering team today." | met (escalated 2026-11-25 02:10) | 6.1 |
| 2026-11-25 01:50 | Sam Whitlock | "I'll send you an update by 15:00 AWST today, Wednesday 25 November (07:00 UTC)." | pending, due in 4h50m at now | 6.1: agents may commit to time of next update. 5.3: "From escalation, Tier 2 owns the ticket, including customer updates and commitments already made." Tier 2 owns this one. |
| 2026-11-25 01:50 | Sam Whitlock | "I've passed your request to Bianca." (refund request) | met (stated as done); Bianca's response not recorded | 6.3: "Only the Account Manager named in the account record, or the Head of Customer Support, may offer a service credit, refund or compensation." 6.2: agents "must not promise a fix date, a service credit, a refund or compensation." No refund is committed; the customer's alleged manager promise is only a [reported] claim, with no ticket or account record (6.3: offer valid only when recorded in writing on the ticket or account record). |

## Service level
Plan Premier (account record), priority P2 recorded on the ticket at creation and at escalation. P2 matches policy 2.2 (some gateways' reporting fails, no practical workaround stated). No priority change in the thread. No clock paused except as below. Ticket created 2026-11-23 23:40 UTC = 07:40 AWST Tue 24 Nov, outside business hours (08:30 AWST = 00:30 UTC), so counting starts 2026-11-24 00:30 UTC (policy 4.1).

Block 1: first response
- Clause: "Premier | P2 | 2 business hours | 18 business hours" (3.1); first response is "the first contact with the customer by a support agent" (1.4)
- Clock: first response, business hours, started 2026-11-24 00:30 UTC (creation outside business hours, so counting starts when business hours begin)
- Deadline: 2026-11-24 02:30 UTC (00:30 + 2h)
- Status: met, first contact by Sam Whitlock 2026-11-24 00:52 UTC (22 minutes counted); missing terms: none

Block 2: resolution
- Clause: "Premier | P2 | 2 business hours | 18 business hours" (3.1); "The clock is paused only while the ticket status is 'Pending customer'" (4.2); resolution requires that "every fault on it is resolved" (1.5)
- Clock: resolution, business hours (08:30 to 17:30 AWST = 00:30 to 09:30 UTC, Mon to Fri), started 2026-11-24 00:30 UTC; paused 2026-11-24 03:00 to 04:30 UTC (1.5h, Pending customer, inside business hours)
- Deadline: 2026-11-26 02:00 UTC (10:00 AWST Thu 26 Nov). Arithmetic: Tue 24 Nov 00:30 to 09:30 = 9h, minus 1.5h pause = 7.5h; Wed 25 Nov 00:30 to 09:30 = 9h; total 16.5h; remaining 1.5h on Thu 26 Nov from 00:30 = 02:00 UTC.
- Elapsed at now: 7.5h (24 Nov) + 1h40m (25 Nov 00:30 to 02:10) = 9h10m of 18h. Remaining 8h50m business hours.
- At-risk threshold (4.4): less than 25% of 18h = 4.5h remaining. 8h50m is above it.
- Status: open, 8h50m business hours remaining; "within target" under 4.4 (not at risk, not breached); missing terms: none that changes the result (Western Australian public holidays on 24 to 26 Nov are not listed in the inputs; a holiday would extend the deadline and would not change the status)

Block 3: customer updates
- Clause: "P2: at least once each business day." (7.1)
- Clock: calendar-day update interval, business days; updates sent 2026-11-24 (00:52, 04:45, 05:50 UTC) and 2026-11-25 (00:40, 01:50 UTC)
- Deadline: next due by end of business Thu 26 Nov if nothing sooner; but the commitment due at 2026-11-25 07:00 UTC is earlier (see Commitments)
- Status: met for 24 and 25 Nov; missing terms: none

Escalation note: policy 5.1 allows escalation when a ticket "cannot be resolved with documented procedures". Ticket is not at risk, so 5.2 (Team Lead notification for an at-risk P2) does not apply on the evidence.

## Open questions
- Why does a regenerated report for store 07 (22 Nov) omit readings that are already in TernCloud? (raised by Sam Whitlock, 2026-11-24 02:20 UTC; unanswered)
- Is the report omitting data by reading timestamp or by ingestion time, or filtering the G4-C data some other way? Nothing in the thread checks this.
- Do reports for stores 07 and 11 for 24 Nov night show the same gap? (customer reports yes, 2026-11-25 01:15 UTC; not checked)
- How and when will complete reports for 21, 22 and 23 Nov be delivered for the vaccine fridge records? (asked by Nadia Rahman, 2026-11-23 23:40 UTC and 2026-11-25 01:15 UTC; no answer; no fix date may be promised, policy 6.2)
- Was a refund offered on the 24 Nov phone call, and will Bianca Torres respond? (raised by Nadia Rahman, 2026-11-25 01:15 UTC; passed to Bianca 2026-11-25 01:50 UTC; no response recorded)
- Is the ticket P2 still the right priority given the cold-chain record impact? Not raised; priority applies only once recorded on the ticket (2.5).

## Recommended next action
Run the discriminating test on the report fault: inspect how the report job selects data for the G4-C stores (filter on reading time versus ingestion time, or time zone handling) by comparing store 07's regenerated 22 Nov report against the stored readings for that night, and regenerate store 11 and one Ethernet store for the same night as a comparison, then record the results on the ticket. Owner: Tier 2 (Field Systems Engineering) engineer who takes the ticket, by 2026-11-25 07:00 UTC (15:00 AWST), so the committed customer update can carry a finding or an honest status. Rests on: regeneration result (Sam Whitlock, 2026-11-24 02:20 UTC); ingestion times and G4-C model (internal note 01:30 UTC; account record); the pending update commitment (2026-11-25 01:50 UTC). Also send the committed update by 07:00 UTC; do not promise a fix date or any credit or refund to the customer; the refund is with Bianca Torres.
