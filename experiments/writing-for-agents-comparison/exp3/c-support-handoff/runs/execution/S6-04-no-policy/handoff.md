# Escalation handoff: QB-203977 Per-line VAT rounding not applied to some EUR invoices since 8.2.4

Reference time ("now"): 2026-11-10 14:20 UTC (last thread message)
Inputs missing: support policy (no policy document supplied; the account record says Enterprise terms are in "Master Services Agreement, Schedule 3", which is not in the case)

## Problem as currently understood
On an account set to per-line VAT rounding, some EUR invoices issued since 2 November show an invoice VAT total that differs by EUR 0.01 from the sum of the line VAT. Support reproduced it in the customer's sandbox, where the EUR invoice VAT total matched 20% of the rounded invoice net rather than the sum of line VAT; the same invoice in GBP was correct. No differences were found in the NOK or GBP samples. A link to release 8.2.4 (deployed 2 Nov) is a hypothesis only.
- Account VAT rounding is set to per line [verified] (account record; Tom Reyes internal note, 2026-11-09 14:30 UTC: "last changed 14 March 2026")
- Account base currency is GBP; invoice currencies enabled are GBP, EUR, NOK [verified] (account record)
- INV-LM-11402, INV-LM-11417 and INV-LM-11431 (all EUR) each have an invoice VAT total EUR 0.01 lower than the sum of line VAT [verified] (Tom Reyes internal note, 2026-11-09 14:30 UTC)
- Of 20 EUR invoices issued 2 to 9 Nov, 7 differ by EUR 0.01 (5 lower, 2 higher) and 13 match [verified] (Tom Reyes internal note, 2026-11-09 14:30 UTC)
- All 9 NOK invoices in the same period show no difference; 11 sampled GBP invoices show no difference [verified] (Tom Reyes internal note, 2026-11-09 14:30 UTC)
- Sandbox reproduction: EUR invoice, 3 lines of EUR 10.33 at 20% VAT; line VAT 2.07 each, sum 6.21; invoice VAT total 6.20 (20% of 30.99 rounded); same invoice in GBP gives 6.21 [verified] (Tom Reyes internal note, 2026-11-09 14:30 UTC)
- Per-line rounding is not applied to EUR invoices; the VAT total is calculated on the invoice total [suspected] (Tom Reyes internal note, 2026-11-09 14:30 UTC; Tom Reyes to customer, 2026-11-09 14:45 UTC)
- Fault is linked to release 8.2.4 (deployed 2 Nov; release note: "Improved currency conversion precision for non-base-currency invoices") [suspected] (Tom Reyes internal note, 2026-11-09 14:30 UTC: "Possible link; not confirmed")
- Problem began after "your update last week" [reported] (Marta Kowalczyk, 2026-11-09 10:47 UTC)
- About 140 invoices issued in EUR and NOK since 2 November [reported] (Marta Kowalczyk, 2026-11-09 10:47 UTC)
- Auditors require per-line VAT rounding; per-invoice rounding is not acceptable to them [reported] (Marta Kowalczyk, 2026-11-09 10:47 and 15:30 UTC)
- External audit on site 12 to 13 November 2026 [verified] (account record, noted by CSM); auditors in on Thursday [reported] (Marta Kowalczyk, 2026-11-10 13:55 UTC)
- Enterprise contract requires a fix within 24 hours [reported] (Marta Kowalczyk, 2026-11-09 10:47 UTC); not checked against the policy, which was not supplied

Conflicts:
- Scope: customer says "every multi-currency invoice we issue has the wrong VAT total" [reported] (Marta Kowalczyk, 2026-11-09 10:47 UTC); support found 7 of 20 EUR invoices differ and none of 9 NOK invoices [verified] (Tom Reyes internal note, 2026-11-09 14:30 UTC).
- Fix time: customer says the contract requires a fix within 24 hours [reported] (Marta Kowalczyk, 2026-11-09 10:47 UTC); support has not confirmed it and referred it to the CSM (Tom Reyes, 2026-11-10 09:10 UTC).

## Tried so far
| When | Who | What | Result |
|------|-----|------|--------|
| 2026-11-09 11:20 UTC | Tom Reyes (Tier 1) | Asked customer for example invoice numbers | Customer sent INV-LM-11402, INV-LM-11417, INV-LM-11431 (2026-11-09 12:05 UTC) |
| 2026-11-09 14:30 UTC | Tom Reyes | Checked account VAT rounding setting | "per line" on, last changed 14 March 2026 |
| 2026-11-09 14:30 UTC | Tom Reyes | Checked the three customer invoices | Each invoice VAT total EUR 0.01 below sum of line VAT |
| 2026-11-09 14:30 UTC | Tom Reyes | Sampled invoices issued 2 to 9 Nov: 20 EUR, all 9 NOK, 11 GBP | EUR: 7 differ by 0.01 (5 lower, 2 higher), 13 match; NOK: none differ; GBP: none differ |
| 2026-11-09 14:30 UTC | Tom Reyes | Reproduced in sandbox: EUR invoice, 3 lines of EUR 10.33 at 20%; same invoice in GBP | EUR VAT total 6.20 vs line sum 6.21; GBP VAT total 6.21 |
| 2026-11-09 14:30 UTC | Tom Reyes | In sandbox, switched rounding to "per invoice" and back to "per line" | No change for EUR |
| 2026-11-09 14:30 UTC | Tom Reyes | Read release notes for 8.2.4 (deployed 2 Nov) | Possible link; not confirmed |
| 2026-11-09 14:45 UTC | Tom Reyes | Offered workaround: switch to per-invoice rounding | Rejected by customer: not acceptable to auditors (2026-11-09 15:30 UTC) |

