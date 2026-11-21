Clarifying question: The support policy / service levels are not among the three sources supplied (only the ticket thread and account record). The account record says the Enterprise terms are in "Master Services Agreement, Schedule 3". Please supply Schedule 3 (or the support policy). Continuing without it; all service-level terms are recorded as Not determinable.

# Escalation handoff: QB-203977 Per-line VAT rounding not applied to some EUR invoices since release 8.2.4

**Customer:** Lindqvist Marine Supplies Ltd, account LMS-0855, Quillbill Trade (annual), support level Enterprise (account record: "Enterprise (terms in Master Services Agreement, Schedule 3)")   **Severity/priority:** Priority P2 (thread, ticket created 2026-11-09 10:47 UTC and Tier 2 escalation 2026-11-10 14:20 UTC). Severity: Not determinable (policy not supplied, so P2's meaning and any severity mapping are unknown).
**Most urgent deadline:** Written summary promised to the customer by 17:00 UK time Tue 10 Nov 2026 (= 17:00 UTC, UK on GMT), 2h40m after the as-of time of 14:20 UTC; not yet sent (Tom Reyes, 09:10 UTC message; escalation note 14:20 UTC). Customer's auditors are on site Thu 12 Nov (escalation note; account flag "External audit on site 12 to 13 November 2026").

## Problem as currently understood
Since release 8.2.4 (deployed 2 Nov), some EUR invoices show an invoice VAT total EUR 0.01 different from the sum of line VAT, although the account is set to per-line VAT rounding. It is reproduced in the customer's sandbox; NOK and GBP samples showed no differences. The cause is not confirmed; the 8.2.4 link is only a hypothesis. The customer cannot use per-invoice rounding (auditors) and needs a fix, a decision on already-issued invoices, and a written summary before the audit.

| Fact | Status | How established / cite |
|---|---|---|
| Account setting "VAT rounding: per line" is on, last changed 14 March 2026 | Verified | Tom Reyes internal note 2026-11-09 14:30 UTC (read from account settings); account record "VAT rounding per line" |
| INV-LM-11402, INV-LM-11417, INV-LM-11431 (EUR) each have invoice VAT total EUR 0.01 lower than the sum of line VAT | Verified | Tom Reyes internal note 2026-11-09 14:30 UTC ("Confirmed") |
| Of 20 EUR invoices sampled (issued 2 to 9 Nov), 7 differ by 0.01 (5 lower, 2 higher), 13 match | Verified | Tom Reyes internal note 2026-11-09 14:30 UTC. Sampling method and total EUR invoice count not recorded |
| 0 of 9 NOK invoices (2 to 9 Nov) and 0 of 11 GBP invoices sampled differ | Verified | Tom Reyes internal note 2026-11-09 14:30 UTC |
| Sandbox repro: new EUR invoice, 3 lines of EUR 10.33 at 20% VAT, line VAT 2.07 each (sum 6.21), invoice VAT total 6.20 (20% of 30.99 rounded); same invoice in GBP gives 6.21 | Verified (in sandbox only) | Tom Reyes internal note 2026-11-09 14:30 UTC. Sandbox is a "copy of production settings, refreshed monthly" (account record) |
| Switching sandbox rounding to "per invoice" and back to "per line" made no change for EUR | Verified (in sandbox only) | Tom Reyes internal note 2026-11-09 14:30 UTC |
| Per-line rounding is not applied to EUR invoices / VAT total is calculated on the invoice total | Hypothesis | Tom Reyes internal note 14:30 UTC ("Looks like"); Tom's customer message 14:45 UTC ("seems to be") |
| Release 8.2.4 (deployed 2 Nov) caused it | Hypothesis | Tom Reyes internal note 14:30 UTC: release note "Improved currency conversion precision for non-base-currency invoices"; "Possible link; not confirmed" |
| The 8.2.4 deployment date is 2 Nov | Reported (by release notes quoted in the note; not independently checked in the thread) | Tom Reyes internal note 14:30 UTC |
| Problem began after "your update last week" / since 2 Nov | Reported | Marta Kowalczyk 2026-11-09 10:47 UTC |
| "Every multi-currency invoice we issue has the wrong VAT total" | Reported (contradicted in part, see disagreements) | Marta Kowalczyk 2026-11-09 10:47 UTC |
| About 140 invoices in EUR and NOK issued since 2 Nov | Reported | Marta Kowalczyk 2026-11-09 10:47 UTC |
| Auditors require VAT rounded line by line; per-invoice rounding not acceptable | Reported | Marta Kowalczyk 10:47 UTC and 15:30 UTC (2026-11-09) |
| Auditors are in on Thursday (12 Nov) | Reported (customer, 2026-11-10 13:55 UTC; Tom's note 14:20 UTC repeats it). Account flag "External audit on site 12 to 13 November 2026" is a CSM note | Marta Kowalczyk 13:55 UTC; account record flags |
| Customer has no confidence in any issued invoice | Reported | Marta Kowalczyk 2026-11-09 10:47 UTC |
| Contract requires a fix within 24 hours | Reported | Marta Kowalczyk 2026-11-09 10:47 UTC; not checked against the contract (policy not supplied) |

**Open disagreements:** (1) Customer says "every multi-currency invoice" is wrong; support found only 7 of 20 sampled EUR invoices differ and none of 9 NOK (Marta 10:47 UTC 2026-11-09 vs Tom note 14:30 UTC). (2) Customer says the fix is owed within 24 hours under the contract; support has not confirmed the term (Tom 2026-11-10 09:10 UTC: "I'm not able to confirm contract terms myself"). (3) Tom's cause statement to the customer is stated more firmly than the evidence (see hypotheses).

## What has been tried
| When | Who | Action | Result | Cite |
|---|---|---|---|---|
| 2026-11-09 11:20 UTC | Tom Reyes | Asked customer for 2 to 3 example invoice numbers | Customer supplied three at 12:05 UTC | Thread 11:20, 12:05 |
| 2026-11-09 14:30 UTC | Tom Reyes | Checked account rounding setting | "per line" on, changed 14 March 2026 | Internal note 14:30 |
| 2026-11-09 14:30 UTC | Tom Reyes | Checked the three invoices | Each VAT total EUR 0.01 below line sum | Internal note 14:30 |
| 2026-11-09 14:30 UTC | Tom Reyes | Sampled 20 EUR, 9 NOK, 11 GBP invoices | 7/20 EUR differ; NOK and GBP none | Internal note 14:30 |
| 2026-11-09 14:30 UTC | Tom Reyes | Reproduced in sandbox (3 x EUR 10.33 at 20%) | EUR 6.20 vs expected 6.21; GBP 6.21 | Internal note 14:30 |
| 2026-11-09 14:30 UTC | Tom Reyes | Toggled sandbox rounding to per invoice and back | No change for EUR | Internal note 14:30 |
| 2026-11-09 14:30 UTC | Tom Reyes | Read release notes for 8.2.4 | Possible link, not confirmed | Internal note 14:30 |
| 2026-11-09 14:45 UTC | Tom Reyes | Sent customer findings and mentioned per-invoice workaround | Customer rejected the workaround at 15:30 UTC | Thread 14:45, 15:30 |
| 2026-11-10 09:10 UTC | Tom Reyes | Said he asked CSM Owen Pryce to go through service-level terms with the customer | Result not recorded | Thread 09:10 |
| 2026-11-10 14:20 UTC | Tom Reyes | Escalated to Tier 2 | Status Escalated, P2 | Thread 14:20 |
| 2026-11-10 09:10 UTC | Tom Reyes | Said he would ask engineering whether a fix recalculates issued invoices | Result not recorded | Thread 09:10 |

## Commitments to the customer
| Commitment (verbatim) | Made by (role) | When / cite | Deadline | Kept / Open / Missed |
|---|---|---|---|---|
| "I'm escalating the fault to our Product Engineering Support team today." | Tom Reyes (Tier 1 Support Agent) | 2026-11-10 09:10 UTC, thread | Today, 10 Nov | Kept (escalated 2026-11-10 14:20 UTC) |
| "I'll ask engineering whether a fix would recalculate invoices already issued." | Tom Reyes (Tier 1) | 2026-11-10 09:10 UTC, thread | None stated | Open (answer owed to customer; auditors Thu 12 Nov) |
| "I'll send you a written summary of what we've reproduced, including the sandbox example, by 17:00 UK time today (Tuesday 10 November)." | Tom Reyes (Tier 1) | 2026-11-10 09:10 UTC, thread | 17:00 UK time 10 Nov = 17:00 UTC | Open (not sent as of 14:20 UTC, 2h40m left) |
| "I've asked your Customer Success Manager, Owen Pryce, to go through the service-level terms in your contract with you." | Tom Reyes (Tier 1) | 2026-11-10 09:10 UTC, thread | None stated | Open (no evidence in thread that Owen has contacted the customer; the customer's 13:55 UTC reply does not mention it) |

Not commitments: "Could you send me..." (11:20), "I can't give you a fix date", "I can't promise that it will", and "I'm not able to confirm contract terms myself". Message of 2026-11-09 11:20 UTC ("I've started looking at this") promises nothing. The 24-hour fix is the customer's demand and has not been confirmed by support. No policy was supplied, so no check against what Tom is permitted to promise could be made.

## Service-level status
| Clock | Policy clause (quoted) | Started | Deadline (with arithmetic) | Status |
|---|---|---|---|---|
| First response | Not determinable: policy not supplied (account points to "Master Services Agreement, Schedule 3") | Ticket created 2026-11-09 10:47 UTC; first support reply 2026-11-09 11:20 UTC (33 min later) | Not determinable (term missing) | Not determinable |
| Update interval | Not determinable: policy not supplied | Not determinable | Not determinable | Not determinable |
| Resolution / fix | Customer's claim only (Reported): "required to fix this within 24 hours" (Marta 2026-11-09 10:47 UTC). No policy quote | Ticket created 2026-11-09 10:47 UTC (if clock starts at creation) | Conditional, if the claim is correct and runs from creation with no pause or business-hours rule: 2026-11-09 10:47 + 24h = 2026-11-10 10:47 UTC | Conditional: would be breached at the as-of time (14:20 UTC is 3h33m past). Not confirmed; also unknown whether it applies to P2, to a fix or a workaround, or whether business hours count |

Tier: Enterprise (account record). Priority P2; severity Not determinable. Missing input: the text of Schedule 3. With it, each clock can be given a deadline and status; priority-dependent values should be shown as conditional.

## Recommended next action
Tier 2 should (a) confirm in production, not only in the sandbox, the failing EUR calculation and check whether 8.2.4's currency-conversion change touches per-line VAT rounding for EUR invoices (the sandbox repro with 3 x EUR 10.33 at 20% is the test case; the per-invoice toggle did not change EUR), and (b) in the same step, check why 13 of 20 EUR invoices are correct and 2 of the 7 differ upward, and check whether the 9 NOK invoices were genuinely unaffected. The result would settle whether the cause is 8.2.4 (currently Hypothesis), whether the fault is in EUR only, and whether issued invoices can be listed and recalculated. Deadline it must beat: the 17:00 UTC (17:00 UK) written summary today. Supplying the summary needs only the verified facts above; keep causes marked as unconfirmed and do not state a fix date. Also answer the open question whether a fix recalculates issued invoices before the audit on Thu 12 Nov.

## Gaps
- Support policy / service levels missing (MSA Schedule 3 not supplied): all service-level clauses, severity mapping, the 24-hour claim, and limits on what Tier 1 may promise are Not determinable. Close by supplying Schedule 3.
- Result of Tom's request to Owen Pryce (CSM) not recorded; whether Owen has contacted the customer is unknown.
- Result of the question to engineering about recalculating issued invoices not recorded.
- Written summary to the customer not yet sent as of 14:20 UTC.
- Sample method, total number of EUR invoices issued since 2 Nov, and which invoices differ (beyond the three named) not recorded.
- Cause unconfirmed; the 8.2.4 link and "calculated on invoice total" explanation are hypotheses.
- Whether the sandbox reproduces production behaviour is assumed from the three production invoices; no production reproduction recorded.
- Whether credit notes or credits are offered: none promised; account record shows "Open credits: None".
