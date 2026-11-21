# Escalation handoff: QB-203977 - Per-line VAT rounding not applied to some EUR invoices since 8.2.4

Customer: Lindqvist Marine Supplies Ltd (LMS-0855) | Tier: Enterprise (account record) | Priority: P2 (set on case, 2026-11-09 10:47 UTC and 2026-11-10 14:20 UTC) | Prepared: current time not given in the case; this handoff reflects the thread up to its last entry, 2026-11-10 14:20 UTC

## Service level
Not determinable: support policy not supplied. | Deadline: not determinable | Status: not determinable
The account record says Enterprise terms are in "Master Services Agreement, Schedule 3", which was not supplied. Look up the P2 response and resolution targets for Enterprise there. The customer states "Under our Enterprise contract you are required to fix this within 24 hours" [Reported] (Marta Kowalczyk, 2026-11-09 10:47 UTC); support has not confirmed it (Tom Reyes, 2026-11-10 09:10 UTC) and it is unchecked against the contract.

## Problem as currently understood
Since release 8.2.4 (deployed 2 Nov), some EUR invoices for this account show an invoice VAT total that differs by EUR 0.01 from the sum of the line VAT, although the account is set to per-line VAT rounding. Support reproduced it in the customer's sandbox: the EUR invoice VAT total appears to be computed on the invoice total, while the same invoice in GBP rounds per line. Support found no differences in NOK or GBP samples. The customer says every multi-currency invoice (EUR and NOK) is wrong; support's sample does not support that for NOK or for all EUR invoices.
- [Verified] Account setting "VAT rounding: per line" is on, last changed 14 March 2026 (Tom Reyes internal note, 2026-11-09 14:30 UTC)
- [Verified] INV-LM-11402, INV-LM-11417, INV-LM-11431 (all EUR): each invoice VAT total is EUR 0.01 lower than the sum of line VAT (Tom Reyes internal note, 2026-11-09 14:30 UTC)
- [Verified] Sample of 20 EUR invoices issued 2 to 9 Nov: 7 differ by 0.01 (5 lower, 2 higher), 13 match. All 9 NOK invoices: none differ. 11 GBP invoices sampled: none differ (Tom Reyes internal note, 2026-11-09 14:30 UTC)
- [Verified] Sandbox repro: EUR invoice, 3 lines of EUR 10.33 at 20% VAT; line VAT 2.07 each, sum 6.21; invoice VAT total 6.20 (20% of 30.99, rounded). Same invoice in GBP: VAT total 6.21 (Tom Reyes internal note, 2026-11-09 14:30 UTC)
- [Verified] Release notes for 8.2.4 (deployed 2 Nov) read "Improved currency conversion precision for non-base-currency invoices" (Tom Reyes internal note, 2026-11-09 14:30 UTC)
- [Reported] The 8.2.4 change is the cause: Tom Reyes's hypothesis, "Possible link; not confirmed" (Tom Reyes internal note, 2026-11-09 14:30 UTC)
- [Reported] Problem started "since your update last week"; "every multi-currency invoice" has the wrong VAT total; about 140 EUR and NOK invoices issued since 2 November (Marta Kowalczyk, 2026-11-09 10:47 UTC)
- [Reported] Auditors require per-line rounding; per-invoice rounding is not acceptable (Marta Kowalczyk, 2026-11-09 10:47 and 15:30 UTC)
- [Reported] Auditors are on site Thursday (12 Nov) (Marta Kowalczyk, 2026-11-10 13:55 UTC); the account record also flags "External audit on site 12 to 13 November 2026 (noted by CSM)"

## What has been tried
1. In the sandbox, switched VAT rounding to "per invoice" and back to "per line" - Tom Reyes, 2026-11-09 14:30 UTC - No change (EUR still wrong)

Not tried: switching production to per-invoice rounding was offered as a workaround (Tom Reyes, 2026-11-09 14:45 UTC) and rejected by the customer because of auditor requirements (Marta Kowalczyk, 2026-11-09 15:30 UTC). The thread records no fix attempts by the customer.

## Commitments to the customer
- "I'm escalating the fault to our Product Engineering Support team today." - Tom Reyes, 2026-11-10 09:10 UTC - due 2026-11-10 - met (escalated to Tier 2, 2026-11-10 14:20 UTC)
- "I'll send you a written summary of what we've reproduced, including the sandbox example, by 17:00 UK time today (Tuesday 10 November)." - Tom Reyes, 2026-11-10 09:10 UTC - due 2026-11-10 17:00 UTC (UK time is GMT, UTC+0, in November) - open: not sent as of 2026-11-10 14:20 UTC (Tom Reyes escalation note); overdue if not sent by 17:00 UTC
- "I'll ask engineering whether a fix would recalculate invoices already issued. I can't promise that it will" - Tom Reyes, 2026-11-10 09:10 UTC - due none stated - open (listed as an open ask in the escalation note, 2026-11-10 14:20 UTC). This is a promise to ask, not a promise of recalculation.
- "I've asked your Customer Success Manager, Owen Pryce, to go through the service-level terms in your contract with you." - Tom Reyes, 2026-11-10 09:10 UTC - due none stated - status unknown: no CSM contact recorded in the thread

No fix date has been given: "I can't give you a fix date" (Tom Reyes, 2026-11-10 09:10 UTC).

Claimed by customer, not found in thread: a contractual obligation to fix within 24 hours (Marta Kowalczyk, 2026-11-09 10:47 UTC, repeated 15:30 UTC). Support declined to confirm it; check against MSA Schedule 3.

## Open questions
- What are the Enterprise P2 targets in MSA Schedule 3, and which timestamp starts the clock?
- Is the issue confined to EUR? Support's samples found nothing in NOK (9 of 9) or GBP (11 sampled), but the customer says NOK is affected too. Why would NOK, also a non-base currency for this GBP-based account, behave differently from EUR?
- How many EUR (and NOK) invoices has the account issued since 2 Nov 2026, and exactly which ones differ? Only a sample of 20 EUR invoices has been checked against the customer's figure of about 140.
- Is 8.2.4 the cause? Do the 5 lower and 2 higher differences in the sample both come from the same code path as the sandbox result?
- Does the sandbox run the same release (8.2.4) as production? The account record says it is refreshed monthly; the last refresh date is not given.
- Will a fix recalculate already-issued invoices, or must the customer raise credit notes?
- Has the 17:00 UTC written summary been sent, and has Owen Pryce contacted the customer?

## Recommended next action
On LMS-0855 production data, run a query for every invoice issued since 2026-11-02 where the invoice VAT total differs from the sum of line VAT, broken down by currency (EUR, NOK, GBP); in parallel, trace the 8.2.4 VAT-total calculation for non-base-currency invoices using the sandbox repro (3 lines of EUR 10.33 at 20%: expected 6.21, shows 6.20). Reason: support has a confirmed repro but only a 20-invoice EUR sample, the customer reports NOK too, and the customer must decide per invoice whether to raise credit notes before the audit. Do this before the auditors arrive on Thursday 2026-11-12 [Reported by customer, corroborated by account flag]; the contractual deadline is not determinable without MSA Schedule 3.

Follow-ups:
1. Answer whether the fix will recalculate issued invoices, so Tom Reyes can reply to the customer's open question before 2026-11-12.
2. Confirm with Tom Reyes that the written summary went out by 2026-11-10 17:00 UTC; it covers only what was reproduced and does not depend on engineering findings.

---
Missing input: support policy (MSA Schedule 3 for Enterprise). Supplying it would unlock the P2 service-level targets, the deadline and the status, and would settle the customer's 24-hour claim.
