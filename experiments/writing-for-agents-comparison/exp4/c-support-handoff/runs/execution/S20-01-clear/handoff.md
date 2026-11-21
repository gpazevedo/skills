# Escalation handoff: QB-204518 Recurring invoices created but not sent (112 queued, not dispatched)

**Customer:** Harrow & Finch Accounting Ltd (HF-0192), Quillbill Practice, Enterprise support | **Priority:** P2 (set by Daniel Okafor at ticket creation; unchanged at escalation, 11:30 note)
**Service level:** within target (worst status), next deadline 2026-11-12 16:00 UTC (4h30m remaining), the update promised to the customer
**Open commitments:** 1, earliest due 2026-11-12 16:00 UTC

## Problem as currently understood
The 07:00 UTC recurring run on 12 Nov generated 112 invoices, all stuck "Queued - not dispatched" with 0 send attempts and no errors (Verified by Priya Nair, job log, 10:20 note). All 112 come from schedules created before the 10 Nov v8.3 release. Symptoms match KI-3381, but the match is Priya Nair's Hypothesis and engineering has not confirmed it. Manual send works, and re-saving one schedule restored dispatch in test mode only. Next runs: 13 Nov 07:00 UTC (64 invoices, Reported) and 15 Nov (90, Reported).

| Fact | Tag | Source |
|---|---|---|
| Recurring invoices created this morning but none emailed to clients | Reported | Okafor, 09:14 |
| Run at 07:00:03 UTC generated 112 invoices (customer said "around 110") | Verified (Nair, job log) | Internal note 10:20 |
| All 112 in dispatch state "Queued - not dispatched"; dispatcher shows 0 send attempts and no errors | Verified (Nair, job log) | Internal note 10:20 |
| All 112 come from schedules created before 10 Nov (v8.3 release) | Verified (Nair) | Internal note 10:20 |
| Account has 3 schedules created after 10 Nov; none due today, so no direct comparison yet | Verified (Nair) | Internal note 10:20 |
| Account has 340 active recurring schedules | Verified (account record, as of 1 Nov 2026) | account.md Products; Okafor 10:52 agrees |
| Manual Send of INV-2026-11-0457 at 10:15 accepted by recipient mail server 10:16 | Verified (Nair, delivery log) | Internal note 10:20; message 10:34 |
| Re-saving schedule "Meadowgate monthly retainer" unchanged, then "Run now (test mode)" dispatched within 40 seconds (test mode sends to account owner only) | Verified (Nair), for one schedule in test mode only | Internal note 10:20 |
| Re-save fixes automatic sending on real scheduled runs | Hypothesis (Nair: "not yet seen on a real scheduled run") | Internal note 10:20 |
| Cause is KI-3381 "Legacy recurring schedules skip auto-send after v8.3" (Investigating, opened 11 Nov, 2 other customers linked) | Hypothesis (Nair: "Not confirmed as the same cause") | Internal note 10:20; escalation note 11:30 |
| No settings changed on customer side | Reported | Okafor, 09:14 |
| Two clients have phoned asking where their invoice is | Reported | Okafor, 09:14 |
| Client payment terms run from send date, so delay pushes back collections | Reported | Okafor, 09:14 |
| Next runs: 13 Nov 07:00 UTC with 64 invoices; Sunday 15 Nov with 90 | Reported | Okafor, 10:52; Nair 11:05 (repeats) |
| Customer will bulk-send the remaining 111 invoices themselves this afternoon | Reported (customer's stated plan; not confirmed done) | Okafor, 10:52 |

**Open questions:** Is the cause KI-3381, and is it the same mechanism for all 112? Does re-save fix a real scheduled run, not only test mode? Which of the 340 schedules are affected (all pre-10 Nov ones?) and is there a bulk fix other than re-saving each? Will the 64 invoices due 13 Nov 07:00 UTC dispatch? Has the customer sent the 111 invoices? (The thread does not show how Priya's test of INV-2026-11-0457 relates to the customer's 111 count; assumed 112 minus the one manually sent.)

## What has been tried
| Action | By | When | Result |
|---|---|---|---|
| Reviewed job log for HF-0192 and dispatcher state | Priya Nair | by 10:20 | 112 queued, 0 send attempts, no errors |
| Checked known issues | Priya Nair | by 10:20 | KI-3381 found; symptoms match, cause unconfirmed |
| Manual Send of INV-2026-11-0457 (customer consented 09:58) | Priya Nair | 10:15 | Accepted by recipient mail server 10:16 |
| Re-save schedule "Meadowgate monthly retainer" without changes, then "Run now (test mode)" | Priya Nair | by 10:20 (time not recorded) | Test invoice dispatched within 40 seconds |
| Advised customer to bulk-send queued invoices (filter "Queued", up to 50 at a time) | Priya Nair | 10:34 | Customer said they would do so this afternoon; completion not recorded |
| Escalated to Tier 2 and linked to KI-3381 | Priya Nair | 11:30 | Status Escalated; no Tier 2 action yet recorded |

## Commitments to the customer
| Commitment (quoted) | Made by | When | Status |
|---|---|---|---|
| "I will email you an update by 16:00 UTC today with what they've found, even if that is only that they are still investigating." | Priya Nair | 11:05 | Open, due 2026-11-12 16:00 UTC (policy 5.2: Tier 2 now owns it) |
| "I'm escalating your ticket to our Product Engineering Support team now" | Priya Nair | 11:05 | Met, escalated at 11:30 |
| "I'll make sure they know your next run is at 07:00 UTC tomorrow, 13 November, with 64 invoices." | Priya Nair | 11:05 | Met, stated in the 11:30 escalation note (internal note says "next runs 13 Nov 07:00 UTC (64 invoices)") |

**Requested, not committed:** Okafor's request for a guarantee the fix lands before tomorrow's 07:00 run (10:52). Priya declined: "I can't promise a fix time" (11:05). Policy 6.2 bars promising a fix date. Okafor's wish to avoid re-saving 340 schedules by hand is not agreed to either.

## Service level
Measured at 2026-11-12 11:30 UTC (the export's as-of time). Readings used for ambiguous terms: none. The case is Enterprise (account record: "Support level: Enterprise"), P2, set by the customer in the portal at creation and not changed on the ticket. Policy 2.5 says support sets priority; no support agent recorded a change.
Note for the engineer: the customer's workaround (bulk send) may fit the P3 definition (2.3), but P2 stands on the ticket and any change must be recorded by an agent (2.5, 4.4); this handoff does not change it.

| Target (policy quote) | Clock start | Deadline (arithmetic) | Status |
|---|---|---|---|
| First response: "Enterprise P2: 2 hours, 24x7" (3.1, 3.3) | Ticket creation 09:14 (4.1) | 09:14 + 2h = 11:14. First agent reply (1.4) was Priya's at 09:41, 27 minutes after creation | Met |
| Resolution: "Enterprise P2: 24 hours, 24x7" (3.1, 3.3) | 09:14 (4.1) | 09:14 + 24h = 2026-11-13 09:14 UTC. Elapsed at 11:30 is 2h16m, so 21h44m remain (90.6% of target). At-risk line (4.5, under 25%) is 6h remaining, i.e. 03:14 on 13 Nov | Within target (not resolved; Resolved status not set) |
| Update cadence: "P2 tickets: an update at least once each business day" (7.1) | 12 Nov (Thursday, a business day under 1.1, assuming no England bank holiday) | Update due by end of 12 Nov business hours (18:00 London = 18:00 UTC, GMT per 1.1). Priya's 10:34 message already gave an update today; the 16:00 promise is a further one | Met for 12 Nov; next due 13 Nov |

Pauses: "The clock is paused only while the ticket status is 'Pending customer'" (4.2). The thread shows no Pending customer status (New, Open, Escalated only), so there is no paused time. Policy 5.3 (duty manager) applies only to P1 or breached P2; neither currently applies. Policy 5.1 allows escalation of a P2 when it cannot be resolved with documented procedures.

## Recommended next action
My recommendation: a Tier 2 engineer confirms whether KI-3381 is the cause for HF-0192 (compare the dispatcher state of the pre-10 Nov schedules with the 3 post-10 Nov schedules, and establish whether re-save is valid for real runs and whether a bulk fix exists), owner Tier 2 (Product Engineering Support), by 15:00 UTC on 2026-11-12, so Tier 2 can send the committed customer update by 16:00 UTC, because that update is the only open commitment, the 13 Nov 07:00 UTC run (64 invoices) is the next customer impact, and the 24h resolution deadline is 2026-11-13 09:14 UTC. Do not promise a fix date or credit to the customer (policy 6.2, 6.3).
