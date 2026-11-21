# Escalation handoff: QB-204518, Harrow & Finch Accounting Ltd (HF-0192)

**In one line:** 112 invoices from pre-v8.3 recurring schedules sat "Queued - not dispatched" after the 12 Nov 07:00 UTC run (suspected KI-3381); the next run is 13 Nov 07:00 UTC (64 invoices, reported), a customer update is promised by 12 Nov 16:00 UTC, and the P2 Enterprise resolution deadline is 13 Nov 09:14 UTC.

## Problem as currently understood
- [verified] The recurring run at 07:00:03 UTC on 12 Nov generated 112 invoices; all 112 are in dispatch state "Queued - not dispatched", with 0 send attempts and no errors in the dispatcher (evidence: job log for HF-0192 read by Priya Nair, Tier 1, internal note 2026-11-12 10:20 UTC).
- [verified] All 112 come from schedules created before 10 Nov (the v8.3 release). The account has 3 schedules created after 10 Nov; none was due on 12 Nov, so there is no post-v8.3 comparison yet (evidence: same internal note, Priya Nair, 2026-11-12 10:20 UTC).
- [verified] Manual send works: INV-2026-11-0457 sent manually from the invoice list at 10:15; delivery log shows it accepted by the recipient's mail server at 10:16 (evidence: Test 1, Priya Nair, internal note 2026-11-12 10:20 UTC).
- [verified, test mode only] After re-saving schedule "Meadowgate monthly retainer" without changes, "Run now (test mode)" (sends only to the account owner) dispatched within 40 seconds (evidence: Test 2, Priya Nair, internal note 2026-11-12 10:20 UTC). Not yet seen on a real scheduled run.
- [verified] The account has 340 active Recurring Billing schedules as of 1 November 2026 (evidence: account record, Products). The customer also says 340 (reported, 2026-11-12 10:52 UTC).
- [verified] Support level Enterprise, plan Quillbill Practice, data region UK, primary technical contact Daniel Okafor, CSM Elena Marsh (evidence: account record).
- [reported] Not one client appears to have received their invoice, and two clients have already rung to ask where it is (source: Daniel Okafor, customer, 2026-11-12 09:14 UTC).
- [reported] The customer has not changed any settings on their side (source: Daniel Okafor, 2026-11-12 09:14 UTC).
- [reported] The customer's clients' payment terms run from the send date, so each day of delay pushes back collections (source: Daniel Okafor, 2026-11-12 09:14 UTC).
- [reported] Next runs: 13 Nov 07:00 UTC with 64 invoices, and Sunday 15 Nov with 90 invoices (source: Daniel Okafor, 2026-11-12 09:14 and 10:52 UTC). The 15 Nov run time is not stated; the customer's 09:14 message implies runs are at 07:00.
- [reported] The customer will bulk-send the remaining 111 invoices from 12 Nov themselves "this afternoon" (source: Daniel Okafor, 2026-11-12 10:52 UTC). No result recorded.
- [suspected] Cause is known issue KI-3381 "Legacy recurring schedules skip auto-send after v8.3" (opened by Engineering 11 Nov, status Investigating, 2 other customers linked) (held by: Priya Nair; basis: symptoms match and all affected schedules are pre-v8.3; "Not confirmed as the same cause", internal note 2026-11-12 10:20 UTC). Ticket was linked to KI-3381 at escalation, 2026-11-12 11:30 UTC.
- [suspected] Re-saving a schedule clears the fault for that schedule (held by: Priya Nair; basis: Test 2 in test mode only; "Not yet seen on a real scheduled run").
- Conflicts: customer says "around 110 invoices" (09:14 UTC); the job log shows 112 (Priya Nair, 10:20 UTC). The job log figure is the checked one. No conflict on account facts (the customer did not state a plan or tier).

