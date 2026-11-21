# Escalation handoff: QB-203977 Per-line VAT rounding not applied to some EUR invoices since 8.2.4

**Customer:** Lindqvist Marine Supplies Ltd, Quillbill Trade (annual), Enterprise support level (account record: Plan, Support level)
**Earliest deadline:** 2026-11-10 17:00 UTC (17:00 UK time is 17:00 UTC on 10 Nov): written summary of reproduced findings promised to the customer by Tom Reyes (thread, Tom Reyes 2026-11-10 09:10 UTC). Not yet sent as of 14:20 UTC (thread, escalation note 2026-11-10 14:20 UTC). No policy-based deadline can be determined (see Service level).

## Problem as currently understood
On EUR invoices issued since 2 Nov (release 8.2.4), the invoice VAT total is sometimes EUR 0.01 different from the sum of line VAT, even though the account is set to per-line rounding. It was reproduced in the customer's sandbox on EUR but not on GBP, and no NOK differences were found in the sample. Hypothesis only: the 8.2.4 currency conversion change bypasses per-line rounding for EUR.

### Verified
- Account setting "VAT rounding: per line" is on, last changed 14 March 2026 (thread, Tom Reyes internal note 2026-11-09 14:30; account record: VAT settings "VAT rounding per line")
- INV-LM-11402, INV-LM-11417 and INV-LM-11431 each have an invoice VAT total EUR 0.01 lower than the sum of line VAT (thread, internal note 2026-11-09 14:30)
- Sample of 20 EUR invoices issued 2 to 9 Nov: 7 differ by 0.01 (5 lower, 2 higher), 13 match (thread, internal note 2026-11-09 14:30)
- Sample of 9 NOK invoices (same period): none differ; 11 GBP invoices sampled: none differ (thread, internal note 2026-11-09 14:30)
- Sandbox reproduction (copy of production settings): new EUR invoice, 3 lines of EUR 10.33 at 20% VAT; line VAT 2.07 each, sum 6.21; invoice VAT total 6.20 (20% of 30.99 rounded); same invoice in GBP gives 6.21 (thread, internal note 2026-11-09 14:30)
- Switching the sandbox setting to "per invoice" and back to "per line" made no change for EUR (thread, internal note 2026-11-09 14:30)
- Release notes for 8.2.4, deployed 2 Nov, say "Improved currency conversion precision for non-base-currency invoices" (as quoted in thread, internal note 2026-11-09 14:30). The release note text is verified as quoted by the agent; its link to the fault is not.
- EUR and NOK invoice currencies are enabled on the account; base currency GBP (account record)

### Reported, not verified
- About 140 invoices in EUR and NOK issued since 2 November (thread, Marta Kowalczyk 2026-11-09 10:47). Support only sampled 29 EUR/NOK invoices.
- Problem began with the update "last week" (thread, Marta Kowalczyk 2026-11-09 10:47). Support's samples cover 2 to 9 Nov only; no pre-2 Nov invoices were checked in the thread.
- Per-invoice rounding is not acceptable to the customer's auditors, who require line-by-line rounding (thread, Marta Kowalczyk 2026-11-09 10:47 and 15:30)
- Auditors arrive Thursday (thread, Marta Kowalczyk 2026-11-10 13:55). The account record flags an external audit on site 12 to 13 November 2026, noted by the CSM (account record, Account flags), which is consistent; 12 Nov 2026 is a Thursday.
- The customer has no confidence in any issued invoices (thread, Marta Kowalczyk 2026-11-09 10:47)

### Contradicted
- "Every multi-currency invoice we issue has the wrong VAT total" (Marta Kowalczyk 2026-11-09 10:47): support found 13 of 20 EUR invoices correct and 0 of 9 NOK and 0 of 11 GBP sampled incorrect (internal note 2026-11-09 14:30). Samples are small, so this is a finding on the sample, not a full-population result.

### Hypotheses
- Per-line rounding is not applied to EUR invoices, so VAT total is calculated on the invoice total, proposed by Tom Reyes (internal note 2026-11-09 14:30 "Looks like..."; message 2026-11-09 14:45 "seems to be")
- The 8.2.4 change to currency conversion precision is linked to the fault, proposed by Tom Reyes, explicitly "not confirmed" (internal note 2026-11-09 14:30)

