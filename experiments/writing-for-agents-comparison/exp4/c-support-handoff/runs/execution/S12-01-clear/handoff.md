# Escalation handoff: QB-204518 - Recurring invoices created at 07:00 but never dispatched (KI-3381 suspected)

Customer: Harrow & Finch Accounting Ltd (HF-0192) | Tier: Enterprise (account record) | Priority: P2 (set on the case at creation, unchanged at escalation) | Prepared: 2026-11-12 11:30 UTC (export as-of time)

## Service level
Policy 3.1, Enterprise P2: first response "2 hours, 24x7"; resolution "24 hours, 24x7". Clock starts at ticket creation (4.1); never paused (status was never "Pending customer", 4.2) | Resolution deadline: 2026-11-13 09:14 UTC | Status: Within target, 21h 44m remaining (not "at risk": the threshold is under 6h, i.e. 25% of 24h, per 4.5)
Arithmetic: created 2026-11-12 09:14 + 24h calendar = 2026-11-13 09:14; now 11:30, so elapsed 2h 16m, remaining 21h 44m. First response: first agent reply 09:41 (27 min after creation, 1.4) - Met against 2h. Note the 07:00 UTC run on 13 Nov falls before the 09:14 deadline.

## Problem as currently understood
The 07:00:03 UTC recurring run on 12 Nov generated 112 invoices, all stuck in dispatch state "Queued - not dispatched" with no send attempts and no errors. All 112 come from schedules created before the v8.3 release (10 Nov). Support suspects known issue KI-3381 but has not confirmed the same cause. The customer's concern is the next runs: 13 Nov 07:00 UTC (64 invoices) and 15 Nov (90 invoices), with 340 schedules in total.
- [Verified] 112 invoices generated at 07:00:03, all "Queued - not dispatched", 0 send attempts, no errors (Priya Nair, internal note, 2026-11-12 10:20)
- [Verified] All 112 come from schedules created before 10 Nov; 3 schedules created after 10 Nov exist, none due today, so no comparison (Priya Nair, 10:20)
- [Verified] Manual Send of INV-2026-11-0457 at 10:15 was accepted by the recipient's mail server at 10:16 (Priya Nair, 10:20)
- [Verified] Re-saving schedule "Meadowgate monthly retainer" unchanged, then "Run now (test mode)" dispatched within 40 seconds; not yet seen on a real scheduled run (Priya Nair, 10:20)
- [Verified] KI-3381 "Legacy recurring schedules skip auto-send after v8.3" exists, opened by Engineering 11 Nov, Investigating, 2 other customers linked; symptoms match, cause not confirmed (Priya Nair, 10:20)
- [Reported] About 110 invoices expected at 07:00 (the log shows 112); none received by clients; two clients rang to ask (Daniel Okafor, 09:14)
- [Reported] No settings changed on the customer side (Daniel Okafor, 09:14)
- [Reported] Client payment terms run from send date, so delay pushes back collections (Daniel Okafor, 09:14)
- [Reported] 340 schedules; next runs 13 Nov 07:00 UTC with 64 invoices and 15 Nov with 90 (Daniel Okafor, 10:52). The 340 figure also appears in the account record (as of 1 Nov).
Customer and support do not disagree on the problem.

## What has been tried
1. Manual Send of INV-2026-11-0457 (customer consented 09:58) - Priya Nair, 10:15 - Resolved for that invoice (accepted by recipient's server 10:16)
2. Re-save of "Meadowgate monthly retainer" without changes, then "Run now (test mode)" - Priya Nair, ~10:20 or earlier - Partial: test invoice dispatched in 40 s, but test mode sends only to account owner and a real scheduled run is not yet observed
3. Workaround advised to customer: filter "Queued", select up to 50, Send - Priya Nair, 10:34 - Unknown: no result recorded (customer said at 10:52 they will bulk-send the 111 themselves this afternoon; Reported intention)
4. Customer-side fixes: none reported. Customer says no settings were changed.

## Commitments to the customer
- "I will email you an update by 16:00 UTC today with what they've found, even if that is only that they are still investigating." - Priya Nair, 2026-11-12 11:05 - due 2026-11-12 16:00 UTC - open (4h 30m left). Under policy 5.2 Tier 2 now owns this.
- "I'll make sure they know your next run is at 07:00 UTC tomorrow, 13 November, with 64 invoices." - Priya Nair, 11:05 - no time stated - met by the escalation note at 11:30 (which gives the run time and count).
- Not commitments: "I can't promise a fix time" (11:05) explicitly declines the customer's request to guarantee a fix before tomorrow's run; no fix date, credit or refund was promised (policy 6.2 forbids agents doing so).
Claimed by customer, not found in thread: none. (The customer asked for a guarantee at 10:52; none was given.)

## Open questions
- Is the root cause the same as KI-3381? Engineering's finding so far is "Investigating" only.
- Is the fault tied to schedules created before 10 Nov? Only 3 post-10 Nov schedules exist and none has run.
- Does re-saving a schedule fix a real scheduled run, not just test mode? Can this be done in bulk server-side for 340 schedules (how many are pre-v8.3)?
- Are all 64 invoices for 13 Nov and 90 for 15 Nov from affected schedules?
- Error text, product version/build for the account, and why the dispatcher shows no attempts and no errors: none recorded in the case.
- Has the customer actually sent the 111 queued invoices? Unknown.
- Priority: P2 requires "no practical workaround" (policy 2.2), yet manual bulk send works. Whether P2 stands is for support to decide (2.5); not changed here. If it were P3 the Enterprise resolution target would differ.
- Does Elena Marsh (CSM) need to be informed? No credit or refund was offered.

## Recommended next action
Ask Engineering on KI-3381 whether HF-0192's pre-v8.3 recurring schedules (340 active) can be repaired in bulk server-side (equivalent to the re-save that cleared the test schedule), and check whether the 07:00 UTC 13 Nov run would dispatch automatically afterwards. Reason: the re-save evidence (10:20) points to a per-schedule state fault, and the customer cannot re-save 340 schedules by hand. Timing: have a finding in time for the 16:00 UTC update today (promised by Priya Nair, owned by Tier 2), and any fix or fallback in place before the 13 Nov 07:00 UTC run (64 invoices), which precedes the 09:14 resolution deadline. Do not promise the customer a fix date (policy 6.2).
Follow-ups: (1) send the customer the update by 16:00 UTC even if only "still investigating"; (2) if no bulk fix is ready by the evening, tell the customer the manual bulk-send procedure for the 13 Nov run.
