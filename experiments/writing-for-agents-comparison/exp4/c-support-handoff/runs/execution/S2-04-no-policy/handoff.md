# Escalation handoff: QB-203977 | Lindqvist Marine Supplies Ltd | Per-line VAT rounding not applied on some EUR invoices

**Service level:** Not determined: no policy supplied (Enterprise terms are in MSA Schedule 3, which is not in the case). The only dated item in the thread is Tom Reyes's own promise of a written summary by 17:00 UK time (17:00 UTC) on 2026-11-10, which is a commitment, not a policy term. | Status as of 2026-11-10 14:20 UTC (export time)

## Problem as currently understood
Since release 8.2.4 (deployed 2 Nov), some EUR invoices have an invoice VAT total that differs by EUR 0.01 from the sum of the line VAT, although the account is set to per-line rounding. Support Verified this on the three invoices the customer named, in a 20-invoice EUR sample (7 differ), and in a sandbox reproduction. No difference was found in the 9 NOK or 11 GBP invoices sampled. The link to 8.2.4 is only Suspected. The customer's wider claims (every multi-currency invoice, about 140 invoices, NOK affected) are Reported and not borne out by the sample so far.

| Statement | Label | Source (author, timestamp) |
| --- | --- | --- |
| Every multi-currency invoice since last week has the wrong VAT total | Reported | Marta Kowalczyk, 2026-11-09 10:47 |
| About 140 EUR and NOK invoices issued since 2 Nov are affected or in doubt | Reported | Marta Kowalczyk, 2026-11-09 10:47 |
| Auditors require line-by-line VAT rounding and per-invoice rounding is not acceptable | Reported | Marta Kowalczyk, 2026-11-09 10:47 and 15:30 |
| Account setting "VAT rounding: per line" is on, last changed 14 March 2026 | Verified (Tom Reyes) | Tom Reyes, internal note, 2026-11-09 14:30 |
| INV-LM-11402, INV-LM-11417, INV-LM-11431 (EUR) each have invoice VAT EUR 0.01 below the sum of line VAT | Verified (Tom Reyes) | Tom Reyes, internal note, 2026-11-09 14:30 |
| 7 of 20 sampled EUR invoices (2 to 9 Nov) differ by 0.01 (5 lower, 2 higher); 13 match | Verified (Tom Reyes) | Tom Reyes, internal note, 2026-11-09 14:30 |
| 0 of 9 NOK and 0 of 11 GBP invoices sampled differ | Verified (Tom Reyes) | Tom Reyes, internal note, 2026-11-09 14:30 |
| Sandbox: 3 lines of EUR 10.33 at 20% VAT give line VAT 2.07 each (6.21) but invoice VAT 6.20; same invoice in GBP gives 6.21 | Verified (Tom Reyes) | Tom Reyes, internal note, 2026-11-09 14:30 |
| Toggling the sandbox setting to per invoice and back does not change the EUR result | Verified (Tom Reyes) | Tom Reyes, internal note, 2026-11-09 14:30 |
| On EUR invoices the VAT total is calculated on the invoice total instead of line by line | Suspected | Tom Reyes, 2026-11-09 14:30 and 14:45 ("seems to be") |
| Release 8.2.4 ("Improved currency conversion precision for non-base-currency invoices", deployed 2 Nov) caused it | Suspected | Tom Reyes, internal note, 2026-11-09 14:30 ("Possible link; not confirmed") |
| Customer's auditors are on site Thursday 12 Nov | Reported | Marta Kowalczyk, 2026-11-10 13:55; Tom Reyes, escalation note, 2026-11-10 14:20; account flag by CSM (12 to 13 Nov) |

