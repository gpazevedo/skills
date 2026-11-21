Clarifying question: What is the current time (and time zone) for measuring the service-level clocks and commitments? The thread export ends at 2026-11-12 11:30 UTC, so the statuses below are measured at that moment, with the change that follows if the current time is later stated beside each one.

# Escalation handoff: QB-204518 Recurring invoices from pre-v8.3 schedules generated but never dispatched

**Customer:** Harrow & Finch Accounting Ltd, HF-0192, Plan "Quillbill Practice (annual subscription)", Support level "Enterprise" (account record: Plan; Support level)   **Severity/priority:** P2, set at ticket creation and recorded "Priority: P2 (unchanged)" at escalation (thread: Event 2026-11-12 09:14 UTC; Event 2026-11-12 11:30 UTC). See Gaps on whether P2 still fits policy 2.2.
**Most urgent deadline:** Priya Nair's promised customer update, "by 16:00 UTC today" = 2026-11-12 16:00 UTC (thread: Priya Nair, 2026-11-12 11:05 UTC). Tier 2 now owns it: "From escalation, Tier 2 owns the ticket, including customer updates and any commitments already made to the customer" (policy 5.2). Next after that: the customer's next scheduled run, 2026-11-13 07:00 UTC (Reported), then the P2 resolution target, 2026-11-13 09:14 UTC (policy 3.1).

## Problem as currently understood
The 07:00 UTC recurring run on 12 Nov generated 112 invoices for HF-0192, and none was dispatched: all sit in "Queued - not dispatched" with 0 send attempts and no errors. All 112 come from schedules created before the v8.3 release of 10 Nov, which matches known issue KI-3381, but the shared cause is not confirmed. Manual sending works, and re-saving one schedule restored sending in test mode only; the customer has 340 schedules and further runs on 13 Nov (64 invoices) and 15 Nov (90 invoices).

| Fact | Status | How established / cite |
|---|---|---|
| The 07:00:03 UTC run on 12 Nov generated 112 invoices | Verified | Priya read the job log (thread: internal note, Priya Nair, 2026-11-12 10:20 UTC) |
| All 112 are in dispatch state "Queued - not dispatched"; dispatcher shows 0 send attempts and no errors | Verified | Priya read the job log and dispatcher (thread: internal note, Priya Nair, 2026-11-12 10:20 UTC) |
| "around 110 invoices should have been emailed at 07:00"; "they all show 'Queued'" | Reported | Customer (thread: Daniel Okafor, 2026-11-12 09:14 UTC). Count differs from the 112 in the job log; see Open disagreements |
| "not one client has received theirs" | Reported | Customer (thread: Daniel Okafor, 2026-11-12 09:14 UTC); consistent with the Verified 0 send attempts |
| "two clients have already rung to ask where it is" | Reported | Customer (thread: Daniel Okafor, 2026-11-12 09:14 UTC) |
| "We haven't changed any settings on our side." | Reported | Customer (thread: Daniel Okafor, 2026-11-12 09:14 UTC); not checked by support |
| Impact: "payment terms run from the send date, so every day this waits pushes back our collections" | Reported | Customer (thread: Daniel Okafor, 2026-11-12 09:14 UTC) |
| All 112 invoices come from schedules created before 10 Nov (the v8.3 release) | Verified | Priya checked schedule creation dates (thread: internal note, Priya Nair, 2026-11-12 10:20 UTC) |
| The account has 3 schedules created after 10 Nov; none was due on 12 Nov, so there is no comparison with a post-v8.3 schedule | Verified | Priya checked the account (thread: internal note, Priya Nair, 2026-11-12 10:20 UTC) |
| The fault is caused by schedule creation before v8.3 | Hypothesis | Inferred from the correlation above; untested because no post-10 Nov schedule has run (thread: internal note, Priya Nair, 2026-11-12 10:20 UTC) |
| The fault is KI-3381 "Legacy recurring schedules skip auto-send after v8.3" (opened by Engineering 11 Nov, status Investigating, 2 other customers linked) | Hypothesis | Priya: "Symptoms match. Not confirmed as the same cause." (thread: internal note, Priya Nair, 2026-11-12 10:20 UTC); ticket linked to KI-3381 (thread: Event 2026-11-12 11:30 UTC) |
| Manual Send works: INV-2026-11-0457 sent at 10:15 was accepted by the recipient's mail server at 10:16 | Verified | Priya read the delivery log (thread: internal note, Priya Nair, 2026-11-12 10:20 UTC) |
| After re-saving schedule "Meadowgate monthly retainer" without changes, "Run now (test mode)" dispatched the test invoice within 40 seconds | Verified | Priya ran the test (thread: internal note, Priya Nair, 2026-11-12 10:20 UTC) |
| Re-saving a schedule restores automatic sending on a real scheduled run | Hypothesis | "Not yet seen on a real scheduled run." (thread: internal note, Priya Nair, 2026-11-12 10:20 UTC) |
| Scope: customer has 340 schedules | Verified (as of 1 Nov) | Account record: "Recurring Billing add-on (340 active schedules as of 1 November 2026)"; also stated by customer (thread: Daniel Okafor, 2026-11-12 10:52 UTC) |
| Next runs: 13 Nov 07:00 UTC with 64 invoices; 15 Nov with 90 invoices | Reported | Customer (thread: Daniel Okafor, 2026-11-12 09:14 UTC and 10:52 UTC); repeated by Priya but not checked against schedules (thread: Priya Nair, 2026-11-12 11:05 UTC; internal note 11:30 UTC) |
| Product: Quillbill Invoicing, Recurring Billing add-on; data region UK | Verified | Account record: Products; Data region |

