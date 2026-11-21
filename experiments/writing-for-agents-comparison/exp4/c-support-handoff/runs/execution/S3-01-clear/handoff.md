# Escalation handoff: QB-204518, Harrow & Finch Accounting Ltd (HF-0192)

**Service level:** within target, resolution deadline 2026-11-13 09:14 UTC, Enterprise P2 resolution "24 hours, 24x7" (policy 3.1); the next scheduled run (13 Nov 07:00 UTC) falls about 2 hours before it
**Next action:** Confirm the cause on HF-0192's schedules and fix or bulk-repair them before the 13 Nov 07:00 UTC run (64 invoices).

## Problem as currently understood
The 07:00 UTC recurring run on 12 Nov generated 112 invoices that all sit in "Queued - not dispatched" with no send attempts, apparently because pre-v8.3 schedules skip auto-send (known issue KI-3381, symptoms match but cause not confirmed for this account). The customer's urgent concern has shifted from today's invoices (manually sendable) to the 13 Nov and 15 Nov runs, across 340 schedules.

Evidence:
- [Reported] Around 110 invoices should have been emailed at 07:00, all show "Queued", and no client has received theirs (Daniel Okafor, 2026-11-12 09:14)
- [Verified] The run at 07:00:03 UTC generated 112 invoices, all "Queued - not dispatched", dispatcher shows 0 send attempts and no errors (Priya Nair, job log for HF-0192, internal note 2026-11-12 10:20)
- [Verified] All 112 come from schedules created before 10 Nov (v8.3 release); 3 schedules created after 10 Nov exist, none due today, so no comparison yet (Priya Nair, account job log, 10:20)
- [Verified] Manual Send of INV-2026-11-0457 at 10:15 was accepted by the recipient's mail server at 10:16 (Priya Nair, delivery log, 10:20)
- [Verified] Re-saving schedule "Meadowgate monthly retainer" unchanged, then "Run now (test mode)", dispatched in 40 seconds; test mode sends only to the account owner; not seen on a real scheduled run (Priya Nair, 10:20)
- [Verified] KI-3381 "Legacy recurring schedules skip auto-send after v8.3" opened by Engineering 11 Nov, status Investigating, 2 other customers linked; not confirmed as the same cause (Priya Nair, known-issue record, 10:20)
- [Reported] No settings were changed on the customer side (Daniel Okafor, 09:14)
- [Reported] Two clients have already rung to ask where their invoice is; payment terms run from send date (Daniel Okafor, 09:14)
- [Reported] The 13 Nov run has 64 invoices and the 15 Nov run has 90; the account has 340 schedules (Daniel Okafor, 10:52; account record shows 340 active schedules as of 1 Nov)
- [Reported] Customer will bulk-send today's 111 remaining invoices themselves this afternoon (Daniel Okafor, 10:52); not yet confirmed done
- Conflict: Daniel reported "around 110" invoices; the job log verifies 112 (111 still queued after the manual test send). Minor, but use 112/111 as the figures.

## Tried so far
- 2026-11-12 09:41, Priya Nair: asked for one invoice number and consent to send a test -> customer agreed 09:58
- 2026-11-12 10:15, Priya Nair: manual Send of INV-2026-11-0457 -> accepted by recipient mail server 10:16
- 2026-11-12 ~10:15-10:20, Priya Nair: re-saved schedule "Meadowgate monthly retainer", ran "Run now (test mode)" -> dispatched within 40 seconds (test mode only)
- 2026-11-12 10:34, Priya Nair: gave customer bulk-send workaround (filter "Queued", select up to 50, Send) -> customer plans to apply it this afternoon; result not recorded
- 2026-11-12 11:30, Priya Nair: escalated to Tier 2 and linked KI-3381 -> pending

## Commitments to the customer
- "I will email you an update by 16:00 UTC today with what they've found, even if that is only that they are still investigating." (Priya Nair, 2026-11-12 11:05), due 16:00 UTC 12 Nov, open (Tier 2 owns it from escalation, policy 5.2)
- "I'll make sure they know your next run is at 07:00 UTC tomorrow, 13 November, with 64 invoices." (Priya Nair, 2026-11-12 11:05), no due time stated; escalation note at 11:30 records the run time and count, so met
- Not a commitment: Priya explicitly declined to promise a fix time ("I can't promise a fix time", 11:05), consistent with policy 6.2. No credit or refund has been offered (account record: none).

## Service level
- Plan: Quillbill Practice, support level Enterprise (account record; policy 1.3 "the level recorded in the customer's account record")
- Priority: P2, set at creation and unchanged at escalation (ticket event 09:14; 11:30). Mismatch to consider: policy 2.2 P2 is "no practical workaround", 2.3 P3 is "a function is impaired but a practical workaround exists". A manual bulk send is a workaround for today's invoices but not practical for ongoing automatic sends across 340 schedules, so P2 looks defensible. Per 2.5 any change takes effect only when an agent records it; do not change it without recording.
- Target: "Enterprise | P2 | 2 hours, 24x7 | 24 hours, 24x7" (3.1); "Targets marked 24x7 run on calendar time" (3.3). First response met: first agent reply 09:41, 27 minutes after creation (automated acknowledgements do not count, 1.4; none shown).
- Clock: started 2026-11-12 09:14 UTC, ticket creation ("The clock starts when the ticket is created", 4.1); never in "Pending customer", so no pauses (4.2); business-hours rules not applicable (24x7). Timestamps are UTC (1.2).
- Deadline: 2026-11-13 09:14 UTC as of now = 2026-11-12 11:30 UTC (user-supplied as-of time in the ticket export). Elapsed 2h16m of 24h; 21h44m remain, above the 25% (6h) at-risk threshold (4.5), so within target. It becomes "at risk" at 03:14 UTC on 13 Nov. Resolution requires a fix or workaround plus status Resolved (1.5); status is currently Escalated.
- Update cadence: P2 needs "an update at least once each business day" (7.1). 12 Nov is covered by the 16:00 commitment; 13 Nov is also a business day.
- Duty Manager (5.3) must be told only if the P2 ticket is breached; not breached.

## Recommended next action
Have Tier 2 establish whether the fault will recur on the 13 Nov 07:00 UTC run (64 invoices) and, if so, repair or bulk-reset HF-0192's legacy schedules (or get an Engineering fix) before 07:00. This comes first because the next run precedes the SLA deadline by about 2 hours, the customer asked for a guarantee that cannot be given, and the only evidence that re-saving works is a test-mode run. Do not promise a fix date to the customer (6.2); promise only actions and update times (6.1).

Open questions:
- Is the HF-0192 cause the same as KI-3381? Does re-saving fix a real scheduled run, not just test mode?
- Which of the 340 schedules predate 10 Nov, and is a bulk re-save or backend repair possible?
- Did the customer bulk-send the 111 queued invoices this afternoon? Any duplicates risk once dispatch is fixed (queued invoices may send automatically after a fix)?
- Should priority stay P2 (see Service level)?

Next customer update due: 16:00 UTC 12 Nov (commitment by Priya Nair, 11:05); then at least once on 13 Nov (policy 7.1)
