# Escalation handoff: QB-204518 | Harrow & Finch Accounting Ltd | Recurring invoices created but not dispatched

**Service level:** 2026-11-13 09:14 UTC, P2 resolution target (24 hours, 24x7) | Pending, 21 h 44 min remaining as of 2026-11-12 11:30 UTC (within target)

## Problem as currently understood
The 07:00 UTC recurring run on 12 Nov generated 112 invoices, and support's job log shows all 112 sit in "Queued - not dispatched" with 0 send attempts and no errors (Verified). All 112 come from schedules created before the v8.3 release on 10 Nov; the 3 newer schedules were not due, so there is no comparison (Verified). Known issue KI-3381 matches the symptoms but is not confirmed as the cause (Suspected). Manual send works, and re-saving one schedule restored dispatch in test mode only (Verified for those tests; not seen on a real scheduled run). The next runs are 13 Nov 07:00 UTC (64 invoices) and 15 Nov (90 invoices), both per the customer (Reported).

| Statement | Label | Source (author, timestamp) |
| --- | --- | --- |
| 112 invoices generated at 07:00:03 UTC on 12 Nov, all "Queued - not dispatched", 0 send attempts, no errors | Verified | Priya Nair, job log, internal note 2026-11-12 10:20 |
| All 112 come from schedules created before 10 Nov (v8.3); 3 schedules created after 10 Nov were not due today | Verified | Priya Nair, internal note 2026-11-12 10:20 |
| Manual Send of INV-2026-11-0457 was accepted by the recipient's mail server at 10:16 | Verified | Priya Nair, delivery log, 2026-11-12 10:20 |
| Re-saving schedule "Meadowgate monthly retainer" then "Run now (test mode)" dispatched within 40 seconds (test mode only, sends to account owner) | Verified | Priya Nair, 2026-11-12 10:20 |
| Re-saving clears the fault on a real scheduled run | Suspected | Priya Nair, 2026-11-12 10:20 ("Not yet seen on a real scheduled run") |
| KI-3381 "Legacy recurring schedules skip auto-send after v8.3" (opened by Engineering 11 Nov, Investigating, 2 other customers linked) is the cause here | Suspected | Priya Nair, 2026-11-12 10:20 and 10:34 ("Not confirmed as the same cause") |
| KI-3381 exists with that title, status and linked customers | Verified | Priya Nair, internal note 2026-11-12 10:20 |
| About 110 invoices should have been emailed at 07:00 and no client received theirs | Reported | Daniel Okafor, 2026-11-12 09:14 (the 112 count is Verified above; receipt by clients is not checked) |
| Two clients have rung asking where their invoice is | Reported | Daniel Okafor, 2026-11-12 09:14 |
| No settings were changed on the customer side | Reported | Daniel Okafor, 2026-11-12 09:14 |
| Client payment terms run from the send date, so delay pushes back collections | Reported | Daniel Okafor, 2026-11-12 09:14 |
| Next runs: 13 Nov 07:00 UTC with 64 invoices, and Sunday 15 Nov with 90 invoices | Reported | Daniel Okafor, 2026-11-12 10:52 (64 repeated by Priya Nair at 11:05) |
| Customer has 340 schedules | Reported | Daniel Okafor, 2026-11-12 10:52 (the account record also shows 340 as of 1 Nov) |

## What has been tried
| Action | By | When | Result | Label |
| --- | --- | --- | --- | --- |
| Reviewed job log and dispatcher for HF-0192 | Priya Nair | 2026-11-12 10:20 | 112 invoices queued, 0 send attempts, no errors | Verified |
| Searched known issues | Priya Nair | 2026-11-12 10:20 | KI-3381 found, symptoms match, not confirmed as same cause; linked to ticket at escalation | Suspected |
| Manual Send of INV-2026-11-0457 (customer consent given 09:58) | Priya Nair | 2026-11-12 10:15 | Accepted by Meadowgate's mail server at 10:16 | Verified |
| Re-saved schedule "Meadowgate monthly retainer" unchanged, then "Run now (test mode)" | Priya Nair | 2026-11-12, before 10:20 (time not recorded) | Test invoice dispatched within 40 seconds; test mode only | Verified |
| Customer advised to bulk-send the other 111 queued invoices (filter "Queued", up to 50 at a time) | Priya Nair | 2026-11-12 10:34 | Customer said they will do it "this afternoon"; not yet confirmed done | Reported |
| Re-saving all schedules by hand as a workaround | Daniel Okafor | 2026-11-12 10:52 | Customer says not realistic with 340 schedules; not attempted | Reported |