## Tried so far
| What was tried | Who, when | Result |
|---|---|---|
| Read HF-0192 job log and dispatcher for the 12 Nov 07:00 run | Priya Nair (Tier 1), recorded 2026-11-12 10:20 UTC | 112 invoices generated, all "Queued - not dispatched", 0 send attempts, no errors; all from pre-10 Nov schedules |
| Checked known issues | Priya Nair, recorded 2026-11-12 10:20 UTC | KI-3381 matches symptoms; not confirmed as same cause |
| Test 1: manual Send on INV-2026-11-0457 (to Meadowgate Ltd) from the invoice list, with customer's permission (09:58 UTC) | Priya Nair, 2026-11-12 10:15 UTC | Accepted by recipient's mail server at 10:16 UTC |
| Test 2: re-saved schedule "Meadowgate monthly retainer" without changes, then "Run now (test mode)" | Priya Nair, before 2026-11-12 10:20 UTC (exact time not recorded) | Test invoice dispatched within 40 seconds; real scheduled run not yet observed |
| Customer to bulk-send the other 111 queued invoices (filter "Queued", up to 50 at a time, Send), as suggested by support at 10:34 UTC | Daniel Okafor (customer), planned for afternoon of 2026-11-12 | No result recorded |

## Commitments to the customer
| Commitment (quoted) | Made by | When | Due | Status |
|---|---|---|---|---|
| "I'm escalating your ticket to our Product Engineering Support team now" | Priya Nair (Tier 1) | 2026-11-12 11:05 UTC | Immediately | Met: escalated to Tier 2 at 2026-11-12 11:30 UTC |
| "I'll make sure they know your next run is at 07:00 UTC tomorrow, 13 November, with 64 invoices." | Priya Nair (Tier 1) | 2026-11-12 11:05 UTC | No date given (with the escalation) | Met: escalation note at 11:30 UTC states "next runs 13 Nov 07:00 UTC (64 invoices)" |
| "I will email you an update by 16:00 UTC today with what they've found, even if that is only that they are still investigating." | Priya Nair (Tier 1) | 2026-11-12 11:05 UTC | 2026-11-12 16:00 UTC | Pending (4h30m remaining as of 11:30 UTC). Under policy 5.2, Tier 2 now owns this commitment |

Not commitments: the customer asked "Can you guarantee this will be fixed before tomorrow morning's run?" (10:52 UTC); Priya replied "I can't promise a fix time" (11:05 UTC). No fix date, credit or refund has been offered (account record: "Open credits: None", "Refunds: None").

## Service level
- Tier: Enterprise (account record, "Support level: Enterprise"; policy 1.3: support level is "the level recorded in the customer's account record")
- Priority/severity: P2 (ticket event 2026-11-12 09:14 UTC "Priority: P2"; unchanged at escalation 11:30 UTC "Priority: P2 (unchanged)")
- Target: First response "2 hours, 24x7"; Resolution "24 hours, 24x7" (policy 3.1, row "Enterprise | P2"). Policy 3.3: "Targets marked "24x7" run on calendar time."
- Clock rule: "The clock starts when the ticket is created." (4.1). "The clock is paused only while the ticket status is "Pending customer"." (4.2). Calendar time, not business hours (3.3). The status history in the thread is New (09:14) → Open (09:41) → Escalated (11:30); it never enters "Pending customer", so no paused time.
- Deadline:
  - First response: 2026-11-12 11:14 UTC (09:14 + 2h). Met: Priya Nair replied at 09:41 UTC (27 minutes).
  - Resolution: 2026-11-13 09:14 UTC (UTC = Europe/London GMT in this period, policy 1.1) (arithmetic: created 2026-11-12 09:14 UTC + 24h calendar, 0h paused = 2026-11-13 09:14 UTC). This falls 2h14m after the 13 Nov 07:00 UTC run.
  - "At risk" threshold (policy 4.5, less than 25% of 24h = 6h remaining): from 2026-11-13 03:14 UTC.
