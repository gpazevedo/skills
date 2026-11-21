# Escalation handoff: QB-203977 VAT totals wrong on multi-currency invoices since update

**Customer:** Lindqvist Marine Supplies Ltd, LMS-0855, Quillbill Trade (annual), Support level: Enterprise (MSA Schedule 3)  **Priority:** P2 (ticket header, 2026-11-09 10:47 and 2026-11-10 14:20)  **Prepared:** 2026-11-10 14:20 UTC (14:20 UK, GMT), the as-of time of the export

## Service level
| Clock | Policy clause | Started | Deadline | Status |
|---|---|---|---|---|
| Any Enterprise/P2 clock (first response, update, resolution) | Not supplied. Account record says terms are in "Master Services Agreement, Schedule 3"; no policy or Schedule 3 text was provided | Ticket created 2026-11-09 10:47 UTC | Not stated | Cannot be determined |

Gap: no support policy was supplied, so no clause is quoted and no deadline or breach status is computed. The only 24-hour term in the case is the customer's own statement (Marta, 2026-11-09 10:47: "Under our Enterprise contract you are required to fix this within 24 hours"), which is reported and unverified. Tom (2026-11-10 09:10) said he cannot confirm contract terms and has asked CSM Owen Pryce to go through them with the customer. For reference only, if her 24 hours were a resolution clock from creation, it would have run out at 2026-11-10 10:47 UTC, 3h33m before the as-of time. That reading is unconfirmed. The needed input is Schedule 3 and the priority definitions.

## Problem as currently understood
Since release 8.2.4 (deployed 2 Nov), some EUR invoices show an invoice VAT total that differs by EUR 0.01 from the sum of the line VAT. In the sandbox, which copies production settings, the EUR invoice's total VAT appears to be computed on the invoice total instead of per line, even with "VAT rounding: per line" on. GBP does not show it and no NOK difference was found in the sample. The link to 8.2.4 is a suspicion, not confirmed. The customer's auditors are on site Thursday 12 Nov and she needs a written summary today.

| Fact | Status | Evidence |
|---|---|---|
| Account setting "VAT rounding: per line" is on, last changed 14 March 2026 | Verified | Tom internal note 2026-11-09 14:30 (read in account settings) |
| INV-LM-11402, 11417, 11431 (EUR): invoice VAT total is EUR 0.01 lower than sum of line VAT | Verified | Tom internal note 14:30, "Confirmed"; customer gave the numbers 12:05 |
| Of 20 EUR invoices issued 2 to 9 Nov, 7 differ by 0.01 (5 lower, 2 higher), 13 match | Verified (sample of 20 only) | Tom internal note 14:30 |
| 9 NOK invoices in the same period: none differ; 11 GBP invoices sampled: none differ | Verified (samples only) | Tom internal note 14:30 |
| Reproduced in sandbox: 3 lines of EUR 10.33 at 20% VAT gives line VAT 2.07 each (sum 6.21), invoice VAT 6.20 (20% of 30.99); same invoice in GBP gives 6.21 | Verified | Tom internal note 14:30, sandbox reproduction |
| In sandbox, switching to "per invoice" and back to "per line" did not change EUR behaviour | Verified (sandbox) | Tom internal note 14:30 |
| Invoice VAT is calculated on the invoice total, not per line, on EUR invoices | Verified in sandbox example; Suspected as the general cause | Tom 14:30 ("Looks like per-line rounding isn't applied to EUR invoices"); Tom to customer 14:45 ("seems to be") |
| Cause is release 8.2.4 (deployed 2 Nov; note: "Improved currency conversion precision for non-base-currency invoices") | Suspected | Tom 14:30, "Possible link; not confirmed" |
| Every multi-currency invoice is wrong | Reported, contradicted by sample (see below) | Marta 2026-11-09 10:47 |
| About 140 invoices in EUR and NOK issued since 2 Nov, none trusted | Reported (count not checked) | Marta 10:47 |
| Started with "your update last week" | Reported; matches 8.2.4 date but start of the fault not independently checked | Marta 10:47; Tom 14:30 release note |
| Per-invoice rounding is unacceptable to the auditors | Reported (twice) | Marta 10:47, 15:30; Tom 14:45 and the escalation note accept it |
| Auditors on site Thursday 12 Nov | Reported by customer; also recorded in account flag as 12 to 13 Nov | Marta 2026-11-10 13:55; account record flags |

