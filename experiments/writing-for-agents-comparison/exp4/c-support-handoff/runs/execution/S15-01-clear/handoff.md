# Handoff: QB-204518, Harrow & Finch Accounting Ltd (HF-0192)

## 1. Summary
Harrow & Finch Accounting Ltd (account HF-0192, Quillbill Invoicing, Recurring Billing add-on) had 112 invoices from its 07:00 UTC run on 12 November 2026 created but never dispatched (status "Queued - not dispatched"), which matches known issue KI-3381 (not confirmed as the same cause). It is urgent: the ticket is Enterprise P2, the 24-hour resolution deadline is 13 November 2026 09:14 UTC, and the customer's next run (64 invoices) is at 07:00 UTC on 13 November, before that deadline.

## 2. Problem and evidence
- _Reported_ (Daniel Okafor, 09:14 UTC): around 110 recurring invoices should have been emailed at 07:00; all show "Queued"; no client has received theirs; two clients have phoned; no settings were changed on the customer side. (Thread, 12 Nov 09:14.) The "no settings changed" and "two clients have rung" statements are not independently verified.
- _Verified_ (job log, Priya Nair internal note 10:20): the 07:00:03 UTC run generated 112 invoices, all in dispatch state "Queued - not dispatched", with 0 send attempts and no errors.
- _Verified_ (same note): all 112 come from schedules created before 10 Nov (v8.3 release). The account has 3 schedules created after 10 Nov; none was due today, so there is no direct comparison.
- _Verified_ (Test 1, delivery log): manual Send of INV-2026-11-0457 at 10:15 was accepted by Meadowgate's mail server at 10:16. So manual dispatch works, and not "no client has received" any invoice (this one has).
- _Verified_ (Test 2): re-saving schedule "Meadowgate monthly retainer" unchanged, then "Run now (test mode)" (sends only to the account owner), dispatched within 40 seconds. This is test mode on one schedule only.
- _Hypothesis_: the cause is KI-3381 "Legacy recurring schedules skip auto-send after v8.3" (opened by Engineering 11 Nov, status Investigating, 2 other customers linked). Priya notes the symptoms match but it is not confirmed.
- _Hypothesis_: re-saving a schedule restores automatic sending on real scheduled runs. Not yet seen on a real run.
- _Reported_ (Daniel, 10:52): 340 schedules; tomorrow 07:00 run has 64 invoices; Sunday's has 90. Run sizes are not verified from the record. Account record confirms 340 active schedules as of 1 November 2026.
- _Reported_ (Daniel, 09:14): client payment terms run from the send date, so each day of delay defers collections.

## 3. Tried so far
| Action | Result | Who |
| --- | --- | --- |
| Reviewed job log and dispatcher for HF-0192 | 112 invoices Queued, 0 send attempts, no errors | Priya Nair, T1 |
| Checked known issues | KI-3381 found, symptoms match, not confirmed | Priya Nair |
| Manual Send of INV-2026-11-0457 (10:15, with customer consent at 09:58) | Accepted by recipient mail server 10:16 | Priya Nair |
| Re-saved "Meadowgate monthly retainer" unchanged, then "Run now (test mode)" | Test invoice dispatched within 40 s; real scheduled run not yet observed | Priya Nair |
| Advised customer to bulk-send the other 111 from the invoice list (filter "Queued", up to 50 at a time) | Customer said they will do it this afternoon; completion result not recorded | Priya Nair (advice), customer (execution) |
| Linked ticket to KI-3381 and escalated to Tier 2 at 11:30 | Done; status Escalated, priority P2 unchanged | Priya Nair |

## 4. Commitments to the customer
| Quote | Author | Date/time (UTC) | Status |
| --- | --- | --- | --- |
| "I will email you an update by 16:00 UTC today with what they've found, even if that is only that they are still investigating." | Priya Nair | 2026-11-12 11:05 | Open, due 2026-11-12 16:00 UTC (4h30m after the as-of time). Under policy 5.2 Tier 2 now owns it. |
| "I'm escalating your ticket to our Product Engineering Support team now" | Priya Nair | 2026-11-12 11:05 | Kept: escalated 11:30. |
| "I'll make sure they know your next run is at 07:00 UTC tomorrow, 13 November, with 64 invoices." | Priya Nair | 2026-11-12 11:05 | Kept in the escalation note (11:30), which includes the 13 Nov run and 64 invoices. |
| "I can't promise a fix time, because that depends on what engineering finds." | Priya Nair | 2026-11-12 11:05 | A refusal, not a promise. No fix date, credit or refund has been promised (consistent with policy 6.2). |
| "Our engineering team is already investigating a known issue that looks like yours..." | Priya Nair | 2026-11-12 10:34 | A statement, not a promise. |

