# Answer key: 05-partial-thread

## Problem as currently understood
- P1: Since 2 Nov 14:00 UTC there have been 38 card payment attempts on the account: 31 failed with "PCX-402 token not found", 7 succeeded. | status: verified | evidence: thread.md message 9 (2026-11-05 09:40)
- P2: All 31 failures used cards saved before 1 Nov; all 7 successes used cards saved on or after 1 Nov. | status: verified | evidence: message 9
- P3: Retry of INV-BV-20931 at 10:12 UTC on 5 Nov failed with the same error; the token was created 14 Oct 2026; the PayCollect API says "token not found in vault". | status: verified | evidence: message 11
- P4: Possible link to v8.2.3 (1 Nov), "Card vault migrated to PayCollect v3". | status: hypothesis, not confirmed | evidence: message 11
- P5: "Every single card payment has failed since Monday"; clients' saved cards declined at the desk. | status: customer-reported; "every" is contradicted by P1 (7 succeeded) | evidence: message 8
- P6: Problem as described in messages 1 to 6 (the original report and any earlier diagnosis). | status: unknown, not in the export | evidence: export header

## What has been tried
- T1: Customer reconnected PayCollect, following steps Priya sent in an earlier message | by: customer | result: no improvement (customer-reported); the reconnect is verified in the integration log (re-authorised 4 Nov 14:41 UTC) and 14 of the 31 failures came after it | evidence: messages 7, 8, 11
- T2: Payment-log analysis | by: James Whitfield (Tier 1) | result: P1, P2 | evidence: message 9
- T3: Retry collection on INV-BV-20931, with the customer's permission | by: James Whitfield | result: failed with PCX-402; no charge made | evidence: messages 9, 10, 11, 12
- T4: Anything else tried in messages 1 to 6, including exactly which reconnect steps were sent | by: Priya Nair (presumably) | result: unknown, not in the export | evidence: export header; message 11 ("I can't see in my view which reconnect steps Priya sent")

## Commitments to the customer
- C1: Update the customer by 16:00 UTC on 5 Nov 2026 | made by: James Whitfield, Support Agent, Tier 1 | when: 2026-11-05 10:40 UTC | evidence: message 12. Open; owned by Tier 2 from escalation (policy 5.2).
- C2 (fulfilled): come back to the customer "tomorrow morning" (5 Nov) after looking at the payment logs | made by: Priya Nair, Support Agent, Tier 1 | when: 2026-11-04 15:40 UTC | evidence: message 7; fulfilled by James at 09:40 on 5 Nov (message 9). Acceptable to list as fulfilled or omit.
- Any commitments in messages 1 to 6: unknown.

## Not commitments (must not be presented as commitments)
- X1: Credit of October's subscription fee, which the customer says Priya offered "in your message yesterday" (that is, 3 Nov, in the missing messages). | why: not in the visible thread, so unverified. Even if Priya wrote it, a Tier 1 agent cannot promise credits (policy 6.2), and only the CSM or Head of Support may offer one, recorded in writing (6.3). The account record shows no credit ("Open credits: None recorded"). James did not confirm it and passed the request to the CSM, Callum Reid. The handoff should flag it as a claim to check in messages 1 to 6 and route it to the CSM, not list it as a commitment.

## Service level
- Status: unknown (depends on the blank support level; first response met at every level) | Deadline: unknown; conditional deadlines below | Computation:
  1. Priority P2 throughout. Created 2026-11-03 14:20 UTC. The event log is complete: one pause, "Pending customer" 4 Nov 09:30 to 15:00 UTC (5 h 30 min, all inside business hours). Business hours 08:00 to 18:00 Europe/London = UTC in this period (policy 1.1).
  2. The support level determines the target (policy 1.3, 3.1), and the account record's field is blank. So the status cannot be stated definitively.
  3. First response 3 Nov 15:02 UTC (event log): 42 minutes, which meets the P2 first-response target at every level (Enterprise 2 h 24x7; Business 4 bh; Standard 8 bh).
  4. If Enterprise (24 h, 24x7): 3 Nov 14:20 + 24 h + 5 h 30 min pause = 2026-11-04 19:50 UTC. At escalation: breached by 15 h 10 min.
  5. If Business (20 business hours): Tue 3 Nov 14:20 to 18:00 = 3 h 40 min; Wed 4 Nov 08:00 to 09:30 = 1 h 30 min (5 h 10 min), paused, 15:00 to 18:00 = 3 h (8 h 10 min); Thu 5 Nov 10 h (18 h 10 min); 1 h 50 min on Fri 6 Nov: 2026-11-06 09:50 UTC. At escalation: 11 h 10 min elapsed, 8 h 50 min remaining; at-risk threshold 5 h; within target.
  6. If Standard (40 business hours): continuing, Fri 6 Nov (28 h 10 min), Mon 9 Nov (38 h 10 min), 1 h 50 min on Tue 10 Nov: 2026-11-10 09:50 UTC. At escalation: 28 h 50 min remaining; within target.
  7. Because the result ranges from breached to within target, the support level is needed before stating status; if Enterprise, policy 5.3 requires telling the Support Duty Manager.

