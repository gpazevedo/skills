Clarifying question: Please supply the support policy (the service-level terms in the Master Services Agreement, Schedule 3, referenced in the account record) so the service-level targets, deadlines and the customer's "fix within 24 hours" claim can be checked.

# Escalation handoff: QB-203977 Per-line VAT rounding not applied to some EUR invoices since release 8.2.4

**Customer:** Lindqvist Marine Supplies Ltd (LMS-0855), plan Quillbill Trade (annual subscription), support level Enterprise (account record: Plan, Support level)
**Earliest deadline:** 17:00 UK time, Tuesday 10 November 2026 (17:00 UTC, as UK time in November is GMT): written summary of findings for the customer's auditors, promised by Tom Reyes and not yet sent (thread, Tom Reyes 2026-11-10 09:10 UTC; escalation note 2026-11-10 14:20 UTC). Service-level deadlines: Not determinable: support policy not supplied.

## Problem as currently understood
On some EUR invoices the invoice VAT total differs by EUR 0.01 from the sum of the line VAT, even though the account is set to per-line VAT rounding; support found this in 7 of 20 sampled EUR invoices, none in NOK or GBP, and reproduced it in the sandbox, where the EUR VAT total equals invoice-level rounding (6.20) instead of the line sum (6.21). Two hypotheses are open: that per-line rounding is not applied to EUR invoices, and that release 8.2.4 (deployed 2 Nov, "Improved currency conversion precision for non-base-currency invoices") caused it, both from Tom Reyes. Neither explains why NOK, also a non-base currency, is unaffected, or why only some EUR invoices differ.

### Verified
- Account setting "VAT rounding: per line" is on, last changed 14 March 2026 (internal note, Tom Reyes 2026-11-09 14:30 UTC; account record: VAT settings)
- INV-LM-11402, INV-LM-11417 and INV-LM-11431 (all EUR) each have an invoice VAT total EUR 0.01 lower than the sum of their line VAT (internal note, Tom Reyes 2026-11-09 14:30 UTC)
- Of 20 EUR invoices issued 2 to 9 Nov, 7 show a EUR 0.01 difference (5 lower, 2 higher) and 13 match (internal note, Tom Reyes 2026-11-09 14:30 UTC)
- All 9 NOK invoices issued 2 to 9 Nov show no difference (internal note, Tom Reyes 2026-11-09 14:30 UTC)
- 11 sampled GBP invoices show no difference (internal note, Tom Reyes 2026-11-09 14:30 UTC)
- Reproduced in the customer's sandbox: EUR invoice with 3 lines of EUR 10.33 at 20% VAT gives line VAT 2.07 each (sum 6.21) but invoice VAT total 6.20, which is 20% of 30.99 rounded; the same invoice in GBP gives VAT total 6.21 (internal note, Tom Reyes 2026-11-09 14:30 UTC)
- Switching the sandbox rounding setting to "per invoice" and back to "per line" made no change for EUR (internal note, Tom Reyes 2026-11-09 14:30 UTC)
- Release 8.2.4 was deployed 2 Nov with the release note "Improved currency conversion precision for non-base-currency invoices" (internal note, Tom Reyes 2026-11-09 14:30 UTC)

### Reported, not verified
- The problem started after "your update last week" (Marta Kowalczyk 2026-11-09 10:47 UTC); support sampled only invoices from 2 Nov onward, so no before/after comparison exists in the thread
- About 140 EUR and NOK invoices have been issued since 2 November (Marta Kowalczyk 2026-11-09 10:47 UTC)
- The customer's auditors require line-by-line VAT rounding, so per-invoice rounding is not acceptable (Marta Kowalczyk 2026-11-09 10:47 UTC and 15:30 UTC)
- Auditors are on site Thursday 12 November (Marta Kowalczyk 2026-11-10 13:55 UTC); consistent with the account record flag "External audit on site 12 to 13 November 2026 (noted by CSM)" (account record: Account flags)

### Contradicted
- "Every multi-currency invoice we issue has the wrong VAT total" (Marta Kowalczyk 2026-11-09 10:47 UTC): support found 13 of 20 sampled EUR invoices correct and none of the 9 NOK invoices affected (internal note, Tom Reyes 2026-11-09 14:30 UTC; Tom Reyes to customer 2026-11-09 14:45 UTC)

