# Handoff: QB-204518, Harrow & Finch Accounting Ltd (HF-0192)
As of 2026-11-12 11:30 UTC. Escalated Tier 1 (Priya Nair) to Tier 2.

## 1. Problem as understood
The 07:00 UTC recurring run on 12 Nov generated 112 invoices, and all are stuck "Queued - not dispatched" with no send attempts. All 112 come from schedules created before the v8.3 release (10 Nov). The ticket is linked to KI-3381, but the same cause is not confirmed. The customer's next runs are 13 Nov 07:00 UTC and 15 Nov, and they cannot re-save 340 schedules by hand.

Evidence:
- 112 invoices generated at 07:00:03 UTC, all "Queued - not dispatched", 0 send attempts, no errors. **Verified**: Priya Nair, job log, 12 Nov 10:20.
- All 112 are from schedules created before 10 Nov; 3 schedules created after 10 Nov, none due today, so no comparison. **Verified**: Priya Nair, job log, 12 Nov 10:20.
- Manual Send of INV-2026-11-0457 at 10:15 was accepted by the recipient's mail server at 10:16. **Verified**: Priya Nair, delivery log, 12 Nov 10:20.
- Re-saving "Meadowgate monthly retainer" unchanged, then "Run now (test mode)", dispatched in 40 seconds. **Verified for test mode, one schedule only**: Priya Nair, 12 Nov 10:20. It is not seen on a real scheduled run.
- Symptoms match KI-3381 (opened by Engineering 11 Nov, Investigating, 2 other customers linked). Same cause **not confirmed** (Priya Nair, 12 Nov 10:20).
- Account has 340 active recurring schedules as of 1 Nov. **Verified**: account record.
- Next runs: 64 invoices on 13 Nov 07:00 UTC and 90 on Sunday 15 Nov. **Reported**: Daniel Okafor, 12 Nov 10:52. Priya repeated the 64 figure but the thread shows no check of either count.
- No settings changed on their side. **Reported**: Daniel Okafor, 12 Nov 09:14.
- No client has received an invoice, and two clients have phoned. **Reported**: Daniel Okafor, 12 Nov 09:14. Meadowgate did receive one, via Priya's manual send.
- Payment terms run from the send date, so delay pushes back collections. **Reported**: Daniel Okafor, 12 Nov 09:14.
- Contradiction: customer says about 110 invoices were due (09:14), the log shows 112. The log is the better source.
- Contradiction: the customer says "today's 111" remain to be sent. This is 112 minus the one Priya sent and is consistent with the log. The customer says they will bulk-send these themselves this afternoon (12 Nov 10:52). **Reported**, so confirm it has happened.

## 2. Tried and result
- Priya Nair, 10:15: manual Send of INV-2026-11-0457 from the invoice list. Worked (accepted 10:16).
- Priya Nair, ~10:20: re-saved one schedule, then ran test mode. Worked in test mode only. No real-run result.
- Priya Nair, 10:34: advised the customer to bulk-send the remaining 111 from the invoice list (filter "Queued", up to 50 at a time). Outcome unknown. The customer said they would do it this afternoon.
- Ruled out: no send errors in the dispatcher log (0 attempts). The cause is not ruled out. Mail delivery is not the fault, since manual send is accepted.
- Linked to KI-3381 at escalation, 11:30. Outcome: pending.

## 3. Commitments to the customer
- Email an update by 16:00 UTC on 12 Nov, "even if that is only that they are still investigating". Made by Priya Nair, 12 Nov 11:05. Policy 5.2 passes this to Tier 2.
- Make sure Product Engineering Support knows the next run is 07:00 UTC on 13 Nov with 64 invoices. Made by Priya Nair, 12 Nov 11:05. The escalation note at 11:30 does include this.
- Declined: Priya said she "can't promise a fix time". No fix date, credit or refund has been promised. The account record shows no credits or refunds.

## 4. Service-level status and deadline
- Tier: Enterprise (account record, Support level). Priority: P2 (policy 2.2, bank feeds/sending-type major function). Priority was set by support and is unchanged. Policy 2.2 counts "invoice sending" as a major function, and a manual-send workaround exists, but it is impractical at scale. P3 would apply if the workaround were treated as practical (policy 2.3). I assume P2 as recorded.
- Targets (policy 3.1, Enterprise P2): first response "2 hours, 24x7"; resolution "24 hours, 24x7". Calendar time applies (policy 3.3).
- Clock start: ticket creation, 2026-11-12 09:14 UTC (policy 4.1).
- First response: Priya's reply at 09:41, 27 minutes after creation. Met.
- Pause: only "Pending customer" pauses the clock (policy 4.2). The thread shows New, Open, Escalated, so there is no paused time. Assumption: there is no unrecorded "Pending customer" status.
- Resolution deadline: 09:14 + 24h = **2026-11-13 09:14 UTC**. Business hours do not apply.
- Elapsed at 11:30: 2h16m. Remaining: 21h44m (about 90% of the target remains).
- Status: **within target**. "At risk" starts when under 25% remains (policy 4.5), i.e. under 6h, from 2026-11-13 03:14 UTC. Policy 5.1 allows escalation when a P2 is at risk.
- The 07:00 UTC run on 13 Nov falls before the resolution deadline.
- Resolution (policy 1.5) requires a fix or workaround that restores the affected function, and status set to Resolved. Whether manual send alone counts is not stated. Policy does not state this.
- Duty Manager (policy 5.3) must be told only if the P2 is breached. Not applicable now.
- Update cadence for P2 (policy 7.1): at least once each business day. 13 Nov is a Friday.

## 5. Recommended next action
**Action:** Tier 2 engineer (Product Engineering Support) confirms with the KI-3381 owner whether this account's 112 stuck invoices share its cause and whether a server-side fix is possible for all pre-10 Nov schedules (a bulk re-save or a re-queue) before the 13 Nov 07:00 UTC run (64 invoices) and the 09:14 resolution deadline.
**Why:** The symptoms match (item: KI-3381), but only a test-mode re-save of one schedule has been verified (item: re-save test), and the customer cannot re-save 340 schedules by hand (item: Daniel Okafor, 10:52).
**Fallback:** If no fix is available by about 03:14 UTC on 13 Nov (the at-risk point), tell the customer the manual bulk-send procedure applies to the 13 Nov run and brief the Duty Manager as a precaution. Policy 5.3 does not require this unless the ticket breaches.

**Customer contact:** Email Daniel Okafor by 16:00 UTC on 12 Nov with what Engineering has found, or that they are still investigating. Ask him to confirm whether the 111 were bulk-sent. Do not promise a fix date, credit or refund (policy 6.2). Any credit goes through Elena Marsh, CSM (policy 6.3). Give a further update on 13 Nov, the next business day.
