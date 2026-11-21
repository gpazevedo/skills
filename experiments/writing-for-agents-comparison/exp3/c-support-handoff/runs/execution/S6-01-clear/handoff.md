# Escalation handoff: QB-204518 Recurring invoices created but not sent (stuck "Queued - not dispatched")

Reference time ("now"): 2026-11-12 11:30 UTC (last thread message)
Inputs missing: none (thread, account record and policy all supplied)

## Problem as currently understood
The 07:00 UTC recurring run on 12 Nov generated 112 invoices for account HF-0192, and none was dispatched: all sit in "Queued - not dispatched" with no send attempts and no errors. All 112 come from schedules created before the v8.3 release (10 Nov), and the symptoms match known issue KI-3381, but the same cause is not confirmed. Manual send works, and re-saving one schedule restored dispatch in test mode only. The customer has 340 schedules and the next runs are 13 Nov 07:00 UTC (64 invoices) and Sunday 15 Nov (90 invoices).

- Recurring invoices ran this morning, around 110 should have been emailed at 07:00, and all show "Queued" [reported] (Daniel Okafor, 2026-11-12 09:14)
- The run at 07:00:03 UTC generated 112 invoices; all 112 are in dispatch state "Queued - not dispatched"; the dispatcher shows 0 send attempts and no errors for them [verified] (Priya Nair, internal note 2026-11-12 10:20, job log)
- No client has received an invoice; two clients have rung to ask where it is [reported] (Daniel Okafor, 2026-11-12 09:14)
- Customer has not changed any settings on their side [reported] (Daniel Okafor, 2026-11-12 09:14)
- Impact: clients' payment terms run from the send date, so each day of delay pushes back collections [reported] (Daniel Okafor, 2026-11-12 09:14)
- Next runs: 13 Nov 07:00 with 64 invoices and Sunday 15 Nov with 90 invoices [reported] (Daniel Okafor, 2026-11-12 09:14 and 10:52)
- Customer has 340 schedules [reported] (Daniel Okafor, 2026-11-12 10:52); 340 active schedules as of 1 November 2026 [verified] (account record)
- All 112 invoices come from schedules created before 10 Nov (v8.3 release) [verified] (Priya Nair, internal note 2026-11-12 10:20)
- The account has 3 schedules created after 10 Nov; none was due on 12 Nov, so there is no direct comparison [verified] (Priya Nair, internal note 2026-11-12 10:20)
- Known issue KI-3381 "Legacy recurring schedules skip auto-send after v8.3" exists, opened by Engineering 11 Nov, status Investigating, 2 other customers linked [verified] (Priya Nair, internal note 2026-11-12 10:20); ticket linked to KI-3381 [verified] (event 2026-11-12 11:30)
- Cause is KI-3381 (pre-v8.3 schedules skip auto-send): symptoms match, "Not confirmed as the same cause" [suspected] (Priya Nair, 2026-11-12 10:20, 10:34, 11:30)
- Manual send from the invoice list works for an affected invoice [verified] (Priya Nair, internal note 2026-11-12 10:20, Test 1)
- Re-saving the schedule "Meadowgate monthly retainer" restored dispatch for a "Run now (test mode)" run [verified] (Priya Nair, internal note 2026-11-12 10:20, Test 2)
- Re-saving clears the fault on a real scheduled run: "Not yet seen on a real scheduled run" [suspected] (Priya Nair, internal note 2026-11-12 10:20)
- Environment: Quillbill Practice plan, Enterprise support level, Quillbill Invoicing (cloud) with Recurring Billing add-on, data region UK [verified] (account record)

