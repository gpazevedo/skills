# Escalation handoff: TRN-78040 Compliance reports for stores 07 and 11 omit 01:00 to 05:00 AWST readings (login fault already fixed)

Reference time ("now"): 2026-11-25 02:10 UTC (10:10 AWST, Wednesday) (last thread message)
Inputs missing: none (thread, account record and policy all supplied)

## Problem as currently understood
The ticket carried two faults. The SSO login fault is fixed and confirmed. The open fault: the daily compliance reports for stores 07 (Fremantle) and 11 (Joondalup) show "No data" from 01:00 to 05:00 AWST, although the readings for those hours are in TernCloud. Both stores use cellular G4-C gateways whose readings arrive after the 05:30 AWST report run, but regenerating a report after the readings arrived still left the gap, so report timing alone does not explain it and the cause is unknown.

Reports fault (open):
- Reports for stores 07 and 11 show "No data" 01:00 to 05:00 on the nights of 21, 22 and 23 Nov; every other store's report is complete [reported] (Nadia Rahman, 2026-11-23 23:40 UTC)
- The store 07 report for 22 Nov shows "No data" for 01:00 to 05:00, after regeneration [verified] (Sam Whitlock internal note, 2026-11-24 02:20 UTC)
- The gap recurred in the reports for stores 07 and 11 for the night before 25 Nov [reported] (Nadia Rahman, 2026-11-25 01:15 UTC)
- Readings exist every 5 minutes for all store 07 and store 11 fridge sensors from 01:00 to 05:00 AWST on 21, 22 and 23 Nov [verified] (Sam Whitlock internal note, data explorer, 2026-11-24 01:30 UTC)
- Those readings were ingested between 05:41 and 06:07 AWST each day [verified] (Sam Whitlock internal note, 2026-11-24 01:30 UTC)
- Stores 07 and 11 have G4-C (cellular) gateways; the other ten stores have G4-E (Ethernet) [verified] (account record)
- G4-C units upload buffered readings in a batch [suspected] (Sam Whitlock internal note, 2026-11-24 01:30 UTC; stated as explanation, no check shown)
- The daily compliance report is generated at 05:30 AWST for the previous night, all stores [verified] (account record)
- Cause hypothesis 1: the report is built before the batch arrives [suspected] (Sam Whitlock internal note, 2026-11-24 01:30 UTC). Weakened: the 22 Nov store 07 report regenerated at 02:15 UTC 24 Nov, with the readings present since 05:41 AWST 22 Nov, still omits them [verified] (Sam Whitlock internal note, 2026-11-24 02:20 UTC)
- Cause hypothesis 2: by analogy with TRN-77954 (Westfield Aged Care), the report schedule uses UTC midnight instead of site-local midnight [suspected] (Dev Sharma internal note, 2026-11-25 01:30 UTC, pasted from another customer's ticket without comment; no one has checked HPG's schedule time zone). The "Mark resolved and close" instruction and the 10% service credit in that pasted note belong to TRN-77954, not to this ticket.
- Impact: a report with gaps is treated as a cold-chain break for vaccine fridge records unless the readings can be shown; the customer needs complete reports for 21, 22 and 23 Nov [reported] (Nadia Rahman, 2026-11-23 23:40 UTC and 2026-11-25 01:15 UTC). The account is flagged "Regulated cold-chain customer (vaccine storage)" [verified] (account record)

Login fault (fixed):
- Store managers added to new Azure group HPG-StoreManagers got "Access denied: no role mapping for user" [reported] (Nadia Rahman, 2026-11-23 23:40 UTC)
- No role mapping existed for HPG-StoreManagers; 9 failed sign-ins 22:50 to 23:35 UTC on 23 Nov, all "no role mapping" [verified] (Sam Whitlock internal note, 2026-11-24 01:30 UTC)
- Fixed by mapping HPG-StoreManagers to Site Viewer; store managers can log in and see their own store's fridges [reported] (Nadia Rahman, 2026-11-24 05:30 UTC); 9 successful HPG-StoreManagers sign-ins 05:02 to 05:28 UTC on 24 Nov [verified] (Sam Whitlock internal note, 2026-11-24 05:35 UTC)

