# Escalation handoff: QB-204518, Harrow & Finch Accounting Ltd (HF-0192)

**Summary:** 112 invoices from pre-v8.3 recurring schedules were generated but never dispatched at 07:00 UTC on 12 Nov, matching KI-3381 (not confirmed). The most urgent deadlines are the customer update promised by 16:00 UTC today and the next run at 07:00 UTC on 13 Nov (64 invoices), ahead of the resolution deadline of 09:14 UTC on 13 Nov.
**Reference time:** 2026-11-12 11:30 UTC (latest thread entry; the export states it is the as-of time)

## Problem as currently understood
Recurring invoices created by schedules that predate the 10 Nov v8.3 release are stuck in "Queued - not dispatched" with no send attempts and no errors. This resembles known issue KI-3381, but the cause is not confirmed. Manual sending works, and re-saving a schedule appeared to restore sending in test mode only.
- [Verified] 07:00:03 UTC run generated 112 invoices, all "Queued - not dispatched", 0 send attempts, no errors (Priya Nair internal note, 10:20)
- [Verified] All 112 come from schedules created before 10 Nov; the account has 3 schedules created after 10 Nov, none due today (Priya Nair, 10:20)
- [Verified] Manual send of INV-2026-11-0457 was accepted by the recipient's mail server at 10:16 (delivery log, Priya Nair, 10:20)
- [Verified] Re-save plus "Run now (test mode)" on "Meadowgate monthly retainer" dispatched within 40 seconds, test mode only (Priya Nair, 10:20)
- [Verified] KI-3381 "Legacy recurring schedules skip auto-send after v8.3", opened 11 Nov, status Investigating, 2 other customers linked; symptoms match, not confirmed as the same cause (Priya Nair, 10:20)
- [Verified] 340 active recurring schedules as of 1 Nov (account record)
- [Reported] Customer made no setting changes (Daniel Okafor, 09:14)
- [Reported] Two clients have phoned asking where their invoice is; payment terms run from the send date (Daniel Okafor, 09:14)
- [Reported] Next runs are 13 Nov 07:00 UTC with 64 invoices and 15 Nov with 90 (Daniel Okafor, 10:52). Priya stated the 64 and 07:00 UTC figures in her 11:05 reply without recording a check, so they stay Reported.
- [Reported] Customer will bulk-send the other 111 invoices himself this afternoon (Daniel Okafor, 10:52)
Open questions:
- Is the cause the same as KI-3381? Does re-saving fix a real scheduled run, not only test mode?
- Is there a bulk fix for all 340 schedules, or a way to re-save in bulk?
- Are the 3 post-10 Nov schedules unaffected? There is no direct comparison yet.
- Are the 13 Nov and 15 Nov runs made up only of affected pre-v8.3 schedules?

## Tried so far
- Checked job log and dispatcher for HF-0192, by Priya Nair, 10:20: 112 queued, 0 attempts, no errors
- Manual send of INV-2026-11-0457 (customer consented, 09:58), by Priya Nair, 10:15: accepted by recipient mail server 10:16
- Re-saved schedule unchanged, then "Run now (test mode)", by Priya Nair, ~10:20: dispatched within 40 seconds to the account owner only; real scheduled run not yet seen
- Told customer to filter "Queued", select up to 50 and Send, by Priya Nair, 10:34: customer says he will do this this afternoon (Reported); result not recorded
- Linked ticket to KI-3381, by Priya Nair, 11:30: link recorded; cause not confirmed

## Commitments to the customer
- "I will email you an update by 16:00 UTC today with what they've found, even if that is only that they are still investigating.", Priya Nair, 11:05: outstanding (4h30 remaining). Under policy 5.2 Tier 2 owns this commitment now.
- "I'm escalating your ticket to our Product Engineering Support team now", Priya Nair, 11:05: met (escalated 11:30)
- "I'll make sure they know your next run is at 07:00 UTC tomorrow, 13 November, with 64 invoices.", Priya Nair, 11:05: met (stated in the escalation note, 11:30)
- Not a commitment: "I can't promise a fix time". The customer asked for a guarantee of a fix before tomorrow's run and none was given. Policy 6.2 forbids promising a fix date.
- No credits or refunds were offered. The account record shows none.

## Service level
- Tier: Enterprise (account record) | Priority: P2 (ticket, set at creation 09:14 and recorded as unchanged at escalation 11:30)
- Target: first response 2 hours 24x7; resolution 24 hours 24x7 (policy 3.1, Enterprise P2; 3.3 calendar time)
- Deadline: first response 11:14 on 12 Nov (09:14 + 2h); resolution 09:14 UTC on 13 Nov (09:14 + 24h). The clock starts at ticket creation (4.1). The thread records no "Pending customer" status, so no pause time is deducted (4.2).
- Status: first response met (Priya Nair, 09:41, 27 minutes after creation). Resolution is open, within target, with 21h44m remaining. The at-risk threshold is under 6h remaining (25% of 24h, policy 4.5), which is 03:14 UTC on 13 Nov. The 07:00 run falls after that point.
- Note: invoice sending is a P2 function (policy 2.2), but a manual-send workaround exists today, which could point to P3 under 2.3. Ticket priority governs (2.5), so this is left at P2.
- Policy 7.1: P2 needs an update at least once each business day; the 16:00 update covers 12 Nov.

## Recommended next action
Confirm whether KI-3381 is the cause of this account's fault and obtain a fix or bulk workaround covering the schedules due 13 Nov (64 invoices), ideally before 07:00 UTC on 13 Nov, because evidence shows all 112 stuck invoices came from pre-v8.3 schedules and a re-save worked in test mode only. If no fix can be confirmed in time, test re-saving the schedules due on 13 Nov (the untested option) and prepare to have the customer send the 64 by hand. Serves: the 16:00 UTC update commitment, the 07:00 UTC 13 Nov run, and the 09:14 UTC 13 Nov resolution deadline.
Tell the customer: by 16:00 UTC today, send the promised update with the engineering status. Say that manual sending (filter "Queued", up to 50 at a time) remains available if the 13 Nov run is not fixed. Do not promise a fix date (policy 6.2).
