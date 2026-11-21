# Escalation handoff: QB-204518: Recurring invoices generated but never dispatched (pre-v8.3 schedules)

**Customer:** Harrow & Finch Accounting Ltd (HF-0192), Quillbill Practice, Enterprise support · **Priority:** P2 · **Next deadline:** 2026-11-13 09:14 UTC (resolution), breached by 8 d 9 h 19 min (as of 2026-11-21 18:33 UTC)

## Problem as currently understood
The 12 Nov 07:00 UTC recurring run for HF-0192 generated 112 invoices, and none was dispatched: all sit in "Queued - not dispatched" with zero send attempts and no errors. All 112 come from schedules created before the 10 Nov v8.3 release. Manual sending works, and re-saving one schedule restored dispatch in a test-mode run. The leading explanation is known issue KI-3381 (legacy schedules skip auto-send after v8.3), but the same cause is not confirmed. The customer has 340 schedules, with further runs on 13 Nov (64 invoices) and 15 Nov (90); the thread records nothing after 12 Nov 11:30 UTC.

Evidence:
- [Verified] Run at 07:00:03 UTC on 12 Nov generated 112 invoices; all 112 in dispatch state "Queued - not dispatched"; dispatcher shows 0 send attempts and no errors (Priya Nair internal note, 2026-11-12 10:20 UTC)
- [Verified] All 112 come from schedules created before 10 Nov (v8.3); the account's 3 post-10 Nov schedules were not due, so there is no comparison (Priya Nair internal note, 2026-11-12 10:20 UTC)
- [Verified] KI-3381 "Legacy recurring schedules skip auto-send after v8.3": opened 11 Nov, status Investigating, 2 other customers linked; symptoms match, same cause not confirmed (Priya Nair internal note, 2026-11-12 10:20 UTC); ticket linked to KI-3381 (event, 2026-11-12 11:30 UTC)
- [Verified] Manual Send of INV-2026-11-0457 at 10:15 was accepted by the recipient's mail server at 10:16 (Priya Nair internal note, 2026-11-12 10:20 UTC)
- [Verified] Re-saving "Meadowgate monthly retainer" without changes, then "Run now (test mode)", dispatched the test invoice within 40 seconds; not yet seen on a real scheduled run (Priya Nair internal note, 2026-11-12 10:20 UTC)
- [Verified] 340 active recurring schedules as of 1 Nov 2026 (account record, Products: Recurring Billing add-on)
- [Reported] About 110 invoices were due at 07:00; no client has received theirs; two clients have phoned (customer, 2026-11-12 09:14 UTC)
- [Reported] Customer made no settings changes (customer, 2026-11-12 09:14 UTC)
- [Reported] Next runs: 13 Nov 07:00 UTC with 64 invoices, 15 Nov (Sunday, time not stated) with 90 invoices (customer, 2026-11-12 09:14 and 10:52 UTC)
- [Reported] Customer would bulk-send the remaining 111 invoices themselves on the afternoon of 12 Nov (customer, 2026-11-12 10:52 UTC)
- [Inferred] The fault is in automatic dispatch for pre-v8.3 schedules, not in invoice generation or mail delivery (rests on: 112 generated, 0 send attempts, manual send delivered, all affected schedules pre-v8.3)
- [Inferred] Unless fixed, the 13 Nov and 15 Nov runs would fail the same way (rests on: all due schedules are pre-v8.3; re-save only tested on one schedule in test mode)

## Tried so far
| When | Who | Action | Result |
| --- | --- | --- | --- |
| 2026-11-12 09:41 UTC | Priya Nair (T1) | Asked for one affected invoice number and permission to send it as a test | Customer supplied INV-2026-11-0457 (Meadowgate Ltd) and gave permission at 09:58 |
| by 2026-11-12 10:20 UTC | Priya Nair (T1) | Read job log and dispatcher for HF-0192 | 112 invoices queued, 0 send attempts, no errors. Rules out a dispatcher error on send; the dispatcher never tried |
| by 2026-11-12 10:20 UTC | Priya Nair (T1) | Compared schedule creation dates against v8.3 release | All 112 from pre-10 Nov schedules; no post-v8.3 schedule was due, so no control case |
| by 2026-11-12 10:20 UTC | Priya Nair (T1) | Checked known issues | KI-3381 matches symptoms; same cause not confirmed |
| 2026-11-12 10:15 UTC | Priya Nair (T1) | Manual Send of INV-2026-11-0457 | Accepted by recipient mail server at 10:16. Rules out mail delivery as the cause for this invoice |
| by 2026-11-12 10:20 UTC | Priya Nair (T1) | Re-saved "Meadowgate monthly retainer" unchanged, then "Run now (test mode)" | Test invoice dispatched within 40 s (test mode only, sent to account owner) |
| 2026-11-12 10:34 UTC | Priya Nair (T1) | Gave workaround: filter "Queued", select up to 50, Send | Customer said they would bulk-send the 111 that afternoon; no result recorded |
| 2026-11-12 11:30 UTC | Priya Nair (T1) | Escalated to Tier 2, linked to KI-3381 | Status Escalated, priority P2 unchanged |

