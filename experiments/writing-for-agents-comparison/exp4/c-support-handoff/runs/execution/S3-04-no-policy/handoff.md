# Escalation handoff: QB-203977, Lindqvist Marine Supplies Ltd (LMS-0855)

**Service level:** Undetermined (the support policy / MSA Schedule 3 was not supplied), deadline Undetermined; customer reports a 24-hour fix term, unconfirmed. Nearest dated obligation is our own promise: written summary by 17:00 UK time (17:00 UTC) on 2026-11-10, open, 2h40m left.
**Next action:** Confirm on the 8.2.4 code path why EUR invoices skip per-line VAT rounding, starting with the 2 "higher" cases, and give Tom the findings in time for the 17:00 UTC summary.

## Problem as currently understood
Per-line VAT rounding appears not to be applied to some EUR invoices since release 8.2.4 (deployed 2 Nov), so the invoice VAT total can differ by EUR 0.01 from the sum of line VAT; NOK and GBP samples show no difference. The customer's opening claim was that every multi-currency invoice is wrong; testing narrowed it to EUR only, and only some of those (7 of 20).

Evidence:
- [Reported] Wrong VAT totals on every multi-currency invoice since "your update last week"; VAT total does not equal sum of line VAT (Marta Kowalczyk, 2026-11-09 10:47)
- [Reported] About 140 invoices in EUR and NOK issued since 2 Nov (Marta Kowalczyk, 2026-11-09 10:47)
- [Reported] Auditors require line-by-line VAT rounding; per-invoice rounding not acceptable (Marta Kowalczyk, 2026-11-09 10:47 and 15:30)
- [Reported] Auditors are in on Thursday (Marta Kowalczyk, 2026-11-10 13:55); the account record also notes an audit on site 12 to 13 November (CSM note)
- [Verified] Account setting "VAT rounding: per line" is on, last changed 14 March 2026 (Tom Reyes, account setting, 2026-11-09 14:30)
- [Verified] INV-LM-11402, INV-LM-11417, INV-LM-11431 (all EUR): invoice VAT total is EUR 0.01 below sum of line VAT (Tom Reyes, checked invoices, 2026-11-09 14:30)
- [Verified] Sample of 20 EUR invoices issued 2 to 9 Nov: 7 differ by 0.01 (5 lower, 2 higher), 13 match; 9 of 9 NOK and 11 GBP sampled invoices match (Tom Reyes, sample check, 2026-11-09 14:30)
- [Verified] Sandbox repro: EUR invoice, 3 lines of EUR 10.33 at 20% VAT, line VAT 2.07 each (sum 6.21), invoice VAT total 6.20; same invoice in GBP gives 6.21 (Tom Reyes, sandbox, 2026-11-09 14:30)
- [Verified] In sandbox, switching rounding to "per invoice" and back to "per line" did not change EUR behaviour (Tom Reyes, sandbox, 2026-11-09 14:30)
- [Reported] Release notes for 8.2.4 (deployed 2 Nov): "Improved currency conversion precision for non-base-currency invoices." Link to the fault is not confirmed (Tom Reyes, 2026-11-09 14:30, quoting release notes)
- Conflict: customer reports every multi-currency invoice is wrong; verified samples show NOK 0 of 9 and EUR 7 of 20 affected. Not all EUR invoices are affected, and the customer's 140 count is unverified.
- Conflict to check: Tom's hypothesis is that the EUR VAT total is computed on the invoice total ("seems", 2026-11-09 14:45). That fits the sandbox case and the 5 "lower" invoices, but it is not shown to explain the 2 "higher" invoices.

