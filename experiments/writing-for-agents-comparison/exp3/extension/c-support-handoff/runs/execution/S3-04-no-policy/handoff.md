Clarifying question: The support policy was not supplied, and the account record says the Enterprise terms are in "Master Services Agreement, Schedule 3", which is also not in the case. Can you supply the policy or Schedule 3 so the service-level clocks can be checked? Without an answer, this handoff proceeds without it and marks every policy term "not supplied".

# Escalation handoff: QB-203977 VAT totals wrong on multi-currency invoices since update

**Customer:** Lindqvist Marine Supplies Ltd, LMS-0855, plan Quillbill Trade (annual), support level Enterprise (account record)  **Priority:** P2 (ticket event 2026-11-09 10:47 UTC; unchanged at escalation 2026-11-10 14:20 UTC)  **Prepared:** 2026-11-21 18:28 UTC (environment clock)

Note: the thread export ("Export of the full ticket history") has no entries after 2026-11-10 14:20 UTC. Anything that happened since, including whether the promised summary was sent, is not recorded.

## Service level

| Clock | Policy clause | Started | Deadline | Status |
|---|---|---|---|---|
| First response | Not supplied (support policy and MSA Schedule 3 not in case) | 2026-11-09 10:47 UTC (ticket created) | Not stated | Cannot assess. First agent reply was 2026-11-09 11:20 UTC (Tom Reyes) |
| Update interval | Not supplied | Not stated | Not stated | Cannot assess. Last customer-visible support message: 2026-11-10 09:10 UTC |
| Resolution / fix | Not supplied. Customer's claim only (reported, 2026-11-09 10:47 UTC): "Under our Enterprise contract you are required to fix this within 24 hours." Support has not confirmed it (Tom Reyes, 2026-11-10 09:10 UTC: "I'm not able to confirm contract terms myself") | Reading A: ticket creation 2026-11-09 10:47 UTC. Reading B: escalation 2026-11-10 14:20 UTC | A: 2026-11-10 10:47 UTC. B: 2026-11-11 14:20 UTC | If the claim is right: A breached 11 d 7 h 41 m ago; B breached 10 d 4 h 8 m ago. Unverified |

Arithmetic: Reading A, 2026-11-09 10:47 UTC + 24 h = 2026-11-10 10:47 UTC; to 2026-11-21 18:28 UTC = 11 d 7 h 41 m. Reading B, 2026-11-10 14:20 UTC + 24 h = 2026-11-11 14:20 UTC; to 2026-11-21 18:28 UTC = 10 d 4 h 8 m.
Gaps: no policy, so no clock definitions, business-hours rules, holidays or pause conditions are known. Whether the 24-hour term exists, what it covers (fix, response or workaround) and when it starts are all not stated. The CSM (Owen Pryce) was asked to go through the terms with the customer; outcome not recorded.

## Problem as currently understood

Since release 8.2.4 (deployed 2 Nov), some EUR invoices on an account set to per-line VAT rounding show an invoice VAT total that differs by EUR 0.01 from the sum of line VAT. A sandbox reproduction showed the EUR VAT total matching VAT computed on the invoice net total (20% of 30.99 = 6.20) instead of the sum of rounded line VAT (6.21), while the same invoice in GBP was correct. NOK and GBP samples showed no differences; the link to 8.2.4 and the exact mechanism are suspected, not confirmed.