Conflicts: none. (Customer's "around 110" invoices [reported] vs 112 in the job log [verified] is an approximation, not a disagreement.)

## Tried so far
| When | Who | What | Result |
|------|-----|------|--------|
| 2026-11-12, by 10:20 | Priya Nair (Tier 1) | Checked job log for HF-0192 | 112 invoices generated at 07:00:03, all "Queued - not dispatched", 0 send attempts, no errors |
| 2026-11-12, by 10:20 | Priya Nair (Tier 1) | Checked known issues | KI-3381 matches symptoms; same cause not confirmed |
| 2026-11-12 10:15 | Priya Nair (Tier 1), with customer's permission (09:58) | Test 1: manual Send on INV-2026-11-0457 (Meadowgate Ltd) from the invoice list | Accepted by recipient's mail server at 10:16 |
| 2026-11-12, by 10:20 | Priya Nair (Tier 1) | Test 2: re-saved schedule "Meadowgate monthly retainer" without changes, then "Run now (test mode)" (sends only to account owner) | Test invoice dispatched within 40 seconds; not yet seen on a real scheduled run |
| 2026-11-12 afternoon (planned, 10:52) | Daniel Okafor (customer) | Bulk-send the remaining 111 queued invoices from the invoice list | Result not recorded |

## Commitments to the customer
| When | Made by | Verbatim commitment | Status (met / pending / overdue) | Policy note |
|------|---------|---------------------|----------------------------------|-------------|
| 2026-11-12 09:41 | Priya Nair (Tier 1) | "I'm looking at your account now." | Met (job-log check in internal note 10:20) | 6.1: "Support agents may commit to the time of the next update and to actions they will take themselves." |
| 2026-11-12 11:05 | Priya Nair (Tier 1) | "I'm escalating your ticket to our Product Engineering Support team now" | Met (escalated to Tier 2, event 11:30) | 6.1 (as above) |
| 2026-11-12 11:05 | Priya Nair (Tier 1) | "I'll make sure they know your next run is at 07:00 UTC tomorrow, 13 November, with 64 invoices." | Met (stated in escalation note 11:30) | 6.1 (as above) |
| 2026-11-12 11:05 | Priya Nair (Tier 1) | "I will email you an update by 16:00 UTC today with what they've found, even if that is only that they are still investigating." | Pending: due 2026-11-12 16:00 UTC, 4 h 30 min after now | 6.1 (as above); 5.2: "From escalation, Tier 2 owns the ticket, including customer updates and any commitments already made to the customer." Tier 2 now owns this. |

Declined, not a commitment: to "Can you guarantee this will be fixed before tomorrow morning's run?" (Daniel Okafor, 10:52), Priya Nair replied "I can't promise a fix time, because that depends on what engineering finds." (11:05). Policy 6.2: "Support agents must not promise a fix date for a product defect, a release date, a service credit or a refund."

## Service level
Basis: support level Enterprise (account record; policy 1.3), priority P2 (set at creation 09:14, unchanged at 11:30). Status history New → Open → Escalated; never "Pending customer", so no paused time (4.2, 4.3).

First response:
- Clause: "Enterprise | P2 | 2 hours, 24x7 | 24 hours, 24x7" (3.1); "Targets marked "24x7" run on calendar time." (3.3); "The clock starts when the ticket is created." (4.1)
- Clock: first response, calendar hours, started at ticket creation, 2026-11-12 09:14 UTC
- Deadline: 2026-11-12 11:14 UTC (09:14 + 2 h)
- Status: met (first agent reply 09:41, 27 minutes after creation); missing terms: none

Resolution:
- Clause: "Enterprise | P2 | 2 hours, 24x7 | 24 hours, 24x7" (3.1); "A ticket is "breached" if its resolution target has passed and it is not resolved, and "at risk" if less than 25% of its resolution target remains, measured on the same basis (calendar hours or business hours) as the target. Otherwise it is "within target"." (4.5)
- Clock: resolution, calendar hours, started at ticket creation, 2026-11-12 09:14 UTC
- Deadline: 2026-11-13 09:14 UTC (09:14 + 24 h, no paused time). At-risk threshold: 25% of 24 h = 6 h, so "at risk" from 2026-11-13 03:14 UTC (09:14 − 6 h).
- Status: open, "within target", 21 h 44 min remaining at now (11:30 on 12 Nov to 09:14 on 13 Nov); becomes "at risk" at 03:14 on 13 Nov, before the 07:00 run; missing terms: none
- Note: if breached, policy 5.3 applies: "The Support Duty Manager must be told of every P1 ticket and of every P2 ticket that is breached."

Customer update interval:
- Clause: "P2 tickets: an update at least once each business day." (7.1); business hours "08:00 to 18:00 Europe/London time, Monday to Friday ... Between 25 October 2026 and 28 March 2027, Europe/London time is GMT, which is the same as UTC." (1.1)
- Clock: update interval, business days; Thursday 12 Nov covered by customer updates at 10:34 and 11:05
- Deadline: next update by end of business day Friday 13 Nov, 18:00 UTC (the 16:00 UTC 12 Nov commitment falls earlier)
- Status: met for 12 Nov; open for 13 Nov; missing terms: none (whether 13 Nov is a bank holiday in England is not stated in the inputs; it does not change the 12 Nov status)

## Open questions
- Can the fix be guaranteed before the 13 Nov 07:00 run (64 invoices)? (asked by Daniel Okafor, 2026-11-12 10:52; declined as a fix-time promise, not answered on substance)
- Is the cause the same as KI-3381? (raised by Priya Nair, 2026-11-12 10:20 and 10:34: "I can't yet confirm that yours has the same cause")
- Does re-saving a schedule restore dispatch on a real scheduled run, not just test mode? (raised by Priya Nair, 2026-11-12 10:20: "Not yet seen on a real scheduled run")
- Do schedules created after 10 Nov dispatch normally? (raised by Priya Nair, 2026-11-12 10:20: "no direct comparison yet")

## Recommended next action
Run a controlled test on the real 13 Nov 07:00 UTC run: with Daniel Okafor's agreement (ask in the 16:00 UTC update already promised), re-save a subset of the schedules due in that run and leave the rest unchanged, then check the dispatch state of both groups right after 07:00 and report the result to the KI-3381 investigation. Owner: Tier 2 (Product Engineering Support) engineer who now owns the ticket; agreement requested by 2026-11-12 16:00 UTC, re-saves done before 2026-11-13 07:00 UTC, result checked by 07:15 UTC, ahead of the 09:14 UTC resolution deadline. Rests on: re-save fix seen in test mode only [verified, Priya Nair 10:20, Test 2]; re-save on a real run not yet seen [suspected, Priya Nair 10:20]; cause suspected as KI-3381 [suspected, Priya Nair 10:20/10:34/11:30]; next run 13 Nov 07:00 with 64 invoices [reported, Daniel Okafor 10:52]; pending 16:00 UTC update commitment [Priya Nair 11:05]; resolution deadline 2026-11-13 09:14 UTC (policy 3.1, 4.1).
