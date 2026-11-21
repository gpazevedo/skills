Clarifying question: The support policy and its service levels (Enterprise terms, MSA Schedule 3) were not supplied. Can you provide it? Without it, every service-level term is "Not determinable: support policy not supplied". The account record names Schedule 3 but does not reproduce it. I have gone ahead without an answer.

# Escalation handoff: QB-203977 Per-line VAT rounding not applied to some EUR invoices since 8.2.4

**Customer:** Lindqvist Marine Supplies Ltd (LMS-0855), Quillbill Trade annual, Enterprise support level (account record) | **Priority:** P2 (set at ticket creation from email; thread does not say who set it)
**Service level:** Not determinable: support policy not supplied. Next deadline known from the thread is the written-summary commitment, 2026-11-10 17:00 UTC (2h40m remaining at 14:20 UTC)
**Open commitments:** 3, earliest due 2026-11-10 17:00 UTC (the other two have no stated time)

## Problem as currently understood
Since release 8.2.4 (2 Nov), some EUR invoices show an invoice VAT total EUR 0.01 different from the sum of line VAT, although the account is set to per-line VAT rounding (Verified by Tom Reyes). A sandbox reproduction (3 lines of EUR 10.33 at 20%) gives line VAT sum 6.21 but invoice total 6.20; the same invoice in GBP gives 6.21 (Verified by Tom Reyes). NOK and GBP samples showed no differences (Verified, small samples). Cause is Hypothesis (Tom Reyes): the EUR VAT total is computed on the invoice total, possibly linked to 8.2.4's currency conversion change. The customer's claim that every multi-currency invoice is wrong (about 140 invoices) is Reported and is not matched by the NOK sample.

| Fact | Tag | Source |
|---|---|---|
| Customer reports VAT total on every multi-currency invoice differs from sum of line VAT, since "your update last week" | Reported | Marta Kowalczyk, 2026-11-09 10:47 |
| About 140 invoices issued in EUR and NOK since 2 Nov | Reported | Marta Kowalczyk, 2026-11-09 10:47 |
| Auditors require per-line rounding; per-invoice rounding not acceptable | Reported | Marta Kowalczyk, 2026-11-09 10:47 and 15:30 |
| Customer auditors on site Thursday 12 Nov (account flag: 12 to 13 Nov, noted by CSM) | Reported (thread, internal note); account record flag | Thread 2026-11-10 13:55 and 14:20; account record |
| Account setting "VAT rounding: per line" is on; last changed 14 March 2026 | Verified | Tom Reyes internal note, 2026-11-09 14:30 |
| INV-LM-11402, 11417, 11431 (EUR) each have invoice VAT total EUR 0.01 below sum of line VAT | Verified | Tom Reyes internal note, 2026-11-09 14:30 |
| EUR sample of 20 invoices, 2 to 9 Nov: 7 differ by 0.01 (5 lower, 2 higher), 13 match | Verified | Tom Reyes internal note, 2026-11-09 14:30 |
| NOK: 9 of 9 sampled match. GBP: 11 of 11 sampled match | Verified | Tom Reyes internal note, 2026-11-09 14:30 |
| Sandbox (copy of production settings) EUR invoice, 3 x EUR 10.33 at 20%: line VAT 2.07 each (sum 6.21), invoice VAT 6.20 (20% of 30.99 rounded); same invoice in GBP gives 6.21 | Verified | Tom Reyes internal note, 2026-11-09 14:30 |
| Switching sandbox rounding to "per invoice" and back made no change for EUR | Verified | Tom Reyes internal note, 2026-11-09 14:30 |
| Release 8.2.4 deployed 2 Nov; notes say "Improved currency conversion precision for non-base-currency invoices" | Reported (release notes as quoted by Tom; not independently checked in the thread) | Tom Reyes internal note, 2026-11-09 14:30 |
| 8.2.4 change may be linked to the fault | Hypothesis (Tom Reyes, "Possible link; not confirmed") | 2026-11-09 14:30 |
| Per-line rounding is not applied to EUR invoices / EUR VAT total is computed on invoice total | Hypothesis (Tom Reyes) | 2026-11-09 14:30 and 14:45 |

