Clarifying question: The support policy with its service levels (the Enterprise terms the account record places in "Master Services Agreement, Schedule 3") was not supplied with this case. Can you supply it? Without it there are no service-level targets, deadlines or statuses, and the customer's claim of a 24-hour fix term cannot be checked. The handoff below goes ahead and marks those parts "Not determinable".

# Escalation handoff: QB-203977 Per-line VAT rounding not applied to some EUR invoices since about 2 Nov

**Customer:** Lindqvist Marine Supplies Ltd (LMS-0855), plan Quillbill Trade, support level Enterprise | **Priority:** P2 (set by: not stated; recorded at ticket creation 2026-11-09 10:47 UTC and kept at P2 by Tom Reyes on escalation 2026-11-10 14:20 UTC)
**Service level:** Not determinable: support policy not supplied, next deadline Not determinable: support policy not supplied
**Open commitments:** 2, earliest due 2026-11-10 17:00 UTC (written summary for auditors; 2h 40m after the last thread entry at 14:20 UTC)

## Problem as currently understood
Tom Reyes (Tier 1) has verified that the account is set to per-line VAT rounding, yet in the customer's sandbox an EUR invoice's VAT total is calculated on the invoice total (6.20) instead of the sum of the line VAT (6.21), while the same invoice in GBP is correct; switching the setting off and on again changed nothing for EUR. In production, 7 of 20 sampled EUR invoices from 2 to 9 Nov differ from the line VAT sum by EUR 0.01 (5 lower, 2 higher), and no differences were found in 9 NOK or 11 GBP invoices. The customer reports that every multi-currency invoice is affected since "your update last week" (about 140 EUR and NOK invoices), but the samples so far support EUR only. That the cause is release 8.2.4 (deployed 2 Nov, "Improved currency conversion precision for non-base-currency invoices") is Tom Reyes's Hypothesis, which he marked "Possible link; not confirmed".

| Fact | Tag | Source |
|---|---|---|
| Every multi-currency invoice issued since "your update last week" has the wrong VAT total | Reported | Marta Kowalczyk, 2026-11-09 10:47 |
| The invoice VAT total does not equal the sum of the line VAT | Reported | Marta Kowalczyk, 2026-11-09 10:47 |
| Customer's auditors require VAT rounded line by line | Reported | Marta Kowalczyk, 2026-11-09 10:47 and 15:30 |
| About 140 invoices issued in EUR and NOK since 2 November | Reported | Marta Kowalczyk, 2026-11-09 10:47 |
| Business impact: customer has "no confidence in any of them" | Reported | Marta Kowalczyk, 2026-11-09 10:47 |
| Customer says the Enterprise contract requires a fix within 24 hours | Reported (unchecked: policy not supplied) | Marta Kowalczyk, 2026-11-09 10:47 |
| Account has Enterprise support, terms in Master Services Agreement, Schedule 3 | Verified | Account record (Support level) |
| Account setting "VAT rounding: per line" is on, last changed 14 March 2026 | Verified (Tom Reyes) | Internal note, 2026-11-09 14:30; also account record (VAT settings) |
| Base currency GBP; invoice currencies GBP, EUR, NOK; UK standard VAT rate; data region UK | Verified | Account record |
| INV-LM-11402, INV-LM-11417, INV-LM-11431 (all EUR) each have an invoice VAT total EUR 0.01 lower than the sum of line VAT | Verified (Tom Reyes) | Customer supplied numbers 2026-11-09 12:05; checked in internal note 2026-11-09 14:30 |
| 20 EUR invoices issued 2 to 9 Nov: 7 differ by 0.01 (5 lower, 2 higher), 13 match | Verified (Tom Reyes) | Internal note, 2026-11-09 14:30 |
| All 9 NOK invoices 2 to 9 Nov: none differ | Verified (Tom Reyes) | Internal note, 2026-11-09 14:30 |
| 11 GBP invoices sampled: none differ | Verified (Tom Reyes) | Internal note, 2026-11-09 14:30 |
| Sandbox repro: EUR invoice, 3 lines of EUR 10.33 at 20% VAT; line VAT 2.07 each, sum 6.21; invoice VAT total 6.20 (20% of 30.99 rounded) | Verified (Tom Reyes) | Internal note, 2026-11-09 14:30 |
| Same invoice in GBP in sandbox: VAT total 6.21 | Verified (Tom Reyes) | Internal note, 2026-11-09 14:30 |
| Switching sandbox rounding to "per invoice" and back to "per line": no change for EUR | Verified (Tom Reyes) | Internal note, 2026-11-09 14:30 |
| Sandbox is a copy of production settings, refreshed monthly | Verified | Account record (Products) |
| Release notes for 8.2.4 (deployed 2 Nov): "Improved currency conversion precision for non-base-currency invoices." | Verified (Tom Reyes read the release notes) | Internal note, 2026-11-09 14:30 |
| Per-line rounding is not applied to EUR invoices | Hypothesis (Tom Reyes) | Internal note 2026-11-09 14:30; customer message 2026-11-09 14:45 |
| The fault is linked to 8.2.4 ("Possible link; not confirmed"); the escalation note states it as "since 8.2.4 (2 Nov)" | Hypothesis (Tom Reyes) | Internal note 2026-11-09 14:30; escalation note 2026-11-10 14:20 |
| Per-invoice rounding is not acceptable to the customer's auditors | Reported | Marta Kowalczyk, 2026-11-09 15:30 |
| Auditors are in on Thursday | Reported | Marta Kowalczyk, 2026-11-10 13:55 |
| External audit on site 12 to 13 November 2026 | Verified | Account record (Account flags, noted by CSM) |
| Earlier ticket QB-196320 (P3, NOK currency formatting on PDF invoices), resolved 21 August 2026 | Verified | Account record (Recent tickets) |

