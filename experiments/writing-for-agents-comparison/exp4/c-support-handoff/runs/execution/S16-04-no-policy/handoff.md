# Handoff: QB-203977, Lindqvist Marine Supplies Ltd (LMS-0855)

As of 2026-11-10 14:20 UTC (export time). Escalated to Tier 2, P2.

## 1. Problem as understood

Since release 8.2.4 (2 Nov), some EUR invoices on a per-line VAT rounding account show an invoice VAT total that differs by EUR 0.01 from the sum of line VAT. The cause is not confirmed; the customer needs a fix, a decision on invoices already issued, and a written summary for auditors on site Thursday 12 Nov.

Evidence:
- Reported: every multi-currency invoice issued since the update has a wrong VAT total; about 140 EUR and NOK invoices since 2 Nov (Marta Kowalczyk, 2026-11-09 10:47).
- Reported: auditors require per-line rounding and the account is set that way (Marta, 2026-11-09 10:47 and 15:30).
- Verified (account record setting, Tom Reyes note 2026-11-09 14:30): "VAT rounding: per line" is on, last changed 14 March 2026.
- Verified (invoice inspection): INV-LM-11402, -11417, -11431 (EUR) each have invoice VAT EUR 0.01 below the line VAT sum (Tom, 2026-11-09 14:30).
- Verified (sample): 7 of 20 EUR invoices issued 2 to 9 Nov differ by 0.01 (5 lower, 2 higher); 0 of 9 NOK; 0 of 11 GBP (Tom, 2026-11-09 14:30). This contradicts the customer's "every" and "NOK" claims for the sample checked.
- Verified (sandbox reproduction): 3 lines of EUR 10.33 at 20%; line VAT 2.07 each, sum 6.21; invoice total VAT 6.20 (20% of 30.99 rounded). Same invoice in GBP gives 6.21 (Tom, 2026-11-09 14:30).
- Verified (test): toggling sandbox rounding to per invoice and back made no change for EUR.
- Reported/unconfirmed: release notes for 8.2.4 (deployed 2 Nov) say "Improved currency conversion precision for non-base-currency invoices"; link to the bug is a suspicion only (Tom).

Open questions for Tier 2:
- Root cause, and why only some EUR invoices differ and NOK does not (NOK is also non-base currency).
- Whether a fix can recalculate already-issued invoices, or whether credit notes are needed.
- Real scope: the 140 figure is unverified; only samples were checked.

## 2. Tried so far

- Tom Reyes: inspected three customer invoices; confirmed 0.01 difference. Worked (confirmed symptom).
- Tom Reyes: sampled 20 EUR, 9 NOK, 11 GBP invoices. Worked (scoped to EUR in sample).
- Tom Reyes: reproduced in sandbox. Worked.
- Tom Reyes: switched sandbox to per-invoice and back to per-line. Failed (no change for EUR).
- Customer: no attempts reported. Workaround of per-invoice rounding offered by Tom (2026-11-09 14:45) was refused by the customer because auditors will not accept it.

## 3. Commitments to the customer

- Written summary of what was reproduced, including the sandbox example, by 17:00 UK time today, Tuesday 10 Nov (Tom Reyes, 2026-11-10 09:10). Not yet sent as of 14:20 UTC.
- Tom will ask engineering whether a fix would recalculate issued invoices; he explicitly did not promise it will (Tom, 2026-11-10 09:10).
- Owen Pryce (CSM) asked to go through service-level terms with the customer (Tom, 2026-11-10 09:10); this is a request to Owen, not a promise of an outcome. Whether Owen has done so is not in the thread.
- Soft assurance: "I'm escalating the fault to our Product Engineering Support team today" (Tom, 2026-11-10 09:10).
- No fix date given; Tom said he cannot give one. The 24-hour fix is demanded by the customer; support has not agreed to it (Tom said he cannot confirm contract terms).

## 4. Service-level status

- Plan: Quillbill Trade, Enterprise support level, terms in MSA Schedule 3 (account record). Contract 1 Jan 2026 to 31 Dec 2027.
- Applicable policy clause: Unknown. The support policy was not supplied. Not determinable: support policy not supplied.
- Clock start, deadline, time remaining or breached, breach consequences: Unknown. Needed: the policy / MSA Schedule 3 (response and fix targets, priority definitions, how the clock runs). The customer's "24 hours" is Reported only. If it applied from ticket creation (2026-11-09 10:47 UTC) it would have ended 2026-11-10 10:47 UTC, already past, but this is not established and should not be stated to the customer.
- Ticket priority is P2; whether that matches the policy's classification is Unknown.
- Dated commitment that is known: 17:00 UK time on 10 Nov. UK is on GMT in November, so 17:00 UTC; 2 h 40 min remain as of 14:20 UTC.

## 5. Recommended next action

Primary: the Tier 2 owner confirms with Tom Reyes now that the written auditor summary goes out before 17:00 UTC today, limited to verified facts (the invoice checks, sample counts, sandbox example) and stating that the cause is not confirmed and no fix date or recalculation commitment exists. Why: it is the only hard deadline in the thread, it was promised in writing, and the customer's auditors are on site Thursday 12 Nov. Then start on the 8.2.4 EUR rounding path as the likely cause.

Unverified items this depends on: root cause; whether the 7/20 rate holds across the ~140 invoices; the customer's contractual entitlement (policy not supplied).

Customer update due: the written summary by 17:00 UTC today. Do not confirm or deny the 24-hour term until the policy is read; ask Owen Pryce to take that conversation.

Missing input, requested: please supply the support policy / MSA Schedule 3 service levels so section 4 can be completed.