**Open questions:** Why 7 of 20 EUR invoices differ and 13 do not (the sandbox case differs on a 3-line example; the rule that selects affected invoices is unknown). Why NOK, also non-base currency, showed no differences in 9 samples. Whether 8.2.4 caused it. Total number of affected invoices (the 140 is the customer's count of EUR and NOK, not affected ones). Whether a fix will recalculate issued invoices. Whether the 2 "higher" cases fit the same cause. Sample sizes are small; the 2 Nov start date for the customer's invoices is Reported.

## What has been tried
| Action | By | When | Result |
|---|---|---|---|
| Asked customer for example invoice numbers | Tom Reyes | 2026-11-09 11:20 | Received 3 EUR invoices at 12:05 |
| Checked account rounding setting | Tom Reyes | 2026-11-09 14:30 | "per line" on, last changed 14 Mar 2026 |
| Checked the three invoices | Tom Reyes | 2026-11-09 14:30 | Each 0.01 lower than line VAT sum |
| Sampled 20 EUR, 9 NOK, 11 GBP invoices | Tom Reyes | 2026-11-09 14:30 | 7 EUR differ; NOK and GBP none |
| Reproduced in customer sandbox | Tom Reyes | 2026-11-09 14:30 | Reproduced on EUR, not on GBP |
| Toggled sandbox rounding per invoice and back | Tom Reyes | 2026-11-09 14:30 | No change for EUR |
| Reviewed 8.2.4 release notes | Tom Reyes | 2026-11-09 14:30 | Possible link, not confirmed |
| Asked CSM Owen Pryce to go through service-level terms with customer | Tom Reyes (stated 09:10 message) | by 2026-11-10 09:10 | result not recorded (thread has no reply from Owen) |
| Escalated to Tier 2 | Tom Reyes | 2026-11-10 14:20 | Escalated, P2 |

## Commitments to the customer
| Commitment (quoted) | Made by | When | Status |
|---|---|---|---|
| "I'll send you a written summary of what we've reproduced, including the sandbox example, by 17:00 UK time today (Tuesday 10 November)." | Tom Reyes | 2026-11-10 09:10 | Open, due 2026-11-10 17:00 UTC (UK is on GMT in November, so 17:00 UK = 17:00 UTC). Not sent as of 14:20 (escalation note) |
| "I'll ask engineering whether a fix would recalculate invoices already issued." (commitment to ask only; recalculation not promised) | Tom Reyes | 2026-11-10 09:10 | Open; no answer recorded. Escalation note lists it as an open ask |
| "I'm escalating the fault to our Product Engineering Support team today." | Tom Reyes | 2026-11-10 09:10 | Met: escalated 2026-11-10 14:20 |
| "I've asked your Customer Success Manager, Owen Pryce, to go through the service-level terms in your contract with you." (a statement of action taken; no outcome promised) | Tom Reyes | 2026-11-10 09:10 | Not a time-bound promise; outcome not recorded. Customer has not been told the 24-hour term's result |

**Requested, not committed:** fix within 24 hours and confirmation of the 24 hours (Tom: "I'm not able to confirm contract terms myself"; "I can't give you a fix date"); the bug fixed; recalculation of issued invoices, or a decision on credit notes per invoice (Tom: "I can't promise that it will"); written confirmation for auditors beyond the summary above (the summary is committed, a wider confirmation is not).

## Service level
Measured at 2026-11-10 14:20 UTC (as-of time of the export). Readings used for ambiguous terms: none (no policy terms are available to read).

| Target (policy quote) | Clock start | Deadline (arithmetic) | Status |
|---|---|---|---|
| First response | Not determinable: support policy not supplied | Not determinable: support policy not supplied | Not determinable |
| Update cadence | Not determinable: support policy not supplied | Not determinable: support policy not supplied | Not determinable |
| Resolution | Not determinable: support policy not supplied | Not determinable: support policy not supplied | Not determinable |

The customer says the Enterprise contract requires a fix "within 24 hours" (Reported, 2026-11-09 10:47). If that were measured from ticket creation (10:47 UTC on 9 Nov) it would already have passed at 10:47 on 10 Nov. This is not a service-level finding; the policy has not been seen. The account record names Enterprise terms in "Master Services Agreement, Schedule 3". The tier-1 first reply was at 11:20 on 9 Nov (33 minutes after creation); whether that meets any target is not determinable.

Pauses: Policy does not state (policy not supplied)

## Recommended next action
Check how 8.2.4's non-base-currency calculation affects VAT rounding: run the sandbox EUR reproduction (3 x EUR 10.33 at 20%) against the 8.2.4 EUR code path and find why only some EUR invoices (7 of 20) are hit while NOK is not. Owner: Tier 2 Product Engineering Support engineer, by 2026-11-10 16:00 UTC, so Tom Reyes has the finding for the written summary due 17:00 UTC and Tier 2 can state whether issued invoices can be recalculated before the customer's auditors arrive on Thursday 12 Nov. Separately, Tom Reyes must send the promised summary by 17:00 UTC (it is his open commitment). Someone should obtain the Schedule 3 policy text to compute the service-level targets (own recommendation).
