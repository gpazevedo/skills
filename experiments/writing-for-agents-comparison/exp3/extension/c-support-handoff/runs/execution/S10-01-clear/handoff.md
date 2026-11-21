# Escalation handoff: QB-204518 | Harrow & Finch Accounting Ltd (HF-0192) | Recurring invoices generated but never dispatched after v8.3

**Service level:** Resolution due 2026-11-13 09:14 UTC (Enterprise P2, 24 hours, 24x7, policy 3.1) | Pending, 21 h 44 min remaining as of 2026-11-12 11:30 UTC (latest thread timestamp). The customer's next run, 2026-11-13 07:00 UTC, falls before that deadline.

## Problem as currently understood
The 07:00 UTC recurring run on 2026-11-12 generated 112 invoices for HF-0192, and all 112 sit in dispatch state "Queued - not dispatched" with 0 send attempts and no errors (Verified, Priya Nair, 10:20 UTC). All 112 come from schedules created before the 10 Nov v8.3 release (Verified), and the symptoms match known issue KI-3381, but the shared cause is only Suspected. Manual sending works for one invoice (Verified), and re-saving one schedule restored dispatch in test mode only (Verified for test mode); whether re-saving fixes a real scheduled run is Suspected. The customer reports 340 schedules and further runs on 13 Nov 07:00 (64 invoices) and 15 Nov (90 invoices).

| Statement | Label | Source (author, timestamp) |
| --- | --- | --- |
| Around 110 invoices should have been emailed at 07:00 on 12 Nov | Reported | Daniel Okafor, 2026-11-12 09:14 UTC |
| The run generated 112 invoices at 07:00:03 UTC | Verified (job log) | Priya Nair, internal note, 2026-11-12 10:20 UTC |
| All 112 are in dispatch state "Queued - not dispatched"; dispatcher shows 0 send attempts and no errors | Verified (job log, dispatcher) | Priya Nair, internal note, 2026-11-12 10:20 UTC |
| No client has received an invoice; two clients have phoned asking for theirs | Reported | Daniel Okafor, 2026-11-12 09:14 UTC |
| Customer has changed no settings | Reported | Daniel Okafor, 2026-11-12 09:14 UTC |
| All 112 invoices come from schedules created before 10 Nov (v8.3 release) | Verified (job log) | Priya Nair, internal note, 2026-11-12 10:20 UTC |
| Account has 3 schedules created after 10 Nov; none was due on 12 Nov, so no comparison exists | Verified | Priya Nair, internal note, 2026-11-12 10:20 UTC |
| Cause is KI-3381 "Legacy recurring schedules skip auto-send after v8.3" (Engineering, opened 11 Nov, Investigating, 2 other customers linked) | Suspected | Priya Nair, internal note, 2026-11-12 10:20 UTC ("Not confirmed as the same cause") |
| Re-saving a pre-v8.3 schedule clears the fault for real scheduled runs | Suspected (seen only in test mode, one schedule) | Priya Nair, internal note, 2026-11-12 10:20 UTC |
| Customer has 340 schedules (account record: 340 active as of 1 Nov 2026) | Reported | Daniel Okafor, 2026-11-12 10:52 UTC |
| Next runs: 13 Nov 07:00 with 64 invoices; 15 Nov (Sunday, time not stated) with 90 invoices | Reported | Daniel Okafor, 2026-11-12 09:14 and 10:52 UTC |
| Clients' payment terms run from send date, so delay pushes back collections | Reported | Daniel Okafor, 2026-11-12 09:14 UTC |

