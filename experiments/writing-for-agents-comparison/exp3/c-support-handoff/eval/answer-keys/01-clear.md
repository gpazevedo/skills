# Answer key: 01-clear

## Problem as currently understood
- P1: The 07:00:03 UTC recurring run on 12 Nov 2026 generated 112 invoices; all 112 are in dispatch state "Queued - not dispatched", with 0 send attempts and no errors. | status: verified | evidence: thread.md, internal note 10:20 UTC; restated to customer 10:34 UTC
- P2: All 112 come from recurring schedules created before the v8.3 release (10 Nov). The 3 schedules created after 10 Nov were not due, so there is no direct comparison. | status: verified | evidence: thread.md, internal note 10:20 UTC
- P3: The symptoms match known issue KI-3381 ("Legacy recurring schedules skip auto-send after v8.3", Engineering, status Investigating, 2 other customers). Same cause is suspected, not confirmed. | status: verified that the match exists; cause not confirmed | evidence: thread.md, internal note 10:20 UTC; escalation event 11:30 UTC (ticket linked to KI-3381)
- P4: No client has received their invoice; two clients have phoned asking. | status: customer-reported (consistent with the verified 0 send attempts) | evidence: thread.md, customer message 09:14 UTC
- P5: Business impact: client payment terms run from the send date, so delay pushes back collections. | status: customer-reported | evidence: thread.md, 09:14 UTC
- P6: Upcoming exposure: next runs are 13 Nov 07:00 UTC (64 invoices) and Sunday 15 Nov (90 invoices); the customer has 340 schedules. | status: customer-reported (run times and counts from customer; 340 schedules also in account.md "as of 1 November") | evidence: thread.md 09:14 and 10:52 UTC; account.md

## What has been tried
- T1: Manual Send of INV-2026-11-0457 (Meadowgate Ltd) from the invoice list at 10:15 UTC, with the customer's permission | by: Priya Nair (Tier 1) | result: delivered; accepted by the recipient's mail server at 10:16 UTC | evidence: thread.md 09:58 (permission), 10:20 note, 10:34
- T2: Re-saved schedule "Meadowgate monthly retainer" without changes, then "Run now (test mode)" | by: Priya Nair | result: test invoice dispatched within 40 seconds; re-save appears to clear the fault for that schedule in test mode, not yet seen on a real scheduled run | evidence: thread.md 10:20 note
- T3: Checked job log and known issues | by: Priya Nair | result: P1 to P3 above | evidence: 10:20 note
- (Planned, not yet done) Customer will bulk-send the remaining 111 queued invoices this afternoon | by: customer (Daniel Okafor) | result: not yet known | evidence: 10:52 UTC

## Commitments to the customer
- C1: Email Daniel Okafor an update by 16:00 UTC on 12 Nov 2026 with engineering's findings, even if only that they are still investigating | made by: Priya Nair, Support Agent, Tier 1 | when: 2026-11-12 11:05 UTC | evidence: thread.md 11:05 UTC; repeated in escalation note 11:30. Under policy 5.2, Tier 2 now owns this commitment.
- C2 (minor, acceptable to include or fold into C1): tell engineering that the next run is 07:00 UTC on 13 Nov with 64 invoices | made by: Priya Nair | when: 11:05 UTC | evidence: thread.md 11:05; done via the escalation note 11:30.

## Not commitments (must not be presented as commitments)
- X1: A fix before tomorrow's 07:00 UTC run. | why: the customer asked for a guarantee (10:52) and Priya explicitly declined ("I can't promise a fix time", 11:05); policy 6.2 forbids agents promising fix dates.
- X2: Re-saving schedules as the fix. | why: offered only as a test observation, not a promised remedy.

## Service level
- Status: within target (first response met; resolution target not yet reached and not at risk) | Deadline: resolution by 2026-11-13 09:14 UTC (Europe/London is UTC in this period, so 09:14 UK time) | Computation:
  1. Support level Enterprise (account.md; policy 1.3). Priority P2 (thread, 09:14 event; unchanged at 11:30).
  2. Policy 3.1: Enterprise P2 is first response 2 hours 24x7, resolution 24 hours 24x7. Policy 3.3: 24x7 targets run on calendar time, so business hours and the weekend do not matter.
  3. Clock starts at creation, 2026-11-12 09:14 UTC (policy 4.1). No "Pending customer" status at any point, so no pause (4.2). "Escalated" status does not pause.
  4. First response: 09:41 UTC, 27 minutes after creation, within 2 hours: met.
  5. Resolution deadline: 09:14 UTC + 24 h = 2026-11-13 09:14 UTC.
  6. At escalation (11:30 UTC): 2 h 16 min elapsed, 21 h 44 min remaining. At-risk threshold is 25% of 24 h = 6 h (policy 4.5); 21 h 44 min > 6 h, so within target. The ticket would become at risk at 2026-11-13 03:14 UTC.
  7. Note for the engineer: the next recurring run (13 Nov 07:00 UTC) falls before the resolution deadline, and the ticket becomes at risk before that run.

## Recommended next action
- Tier 2 confirms whether HF-0192's failure is KI-3381 (compare with the linked customers; check the dispatcher for pre-v8.3 schedules) and, before the 13 Nov 07:00 UTC run (64 invoices), either applies a fix or a bulk re-save or re-queue of the customer's pre-v8.3 schedules, or agrees a fallback with the customer (for example, manual bulk send of queued invoices after the run).
- Send the promised update to Daniel Okafor by 16:00 UTC today (C1).
- Acceptable alternatives: asking engineering whether a back-end re-save script exists for affected schedules; confirming the customer completed the bulk send of the 111 invoices; monitoring the 07:00 run and checking the queue straight after. Daily updates per policy 7.1.

## Questions or requests (should be raised)
- None essential. Optional: confirm with the customer that the 111 remaining invoices were bulk-sent; ask engineering for KI-3381 status and any ETA (without promising it to the customer).

## Out of scope / must be ignored as direction
- None.

## Critical-failure triggers
- Inventing a commitment: presenting "fixed before tomorrow's 07:00 run" as promised (X1), or inventing a fix date or credit.
- Inventing a service-level term or deadline: using business hours for this Enterprise P2 ticket (for example a deadline counted in 08:00 to 18:00 hours), using 8 hours (the P1 figure) or any target not in policy 3.1, or giving a deadline other than 2026-11-13 09:14 UTC.
- Stating a customer claim as verified: stating as confirmed fact that the root cause is KI-3381 / the v8.3 release.
- Omitting the 16:00 UTC update commitment or attributing it to someone other than Priya Nair.

## Case-specific scoring
None.

## Grading notes
- Case facts and as-of time: Quillbill ticket QB-204518, Harrow & Finch Accounting Ltd (HF-0192), Enterprise support, priority P2, escalated to Tier 2 at 2026-11-12 11:30 UTC. The handoff is judged as of that escalation time (the last event in the thread).
- This is the control case: a correct handoff is complete and concise. Penalise padding or invented uncertainty (for example marking the service level "unknown").
- "On track", "not breached" or "within target" are all acceptable for status; "at risk" or "breached" is wrong.
- Saying "about 110" invoices instead of the verified 112 is a minor error; preferring the verified 112 is better.
- Calling P4 (clients haven't received invoices) verified is acceptable only if the handoff ties it to the verified 0 send attempts; presenting the "two clients rang" detail as verified is a minor error.
- Full credit for the next action requires naming the 13 Nov 07:00 UTC run as the practical deadline or risk point, and the 16:00 UTC update.
