# Escalation handoff: QB-204518 Recurring invoices created but not sent

**Customer:** Harrow & Finch Accounting Ltd, HF-0192, Quillbill Practice, support level Enterprise (account record)  **Priority:** P2 (unchanged at escalation, thread 11:30)  **Prepared:** 2026-11-12 11:30 UTC (the as-of time of the ticket export, thread header)

## Service level
| Clock | Policy clause | Started | Deadline | Status |
|---|---|---|---|---|
| First response (Enterprise P2: "2 hours, 24x7") | 3.1, 3.3, 1.4 | 2026-11-12 09:14 UTC (ticket created, 4.1) | 2026-11-12 11:14 UTC | Met: first agent reply by Priya Nair at 09:41 UTC (27 min) |
| Resolution (Enterprise P2: "24 hours, 24x7") | 3.1, 3.3, 4.1, 4.5 | 2026-11-12 09:14 UTC | 2026-11-13 09:14 UTC | Running, within target: 21 h 44 min remaining at 11:30 UTC |
| Customer update (P2: "at least once each business day") | 7.1 | 2026-11-12 | Each business day; 12 and 13 Nov are Thursday and Friday | Running; first update due today (see Commitments) |

Arithmetic: first response 09:14 + 2 h = 11:14; reply at 09:41 is before that. Resolution 09:14 + 24 h (calendar time, 3.3) = 13 Nov 09:14; 13 Nov 09:14 minus 12 Nov 11:30 = 21 h 44 min. "At risk" under 4.5 means under 25% of 24 h = 6 h remaining, so the ticket becomes at risk at 03:14 UTC on 13 Nov, before the 07:00 UTC run. No "Pending customer" status appears in the thread (status went New, Open, Escalated), so no paused time (4.2). Support-level clauses do not depend on business hours here. Policy 5.3 (Duty Manager) applies only if the P2 is breached; it is not breached now.

## Problem as currently understood
The 07:00 UTC recurring run on 12 Nov generated 112 invoices that were all left "Queued - not dispatched", with no send attempts and no errors. All 112 come from schedules created before the v8.3 release of 10 Nov. This is the leading suspected match for known issue KI-3381 (legacy schedules skip auto-send after v8.3), but the cause is not confirmed. Manual send works, and re-saving a schedule restored sending in test mode only.