**Open disagreements:**
- Invoice count: customer says "around 110 invoices" (thread: Daniel Okafor, 2026-11-12 09:14 UTC); the job log shows 112 (thread: internal note, Priya Nair, 2026-11-12 10:20 UTC). Likely approximation, not reconciled.
- Schedule count: customer and account record give 340 schedules (account record: Products, "as of 1 November 2026"; thread: Daniel Okafor, 10:52 UTC), but the account has 3 schedules created after 10 Nov (thread: internal note, Priya Nair, 10:20 UTC), so the current count may differ from 340. Not reconciled.

## What has been tried
| When | Who | Action | Result | Cite |
|---|---|---|---|---|
| 2026-11-12, before 10:20 UTC | Priya Nair (Tier 1) | Read the HF-0192 job log and dispatcher for the 07:00 run | 112 invoices generated, all "Queued - not dispatched", 0 send attempts, no errors | thread: internal note, Priya Nair, 2026-11-12 10:20 UTC |
| 2026-11-12, before 10:20 UTC | Priya Nair (Tier 1) | Checked creation dates of the affected schedules | All 112 from schedules created before 10 Nov; 3 post-10 Nov schedules, none due today | thread: internal note, Priya Nair, 2026-11-12 10:20 UTC |
| 2026-11-12, before 10:20 UTC | Priya Nair (Tier 1) | Searched known issues | KI-3381 symptoms match; same cause not confirmed | thread: internal note, Priya Nair, 2026-11-12 10:20 UTC |
| 2026-11-12 10:15 UTC | Priya Nair (Tier 1), with customer consent (thread: Daniel Okafor, 09:58 UTC) | Test 1: manual Send of INV-2026-11-0457 from the invoice list | Accepted by recipient's mail server at 10:16 | thread: internal note, Priya Nair, 2026-11-12 10:20 UTC; Priya Nair, 10:34 UTC |
| 2026-11-12, before 10:20 UTC | Priya Nair (Tier 1) | Test 2: re-saved "Meadowgate monthly retainer" without changes, then "Run now (test mode)" (sends only to account owner) | Test invoice dispatched within 40 seconds; not yet seen on a real scheduled run | thread: internal note, Priya Nair, 2026-11-12 10:20 UTC |
| 2026-11-12 10:34 UTC | Priya Nair (Tier 1) | Gave the customer a workaround: filter "Queued", select up to 50, choose Send | Customer said they would bulk-send the 111 that afternoon; result not recorded | thread: Priya Nair, 10:34 UTC; Daniel Okafor, 10:52 UTC |
| 2026-11-12 afternoon (planned) | Customer (Daniel Okafor) | Bulk-send the remaining 111 invoices | not recorded | thread: Daniel Okafor, 2026-11-12 10:52 UTC |
| 2026-11-12 11:30 UTC | Priya Nair (Tier 1) | Escalated to Tier 2 (Product Engineering Support), linked to KI-3381 | Status Open → Escalated; Tier 2 outcome not recorded | thread: Event 2026-11-12 11:30 UTC; internal note 11:30 UTC |

