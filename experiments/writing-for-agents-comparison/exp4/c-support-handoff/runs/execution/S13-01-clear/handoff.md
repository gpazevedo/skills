# Escalation handoff: QB-204518 Recurring invoices created but not sent (Harrow & Finch, HF-0192)

Reference time ("now"): 2026-11-12 11:30 UTC (given in the thread export header as the as-of time; also the timestamp of the last thread message)
Inputs missing: none (thread, account record and policy v4.2 all supplied). The thread has no "Pending customer" status entries, so no paused time is recorded.

## Problem as currently understood
The 07:00 UTC recurring run on 12 Nov generated 112 invoices that sit in "Queued - not dispatched" with no send attempts and no errors. All 112 come from schedules created before 10 Nov (the v8.3 release). The leading hypothesis is known issue KI-3381 (legacy schedules skip auto-send after v8.3), but support has not confirmed it as the cause. A manual send works, and re-saving one schedule appeared to restore sending in test mode only. The next runs are 13 Nov 07:00 UTC (64 invoices) and 15 Nov (90 invoices).

- 07:00:03 UTC run generated 112 invoices, all "Queued - not dispatched", 0 send attempts, no errors [verified] (Priya Nair internal note, 2026-11-12 10:20, job log)
- All 112 come from schedules created before 10 Nov; the account has 3 schedules created after 10 Nov, none due today, so there is no direct comparison [verified] (Priya Nair, 10:20, job log)
- Manual Send of INV-2026-11-0457 at 10:15 was accepted by the recipient's mail server at 10:16 [verified] (Priya Nair, 10:20, delivery log)
- Re-saving "Meadowgate monthly retainer" unchanged, then "Run now (test mode)", dispatched the test invoice within 40 seconds [verified as an observation] (Priya Nair, 10:20); that re-saving clears the fault on real scheduled runs is [suspected] (Priya Nair, 10:20: "Not yet seen on a real scheduled run")
- Cause is KI-3381 (opened by Engineering 11 Nov, Investigating, 2 other customers linked) [suspected] (Priya Nair, 10:20 and 10:34: "Not confirmed as the same cause"; "I can't yet confirm")
- Account has 340 active recurring schedules (as of 1 Nov) [verified] (account record)
- Nothing was changed on the customer's side [reported] (Daniel Okafor, 09:14)
- No client has received an invoice from this morning's run; two clients have rung to ask [reported] (Daniel Okafor, 09:14); only Meadowgate's manual send is known to have been delivered
- About 110 invoices were expected at 07:00 [reported] (Daniel Okafor, 09:14); the job log shows 112 [verified] (10:20)
- Client payment terms run from the send date, so delay pushes back collections [reported] (Daniel Okafor, 09:14)
- Next runs are 13 Nov 07:00 UTC with 64 invoices and 15 Nov with 90 invoices [reported] (Daniel Okafor, 10:52; Priya Nair repeats the 64 and the time at 11:05); not checked against the schedule data
- Bulk-send workaround (filter "Queued", select up to 50, Send) [suspected as to whether it works at scale] (Priya Nair, 10:34); no test of it is recorded. The customer says they will bulk-send 111 this afternoon [reported] (Daniel Okafor, 10:52)
Conflicts: none. The customer's "about 110" versus the log's 112 is a count difference, not a disagreement about the cause.

## Tried so far
| When | Who | What | Result |
|------|-----|------|--------|
| 2026-11-12 10:15 | Priya Nair | Manual Send of INV-2026-11-0457 from the invoice list (customer agreed at 09:58) | Accepted by recipient mail server 10:16 |
| 2026-11-12 ~10:15-10:20 (time not stated) | Priya Nair | Re-saved "Meadowgate monthly retainer" unchanged, then "Run now (test mode)" (sends to account owner only) | Test invoice dispatched within 40 seconds; not seen on a real scheduled run |
| 2026-11-12 10:20 | Priya Nair | Checked job log and dispatcher for HF-0192 | 112 invoices queued, 0 send attempts, no errors |
| 2026-11-12 10:20 | Priya Nair | Matched the symptoms to KI-3381 | Symptoms match; cause not confirmed |
| 2026-11-12 10:34 | Priya Nair | Proposed bulk send from the invoice list (up to 50 at a time) | Result not recorded; the customer plans to run it this afternoon |
| 2026-11-12 | Daniel Okafor | Said no settings were changed | Reported only |

