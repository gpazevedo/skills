# Escalation handoff: QB-203977, Lindqvist Marine Supplies Ltd (LMS-0855)

**In one line:** Since release 8.2.4 (2 Nov), some EUR invoices show an invoice VAT total that differs by EUR 0.01 from the sum of line VAT despite per-line rounding; the written summary promised to the customer is due at 17:00 UK time (17:00 UTC) today, 10 Nov, 2h40m from now, and the customer's auditors are on site Thursday 12 Nov.

## Problem as currently understood
- [verified] Account setting "VAT rounding: per line" is on, last changed 14 March 2026 (evidence: Tom Reyes inspected the account setting, internal note 2026-11-09 14:30 UTC; account record also lists VAT rounding per line)
- [verified] The three customer-named invoices INV-LM-11402, INV-LM-11417, INV-LM-11431 (EUR) each have an invoice VAT total EUR 0.01 lower than the sum of line VAT (evidence: Tom Reyes checked the invoices, internal note 2026-11-09 14:30 UTC)
- [verified] In a sample of 20 EUR invoices issued 2 to 9 Nov, 7 differ by EUR 0.01 (5 lower, 2 higher) and 13 match; 9 of 9 NOK invoices and 11 of 11 sampled GBP invoices show no difference (evidence: Tom Reyes sample, internal note 2026-11-09 14:30 UTC). Samples only; not the full population.
- [verified] Reproduced in the customer's sandbox (copy of production settings): new EUR invoice, 3 lines of EUR 10.33 at 20% VAT; line VAT 2.07 each, sum 6.21, invoice VAT total shows 6.20 (20% of 30.99 rounded). The same invoice in GBP shows 6.21 (evidence: Tom Reyes, 2026-11-09 14:30 UTC)
- [verified] In the sandbox, switching rounding to "per invoice" and back to "per line" made no change for EUR (evidence: Tom Reyes, 2026-11-09 14:30 UTC). Consequence: the per-invoice workaround Tom described to the customer would not have fixed EUR invoices anyway; the customer rejected it on audit grounds regardless.
- [verified] Release notes for 8.2.4, deployed 2 Nov, say "Improved currency conversion precision for non-base-currency invoices" (evidence: Tom Reyes read the release notes, 2026-11-09 14:30 UTC). That this change causes the fault is not established.
- [suspected] EUR VAT total is computed on the invoice total rather than line by line, ignoring the per-line setting (held by: Tom Reyes; basis: sandbox example matches the invoice-total calculation; he wrote "looks like" and "seems to be")
- [suspected] Release 8.2.4's currency conversion change caused it (held by: Tom Reyes; basis: timing; he wrote "Possible link; not confirmed")
- [reported] Every multi-currency invoice since the update has the wrong VAT total (source: Marta Kowalczyk, 2026-11-09 10:47). Support's sample contradicts "every": 13 of 20 EUR and 0 of 9 NOK sampled were correct.
- [reported] About 140 invoices in EUR and NOK issued since 2 Nov (source: Marta Kowalczyk, 2026-11-09 10:47). Support has not counted them.
- [reported] The customer's auditors require per-line VAT rounding; per-invoice is not acceptable (source: Marta Kowalczyk, 2026-11-09 10:47 and 15:30). Auditors are in on Thursday (2026-11-10 13:55); the account record also flags the on-site audit as 12 to 13 November 2026 (noted by CSM).
- Conflicts: customer says all multi-currency invoices are wrong; support's samples show EUR partly affected and NOK and GBP unaffected. Customer says the 24-hour fix is required under the Enterprise contract; the contract terms are not supplied (see Service level). Otherwise the account record (Enterprise, UK region, GBP base, EUR/NOK/GBP enabled) is consistent with the thread.

## Tried so far
| What was tried | Who, when | Result |
|---|---|---|
| Asked customer for example invoice numbers | Tom Reyes, 2026-11-09 11:20 | Customer sent three EUR invoice numbers at 12:05 |
| Checked the three invoices | Tom Reyes, 2026-11-09 14:30 | Each is EUR 0.01 lower than line VAT sum |
| Sampled 20 EUR, 9 NOK, 11 GBP invoices from 2 to 9 Nov | Tom Reyes, 2026-11-09 14:30 | 7 of 20 EUR differ; none of NOK or GBP |
| Reproduced in customer sandbox | Tom Reyes, 2026-11-09 14:30 | Reproduced on EUR; GBP correct |
| Toggled sandbox rounding to per invoice and back to per line | Tom Reyes, 2026-11-09 14:30 | No change for EUR |
| Checked release notes for 8.2.4 | Tom Reyes, 2026-11-09 14:30 | Currency conversion precision change; link unconfirmed |
| Offered per-invoice rounding as a workaround | Tom Reyes, 2026-11-09 14:45 | Customer rejected it (auditors); it also did not change EUR in the sandbox |
| Asked CSM Owen Pryce to take the customer through the service-level terms | Tom Reyes, 2026-11-10 09:10 | No result recorded |
| Escalated to Product Engineering Support | Tom Reyes, 2026-11-10 14:20 | Done; this handoff |