## What has been tried
| Action | By | When | Result | Label |
| --- | --- | --- | --- | --- |
| Reviewed the recurring-run job log and dispatcher for HF-0192 | Priya Nair (Tier 1) | Before 2026-11-12 10:20 UTC (note time) | 112 invoices generated, all "Queued - not dispatched", 0 send attempts, no errors; all from pre-v8.3 schedules | Verified |
| Checked known issues | Priya Nair (Tier 1) | Before 2026-11-12 10:20 UTC | KI-3381 symptoms match; same cause not confirmed | Suspected |
| Manual Send of INV-2026-11-0457 (Meadowgate Ltd) from the invoice list, with customer consent given at 09:58 UTC | Priya Nair (Tier 1) | 2026-11-12 10:15 UTC | Delivery log shows it accepted by recipient's mail server at 10:16 UTC | Verified |
| Re-saved schedule "Meadowgate monthly retainer" without changes, then "Run now (test mode)" (sends to account owner only) | Priya Nair (Tier 1) | Before 2026-11-12 10:20 UTC (exact time not recorded) | Test invoice dispatched within 40 seconds; not yet observed on a real scheduled run | Verified (test mode only) |
| Bulk-send of the remaining 111 invoices from the invoice list (filter "Queued", up to 50 at a time), as advised by Priya at 10:34 UTC | Customer (Daniel Okafor's team), planned | Planned for afternoon of 2026-11-12 (stated 10:52 UTC) | Not done as of the latest thread entry; outcome unknown | Reported |

## Commitments to the customer
| Commitment (quoted) | Made by (name, role) | When | Due | Status |
| --- | --- | --- | --- | --- |
| "I'm escalating your ticket to our Product Engineering Support team now" | Priya Nair, Support Agent, Tier 1 | 2026-11-12 11:05 UTC | "now" (no date given) | Kept: escalated to Tier 2 at 11:30 UTC |
| "I'll make sure they know your next run is at 07:00 UTC tomorrow, 13 November, with 64 invoices." | Priya Nair, Support Agent, Tier 1 | 2026-11-12 11:05 UTC | No date given | Kept: stated in the 11:30 UTC escalation note |
| "I will email you an update by 16:00 UTC today with what they've found, even if that is only that they are still investigating." | Priya Nair, Support Agent, Tier 1 | 2026-11-12 11:05 UTC | 2026-11-12 16:00 UTC ("by 16:00 UTC today") | Outstanding; Tier 2 now owns it (policy 5.2) |

Claimed by the customer but not found in the thread: None. (The customer asked at 10:52 UTC for a guarantee of a fix before the 13 Nov run; Priya declined at 11:05 UTC: "I can't promise a fix time".)

## Service level
- Tier: Enterprise (account record, "Support level: Enterprise")
- Priority: P2, recorded at ticket creation and unchanged at escalation (2026-11-12 11:30 UTC)
- Timestamps: all thread timestamps are UTC (thread header; policy 1.2). The ticket status was never "Pending customer", so no clock pause applies (policy 4.2).
- First response: 2 hours, 24x7, clock start 2026-11-12 09:14 UTC (ticket created, policy 4.1); deadline 2026-11-12 11:14 UTC; Met (first agent reply 09:41 UTC); policy 3.1, 1.4.
- Resolution: 24 hours, 24x7, clock start 2026-11-12 09:14 UTC; deadline 2026-11-13 09:14 UTC; Pending, 21 h 44 min remaining, within target; becomes "at risk" when less than 6 h (25%) remains, at 2026-11-13 03:14 UTC; policy 3.1, 3.3, 4.5.
- Customer updates: P2 requires an update at least once each business day; business days in play are Thu 12 Nov and Fri 13 Nov (08:00 to 18:00 UTC, which equals Europe/London GMT in this period); 14 and 15 Nov are a weekend; status for 12 Nov Pending (the 16:00 UTC commitment would satisfy it); policy 7.1, 1.1.
- If unresolved at 2026-11-13 09:14 UTC the ticket is breached and the Support Duty Manager must be told (policy 5.3).
- Status as of: 2026-11-12 11:30 UTC (latest timestamp in the thread; current time not supplied)

## Recommended next action
The Tier 2 engineer should confirm with the Engineering team on KI-3381, before the 16:00 UTC update is due, whether HF-0192's stuck invoices share the KI-3381 cause and whether re-saving a pre-v8.3 schedule is a validated fix for real scheduled runs, given that the only evidence so far is one test-mode run. If confirmed, the plan for the 13 Nov 07:00 UTC run (64 invoices) becomes re-saving the schedules due in it, or an engineering-side fix; if not, the customer must be told in the 16:00 UTC update to expect a manual bulk-send again.

## Open questions
- Current time was not supplied; all statuses are as of the latest thread timestamp, 2026-11-12 11:30 UTC. Please confirm the current time and whether the 16:00 UTC update was sent; recompute statuses if later.
- KI-3381 match is unconfirmed (Priya Nair, 10:20 UTC). Needs Engineering confirmation.
- Re-save workaround has been seen only in test mode, on one schedule. No post-v8.3 schedule for this account has yet run, so there is no direct comparison.
- How many of the schedules due on 13 Nov (64 invoices) and 15 Nov (90 invoices) are pre-v8.3 is not recorded. The time of the 15 Nov run is not stated in the thread.
- Whether the customer completed the bulk-send of the remaining 111 invoices on 12 Nov is not confirmed.
- Invoice count: customer said "around 110"; job log shows 112. The job log is used.
- Schedule count: customer and account record both say 340 (record dated 1 Nov), but the thread notes 3 schedules created after 10 Nov; the exact current count of pre-v8.3 schedules is unknown.
- Priority fit: P2 is as recorded. Policy 2.2 defines P2 as having "no practical workaround", while 2.3 (P3) applies when one exists. A manual bulk-send (Verified for one invoice) exists; whether support judges it practical for runs of 64 to 112 invoices across 340 schedules is not decided in the thread. A change to P3 would move resolution to 30 business hours counted from creation (policy 4.4).
- Policy 1.5 defines resolution as a fix or workaround that "restores the affected function"; the policy does not say whether manual sending or per-schedule re-saving counts as restoring automatic sending. This decides when the ticket can be set to Resolved.
- Policy 7.1 does not say by what time of day the daily P2 update is due, and requires no weekend update, although the customer has a run on Sunday 15 Nov.
- The customer asked to "treat this as urgent" (Daniel Okafor, 09:14 UTC) and for a guaranteed fix before 13 Nov 07:00 UTC (10:52 UTC). Reported, not followed: priority remains as recorded, and policy 6.2 bars promising a fix date.