## Commitments to the customer
| When | Made by | Verbatim commitment | Status (met / pending / overdue) | Policy note |
|------|---------|---------------------|----------------------------------|-------------|
| 2026-11-12 11:05 | Priya Nair | "I will email you an update by 16:00 UTC today with what they've found, even if that is only that they are still investigating." | pending (deadline 16:00 UTC, 4h30m after now) | Policy 6.1: "Support agents may commit to the time of the next update and to actions they will take themselves." Policy 5.2: "From escalation, Tier 2 owns the ticket, including customer updates and any commitments already made to the customer." Tier 2 owns this now. |
| 2026-11-12 11:05 | Priya Nair | "I'll make sure they know your next run is at 07:00 UTC tomorrow, 13 November, with 64 invoices." | met (it is in the escalation note, 11:30) | Action Priya takes herself; allowed under 6.1 |
No fix date, credit or refund was promised: Priya said "I can't promise a fix time" (11:05), which is in line with Policy 6.2: "Support agents must not promise a fix date for a product defect, a release date, a service credit or a refund." The customer asked for a guarantee of a fix before tomorrow's run [reported expectation] (Daniel Okafor, 10:52); it is unanswered beyond that refusal. Only the CSM named in the account record (Elena Marsh) or the Head of Support may offer credits (Policy 6.3); none is offered or on record (account record: Open credits None).

## Service level
Applicable: Enterprise support level (account record), priority P2 (ticket header; unchanged at escalation; the customer has not asked for a different priority, only said "urgent"). Tier 2 should note that Policy 2.2 defines P2 as "no practical workaround", and a manual bulk send is offered for today's invoices; priority is set by support (Policy 2.5), and I make no change.

Clock 1, first response
- Clause: "Enterprise | P2 | 2 hours, 24x7" (Policy 3.1); "First response means the first reply to the customer from a support agent" (1.4)
- Clock: first response, calendar hours, started ticket creation 2026-11-12 09:14 (Policy 4.1)
- Deadline: 2026-11-12 11:14 (09:14 + 2h)
- Status: met; first reply 09:41 (27 minutes); missing terms: none

Clock 2, resolution
- Clause: "Enterprise | P2 | 2 hours, 24x7 | 24 hours, 24x7" (Policy 3.1); "Targets marked '24x7' run on calendar time" (3.3); "The clock starts when the ticket is created" (4.1)
- Clock: resolution, calendar hours, started 2026-11-12 09:14; no paused time recorded
- Deadline: 2026-11-13 09:14 (09:14 + 24h). Elapsed at now: 2h16m; remaining: 21h44m
- Status: open, 21h44m remaining, "within target" under 4.5 ("at risk" is less than 25% remaining; 25% of 24h = 6h, and 21h44m is more than 6h). It becomes "at risk" at 2026-11-13 03:14 (09:14 + 18h). Note that tomorrow's 07:00 run falls before the 09:14 deadline; missing terms: none
- Resolution needs a fix or workaround that restores the affected function and the ticket status set to Resolved (Policy 1.5)

Clock 3, customer update
- Clause: "P2 tickets: an update at least once each business day." (Policy 7.1)
- Clock: business-day update; 12 Nov 2026 is a Thursday; updates at 10:34 and 11:05 already sent
- Status: met for 12 Nov; the next is due by end of the next business day, Fri 13 Nov (separate from the 16:00 commitment above); missing terms: none. The bank-holiday calendar was not supplied, but 12-13 Nov are not bank holidays in England as far as the inputs show.
Escalation: Policy 5.1 allows escalation when it cannot be resolved with documented procedures. Policy 5.3 (Duty Manager) applies only to breached P2 tickets, so it does not apply now; it would apply if 09:14 tomorrow passes unresolved.

## Open questions
- Can I guarantee this will be fixed before tomorrow morning's run? (asked by Daniel Okafor, 2026-11-12 10:52; Priya declined to promise a fix time at 11:05; no answer on what engineering can do before 07:00)
- Is the cause the same as KI-3381? (raised by Priya Nair, 10:20 and 10:34; unanswered)
- Does re-saving a schedule restore auto-send on a real scheduled run, not only test mode? (Priya Nair, 10:20: "Not yet seen on a real scheduled run")
- Will the 64 invoices due tomorrow come from pre-10 Nov schedules (and the 90 on Sunday)? Not stated in the thread.
- Does the bulk send work for the 111 queued invoices? Result not recorded.
- Is a re-save of all 340 schedules, or a backend fix, available? Daniel Okafor said that re-saving each by hand "isn't realistic" (10:52).

## Recommended next action
Tier 2 engineer to test KI-3381 directly: check whether the 64 schedules due 13 Nov 07:00 UTC were created before 10 Nov, then re-save a small subset of them (with the customer's agreement, as it affects real client sends) and confirm at the 07:00 run that they dispatch while an untouched pre-10 Nov schedule does not; also compare the 3 post-10 Nov schedules when due. Owner: Tier 2 (Product Engineering Support), by 2026-11-12 15:30 UTC, so the result can go into the update promised by 16:00 UTC. Rests on: job log (10:20), the re-save/test-mode result (10:20), the KI-3381 link (10:20, 11:30), the commitment of an update by 16:00 (11:05), the customer's questions on 13 Nov 07:00 (10:52), and the resolution deadline 2026-11-13 09:14.
