# Handoff: QB-204518 Recurring invoices created but not sent (Harrow & Finch Accounting Ltd, HF-0192)

## Problem
- The 07:00 UTC recurring run on 12 Nov 2026 was expected to email about 110 invoices and none reached clients. [Reported: Daniel Okafor, 09:14 message; his figure is approximate]
- The 07:00:03 UTC run generated 112 invoices. All 112 are in dispatch state "Queued - not dispatched", with 0 send attempts and no errors. [Verified: Priya Nair internal note 10:20, job log for HF-0192]
- All 112 come from schedules created before 10 Nov (the v8.3 release). The account has 3 schedules created after 10 Nov, and none was due today, so there is no comparison yet. [Verified: internal note 10:20, job log]
- KI-3381 "Legacy recurring schedules skip auto-send after v8.3" (opened by Engineering 11 Nov, status Investigating, 2 other customers linked) has matching symptoms. It is not confirmed as the same cause. [Verified: internal note 10:20 for the known issue's details; linkage on the ticket at 11:30]
- Manual Send of INV-2026-11-0457 worked: the recipient's mail server accepted it at 10:16. [Verified: delivery log, internal note 10:20]
- Re-saving the "Meadowgate monthly retainer" schedule unchanged, then "Run now (test mode)", dispatched the test invoice within 40 seconds. Test mode sends only to the account owner. This has not been seen on a real scheduled run. [Verified: support-side test, internal note 10:20]
- The customer made no settings changes. [Reported: 09:14 message]
- Two clients have phoned asking where their invoices are. [Reported: 09:14 message]
- Client payment terms run from the send date, so delay pushes back collections. [Reported: 09:14 message]
- The account has 340 active recurring schedules. [Verified: account record, as of 1 Nov 2026; the customer's 10:52 message also says 340]
- The next runs are 13 Nov 07:00 UTC with 64 invoices and Sun 15 Nov with 90 invoices. [Reported: Daniel Okafor, 10:52 message. The escalation note repeats 13 Nov at 64 and 15 Nov at 90, but it is a restatement of the customer's figures, not independent confirmation. The 15 Nov run time is not stated.]
- Conflict to note: the customer said "around 110" and the system shows 112 generated. This is a minor difference, and the system count is authoritative.
- Priority is P2 and unchanged. The customer asked for urgent treatment but did not ask for a different priority. [Verified: ticket events 09:14 and 11:30]

## Open questions
- Is the cause the same as KI-3381? Ask Engineering to compare the job log for HF-0192 against KI-3381 findings.
- Does re-saving fix a schedule on a real scheduled run, rather than only in test mode? Verify by re-saving one or more schedules due 13 Nov before 07:00 UTC and checking dispatch after the run.
- Are all 340 schedules affected, or only those created before 10 Nov? The account has only 3 post-10-Nov schedules, none due yet. Check them on their first due run, and check the other schedules' creation dates.
- Can Engineering re-save or repair schedules in bulk from the server side? The customer will not hand-edit 340 schedules. This is not addressed in the thread.
- Did the customer bulk-send the remaining 111 invoices this afternoon, as they said they would? [Reported intention, 10:52] Confirm in the dispatch log.
- What time does the 15 Nov run happen, and is the 90-invoice count right? Check against the schedule list.

## Attempts
1. Priya Nair asked for a sample invoice number and permission to test-send (09:41). Result: customer gave INV-2026-11-0457 and consent at 09:58.
2. Priya Nair reviewed the job log (by 10:20). Result: 112 invoices queued, 0 send attempts, no errors.
3. Priya Nair linked the symptoms to KI-3381 (10:20; formally linked 11:30). Result: symptoms match; cause unconfirmed.
4. Priya Nair did a manual Send of INV-2026-11-0457 at 10:15. Result: worked; accepted by the recipient's mail server at 10:16.
5. Priya Nair re-saved the Meadowgate schedule and ran "Run now (test mode)". Result: worked; dispatched within 40 seconds (test mode only).
6. Priya Nair gave the customer a workaround at 10:34: filter Queued, select up to 50, Send. Result: the customer said at 10:52 they will bulk-send the 111 remaining invoices themselves this afternoon; completion unknown.
7. Priya Nair escalated to Tier 2 at 11:30, with the customer told at 11:05. Result: escalated; no Tier 2 action yet.

## Commitments to the customer
| Commitment | Made by | When | Quote |
| --- | --- | --- | --- |
| Email the customer an update by 16:00 UTC on 12 Nov, even if engineering is still investigating | Priya Nair, Support Agent (Tier 1) | 2026-11-12 11:05 UTC | "I will email you an update by 16:00 UTC today with what they've found, even if that is only that they are still investigating." |
| Make sure Engineering knows the next run is 07:00 UTC on 13 Nov with 64 invoices | Priya Nair, Support Agent (Tier 1) | 2026-11-12 11:05 UTC | "I'll make sure they know your next run is at 07:00 UTC tomorrow, 13 November, with 64 invoices." |
| Escalate to Product Engineering Support | Priya Nair, Support Agent (Tier 1) | 2026-11-12 11:05 UTC | "I'm escalating your ticket to our Product Engineering Support team now" (done at 11:30) |

No fix date, credit or refund was promised. Priya declined to give a fix time: "I can't promise a fix time". The customer's request to guarantee a fix before tomorrow's run is unanswered. Under policy 5.2, Tier 2 now owns these commitments.

## Service level
Term: Enterprise P2, first response "2 hours, 24x7"; resolution "24 hours, 24x7" (policy 3.1, with 3.3 for calendar time). Support level Enterprise per account record (policy 1.3); priority P2 per ticket (policy 2.2, 2.5).
Clock start: 2026-11-12 09:14 UTC, when the ticket was created (policy 4.1). The status was never "Pending customer", so the clock was never paused (policy 4.2). [Verified: thread events]
Deadline: first response 11:14 UTC on 12 Nov, met at 09:41 UTC (27 minutes, Priya Nair). Resolution 09:14 UTC on 13 Nov 2026.
Status: Within target as of 2026-11-12 11:30 UTC. 2h16m elapsed, 21h44m remaining. The 25% "at risk" threshold is 6 hours remaining, so it is reached at 03:14 UTC on 13 Nov. The 07:00 UTC run on 13 Nov falls inside the resolution window, 2h14m before the deadline. Policy 5.1 allows escalation for a P2 that is at risk; this ticket was escalated because it cannot be resolved with documented procedures. Policy 7.1 requires a P2 update at least once each business day, and the 16:00 commitment satisfies that for 12 Nov. 13 Nov is a Friday and needs another update.

## Recommended next action
Primary action: Tier 2 should confirm whether KI-3381 is the cause, and get a repair applied to all of HF-0192's pre-v8.3 schedules (for example a bulk re-save or server-side reset) before the 13 Nov 07:00 UTC run. If that is not possible, check dispatch right after 07:00 on 13 Nov and have the 64 invoices ready to bulk-send by the manual route.
Reason: the log shows all 112 invoices from pre-v8.3 schedules undispatched with no errors. A single-schedule re-save worked in test mode, and manual send works. The customer cannot practically re-save 340 schedules by hand.
Must satisfy:
- Send the customer the update promised by 16:00 UTC on 12 Nov, even if the update is only that investigation is continuing. Do not promise a fix date or release date (policy 6.2).
- Pass on the 13 Nov 07:00 UTC, 64-invoice run to Engineering, as committed.
- Answer the customer's unanswered question about a fix before tomorrow's run honestly: say what is known and do not guarantee it.
- Resolve before 09:14 UTC on 13 Nov, and send a further update that day.
- Any credit or refund (the customer has not asked for one) can come only from Elena Marsh (the Customer Success Manager) or the Head of Support, recorded in writing (policy 6.3). The account shows no open credits.
Assumptions to check:
- KI-3381 is the cause (see Open questions).
- Re-save works in real runs, not just test mode.
- The customer's 64 and 90 counts are right.
- The customer actually bulk-sent the 111 invoices.
