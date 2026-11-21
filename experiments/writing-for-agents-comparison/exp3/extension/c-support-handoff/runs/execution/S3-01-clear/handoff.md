# Escalation handoff: QB-204518 Recurring invoices created but not sent

**Customer:** Harrow & Finch Accounting Ltd, account HF-0192, plan Quillbill Practice (annual), support level Enterprise  **Priority:** P2 (recorded at creation 2026-11-12 09:14 UTC; "unchanged" at escalation 11:30 UTC)  **Prepared:** 2026-11-21 18:35 UTC (Europe/London is GMT = UTC on this date, policy 1.1)

Note on timing: the ticket export ends at the escalation note of 2026-11-12 11:30 UTC. Nothing after that is in the case supplied. Every "overdue" or "breached" status below means "no later record in the export"; if Tier 2 has history outside this export, recheck those rows first.

## Service level
| Clock | Policy clause | Started | Deadline | Status |
|---|---|---|---|---|
| First response | 3.1 "Enterprise / P2 / First response: 2 hours, 24x7"; 1.4 "the first reply to the customer from a support agent" | 2026-11-12 09:14 UTC (ticket created, 4.1) | 2026-11-12 11:14 UTC | Met (Priya Nair replied 09:41 UTC, after 27 min) |
| Resolution | 3.1 "Enterprise / P2 / Resolution: 24 hours, 24x7"; 3.3 "Targets marked '24x7' run on calendar time" | 2026-11-12 09:14 UTC (4.1) | 2026-11-13 09:14 UTC | Breached, 8 d 9 h 21 min ago |
| Customer updates | 7.1 "P2 tickets: an update at least once each business day" | 2026-11-12 (first business day) | Each business day (1.1: Mon to Fri, 08:00 to 18:00 Europe/London) | Met on 12 Nov; no update recorded for 13, 16, 17, 18, 19 or 20 Nov, so overdue |

- First response: 09:14 + 2 h = 11:14 UTC; reply at 09:41 is 27 min after creation. Met.
- Resolution: 09:14 on 12 Nov + 24 h calendar = 09:14 on 13 Nov. No "Pending customer" status anywhere in the thread (statuses were New, Open, Escalated), so no paused time (4.2, 4.3). Status is Escalated, not Resolved (1.5). 2026-11-21 18:35 minus 2026-11-13 09:14 = 8 d 9 h 21 min past deadline. For reference: "at risk" (4.5, under 25% of 24 h = 6 h left) began 2026-11-13 03:14 UTC; at the last thread entry (12 Nov 11:30) 21 h 44 min remained.
- Customer updates: the policy does not say when a "business day" ends for this clock. Read as the 18:00 close of business hours, the first missed update was due 2026-11-13 18:00 UTC; read as the calendar day, 2026-11-13 23:59 UTC. Overdue under both readings.
- Priority note: support has a workaround on record (manual bulk send, Priya 10:34), which is closer to the P3 definition (2.3 "a practical workaround exists") than P2 (2.2 "no practical workaround"). The recorded priority is P2 and only a recorded change counts (2.5), so P2 applies. Under a P3 reading (3.1 "30 business hours", 4.4 counted from creation) the deadline would be 2026-11-17 09:14 UTC (Thu 8 h 46 min + Fri 10 h + Mon 10 h + Tue 1 h 14 min): also breached.
- Policy 5.3: "The Support Duty Manager must be told of ... every P2 ticket that is breached." No record that this has happened.

## Problem as currently understood
The 07:00 UTC recurring run on 12 Nov generated 112 invoices, all from schedules created before the 10 Nov v8.3 release, and the dispatcher never attempted to send any of them, with no errors logged. The leading suspected cause is known issue KI-3381 "Legacy recurring schedules skip auto-send after v8.3", which is not yet confirmed as the same cause. Manual sending works, and re-saving one schedule restored dispatch in test mode only.

| Fact | Status | Evidence |
|---|---|---|
| 12 Nov 07:00:03 UTC run generated 112 invoices, all in dispatch state "Queued - not dispatched" | Verified | Customer reported "around 110 invoices" showing "Queued" (Daniel 09:14); job log read by Priya (internal note 10:20) |
| Dispatcher shows 0 send attempts and no errors for the 112 | Verified | Job log (Priya internal note 10:20); consistent with customer's "not one client has received theirs" (Daniel 09:14) |
| Two clients rang asking where their invoice was | Reported | Daniel 09:14 |
| Customer changed no settings | Reported | Daniel 09:14 |
| All 112 come from schedules created before 10 Nov (v8.3 release) | Verified | Job log (Priya internal note 10:20) |
| Account has 3 schedules created after 10 Nov; none was due 12 Nov, so no comparison with post-v8.3 schedules yet | Verified | Priya internal note 10:20 |
| Cause is KI-3381 | Suspected | Priya internal note 10:20: "Symptoms match. Not confirmed as the same cause." Ticket linked to KI-3381 at escalation (event 11:30) |
| KI-3381 opened by Engineering 11 Nov, status Investigating, 2 other customers linked | Verified (as of 12 Nov 10:20) | Known-issues record read by Priya (internal note 10:20) |
| Manual Send works for an affected invoice | Verified | INV-2026-11-0457 sent manually 10:15, accepted by recipient mail server 10:16 (delivery log, Priya internal note 10:20) |
| Re-saving the "Meadowgate monthly retainer" schedule, then "Run now (test mode)", dispatched within 40 s | Verified (one schedule, test mode only) | Priya internal note 10:20, Test 2 |
| Re-saving a schedule fixes real scheduled runs | Suspected | Priya internal note 10:20: "Not yet seen on a real scheduled run" |
| Customer has 340 recurring schedules | Verified (as of 1 Nov) | Account record "340 active schedules as of 1 November 2026"; Daniel 10:52 |
| Next runs: 13 Nov 07:00 UTC with 64 invoices; 15 Nov (Sunday) with 90 invoices, time not stated | Reported | Daniel 09:14 and 10:52; repeated in Priya escalation note 11:30 |
| Business impact: client payment terms run from send date, so delay pushes back collections; retainer clients billed on the 12th each month | Reported | Daniel 09:14 |

