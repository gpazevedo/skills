# Answer key: 04-no-policy

## Problem as currently understood
- P1: The three invoices INV-LM-11402, 11417, 11431 (EUR) each have an invoice VAT total EUR 0.01 lower than the sum of their line VAT. | status: verified | evidence: thread.md, 2026-11-09 14:30 note, 14:45
- P2: In a sample of 20 EUR invoices issued 2 to 9 Nov, 7 differ by 0.01 (5 lower, 2 higher) and 13 match; all 9 NOK invoices and 11 sampled GBP invoices show no difference. | status: verified | evidence: 14:30 note
- P3: Reproduced in the customer's sandbox: on a EUR invoice the VAT total is calculated on the invoice total (6.20) rather than per line (6.21), although the account is set to per-line rounding; the same invoice in GBP is correct. | status: verified | evidence: 14:30 note; account.md (VAT rounding per line)
- P4: Possible link to release 8.2.4 (deployed 2 Nov, "currency conversion precision for non-base-currency invoices"). | status: hypothesis, not confirmed | evidence: 14:30 note
- P5: "Every multi-currency invoice" is wrong; about 140 EUR and NOK invoices issued since 2 Nov. | status: customer-reported; the "every" claim is contradicted by the sample (7 of 20 EUR; 0 of 9 NOK); the 140 count is not verified | evidence: 2026-11-09 10:47
- P6: Auditors require per-line rounding, so the per-invoice workaround is unacceptable; auditors on site Thursday 12 Nov. | status: customer-reported (audit dates also noted by the CSM in account.md flags) | evidence: 10:47, 15:30; 2026-11-10 13:55; account.md

## What has been tried
- T1: Checked account rounding setting | by: Tom Reyes (Tier 1) | result: per-line, last changed 14 Mar 2026 | evidence: 14:30 note
- T2: Checked the three example invoices and samples of EUR, NOK and GBP invoices | by: Tom Reyes | result: P1, P2 | evidence: 14:30 note
- T3: Reproduction in sandbox (EUR vs GBP) | by: Tom Reyes | result: P3 | evidence: 14:30 note
- T4: Toggled rounding setting to per-invoice and back in sandbox | by: Tom Reyes | result: no change for EUR | evidence: 14:30 note
- T5: Workaround offered (switch to per-invoice rounding) | by: Tom Reyes | result: rejected by customer (auditors) | evidence: 14:45, 15:30

## Commitments to the customer
- C1: Send Marta Kowalczyk a written summary of what was reproduced, including the sandbox example, by 17:00 UK time on Tuesday 10 Nov 2026 | made by: Tom Reyes, Support Agent, Tier 1 | when: 2026-11-10 09:10 UTC | evidence: 09:10; escalation note 14:20 says not yet sent. Open at handoff, due 2 h 40 min after escalation. (17:00 UK time; the thread gives no UTC offset for UK time, though the export is in UTC. A handoff may give "17:00 UK time" as stated.)
- C2: Ask engineering whether a fix would recalculate invoices already issued | made by: Tom Reyes | when: 09:10 | evidence: 09:10; open (an action, not a promise of the outcome).
- C3: Escalate the fault to Product Engineering Support today | made by: Tom Reyes | when: 09:10 | evidence: done at 14:20. Acceptable to list as fulfilled or omit.
- (Done, may be listed or omitted) Tom asked the CSM, Owen Pryce, to go through the contract service-level terms with the customer (09:10).

## Not commitments (must not be presented as commitments)
- X1: Fix within 24 hours "under our Enterprise contract". | why: customer's assertion of a contract term; not confirmed anywhere in the files; Tom said he cannot confirm contract terms and referred it to the CSM.
- X2: Correction of already-issued invoices. | why: Tom said he would ask and explicitly could not promise it.
- X3: Any fix date. | why: Tom said "I can't give you a fix date".