- Status: open (within target), 21h44m remaining to resolution deadline, as of 2026-11-12 11:30 UTC (the last thread timestamp, used as "now" because the thread is the only time reference for the case; see Gaps).
- Related policy terms:
  - Updates: "P2 tickets: an update at least once each business day." (7.1)
  - Ownership: "From escalation, Tier 2 owns the ticket, including customer updates and any commitments already made to the customer." (5.2)
  - Breach: "The Support Duty Manager must be told of ... every P2 ticket that is breached." (5.3)
  - Resolution means "a fix or a workaround that restores the affected function and the ticket status has been set to Resolved." (1.5)
  - Fix dates: agents "must not promise a fix date for a product defect" (6.2).

## Recommended next action
Take Priya's job-log evidence (HF-0192, 12 Nov 07:00:03 UTC run, 112 invoices "Queued - not dispatched", 0 send attempts, no errors, all from pre-10 Nov schedules, re-save plus test-mode run dispatched for "Meadowgate monthly retainer") to the Engineering owners of KI-3381 now, and ask them two things: (a) is this the KI-3381 signature, and (b) is re-saving a schedule a valid workaround on real scheduled runs, and can it be applied in bulk to HF-0192's pre-v8.3 schedules, at least the ones due at 13 Nov 07:00 UTC?

What each outcome means:
- **Confirmed KI-3381, bulk re-save possible:** apply it to the schedules due 13 Nov before 07:00 UTC, then read the job log just after 07:00 UTC to confirm the 64 invoices dispatch. That turns the re-save theory from suspected to verified on a real run, and it may count as a workaround that restores the function (policy 1.5) before the 09:14 UTC deadline. Repeat for the 15 Nov run and the remaining schedules.
- **Confirmed KI-3381, no bulk workaround:** the customer must manually send the 13 Nov invoices (and the 15 Nov invoices, a Sunday) as on 12 Nov; tell them so, without giving a fix date (policy 6.2). Expect the resolution target to breach at 2026-11-13 09:14 UTC; if it does, tell the Support Duty Manager (policy 5.3).
- **Not KI-3381:** treat it as a separate defect in the dispatcher for this account and investigate why queued invoices get no send attempt, using the 112 invoices as the sample.

Customer update due first: the email promised by **2026-11-12 16:00 UTC** (now owned by Tier 2, policy 5.2). It must go out by then whatever Engineering has found, and should say what will happen with the 13 Nov 07:00 UTC run (re-save applied, or manual send needed). A further update is due on 13 Nov (policy 7.1, one per business day for P2).

## Gaps
- "Now": no current time came with the case, so this handoff uses the last thread timestamp (2026-11-12 11:30 UTC). The session clock reads 2026-11-21 UTC; if that is the real current date, the 16:00 UTC update commitment is overdue and the resolution target is breached by about 8 days, but the export contains no events after 11:30 UTC on 12 Nov, so whether the update was sent, the 13 and 15 Nov runs dispatched, or the ticket was resolved is unknown. Check the live ticket before acting.
- The re-save workaround has only been seen in test mode for one schedule; no real scheduled run has been observed after a re-save.
- Whether the schedules due on 13 Nov (64 invoices) and 15 Nov (90 invoices) are pre- or post-v8.3 has not been checked; if any of the 3 post-10 Nov schedules is due, that run gives the first direct comparison.
- The number of invoices in the next runs (64, 90) and the 15 Nov run time are reported by the customer, not checked in the scheduler.
- Customer's bulk send of the other 111 invoices on 12 Nov: no result recorded. Nobody has confirmed the 111 went out.
- That no client received an invoice and that no settings were changed are reported only; no audit of HF-0192's settings history is recorded.
- KI-3381's details (root cause, whether the 2 linked customers show the same 0-send-attempt pattern, any planned fix) are not in the supplied material.
- Priority: the ticket is P2. Policy 2.2 defines P2 as a major function failing with "no practical workaround", and a manual bulk-send workaround now exists (policy 2.3, P3). Nobody has recorded a priority change; any change is support's decision (2.5) and would change the resolution target (4.4).
- Whether Elena Marsh (CSM) or Ruth Finch (contract contact) has been told: not stated in the thread.