Contradictions:
- Invoice count: customer said "around 110 invoices" (Daniel 09:14); job log shows 112 (Priya internal note 10:20). The job log figure is verified.
- Schedule count: account record and customer give 340 schedules (record "as of 1 November 2026"; Daniel 10:52); Priya found 3 schedules created after 10 Nov (internal note 10:20). Whether the current total is 340 or 343, and so how many are pre-v8.3, is not stated.

## What has been tried
| When | Who | Action | Result |
|---|---|---|---|
| 2026-11-12 10:20 UTC (note time) | Priya Nair (Tier 1) | Reviewed HF-0192 job log for the 07:00 run | 112 invoices "Queued - not dispatched", 0 send attempts, no errors; all from pre-v8.3 schedules |
| 2026-11-12 10:20 UTC (note time) | Priya Nair | Checked known issues | KI-3381 matches symptoms; not confirmed as same cause |
| 2026-11-12 10:15 UTC | Priya Nair, with customer's permission (Daniel 09:58) | Manual Send of INV-2026-11-0457 to Meadowgate Ltd from the invoice list | Accepted by recipient mail server at 10:16 |
| 2026-11-12, before 10:20 UTC (exact time not stated) | Priya Nair | Re-saved "Meadowgate monthly retainer" without changes, then "Run now (test mode)" (sends to account owner only) | Test invoice dispatched within 40 s; not tested on a real scheduled run |
| 2026-11-12 afternoon (planned, Daniel 10:52) | Customer | Bulk-send the remaining 111 queued invoices, using the workaround Priya gave at 10:34 | Result not recorded |
| 2026-11-12 11:30 UTC | Priya Nair | Escalated to Tier 2, linked to KI-3381 | Status Escalated; priority P2 unchanged |

## Commitments to the customer
| When | Made by | Commitment (quoted) | Due | State |
|---|---|---|---|---|
| 2026-11-12 11:05 UTC | Priya Nair (Tier 1) | "I'm escalating your ticket to our Product Engineering Support team now" | 2026-11-12 (now) | Met (escalated 11:30 UTC) |
| 2026-11-12 11:05 UTC | Priya Nair (Tier 1) | "I'll make sure they know your next run is at 07:00 UTC tomorrow, 13 November, with 64 invoices." | Before 2026-11-13 07:00 UTC | Met (stated in escalation note 11:30 UTC) |
| 2026-11-12 11:05 UTC | Priya Nair (Tier 1) | "I will email you an update by 16:00 UTC today with what they've found, even if that is only that they are still investigating." | 2026-11-12 16:00 UTC | Overdue (no update in the export) |

Not committed: Priya said "I can't promise a fix time" (11:05) in reply to Daniel's request to "guarantee this will be fixed before tomorrow morning's run" (10:52). No credit or refund offered; account record shows "Open credits: None", "Refunds: None". Under policy 5.2 Tier 2 now owns all customer updates and these commitments.

## Recommended next action
Pull the HF-0192 job and dispatch logs for every recurring run after 2026-11-12 11:30 UTC, starting with 13 Nov 07:00 UTC (64 invoices) and 15 Nov (90 invoices). For each invoice record its dispatch state, send attempts, and whether its schedule was created before or after 10 Nov or was re-saved (the Meadowgate schedule). This turns the reported run sizes and the current customer impact into verified facts, and directly tests the suspected KI-3381 cause.

- Confirms KI-3381 as the cause: pre-v8.3 schedules again show "Queued - not dispatched" with 0 attempts, while any post-v8.3 or re-saved schedule that ran was dispatched.
- Rules it out or widens scope: post-v8.3 or re-saved schedules also stuck, or errors now appear in the dispatcher.
- Also check in the same pass: whether the 111 invoices from 12 Nov were sent (customer's bulk send), and the current status of KI-3381.

This is racing obligations that are already past due: the resolution target (breached since 2026-11-13 09:14 UTC), the 16:00 UTC update promised on 12 Nov, and the daily P2 updates (7.1). The customer update and the Support Duty Manager notification (5.3) should go out as soon as the log check gives a current picture.

Open questions:
- Was the 16:00 UTC update on 12 Nov, or any later update, sent outside this export?
- Has the Support Duty Manager been told of the breach (5.3)?
- Does KI-3381 have a root cause, a fix, or a bulk workaround (for example a bulk re-save) that avoids re-saving 340 schedules by hand?
- What time does the 15 Nov run fire, and which further runs are due before the 12 Dec retainer run?
- How many of the customer's schedules were created before 10 Nov (340 vs 343 total, see contradictions)?
- Does re-saving fix real scheduled runs, not only test mode? The Meadowgate schedule's next real run is not stated.
