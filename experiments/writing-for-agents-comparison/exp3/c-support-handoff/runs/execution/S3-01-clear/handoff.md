# Escalation handoff: QB-204518, Harrow & Finch Accounting Ltd (HF-0192)

**Service level:** within target, resolution deadline 2026-11-13 09:14 UTC (at risk from 03:14 UTC), Enterprise P2 resolution "24 hours, 24x7" (policy 3.1)
**Next action:** Before 16:00 UTC today, get the KI-3381 engineering owners to confirm whether HF-0192 has the same cause and whether re-saving schedules is a safe interim fix for the 64 invoices due at 07:00 UTC on 13 Nov.

## Problem as currently understood
Since the v8.3 release (10 Nov), recurring schedules created before that release generate invoices but never dispatch them: the 07:00 UTC run on 12 Nov created 112 invoices that sit "Queued - not dispatched" with no send attempts and no errors. The symptoms match known issue KI-3381, but the cause is not confirmed. This has moved on from the opening report ("invoices show Queued, nothing sent"): Tier 1's log check and tests showed that dispatch is never attempted, that only pre-v8.3 schedules are affected, that manual send works, and that re-saving one schedule restored dispatch in test mode.

Evidence:
- [Verified] The recurring run at 07:00:03 UTC on 12 Nov generated 112 invoices, all in dispatch state "Queued - not dispatched"; the dispatcher shows 0 send attempts and no errors (Priya Nair, HF-0192 job log, internal note 2026-11-12 10:20 UTC)
- [Verified] All 112 invoices come from schedules created before 10 Nov (v8.3 release). The account has 3 schedules created after 10 Nov; none was due on 12 Nov, so there is no direct comparison yet (Priya Nair, job log, 2026-11-12 10:20 UTC)
- [Verified] Known issue KI-3381 "Legacy recurring schedules skip auto-send after v8.3", opened by Engineering 11 Nov, status Investigating, 2 other customers linked; symptoms match, same cause not confirmed (Priya Nair, known-issues list, 2026-11-12 10:20 UTC). Ticket linked to KI-3381 at escalation (event, 2026-11-12 11:30 UTC)
- [Verified] Manual Send works: INV-2026-11-0457 sent from the invoice list at 10:15, accepted by the recipient's mail server at 10:16 (Priya Nair, delivery log, 2026-11-12 10:20 UTC)
- [Verified] Re-saving schedule "Meadowgate monthly retainer" without changes, then "Run now (test mode)", dispatched the test invoice within 40 seconds. Seen in test mode only, not yet on a real scheduled run (Priya Nair, test, 2026-11-12 10:20 UTC)
- [Verified] The account has 340 active Recurring Billing schedules as of 1 Nov 2026 (account record)
- [Reported] Around 110 invoices should have been emailed at 07:00; not one client has received theirs; two clients have rung to ask (Daniel Okafor, 2026-11-12 09:14 UTC)
- [Reported] No settings were changed on the customer's side (Daniel Okafor, 2026-11-12 09:14 UTC)
- [Reported] Clients' payment terms run from the send date, so each day of delay pushes back collections (Daniel Okafor, 2026-11-12 09:14 UTC)
- [Reported] Next runs: 13 Nov 07:00 with 64 invoices, and Sunday 15 Nov with 90 invoices (Daniel Okafor, 2026-11-12 09:14 and 10:52 UTC; repeated, not checked, in Priya Nair's escalation note 11:30 UTC)
- [Reported] The customer will bulk-send the remaining 111 invoices themselves on the afternoon of 12 Nov (Daniel Okafor, 2026-11-12 10:52 UTC)
- Conflict (minor): the customer reported "around 110" invoices; the job log shows 112. The log figure stands; 111 remain after the manual test send.
- Note: Priya's customer message (10:34) says re-saving "appeared to restore automatic sending"; her own note (10:20) limits this to a test-mode run. Automatic sending after a re-save has not been seen on a real scheduled run.

## Tried so far
- 2026-11-12 10:15 UTC, Priya Nair: manually sent INV-2026-11-0457 (Meadowgate Ltd) from the invoice list, with the customer's permission -> accepted by the recipient's mail server at 10:16
- 2026-11-12 ~10:20 UTC, Priya Nair: re-saved schedule "Meadowgate monthly retainer" without changes, then "Run now (test mode)" -> test invoice dispatched within 40 seconds; not yet seen on a real scheduled run
- 2026-11-12 10:34 UTC, Priya Nair: gave customer the bulk-send workaround (filter "Queued", select up to 50, Send) -> customer said they would bulk-send the 111 that afternoon; result not recorded
- 2026-11-12 11:30 UTC, Priya Nair: escalated to Tier 2 and linked to KI-3381 -> ticket status Escalated, priority P2 unchanged

## Commitments to the customer
Tier 2 now owns these (policy 5.2: "From escalation, Tier 2 owns the ticket, including customer updates and any commitments already made to the customer").

- "I will email you an update by 16:00 UTC today with what they've found, even if that is only that they are still investigating." (Priya Nair, 2026-11-12 11:05 UTC), due 16:00 UTC today (12 Nov), open
- "I'm escalating your ticket to our Product Engineering Support team now" (Priya Nair, 2026-11-12 11:05 UTC), due now, met (escalation event 11:30 UTC)
- "I'll make sure they know your next run is at 07:00 UTC tomorrow, 13 November, with 64 invoices." (Priya Nair, 2026-11-12 11:05 UTC), due at escalation, met (stated in escalation note 11:30 UTC)
- Not a commitment: the customer asked "Can you guarantee this will be fixed before tomorrow morning's run?" (10:52); Priya declined: "I can't promise a fix time" (11:05). No fix time has been promised; policy 6.2 bars promising one.

## Service level
- Plan: Quillbill Practice, support level Enterprise (account record; policy 1.3: "A customer's support level ... is the level recorded in the customer's account record")
- Priority: P2 (set at ticket creation 09:14 UTC, unchanged at escalation 11:30 UTC). Mismatch flag: policy 2.2 defines P2 as "a major function, such as invoice sending ... does not work and there is no practical workaround", while 2.3 defines P3 as "a function is impaired but a practical workaround exists". A verified workaround exists (manual bulk send from the invoice list, up to 50 at a time), and the customer accepted it for 12 Nov, though they say re-saving 340 schedules is not realistic. Whether the workaround is "practical" for recurring daily runs is a judgement for support (policy 2.5); the recorded P2 stands until an agent changes it. If changed to P3, policy 4.4 makes the resolution target "30 business hours", counted from creation, giving a deadline of Tue 17 Nov 2026 09:14 UTC.
- Target: "Enterprise | P2 | 2 hours, 24x7 | 24 hours, 24x7" (policy 3.1); "Targets marked '24x7' run on calendar time" (3.3). First response met: Priya Nair replied at 09:41 UTC, 27 minutes after creation (policy 1.4).
- Clock: started at ticket creation, 2026-11-12 09:14 UTC ("The clock starts when the ticket is created", 4.1). No pauses: the status has never been "Pending customer" (New -> Open -> Escalated) (4.2). Calendar time, so business hours do not apply. At-risk threshold: "less than 25% of its resolution target remains" (4.5), i.e. under 6 hours, from 2026-11-13 03:14 UTC.
- Deadline: 2026-11-13 09:14 UTC (Europe/London is GMT = UTC in this period, policy 1.1). As of now = 2026-11-12 11:30 UTC (latest timestamp in the thread; no "now" given by the user), 21 h 44 min remain: within target. Note that the next run (13 Nov 07:00 UTC) falls inside the at-risk window and before the deadline. If breached, the Support Duty Manager must be told (5.3).

## Recommended next action
Get the KI-3381 engineering owners to confirm, before 16:00 UTC today, whether HF-0192's stuck invoices share KI-3381's cause and whether re-saving a pre-v8.3 schedule is a safe interim fix (that is, it restores dispatch on a real scheduled run, not just in test mode). If it is, arrange for the schedules due at 07:00 UTC on 13 Nov (64 invoices) to be re-saved before that run, with the customer's agreement, and watch that run's dispatch log. This comes first because it is the most decisive open question: it turns the KI-3381 match and the re-save fix from unconfirmed into verified. It also covers the two nearest deadlines: the 16:00 UTC update commitment and the 07:00 run, which lands inside the P2 at-risk window three hours before the resolution deadline.

Open questions:
- Is the cause the same as KI-3381, and does Engineering have a fix or ETA (not to be promised to the customer, policy 6.2)?
- Does a re-saved schedule dispatch on a real scheduled run, not only in test mode? Can re-saving be done in bulk on Quillbill's side for 340 schedules?
- Did the customer bulk-send the remaining 111 invoices on 12 Nov? If a backend fix later releases the "Queued" invoices, could clients receive duplicates?
- Are the 64 (13 Nov) and 90 (15 Nov) invoice counts confirmed from the schedule data? Do any of the 3 post-v8.3 schedules run on 13 or 15 Nov, giving a comparison?
- Should the priority stay P2 given the manual bulk-send workaround (policy 2.2 vs 2.3)?

Next customer update due: 16:00 UTC on 12 Nov 2026 (Priya Nair's commitment, now owned by Tier 2); after that, at least once each business day for P2 (policy 7.1), so by end of business Fri 13 Nov at the latest, and in practice straight after the 07:00 UTC run.
