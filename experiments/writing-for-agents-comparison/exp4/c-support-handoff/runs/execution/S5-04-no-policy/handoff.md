# Handoff: QB-203977, VAT totals wrong on multi-currency invoices since update (Lindqvist Marine Supplies Ltd, LMS-0855)

## Problem
- Invoice VAT total differs from the sum of line VAT on some EUR invoices issued since 2 Nov 2026. [Reported: Marta Kowalczyk, 2026-11-09 10:47; the 2 Nov start is corroborated by the 8.2.4 deployment below]
- Account setting "VAT rounding: per line" is on, last changed 14 March 2026. [Verified: Tom Reyes internal note 2026-11-09 14:30]
- INV-LM-11402, INV-LM-11417 and INV-LM-11431 (all EUR) each have an invoice VAT total EUR 0.01 lower than the sum of line VAT. [Verified: Tom Reyes internal note 2026-11-09 14:30]
- In a sample of 20 EUR invoices issued 2 to 9 Nov, 7 differ by 0.01 (5 lower, 2 higher) and 13 match. [Verified: Tom Reyes internal note, sample check]
- No differences in 9 NOK invoices or 11 GBP invoices sampled for the same period. [Verified: Tom Reyes internal note; sample sizes are small]
- Conflict: the customer says "every multi-currency invoice" has the wrong VAT total. Support's sample shows 7 of 20 EUR invoices affected and none of 9 NOK. [Reported vs Verified: Tom Reyes sample]. Scope is not established.
- Sandbox reproduction (copy of production settings): new EUR invoice, 3 lines of EUR 10.33 at 20% VAT. Line VAT is 2.07 each, sum 6.21. Invoice VAT total shows 6.20, which is 20% of 30.99 rounded. The same invoice in GBP shows 6.21. [Verified: Tom Reyes sandbox reproduction, 2026-11-09 14:30]
- Switching the sandbox rounding setting to "per invoice" and back to "per line" made no change for EUR. [Verified: Tom Reyes sandbox test]
- Release 8.2.4 was deployed 2 Nov with the note "Improved currency conversion precision for non-base-currency invoices." [Verified: release notes as cited by Tom Reyes]. A link to the fault is a possibility only, not confirmed (Tom's note).
- Working theory: per-line rounding is not applied to some EUR invoices, so the VAT total is computed on the invoice total. [Unconfirmed hypothesis from Tom Reyes; no root cause identified]
- The customer says about 140 invoices in EUR and NOK were issued since 2 Nov and she has no confidence in any of them. [Reported: Marta Kowalczyk]. The account record does not confirm this count.
- The customer's auditors require per-line rounding, so per-invoice rounding is not acceptable. [Reported: Marta Kowalczyk, 2026-11-09 10:47 and 15:30]
- External audit on site 12 to 13 November 2026. [Verified: account record flag, noted by CSM]. The customer says the auditors arrive Thursday (12 Nov). [Reported: 2026-11-10 13:55]
- Account: Enterprise support, Quillbill Trade annual plan, contract 1 Jan 2026 to 31 Dec 2027, invoice currencies GBP/EUR/NOK, base GBP. [Verified: account record]

## Open questions
- Root cause: is this 8.2.4, and why are only some EUR invoices affected (7 of 20) while NOK and GBP are not? Check: Tier 2 reviews the 8.2.4 change and the EUR rounding path against the 20-invoice sample and the sandbox example.
- Real scope: how many of the roughly 140 invoices are actually affected, and is the direction (5 lower, 2 higher) consistent? Check: query all EUR and NOK invoices since 2 Nov and compare VAT total with the sum of line VAT.
- Will a fix recalculate invoices already issued, or must the customer raise credit notes? Unanswered. Check: Tier 2 or Engineering. Tom said he would ask engineering; no answer is in the thread.
- Enterprise service-level terms (the customer's claimed 24-hour fix) are unverified. No policy text was supplied. Check: MSA Schedule 3, and Owen Pryce (CSM), whom Tom says he asked. No reply is recorded.
- Has the written summary been sent? The escalation note says not yet sent as of 14:20.
- Does the customer's own sandbox test, EUR only, also reflect production exactly? The sandbox is refreshed monthly; the reproduction matched the production pattern, but not every production EUR invoice was reproduced.

## Attempts
1. Confirmed the per-line rounding setting is on; last changed 14 March 2026. By Tom Reyes, 2026-11-09. Result: setting is correct, so the fault is not a configuration error.
2. Asked the customer for example invoice numbers (11:20). By Tom Reyes. Result: worked; customer sent INV-LM-11402, 11417, 11431 at 12:05.
3. Checked the three invoices. By Tom Reyes. Result: each VAT total is EUR 0.01 below the sum of line VAT.
4. Sampled 20 EUR, 9 NOK and 11 GBP invoices. By Tom Reyes. Result: 7 of 20 EUR differ; none of the NOK or GBP.
5. Reproduced in the customer's sandbox. By Tom Reyes. Result: reproduced on EUR (6.20 vs 6.21); GBP correct.
6. Toggled sandbox rounding to per invoice and back to per line. By Tom Reyes. Result: failed, no change for EUR.
7. Reviewed the release notes for 8.2.4. By Tom Reyes. Result: possible link, unconfirmed.
8. Gave the customer a status update with the findings and offered per-invoice rounding as a workaround (14:45). By Tom Reyes. Result: customer rejected the workaround (auditors).
9. Replied on the three points (2026-11-10 09:10): escalation, ask engineering on recalculation, written summary, asked CSM about service-level terms. By Tom Reyes. Result: customer replied "Fine" and asked that the summary arrive today (13:55).
10. Escalated to Tier 2 (Product Engineering Support), P2, 14:20. By Tom Reyes. Result: pending.
11. Asked CSM Owen Pryce to take the customer through the service-level terms. By Tom Reyes (stated in the customer message of 09:10). Result: unknown; no reply in the thread.
12. Asked engineering whether a fix would recalculate issued invoices. Stated as intended ("I'll ask"); no evidence it was done. Result: no response.

## Commitments to the customer
| Commitment | Made by | When | Quote |
|---|---|---|---|
| Escalate the fault to Product Engineering Support today | Tom Reyes, Tier 1 Support Agent | 2026-11-10 09:10 UTC | "I'm escalating the fault to our Product Engineering Support team today." (done 14:20) |
| Ask engineering whether a fix would recalculate issued invoices | Tom Reyes, Tier 1 Support Agent | 2026-11-10 09:10 UTC | "I'll ask engineering whether a fix would recalculate invoices already issued." Open |
| Send a written summary of what was reproduced, including the sandbox example, by 17:00 UK time on 10 Nov | Tom Reyes, Tier 1 Support Agent | 2026-11-10 09:10 UTC | "I'll send you a written summary of what we've reproduced, including the sandbox example, by 17:00 UK time today (Tuesday 10 November)." Open, not yet sent as of 14:20 |
| Have the CSM go through the contract service-level terms with the customer | Tom Reyes, Tier 1 Support Agent | 2026-11-10 09:10 UTC | "I've asked your Customer Success Manager, Owen Pryce, to go through the service-level terms in your contract with you." Open |

No fix date, recalculation, credit or 24-hour commitment was made. Tom stated "I can't give you a fix date", "I can't promise that it will" and "I'm not able to confirm contract terms myself".

## Service level
Term: Not determinable: the support policy and MSA Schedule 3 were not supplied. The account record says only "Enterprise (terms in Master Services Agreement, Schedule 3)". The customer's claim of a 24-hour fix is reported only and unverified.
Clock start: Not determinable: depends on the policy. The ticket was created at 2026-11-09 10:47 UTC at P2; whether the clock starts at creation or at another event is unknown.
Deadline: Not determinable: no verified term. If the customer's 24 hours ran from creation it would be 2026-11-10 10:47 UTC, but this is unverified.
Status: Not determinable as of 2026-11-10 14:20 UTC. The only dated deadline in the thread is the promised summary: 17:00 UK time on 10 Nov is 17:00 UTC (GMT in November), so 2 h 40 min remained as of 14:20 UTC.

## Recommended next action
Primary action: Send the written summary to Marta Kowalczyk before 17:00 UTC today, 10 Nov. Do this as a joint step with Tier 2: Tier 2 reviews the reproduction and 8.2.4 EUR rounding path now, confirms a root cause or states plainly that none is established yet, and answers whether issued invoices can be recalculated. The summary should state only verified findings (the three invoices, the 7 of 20 sample, no NOK or GBP differences, the sandbox example with figures, the 8.2.4 link as unconfirmed). It should say that the fix date and recalculation are not yet known.
Reason: it is the only commitment with a hard deadline, the auditors are on site 12 to 13 Nov, and the customer has asked twice for it.
It must satisfy:
- The 17:00 UK summary commitment.
- The open recalculation question (give the customer an answer or a time for one), so she can decide on credit notes before Thursday.
- The service-level question: ask Owen Pryce to confirm the Schedule 3 terms and whether the 24-hour claim applies, and confirm that he has contacted her.
- The clock and any breach should be checked against Schedule 3 once it is obtained.
Assumptions and checks:
- That the cause is 8.2.4: check the change against the sample.
- That the sample reflects all invoices: run the full count of affected EUR and NOK invoices.
- That Owen Pryce has been contacted: confirm with him.
- That the sandbox mirrors production: confirm on one affected production invoice.
- That priority P2 is correct given the audit and a possible compliance impact: confirm against the policy severity definitions.