Contradictions:
- Scope. Marta: "every multi-currency invoice we issue has the wrong VAT total" (10:47). Tom's sample: 7 of 20 EUR invoices affected, none of 9 NOK and none of 11 GBP (14:30). Both kept; the sample is small and NOK was not verified as affected.
- Sandbox vs production. Tom's explanation of the mechanism (14:45) rests on the sandbox reproduction; production invoices were only checked for the 0.01 difference, not for how the figure was computed. Not a direct disagreement, but the mechanism is unverified in production.
- Tom's note says the bug is "per-line rounding isn't applied to EUR invoices", but 13 of 20 sampled EUR invoices were correct; the pattern for which invoices fail is not explained.
- Audit dates: Marta says "Thursday" (12 Nov); account flag says 12 to 13 Nov. Consistent, noted for completeness.

## What has been tried
| When | Who | Action | Result |
|---|---|---|---|
| 2026-11-09 11:20 | Tom Reyes | Asked customer for 2 or 3 invoice numbers | Customer gave three at 12:05 |
| 2026-11-09 14:30 | Tom Reyes | Checked the account VAT rounding setting | "per line" on, last changed 14 March 2026 |
| 2026-11-09 14:30 | Tom Reyes | Checked the three invoices | Each invoice VAT total EUR 0.01 lower than line sum |
| 2026-11-09 14:30 | Tom Reyes | Sampled 20 EUR, 9 NOK, 11 GBP invoices | 7 EUR differ; NOK and GBP none |
| 2026-11-09 14:30 | Tom Reyes | Reproduced in customer sandbox (3 x EUR 10.33 at 20%) | EUR 6.20 against line sum 6.21; GBP 6.21 |
| 2026-11-09 14:30 | Tom Reyes | In sandbox, toggled rounding to "per invoice" and back to "per line" | No change for EUR |
| 2026-11-09 14:30 | Tom Reyes | Read 8.2.4 release notes | Possible link, not confirmed |
| 2026-11-09 14:45 | Tom Reyes | Offered per-invoice rounding workaround | Customer refused (auditors), 15:30 |
| 2026-11-10 09:10 | Tom Reyes | Asked CSM Owen Pryce to go through the service-level terms with the customer | Result not recorded |
| 2026-11-10 14:20 | Tom Reyes | Escalated to Tier 2 | Status Escalated, P2 |

## Commitments to the customer
| When | Made by | Commitment (quoted) | Due | State |
|---|---|---|---|---|
| 2026-11-10 09:10 | Tom Reyes | "I'll send you a written summary of what we've reproduced, including the sandbox example, by 17:00 UK time today (Tuesday 10 November)." | 2026-11-10 17:00 UK = 17:00 UTC (GMT in November), 2h40m after the as-of time | Open; escalation note (14:20) says "haven't sent yet". Customer reconfirmed need (13:55): "Please make sure the summary arrives today." |
| 2026-11-10 09:10 | Tom Reyes | "I'm escalating the fault to our Product Engineering Support team today." | 2026-11-10 | Met, escalated 14:20 |
| 2026-11-10 09:10 | Tom Reyes | "I'll ask engineering whether a fix would recalculate invoices already issued." | No time stated | Open; he also said "I can't promise that it will" |
| 2026-11-10 09:10 | Tom Reyes | "I've asked your Customer Success Manager, Owen Pryce, to go through the service-level terms in your contract with you." | No time stated | Open; outcome not recorded |

No fix date, no confirmation of the 24 hours, and no credit have been promised ("I can't give you a fix date"; open credits: None). Account record contains no contract promise relating to this issue.

## Recommended next action
Determine what separates the 7 failing EUR invoices from the 13 correct ones and from NOK and GBP, and test the suspected 8.2.4 cause. In the sandbox, rerun the 3 x EUR 10.33 at 20% example (expected line sum 6.21; currently 6.20), then trace how invoice VAT is computed for non-base-currency invoices in 8.2.4 (the "currency conversion precision" change) against 8.2.3, using the line data of INV-LM-11402, 11417, 11431 and a few of the 13 matching EUR invoices. Confirmed if the failing invoices are exactly those where rounding the whole-invoice VAT differs from the per-line sum and the 8.2.3 path gives line-sum totals. Ruled out if the 8.2.3 path gives the same 6.20, or if matching invoices go through the same code path. Also check whether NOK invoices can be affected (the customer reports NOK among the 140). Racing: the written summary for the customer due 17:00 UTC today (2h40m left) and the auditors on site 12 Nov. The summary can state only the verified items above, labelling the 8.2.4 link as unconfirmed.

Open questions:
- Schedule 3 terms and priority definitions for Enterprise, so the 24-hour claim can be checked and a clock calculated. Who owns the response, Tier 2 or CSM Owen Pryce?
- Who sends the 17:00 summary: Tom, or Tier 2? It must go today.
- Will a fix recalculate the roughly 140 issued invoices, or must the customer raise credit notes? Is the customer's count of 140 (EUR and NOK) correct, and how many are actually affected?
- Does the fault occur in production for the same reason as in the sandbox?
- Any per-line workaround other than "per invoice" rounding acceptable to the customer?