Daniel's question "Can you guarantee this will be fixed before tomorrow morning's run?" has no guarantee in reply and remains unanswered in substance.

## 5. Service level
- Tier: Enterprise (account record, "Support level: Enterprise"; policy 1.3).
- Priority: P2 (ticket field, unchanged). Policy 2.2 defines P2 as a major function that does not work with no practical workaround.
- First response (policy 3.1, Enterprise P2: 2 hours, 24x7): clock start 09:14 UTC (4.1), target 11:14 UTC. First agent reply 09:41 UTC, 27 minutes after creation. Met.
- Resolution (policy 3.1, Enterprise P2: 24 hours, 24x7; 3.3 calendar time): 09:14 UTC on 12 Nov + 24h = 09:14 UTC on 13 Nov 2026. No "Pending customer" status in the thread, so no paused time (4.2).
- Time remaining at the 11:30 UTC as-of time: 09:14 on 13 Nov minus 11:30 on 12 Nov = 21h44m. Elapsed 2h16m.
- Status (4.5): within target. At risk begins when less than 25% remains: 25% of 24h = 6h, so from 03:14 UTC on 13 Nov. The 07:00 UTC run on 13 Nov falls inside the at-risk window, 2h14m before the deadline.
- Customer updates (7.1): P2 needs at least one update per business day; 12 Nov is a Thursday and updates were sent. The promised 16:00 update goes beyond that minimum.
- Duty Manager (5.3): required only for a breached P2; not breached now.
- Credits and refunds (6.3): none offered. Only the Customer Success Manager (Elena Marsh) or Head of Support may offer one, in writing on the ticket or account record.

## 6. Recommended next action
Primary (owner: Tier 2 Product Engineering Support engineer): determine whether HF-0192's stuck dispatch is the KI-3381 cause and whether Engineering can restore automatic dispatch for all of the account's pre-v8.3 schedules server-side, so the real 13 Nov 07:00 UTC run (64 invoices) sends without the customer re-saving 340 schedules by hand. It would confirm or rule out KI-3381 as the cause, and whether re-save fixes real runs. Serves: the 16:00 UTC customer update (now owned by Tier 2), the 13 Nov 07:00 run, and the resolution deadline of 13 Nov 09:14 UTC. Make no promise to the customer of a fix date (policy 6.2); the 16:00 update can report findings or state that investigation continues.

Alternatives, in order:
1. If no server-side fix is possible before 07:00 UTC on 13 Nov, tell the customer in the 16:00 update that the 13 Nov invoices can be bulk-sent from the invoice list (up to 50 at a time, so two batches for 64), as was advised for 12 Nov. This serves the customer's collections timing.
2. Ask the customer to re-save only the schedules due on 13 Nov, as a targeted test on real runs. This would show whether re-save works outside test mode. It may be practical for the 64 invoices' schedules, though how many schedules that is has not been established.
3. Consider whether priority should be reviewed (see Gaps). Only a support agent can record a change (policy 2.5).

## 7. Gaps and conflicts
- Missing inputs: none missing. No Engineering notes on KI-3381 are supplied beyond Priya's summary, and the root cause and any ETA are unknown.
- Customer vs record: Daniel says "not one client has received theirs"; the delivery log shows Meadowgate received INV-2026-11-0457 after support's manual send at 10:16. Meadowgate would not have received it from the scheduled run.
- Count: Daniel wrote "around 110"; the log shows 112; Priya called the remainder "111". Whether the customer has bulk-sent the 111 is not recorded.
- Schedule count: the record says 340 active schedules as of 1 November 2026, but the log says 3 schedules were created after 10 Nov. Whether the 340 includes them, and how many are pre-v8.3, is not stated.
- The 13 Nov (64) and 15 Nov (90) invoice counts, and whether those schedules are pre-v8.3, are customer-reported only.
- Priority: P2 requires "no practical workaround" (policy 2.2). A manual bulk send is a workaround (policy 2.3 for P3), though the customer says re-saving 340 schedules is not realistic and daily manual sending is a cost. Priority is unchanged; no agent has recorded a review. Changing to P3 would change the resolution target to 30 business hours under Enterprise (policy 4.4), so decide deliberately.
- Policy leaves out: no definition of what counts as "workaround" effort, and no term on service-level treatment of a known issue that is linked across customers.
- The thread does not say who from Tier 2 has been assigned; the owner per 5.2 is Tier 2 generally.
- Timezone: all times UTC; Europe/London equals UTC from 25 Oct 2026 (policy 1.1).
