# Handoff: QB-203977, Lindqvist Marine Supplies Ltd (LMS-0855)

As-of: 2026-11-10 14:20 UTC. Escalated from Tier 1 (Tom Reyes) to Tier 2 (Product Engineering Support). Priority P2.

## 1. Problem as understood

On EUR invoices, the invoice VAT total sometimes differs by EUR 0.01 from the sum of the line VAT, although the account is set to per-line rounding. It has been seen since release 8.2.4 (deployed 2 Nov), and a sandbox reproduction suggests the total is computed on the invoice total, not per line. NOK and GBP samples show no differences. The customer's auditors require per-line rounding and are on site Thursday 12 Nov. A link to 8.2.4 is a possibility only, not confirmed.

Evidence:
- Account setting "VAT rounding: per line" is on, last changed 14 Mar 2026. Verified, Tom Reyes internal note 2026-11-09 14:30 (account setting check).
- INV-LM-11402, -11417, -11431 (EUR) each have invoice VAT EUR 0.01 below the sum of line VAT. Verified, Tom Reyes, 2026-11-09 14:30.
- Sample of 20 EUR invoices issued 2 to 9 Nov: 7 differ by 0.01 (5 lower, 2 higher), 13 match. Verified, Tom Reyes, same note. This is a sample only; the full extent is unknown.
- 9 of 9 NOK and 11 of 11 sampled GBP invoices show no difference. Verified, Tom Reyes, same note.
- Sandbox (copy of production settings): 3 lines of EUR 10.33 at 20% gives line VAT 2.07 each (sum 6.21), but invoice VAT shows 6.20 (20% of 30.99 rounded). The same invoice in GBP shows 6.21. Verified, Tom Reyes, same note.
- Switching the sandbox between "per invoice" and "per line" did not change EUR behaviour. Verified, Tom Reyes, same note.
- Cause is "per-line rounding not applied to EUR invoices" and "calculated on invoice total". This is Tom's inference from the reproduction, not a confirmed root cause. 8.2.4 release note ("Improved currency conversion precision for non-base-currency invoices") is a possible link, not confirmed (Tom, 2026-11-09 14:30).
- Customer states "every multi-currency invoice" has the wrong VAT total. Reported (Marta Kowalczyk, 2026-11-09 10:47). Contradicted by the 13 of 20 EUR matches and the NOK result above.
- Customer states about 140 EUR and NOK invoices issued since 2 Nov. Reported (Marta, 2026-11-09 10:47); count not checked.
- Customer states per-invoice rounding is unacceptable to auditors. Reported (Marta, 2026-11-09 15:30). Account record notes an external audit on site 12 to 13 Nov (CSM note), which is consistent but does not verify the auditors' requirement.

## 2. Tried and result

- Tom Reyes, 2026-11-09: asked for example invoice numbers. Worked (customer supplied three, 12:05).
- Tom Reyes, 2026-11-09: checked the three invoices, a 20-invoice EUR sample, 9 NOK and 11 GBP invoices. Outcome: difference found in EUR only.
- Tom Reyes, 2026-11-09: reproduced in the customer's sandbox. Worked (reproduced).
- Tom Reyes, 2026-11-09: toggled the sandbox rounding setting to per invoice and back to per line. Failed (no change for EUR).
- Ruled out: the account setting being off (it is on); NOK and GBP invoices (no differences in samples).
- Tom Reyes, 2026-11-10 09:10: asked CSM Owen Pryce to take the customer through the service-level terms. Outcome unknown (no reply in the thread).
- Per-invoice rounding offered as a workaround. Rejected by the customer.

## 3. Commitments to the customer

- Tom Reyes, 2026-11-10 09:10: will escalate the fault to Product Engineering Support "today". Done at 14:20.
- Tom Reyes, 2026-11-10 09:10: will "ask engineering whether a fix would recalculate invoices already issued"; "can't promise that it will". No date given. Not yet answered.
- Tom Reyes, 2026-11-10 09:10: will send a written summary of what has been reproduced, including the sandbox example, "by 17:00 UK time today (Tuesday 10 November)". Not sent as of 14:20 (escalation note). 17:00 UK time is 17:00 UTC (UK is on GMT in November; this is my assumption from the date).
- Tom Reyes, 2026-11-10 09:10: no fix date given ("I can't give you a fix date"); the 24-hour fix was not confirmed ("not able to confirm contract terms myself").
- Unconfirmed customer assertion (Reported): Marta states the Enterprise contract requires a fix within 24 hours. No support person agreed to it.

## 4. Service-level status and deadline

Not determinable: support policy with service levels not supplied.

What is known without the policy: the account record says support level Enterprise, with terms in "Master Services Agreement, Schedule 3" (the schedule itself was not supplied). Ticket created 2026-11-09 10:47 UTC, priority P2; 27 h 33 min had elapsed by 2026-11-10 14:20 UTC (10:47 on 9 Nov to 10:47 on 10 Nov is 24 h, plus 3 h 33 min). I cannot say whether this is inside or outside any response or resolution target, whether the customer's "24 hours" is a contract term, which clock start applies, or whether any pause or exclusion applies. The only deadline the thread supports is the Tier 1 commitment: 2026-11-10 17:00 UTC, 2 h 40 min after the as-of time, at risk because the summary is not yet sent.

## 5. Recommended next action

Primary action: send the customer the promised written summary before 2026-11-10 17:00 UTC. Owner: Tier 1 agent (Tom Reyes) who made the promise, with Tier 2 confirming the technical wording. It should contain only the verified facts in section 1 (the three invoices, the 7-of-20 EUR sample, the NOK and GBP results, the sandbox example) and should state that the cause is not yet confirmed. Rationale: the 17:00 promise is the only dated commitment, and the customer has repeated that the summary must arrive today because auditors attend on Thursday 12 Nov.

Tell the customer in the same message: engineering is investigating, there is still no fix date or answer on recalculating issued invoices, and the 24-hour question is with Owen Pryce. Next contact once Tier 2 has an answer on recalculation or a fix date, or sooner if the audit timing changes.

After this handoff: please supply the support policy and the MSA Schedule 3 service levels so section 4 can be completed.
