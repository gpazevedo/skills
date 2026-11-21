# Escalation handoff: QB-204518 112 recurring invoices stuck "Queued - not dispatched" after the 07:00 UTC run on 12 Nov

**Customer:** Harrow & Finch Accounting Ltd, HF-0192, Quillbill Practice, support level Enterprise (account record: "Support level: Enterprise")   **Severity/priority:** P2, set at ticket creation ("Priority: P2", thread 2026-11-12 09:14 UTC) and "P2 (unchanged)" at escalation (thread 11:30 UTC)
**Most urgent deadline:** Email update to the customer by 16:00 UTC on 12 Nov 2026 (Priya Nair, thread 11:05 UTC). Next after that: the customer's next recurring run at 07:00 UTC on 13 Nov (64 invoices, Reported), then the resolution target at 09:14 UTC on 13 Nov (policy 3.1, Enterprise P2). As-of time is 2026-11-12 11:30 UTC.

## Problem as currently understood
The 07:00 UTC recurring run on 12 Nov generated 112 invoices, and none was dispatched; all sit in "Queued - not dispatched" with no send attempts and no errors. All 112 come from schedules created before the 10 Nov v8.3 release, which matches known issue KI-3381, but support has not confirmed the same cause. Manual send works, and re-saving a schedule appeared to restore dispatch in test mode only. The customer has about 340 schedules and cannot re-save them by hand before the next runs.

| Fact | Status | How established / cite |
|---|---|---|
| Recurring run at 07:00:03 UTC on 12 Nov generated 112 invoices | Verified | Job log read by Priya Nair, internal note 10:20 UTC |
| All 112 are in dispatch state "Queued - not dispatched"; dispatcher shows 0 send attempts and no errors | Verified | Job log, internal note 10:20 UTC |
| All 112 come from schedules created before 10 Nov (v8.3 release); account has 3 schedules created after 10 Nov, none due today, so no direct comparison exists | Verified | Priya Nair internal note 10:20 UTC |
| Manual Send of INV-2026-11-0457 (Meadowgate Ltd) at 10:15 was accepted by the recipient's mail server at 10:16 | Verified | Delivery log, internal note 10:20 UTC |
| Re-saving schedule "Meadowgate monthly retainer" unchanged, then "Run now (test mode)", dispatched a test invoice within 40 seconds | Verified (for that one schedule, test mode only) | Test 2, internal note 10:20 UTC |
| Re-saving clears the fault on a real scheduled run | Hypothesis | Priya Nair: "Not yet seen on a real scheduled run" (10:20 UTC); no test result |
| Re-saving clears the fault for schedules other than Meadowgate | Hypothesis | Only one schedule tested; no cite for others |
| The cause is KI-3381 "Legacy recurring schedules skip auto-send after v8.3" (status Investigating, 2 other customers linked, opened by Engineering 11 Nov) | Hypothesis | Priya Nair: "Symptoms match. Not confirmed as the same cause." (10:20 UTC); ticket linked to KI-3381 at 11:30 UTC |
| Account has 340 active recurring schedules (as of 1 Nov 2026) | Verified | Account record, Recurring Billing add-on |
| About 110 invoices were expected at 07:00; no client has received theirs | Reported | Daniel Okafor, 09:14 UTC (the 112 count is Verified above) |
| Two clients have rung to ask where their invoice is | Reported | Daniel Okafor, 09:14 UTC |
| No settings changed on the customer side | Reported | Daniel Okafor, 09:14 UTC |
| Client payment terms run from the send date, so delay pushes back collections | Reported | Daniel Okafor, 09:14 UTC |
| Next runs: 13 Nov 07:00 UTC with 64 invoices, and Sunday 15 Nov with 90 invoices | Reported | Daniel Okafor 10:52 UTC; Priya Nair repeats 64 at 13 Nov 07:00 UTC (11:05 UTC) without independent check |
| Whether the 64 and 90 invoices come from pre-v8.3 schedules (and so are affected) | Hypothesis | Inferred from KI-3381 pattern; nothing in the thread checks it |
| Customer intends to bulk-send the remaining 111 today themselves | Reported | Daniel Okafor, 10:52 UTC |

**Open disagreements:** None between customer and support findings. Minor: the customer says "around 110" invoices (09:14 UTC) and support's job log shows 112 (10:20 UTC); the log count is the one to use.

## What has been tried
| When | Who | Action | Result | Cite |
|---|---|---|---|---|
| 12 Nov 09:41-10:20 | Priya Nair | Reviewed the job log and dispatcher for HF-0192 | 112 invoices queued, 0 send attempts, no errors; all from pre-10 Nov schedules | Internal note 10:20 UTC |
| 12 Nov 10:15 | Priya Nair (customer consented 09:58) | Manual Send of INV-2026-11-0457 from the invoice list | Accepted by recipient mail server at 10:16 | Internal note 10:20 UTC; customer 09:58 UTC |
| 12 Nov before 10:20 (time not recorded) | Priya Nair | Opened schedule "Meadowgate monthly retainer", saved unchanged, ran "Run now (test mode)" | Test invoice dispatched within 40 seconds; real scheduled run not tested | Internal note 10:20 UTC |
| 12 Nov 10:20 | Priya Nair | Checked known issues | KI-3381 found, symptoms match, cause not confirmed | Internal note 10:20 UTC |
| 12 Nov 10:34 | Priya Nair | Gave the customer the bulk-send workaround (filter "Queued", select up to 50, Send) | Customer will use it this afternoon; not yet done as of 11:30 | Priya 10:34 UTC; customer 10:52 UTC |
| 12 Nov 11:30 | Priya Nair | Escalated to Tier 2 and linked to KI-3381 | Status Open to Escalated | Event 11:30 UTC |