## Commitments to the customer
| Commitment (quoted) | Made by (name, role) | When | Due | Status |
| --- | --- | --- | --- | --- |
| "I'm escalating your ticket to our Product Engineering Support team now" | Priya Nair, Support Agent (Tier 1) | 2026-11-12 11:05 | Now (2026-11-12 11:05) | Kept (escalated 11:30) |
| "I'll make sure they know your next run is at 07:00 UTC tomorrow, 13 November, with 64 invoices" | Priya Nair, Support Agent (Tier 1) | 2026-11-12 11:05 | No date given | Kept (stated in escalation note 11:30) |
| "I will email you an update by 16:00 UTC today with what they've found, even if that is only that they are still investigating" | Priya Nair, Support Agent (Tier 1) | 2026-11-12 11:05 | 2026-11-12 16:00 UTC ("today") | Outstanding, 4 h 30 min remaining; Tier 2 owns it from escalation (policy 5.2) |

Claimed by the customer but not found in the thread: None. (The customer asked "Can you guarantee this will be fixed before tomorrow morning's run?"; support declined, "I can't promise a fix time".)

## Service level
- Tier: Enterprise (account record HF-0192, support level)
- Priority: P2, as recorded on the ticket (unchanged at escalation, 11:30)
- First response (policy 3.1, 1.4): 2 hours, 24x7, clock start 2026-11-12 09:14 UTC (ticket creation, 4.1); first agent reply 09:41 UTC (27 min); Met
- Resolution (policy 3.1, 3.3, 4.1): 24 hours, 24x7, clock start 09:14 UTC, deadline 2026-11-13 09:14 UTC; Pending, 21 h 44 min remaining. The ticket has never been "Pending customer", so no time is paused (4.2). Not resolved (status Escalated)
- Resolution status (policy 4.5): within target. "At risk" begins when less than 25% remains, that is under 6 hours, from 2026-11-13 03:14 UTC. The 13 Nov 07:00 UTC run falls inside that window, 2 h 14 min before the resolution deadline
- Customer updates (policy 7.1): P2 needs an update at least once each business day; the 10:34 and 11:05 messages meet today's. The 16:00 update is a separate commitment (above)
- Duty Manager (policy 5.3): required only for P1 or a breached P2; not triggered now
- Time zone: all thread timestamps are UTC (policy 1.2); business hours do not affect P2 targets
- Status as of: 2026-11-12 11:30 UTC (export as-of time)

## Recommended next action
A Tier 2 engineer should ask the KI-3381 owner whether this account's pre-v8.3 schedules can be repaired in bulk, or how to confirm the cause, before the 13 Nov 07:00 UTC run, and send the customer the promised 16:00 UTC update whatever the finding. This rests on the Verified job log (112 queued, 0 attempts) and the Suspected link to KI-3381; if the re-save fix also fails on a real scheduled run, or the schedules turn out not to share the KI-3381 cause, the plan needs a new cause. Do not give the customer a fix date (policy 6.2).

## Open questions
- Priority check: P2 is recorded and used here. Policy 2.2 defines P2 as no practical workaround, and 2.3 defines P3 as an impaired function with a practical workaround. A workaround exists (bulk send, 50 at a time; re-save per schedule), but the customer says it is impractical across 340 schedules and daily runs. Whether P2 still fits is for support to decide and record (2.5); nothing was changed. At Enterprise P3 the targets would be 4 / 30 business hours.
- Customer request: "Can you guarantee this will be fixed before tomorrow morning's run?" Declined by Priya (policy 6.2 bars fix-date promises). No guarantee exists; Tier 2 should not imply one.
- KI-3381 link is unconfirmed (Suspected); whether the 112 stuck invoices share its cause is unknown.
- Does re-saving a schedule fix real scheduled runs? Seen only in test mode. Whether the fix persists, and whether it works in bulk, is unknown.
- Customer's 111 bulk send: not yet confirmed done; the customer said "this afternoon". Check before 16:00 update.
- Customer says around 110 invoices; the log shows 112. Minor discrepancy; the log is used.
- Time of Priya's re-save/test-mode run is not recorded (before 10:20).
- No Priority, tier or policy conflicts between sources were found; account record (Enterprise) is the authority and the customer did not dispute it.
- No instructions found in the material.