## Commitments to the customer
| Commitment (quoted) | Made by | When | Status |
| --- | --- | --- | --- |
| "I will email you an update by 16:00 UTC today with what they've found, even if that is only that they are still investigating." (resolves to 2026-11-12 16:00 UTC, Inferred) | Priya Nair (T1) | 2026-11-12 11:05 UTC | Overdue by 9 d 2 h 33 min: no update appears in the thread, which is described as the full history |
| "I'm escalating your ticket to our Product Engineering Support team now" | Priya Nair (T1) | 2026-11-12 11:05 UTC | Met: escalated 2026-11-12 11:30 UTC |
| "I'll make sure they know your next run is at 07:00 UTC tomorrow, 13 November, with 64 invoices." | Priya Nair (T1) | 2026-11-12 11:05 UTC | Met: stated in escalation note 2026-11-12 11:30 UTC |

No fix time was promised: the customer asked for a guarantee before the 13 Nov run (10:52 UTC) and Priya Nair declined ("I can't promise a fix time", 11:05 UTC).

Claimed by the customer, not found in the thread: none.

## Service level
- **Plan / support level:** [Verified] Quillbill Practice, support level Enterprise (account record, Plan and Support level)
- **Priority:** [Verified] P2, set at ticket creation and unchanged at escalation (events, 2026-11-12 09:14 and 11:30 UTC)
- **Target:** [Verified] policy 3.1: "Enterprise | P2 | 2 hours, 24x7 | 24 hours, 24x7"; 3.3: "Targets marked "24x7" run on calendar time." (support policy v4.2)
- **Clock start:** [Verified] policy 4.1 "The clock starts when the ticket is created": 2026-11-12 09:14 UTC (event). Policy time zone Europe/London is GMT = UTC in this period (1.1). No pause applies: the status was never "Pending customer" (4.2; events show New, Open, Escalated).
- **First response:** due 2026-11-12 11:14 UTC; [Verified] met at 09:41 UTC (Priya Nair reply), 27 min after creation.
- **Resolution:** due 2026-11-13 09:14 UTC. [Inferred] As of 2026-11-21 18:33 UTC: breached by 8 d 9 h 19 min (status not Resolved in the thread). For reference, at escalation (2026-11-12 11:30 UTC) it had 21 h 44 min left and would become "at risk" (under 25%, 6 h) at 2026-11-13 03:14 UTC (policy 4.5).
- **Update cadence:** [Verified] policy 7.1 "P2 tickets: an update at least once each business day"; Tier 2 owns customer updates and existing commitments from escalation (5.2). [Inferred] No update after 2026-11-12 11:05 UTC appears in the thread.
- **Breach notification:** [Verified] policy 5.3 requires the Support Duty Manager to be told of every breached P2 ticket; [Inferred] no such notification appears in the thread.

## Recommended next action
Tier 2 (Product Engineering Support, owner per policy 5.2) should, immediately, read the HF-0192 job log for the 13 Nov 07:00 UTC and 15 Nov runs and send Daniel Okafor the overdue update covering what happened to those runs and the status of KI-3381. The key unverified question is whether the 13 and 15 Nov invoices also stuck, since the customer's collections run from send date and nothing in the thread shows they were sent.

Follow-ups:
1. Notify the Support Duty Manager that this P2 is breached (policy 5.3).
2. Confirm with the KI-3381 engineers whether HF-0192 has the same cause, and whether re-saving holds on a real scheduled run (not test mode) or a bulk fix is possible for 340 schedules.

## Gaps and open questions
- **"As of" time:** the thread ends at 2026-11-12 11:30 UTC but this handoff is written at 2026-11-21 18:33 UTC. If later activity exists outside the supplied export (an update sent, the 13/15 Nov runs, a resolution), the overdue and breached statuses above may be wrong.
- **KI-3381 match unconfirmed:** the diagnosis rests on symptom similarity; no post-v8.3 schedule has run as a control.
- **Re-save workaround unproven:** tested on one schedule in test mode only; not seen on a real scheduled run, and impractical across 340 schedules (customer, 10:52 UTC).
- **Customer's bulk send of the 111 invoices:** reported as planned; not confirmed done.
- **Count discrepancy:** customer expected about 110 invoices; job log shows 112. Minor, unexplained.
- **15 Nov run time:** not stated in the thread.
- **Priority fit:** policy 2.2 defines P2 as "no practical workaround", and a manual bulk-send workaround exists (2.3, P3). [Inferred] Support kept P2; the customer's view is that per-run manual sending across 340 schedules is not realistic. Priority is support's call, noted only because it governs the clock.
- **No missing inputs:** thread, account record and policy were all supplied.
