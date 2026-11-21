Clarifying question: Please supply the support policy (and the MSA Schedule 3 terms referred to in the account record): the response and resolution targets per plan and priority, the clock start event, any business-hours rule and any pause rules. Until then the service-level deadline is cannot determine.

# Escalation handoff: QB-203977: EUR invoices show VAT total off by 0.01 from the sum of line VAT since 8.2.4

**Customer:** Lindqvist Marine Supplies Ltd (LMS-0855), Quillbill Trade, Enterprise support level · **Priority:** P2 · **Next deadline:** cannot determine: support policy not supplied (as of 2026-11-10 14:20 UTC). Nearest known date: written summary promised to the customer by 17:00 UK time, 2026-11-10, open with 2h 40m remaining.

## Problem as currently understood
Per-line VAT rounding appears not to be applied to some EUR invoices since release 8.2.4 (deployed 2 Nov); the invoice VAT total is calculated on the invoice total instead, giving a 0.01 difference from the sum of line VAT. NOK and GBP samples show no differences. The 8.2.4 change is a possible cause, not confirmed. The customer's external auditors are on site 12 to 13 November and the customer needs per-line rounding.

Evidence:
- [Verified] Account setting "VAT rounding: per line" is on, last changed 14 March 2026 (Tom Reyes internal note, 2026-11-09 14:30)
- [Verified] INV-LM-11402, INV-LM-11417 and INV-LM-11431 (EUR) each have an invoice VAT total EUR 0.01 below the sum of line VAT (Tom Reyes, 2026-11-09 14:30)
- [Verified] Sample of 20 EUR invoices issued 2 to 9 Nov: 7 differ by 0.01 (5 lower, 2 higher), 13 match (Tom Reyes, 2026-11-09 14:30)
- [Verified] 9 NOK and 11 GBP invoices sampled in the same period: none differ (Tom Reyes, 2026-11-09 14:30)
- [Verified] Reproduced in the customer's sandbox: 3 lines of EUR 10.33 at 20% VAT, line VAT 2.07 each (sum 6.21), invoice VAT total 6.20 (20% of 30.99). Same invoice in GBP gives 6.21 (Tom Reyes, 2026-11-09 14:30)
- [Verified] Switching the sandbox setting to "per invoice" and back to "per line" made no change for EUR (Tom Reyes, 2026-11-09 14:30)
- [Verified] Release notes for 8.2.4, deployed 2 Nov: "Improved currency conversion precision for non-base-currency invoices" (Tom Reyes, 2026-11-09 14:30; he says link "not confirmed")
- [Reported] About 140 invoices in EUR and NOK issued since 2 November, all said to have wrong VAT totals (Marta Kowalczyk, 2026-11-09 10:47). The support sample (7 of 20 EUR differ, no NOK differences) does not support "every" invoice
- [Reported] Auditors require per-line VAT rounding, so per-invoice rounding is unacceptable (Marta Kowalczyk, 2026-11-09 10:47 and 15:30)
- [Reported] The Enterprise contract requires a fix within 24 hours (Marta Kowalczyk, 2026-11-09 10:47). Not checked against any contract text
- [Inferred] Defect is specific to non-base-currency (EUR) invoices, not NOK (rests on: GBP is base currency and unaffected; NOK sample of 9 clean, though NOK is also non-base and could be a small-sample miss)
- [Inferred] Possible exposure is EUR invoices issued since 2 Nov, of which about 35% in the sample differ (rests on: 7 of 20 sample; the 140 count is Reported and mixes EUR and NOK)

## Tried so far
| When (UTC) | Who | Action | Result |
|---|---|---|---|
| 2026-11-09 11:20 | Tom Reyes | Asked customer for two or three affected invoice numbers | Customer supplied three at 12:05 |
| 2026-11-09 14:30 | Tom Reyes | Checked the three invoices | Each EUR 0.01 lower than sum of line VAT |
| 2026-11-09 14:30 | Tom Reyes | Sampled 20 EUR, 9 NOK, 11 GBP invoices | EUR 7 of 20 differ; NOK and GBP none |
| 2026-11-09 14:30 | Tom Reyes | Reproduced in sandbox (copy of production settings) | Reproduced for EUR; GBP correct |
| 2026-11-09 14:30 | Tom Reyes | Toggled sandbox rounding to per invoice and back to per line | No change for EUR |
| 2026-11-09 14:30 | Tom Reyes | Checked release notes | 8.2.4 currency precision change, link unconfirmed |
| 2026-11-09 14:45 | Tom Reyes | Offered per-invoice rounding as workaround | Ruled out: customer's auditors do not accept it (2026-11-09 15:30) |
| 2026-11-10 09:10 | Tom Reyes | Asked CSM Owen Pryce to go through the service-level terms with the customer | No result recorded |
| 2026-11-10 14:20 | Tom Reyes | Escalated to Tier 2 | Open |

