# Escalation handoff: QB-203977 - Per-line VAT rounding not applied to some EUR invoices since 8.2.4

Customer: Lindqvist Marine Supplies Ltd (LMS-0855) | Tier: Enterprise (terms in MSA Schedule 3) | Priority: P2 (set on case at creation and at escalation) | Prepared: 2026-11-10 14:20 UTC (as-of time in the ticket export)

## Service level
Not determinable: support policy not supplied, so no target is quoted. The MSA Schedule 3 terms are not in the material. | Deadline: not determinable | Status: not determinable
Marta says the Enterprise contract requires a fix "within 24 hours" [Reported, Marta Kowalczyk, 2026-11-09 10:47]. Nobody has checked this against a policy or contract. Tom Reyes would not confirm it and passed it to the CSM, Owen Pryce [Verified, Tom Reyes, 2026-11-10 09:10]. Look up the Enterprise P2 terms yourself. If Marta's 24 hours counted from ticket creation (2026-11-09 10:47 UTC), it would already have passed, but that is unconfirmed and depends on the clock and pause rules, which are not supplied.

## Problem as currently understood
Since release 8.2.4 (deployed 2 Nov), some EUR invoices show an invoice VAT total that differs by EUR 0.01 from the sum of the line VAT, although the account is set to per-line VAT rounding. The sandbox reproduction suggests the total is computed on the invoice net total rather than line by line. The customer says every multi-currency invoice is affected; support's sample shows 7 of 20 EUR invoices, and no NOK or GBP differences.
- [Verified] Account setting "VAT rounding: per line" is on, last changed 14 March 2026 (Tom Reyes, 2026-11-09 14:30)
- [Verified] The 3 invoices INV-LM-11402, 11417 and 11431 (EUR) each have an invoice VAT total EUR 0.01 below the sum of line VAT (Tom Reyes, 2026-11-09 14:30)
- [Verified] Sample of 20 EUR invoices issued 2-9 Nov: 7 differ by 0.01 (5 lower, 2 higher), 13 match. 9 of 9 NOK sampled and 11 GBP sampled show no difference (Tom Reyes, 2026-11-09 14:30)
- [Verified] Sandbox repro (copy of production settings): EUR invoice, 3 lines of EUR 10.33 at 20% VAT. Line VAT 2.07 each, sum 6.21; invoice VAT total 6.20 (20% of 30.99 rounded). The same invoice in GBP gives 6.21 (Tom Reyes, 2026-11-09 14:30)
- [Verified] Switching the sandbox setting to "per invoice" and back to "per line" made no change for EUR (Tom Reyes, 2026-11-09 14:30)
- [Reported] Release notes for 8.2.4 (deployed 2 Nov) say "Improved currency conversion precision for non-base-currency invoices". Tom calls the link "possible; not confirmed" (Tom Reyes, 2026-11-09 14:30)
- [Reported] "Every multi-currency invoice we issue has the wrong VAT total"; about 140 invoices in EUR and NOK issued since 2 Nov (Marta Kowalczyk, 2026-11-09 10:47). This conflicts with the sample above, where NOK showed no differences.
- [Reported] The auditors require line-by-line rounding, so per-invoice rounding is not acceptable (Marta Kowalczyk, 2026-11-09 10:47 and 15:30). Auditors are on site Thursday 12 Nov (Tom Reyes escalation note, 2026-11-10 14:20; also in the account record as a CSM-noted flag, 12 to 13 Nov).

## What has been tried
1. Asked the customer for example invoice numbers - Tom Reyes, 2026-11-09 11:20 - Resolved (customer supplied three, 12:05)
2. Checked the three invoices, sampled 20 EUR, 9 NOK and 11 GBP invoices - Tom Reyes, 2026-11-09 14:30 - Partial: difference confirmed on EUR only
3. Reproduced in the customer's sandbox - Tom Reyes, 2026-11-09 14:30 - Partial: reproduced the EUR discrepancy; cause not established
4. Switched sandbox rounding to "per invoice" and back to "per line" - Tom Reyes, 2026-11-09 14:30 - No change for EUR
5. Offered per-invoice rounding as a workaround - Tom Reyes, 2026-11-09 14:45 - No change to the problem: customer rejected it, auditors require per-line
6. Asked the CSM Owen Pryce to go through the service-level terms with the customer - Tom Reyes, 2026-11-10 09:10 - Unknown: no result recorded

## Commitments to the customer
- "I'm escalating the fault to our Product Engineering Support team today." - Tom Reyes, 2026-11-10 09:10 - due 2026-11-10 - met (escalated 14:20)
- "I'll ask engineering whether a fix would recalculate invoices already issued. I can't promise that it will" - Tom Reyes, 2026-11-10 09:10 - no time stated - open (the escalation note lists it as an open ask; no answer recorded). No outcome is promised.
- "I'll send you a written summary of what we've reproduced, including the sandbox example, by 17:00 UK time today (Tuesday 10 November)." - Tom Reyes, 2026-11-10 09:10 - due 2026-11-10 17:00 UK time (UK is on GMT on this date, so 17:00 UTC; 2h40m after the as-of time) - open; the escalation note says it has not been sent yet. Customer: "Please make sure the summary arrives today" (13:55).
- "I can't give you a fix date." - Tom Reyes, 2026-11-10 09:10 - this is a statement, not a promise, and no fix date has been committed.
Claimed by customer, not found in thread: that the Enterprise contract requires a fix within 24 hours, and a request for confirmation "today" (Marta Kowalczyk, 2026-11-09 10:47). The thread has no support confirmation of this, and Tom declined to confirm it.

## Open questions
- What Enterprise P2 terms apply (MSA Schedule 3 and the support policy are not supplied), and what Owen Pryce told the customer.
- What in 8.2.4 changed for EUR invoices, and why NOK, also non-base, shows no differences. Is the code path currency-specific?
- Why 13 of 20 EUR invoices are unaffected, and whether the affected ones share a pattern, for example line count or rounding boundaries.
- Exact error text and version details in production: no logs or version checks beyond the release notes are recorded.
- Total count of affected invoices. The customer's "about 140" covers EUR and NOK and is unverified, and the sample is only 20.
- Whether a fix would recalculate issued invoices or whether credit notes are needed (the customer's question 2).
- Who sends the written summary due at 17:00 UK time, and whether it may state a cause.

## Recommended next action
Inspect how 8.2.4 computes invoice VAT total for non-base-currency (EUR) invoices, using the sandbox repro (3 x EUR 10.33 at 20%, expected 6.21, actual 6.20), and confirm whether per-line rounding is bypassed. Reason: this is the only reproduced failure, and the 8.2.4 conversion-precision change is the one candidate cause. Get the confirmed finding to Tom Reyes in time for his customer summary due 17:00 UK time (17:00 UTC) today, 2026-11-10, since the auditors arrive Thursday 12 Nov. Follow-ups: (1) answer whether a fix can recalculate issued invoices; (2) confirm the service-level terms with Owen Pryce, as the policy was not supplied.

Missing input: support policy. With it, the service-level section (target, deadline, status) could be completed.
