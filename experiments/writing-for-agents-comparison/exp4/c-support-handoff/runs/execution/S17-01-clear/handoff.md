# Handoff: QB-204518, Harrow & Finch Accounting Ltd (HF-0192)

As-of: 2026-11-12 11:30 UTC (thread export time). Escalated Tier 1 (Priya Nair) to Tier 2 (Product Engineering Support).

## 1. Problem and evidence

Problem: 112 invoices from the 07:00 UTC recurring run on 12 Nov were generated but never dispatched (state "Queued - not dispatched", 0 send attempts, no errors). This is probably KI-3381 (legacy recurring schedules skip auto-send after v8.3), but the cause is not confirmed. The customer's next runs are 13 Nov 07:00 UTC (64 invoices, per customer) and 15 Nov (90, per customer).

Evidence:
1. Verified (job log, Priya internal note 10:20): the 07:00:03 UTC run generated 112 invoices. All 112 are "Queued - not dispatched", with 0 send attempts and no errors.
2. Verified (job log, 10:20): all 112 come from schedules created before 10 Nov (the v8.3 release). The account has 3 schedules created after 10 Nov, and none was due today, so there is no comparison yet.
3. Verified (delivery log, 10:20 note): a manual Send of INV-2026-11-0457 at 10:15 was accepted by the recipient's mail server at 10:16.
4. Verified (test, 10:20 note): re-saving the "Meadowgate monthly retainer" schedule unchanged, then "Run now (test mode)", dispatched the test invoice within 40 seconds. This is verified for test mode only. It is not seen on a real scheduled run.
5. Verified (known-issue record, per 10:20 note): KI-3381 opened by Engineering 11 Nov, status Investigating, 2 other customers linked, symptoms match. Same cause "not confirmed". Linked to the ticket at 11:30.
6. Reported (Daniel, 09:14): "around 110 invoices" should have been emailed at 07:00. Conflict with evidence 1: the log shows 112. Treat the log as authoritative.
7. Reported (Daniel, 09:14): no settings were changed on their side. Not checked by support.
8. Reported (Daniel, 09:14): two clients have rung to ask where their invoice is. Also reported: client payment terms run from the send date, so delay pushes back collections.
9. Reported (Daniel, 10:52): 340 schedules; tomorrow's run has 64 invoices and Sunday's has 90. The account record shows 340 active schedules as of 1 Nov (a record field), which supports the schedule count. The 64 and 90 figures are not verified.
10. Reported (Daniel, 10:52): he will bulk-send today's 111 himself this afternoon. Not yet confirmed done.

## 2. Tried and results

| Who | When (UTC) | What | Result |
| --- | --- | --- | --- |
| Priya | 09:41 | Asked for an example invoice and permission to send one as a test | Daniel agreed at 09:58 |
| Priya | 10:15 | Manual Send of INV-2026-11-0457 from the invoice list | Worked (accepted 10:16) |
| Priya | before 10:20 | Re-saved schedule "Meadowgate monthly retainer" unchanged, then "Run now (test mode)" | Worked in test mode (sent to account owner only, within 40 s). Not tested on a real scheduled run |
| Priya | 10:20 | Reviewed job log and dispatcher | Found the 112 queued, 0 attempts, no errors |
| Priya | 10:34 | Gave the customer the workaround: filter "Queued", select up to 50, Send | Customer intends to use it today. No result recorded |
| Priya | 11:30 | Escalated to Tier 2, linked KI-3381 | Done. Priority left at P2 |

Not an attempt: the ledger entries for the customer's messages (09:14, 09:58, 10:52) and Priya's questions.

## 3. Commitments to the customer

1. Update by 16:00 UTC today. Priya, 11:05: "I will email you an update by 16:00 UTC today with what they've found, even if that is only that they are still investigating." Under policy 5.2 Tier 2 now owns this commitment ("From escalation, Tier 2 owns the ticket, including customer updates and any commitments already made to the customer"). Due in 4h30m from as-of.
2. Pass on the run timing. Priya, 11:05: "I'll make sure they know your next run is at 07:00 UTC tomorrow, 13 November, with 64 invoices." This is a promise of Priya's own action, and it was done in the 11:30 escalation note. The wording is ambiguous only in whether it implies ongoing follow-up.

Not promises: "I can't promise a fix time" (Priya, 11:05) is an explicit non-commitment. "Our engineering team is already investigating" is a statement of fact. No fix date, credit or refund has been promised (policy 6.2, 6.3). The account record shows no credits and no refunds.

## 4. Service level and deadline

