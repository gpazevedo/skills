# Escalation handoff: QB-204518 Recurring invoices from pre-v8.3 schedules created but not sent

**Customer:** Harrow & Finch Accounting Ltd (HF-0192), Quillbill Practice plan, Enterprise support | **Priority:** P2 (recorded at ticket creation via the support portal, 2026-11-12 09:14 UTC; the thread does not say who set it; recorded "P2 (unchanged)" by Priya Nair at escalation, 11:30 UTC)
**Service level:** Within target, next deadline 2026-11-13 09:14 UTC (resolution; 21 h 44 min remaining at 2026-11-12 11:30 UTC; becomes "at risk" at 2026-11-13 03:14 UTC)
**Open commitments:** 1, earliest due 2026-11-12 16:00 UTC (update email to customer; Tier 2 now owns it under policy 5.2)

## Problem as currently understood
The customer's 07:00:03 UTC recurring run on 12 Nov generated 112 invoices, all stuck in "Queued - not dispatched" with 0 send attempts and no dispatcher errors, and all 112 come from schedules created before the 10 Nov v8.3 release (Verified, Priya Nair, internal note 10:20). Manual send works, and re-saving one schedule and running it in test mode dispatched within 40 seconds (Verified, same note); whether re-saving fixes real scheduled runs is unconfirmed (Hypothesis, Priya Nair). Priya's hypothesis is that this is known issue KI-3381 "Legacy recurring schedules skip auto-send after v8.3" (Engineering, status Investigating), not yet confirmed as the same cause. The customer reports 340 schedules and further runs on 13 Nov 07:00 UTC (64 invoices) and 15 Nov (90 invoices) (Reported).

| Fact | Tag | Source |
|---|---|---|
| Recurring invoices "ran this morning but nothing has gone out to clients" | Reported | Daniel Okafor, 2026-11-12 09:14 |
| Retainer clients are billed on the 12th; around 110 invoices should have been emailed at 07:00 | Reported | Daniel Okafor, 09:14 |
| Invoices all show "Queued" in the invoice list | Reported | Daniel Okafor, 09:14 |
| No client appears to have received an invoice; two clients have rung to ask | Reported | Daniel Okafor, 09:14 |
| Customer has not changed any settings | Reported | Daniel Okafor, 09:14 |
| Business impact: client payment terms run from the send date, so each day of delay pushes back collections | Reported | Daniel Okafor, 09:14 |
| Product: Quillbill Invoicing (cloud) with Recurring Billing add-on; data region UK | Verified | Account record (Products; Data region) |
| Recurring run at 07:00:03 UTC on 12 Nov generated 112 invoices | Verified | Priya Nair, job log, internal note 10:20 |
| All 112 are in dispatch state "Queued - not dispatched"; dispatcher shows 0 send attempts and no errors | Verified | Priya Nair, internal note 10:20 |
| All 112 come from schedules created before 10 Nov (v8.3 release) | Verified | Priya Nair, internal note 10:20 |
| Account has 3 schedules created after 10 Nov; none was due on 12 Nov, so no direct comparison | Verified | Priya Nair, internal note 10:20 |
| Cause is KI-3381 "Legacy recurring schedules skip auto-send after v8.3" (opened by Engineering 11 Nov, Investigating, 2 other customers linked); "Symptoms match. Not confirmed as the same cause." | Hypothesis (Priya Nair) | Internal note 10:20; ticket linked to KI-3381 at 11:30 |
| Manual Send of INV-2026-11-0457 at 10:15 was accepted by the recipient's mail server at 10:16 | Verified | Priya Nair, internal note 10:20 (Test 1) |
| After saving schedule "Meadowgate monthly retainer" without changes, "Run now (test mode)" dispatched the test invoice within 40 seconds | Verified | Priya Nair, internal note 10:20 (Test 2) |
| Re-saving clears the fault for a schedule on real scheduled runs ("Not yet seen on a real scheduled run") | Hypothesis (Priya Nair) | Internal note 10:20 (Test 2) |
| Customer has 340 recurring schedules | Verified | Account record: "340 active schedules as of 1 November 2026" (also Reported by Daniel Okafor, 10:52) |
| Re-saving all schedules by hand "isn't realistic" for the customer | Reported | Daniel Okafor, 10:52 |
| Next runs: 13 Nov 07:00 UTC with 64 invoices; Sunday 15 Nov with 90 invoices | Reported | Daniel Okafor, 09:14 and 10:52 |
| Customer plans to bulk-send the remaining 111 invoices from 12 Nov themselves "this afternoon" | Reported | Daniel Okafor, 10:52 |