## Tried so far
| # | Action | By | Result | Source |
| --- | --- | --- | --- | --- |
| 1 | Asked customer for 2 or 3 example invoice numbers | Tom Reyes | Customer supplied INV-LM-11402, 11417, 11431 (all EUR) | Thread 2026-11-09 11:20, 12:05 |
| 2 | Checked the account VAT rounding setting | Tom Reyes | "per line" is on, last changed 14 March 2026 | Internal note 2026-11-09 14:30 |
| 3 | Checked the three invoices | Tom Reyes | Each invoice VAT total EUR 0.01 below line VAT sum | Internal note 2026-11-09 14:30 |
| 4 | Sampled 20 EUR, 9 NOK, 11 GBP invoices | Tom Reyes | EUR 7 of 20 differ; NOK and GBP none | Internal note 2026-11-09 14:30 |
| 5 | Reproduced in sandbox (EUR vs GBP, 3 x EUR 10.33 at 20%) | Tom Reyes | EUR 6.20 vs expected 6.21; GBP 6.21 | Internal note 2026-11-09 14:30 |
| 6 | Toggled sandbox rounding to "per invoice" and back to "per line" | Tom Reyes | No change for EUR | Internal note 2026-11-09 14:30 |
| 7 | Reviewed 8.2.4 release notes | Tom Reyes | Possible link, not confirmed | Internal note 2026-11-09 14:30 |
| 8 | Proposed per-invoice rounding as workaround | Tom Reyes | Customer rejected (auditors). Note: in the sandbox, per-invoice did not change EUR behaviour, so it may not work as a workaround anyway | Thread 2026-11-09 14:45, 15:30; internal note 2026-11-09 14:30 |
| 9 | Asked CSM Owen Pryce to take the customer through service-level terms | Tom Reyes | Result not recorded | Thread 2026-11-10 09:10 |
| 10 | Escalated to Tier 2 | Tom Reyes | Status Escalated, priority P2 | Thread 2026-11-10 14:20 |

## Commitments to the customer
| Commitment (quoted) | Made by | When | Due | Kept / Missed / Open | Source |
| --- | --- | --- | --- | --- | --- |
| "I'll send you a written summary of what we've reproduced, including the sandbox example, by 17:00 UK time today (Tuesday 10 November)." | Tom Reyes (Tier 1) | 2026-11-10 09:10 UTC | 17:00 UK time, Tue 10 Nov (= 17:00 UTC; UK is on GMT in November) | Open: 2h40m left as of 14:20 UTC; escalation note says not yet sent | Thread 2026-11-10 09:10; escalation note 14:20 |
| "I'm escalating the fault to our Product Engineering Support team today." | Tom Reyes | 2026-11-10 09:10 UTC | "today" (10 Nov) | Kept | Thread 2026-11-10 09:10; escalation event 14:20 |
| "I'll ask engineering whether a fix would recalculate invoices already issued." | Tom Reyes | 2026-11-10 09:10 UTC | No time stated | Open (question is for Tier 2; no answer in thread) | Thread 2026-11-10 09:10; escalation note lists it as open ask |
| "I've asked your Customer Success Manager, Owen Pryce, to go through the service-level terms in your contract with you." | Tom Reyes | 2026-11-10 09:10 UTC | No time stated | Open (no CSM contact recorded) | Thread 2026-11-10 09:10 |

Customer-claimed, not found in thread:
- "Under our Enterprise contract you are required to fix this within 24 hours" and "please confirm the 24 hours" (Marta Kowalczyk 2026-11-09 10:47 and 15:30). No support person confirmed this; Tom Reyes said he could not confirm contract terms (thread 2026-11-10 09:10). Not a commitment.

Not commitments, listed as possible expectations:
- "I can't give you a fix date" and "I can't promise that it will [recalculate]" are explicit non-promises (thread 2026-11-10 09:10). The customer's three asks (fix; correction of issued invoices vs credit notes; written confirmation for auditors) are open asks (thread 2026-11-09 15:30).

## Service level
- Tier and priority: Enterprise support level, terms in MSA Schedule 3 (account record); priority P2 assigned at ticket creation and still P2 at escalation (thread 2026-11-09 10:47 and 2026-11-10 14:20)
- Status as of: 2026-11-10 14:20 UTC (as-of time stated in the thread export, treated as current)

| Target (quoted) | Policy section | Clock start / pauses | Deadline (arithmetic) | Status |
| --- | --- | --- | --- | --- |
| Customer's claimed "fix this within 24 hours" | Not determinable: support policy not supplied; MSA Schedule 3 not supplied | Not determinable | Not determinable | Not determinable |
| First response, update interval, resolution targets for Enterprise P2 | Not determinable: support policy not supplied | Ticket created 2026-11-09 10:47 UTC; first agent reply 2026-11-09 11:20 UTC (timestamps only) | Not determinable | Not determinable |

Whether P2 is the right priority also cannot be judged without the policy's criteria.

## Recommended next action
Send Marta the written summary of the reproduced findings (the sandbox example, the EUR 7 of 20 sample, no NOK or GBP differences) before 17:00 UTC today, 10 Nov, then investigate why 8.2.4 breaks per-line rounding on EUR invoices. Also answer whether a fix will recalculate issued invoices, because her auditors arrive Thursday 12 Nov and she is deciding between credit notes and correction.

## Gaps
- Support policy not supplied: all service-level targets, clocks and deadlines are Not determinable. MSA Schedule 3 (referenced by the account record) is also not supplied. The customer's "24 hours" claim cannot be checked. Please supply the policy.
- The scope is unmeasured: the "about 140 invoices" claim is unverified, and no pre-2 Nov invoices or full EUR population were checked. The pattern (7 of 20 EUR, none NOK/GBP) is unexplained.
- Whether the per-invoice workaround works is unclear: sandbox toggling made no difference on EUR.
- Whether the written summary has been sent: escalation note says "haven't sent yet" as of 14:20 UTC.
- Result of the CSM service-level discussion with Owen Pryce is not recorded.
- Whether a fix would recalculate issued invoices is unanswered.

Please supply the support policy (including MSA Schedule 3 service-level terms) so the service-level section can be completed.
