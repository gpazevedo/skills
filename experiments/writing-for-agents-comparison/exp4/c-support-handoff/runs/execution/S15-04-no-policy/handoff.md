## 1. Summary

Lindqvist Marine Supplies Ltd (account LMS-0855, Enterprise support level) reports that Quillbill Invoicing, since release 8.2.4 on 2 November 2026, issues some EUR invoices whose VAT total differs by EUR 0.01 from the sum of the line VAT, despite the account being set to per-line VAT rounding. It is urgent because Tier 1 promised the customer a written summary by 17:00 UK time (17:00 UTC; see Section 5) on 10 November 2026, about 2h40m after the 14:20 UTC escalation, and the customer's auditors are on site 12 to 13 November 2026.

## 2. Problem and evidence

Symptoms
- _Reported_: Since "your update last week", invoices have an invoice VAT total that does not equal the sum of line VAT. Source: Marta Kowalczyk, 2026-11-09 10:47 UTC.
- _Reported_: "every multi-currency invoice" is affected, and about 140 invoices in EUR and NOK were issued since 2 November. Source: same message. Conflicts with the sample below (Section 7).
- _Reported_: Auditors require per-line VAT rounding. Source: 2026-11-09 10:47 and 15:30 UTC. Per-invoice rounding is "not acceptable" to them.
- _Verified_: Account setting "VAT rounding: per line" is on, last changed 14 March 2026. Source: Tom Reyes internal note, 2026-11-09 14:30 UTC.
- _Verified_: INV-LM-11402, INV-LM-11417 and INV-LM-11431 (all EUR, named by the customer at 12:05 UTC) each have an invoice VAT total EUR 0.01 lower than the sum of line VAT. Source: Tom's internal note, 14:30 UTC.
- _Verified_: In a sample of 20 EUR invoices issued 2 to 9 Nov, 7 differ by 0.01 (5 lower, 2 higher) and 13 match. All 9 NOK invoices sampled in the same period match. All 11 GBP invoices sampled match. Source: Tom's internal note, 14:30 UTC. How the 20 were chosen is not recorded.
- _Verified_: Reproduction in the customer's sandbox (copy of production settings): new EUR invoice, 3 lines of EUR 10.33 at 20% VAT. Line VAT is 2.07 each, sum 6.21. Invoice VAT total shows 6.20, which is 20% of 30.99 rounded. The same invoice in GBP shows 6.21. Source: Tom's internal note, 14:30 UTC.
- _Verified_: In the sandbox, switching the setting to "per invoice" and back to "per line" made no change for EUR. Source: same note.

Diagnosis
- _Hypothesis_: Per-line rounding is not applied to EUR invoices; the VAT total appears to be computed on the invoice total. Tom's note says "Looks like"; his customer message says "seems". Untested beyond the sandbox example and the sample.
- _Hypothesis_: Release 8.2.4 (deployed 2 Nov, "Improved currency conversion precision for non-base-currency invoices") is the cause. Tom: "Possible link; not confirmed." Timing matches the customer's report; no log, diff or rollback test is recorded.

## 3. Tried so far

| Action | Result | Who |
|---|---|---|
| Asked customer for 2-3 affected invoice numbers (2026-11-09 11:20 UTC) | Customer supplied three EUR invoices at 12:05 UTC | Tom Reyes |
| Checked account VAT rounding setting | "Per line", last changed 14 March 2026 | Tom Reyes |
| Checked the three named invoices | Each 0.01 lower than the line VAT sum | Tom Reyes |
| Sampled 20 EUR, 9 NOK and 11 GBP invoices, 2 to 9 Nov | EUR 7/20 differ; NOK 0/9; GBP 0/11 | Tom Reyes |
| Reproduced in the customer's sandbox (EUR, 3 x 10.33 at 20%) | Reproduced; GBP equivalent correct | Tom Reyes |
| Toggled sandbox rounding to "per invoice" and back to "per line" | No change for EUR; result with per-invoice on a GBP invoice or on the earlier "per invoice" EUR total not recorded | Tom Reyes |
| Compared with release notes for 8.2.4 | Possible link, not confirmed | Tom Reyes |
| Asked CSM Owen Pryce to take the customer through the contract service-level terms (stated 2026-11-10 09:10 UTC) | Result not recorded | Tom Reyes |
| Escalated to Tier 2 (2026-11-10 14:20 UTC) | Done | Tom Reyes |

Not tried (no record): checking the production invoice logs or calculation path, testing NOK or other currencies in the sandbox with the same line values, testing whether the sandbox mismatch exists before 8.2.4, identifying which EUR invoices are affected across all ~140.

## 4. Commitments to the customer

