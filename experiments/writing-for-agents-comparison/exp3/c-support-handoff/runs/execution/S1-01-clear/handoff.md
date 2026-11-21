# Escalation handoff: QB-204518 - Recurring invoices from pre-v8.3 schedules created but not sent

Customer: Harrow & Finch Accounting Ltd (HF-0192) | Tier: Enterprise (account record) | Priority: P2 (set on case, event 2026-11-12 09:14 UTC; unchanged at escalation 11:30 UTC) | Prepared: as at 2026-11-12 11:30 UTC, the last entry in the thread export (the case does not state a current time; re-check status against the actual time)

## Service level
Policy 3.1, Enterprise P2: "2 hours, 24x7" first response, "24 hours, 24x7" resolution | Resolution deadline: 2026-11-13 09:14 UTC | Status at 2026-11-12 11:30 UTC: Within target: 21 h 44 min remaining (first response: Met)
Clock starts "when the ticket is created" (policy 4.1): 2026-11-12 09:14 UTC + 24 calendar hours ("24x7" runs on calendar time, policy 3.3) = 2026-11-13 09:14 UTC. No paused time: status went New, Open, Escalated and was never "Pending customer" (policy 4.2). First response due 11:14 UTC; Priya Nair replied at 09:41 UTC (27 min). "At risk" once less than 25% remains (policy 4.5), i.e. from 2026-11-13 03:14 UTC. If breached, the Support Duty Manager must be told (policy 5.3). Policy 5.2: from escalation, Tier 2 owns customer updates and commitments already made.

## Problem as currently understood
The 07:00 UTC recurring run on 12 Nov generated 112 invoices that are stuck in "Queued - not dispatched" with no send attempt and no error. All 112 come from schedules created before the v8.3 release on 10 Nov, which matches known issue KI-3381 (Investigating), but the same cause is not confirmed. Manual send works, and re-saving one schedule restored sending in test mode only. The customer has 340 schedules and further runs on 13 Nov 07:00 UTC (64 invoices) and 15 Nov (90 invoices).
- [Verified] Job log: 07:00:03 UTC run generated 112 invoices, all "Queued - not dispatched", dispatcher shows 0 send attempts and no errors (Priya Nair, internal note, 2026-11-12 10:20 UTC)
- [Verified] All 112 come from schedules created before 10 Nov; the account's 3 schedules created after 10 Nov were not due, so no comparison yet (Priya Nair, 2026-11-12 10:20 UTC)
- [Verified] Symptoms match KI-3381 "Legacy recurring schedules skip auto-send after v8.3" (opened 11 Nov, Investigating, 2 other customers linked); "Not confirmed as the same cause" (Priya Nair, 2026-11-12 10:20 UTC); ticket linked to KI-3381 (event, 2026-11-12 11:30 UTC)
- [Reported] Around 110 invoices were due to email at 07:00; no client has received theirs; two clients have phoned (Daniel Okafor, 2026-11-12 09:14 UTC)
- [Reported] Customer has not changed any settings (Daniel Okafor, 2026-11-12 09:14 UTC)
- [Reported] Customer has 340 schedules; 13 Nov 07:00 run has 64 invoices, Sunday 15 Nov run has 90 (Daniel Okafor, 2026-11-12 10:52 UTC). Account record lists 340 active schedules as of 1 Nov 2026.
- [Reported] Client payment terms run from the send date, so delay pushes back collections (Daniel Okafor, 2026-11-12 09:14 UTC)

## What has been tried
1. Manual Send of INV-2026-11-0457 (Meadowgate Ltd) from the invoice list, with customer permission (Daniel Okafor, 09:58 UTC) - Priya Nair, 2026-11-12 10:15 UTC - Resolved for that invoice: accepted by recipient's mail server 10:16 UTC [Verified, Priya Nair 10:20 UTC]
2. Re-saved schedule "Meadowgate monthly retainer" without changes, then "Run now (test mode)" (sends to account owner only) - Priya Nair, before 2026-11-12 10:20 UTC - Partial: test invoice dispatched within 40 seconds; not yet seen on a real scheduled run [Verified, Priya Nair 10:20 UTC]
3. Customer to bulk-send the remaining 111 queued invoices from the invoice list "this afternoon" - Daniel Okafor, stated 2026-11-12 10:52 UTC - Unknown: no result recorded [Reported]
4. Escalated to Tier 2 and linked to KI-3381 - Priya Nair, 2026-11-12 11:30 UTC - Unknown: no result recorded

## Commitments to the customer
- "I'm escalating your ticket to our Product Engineering Support team now" - Priya Nair, 2026-11-12 11:05 UTC - due now - met (escalation event 11:30 UTC)
- "I'll make sure they know your next run is at 07:00 UTC tomorrow, 13 November, with 64 invoices." - Priya Nair, 2026-11-12 11:05 UTC - due none stated - met (stated in escalation note, 11:30 UTC)
- "I will email you an update by 16:00 UTC today with what they've found, even if that is only that they are still investigating." - Priya Nair, 2026-11-12 11:05 UTC - due 2026-11-12 16:00 UTC - open (now owned by Tier 2, policy 5.2)
- Not a commitment: "I can't promise a fix time, because that depends on what engineering finds." (Priya Nair, 11:05 UTC) in reply to the customer's request to "guarantee this will be fixed before tomorrow morning's run" (Daniel Okafor, 10:52 UTC). No fix time has been promised.
Claimed by customer, not found in thread: none

## Open questions
- Has the customer bulk-sent the other 111 invoices from 12 Nov? No result recorded.
- Was the 16:00 UTC update sent? Nothing after 11:30 UTC in the export.
- Does the re-save fix hold on a real scheduled run, not just test mode? Not yet observed.
- Is this KI-3381? Engineering has not confirmed the cause, a fix, or a fix time.
- Is there a bulk or backend way to fix all affected schedules? The customer says re-saving 340 by hand "isn't realistic".
- Which of the 64 (13 Nov) and 90 (15 Nov) invoices come from pre-10 Nov schedules? Not shown.
- What time is the 15 Nov run? The thread does not say.
- Do the 3 schedules created after 10 Nov auto-send? None has run yet.
- Is the schedule count 340 or 343? The account record says 340 active as of 1 Nov, the customer says 340 now, and Priya's note mentions 3 created after 10 Nov.

## Recommended next action
With the Engineering owner of KI-3381, confirm whether HF-0192's 12 Nov failure is KI-3381, and whether the pre-10 Nov schedules due in the 13 Nov 07:00 UTC run can be fixed in bulk (backend fix or bulk re-save) before that run. Reason: the job log shows all 112 stuck invoices came from pre-v8.3 schedules with 0 send attempts (Priya Nair, 10:20 UTC), and a re-save restored sending in test mode for one schedule. Hand-fixing 340 schedules is not practical for the customer. Must be done before 2026-11-13 07:00 UTC; the SLA resolution deadline is 2026-11-13 09:14 UTC.
- Follow-up 1: send the committed customer update by 2026-11-12 16:00 UTC (the nearest deadline). State the findings or "still investigating". Do not give a fix time (policy 6.2).
- Follow-up 2: if there is no fix before 07:00 UTC, tell the customer before the run to plan a bulk manual send from the "Queued" filter, up to 50 at a time. After the run, check the job log for the 13 Nov invoices' dispatch state.
