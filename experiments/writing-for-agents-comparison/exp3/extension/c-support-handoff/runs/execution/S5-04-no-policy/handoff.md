Clarifying question: Please supply the support policy for this account (the account record points to Master Services Agreement, Schedule 3). Without it the service-level target and deadline for this Enterprise P2 ticket cannot be worked out, and the customer's "24 hours" claim cannot be checked.

# Escalation handoff: QB-203977, Lindqvist Marine Supplies Ltd

**Summary:** Since release 8.2.4 (2 Nov), per-line VAT rounding is not applied to some EUR invoices, so the invoice VAT total differs from the sum of line VAT by EUR 0.01; support has reproduced it in the customer's sandbox. Most urgent: Tom Reyes promised the customer a written summary by 17:00 UK time (17:00 UTC, GMT) on 10 Nov, not yet sent, 2 h 40 min after the reference time; auditors are on site 12 to 13 Nov.
**Reference time:** 2026-11-10 14:20 UTC (latest thread entry)

## Problem as currently understood
On EUR invoices, the invoice VAT total appears to be calculated on the invoice net total rather than summed from per-line rounded VAT, although the account is set to per-line rounding. The fault was not found in NOK or GBP samples. A link to release 8.2.4 is suspected but not confirmed.
- [Verified] Account setting "VAT rounding: per line" is on, last changed 14 March 2026 (Tom Reyes, internal note, 2026-11-09 14:30; account record)
- [Verified] INV-LM-11402, INV-LM-11417, INV-LM-11431 each have an invoice VAT total EUR 0.01 lower than the sum of line VAT (Tom Reyes, internal note, 2026-11-09 14:30)
- [Verified] Of 20 EUR invoices issued 2 to 9 Nov, 7 differ by EUR 0.01 (5 lower, 2 higher), 13 match; 0 of 9 NOK and 0 of 11 sampled GBP invoices differ (Tom Reyes, internal note, 2026-11-09 14:30)
- [Verified] Sandbox repro: EUR invoice, 3 lines of EUR 10.33 at 20%: line VAT 2.07 each, sum 6.21, invoice VAT total 6.20 (20% of 30.99 rounded); same invoice in GBP gives 6.21 (Tom Reyes, internal note, 2026-11-09 14:30)
- [Verified] Release 8.2.4 deployed 2 Nov; its notes say "Improved currency conversion precision for non-base-currency invoices" (Tom Reyes, internal note, 2026-11-09 14:30)
- [Reported] "Every multi-currency invoice" has the wrong VAT total, about 140 EUR and NOK invoices issued since 2 Nov (Marta Kowalczyk, 2026-11-09 10:47). The recorded sample governs: 7 of 20 EUR and 0 of 9 NOK differ.
- [Reported] Auditors require per-line rounding, so the per-invoice workaround is not acceptable (Marta Kowalczyk, 2026-11-09 10:47 and 15:30)
- [Verified] External audit on site 12 to 13 Nov 2026 (account record; also Reported by Marta Kowalczyk, 2026-11-10 13:55)
Open questions:
- Did the 8.2.4 change cause this, and why EUR but not NOK, when both are non-base currencies?
- How many of the roughly 140 issued EUR and NOK invoices are affected (only 20 EUR and 9 NOK checked)?
- Will a fix recalculate invoices already issued, or must the customer raise credit notes?
- Are other customers with per-line rounding and non-base-currency invoices affected?

## Tried so far
- Asked customer for example invoice numbers, by Tom Reyes, 2026-11-09 11:20: three EUR invoices supplied 12:05
- Inspected account rounding setting, by Tom Reyes, 2026-11-09 14:30: per line, on
- Checked the three invoices and sampled EUR, NOK, GBP invoices, by Tom Reyes, 2026-11-09 14:30: results as above
- Reproduced in customer sandbox, by Tom Reyes, 2026-11-09 14:30: EUR VAT total 6.20 vs line sum 6.21; GBP correct
- Switched sandbox rounding to per invoice and back to per line, by Tom Reyes, 2026-11-09 14:30: no change for EUR
- Reviewed 8.2.4 release notes, by Tom Reyes, 2026-11-09 14:30: possible link, not confirmed
- Offered per-invoice rounding as workaround, by Tom Reyes, 2026-11-09 14:45: rejected by customer 15:30 (auditors)
- Escalated to Tier 2 (Product Engineering Support), by Tom Reyes, 2026-11-10 14:20: status Escalated, priority P2

## Commitments to the customer
- "I'll send you a written summary of what we've reproduced, including the sandbox example, by 17:00 UK time today (Tuesday 10 November).", Tom Reyes, 2026-11-10 09:10: outstanding, due 2026-11-10 17:00 UTC (UK on GMT), 2 h 40 min remaining; escalation note confirms it has not been sent
- "I'm escalating the fault to our Product Engineering Support team today.", Tom Reyes, 2026-11-10 09:10: met (escalated 2026-11-10 14:20)
- "I'll ask engineering whether a fix would recalculate invoices already issued.", Tom Reyes, 2026-11-10 09:10: unclear: the question is listed as an open ask in the escalation note (14:20), but no answer or reply to the customer is recorded
- "I've asked your Customer Success Manager, Owen Pryce, to go through the service-level terms in your contract with you.", Tom Reyes, 2026-11-10 09:10: unclear: no contact from Owen Pryce is recorded in the thread
- Claimed by customer, not found in thread: that the Enterprise contract requires a fix within 24 hours (Marta Kowalczyk, 2026-11-09 10:47 and 15:30). No vendor entry confirms it; Tom Reyes declined to confirm it (2026-11-10 09:10).

## Service level
- Tier: Enterprise, terms in MSA Schedule 3 (account record) | Priority: P2 (ticket, events 2026-11-09 10:47 and 2026-11-10 14:20)
- Target: Not determinable: the support policy (MSA Schedule 3) was not supplied. The customer's claim of a 24-hour fix obligation is content attributed to Marta Kowalczyk, not a service-level term.
- Deadline: Not determinable: no policy target or clock rules.
- Status: Not determinable.

## Recommended next action
Investigate the EUR VAT total calculation changed in 8.2.4 against the sandbox repro (3 x EUR 10.33 at 20%), and establish why NOK is unaffected and whether a fix would recalculate issued invoices, because the fault is reproduced, isolated to EUR, and dates from the 8.2.4 deployment. Serves: the customer's open asks (fix, recalculation of issued invoices) and the 12 to 13 Nov audit.
Tell the customer: by 17:00 UTC on 10 Nov, the promised written summary (sandbox example, invoice findings, sample results including that 2 of the 7 EUR differences were higher, not lower); confirm with Tom Reyes who sends it. Before the audit on 12 Nov, whether issued invoices will be recalculated or need credit notes.

## Blocked
Support policy (MSA Schedule 3) missing: blocks the service-level target, deadline and status, and checking the customer's 24-hour claim.