| Quote | Author | When (UTC) | Status |
|---|---|---|---|
| "I'm escalating the fault to our Product Engineering Support team today." | Tom Reyes | 2026-11-10 09:10 | Kept: escalated 14:20 UTC the same day |
| "I can't give you a fix date." | Tom Reyes | 2026-11-10 09:10 | Not a commitment; no fix date has been given |
| "I'll ask engineering whether a fix would recalculate invoices already issued. I can't promise that it will" | Tom Reyes | 2026-11-10 09:10 | Open. The escalation note lists it as an open ask; no answer yet. No recalculation is promised |
| "I'll send you a written summary of what we've reproduced, including the sandbox example, by 17:00 UK time today (Tuesday 10 November)." | Tom Reyes | 2026-11-10 09:10 | Open, not sent as of 14:20 UTC (escalation note: "haven't sent yet") |
| "I've asked your Customer Success Manager, Owen Pryce, to go through the service-level terms in your contract with you." | Tom Reyes | 2026-11-10 09:10 | Open. No record that Owen has done so |
| "I've started looking at this." | Tom Reyes | 2026-11-09 11:20 | Vague; kept in the sense that investigation took place |

Not promised: the 24-hour fix the customer demands. Tom wrote "I'm not able to confirm contract terms myself". The customer asked on 2026-11-09 10:47 and 15:30 for confirmation of the 24 hours and none was given.

## 5. Service level

- Tier: Enterprise support level, terms in Master Services Agreement, Schedule 3 (account record, 2026 contract term 1 Jan 2026 to 31 Dec 2027).
- Policy text: not supplied. Response time, resolution time and severity definition (including what P2 means) are all "not stated in the supplied policy". No deadline is given for any of them.
- Customer's claim (_reported_, not verified): "Under our Enterprise contract you are required to fix this within 24 hours." Clock start for that claim would be ticket creation, 2026-11-09 10:47 UTC, but it cannot be confirmed or used. Whether any 24-hour term exists, what it covers (fix versus response) and whether it applies at P2 must be checked in Schedule 3.
- The only deadline in the case is the one support set itself: written summary by 17:00 UK time on 10 November 2026. UK time on that date is GMT (clocks go back in October), so that is 17:00 UTC. As of 2026-11-10 14:20 UTC: 2 hours 40 minutes remaining.
- Customer's external date: auditors on site 12 to 13 November 2026 (account flag; customer says "Thursday", which is 12 November).

## 6. Recommended next action

Primary: Tier 2 (Product Engineering Support) engineer on this ticket to send the promised written summary to Marta Kowalczyk before 17:00 UTC on 10 November 2026, limited to verified facts: the three invoices, the 20/9/11 sample results, the sandbox example (3 x EUR 10.33 at 20%: 6.21 versus 6.20) and the unchanged-on-toggle result. State the cause as under investigation and make no claim about the fix date, recalculation of issued invoices or contract terms. This serves the open 17:00 commitment. It confirms nothing new technically; its purpose is the commitment and the auditors' need.

In parallel (same owner or Tier 2 lead):
1. Confirm whether 8.2.4 is the cause (compare calculation path for non-base-currency invoices, or test the sandbox example on a pre-8.2.4 build). This confirms or rules out the release-notes hypothesis and the "total computed from invoice total" hypothesis.
2. Get engineering's answer on recalculating already-issued invoices (open commitment from 09:10 UTC), and an estimate of how many of the ~140 EUR/NOK invoices are affected.
3. Ask the CSM Owen Pryce (or account management) to confirm he has gone through Schedule 3 with the customer, and obtain the actual clause text so Section 5 can be completed.

Alternative: if the summary cannot be finished by 17:00 UTC, send a short holding message before then saying when it will follow, rather than missing the promise silently.

## 7. Gaps and conflicts

- Missing input: the support policy text (not supplied) and the Schedule 3 terms. No response, resolution or severity terms can be stated. P2 priority is unexplained.
- Conflict: customer says "every multi-currency invoice" is wrong; the sample found 7 of 20 EUR invoices affected and 0 of 9 NOK. Whether NOK is affected at all is unestablished. The customer's 140 count is unverified. Customer counts EUR and NOK together.
- Conflict/uncertainty: 2 of the 7 sample differences were higher, while all 3 customer invoices were lower. Compatible with an invoice-level calculation but not confirmed.
- Odd: the sandbox shows no change on toggling rounding for EUR, which suggests the setting is ignored for EUR, so "switch to per-invoice rounding" (Tom's workaround, 14:45 UTC on 9 Nov) may not work. Not tested on production data.
- Setting last changed 14 March 2026, before 8.2.4, so a settings change is not an explanation.
- Not recorded: whether Owen Pryce has been contacted or replied; the customer has said "Fine" (13:55 UTC) only in response to this.
- Sample method for the 20 EUR invoices not recorded. Whether the sandbox, a monthly copy of production settings, reflects production code is assumed.
- Customer expects a statement on credit notes for issued invoices; none has been given. No open credits on account.
- Related earlier ticket QB-196320 (P3, NOK currency formatting on PDF invoices, resolved 21 August 2026) is not obviously linked; no evidence either way.