## Commitments to the customer
| Commitment (verbatim) | Made by (role) | When / cite | Deadline | Kept / Open / Missed |
|---|---|---|---|---|
| "I'm looking at your account now." | Priya Nair (Support Agent, Tier 1) | thread: Priya Nair, 2026-11-12 09:41 UTC | None stated | Kept: job log findings recorded (thread: internal note, 10:20 UTC) |
| "I'm escalating your ticket to our Product Engineering Support team now" | Priya Nair (Support Agent, Tier 1) | thread: Priya Nair, 2026-11-12 11:05 UTC | "now" | Kept: escalated at 11:30 UTC (thread: Event 2026-11-12 11:30 UTC) |
| "I'll make sure they know your next run is at 07:00 UTC tomorrow, 13 November, with 64 invoices." | Priya Nair (Support Agent, Tier 1) | thread: Priya Nair, 2026-11-12 11:05 UTC | Implicitly at escalation | Kept: stated in escalation note (thread: internal note, Priya Nair, 2026-11-12 11:30 UTC) |
| "I will email you an update by 16:00 UTC today with what they've found, even if that is only that they are still investigating." | Priya Nair (Support Agent, Tier 1); now owned by Tier 2 under policy 5.2 | thread: Priya Nair, 2026-11-12 11:05 UTC | 2026-11-12 16:00 UTC | Open as of 11:30 UTC. If the current time is after 16:00 UTC on 12 Nov and no update is recorded, Missed. Within policy 6.1: "Support agents may commit to the time of the next update and to actions they will take themselves." |

Priya declined to promise a fix time ("I can't promise a fix time, because that depends on what engineering finds", thread: 2026-11-12 11:05 UTC), consistent with policy 6.2: "Support agents must not promise a fix date for a product defect". No credit or refund was offered (account record: "Open credits: None", "Refunds: None").

## Service-level status
Inputs: Support level "Enterprise" (account record: Support level; policy 1.3). Priority P2 (thread: Event 09:14 UTC and 11:30 UTC). Clock start: "The clock starts when the ticket is created." (policy 4.1), ticket created 2026-11-12 09:14 UTC (thread: Event 09:14 UTC). Pauses: "The clock is paused only while the ticket status is 'Pending customer'." (policy 4.2); the thread records statuses New, Open and Escalated only, so no paused time. Statuses measured at 2026-11-12 11:30 UTC (last thread entry; see clarifying question).

| Clock | Policy clause (quoted) | Started | Deadline (with arithmetic) | Status |
|---|---|---|---|---|
| First response | 3.1: "Enterprise \| P2 \| 2 hours, 24x7"; 3.3: "Targets marked '24x7' run on calendar time."; 1.4: "First response means the first reply to the customer from a support agent" | 2026-11-12 09:14 UTC (ticket created) | 09:14 + 2 h = 2026-11-12 11:14 UTC | Met: first agent reply 2026-11-12 09:41 UTC (Priya Nair), 27 minutes after creation |
| Resolution | 3.1: "Enterprise \| P2 \| ... \| 24 hours, 24x7"; 1.5: "Resolution means that Quillbill has provided a fix or a workaround that restores the affected function and the ticket status has been set to Resolved." | 2026-11-12 09:14 UTC (ticket created) | 09:14 + 24 h = 2026-11-13 09:14 UTC. At-risk threshold per 4.5 ("'at risk' if less than 25% of its resolution target remains"): 25% of 24 h = 6 h, so at risk from 09:14 − 6 h = 2026-11-13 03:14 UTC | Within target (on track) at 11:30 UTC: 2 h 16 min elapsed, 21 h 44 min remaining. If current time is from 13 Nov 03:14 UTC: at risk; after 13 Nov 09:14 UTC without status Resolved: breached, and policy 5.3 applies: "The Support Duty Manager must be told of ... every P2 ticket that is breached." |
| Customer update interval | 7.1: "P2 tickets: an update at least once each business day."; 1.1: "Business hours are 08:00 to 18:00 Europe/London time, Monday to Friday ... Between 25 October 2026 and 28 March 2027, Europe/London time is GMT, which is the same as UTC." | Business day Thu 2026-11-12 | For 12 Nov: met by updates at 10:34 and 11:05 UTC. Next: during business day Fri 2026-11-13, i.e. by 18:00 UTC (end of business hours per 1.1; the policy does not state a time within the day, so 18:00 is the latest reading). Then Mon 2026-11-16 by 18:00 UTC (Sat 14 and Sun 15 are not business days) | Met for 12 Nov; 13 Nov update open. If the current time is after 13 Nov 18:00 UTC with no recorded update, breached for 13 Nov |

