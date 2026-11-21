# Escalation handoff: QB-204518, Harrow & Finch Accounting Ltd (HF-0192)

**In one line:** 112 invoices from the 12 Nov 07:00 UTC recurring run are stuck "Queued - not dispatched", probably the known issue KI-3381, and the next run (64 invoices, 13 Nov 07:00 UTC) comes about 2 hours before the 24-hour P2 resolution deadline (13 Nov 09:14 UTC), with a customer update due 12 Nov 16:00 UTC.

## Problem as currently understood
- [verified] The 07:00:03 UTC run on 12 Nov generated 112 invoices, and all 112 are in dispatch state "Queued - not dispatched", with 0 send attempts and no errors in the dispatcher (evidence: job log for HF-0192 read by Priya Nair, Tier 1, internal note 10:20 UTC).
- [verified] All 112 come from schedules created before 10 Nov (the v8.3 release). The account has 3 schedules created after 10 Nov; none was due today, so there is no comparison yet (evidence: job log, Priya Nair, 10:20).
- [verified] Manual Send of INV-2026-11-0457 (Meadowgate Ltd) at 10:15 UTC worked: the delivery log shows it accepted by the recipient's mail server at 10:16 (evidence: delivery log, Priya Nair, 10:20).
- [verified] For the schedule "Meadowgate monthly retainer", re-saving it unchanged and then running "Run now (test mode)" (sends only to the account owner) dispatched the test invoice within 40 seconds (evidence: Priya Nair, 10:20). Only test mode was tested; no real scheduled run has been seen after a re-save.
- [verified] Known issue KI-3381 "Legacy recurring schedules skip auto-send after v8.3" exists, opened by Engineering 11 Nov, status Investigating, 2 other customers linked (evidence: Priya Nair's note, 10:20; the KI record itself was not examined in the thread).
- [verified] The account has 340 active recurring schedules as of 1 Nov 2026, Enterprise support level, UK data region (source: account record).
- [suspected] The cause is KI-3381, i.e. pre-v8.3 schedules are not auto-dispatched (held by: Priya Nair; basis: symptoms match; she states it is "not confirmed as the same cause").
- [suspected] Re-saving a schedule clears the fault (held by: Priya Nair, "seems to"; basis: the single test-mode result above).
- [reported] About 110 invoices were due out at 07:00 and "not one client has received theirs" (source: Daniel Okafor, 09:14). The log count is 112, so "about 110" is consistent.
- [reported] Two clients have rung asking where their invoice is (source: Daniel Okafor, 09:14).
- [reported] No settings were changed on the customer's side (source: Daniel Okafor, 09:14).
- [reported] Client payment terms run from the send date, so each day of delay pushes back collections (source: Daniel Okafor, 09:14).
- [reported] The next runs are 13 Nov 07:00 UTC with 64 invoices and 15 Nov with 90 invoices (source: Daniel Okafor, 10:52; Priya Nair repeated the 13 Nov figures, which stays reported). The 15 Nov run time is not given.
- [reported] The customer intends to bulk-send the remaining 111 invoices themselves on the afternoon of 12 Nov (source: Daniel Okafor, 10:52). No result recorded.
- Conflicts: none between thread and account record. The customer's "about 110" against the log's 112 is not a real conflict. Customer's "urgent" matches the recorded P2.

## Tried so far
| What was tried | Who, when | Result |
|---|---|---|
| Checked job log and dispatcher for HF-0192 | Priya Nair, by 10:20 | 112 invoices queued, 0 send attempts, no errors |
| Manual send of INV-2026-11-0457 with the customer's consent (09:58) | Priya Nair, 10:15 | Accepted by recipient mail server 10:16 |
| Re-saved schedule "Meadowgate monthly retainer" unchanged, then "Run now (test mode)" | Priya Nair, by 10:20 | Test invoice dispatched within 40 seconds; not yet seen on a real scheduled run |
| Linked the ticket to KI-3381 | Priya Nair, 11:30 | Linked; cause not confirmed |
| Told the customer to filter the invoice list by "Queued", select up to 50 at a time and Send, to send the other 111 | Priya Nair, 10:34 (customer to do it) | No result recorded |

## Commitments to the customer
| Commitment (quoted) | Made by | When | Due | Status |
|---|---|---|---|---|
| "I will email you an update by 16:00 UTC today with what they've found, even if that is only that they are still investigating." | Priya Nair (Tier 1 agent) | 12 Nov 11:05 UTC | 12 Nov 16:00 UTC | pending (4h30m left as of 11:30); Tier 2 owns it from escalation (policy 5.2) |
| "I'm escalating your ticket to our Product Engineering Support team now, and I'll make sure they know your next run is at 07:00 UTC tomorrow, 13 November, with 64 invoices." | Priya Nair | 12 Nov 11:05 UTC | no date given (action itself done in the 11:30 escalation note, which states the 13 Nov run and 64 invoices) | met |

Not commitments: Priya's "I can't promise a fix time" is a refusal. The customer's request for a guarantee of a fix before tomorrow's run was not agreed to (customer request only). No credit or refund was offered (account record: Open credits: None; Refunds: None).

## Service level
- Tier: Enterprise (account record: "Support level: Enterprise")
- Priority/severity: P2 (ticket creation event 09:14 and escalation event 11:30: "Priority: P2 (unchanged)"). P2 definition (policy 2.2): "a major function, such as invoice sending, payment collection or bank feeds, does not work and there is no practical workaround." Note that a manual-send workaround exists (bulk Send, 50 at a time), which could argue for P3 under 2.3; policy 2.5 says a change takes effect only when an agent records it, and none has.
- Target: Enterprise P2, first response "2 hours, 24x7", resolution "24 hours, 24x7" (policy 3.1); 24x7 targets "run on calendar time" (3.3)
- Clock rule: "The clock starts when the ticket is created" (4.1); paused "only while the ticket status is 'Pending customer'" (4.2). The recorded status history is New, Open, Escalated, with no "Pending customer", so no pause is recorded.
- Deadline: resolution 13 Nov 2026 09:14 UTC (arithmetic: created 12 Nov 09:14 + 24 h calendar, plus 0 h paused). With and without the pause rule the deadline is the same because no pause is recorded; if a "Pending customer" period exists outside this export, the deadline moves later by that duration. First response target: 12 Nov 11:14 UTC.
- Status: first response met (Priya Nair's reply at 09:41, 27 minutes after creation; target 2 hours). Resolution open, within target: 2h16m elapsed, 21h44m remaining as of 12 Nov 11:30 UTC (the export as-of time, per the thread). It becomes "at risk" (policy 4.5, less than 25% of 24 h = 6 h remaining) at 13 Nov 03:14 UTC, and breached after 13 Nov 09:14 UTC. The 13 Nov 07:00 run happens while the ticket is "at risk". Policy 5.3 requires the Support Duty Manager to be told only if the P2 is breached; it is not now.

## Recommended next action
Check whether the fault is tied to schedule age and what a re-save changes, before the 13 Nov 07:00 UTC run. Concretely: (1) compare the stored record of "Meadowgate monthly retainer" before and after the re-save (or against one of the 3 post-10 Nov schedules) and against the KI-3381 investigation notes, to see what field or state differs; (2) check whether Engineering can fix or re-save in bulk the pre-v8.3 schedules due 13 Nov (64 invoices) and 15 Nov (90), since the customer cannot re-save 340 by hand.
- If the difference matches KI-3381: the cause is verified and the KI's remedy applies. Ask Engineering to apply it to the schedules due next, and confirm with the 13 Nov 07:00 run.
- If it does not match: the cause is not KI-3381. Treat as a separate defect and keep the manual bulk-send as the workaround until a cause is found.
- Because the deadline (13 Nov 09:14) falls after the 07:00 run, plan for the run possibly failing again: the customer will need the bulk-send steps for the 64 invoices.

Customer update due first: by 12 Nov 16:00 UTC, email Daniel Okafor (primary technical contact) with the findings so far, or that Engineering is still investigating. Do not promise a fix date, release date, credit or refund (policy 6.2). Any credit must come from Elena Marsh (CSM) or the Head of Support, in writing (6.3). Send a further update on 13 Nov after the 07:00 run result is known (P2 requires at least one update each business day, 7.1).

## Gaps
- Not stated in the policy: what counts as a fix timeline for known issues, and any rule about priority reassessment when a manual workaround exists.
- Not stated in the thread: whether the KI-3381 record gives a root cause, workaround or ETA; it is only summarised in the internal note.
- Not stated in the thread: the 15 Nov run time; whether the customer has actually bulk-sent the 111 invoices; whether Meadowgate has received the manually sent invoice beyond mail-server acceptance.
- Not checked: whether the 64 invoices due 13 Nov and 90 due 15 Nov are all from pre-v8.3 schedules; whether re-saving works on a real scheduled run; whether all 340 schedules are pre-v8.3.
- Status history beyond the export's events was not supplied; the deadline assumes no "Pending customer" period.
- Not stated in the account record or policy: Support Duty Manager name (not needed unless breached).