### Hypotheses
- Per-line rounding is not applied to EUR invoices; the EUR VAT total is calculated on the invoice total, proposed by Tom Reyes (internal note 2026-11-09 14:30 UTC; Tom Reyes to customer 2026-11-09 14:45 UTC)
- Release 8.2.4's currency conversion change caused the fault ("Possible link; not confirmed"), proposed by Tom Reyes (internal note 2026-11-09 14:30 UTC; escalation note 2026-11-10 14:20 UTC)

## Tried so far
| # | Action | By | Result | Source |
| --- | --- | --- | --- | --- |
| 1 | Asked customer for two or three affected invoice numbers | Tom Reyes | Customer sent INV-LM-11402, INV-LM-11417, INV-LM-11431, all EUR | Tom Reyes 2026-11-09 11:20 UTC; Marta Kowalczyk 2026-11-09 12:05 UTC |
| 2 | Checked account VAT rounding setting | Tom Reyes | "Per line" on, last changed 14 March 2026 | Internal note 2026-11-09 14:30 UTC |
| 3 | Checked the three supplied invoices | Tom Reyes | Each invoice VAT total EUR 0.01 below sum of line VAT | Internal note 2026-11-09 14:30 UTC |
| 4 | Sampled 20 EUR invoices issued 2 to 9 Nov | Tom Reyes | 7 differ by EUR 0.01 (5 lower, 2 higher); 13 match | Internal note 2026-11-09 14:30 UTC |
| 5 | Checked all 9 NOK invoices issued 2 to 9 Nov | Tom Reyes | None differ | Internal note 2026-11-09 14:30 UTC |
| 6 | Sampled 11 GBP invoices | Tom Reyes | None differ | Internal note 2026-11-09 14:30 UTC |
| 7 | Created EUR test invoice in sandbox (3 lines of EUR 10.33 at 20% VAT) | Tom Reyes | Invoice VAT total 6.20 against line VAT sum 6.21 | Internal note 2026-11-09 14:30 UTC |
| 8 | Created the same invoice in GBP in sandbox | Tom Reyes | VAT total 6.21 (correct) | Internal note 2026-11-09 14:30 UTC |
| 9 | Switched sandbox rounding to "per invoice" and back to "per line" | Tom Reyes | No change for EUR | Internal note 2026-11-09 14:30 UTC |
| 10 | Reviewed release notes for 8.2.4 | Tom Reyes | Possible link to currency conversion change; not confirmed | Internal note 2026-11-09 14:30 UTC |
| 11 | Offered per-invoice rounding as a workaround | Tom Reyes | Customer rejected it: not acceptable to auditors | Tom Reyes 2026-11-09 14:45 UTC; Marta Kowalczyk 2026-11-09 15:30 UTC |
| 12 | Escalated to Tier 2 (Product Engineering Support), priority P2 | Tom Reyes | Status Open to Escalated | Event 2026-11-10 14:20 UTC |

## Commitments to the customer
| Commitment (quoted) | Made by | When | Due | Kept / Missed / Open | Source |
| --- | --- | --- | --- | --- | --- |
| "I'm escalating the fault to our Product Engineering Support team today." | Tom Reyes (Tier 1) | 2026-11-10 09:10 UTC | "today" (10 November 2026) | Kept: escalated 2026-11-10 14:20 UTC | Tom Reyes 2026-11-10 09:10 UTC; event 2026-11-10 14:20 UTC |
| "I'll ask engineering whether a fix would recalculate invoices already issued." | Tom Reyes (Tier 1) | 2026-11-10 09:10 UTC | No time stated | Kept: question included in escalation note as an open ask; no answer to the customer was promised and none exists yet | Tom Reyes 2026-11-10 09:10 UTC; escalation note 2026-11-10 14:20 UTC |
| "I'll send you a written summary of what we've reproduced, including the sandbox example, by 17:00 UK time today (Tuesday 10 November)." | Tom Reyes (Tier 1) | 2026-11-10 09:10 UTC | 17:00 UK time, 10 November 2026 (17:00 UTC) | Open as of last thread timestamp (2026-11-10 14:20 UTC), 2h 40m remaining; escalation note says "haven't sent yet". See Gaps on current time | Tom Reyes 2026-11-10 09:10 UTC; escalation note 2026-11-10 14:20 UTC |
| "I've asked your Customer Success Manager, Owen Pryce, to go through the service-level terms in your contract with you." | Tom Reyes (Tier 1), on behalf of Owen Pryce | 2026-11-10 09:10 UTC | No time stated | Open: no message from Owen Pryce in thread | Tom Reyes 2026-11-10 09:10 UTC |

