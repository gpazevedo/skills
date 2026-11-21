# Escalation handoff: QB-204518, Harrow & Finch Accounting Ltd (HF-0192)

**Summary:** Invoices from pre-v8.3 recurring schedules are generated but never dispatched (112 stuck "Queued" from the 12 Nov 07:00 run), likely KI-3381 but unconfirmed. Most urgent: the 16:00 UTC 12 Nov update promised to the customer, then the next run at 07:00 UTC 13 Nov (64 invoices), ahead of the P2 resolution deadline at 09:14 UTC 13 Nov.
**Reference time:** 2026-11-12 11:30 UTC (latest thread entry)

## Problem as currently understood
Recurring runs for this account create invoices but the dispatcher never attempts to send them; manual sending works. All affected invoices come from schedules created before the 10 Nov v8.3 release, matching known issue KI-3381, though the shared cause is not confirmed. Re-saving one schedule restored sending in test mode only.
- [Verified] The 07:00:03 UTC run on 12 Nov generated 112 invoices, all "Queued - not dispatched", 0 send attempts, no errors (job log, Priya Nair internal note, 12 Nov 10:20). The customer's "around 110" (Daniel Okafor, 12 Nov 09:14) is superseded by the job log.
- [Verified] All 112 come from schedules created before 10 Nov (v8.3); the 3 schedules created after 10 Nov were not due, so there is no comparison (Priya Nair internal note, 12 Nov 10:20).
- [Verified] Ticket linked to KI-3381 "Legacy recurring schedules skip auto-send after v8.3" (Engineering, status Investigating, 2 other customers); symptoms match, cause not confirmed (Priya Nair internal note 10:20; system event 11:30).
- [Verified] Account has 340 active recurring schedules as of 1 Nov (account record).
- [Reported] No settings changed on the customer side; two clients have phoned about missing invoices (Daniel Okafor, 12 Nov 09:14).
- [Reported] Next runs: 13 Nov 07:00 UTC (64 invoices) and 15 Nov, a Sunday (90 invoices) (Daniel Okafor, 12 Nov 09:14 and 10:52).
- [Reported] Client payment terms run from the send date, so each day of delay defers collections (Daniel Okafor, 12 Nov 09:14).

Open questions:
- Is the cause KI-3381, and does Engineering have a fix or an ETA?
- Does a re-save fix a real scheduled run, not just "Run now (test mode)"?
- Can the re-save (or a fix) be applied in bulk to this account's pre-v8.3 schedules before 07:00 UTC 13 Nov?
- Do post-v8.3 schedules send normally on a real run?
- Did the customer's bulk send of the other 111 invoices succeed?

## Tried so far
- Job log and dispatcher inspection, by Priya Nair, 12 Nov 10:20: 112 queued, 0 send attempts, no errors.
- Known-issue search, by Priya Nair, 12 Nov 10:20: KI-3381 matches symptoms; not confirmed.
- Manual Send of INV-2026-11-0457 (customer approved, 09:58), by Priya Nair, 12 Nov 10:15: accepted by recipient's mail server at 10:16.
- Re-save of schedule "Meadowgate monthly retainer" plus "Run now (test mode)", by Priya Nair, 12 Nov 10:20 note: test invoice dispatched within 40 seconds; not yet seen on a real scheduled run.
- Bulk manual send of the remaining 111 invoices, by the customer, planned for the afternoon of 12 Nov (Daniel Okafor, 10:52): result not recorded. [Reported]

## Commitments to the customer
- "I'm escalating your ticket to our Product Engineering Support team now", Priya Nair, 12 Nov 11:05: met (system event, escalated to Tier 2 at 11:30).
- "I'll make sure they know your next run is at 07:00 UTC tomorrow, 13 November, with 64 invoices", Priya Nair, 12 Nov 11:05: met (escalation note, 11:30).
- "I will email you an update by 16:00 UTC today with what they've found, even if that is only that they are still investigating", Priya Nair, 12 Nov 11:05: outstanding, due 12 Nov 16:00 UTC (4h30m after reference time). Tier 2 now owns it (policy, section 5.2).
- Note: the customer asked for a guarantee of a fix before the 13 Nov run (10:52); Priya Nair declined ("I can't promise a fix time", 11:05). No fix date has been promised, and policy, section 6.2 bars one.

## Service level
- Tier: Enterprise (account record) | Priority: P2 (ticket, set at creation 09:14 and unchanged at escalation 11:30)
- Target: first response 2 hours, 24x7; resolution 24 hours, 24x7 (policy, section 3.1; calendar time per section 3.3)
- First response: due 12 Nov 11:14 UTC; met at 09:41 by Priya Nair (27 minutes after creation; section 1.4).
- Resolution deadline: 2026-11-13 09:14 UTC, from creation 12 Nov 09:14 (section 4.1) + 24 calendar hours, no pauses (status was never "Pending customer", section 4.2).
- Status: open, within target, 21h44m remaining. Becomes "at risk" when under 6 hours (25% of 24h) remain, at 13 Nov 03:14 UTC (section 4.5). If breached, the Support Duty Manager must be told (section 5.3).
- Updates: P2 requires at least one customer update each business day (section 7.1).

## Recommended next action
Ask the KI-3381 Engineering owners, today, to confirm whether a re-save (or a fix) restores sending on a real scheduled run and whether it can be applied in bulk to HF-0192's pre-v8.3 schedules before 07:00 UTC on 13 Nov, because the job log shows only pre-v8.3 schedules affected and the re-save test worked only in test mode on one of 340 schedules. Serves: the 16:00 UTC update commitment, the 13 Nov 07:00 UTC run (64 invoices), and the resolution deadline of 13 Nov 09:14 UTC.
Tell the customer: by 16:00 UTC on 12 Nov, email Daniel Okafor what Engineering has found, without a fix date (policy, section 6.2); if no bulk fix will be applied before 07:00 UTC 13 Nov, tell him tomorrow's 64 invoices will likely queue again and can be sent the same way as today (filter "Queued", up to 50 at a time, Send), and confirm whether his bulk send of today's 111 went through.