Not established: why only some EUR invoices differ (13 of 20 match, possibly rounding-dependent), why NOK is unaffected, and whether the sandbox toggle result also holds in production.

## Commitments to the customer
| Commitment (quoted) | Made by | When | Status |
|---|---|---|---|
| "I'm escalating the fault to our Product Engineering Support team today." | Tom Reyes | 2026-11-10 09:10 | Met: escalated 2026-11-10 14:20 |
| "I'll ask engineering whether a fix would recalculate invoices already issued." | Tom Reyes | 2026-11-10 09:10 | Outstanding: the question is listed as an open ask in the escalation note; no answer yet. No time was promised |
| "I'll send you a written summary of what we've reproduced, including the sandbox example, by 17:00 UK time today (Tuesday 10 November)." | Tom Reyes | 2026-11-10 09:10 | Outstanding: due 17:00 UK time = 17:00 UTC on 10 Nov (Inferred: UK is on GMT in November); 2h 40m left as of 14:20 UTC; escalation note says not yet sent |
| "I've asked your Customer Success Manager, Owen Pryce, to go through the service-level terms in your contract with you." | Tom Reyes | 2026-11-10 09:10 | Outstanding: no date given; thread shows no sign that Owen has contacted the customer |

Support explicitly declined to give a fix date ("I can't give you a fix date") and to confirm the 24 hours ("I'm not able to confirm contract terms myself").
Claimed by the customer, not found in the thread: that the Enterprise contract requires a fix within 24 hours (a contract claim, not a support promise). Nothing else claimed.

## Service level
- Plan: Quillbill Trade, support level Enterprise (terms in MSA Schedule 3) [Verified: account record]
- Priority: P2 [Verified: ticket event at creation, 2026-11-09 10:47; no change since; the customer did not assert a different priority]
- Target: cannot determine: support policy not supplied, and Schedule 3 is not in the account record. The customer's "24 hours" is [Reported] and unchecked
- Clock start: cannot determine (policy not supplied). Ticket created 2026-11-09 10:47 UTC; elapsed since then is 27h 33m as of 2026-11-10 14:20 UTC, in calendar time only, with no business-hours or pause rules applied
- Deadline and status: cannot determine: support policy not supplied. If the customer's 24-hour claim were counted from creation it would be 2026-11-10 10:47 UTC, but that is unverified and must not be treated as a breach until the contract is checked
- As of: 2026-11-10 14:20 UTC (from the ticket export)

## Recommended next action
Tier 2 engineer: by 16:00 UTC today (about an hour before the 17:00 summary), confirm or rule out the 8.2.4 change as the cause of EUR per-line rounding being skipped, and tell Tom Reyes what can be stated to the customer, so the written summary for the auditors goes out by 17:00 UTC. The cause is the main unverified point, and the summary, the recalculation question and the auditors' visit on Thursday 12 Nov all depend on it. Follow-ups: answer whether a fix would recalculate issued invoices; check why 13 of 20 EUR invoices and all NOK invoices are unaffected.

## Gaps and open questions
- Missing input: support policy (targets, clock start, business hours, pauses). MSA Schedule 3 terms are also not supplied. Please supply them.
- Cause of the defect is unconfirmed (8.2.4 is a possible link only).
- Not checked against production data: only the sandbox reproduction and a 20-invoice sample; the full set of affected EUR invoices is unknown.
- Customer says "every" invoice is wrong across EUR and NOK; the sample contradicts this for NOK and for most EUR invoices.
- Whether affected invoices can be corrected or need credit notes is unanswered; the account record shows no open credits.
- Customer's 24-hour contract claim is unverified; the CSM, Owen Pryce, has been asked to cover contract terms.
- The account record notes external audit on site 12 to 13 November (CSM note); the ticket says auditors are in on Thursday 12 Nov.
- Please supply the support policy and Schedule 3 so the deadline can be worked out.