| Fact | Status | Evidence |
|---|---|---|
| Account setting "VAT rounding: per line" is on; last changed 14 March 2026 | Verified | Reported by Marta 2026-11-09 10:47 UTC; checked in account setting by Tom Reyes, internal note 2026-11-09 14:30 UTC; account record "VAT rounding per line" |
| INV-LM-11402, INV-LM-11417, INV-LM-11431 (all EUR): each invoice VAT total is EUR 0.01 lower than the sum of line VAT | Verified | Invoice numbers from Marta 2026-11-09 12:05 UTC; Tom checked each, internal note 2026-11-09 14:30 UTC ("Confirmed") |
| EUR invoices issued 2 to 9 Nov: 7 of 20 sampled differ by 0.01 (5 lower, 2 higher); 13 match | Verified (sample of 20) | Tom internal note 2026-11-09 14:30 UTC |
| NOK invoices issued 2 to 9 Nov: all 9 checked, none differ | Verified | Tom internal note 2026-11-09 14:30 UTC |
| GBP invoices: 11 sampled, none differ | Verified (sample of 11) | Tom internal note 2026-11-09 14:30 UTC |
| "every multi-currency invoice we issue has the wrong VAT total" | Reported; contradicted by the checks above for NOK and for 13 of 20 EUR | Marta 2026-11-09 10:47 UTC |
| About 140 invoices issued in EUR and NOK since 2 November | Reported | Marta 2026-11-09 10:47 UTC |
| Problem started "since your update last week" | Reported (no pre-2 Nov invoices checked) | Marta 2026-11-09 10:47 UTC |
| Release 8.2.4 deployed 2 Nov, release note: "Improved currency conversion precision for non-base-currency invoices." | Verified (release notes read) | Tom internal note 2026-11-09 14:30 UTC |
| Sandbox reproduction: new EUR invoice, 3 lines of EUR 10.33 at 20% VAT; line VAT 2.07 each, sum 6.21; invoice VAT total 6.20 (20% of 30.99 rounded). Same invoice in GBP: VAT total 6.21 | Verified (reproduced in customer's sandbox, a copy of production settings) | Tom internal note 2026-11-09 14:30 UTC; account record (sandbox refreshed monthly) |
| Switching sandbox rounding to "per invoice" and back to "per line" made no change for EUR | Verified | Tom internal note 2026-11-09 14:30 UTC |
| Per-line rounding is not applied to EUR invoices; VAT total is calculated on the invoice total | Suspected | Tom internal note 2026-11-09 14:30 UTC ("Looks like"); Tom to customer 2026-11-09 14:45 UTC ("seems to be") |
| Cause is the 8.2.4 currency conversion change | Suspected | Tom internal note 2026-11-09 14:30 UTC ("Possible link; not confirmed") |
| Customer's auditors require per-line VAT rounding; per-invoice rounding not acceptable | Reported | Marta 2026-11-09 10:47 UTC and 15:30 UTC |
| External audit on site 12 to 13 November 2026 | Verified (account record flag, noted by CSM) | Account record; Marta 2026-11-10 13:55 UTC ("auditors are in on Thursday"); escalation note 2026-11-10 14:20 UTC |
| Environment: Quillbill Invoicing (cloud), data region UK, base currency GBP, invoice currencies GBP, EUR, NOK, UK standard VAT rate | Verified (account record) | Account record |

Contradictions:
- Scope. Marta (2026-11-09 10:47 UTC): "every multi-currency invoice we issue has the wrong VAT total", and her count covers EUR and NOK. Tom's checks (internal note 2026-11-09 14:30 UTC): 7 of 20 EUR invoices differ, 13 match, and none of the 9 NOK invoices differ.
- Release scope vs observed scope. The 8.2.4 note covers "non-base-currency invoices" (Tom internal note 2026-11-09 14:30 UTC), which includes NOK, yet no NOK invoice was found affected (same note). Not a disagreement between sources, but unexplained.

## What has been tried

| When | Who | Action | Result |
|---|---|---|---|
| 2026-11-09 11:20 UTC | Tom Reyes (Tier 1) | Asked customer for two or three affected invoice numbers | Marta sent INV-LM-11402, INV-LM-11417, INV-LM-11431 (2026-11-09 12:05 UTC) |
| 2026-11-09 by 14:30 UTC | Tom Reyes | Checked account VAT rounding setting | Per line on; last changed 14 March 2026 |
| 2026-11-09 by 14:30 UTC | Tom Reyes | Checked the three invoices | Each invoice VAT total EUR 0.01 below sum of line VAT |
| 2026-11-09 by 14:30 UTC | Tom Reyes | Sampled invoices issued 2 to 9 Nov | EUR 7 of 20 differ (5 lower, 2 higher); NOK 0 of 9; GBP 0 of 11 |
| 2026-11-09 by 14:30 UTC | Tom Reyes | Reproduced in customer sandbox (3 x EUR 10.33 at 20%) and same invoice in GBP | EUR VAT total 6.20 vs line sum 6.21; GBP 6.21 |
| 2026-11-09 by 14:30 UTC | Tom Reyes | Switched sandbox rounding to per invoice and back to per line | No change for EUR |
| 2026-11-09 by 14:30 UTC | Tom Reyes | Read 8.2.4 release notes | Possible link to currency conversion change; not confirmed |
| 2026-11-09 14:45 UTC | Tom Reyes | Offered per-invoice rounding as workaround | Rejected by Marta 2026-11-09 15:30 UTC: "per-invoice rounding isn't acceptable to our auditors" |
| 2026-11-10 09:10 UTC | Tom Reyes | Asked CSM Owen Pryce to go through service-level terms with customer | Result not recorded |
| 2026-11-10 14:20 UTC | Tom Reyes | Escalated to Tier 2 (Product Engineering Support) | Status Open to Escalated, priority P2 |

## Commitments to the customer

| When | Made by | Commitment (quoted) | Due | State |
|---|---|---|---|---|
| 2026-11-10 09:10 UTC | Tom Reyes | "I'm escalating the fault to our Product Engineering Support team today." | 2026-11-10 | Met (escalated 2026-11-10 14:20 UTC) |
| 2026-11-10 09:10 UTC | Tom Reyes | "I'll ask engineering whether a fix would recalculate invoices already issued. I can't promise that it will, so please don't hold off on anything your auditors need." | Not stated | Open (question passed in escalation note; no answer recorded) |
| 2026-11-10 09:10 UTC | Tom Reyes | "I'll send you a written summary of what we've reproduced, including the sandbox example, by 17:00 UK time today (Tuesday 10 November)." | 2026-11-10 17:00 GMT (17:00 UTC) | Overdue by 11 d 1 h 28 m as far as the record shows. Escalation note 2026-11-10 14:20 UTC: "haven't sent yet"; no later entry. Marta 2026-11-10 13:55 UTC: "Please make sure the summary arrives today." |
| 2026-11-10 09:10 UTC | Tom Reyes | "I've asked your Customer Success Manager, Owen Pryce, to go through the service-level terms in your contract with you." | Not stated | Open (no contact recorded) |

Not commitments: Tom said "I can't give you a fix date" (2026-11-10 09:10 UTC). No fix, credit or 24-hour term has been promised; the 24-hour term is the customer's claim only.

## Recommended next action

Test the suspected 8.2.4 cause directly in the customer's sandbox: create the same invoice (3 lines of 10.33 at 20% VAT, per-line rounding) in EUR, NOK and GBP, and compare the invoice VAT total with the sum of line VAT in each; then read the 8.2.4 change to the non-base-currency path to see whether the invoice VAT total is now computed from the converted net total rather than summed from rounded line VAT. Confirms the cause: EUR gives 6.20 while GBP gives 6.21, NOK shows the same fault on an equivalent example, and the 8.2.4 code path recomputes VAT on the total for non-base currencies; a sample of EUR invoices issued before 2 Nov with no differences would support the release link. Rules it out: NOK and EUR behave differently on the same path, or pre-2 Nov EUR invoices show the same differences. The result also answers the open commitment on whether a fix would recalculate issued invoices.

This races the overdue written summary (due 2026-11-10 17:00 UTC, not recorded as sent): before starting, confirm with Tom Reyes whether it went out, and if not, have it sent now, since it needs only the already-verified findings. The customer's 24-hour fix claim, if valid, is already breached under either reading.

Open questions:
- Was the written summary for the auditors sent after 2026-11-10 14:20 UTC? The audit (12 to 13 Nov) has now passed.
- What does MSA Schedule 3 say about service levels for Enterprise P2, and did Owen Pryce speak to the customer?
- Why are NOK invoices unaffected when the 8.2.4 note covers all non-base-currency invoices? Was the NOK sample (9) large enough?
- Were EUR invoices before 2 Nov correct? Not checked.
- How many of the roughly 140 EUR and NOK invoices since 2 Nov are affected? Only 20 EUR and 9 NOK were checked.
- Will a fix recalculate invoices already issued, or must the customer raise credit notes? (Customer ask, 2026-11-09 15:30 UTC.)
- Is the sandbox running the same release as production? Not stated.