## Commitments to the customer
| When | Made by | Verbatim commitment | Status (met / pending / overdue) | Policy note |
|------|---------|---------------------|----------------------------------|-------------|
| 2026-11-10 09:10 UTC | Tom Reyes (Tier 1) | "I'm escalating the fault to our Product Engineering Support team today." | Met (escalated to Tier 2, 2026-11-10 14:20 UTC) | Policy not supplied |
| 2026-11-10 09:10 UTC | Tom Reyes (Tier 1) | "I'll ask engineering whether a fix would recalculate invoices already issued. I can't promise that it will, so please don't hold off on anything your auditors need." | Pending (listed as an open ask in the escalation note, 2026-11-10 14:20 UTC; no answer in the thread) | Policy not supplied |
| 2026-11-10 09:10 UTC | Tom Reyes (Tier 1) | "I'll send you a written summary of what we've reproduced, including the sandbox example, by 17:00 UK time today (Tuesday 10 November)." | Pending; due 17:00 UK time = 17:00 UTC (UK on GMT in November), 2 h 40 min remaining at now; escalation note says "haven't sent yet" | Policy not supplied |
| 2026-11-10 09:10 UTC | Tom Reyes (Tier 1) | "I've asked your Customer Success Manager, Owen Pryce, to go through the service-level terms in your contract with you." | Pending (no record in the thread of Owen Pryce contacting the customer) | Policy not supplied |

No fix date was promised: "I can't give you a fix date" (Tom Reyes, 2026-11-10 09:10 UTC). The 24-hour fix is the customer's claim, not a commitment: "I'm not able to confirm contract terms myself" (Tom Reyes, 2026-11-10 09:10 UTC).

## Service level
- Clause: none available; the policy was not supplied (account record: "Support level: Enterprise (terms in Master Services Agreement, Schedule 3)")
- Clock: resolution clock claimed by the customer ("required to fix this within 24 hours", Marta Kowalczyk, 2026-11-09 10:47 UTC) [reported]; business or calendar hours unknown; would start at ticket creation, 2026-11-09 10:47 UTC, priority P2
- Deadline: cannot compute from policy. If the customer's figure were calendar hours: 2026-11-09 10:47 + 24 h = 2026-11-10 10:47 UTC, passed at now; if business hours, the result depends on the undefined business day.
- Status: cannot determine; missing terms: the support policy (Enterprise Schedule 3 text), the clock that applies to P2, business vs calendar hours, and the business-hours definition and time zone
- First-response and update-interval clocks: cannot determine; missing terms: the support policy. For reference, ticket created 2026-11-09 10:47 UTC, first agent reply 2026-11-09 11:20 UTC (33 min).

## Open questions
- Will a fix recalculate invoices already issued, or must the customer raise a credit note for each one? (asked by Marta Kowalczyk, 2026-11-09 15:30 UTC; Tom Reyes to ask engineering, 2026-11-10 09:10 UTC)
- When will the bug be fixed? (asked by Marta Kowalczyk, 2026-11-09 15:30 UTC; Tom Reyes: "I can't give you a fix date", 2026-11-10 09:10 UTC)
- Confirm the 24-hour fix term under the Enterprise contract (asked by Marta Kowalczyk, 2026-11-09 10:47 and 15:30 UTC; referred to CSM Owen Pryce, 2026-11-10 09:10 UTC)
- Is the fault linked to release 8.2.4? (raised by Tom Reyes, internal note, 2026-11-09 14:30 UTC: "Possible link; not confirmed")

## Recommended next action
Send the customer the promised written summary of what was reproduced (three invoices, 7 of 20 EUR sample, no NOK or GBP differences, the sandbox EUR 10.33 x 3 example, per-line setting confirmed on), owner Tom Reyes (Tier 1), by 17:00 UTC 2026-11-10. Rests on: commitment of 2026-11-10 09:10 UTC (pending, "haven't sent yet" per escalation note 2026-11-10 14:20 UTC); customer request for written confirmation for auditors (2026-11-09 15:30 UTC) and "Please make sure the summary arrives today. Our auditors are in on Thursday." (2026-11-10 13:55 UTC); audit on site 12 to 13 November (account record); verified ledger entries from Tom Reyes internal note, 2026-11-09 14:30 UTC.