- Plan and level, from the account record: Quillbill Practice, support level Enterprise (policy 1.3 takes the level from the account record).
- Priority: P2, as recorded on the ticket at creation (09:14) and unchanged at 11:30. Policy 2.2: "a major function, such as invoice sending, payment collection or bank feeds, does not work and there is no practical workaround."
- Targets, policy 3.1, Enterprise P2: first response 2 hours, 24x7; resolution 24 hours, 24x7. Policy 3.3: "Targets marked '24x7' run on calendar time."
- Clock start, policy 4.1: "The clock starts when the ticket is created." Created 2026-11-12 09:14 UTC. The ticket was never "Pending customer" (it went New, Open, Escalated), so no pause applies (4.2, 4.3). Paused time is 0.
- First response: first agent reply was at 09:41, which is 27 minutes after 09:14. The 2h target (deadline 11:14) was met. The automated acknowledgement rule (1.4) is not an issue, because the 09:41 message is from an agent.
- Resolution deadline: 09:14 on 12 Nov plus 24 h calendar equals 2026-11-13 09:14 UTC. Time remaining at 11:30: 09:14 to 11:30 is 2h16m elapsed, so 21h44m remain.
- Status, policy 4.5: "at risk" if less than 25% of the resolution target remains. 25% of 24 h is 6 h, so the ticket becomes at risk from 2026-11-13 03:14 UTC. Now: within target. It is not breached.
- Related policy points: 5.1 escalation is allowed for unresolved tickets with documented procedures lacking, and for P2 at risk. 5.3 the Duty Manager must be told only if the P2 is breached. This is not applicable yet, but it would apply after 13 Nov 09:14 if unresolved. 7.1 P2 customer updates: at least once each business day. The 16:00 commitment covers 12 Nov.
- Note: the 13 Nov 07:00 UTC run falls after the at-risk point (03:14) and 2h14m before the resolution deadline (09:14). The customer-critical date is that run.

## 5. Recommended next action

Action: Tier 2 (Product Engineering Support) should confirm whether KI-3381 is the cause for HF-0192 and get the customer's pre-10-Nov schedules dispatching automatically before the 13 Nov 07:00 UTC run, then send the customer the 16:00 update.

Reason: the 07:00 run on 13 Nov (64 invoices, reported) is before the SLA resolution deadline (09:14), and the customer cannot re-save 340 schedules by hand. Policy 6.2 means no fix date can be promised, so the update must give status only.

First check: find out whether the dispatch failure is tied to schedule creation date, as KI-3381 suggests. Compare against the 3 post-10-Nov schedules, and look at what re-saving changes on a pre-v8.3 schedule (this worked in test mode). Then check whether a bulk re-save or a data fix by Engineering is possible for the account's schedules, to avoid the customer doing 340 by hand. Check with the KI-3381 engineers for any ETA.

Open questions for engineering:
- Is KI-3381 confirmed to be the cause here, and does a re-save fix a real scheduled run, not only test mode?
- Can Engineering re-save or repair all pre-v8.3 schedules for HF-0192 in bulk before 13 Nov 07:00 UTC?
- Do the 64 invoices for 13 Nov and 90 for 15 Nov come from pre-v8.3 schedules?

Open questions for the customer:
- Have the 111 invoices been bulk-sent (afternoon of 12 Nov)? Any failures?
- Which schedules are due on 13 and 15 Nov, and when were they created? (To confirm the 64 and 90.)

## 6. Gaps (missing inputs, conflicts, unverified assumptions)

- Conflict: customer says around 110 invoices, the log shows 112. The log is used.
- Cause is unconfirmed: KI-3381 is a match on symptoms only, with status Investigating.
- The re-save fix is verified in test mode only, not on a real scheduled run.
- The 64 (13 Nov) and 90 (15 Nov) invoice counts are customer-reported. No schedule list was supplied.
- Not checked: the customer's claim of no settings changes.
- Priority question: Daniel asked for urgent handling, and the ticket is P2. Policy 2.2 requires "no practical workaround". Support supplied a manual bulk-send workaround, which could argue for P3 (Enterprise P3 is 4 business hours first response and 30 business hours resolution), but daily manual sending across 340 schedules is arguably not practical. Priority has not been changed, so P2 targets are used. Per 2.5 any change takes effect only when an agent records it. Recommend keeping P2.
- Assumption: 12 Nov is a business day, and no bank holiday applies (this matters only for 7.1).
- The thread gives no information on the 111 bulk-send outcome, or on a Duty Manager notification (not required now).
- Policy version 4.2 is the one supplied. Thread export time is the as-of time used throughout.