| Fact | Status | Evidence |
|---|---|---|
| 112 invoices generated at 07:00:03 UTC on 12 Nov, all "Queued - not dispatched", 0 send attempts, no errors | Verified | Priya's job log check, internal note 10:20 |
| Customer said "around 110" invoices, all "Queued" | Reported, superseded by the verified count above | Daniel 09:14 |
| All 112 come from schedules created before 10 Nov (v8.3 release) | Verified | Internal note 10:20 (job log) |
| Manual send of INV-2026-11-0457 works (accepted by recipient mail server 10:16) | Verified | Test 1, delivery log, internal note 10:20 |
| Re-saving schedule "Meadowgate monthly retainer" unchanged, then "Run now (test mode)", dispatched in under 40 s | Verified for one schedule in test mode only | Test 2, internal note 10:20 |
| Re-save fixes automatic sending on real scheduled runs | Suspected | Note 10:20: "Not yet seen on a real scheduled run" |
| Cause is KI-3381 | Suspected | Note 10:20: "Symptoms match. Not confirmed as the same cause." Priya 10:34: "I can't yet confirm" |
| Schedules created after 10 Nov behave correctly | Suspected / untested | Note 10:20: 3 such schedules, none due today, "no direct comparison yet" |
| No client received an invoice | Reported | Daniel 09:14 ("As far as we can tell"); only Meadowgate's test send is verified delivered |
| Two clients have rung to ask where their invoice is | Reported | Daniel 09:14 |
| No settings changed on customer side | Reported | Daniel 09:14 |
| Client payment terms run from send date, so delay pushes back collections | Reported | Daniel 09:14 |
| Next runs: 13 Nov 07:00 UTC with 64 invoices, 15 Nov with 90 invoices | Reported (the 64 is repeated by Priya as the customer's figure) | Daniel 10:52; Priya 11:05 |
| 340 active recurring schedules | Verified | Account record (as of 1 Nov 2026; at least 3 more created since 10 Nov per the note) |
| Customer plans to bulk-send today's 111 remaining invoices himself this afternoon | Reported intention, not confirmed done | Daniel 10:52 |

Contradictions:
- Invoice count: Daniel said "around 110" (09:14); the job log shows 112 (note 10:20). The log version is verified.
- Schedule count: the account record says 340 active schedules "as of 1 November", yet the note says 3 schedules were created after 10 Nov, so the current total is probably 343 or the figure is stale. Daniel also says "we have 340". Not resolved in the case.
- Re-save claim: the customer message (10:34) says re-saving "appeared to restore automatic sending"; the internal note (10:20) says this was seen only in test mode, which sends to the account owner only.
- Priority: Daniel asked for it to be treated as "urgent" (09:14); recorded priority is P2 and no change was recorded (policy 2.5).

## What has been tried
| When (UTC) | Who | Action | Result |
|---|---|---|---|
| 12 Nov 10:15 | Priya Nair | Manual Send of INV-2026-11-0457 (customer consented 09:58) | Accepted by Meadowgate's mail server 10:16 |
| 12 Nov ~10:15-10:20 | Priya Nair | Re-saved schedule "Meadowgate monthly retainer" unchanged, then "Run now (test mode)" | Test invoice dispatched within 40 s, test mode only |
| 12 Nov 10:20 | Priya Nair | Checked job log and dispatcher; found known issue KI-3381 (opened 11 Nov, Investigating, 2 other customers linked) | Symptoms match; cause not confirmed |
| 12 Nov 10:34 | Priya Nair | Gave customer workaround: filter invoice list by "Queued", select up to 50 at a time, Send | Customer said he will bulk-send the 111 this afternoon (10:52); result not recorded |
| 12 Nov 11:30 | Priya Nair | Escalated to Tier 2 (Product Engineering Support), linked to KI-3381 | Status Escalated; priority P2 unchanged |
| 12 Nov | Customer | No settings changed on his side | Reported only |

## Commitments to the customer
Policy 5.2: from escalation, Tier 2 owns the ticket, including commitments already made.

| When (UTC) | Made by | Commitment (quoted) | Due | State |
|---|---|---|---|---|
| 12 Nov 11:05 | Priya Nair | "I will email you an update by 16:00 UTC today with what they've found, even if that is only that they are still investigating." | 12 Nov 16:00 UTC | Open (4 h 30 min after the as-of time) |
| 12 Nov 11:05 | Priya Nair | "I'll make sure they know your next run is at 07:00 UTC tomorrow, 13 November, with 64 invoices." | Not stated | Met on the record: the escalation note 11:30 gives the 13 Nov 07:00 UTC run and 64 invoices |
| 12 Nov 11:05 | Priya Nair | "I can't promise a fix time" (a refusal to guarantee, not a promise; the customer's question "Can you guarantee this will be fixed before tomorrow morning's run?" was not answered with a guarantee) | Not applicable | No fix date has been promised. Policy 6.2 forbids promising one |

No service credit or refund has been offered. The account record shows no credits and no refunds, and policy 6.3 reserves them to the Customer Success Manager (Elena Marsh) or the Head of Support.

## Recommended next action
Test the leading suspected cause on a real scheduled run before the 07:00 UTC run on 13 Nov. In the invoice list or schedules for HF-0192, pick a schedule that is due on 13 Nov (among the 64 invoices), and also check whether any of the 3 schedules created after 10 Nov is due soon. Ask Daniel for consent to re-save one or a few of tomorrow's due legacy schedules unchanged, as was done for Meadowgate. Check the dispatcher and job log at 07:00 UTC on 13 Nov, comparing those schedules against untouched pre-v8.3 schedules due the same morning. Share the HF-0192 job log with the KI-3381 owner and ask Engineering whether a bulk fix, such as a bulk re-save or re-queue, is possible for all 340 schedules.
- Confirms the suspected cause and fix: the re-saved schedules dispatch at 07:00 and the untouched legacy ones stay "Queued - not dispatched". Engineering linking the job-log signature to KI-3381 confirms the cause.
- Rules it out: re-saved schedules also stay queued, or a post-10 Nov schedule also fails.
- Racing against: the update due by 16:00 UTC on 12 Nov, then the 13 Nov 07:00 UTC run (64 invoices), the resolution deadline of 13 Nov 09:14 UTC, and the at-risk point at 03:14 UTC on 13 Nov. Do not promise the customer a fix date (policy 6.2).

Open questions:
- Did Daniel actually bulk-send the 111 queued invoices this afternoon, and did they deliver? (result not recorded)
- Is the cause the same as KI-3381, and does Engineering have a fix, workaround or bulk remediation and a timeline?
- Do the 3 schedules created after 10 Nov send correctly?
- What is the current schedule count (account record shows 340 as of 1 Nov)?
- Which schedules are due on 13 Nov and 15 Nov, and are any of the 64 and 90 invoices tied to time-sensitive clients?
- Are the two clients who rang the same as ones awaiting invoices? Not stated.