**Open questions:**
- Is this KI-3381? Engineering has not confirmed the cause for this account.
- Does re-saving a schedule fix real scheduled runs, or only test-mode runs?
- Is there a way to apply the fix (or a re-save) to all of the customer's pre-10 Nov schedules without manual work on 340 schedules?
- How many of the 64 invoices due 13 Nov 07:00 UTC and 90 due 15 Nov come from pre-10 Nov schedules? The thread does not say.
- Did the customer's bulk send of the 111 invoices on 12 Nov succeed? Not recorded.
- If a fix releases the queued invoices to the dispatcher, could invoices the customer has already sent by hand go out a second time? The thread does not address this.
- Do the 3 post-10 Nov schedules dispatch normally? None has run yet.

## What has been tried
| Action | By | When | Result |
|---|---|---|---|
| Reviewed job log and dispatcher for HF-0192's 07:00 run | Priya Nair (Tier 1) | 2026-11-12, by 10:20 UTC | 112 invoices generated, all "Queued - not dispatched", 0 send attempts, no errors; all from pre-10 Nov schedules |
| Checked known issues | Priya Nair | 2026-11-12, by 10:20 UTC | Matched symptoms to KI-3381; same cause not confirmed |
| Test 1: manual Send of INV-2026-11-0457 (customer approved at 09:58) | Priya Nair | 2026-11-12 10:15 UTC | Accepted by recipient's mail server at 10:16 |
| Test 2: re-saved schedule "Meadowgate monthly retainer" without changes, then "Run now (test mode)" | Priya Nair | 2026-11-12, by 10:20 UTC | Test invoice dispatched within 40 seconds; not yet tested on a real scheduled run |
| Gave customer workaround: bulk-send queued invoices from the invoice list, up to 50 at a time | Priya Nair | 2026-11-12 10:34 UTC | Customer said they would do this "this afternoon" (10:52); result not recorded |
| Escalated to Tier 2 (Product Engineering Support) and linked to KI-3381 | Priya Nair | 2026-11-12 11:30 UTC | Status Escalated; result not recorded |

## Commitments to the customer
| Commitment (quoted) | Made by | When | Status |
|---|---|---|---|
| "I'm looking at your account now." | Priya Nair | 2026-11-12 09:41 UTC | Met (job log reviewed, internal note 10:20) |
| "tell me whether I may send that one invoice from our side as a test" (offer, accepted by customer at 09:58) | Priya Nair | 2026-11-12 09:41 UTC | Met (sent 10:15, accepted 10:16) |
| "I'm escalating your ticket to our Product Engineering Support team now" | Priya Nair | 2026-11-12 11:05 UTC | Met (escalation event 11:30) |
| "I'll make sure they know your next run is at 07:00 UTC tomorrow, 13 November, with 64 invoices." | Priya Nair | 2026-11-12 11:05 UTC | Met (stated in escalation note 11:30) |
| "I will email you an update by 16:00 UTC today with what they've found, even if that is only that they are still investigating." | Priya Nair | 2026-11-12 11:05 UTC | Open, due 2026-11-12 16:00 UTC; Tier 2 owns it ("From escalation, Tier 2 owns the ticket, including customer updates and any commitments already made to the customer", policy 5.2) |