## Recommended next action
Before the customer's 13 Nov 07:00 UTC run, have Product Engineering confirm whether HF-0192's stuck invoices are KI-3381 and whether there is an account-level fix for all affected pre-v8.3 schedules; as part of this, confirm the Hypothesis that re-saving a schedule restores automatic sending on a real scheduled run (so far shown only in test mode), and check the Reported 64-invoice count for 13 Nov against the account's schedules.

Evidence: all 112 undispatched invoices come from pre-10 Nov schedules with 0 send attempts and no errors, matching KI-3381's description, and re-save plus test-mode run dispatched within 40 seconds (thread: internal note, Priya Nair, 2026-11-12 10:20 UTC). Re-saving 340 schedules by hand "isn't realistic" for the customer (thread: Daniel Okafor, 10:52 UTC).

What it settles: whether the 13 Nov and 15 Nov runs will dispatch, and whether the customer must bulk-send manually again; whether a fix or workaround that "restores the affected function" (policy 1.5) exists for resolution.

Deadlines it must beat: first, the customer update promised "by 16:00 UTC today" (2026-11-12 16:00 UTC, thread: Priya Nair, 11:05 UTC), which Tier 2 now owns (policy 5.2) and which should carry whatever Engineering has found; then the 13 Nov 07:00 UTC run (Reported); then the P2 resolution target, 2026-11-13 09:14 UTC (at risk from 03:14 UTC).

## Gaps
- Current time not supplied: all statuses are measured at the last thread entry, 2026-11-12 11:30 UTC. Closed by the current time and time zone.
- 16:00 UTC update: no record of whether it was sent. Closed by checking outbound messages on the ticket after 11:30 UTC.
- Customer's bulk send of the 111 remaining 12 Nov invoices: result not recorded (thread: Daniel Okafor, 10:52 UTC). Closed by checking the dispatch state of the 12 Nov invoices.
- Tier 2 / Engineering findings on KI-3381 after escalation: not recorded. Closed by the KI-3381 status and any Tier 2 notes.
- Whether re-saving fixes a real scheduled run: not tested. Closed by observing a re-saved schedule's next real run.
- "We haven't changed any settings on our side": not checked. Closed by the account's settings audit history.
- Reported run sizes (64 on 13 Nov, 90 on 15 Nov) and the current schedule count (340 as of 1 Nov plus 3 created after 10 Nov): not reconciled against the account. Closed by listing the account's active schedules and their next run dates.
- Priority fit: the ticket is P2, defined as "a major function, such as invoice sending ... does not work and there is no practical workaround" (policy 2.2), but a manual-send workaround now exists, which matches P3 "a function is impaired but a practical workaround exists" (policy 2.3) if it is judged practical for 110+ invoices per run. No change has been recorded, and "a change takes effect only when a support agent records it on the ticket" (policy 2.5), so P2 targets apply. If a change to P3 were recorded, policy 4.4 would reset the resolution target to "Enterprise \| P3 \| ... \| 30 business hours", counted from creation. Closed by Tier 2 confirming the priority.