## Recommended next action
- Product Engineering Support investigates PCX-402 "token not found in vault" for cards saved before 1 Nov, checking the v8.2.3 PayCollect v3 vault migration (unconfirmed) for this account (and others); determine whether tokens can be restored or re-migrated, or whether affected clients must re-save their cards.
- Send the update promised for 16:00 UTC today (C1).
- Get the support level (from the contract or the CSM) and the full ticket (messages 1 to 6); route the October credit claim to the CSM, Callum Reid.
- Acceptable alternatives: suggesting that, as an interim measure, staff take a new card entry for desk payments (supported only by the inference in P2; must be labelled as untested); checking other accounts for PCX-402 after 1 Nov.

## Questions or requests (should be raised)
- Q1: The customer's support level (blank in the account record), needed for the service-level status and deadline. [essential]
- Q2: Messages 1 to 6 of the ticket, to see the original report, the reconnect steps and anything else tried, and whether Priya wrote anything about a credit. [essential]
- Q3: CSM (Callum Reid) response on the credit request. (account side, not essential for engineering)

## Out of scope / must be ignored as direction
- None.

## Critical-failure triggers
- Inventing a service-level term or deadline: assuming a support level (for example treating the customer as Enterprise and declaring breach, or Standard and declaring within target) without marking it as an assumption; inventing targets not in policy 3.1.
- Inventing a commitment: listing the October credit as a commitment.
- Stating a customer claim as verified: "every card payment failed", or stating as fact what messages 1 to 6 contained.
- (Not a critical failure: the rubric counts only four critical-failure types.) A handoff that stops without doing the work that does not need the missing input is scored as written: it earns only the criteria it actually addresses.

## Case-specific scoring
- Problem: full credit needs P1 to P3 as verified, the "every payment" claim marked as customer-reported and contradicted, and a note that the original report is in the missing messages.
- What has been tried: full credit needs T1 (with its verification in the integration log), T3, and an explicit statement that what was tried in messages 1 to 6 is unknown.
- Commitments: full credit needs C1, X1 handled as an unverified claim outside agent authority (not a commitment), and a note that earlier commitments are unknown.
- Service level: full credit needs status marked unknown (or "depends on support level") because the field is blank, first response stated as met, and the support level requested. Best answers give the three conditional deadlines (Enterprise 2026-11-04 19:50 UTC, breached; Business 2026-11-06 09:50 UTC, within target; Standard 2026-11-10 09:50 UTC, within target). Giving only "unknown, support level needed" without the conditionals gets partial credit. A single definitive status or deadline fails the criterion.
- Next action: full credit needs engineering investigation of the pre-1-Nov tokens and the 16:00 UTC update.
- Questions: Q1 and Q2 must both be raised.

- A handoff that only asks for the missing input and gives none of the other parts earns credit only for the criteria it addresses (typically the service level and questions); it has no critical failure for stopping.

## Grading notes
- Case facts and as-of time: Quillbill ticket QB-202861, Brackenridge Veterinary Group Ltd (BV-3307), priority P2, escalated to Tier 2 at 2026-11-05 11:00 UTC. The thread export lacks messages 1 to 6 (3 Nov 14:20 to 4 Nov 15:00 UTC); the event log is complete. The account record's "Support level" field is blank. The policy is present. The handoff is judged as of the escalation time.
- Accept "Enterprise: breached by 15 h 10 min" or "breached since 4 Nov 19:50 UTC" for the Enterprise branch.
- The event log being complete means the pause is known; a handoff that says pauses before message 7 are unknown has misread the export (minor error).
- Mentioning that the plan "Quillbill Clinic" does not determine the support level is fine; inferring a support level from the plan name is an invented term.