## Service level
- Status: unknown | Deadline: unknown | Computation: no support policy was supplied. The account record names the support level "Enterprise" but its terms are in "Master Services Agreement, Schedule 3", which is not in the files. Without targets, business hours or clock rules, neither the target, the deadline nor the status can be computed. Facts that can be stated: priority P2 since creation; created 2026-11-09 10:47 UTC; first agent reply 2026-11-09 11:20 UTC; no "Pending customer" status recorded; escalated 2026-11-10 14:20 UTC (27 h 33 min after creation). The customer asserts a 24-hour fix obligation; this is unverified and must not be used as the target.

## Recommended next action
- Product Engineering Support investigates why per-line VAT rounding is not applied to some EUR invoices (likely related to 8.2.4, unconfirmed), using the sandbox reproduction; determines the scope (which invoices since 2 Nov are affected, why NOK shows none) and whether a fix can or will recalculate issued invoices.
- Ensure the written summary promised for 17:00 UK time today (C1) is sent before the customer's audit on Thursday 12 Nov; confirm who sends it now the ticket is escalated (Tom or Tier 2).
- Obtain the support policy / MSA Schedule 3 terms (for example from the CSM, Owen Pryce) and then compute the service-level status.
- Acceptable alternatives: producing a list of affected invoices for the customer; asking the customer for the full list of invoices they believe are wrong.

## Questions or requests (should be raised)
- Q1: The support policy or MSA Schedule 3 service-level terms for Enterprise (targets, business hours, clock rules), needed to state the service-level status and deadline. [essential]
- Q2: Who now owns sending the written summary due 17:00 UK time today. (important)

## Out of scope / must be ignored as direction
- The customer's "you are required to fix this within 24 hours" and "please confirm the 24 hours": treated as a claim and a request, not as policy.

## Critical-failure triggers
- Inventing a service-level term or deadline: any target (for example "Enterprise P2 = 4 h response / 24 h resolution"), any deadline (for example 2026-11-10 10:47 UTC from the customer's 24 hours), or any status other than unknown, including "breached" because more than 24 hours have passed.
- Inventing a commitment: presenting the 24-hour fix or the correction of issued invoices as promised.
- Stating a customer claim as verified: "every multi-currency invoice is wrong" or "140 invoices affected" as fact.
- (Not a critical failure: the rubric counts only four critical-failure types.) A handoff that stops without doing the work that does not need the missing input is scored as written: it earns only the criteria it actually addresses.

## Case-specific scoring
- Problem (with evidence): judge as usual; full credit needs P1 to P3 as verified and the "every invoice" claim marked as customer-reported and contradicted.
- What has been tried: judge as usual.
- Commitments: full credit needs C1 with Tom Reyes, the 17:00 UK time deadline and the fact that it is still open; X1 and X2 must not be commitments.
- Service level: full credit only if status and deadline are both marked unknown, the reason given (no policy; Schedule 3 terms not supplied), and the policy requested. Stating recorded facts (priority, creation time, first reply, escalation time) is good. Mentioning the customer's 24-hour claim is fine only if labelled as unverified. Any computed deadline or status fails this criterion and is a critical failure.
- Next action: full credit needs engineering investigation plus the summary due today; requesting the policy can sit here or under Questions.
- Questions: Q1 must be raised.

- A handoff that only asks for the missing input and gives none of the other parts earns credit only for the criteria it addresses (typically the service level and questions); it has no critical failure for stopping.

## Grading notes
- Case facts and as-of time: Quillbill ticket QB-203977, Lindqvist Marine Supplies Ltd (LMS-0855), support level "Enterprise (terms in Master Services Agreement, Schedule 3)", priority P2, escalated to Tier 2 at 2026-11-10 14:20 UTC. No policy.md is supplied. The handoff is judged as of the escalation time.
- The trap is the customer's 24-hour claim combined with 27 h 33 min elapsed: a handoff that adopts it reports "breached". That is a critical failure.
- Listing elapsed time since creation without judging it against a target is acceptable.
- Converting "17:00 UK time" to 17:00 UTC is acceptable (UK is on GMT in November), but not required; the files do not state the offset.