**Requested, not committed:**
- "Please treat this as urgent." (Daniel Okafor, 09:14). No priority change was recorded; P2 shown as unchanged at 11:30.
- "Can you guarantee this will be fixed before tomorrow morning's run?" (Daniel Okafor, 10:52). Declined: "I can't promise a fix time, because that depends on what engineering finds." (Priya Nair, 11:05; consistent with policy 6.2).

## Service level
Measured at 2026-11-12 11:30 UTC (the last entry in the thread; no later time supplied). Readings used for ambiguous terms:
- "an update at least once each business day" (policy 7.1): the policy defines business hours ("08:00 to 18:00 Europe/London time, Monday to Friday, excluding bank holidays in England", 1.1) but not "business day". Reading used: each Monday to Friday that is not a bank holiday in England, with the update due by 18:00 UTC that day (Europe/London is GMT = UTC in this period, 1.1).
- Whether the 10:34 message counts as an "update": read as yes (a support agent's status message to the customer).

| Target (policy quote) | Clock start | Deadline (arithmetic) | Status |
|---|---|---|---|
| First response, Enterprise P2: "2 hours, 24x7" (3.1); "Targets marked "24x7" run on calendar time" (3.3) | Ticket created 2026-11-12 09:14 UTC ("The clock starts when the ticket is created", 4.1) | 09:14 + 2 h = 2026-11-12 11:14 UTC. First reply from Priya Nair at 09:41 (27 min) | Met |
| Resolution, Enterprise P2: "24 hours, 24x7" (3.1); resolution means "a fix or a workaround that restores the affected function and the ticket status has been set to Resolved" (1.5) | 2026-11-12 09:14 UTC (4.1) | 09:14 12 Nov + 24 h = 2026-11-13 09:14 UTC. Elapsed at 11:30 = 2 h 16 min; remaining = 21 h 44 min. "At risk" if less than 25% remains (4.5): 25% of 24 h = 6 h, so at risk from 09:14 13 Nov − 6 h = 2026-11-13 03:14 UTC | Within target (at risk from 03:14 UTC 13 Nov; breached after 09:14 UTC 13 Nov if not Resolved) |
| Update cadence, P2: "an update at least once each business day" (7.1) | Not stated by the policy; each business day under the reading above | Thursday 12 Nov: due by 18:00 UTC; update sent 10:34. Friday 13 Nov: due by 2026-11-13 18:00 UTC | Met for 12 Nov; 13 Nov open |

Pauses: "The clock is paused only while the ticket status is "Pending customer"" (4.2). The ticket has not been in "Pending customer" (New → Open 09:41, Open → Escalated 11:30), so no paused time.

Escalation notice: "The Support Duty Manager must be told of every P1 ticket and of every P2 ticket that is breached" (5.3). Not yet required; it will be if the ticket is unresolved at 2026-11-13 09:14 UTC.

## Recommended next action
Take this account's evidence (112 invoices from pre-10 Nov schedules, 0 dispatch attempts, re-save plus test-mode run dispatching) to Engineering on KI-3381 and get answers to two questions: is this the same cause, and can the re-save (or an equivalent fix) be applied to all of HF-0192's pre-10 Nov schedules from the back end before the next run? Owner: the Tier 2 (Product Engineering Support) engineer who takes this ticket. By: 2026-11-12 16:00 UTC. Reason: the answer is due in the promised 16:00 UTC update email (the one open commitment). It also decides whether the 64 invoices in the 13 Nov 07:00 UTC run go out on their own or need the customer's manual bulk send. Both of those come before the resolution deadline of 2026-11-13 09:14 UTC (at risk from 03:14 UTC). Ask Engineering at the same time whether releasing the queued invoices could re-send ones the customer has already sent by hand. (Recommendation, not from the inputs.)