## Commitments to the customer
| Commitment (verbatim) | Made by (role) | When / cite | Deadline | Kept / Open / Missed |
|---|---|---|---|---|
| "I'm escalating your ticket to our Product Engineering Support team now" | Priya Nair (Tier 1 Support Agent) | 12 Nov 11:05 UTC, message to customer | Now | Kept (escalated 11:30 UTC) |
| "I'll make sure they know your next run is at 07:00 UTC tomorrow, 13 November, with 64 invoices" | Priya Nair (Tier 1 Support Agent) | 12 Nov 11:05 UTC, message to customer | None stated | Kept (escalation note 11:30 UTC states 13 Nov 07:00 UTC, 64 invoices) |
| "I will email you an update by 16:00 UTC today with what they've found, even if that is only that they are still investigating." | Priya Nair (Tier 1 Support Agent) | 12 Nov 11:05 UTC, message to customer | 12 Nov 16:00 UTC | Open (4.5 hours left at 11:30 UTC). Under policy 5.2, Tier 2 now owns this commitment. Within policy 6.1 (time of next update). |

The customer's question "Can you guarantee this will be fixed before tomorrow morning's run?" was answered with "I can't promise a fix time, because that depends on what engineering finds." No fix date was promised, consistent with policy 6.2. No credit or refund was offered (account record: "Open credits: None", "Refunds: None"; policy 6.3 reserves those to the Customer Success Manager, Elena Marsh, or the Head of Support).

## Service-level status
Support level Enterprise (account record), priority P2 (thread). Status was never "Pending customer", so there is no paused time (policy 4.2: "The clock is paused only while the ticket status is 'Pending customer'"). Clock start: ticket created 12 Nov 09:14 UTC (policy 4.1: "The clock starts when the ticket is created."). Elapsed at 11:30 UTC: 2h16m.

| Clock | Policy clause (quoted) | Started | Deadline (with arithmetic) | Status |
|---|---|---|---|---|
| First response | 3.1: Enterprise P2 "2 hours, 24x7" | 12 Nov 09:14 UTC | 09:14 + 2h = 12 Nov 11:14 UTC. First reply by an agent (policy 1.4) was Priya Nair at 09:41 UTC, 27 min after creation | Met |
| Resolution | 3.1: Enterprise P2 "24 hours, 24x7"; 3.3 "Targets marked '24x7' run on calendar time" | 12 Nov 09:14 UTC | 09:14 + 24h = 13 Nov 09:14 UTC. Remaining at 11:30: 21h44m (90.6% of target) | Within target. "At risk" under 4.5 ("less than 25% of its resolution target remains") begins when under 6h remain, that is after 13 Nov 03:14 UTC. Breached if unresolved after 13 Nov 09:14 UTC. Resolution requires status Resolved (policy 1.5). |
| Customer update interval | 7.1: "P2 tickets: an update at least once each business day." | 12 Nov (Thursday) | Update sent 10:34 UTC on 12 Nov satisfies 12 Nov. Next: by end of business day 13 Nov (18:00 Europe/London = 18:00 UTC, policy 1.1) | On track. The thread's 16:00 UTC commitment is the tighter deadline for today. |

Other policy points: 5.1 allows escalation when "a P1 or P2 ticket is at risk" or it cannot be resolved with documented procedures; escalation done. 5.3 (Duty Manager) applies to a P2 only if breached; not breached now, so not yet required, but required if the 13 Nov 09:14 UTC target passes unresolved.

## Recommended next action
Tier 2 should confirm whether KI-3381 is the cause of this ticket's fault and produce a fix or workaround that works for all affected schedules before the 13 Nov 07:00 UTC run. Evidence: all 112 stuck invoices come from pre-v8.3 schedules, the dispatcher shows 0 attempts and no errors, and re-saving one schedule dispatched in test mode (Hypothesis that it works on a real run). Confirm the dependent facts as part of the action: (1) check whether tomorrow's 64 invoices come from pre-v8.3 schedules and are affected (Reported only); (2) if a re-save or bulk fix is proposed, test it on a real scheduled run, since only test mode has been seen; (3) check whether any of the 3 post-10 Nov schedules dispatch normally, to settle the pre/post v8.3 split. The result would settle whether KI-3381 is the cause, whether the 340 schedules need a bulk remedy, and what to tell the customer. Deadline to beat: send the customer an update by 16:00 UTC today (Tier 2 now owns it, policy 5.2), even if only "still investigating"; then the 13 Nov 07:00 UTC run, and the resolution target at 13 Nov 09:14 UTC. Do not promise a fix date, credit or refund (policy 6.2, 6.3).

## Gaps
- Real scheduled run behaviour after re-save: not recorded; closes with a real-run test or a fix verification.
- Whether tomorrow's 64 invoices and Sunday's 90 are from affected schedules: Reported only; check the schedule creation dates.
- How many of the 340 schedules (as of 1 Nov, account record) predate 10 Nov: not recorded in the thread.
- Time of the test-mode re-save test: not recorded beyond "before 10:20 UTC".
- Whether the customer has completed the bulk send of 111 invoices: not recorded as of 11:30 UTC; check at the 16:00 UTC update.
- Priority basis: P2 (policy 2.2) requires "no practical workaround", yet the thread offers a manual bulk-send workaround, which could point to P3 (policy 2.3). Priority changes only when an agent records it (policy 2.5); no agent has. If P3 were recorded, Enterprise P3 would give resolution "30 business hours" (3.1), conditional deadline 17 Nov 09:14 UTC (Thu 8h46m + Fri 10h + Mon 10h + 1h14m on Tue); first response "4 business hours". Tier 2 should decide whether the priority is right, noting that the workaround does not cover the recurring runs on 13 and 15 Nov.
