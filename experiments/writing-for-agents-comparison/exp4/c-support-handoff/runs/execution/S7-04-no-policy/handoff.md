# Handoff: QB-203977, VAT totals wrong on multi-currency invoices (Lindqvist Marine Supplies Ltd, LMS-0855)

## Problem as understood
Since release 8.2.4 (deployed 2 Nov), some EUR invoices show an invoice VAT total EUR 0.01 different from the sum of the line VAT, although the account is set to per-line VAT rounding. The sandbox reproduction suggests the VAT total is computed on the invoice total for EUR. The cause is not confirmed.
- Verified: INV-LM-11402, INV-LM-11417 and INV-LM-11431 each have an invoice VAT total EUR 0.01 below the line VAT sum (evidence: Tom Reyes's check, internal note 2026-11-09 14:30).
- Verified: 7 of 20 sampled EUR invoices (2 to 9 Nov) differ by 0.01 (5 lower, 2 higher); 13 match (evidence: same sample).
- Verified: 0 of 9 NOK and 0 of 11 GBP sampled invoices differ (evidence: same sample; small samples).
- Verified: account setting "VAT rounding: per line" is on, last changed 14 March 2026 (evidence: account setting as read by Tom Reyes).
- Verified: sandbox repro (copy of production settings), new EUR invoice, 3 lines of EUR 10.33 at 20%: line VAT 2.07 each (sum 6.21), invoice VAT total 6.20 (20% of 30.99). The same invoice in GBP gives 6.21. Switching the setting to "per invoice" and back to "per line" changed nothing for EUR (evidence: sandbox test, 2026-11-09 14:30).
- Reported: about 140 invoices in EUR and NOK issued since 2 Nov, all with wrong VAT totals (customer, 2026-11-09). This conflicts with the NOK and EUR samples, where not all invoices differ.
- Reported: per-invoice rounding is not acceptable to the customer's auditors (customer, 2026-11-09 and 15:30).
- Unconfirmed: link to 8.2.4 note "Improved currency conversion precision for non-base-currency invoices" (Tom Reyes called it "possible link; not confirmed").

## Tried so far
- Asked customer for example invoice numbers, Tom Reyes, 2026-11-09 11:20: customer supplied three at 12:05.
- Checked the three invoices, sampled EUR, NOK and GBP invoices, Tom Reyes, 2026-11-09: differences found as above.
- Reproduced in the customer's sandbox, Tom Reyes, 2026-11-09: reproduced for EUR.
- Toggled rounding setting per line / per invoice / per line in sandbox, Tom Reyes, 2026-11-09: no change for EUR.
- Raised per-invoice rounding as a workaround, Tom Reyes, 2026-11-09 14:45: customer rejected it (auditors).
- Asked CSM Owen Pryce to walk the customer through contract service-level terms, Tom Reyes, 2026-11-10 09:10: no result in the thread.
- Escalated to Tier 2, Tom Reyes, 2026-11-10 14:20.
- Not done: no log review or code-level investigation shown; sample covers only 20 EUR invoices.

## Commitments to the customer
- Escalate the fault to Product Engineering Support today, Tom Reyes, 2026-11-10 09:10: "I'm escalating the fault to our Product Engineering Support team today." (done 14:20)
- Ask engineering whether a fix would recalculate issued invoices, Tom Reyes, 2026-11-10 09:10: "I'll ask engineering whether a fix would recalculate invoices already issued. I can't promise that it will". No promise of recalculation.
- Written summary incl. sandbox example by 17:00 UK time Tue 10 Nov, Tom Reyes, 2026-11-10 09:10: "I'll send you a written summary of what we've reproduced, including the sandbox example, by 17:00 UK time today". Not yet sent as of 14:20. UK time is GMT in November, so 17:00 UTC (2h40 after the as-of time). The customer asked at 13:55 that it arrive today.
- Service-level terms via CSM, Tom Reyes, 2026-11-10 09:10: "I've asked your Customer Success Manager, Owen Pryce, to go through the service-level terms in your contract with you."
- No fix date: Tom stated "I can't give you a fix date." No 24-hour fix or any other deadline was confirmed by support.

## Service level
Tier: Enterprise (source: account record; terms in MSA Schedule 3). Target: not determined, because no support policy or Schedule 3 was supplied. Clock started: ticket created 2026-11-09 10:47 UTC (the clock start under the policy is unknown). Deadline: not determined. Status: not determined.
The customer's claim of a "24 hours" fix is Reported only (Marta Kowalczyk, 2026-11-09 10:47). Support has not confirmed it. If it applied from creation, 24 hours would end 2026-11-10 10:47 UTC, so the ticket would already be past it. This is arithmetic on the customer's claim, not a policy finding. Priority is P2.

## Recommended next action
Send the promised written summary (reproduced facts, sandbox example, EUR/NOK/GBP sample results, explicit note that the cause is unconfirmed) to the customer before 17:00 UTC today, then have Tier 2 investigate the EUR per-line rounding path in 8.2.4. Reason: it is a dated commitment with auditors on site Thursday 12 Nov, and it is the only deadline the thread evidences. Open question: what do MSA Schedule 3 and the policy say about Enterprise response and resolution targets, since a breach may already exist.
- Alternative: confirm with engineering whether 8.2.4 can be rolled back or hotfixed for EUR VAT rounding, as per-invoice rounding is unacceptable to the customer.
- Alternative: ask engineering for a list of affected issued invoices (EUR since 2 Nov), so the customer can plan credit notes or corrections before the audit.

## Gaps
- Support policy and MSA Schedule 3 not supplied: service-level terms, clock start and deadline not determined. Request the policy.
- Customer says about 140 EUR and NOK invoices are affected, but the NOK sample (9) showed no differences and only 7 of 20 EUR differed. The full population is unchecked.
- Cause unconfirmed (8.2.4 link is a hypothesis). Whether issued invoices will be recalculated is unanswered.
- Account record notes an external audit on site 12 to 13 November (CSM note); the customer said auditors are in on Thursday (12 Nov). These are consistent.
- Whether Owen Pryce has contacted the customer is not shown.
