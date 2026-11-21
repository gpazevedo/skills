# Handoff: QB-203977, Lindqvist Marine Supplies Ltd (LMS-0855)

As-of: 2026-11-10 14:20 UTC (ticket export time).

## 1. Summary

Per-line VAT rounding is not applied to some EUR invoices since release 8.2.4 (2 Nov); the invoice VAT total differs from the sum of line VAT by EUR 0.01 on 7 of 20 sampled EUR invoices. Urgent: Tier 1 promised the customer a written summary by 17:00 UK time today (17:00 UTC, 2h40m after this handoff), and the customer's auditors are on site Thursday 12 Nov.

## 2. Problem as understood

**Verified**
- Account setting "VAT rounding: per line" is on, last changed 14 March 2026 (Tom Reyes internal note, 2026-11-09 14:30). Account record also lists "VAT rounding per line" (account record).
- INV-LM-11402, INV-LM-11417, INV-LM-11431 (all EUR): each invoice VAT total is EUR 0.01 lower than the sum of line VAT (Tom's note, 14:30).
- Sample of 20 EUR invoices issued 2 to 9 Nov: 7 differ by 0.01 (5 lower, 2 higher), 13 match. 9 NOK invoices: none differ. 11 GBP invoices sampled: none differ (Tom's note).
- Sandbox reproduction (copy of production settings): new EUR invoice, 3 lines of EUR 10.33 at 20% VAT; line VAT 2.07 each, sum 6.21; invoice VAT total shows 6.20 (20% of 30.99 rounded). Same invoice in GBP gives 6.21 (Tom's note).
- In the sandbox, switching rounding to "per invoice" and back to "per line" made no change for EUR (Tom's note).
- Release notes for 8.2.4 (deployed 2 Nov): "Improved currency conversion precision for non-base-currency invoices" (Tom's note, quoting release notes).
- Account has EUR, NOK and GBP enabled; base currency GBP; UK data region; Enterprise support level; audit on site 12 to 13 Nov (account record; the audit note is from the CSM).

**Reported (no check shown)**
- "Every multi-currency invoice we issue has the wrong VAT total" (Marta, 09 Nov 10:47). Contradicted in part by the sample: 13 of 20 EUR and all 9 NOK invoices matched.
- About 140 invoices in EUR and NOK issued since 2 Nov (Marta). Not counted by support.
- Auditors require per-line rounding and will not accept per-invoice (Marta). Not checked with the auditors.
- Cause: 8.2.4 change to currency conversion. Tom: "Possible link; not confirmed."
- Mechanism: VAT total "seems to be calculated on the invoice total rather than line by line" (Tom to customer, 14:45). This is an inference from one sandbox case; it does not by itself explain the 2 invoices where the total was higher, which were not examined.
- Auditors are in on Thursday (Marta, 10 Nov 13:55). The account record gives 12 to 13 Nov, consistent but from the CSM.

## 3. Tried so far

| Action | By | Result |
|---|---|---|
| Checked account rounding setting | Tom Reyes | Worked (per line is set; so not a misconfiguration) |
| Checked the 3 customer-named invoices | Tom Reyes | Worked: difference EUR 0.01 confirmed on all 3 |
| Sampled 20 EUR, 9 NOK, 11 GBP invoices | Tom Reyes | Worked: 7/20 EUR differ, NOK and GBP none |
| Reproduced in sandbox (EUR vs GBP) | Tom Reyes | Worked: reproduced for EUR only |
| Toggled rounding per invoice and back to per line in sandbox | Tom Reyes | Failed: no change for EUR |
| Compared with release notes | Tom Reyes | Inconclusive: 8.2.4 is a possible link, not confirmed |
| Offered workaround: per-invoice rounding | Tom Reyes | Failed: customer rejects (auditors); also not shown to fix EUR in sandbox |
| Escalation to Tier 2 | Tom Reyes | Done 14:20 |

Not tried or not shown: production code or log inspection, check of the 2 "higher" invoices, check of whether other non-base currencies are affected, count of the ~140 invoices, rollback or hotfix test.

## 4. Commitments to the customer

| Quote | Who | When |
|---|---|---|
| "I'm escalating the fault to our Product Engineering Support team today." | Tom Reyes | 10 Nov 09:10 (done 14:20) |
| "I'll ask engineering whether a fix would recalculate invoices already issued. I can't promise that it will" | Tom Reyes | 10 Nov 09:10. Question is listed as an open ask in the escalation note; no evidence it was put to engineering. Not a promise of recalculation. |
| "I'll send you a written summary of what we've reproduced, including the sandbox example, by 17:00 UK time today (Tuesday 10 November)." | Tom Reyes | 10 Nov 09:10. Not yet sent (escalation note, 14:20). 17:00 UK in November is GMT, so 17:00 UTC. Customer reinforced it: "Please make sure the summary arrives today." (13:55) |
| "I've asked your Customer Success Manager, Owen Pryce, to go through the service-level terms in your contract with you." | Tom Reyes | 10 Nov 09:10. Statement of an action taken; no confirmation from Owen in the material. Ownership of follow-up: unclear. |
| "I can't give you a fix date." | Tom Reyes | 10 Nov 09:10. A refusal, not a promise. No fix date has been given. |

Not a commitment: Tom's 09 Nov 11:20 "I've started looking at this" and the 24-hour fix, which was not confirmed. Tom wrote "On the 24 hours, I'm not able to confirm contract terms myself."

## 5. Service level

- Status: **undetermined**.
- Customer's claim: "Under our Enterprise contract you are required to fix this within 24 hours" (Marta, 09 Nov 10:47). This is Reported only.
- Account record: "Support level: Enterprise (terms in Master Services Agreement, Schedule 3)". Schedule 3 and the support policy were not provided, so response and resolution targets, clock start and pause conditions are "not stated in provided material".
- Illustration only, not a finding: if a 24-hour resolution target existed and the clock started at ticket creation (09 Nov 10:47 UTC), the deadline would be 10 Nov 10:47 UTC, already past by 3h33m at 14:20. If it started at escalation (10 Nov 14:20) it would be 11 Nov 14:20. Which, if either, applies is unknown. Ticket priority is P2 and the policy mapping of P2 is not given.
- Needed to settle it: Schedule 3 text (targets by priority, whether "fix" means resolution or workaround, clock start, pause conditions, business-hours basis), and whether the customer's invoice defect is classed P1 or P2.
- Only dated promise that can be checked: written summary due 10 Nov 17:00 UTC. Time left at 14:20: 2h40m (17:00 minus 14:20). On track only if sent today; currently unsent.

## 6. Recommended next action

Investigate in Product Engineering the EUR rounding path introduced in 8.2.4 (the "currency conversion precision" change): confirm whether VAT is computed on the invoice total for non-base-currency invoices, and why sandbox toggling does not change EUR behaviour and why 2 invoices came out higher.

Reason: the evidence shows a reproducible, currency-specific defect (EUR only, GBP and NOK sampled clean) that began with the 2 Nov release and that setting changes do not fix. The cause is a hypothesis only, and the customer cannot accept the workaround, so only a code-level answer moves the case.

Before 17:00 UTC today:
1. Agree with Tom Reyes who sends the written summary, and send it before 17:00 UTC. Use only the Verified items in section 2, including the sandbox example, and label the 8.2.4 link as unconfirmed. Do not state a fix date or a 24-hour commitment, and do not promise recalculation of issued invoices.
2. Put the question "would a fix recalculate or reissue already-issued invoices?" to engineering and record the answer, as promised to the customer.
3. Ask Owen Pryce (CSM) to supply or confirm Schedule 3 terms, and pass any answer back so the SLA status can be settled.

Open questions for the customer (they do not block the investigation): are there further invoices in other currencies, and is NOK still clean across all issued invoices? The customer should also say what the auditors need on Thursday, so the summary fits that need.

## 7. Gaps

- Support policy and MSA Schedule 3 missing; SLA terms, clock start and pause rules not stated in provided material.
- 8.2.4 as the cause is unconfirmed; the mechanism is inferred from one sandbox case.
- The 2 invoices where the total was higher are unexplained.
- The scale (about 140 invoices) is the customer's figure; the sample is 20 EUR and 9 NOK invoices, so the true affected share is not known.
- No record that Owen Pryce has actually engaged, or that engineering was asked about recalculation.
- The written summary is promised, unsent, and the deadline is 17:00 UTC today.
- Customer says "every" invoice is wrong; the sample shows 7 of 20 EUR. The wording in the summary should follow the sample.
- Priority is P2; whether this should be raised given the audit on 12 to 13 Nov is for Tier 2 to decide against the policy.
