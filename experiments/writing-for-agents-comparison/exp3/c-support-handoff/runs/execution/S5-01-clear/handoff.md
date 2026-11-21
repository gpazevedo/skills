## Escalation handoff: QB-204518 Recurring invoices generated but never dispatched (stuck "Queued")
As of: 2026-11-21 15:34 UTC (Saturday; environment clock). The supplied thread ends at 2026-11-12 11:30 UTC.
Customer: Harrow & Finch Accounting Ltd (HF-0192), Quillbill Practice plan, Enterprise support; Quillbill Invoicing (cloud), Recurring Billing add-on (340 active schedules as of 1 Nov 2026), Bank Feeds; UK data region; primary technical contact Daniel Okafor; CSM Elena Marsh (account record)

### Problem as currently understood
The 12 Nov 07:00 UTC recurring run generated 112 invoices, but none was dispatched: all sit in "Queued - not dispatched" with zero send attempts and no errors. All 112 come from schedules created before the v8.3 release on 10 Nov, which matches known issue KI-3381 ("Legacy recurring schedules skip auto-send after v8.3"); that match is a symptom match only, not a confirmed cause, so confidence in it is moderate. Manual sending works, and re-saving one schedule restored sending in test mode only.
Evidence:
- [Verified] 07:00:03 run generated 112 invoices, all "Queued - not dispatched", dispatcher shows 0 send attempts and no errors (Priya Nair, job log, 12 Nov 10:20)
- [Verified] All 112 are from schedules created before 10 Nov; the 3 schedules created after 10 Nov were not due, so no comparison exists (Priya Nair, job log, 12 Nov 10:20)
- [Verified] KI-3381 is open, status Investigating, 2 other customers linked; ticket linked to it at escalation (Priya Nair, 12 Nov 10:20 and 11:30). Same cause not confirmed.
- [Verified] Account has 340 active recurring schedules as of 1 Nov (account record)
- [Reported] About 110 invoices should have gone at 07:00; no client received one; two clients phoned (Daniel Okafor, 12 Nov 09:14)
- [Reported] No settings changed on the customer's side (Daniel Okafor, 12 Nov 09:14)
- [Reported] Next runs: 13 Nov 07:00 UTC with 64 invoices, 15 Nov with 90 invoices; payment terms run from send date (Daniel Okafor, 12 Nov 09:14 and 10:52)

### Tried so far
- 12 Nov 10:15 Priya Nair: manual Send of INV-2026-11-0457 (Meadowgate Ltd), with customer's consent → accepted by recipient mail server 10:16 [Verified]
- 12 Nov ~10:20 Priya Nair: re-saved schedule "Meadowgate monthly retainer" unchanged, then "Run now (test mode)" (sends to account owner only) → dispatched within 40 seconds; not yet seen on a real scheduled run [Verified]
- 12 Nov 10:34 Priya Nair: gave workaround to bulk-send queued invoices from the invoice list, 50 at a time → customer said they would send the other 111 that afternoon; result not recorded [Reported]
- 12 Nov 11:30 Priya Nair: escalated to Tier 2, linked KI-3381 → no Tier 2 activity in the thread [Verified]

### Commitments to the customer
- Email update "by 16:00 UTC today with what they've found, even if that is only that they are still investigating" | made by Priya Nair, Support Agent Tier 1, on 12 Nov 11:05 | due 12 Nov 16:00 UTC | missed (no update recorded; overdue by 8 d 23 h 34 m). Tier 2 now owns it (policy 5.2).
- "I'll make sure they know your next run is at 07:00 UTC tomorrow, 13 November, with 64 invoices" | Priya Nair, Tier 1, 12 Nov 11:05 | no time given | met (escalation note 11:30)
- Escalate to Product Engineering Support "now" | Priya Nair, Tier 1, 12 Nov 11:05 | no time given | met (11:30)
- Workaround: bulk-send queued invoices, up to 50 at a time | Priya Nair, Tier 1, 12 Nov 10:34 | n/a | met (provided)

### Service level
- Priority P2 under 2.2 ("a major function, such as invoice sending ... does not work and there is no practical workaround"); support level Enterprise (account record). Automatic sending is not restored and re-saving 340 schedules is reported as not realistic, so P2 is supported; manual bulk send could be argued as a practical workaround (P3, 2.3), noted below.
- First response (3.1, Enterprise P2 "2 hours, 24x7"; 4.1 clock starts at creation): deadline 12 Nov 11:14 UTC (09:14 + 2 h) | met (Priya Nair replied 09:41)
- Resolution (3.1, Enterprise P2 "24 hours, 24x7"; 4.2 no "Pending customer" status in thread, so no pause): deadline 13 Nov 09:14 UTC (12 Nov 09:14 + 24 h) | breached by 8 d 6 h 20 m (no Resolved status in thread)
- P2 update interval (7.1 "an update at least once each business day"): first due by end of business day Fri 13 Nov 18:00 UTC (1.1, GMT = UTC) | breached by 7 d 21 h 34 m; no updates recorded for 13, 16, 17, 18, 19 or 20 Nov
- If P3 instead: resolution 30 business hours (3.1, 3.3) → Tue 17 Nov 09:14 UTC (8 h 46 m Thu + 10 h Fri + 10 h Mon + 1 h 14 m Tue) | breached by 38 h 46 m business hours

### Recommended next action
Now, the Tier 2 owner: check the HF-0192 job log and dispatch state for every recurring run since 13 Nov 07:00 UTC and email Daniel Okafor an update with what you find, because the promised 12 Nov 16:00 update and all daily P2 updates are missed and the resolution target has been breached since 13 Nov 09:14 UTC.
Then: notify the Support Duty Manager that this P2 is breached (policy 5.3) and loop in CSM Elena Marsh; confirm with Engineering whether HF-0192 has the KI-3381 cause (compare pre- and post-10 Nov schedules in the later runs) and whether a bulk fix or bulk re-save across the 340 schedules is possible.

### Gaps
- Nothing after 12 Nov 11:30 UTC is in the supplied thread. Every "missed" and "breached" status above assumes the export is complete; if later updates, a status change or a fix exist, recheck them.
- Root cause unconfirmed: KI-3381 match is by symptom only; the re-save fix is seen once, in test mode, on one schedule (that schedule's next real run is monthly).
- Whether the customer bulk-sent the other 111 invoices, and whether the 13 and 15 Nov runs (64 and 90 invoices, customer-reported counts) dispatched, is not recorded.
- Customer asked for a guarantee of a fix before the 13 Nov 07:00 run; not agreed (Priya declined; policy 6.2 bars fix dates).
- Policy silences: 7.1 does not say by what time in a business day the P2 update is due (used end of business hours, 18:00 UTC); 2.2/2.3 do not say whether manual bulk send counts as a "practical workaround" (computed for P2, P3 shown).
- Support Duty Manager notification (5.3) not recorded.