## What has been tried
| Action | By | When | Result | Label |
| --- | --- | --- | --- | --- |
| Asked customer for example invoice numbers | Tom Reyes | 2026-11-09 11:20 | Customer supplied three EUR invoice numbers | Verified |
| Checked the three invoices | Tom Reyes | 2026-11-09 14:30 | Each invoice VAT total is EUR 0.01 below sum of line VAT | Verified (Tom Reyes) |
| Sampled 20 EUR, 9 NOK, 11 GBP invoices | Tom Reyes | 2026-11-09 14:30 | EUR 7/20 differ; NOK 0/9; GBP 0/11 | Verified (Tom Reyes) |
| Reproduced in customer's sandbox (copy of production settings) | Tom Reyes | 2026-11-09 14:30 | Reproduced on EUR, not on GBP | Verified (Tom Reyes) |
| Switched sandbox rounding to per invoice and back to per line | Tom Reyes | 2026-11-09 14:30 | No change for EUR | Verified (Tom Reyes) |
| Compared against 8.2.4 release notes | Tom Reyes | 2026-11-09 14:30 | Possible link, not confirmed | Suspected |
| Offered per-invoice rounding as a workaround | Tom Reyes | 2026-11-09 14:45 | Customer refused: auditors do not accept it (customer statement) | Reported |
| Asked CSM Owen Pryce to take the customer through the contract service-level terms | Tom Reyes | 2026-11-10 09:10 (stated) | No outcome recorded in the thread | Reported (Tom's statement; no record from Owen) |
| Escalated to Tier 2 (Product Engineering Support) | Tom Reyes | 2026-11-10 14:20 | Status Escalated, priority P2 | Verified (ticket event) |

No reproduction on a production invoice other than the visible mismatch on the three named invoices; no engineering investigation has started.

## Commitments to the customer
| Commitment (quoted) | Made by (name, role) | When | Due | Status |
| --- | --- | --- | --- | --- |
| "I'm escalating the fault to our Product Engineering Support team today." | Tom Reyes, Support Agent (Tier 1) | 2026-11-10 09:10 | Today, 2026-11-10 (quoted: "today") | Kept (escalated 14:20) |
| "I'll ask engineering whether a fix would recalculate invoices already issued." | Tom Reyes, Support Agent (Tier 1) | 2026-11-10 09:10 | No date given | Outstanding (the question is listed in the escalation note but no answer yet) |
| "I'll send you a written summary of what we've reproduced, including the sandbox example, by 17:00 UK time today (Tuesday 10 November)." | Tom Reyes, Support Agent (Tier 1) | 2026-11-10 09:10 | 2026-11-10 17:00 UK time (GMT, so 17:00 UTC); about 2 h 40 min left as of 14:20 UTC | Outstanding (escalation note says not yet sent) |
| "I've asked your Customer Success Manager, Owen Pryce, to go through the service-level terms in your contract with you." | Tom Reyes, Support Agent (Tier 1) | 2026-11-10 09:10 | No date given | Outstanding (no confirmation in the thread) |

Claimed by the customer but not found in the thread: that the Enterprise contract requires a fix within 24 hours (Marta Kowalczyk, 2026-11-09 10:47, repeated 15:30); no support-side message confirms it, and Tom Reyes explicitly declined to confirm contract terms. No promise of a fix date, of recalculating issued invoices, or of credit notes was made.

## Service level
- Tier: Enterprise (account record; terms in Master Services Agreement, Schedule 3, not supplied)
- Priority: P2 (as recorded on the ticket at creation and at escalation)
- Targets: Not determined: no policy supplied. The customer's "fix within 24 hours" is a statement by its author and is not confirmed by any policy or thread entry. No clock start, deadline or status can be given for any policy target.
- Time zones: all thread timestamps are UTC. The customer's time zone is not given; the customer is UK-based by data region and the commitment above is in UK time.
- Status as of: 2026-11-10 14:20 UTC (export time given in the thread)

## Recommended next action
A Tier 2 engineer should compare the 8.2.4 change to non-base-currency invoice VAT calculation against the per-line rounding path, using the sandbox example (3 x EUR 10.33 at 20%), including why 2 of 7 sampled differences were higher rather than lower and why NOK and GBP were unaffected. If the 8.2.4 change is not the cause, the plan shifts to inspecting EUR-specific account or currency settings. Separately, Tom Reyes needs to send the written summary before 17:00 UTC today.

## Open questions
- No support policy supplied: request the Enterprise service-level terms (MSA Schedule 3 or the support policy) to determine response, fix and clock rules for P2 Enterprise. Until then no target or deadline can be stated.
- Customer claims a contractual 24-hour fix; unconfirmed. Owen Pryce is reported to be reviewing the terms with her; ask him for the outcome.
- Conflict on scope: the customer says every multi-currency invoice, including NOK, is wrong; support's samples found EUR only (7/20), NOK 0/9, GBP 0/11. The full count of affected invoices (customer says about 140) is unknown.
- Priority: P2 is recorded; whether it should be higher is not determinable without the policy's priority definitions.
- Whether a fix will recalculate issued invoices, or the customer must raise credit notes, is unanswered (promised to be asked of engineering).
- Reproduction is on the sandbox (production settings copy, refreshed monthly) only; no confirmation the sandbox setting state matches production beyond Tom's statement.
- Direction of errors is mixed (5 lower, 2 higher in the sample), which does not fit the simple "calculated on invoice total" hypothesis; untested.
- Deadline pressure: auditors on site 12 to 13 Nov (account flag) and customer needs the summary today. Whether the summary may go to the customer and auditors is Tom's call; engineering input on wording may be needed.