## Tried so far
- 2026-11-09 11:20, Tom Reyes: asked customer for example invoice numbers -> customer supplied three at 12:05
- 2026-11-09 14:30, Tom Reyes: checked the three invoices, sampled 20 EUR, 9 NOK, 11 GBP invoices -> results above
- 2026-11-09 14:30, Tom Reyes: reproduced in customer sandbox -> reproduced for EUR
- 2026-11-09 14:30, Tom Reyes: toggled rounding to per-invoice and back in sandbox -> no change for EUR
- 2026-11-09 14:45, Tom Reyes: proposed per-invoice rounding as workaround -> customer rejected it (15:30); not applied
- 2026-11-10 09:10, Tom Reyes: said he had asked CSM Owen Pryce to go through service-level terms with the customer -> result not recorded; no message to or from Owen is in the thread
- 2026-11-10 14:20, Tom Reyes: escalated to Tier 2 -> status Escalated, priority P2

## Commitments to the customer
- "I'll send you a written summary of what we've reproduced, including the sandbox example, by 17:00 UK time today (Tuesday 10 November)." (Tom Reyes, 2026-11-10 09:10), due 17:00 UK time 2026-11-10 (UK is on GMT in November, so 17:00 UTC), open; not sent as of the 14:20 escalation note.
- "I'm escalating the fault to our Product Engineering Support team today." (Tom Reyes, 2026-11-10 09:10), due today, met (escalated 14:20).
- "I'll ask engineering whether a fix would recalculate invoices already issued." (Tom Reyes, 2026-11-10 09:10), due not stated, open. No fix date or recalculation promised: "I can't give you a fix date" and "I can't promise that it will".
- Reported, unconfirmed: customer says the Enterprise contract requires a fix "within 24 hours" and asked for confirmation (Marta Kowalczyk, 2026-11-09 10:47 and 15:30). This is the customer's claim about the contract, not a promise from us. Tom declined to confirm: "I'm not able to confirm contract terms myself."

## Service level
- Plan: Quillbill Trade (annual subscription); support level Enterprise, "terms in Master Services Agreement, Schedule 3" (account record)
- Priority: P2 (set at ticket creation and unchanged at escalation, thread 2026-11-09 10:47 and 2026-11-10 14:20). The policy's priority criteria were not supplied, so whether the reported impact (about 140 invoices, audit on 12 to 13 Nov) warrants a higher priority is Undetermined.
- Target: Undetermined. Missing input: MSA Schedule 3 / support policy text. No clause is available to quote. The customer's "24 hours" is reported only.
- Clock: start event, business-hours, time-zone and pause rules Undetermined (policy not supplied). Assumes the clock started at ticket creation, 2026-11-09 10:47 UTC; the policy does not state this.
- Deadline: Undetermined. For reference only, if a 24-hour target ran from creation (assumes customer's reading and creation start; the policy does not state either), it would have fallen at 2026-11-10 10:47 UTC, already passed at as-of; whether it applies, and to what (response, fix), is unknown. As of now = 2026-11-10 14:20 UTC (as-of time given in the thread export).

## Recommended next action
Establish the cause on the 8.2.4 EUR path: compare VAT total calculation for non-base-currency invoices before and after 8.2.4, and explain why 7 of 20 EUR invoices are affected (including the 2 where the total is higher than the line sum) while NOK and GBP are not. This is the most decisive open question: the only evidence so far is a sandbox reproduction and an unconfirmed release-note link. The answer feeds the customer's three asks (fix, recalculation of issued invoices, written summary for auditors). Separately, the 17:00 UTC summary promise is imminent; agree today whether Tom sends it or Tier 2 does.

Open questions:
- What does MSA Schedule 3 say for Enterprise at P2 (and at P1), and does the "24 hours" apply? Has Owen Pryce actually been contacted?
- Does the reported impact (about 140 invoices, audit 12 to 13 Nov) qualify for a higher priority under the policy?
- Is 8.2.4 the cause, and why are only some EUR invoices affected, including the 2 "higher" cases?
- Does the fault affect production invoices as in the sandbox? (Repro was sandbox only; the three invoice differences and sample were observed on issued invoices.)
- Would a fix recalculate the invoices already issued, or must the customer raise credit notes?
- How many invoices are actually affected (customer says about 140 EUR and NOK; only a 40-invoice sample was checked)?

Next customer update due: 17:00 UK time (17:00 UTC) on 2026-11-10, the written summary promised by Tom Reyes (2026-11-10 09:10).