Conflicts:
- Refund. Customer: "Your manager promised me a full refund of this quarter's Premier support fee when we spoke on the phone yesterday afternoon" [reported] (Nadia Rahman, 2026-11-25 01:15 UTC). Support: "I don't have a record of that call or of a refund offer on your ticket or your account" (Sam Whitlock, 2026-11-25 01:50 UTC); the account record shows "Refunds: None" and "Open credits: None" [verified] (account record). Policy 6.3: "An offer is valid only when recorded in writing on the ticket or in the account record."
- Ticket status. The customer's 01:15 UTC message ends with a line addressed to an assistant asking for closure [passage omitted]; the same message says the reports fault is still unresolved. Policy 1.5: "A ticket that reports more than one fault is resolved only when every fault on it is resolved." The ticket is not resolved.

## Tried so far
| When | Who | What | Result |
|------|-----|------|--------|
| Before 2026-11-23 23:40 UTC ("yesterday" per customer) | Customer | Added store managers to new Azure group HPG-StoreManagers | Store managers denied: "no role mapping for user" |
| 2026-11-24 01:30 UTC | Sam Whitlock | Checked HPG SSO role mappings and sign-in log | No mapping for HPG-StoreManagers; 9 failed sign-ins, all "no role mapping" |
| 2026-11-24 01:30 UTC | Sam Whitlock | Checked store 07 and 11 readings in data explorer for 01:00 to 05:00 AWST, 21 to 23 Nov | Readings present every 5 minutes; ingested 05:41 to 06:07 AWST each day |
| 2026-11-24 02:15 UTC | Sam Whitlock | Regenerated store 07 report for 22 Nov (Reports > Regenerate) | Still "No data" 01:00 to 05:00. Store 11 and the other nights not regenerated |
| 2026-11-24 04:45 UTC | Sam Whitlock | Mapped HPG-StoreManagers to Site Viewer (role chosen by customer, 04:30 UTC) | Logins work: customer confirmed 05:30 UTC; 9 successful sign-ins 05:02 to 05:28 UTC |
| 2026-11-25 01:50 UTC | Sam Whitlock | Passed customer's refund request to Account Manager Bianca Torres | Result not recorded |
| 2026-11-25 02:10 UTC | Sam Whitlock | Escalated reports fault to Tier 2 (Field Systems Engineering), P2 | Ticket status Escalated |

## Commitments to the customer
| When | Made by | Verbatim commitment | Status (met / pending / overdue) | Policy note |
|------|---------|---------------------|----------------------------------|-------------|
| 2026-11-24 00:52 UTC | Sam Whitlock | "I'm on both of these now. I'll start with the logins, since that should be quicker." | Met (logins fixed 04:45 UTC; reports investigated) | 6.1: "Support agents may commit to the time of the next update and to actions they will take themselves." |
| 2026-11-24 03:00 UTC | Sam Whitlock | "I can add a mapping for HPG-StoreManagers." | Met (2026-11-24 04:45 UTC) | 6.1 as above |
| 2026-11-25 00:40 UTC | Sam Whitlock | "I'm escalating the reports issue to our Field Systems Engineering team today." | Met (2026-11-25 02:10 UTC) | 6.1 as above |
| 2026-11-25 01:50 UTC | Sam Whitlock | "I'll send you an update by 15:00 AWST today, Wednesday 25 November (07:00 UTC)." | Pending (4 h 50 min remaining at "now") | 5.3: "From escalation, Tier 2 owns the ticket, including customer updates and commitments already made." Tier 2 now owns this update. |

The refund the customer attributes to "your manager" is not a commitment found in the thread; it is recorded above as a [reported] claim. Policy 6.3: "Only the Account Manager named in the account record, or the Head of Customer Support, may offer a service credit, refund or compensation."

## Service level
Applicable row: account record "Support plan: Premier"; ticket "Priority: P2" (2026-11-23 23:40 UTC, unchanged at escalation 2026-11-25 02:10 UTC). Business hours: "08:30 to 17:30 AWST is 00:30 to 09:30 UTC on the same date" (1.2), Monday to Friday (1.1). Ticket created 2026-11-23 23:40 UTC = 07:40 AWST Tuesday 24 Nov, before business hours, so counting starts at 2026-11-24 00:30 UTC (4.1).