## Commitments to the customer
| Commitment (quoted) | Made by | When | Due | Status |
|---|---|---|---|---|
| "I'm escalating the fault to our Product Engineering Support team today." | Tom Reyes (Tier 1) | 2026-11-10 09:10 | 2026-11-10 | met (escalated 14:20 UTC) |
| "I'll ask engineering whether a fix would recalculate invoices already issued." | Tom Reyes | 2026-11-10 09:10 | no date given | pending (answer not yet sought; first question for you) |
| "I'll send you a written summary of what we've reproduced, including the sandbox example, by 17:00 UK time today (Tuesday 10 November)." | Tom Reyes | 2026-11-10 09:10 | 2026-11-10 17:00 UK time = 17:00 UTC (UK is on GMT in November) | pending, not yet sent, 2h40m remaining at 14:20 UTC |

Not commitments: Tom's "I can't give you a fix date" and "I can't promise that it will"; Tom declined to confirm the 24 hours. Customer requests (24-hour fix, whether issued invoices are corrected) are claims, not commitments.

## Service level
- Tier: Enterprise (account record: "Support level: Enterprise (terms in Master Services Agreement, Schedule 3)")
- Priority/severity: P2 (ticket event 2026-11-09 10:47; unchanged at escalation)
- Target: not stated in the support policy (no support policy was supplied) and not stated in the account record, which only points to MSA Schedule 3, also not supplied. The customer's "required to fix this within 24 hours" (2026-11-09 10:47) is reported only; support has not confirmed it.
- Clock rule: not stated in the support policy (not supplied)
- Deadline: not determinable. For reference only, if the customer's 24 hours ran from ticket creation (2026-11-09 10:47 UTC), it would have fallen at 2026-11-10 10:47 UTC, 3h33m before the as-of time. That is arithmetic on an unconfirmed claim, with no pause rules known (the status-history data was also not given beyond New, Open, Escalated).
- Status: unknown for any contractual target. As of 2026-11-10 14:20 UTC (the export's as-of time, used as now): the only dated commitment, the 17:00 UTC written summary, is open with 2h40m remaining.

## Recommended next action
1. Send the customer the promised written summary before 17:00 UTC today (one-time update, then no further date promises). Use only the verified items above: three invoices, the 7/20 EUR sample, no NOK or GBP differences in samples, the sandbox example (3 x 10.33 at 20%: 6.21 vs 6.20), and the setting being per line. Label the cause as under investigation; do not state the 8.2.4 link or the root cause as fact. Correct the earlier impression: the per-invoice workaround would not have fixed EUR in the sandbox.
2. Engineering check to start with: reproduce the sandbox invoice on the build before 8.2.4 (or with the 8.2.4 EUR conversion change disabled) and compare. Outcomes: if the pre-8.2.4 build gives 6.21, 8.2.4 is the cause (turn the suspicion into verified; look at the EUR conversion path). If it also gives 6.20, the cause is older or elsewhere (rule out 8.2.4; check why the per-line setting is skipped for EUR only). Also compute for the 13 matching EUR invoices whether per-line and per-total rounding happen to agree; if so, that supports the invoice-total theory.
3. In parallel, ask engineering the customer's question: would a fix recalculate issued invoices, and count affected invoices across all EUR and NOK invoices since 2 Nov (the customer's ~140 is unverified, and NOK in the customer's list is unconfirmed).
4. Ask Owen Pryce to confirm that he has covered the contract terms with the customer, and to supply Schedule 3 or the policy so the 24-hour claim can be checked.

## Gaps
- Support policy not supplied; MSA Schedule 3 not supplied. No response targets, clock rules or priority definitions are known.
- Whether Owen Pryce has contacted the customer is not recorded.
- Written summary not yet sent.
- Only samples were checked (20 EUR, 9 NOK, 11 GBP), not all ~140; full affected count unknown.
- Root cause and 8.2.4 link unchecked; no pre-8.2.4 comparison done.
- Sandbox was refreshed monthly from production; the production settings were checked only by reading the account setting, not by reproducing on a production invoice.