Customer-claimed, not found in thread:
- Contractual obligation to fix within 24 hours: "Under our Enterprise contract you are required to fix this within 24 hours" (Marta Kowalczyk 2026-11-09 10:47 UTC; repeated 15:30 UTC). Support declined to confirm it (Tom Reyes 2026-11-10 09:10 UTC); it cannot be checked because the support policy was not supplied.

Possible expectations from non-committal statements:
- None

## Service level
- Tier and priority: Enterprise support level, terms in Master Services Agreement Schedule 3 (account record: Support level); priority P2 assigned at ticket creation and confirmed at escalation (events 2026-11-09 10:47 UTC and 2026-11-10 14:20 UTC)
- Status as of: last thread timestamp, 2026-11-10 14:20 UTC
- Timestamps a clock could run from: ticket created 2026-11-09 10:47 UTC; first agent reply 2026-11-09 11:20 UTC; last update to customer 2026-11-10 09:10 UTC; escalated to Tier 2 2026-11-10 14:20 UTC (thread events and messages). No pause events in thread.

| Target (quoted) | Policy section | Clock start / pauses | Deadline (arithmetic) | Status |
| --- | --- | --- | --- | --- |
| Not determinable: support policy not supplied | Not determinable: support policy not supplied | Start candidates listed above; pause rules unknown | Not determinable: support policy not supplied | Not determinable: support policy not supplied |

Thread-stated term: the customer says the contract requires a fix within 24 hours (Marta Kowalczyk 2026-11-09 10:47 UTC); no policy term was supplied to compare it against.

## Recommended next action
Make sure the written summary Tom Reyes promised reaches Marta Kowalczyk by 17:00 UTC on 10 November, built only from the verified findings (the three invoices, the 7-of-20 EUR sample, the clean NOK and GBP samples, and the sandbox reproduction) with the 8.2.4 link stated as unconfirmed. It is the only dated commitment, it was still unsent at escalation, and the customer's auditors are on site from 12 November. For root cause, start from the sandbox reproduction (3 lines of EUR 10.33 at 20% VAT) against the 8.2.4 non-base-currency change, and account for NOK invoices being unaffected.

## Gaps
- Support policy (MSA Schedule 3) not supplied: blocks every service-level target, deadline and status, and blocks checking the customer's 24-hour fix claim.
- Current time: the thread ends 2026-11-10 14:20 UTC, but the current date is 2026-11-21. If the supplied export is complete, the written-summary commitment (due 17:00 UTC 10 Nov) has passed with no fulfilling message and would be Missed; statuses above are given as of the last thread timestamp.
- Time zone: "17:00 UK time" converted to 17:00 UTC on the assumption that UK time on 10 November is GMT; the supplied material does not state this.
- Software version of the sandbox is not recorded; the account record says it is a copy of production settings refreshed monthly, so whether it runs 8.2.4 is unknown.
- Start date unverified: no invoices from before 2 November were checked, so the link to the 8.2.4 release rests on timing alone.
- Unexplained: why NOK invoices (also non-base currency) are unaffected, and why only 7 of 20 EUR invoices differ, including 2 that are higher.
- Unanswered customer asks: whether a fix will recalculate already-issued invoices or the customer must raise credit notes (Marta Kowalczyk 2026-11-09 15:30 UTC); no fix date given (Tom Reyes 2026-11-10 09:10 UTC).
- Result not recorded: whether Owen Pryce has contacted the customer about service-level terms.