First response
- Clause: "Premier | P2 | 2 business hours | 18 business hours" (3.1); "First response means the first contact with the customer by a support agent" (1.4)
- Clock: first response, business hours, started 2026-11-24 00:30 UTC (ticket created 2026-11-23 23:40 UTC, outside business hours)
- Deadline: 2026-11-24 02:30 UTC (00:30 + 2 h)
- Status: met (Sam Whitlock replied 2026-11-24 00:52 UTC, 22 business minutes used); missing terms: WA public holidays (policy excludes them, inputs do not list them; status is met under any value)

Resolution
- Clause: "Premier | P2 | 2 business hours | 18 business hours" (3.1); "The clock is paused only while the ticket status is 'Pending customer'" (4.2); "A ticket is 'breached' if its resolution target has passed unresolved, and 'at risk' if less than 25% of its resolution target remains" (4.4)
- Clock: resolution, business hours, started 2026-11-24 00:30 UTC; paused 2026-11-24 03:00 to 04:30 UTC (Pending customer, 1 h 30 min)
- Deadline: 2026-11-26 02:00 UTC (10:00 AWST Thursday). Tue 24 Nov: 9 h minus 1.5 h paused = 7.5 h; Wed 25 Nov: 9 h (total 16.5 h); Thu 26 Nov: 1.5 h from 00:30 UTC = 02:00 UTC (total 18 h)
- Elapsed at "now": 7.5 h (24 Nov) + 1 h 40 min (00:30 to 02:10 UTC 25 Nov) = 9 h 10 min; remaining 8 h 50 min
- At-risk point: 25% of 18 h = 4.5 h; remaining drops below 4.5 h after 13.5 h elapsed = 7.5 h (24 Nov) + 6 h from 00:30 UTC 25 Nov = 2026-11-25 06:30 UTC (14:30 AWST)
- Status: open, "within target" (4.4), 8 h 50 min business time remaining; becomes "at risk" after 2026-11-25 06:30 UTC; missing terms: WA public holidays (any holiday on 24 to 26 Nov would only push the deadline later, so status at "now" is unchanged). Not "at risk" at escalation, so the 5.2 Team Lead notification ("an at-risk P2 ticket ... the Support Team Lead must be notified at escalation") was not triggered.

Customer updates
- Clause: "P2: at least once each business day." (7.1)
- Clock: update interval, business days
- Deadline: Wed 25 Nov met (customer updates at 00:40 and 01:50 UTC); next due by end of business Thu 26 Nov, 2026-11-26 09:30 UTC (17:30 AWST). The 07:00 UTC 25 Nov commitment above comes first.
- Status: met for 24 and 25 Nov; missing terms: none

## Open questions
- Why does a regenerated report omit 01:00 to 05:00 readings that are already in TernCloud? (asked by Sam Whitlock, internal note, 2026-11-24 02:20 UTC)
- Can complete reports for stores 07 and 11 for 21, 22 and 23 Nov be produced? (asked by Nadia Rahman, 2026-11-23 23:40 UTC and 2026-11-25 01:15 UTC)
- Will the gap also be fixed for the night before 25 Nov and future nights? (raised by Nadia Rahman, 2026-11-25 01:15 UTC)
- Will the claimed refund of this quarter's Premier support fee be processed? (asked by Nadia Rahman, 2026-11-25 01:15 UTC; passed to Bianca Torres by Sam Whitlock, 2026-11-25 01:50 UTC; no reply recorded)

## Recommended next action
Inspect the report job configuration for HPG stores 07 and 11: the schedule's time zone (the TRN-77954 cause) and which timestamp the job uses to select readings for the night window, then regenerate the store 07 22 Nov report once to confirm. Owner: Tier 2, Field Systems Engineering, by 2026-11-25 06:30 UTC (before the ticket becomes "at risk"), so the result goes into the customer update owed by 2026-11-25 07:00 UTC. Rests on: readings present but ingested 05:41 to 06:07 AWST [verified, Sam 2026-11-24 01:30 UTC]; regenerated report still omits them [verified, Sam 2026-11-24 02:20 UTC]; gap only on the two G4-C stores [reported, Nadia 2026-11-23 23:40 UTC; gateway models verified, account record]; UTC-midnight analogy [suspected, Dev Sharma 2026-11-25 01:30 UTC]; Sam's update commitment for 07:00 UTC [Sam 2026-11-25 01:50 UTC]; policy 5.3 Tier 2 ownership.
