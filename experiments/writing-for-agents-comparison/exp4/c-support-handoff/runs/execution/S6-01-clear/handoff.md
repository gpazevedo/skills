## Escalation handoff: QB-204518 Recurring invoices created but not sent (112 stuck "Queued")
As of: 2026-11-12, 11:30 UTC (GMT; same as Europe/London)
Customer: Harrow & Finch Accounting Ltd (HF-0192), plan Quillbill Practice, support level Enterprise, UK data region, Quillbill Invoicing (cloud) + Recurring Billing add-on (340 active schedules as of 1 Nov 2026) + Bank Feeds. Contacts: Daniel Okafor (technical, ticket owner), Ruth Finch (contract), CSM Elena Marsh. (account record)

### Problem as currently understood
The 07:00 UTC recurring run on 12 Nov created 112 invoices, but none was dispatched; the dispatcher shows no send attempts and no errors. All 112 come from schedules created before the v8.3 release (10 Nov). Support suspects known issue KI-3381, but the match is not confirmed. Re-saving a schedule may clear the fault, but this is untested on a real scheduled run.
Evidence:
- [Verified] 07:00:03 run generated 112 invoices, all "Queued - not dispatched", 0 send attempts, no errors (Priya Nair, job log, 10:20)
- [Verified] All 112 come from schedules created before 10 Nov; 3 schedules created after 10 Nov exist, none due today, so no comparison yet (Priya Nair, 10:20)
- [Verified] KI-3381 "Legacy recurring schedules skip auto-send after v8.3": opened by Engineering 11 Nov, Investigating, 2 other customers linked; symptoms match, same cause not confirmed (Priya Nair, 10:20)
- [Verified] Manual Send of INV-2026-11-0457 at 10:15 was accepted by the recipient's mail server at 10:16 (Priya Nair, delivery log)
- [Verified] Re-saving the "Meadowgate monthly retainer" schedule unchanged, then "Run now (test mode)", dispatched in 40 seconds, test mode only (Priya Nair, 10:20)
- [Reported] No client has received an invoice, and two clients have phoned to ask (Daniel Okafor, 09:14)
- [Reported] No settings were changed on the customer side (Daniel Okafor, 09:14)
- [Reported] Payment terms run from the send date, so delay pushes back collections (Daniel Okafor)
- [Reported] Next runs: 13 Nov 07:00 UTC with 64 invoices, and 15 Nov with 90 (Daniel Okafor 10:52; Priya Nair repeated the 13 Nov figure)
- [Reported] Daniel says he will bulk-send today's 111 remaining invoices himself this afternoon (Daniel Okafor, 10:52); not confirmed done

### Tried so far
- 12 Nov 10:15 Priya Nair: manual Send of INV-2026-11-0457 → accepted by recipient's mail server 10:16 [Verified, delivery log]
- 12 Nov ~10:15-10:20 Priya Nair: re-save of one schedule plus test-mode run → dispatched within 40 s; real run not tested [Verified, job/test result in internal note]
- 12 Nov 10:34 Priya Nair: gave the customer a workaround for today, bulk Send of Queued invoices, 50 at a time → result not recorded; customer said he would do it this afternoon [Reported]

### Commitments to the customer
- Email an update by 16:00 UTC today "with what they've found, even if that is only that they are still investigating" | made by Priya Nair, Support Agent Tier 1, on 12 Nov 11:05 | due 12 Nov 16:00 UTC | open, 4h 30m remaining; now owned by Tier 2 (policy 5.2)
- Make sure engineering knows the next run is 07:00 UTC on 13 Nov with 64 invoices | made by Priya Nair on 12 Nov 11:05 | no time given | met (stated in the 11:30 escalation note)
- Not a commitment: Priya declined to guarantee a fix time before tomorrow's run ("I can't promise a fix time").

### Service level
- Priority recorded as P2 (unchanged at escalation); the evidence points to P3. Policy 2.2 (P2) requires "no practical workaround", while 2.3 (P3) covers "impaired but a practical workaround exists". Manual bulk Send is verified to work and the customer accepted it for today, though it is laborious. Per 2.5 the priority stays P2 until an agent records a change. Computed for P3 as the supported priority, with P2 shown; plan Enterprise (3.1, 1.3).
- Clock: starts at ticket creation 09:14 UTC 12 Nov (4.1); no "Pending customer" time so no pause (4.2); no pause time recorded.
- P3 first response, 4 business hours (3.1): deadline 12 Nov 13:14 (09:14 + 4h, inside 08:00-18:00 Thursday) | met (Priya replied 09:41, 27 min; the 09:41 reply is not automated, 1.4)
- P3 resolution, 30 business hours (3.1, 3.3): deadline 17 Nov 09:14 (Thu 8h46 to 18:00, Fri 10h = 18h46, Mon 10h = 28h46, +1h14 on Tue; assumes no English bank holiday 13-17 Nov) | open, 27h 44m of business time remaining; within target (at risk below 7.5 business hours, 4.5)
- If P2 stands: first response 2 hours 24x7, deadline 11:14 | met. Resolution 24 hours 24x7, deadline 13 Nov 09:14 (09:14 + 24h) | open, 21h 44m remaining; within target (at risk below 6h). The 07:00 UTC run on 13 Nov falls before this deadline.
- Customer update cadence (7.1): P2 at least once each business day (met today by Priya's 10:34 update; the 16:00 update covers it); P3 update when there is news.
- Duty Manager (5.3): needed only if a P2 is breached; not breached.

### Recommended next action
Tier 2 engineer: by 15:00 UTC today, establish whether this is KI-3381 (compare against the linked cases and the account's pre-v8.3 schedules) and whether a server-side fix or bulk repair of the 340 schedules is possible before 13 Nov 07:00 UTC, so Priya's 16:00 UTC update to Daniel can state findings. Why: the only verified facts are the stuck dispatch and a single-schedule test-mode fix, and the next run (64 invoices) is about 19.5 hours away. Do not promise a fix date to the customer (6.2).
Then: (1) in the 16:00 update, tell Daniel which schedules to re-save before tomorrow's run if no fix is ready (64 schedules is more feasible than 340) and to bulk-send manually if it still fails; (2) after 13 Nov 07:00 UTC, check whether the run dispatched and whether the post-10-Nov schedules behave differently.

### Gaps
- Cause is not confirmed to be KI-3381; the re-save fix is verified only in test mode, not on a real scheduled run.
- Priority is P2 on the ticket but the evidence supports P3 (workaround exists); needs an agent decision, and any priority change should be recorded on the ticket (2.5, 4.4).
- Unknown whether the customer has bulk-sent today's 111 invoices; the "111" is Priya's/Daniel's figure (112 minus the manual send), and the customer's own estimate was ~110.
- Which 64 invoices/schedules are due tomorrow is not listed; the 13 and 15 Nov counts are customer-reported.
- Whether any bank holiday falls on 13-17 Nov is not in the supplied material (assumed none).
- No promises of credit, refund or fix date found in the thread; account record shows no credits or refunds.