**Open questions:**
- Is NOK affected? NOK is also a non-base currency (the 8.2.4 release note's scope), but 9 NOK invoices showed no difference. With only 7 of 20 EUR invoices differing, a clean sample of 9 does not rule NOK out; no NOK sandbox reproduction has been run.
- Did the fault start with 8.2.4? No EUR invoice issued before 2 Nov has been checked, so the onset date is Reported (customer) and Hypothesis (Tom Reyes) only.
- Why are 2 of the 7 differing EUR invoices higher than the line sum while the sandbox repro and the three customer invoices are lower? (Consistent with rounding on the invoice total, which can go either way, but not confirmed.)
- How many of the roughly 140 issued EUR and NOK invoices are wrong? Only 29 have been checked.
- Will a fix recalculate invoices already issued, or must the customer raise credit notes? Passed to engineering in the escalation note; no answer recorded.
- Does MSA Schedule 3 contain the 24-hour fix term the customer cites? Policy not supplied; CSM Owen Pryce has been asked to go through the terms with the customer.
- Are other customers invoicing in a non-base currency with per-line rounding affected? Not examined in the thread.

## What has been tried
| Action | By | When | Result |
|---|---|---|---|
| Asked the customer for two or three example invoice numbers | Tom Reyes (Tier 1) | 2026-11-09 11:20 UTC | Customer sent INV-LM-11402, INV-LM-11417, INV-LM-11431 (all EUR) at 12:05 UTC |
| Checked the account's VAT rounding setting | Tom Reyes | Recorded 2026-11-09 14:30 UTC (exact time not recorded) | "Per line" is on; last changed 14 March 2026 |
| Checked the three customer invoices | Tom Reyes | Recorded 2026-11-09 14:30 UTC | Each invoice VAT total EUR 0.01 below the sum of line VAT |
| Sampled production invoices: 20 EUR, 9 NOK (all), 11 GBP, issued 2 to 9 Nov | Tom Reyes | Recorded 2026-11-09 14:30 UTC | EUR: 7 differ (5 lower, 2 higher), 13 match; NOK: none differ; GBP: none differ |
| Reproduced in customer sandbox: EUR invoice, 3 lines of EUR 10.33 at 20%, compared with the same invoice in GBP | Tom Reyes | Recorded 2026-11-09 14:30 UTC | EUR VAT total 6.20 (sum of line VAT 6.21); GBP VAT total 6.21 |
| Switched sandbox rounding to "per invoice" and back to "per line" | Tom Reyes | Recorded 2026-11-09 14:30 UTC | No change for EUR |
| Read release notes for 8.2.4 | Tom Reyes | Recorded 2026-11-09 14:30 UTC | Found "Improved currency conversion precision for non-base-currency invoices"; possible link, not confirmed |
| Offered per-invoice rounding as a workaround | Tom Reyes | 2026-11-09 14:45 UTC | Declined by customer 2026-11-09 15:30 UTC (not acceptable to auditors) |
| Asked CSM Owen Pryce to go through the service-level terms with the customer | Tom Reyes | By 2026-11-10 09:10 UTC | Result not recorded |
| Escalated to Tier 2 (Product Engineering Support) | Tom Reyes | 2026-11-10 14:20 UTC | Status Escalated, priority P2; Tier 2 result not recorded |

## Commitments to the customer
| Commitment (quoted) | Made by | When | Status |
|---|---|---|---|
| "I'm escalating the fault to our Product Engineering Support team today." | Tom Reyes | 2026-11-10 09:10 UTC | Met: escalated 2026-11-10 14:20 UTC |
| "I'll ask engineering whether a fix would recalculate invoices already issued. I can't promise that it will" | Tom Reyes | 2026-11-10 09:10 UTC | Met: question listed in the escalation note at 2026-11-10 14:20 UTC. Commitment was to ask only; no answer yet recorded |
| "I'll send you a written summary of what we've reproduced, including the sandbox example, by 17:00 UK time today (Tuesday 10 November)." | Tom Reyes | 2026-11-10 09:10 UTC | Open, due 2026-11-10 17:00 UTC; not sent as of the escalation note at 14:20 UTC ("haven't sent yet"). Customer asked again at 13:55 UTC that it arrive today |
| "I've asked your Customer Success Manager, Owen Pryce, to go through the service-level terms in your contract with you." | Tom Reyes | 2026-11-10 09:10 UTC | Open, no time given; no CSM contact recorded in the thread |

**Requested, not committed:**
- Confirmation that the fault will be fixed within 24 hours (Marta Kowalczyk, 2026-11-09 10:47 and 15:30). Tom Reyes declined to confirm contract terms (2026-11-10 09:10).
- The bug fixed (2026-11-09 15:30). Escalation was committed; a fix was not ("I can't give you a fix date").
- Correction of invoices already issued, or guidance on whether to raise a credit note for each (2026-11-09 15:30). Only asking engineering was committed.

## Service level
Measured at 2026-11-10 14:20 UTC (last entry in the thread). Readings used for ambiguous terms: "17:00 UK time" on 10 November (commitment, not policy) read as 17:00 UTC, since the UK is on GMT (UTC+0) in November; the thread states all timestamps are UTC.

| Target (policy quote) | Clock start | Deadline (arithmetic) | Status |
|---|---|---|---|
| First response: Not determinable: support policy not supplied | Not determinable: support policy not supplied | Not determinable: support policy not supplied | Not determinable |
| Update cadence: Not determinable: support policy not supplied | Not determinable: support policy not supplied | Not determinable: support policy not supplied | Not determinable |
| Resolution: Not determinable: support policy not supplied | Not determinable: support policy not supplied | Not determinable: support policy not supplied | Not determinable |

Thread timestamps available for these calculations once the policy is supplied: ticket created 2026-11-09 10:47 UTC; first support reply 2026-11-09 11:20 UTC; further customer-facing updates 2026-11-09 14:45 UTC and 2026-11-10 09:10 UTC; escalated 2026-11-10 14:20 UTC.

Pauses: Not determinable: support policy not supplied

## Recommended next action
Reproduce the sandbox example in NOK (3 lines of NOK 10.33 at 20% VAT, per-line rounding, same as Tom Reyes's EUR and GBP test), owner Tier 2 Product Engineering Support, by 2026-11-10 16:30 UTC, because it is a cheap test that separates "all non-base-currency invoices" (which would match the 8.2.4 release note Hypothesis and put all ~140 EUR and NOK invoices in scope) from "EUR only" (which the 29-invoice sample suggests), and the result should reach Tom Reyes before his written summary for the auditors falls due at 17:00 UTC today, ahead of the on-site audit on 12 November. Tom Reyes must send the summary by 17:00 UTC whether or not the result is in. (This recommendation is my own, drawn from the facts above.)
