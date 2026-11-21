# Escalation handoff: QB-203977 Per-line VAT rounding not applied on some EUR invoices since 8.2.4

Reference time ("now"): 2026-11-10 14:20 UTC (given in the thread export header; also the timestamp of the last thread message)
Inputs missing: policy (no support policy supplied; the account record only says "Enterprise (terms in Master Services Agreement, Schedule 3)" and Schedule 3 is not in the case)

## Problem as currently understood
Since release 8.2.4 (deployed 2 Nov), some EUR invoices on account LMS-0855 show an invoice VAT total that differs by EUR 0.01 from the sum of the line VAT, although the account is set to per-line VAT rounding. NOK and GBP samples show no differences. The working hypothesis is that EUR invoices compute VAT on the invoice total instead of per line, possibly linked to the 8.2.4 currency conversion change; this is not confirmed. The customer's auditors are on site Thursday 12 Nov and she needs a written summary today.

- Account setting "VAT rounding: per line" is on, last changed 14 March 2026 [verified] (Tom Reyes internal note, 2026-11-09 14:30; account record states per-line rounding)
- INV-LM-11402, INV-LM-11417, INV-LM-11431 (EUR) each have invoice VAT total EUR 0.01 below the sum of line VAT [verified] (Tom Reyes, 2026-11-09 14:30)
- In a sample of 20 EUR invoices issued 2 to 9 Nov, 7 differ by 0.01 (5 lower, 2 higher) and 13 match [verified] (Tom Reyes, 2026-11-09 14:30)
- All 9 NOK and 11 GBP invoices sampled show no difference [verified] (Tom Reyes, 2026-11-09 14:30). Sample sizes are small.
- Reproduced in the customer's sandbox: 3 lines of EUR 10.33 at 20% VAT; line VAT 2.07 each, sum 6.21; invoice VAT total 6.20 (20% of 30.99, rounded); same invoice in GBP gives 6.21 [verified] (Tom Reyes, 2026-11-09 14:30)
- Switching sandbox rounding to "per invoice" and back to "per line" made no change for EUR [verified] (Tom Reyes, 2026-11-09 14:30)
- Per-line rounding is not applied to EUR invoices [suspected] (Tom Reyes, 2026-11-09 14:30 "Looks like"; 14:45 "seems to be")
- VAT total on EUR invoices is calculated on the invoice total rather than line by line [suspected] (Tom Reyes, 2026-11-09 14:45)
- Release 8.2.4 (deployed 2 Nov, notes: "Improved currency conversion precision for non-base-currency invoices") is the cause [suspected] (Tom Reyes, 2026-11-09 14:30 "Possible link; not confirmed"). The release notes text and deploy date come from Tom's note; the causal link is unconfirmed.
- Every multi-currency invoice issued has the wrong VAT total [reported] (Marta Kowalczyk, 2026-11-09 10:47)
- About 140 invoices in EUR and NOK issued since 2 Nov [reported] (Marta Kowalczyk, 2026-11-09 10:47); not checked against the system
- The problem began with the update "last week" [reported] (Marta Kowalczyk, 2026-11-09 10:47)
- Per-invoice rounding is not acceptable to the customer's auditors; auditors require line-by-line rounding [reported] (Marta Kowalczyk, 2026-11-09 10:47 and 15:30)
- Auditors are on site Thursday 12 Nov [reported] (Marta Kowalczyk, 2026-11-10 13:55; Tom's note 14:20 repeats it) and the account record flags an audit on site 12 to 13 November 2026 [verified] (account record, noted by CSM)
- Contract requires a fix within 24 hours [reported] (Marta Kowalczyk, 2026-11-09 10:47); not confirmed by support, policy not supplied
Conflicts:
- Scope: customer says every multi-currency invoice is wrong [reported] (2026-11-09 10:47); support sampling found 7 of 20 EUR wrong and 0 of 9 NOK wrong [verified] (2026-11-09 14:30). The customer's own three examples were all in the affected group.
- Fix time: customer says the contract requires a fix within 24 hours [reported]; support has not agreed and has said it cannot confirm contract terms [verified] (Tom Reyes, 2026-11-10 09:10).

## Tried so far
| When | Who | What | Result |
|------|-----|------|--------|
| 2026-11-09 11:20 | Tom Reyes | Asked customer for 2-3 invoice numbers | Customer supplied three EUR invoices at 12:05 |
| 2026-11-09 14:30 | Tom Reyes | Checked the three invoices | Each invoice VAT total is 0.01 below line sum |
| 2026-11-09 14:30 | Tom Reyes | Sampled 20 EUR, 9 NOK, 11 GBP invoices | EUR 7 of 20 differ; NOK and GBP none |
| 2026-11-09 14:30 | Tom Reyes | Reproduced in sandbox (3 x EUR 10.33 at 20%) | EUR total 6.20 vs line sum 6.21; GBP 6.21 |
| 2026-11-09 14:30 | Tom Reyes | Toggled sandbox rounding to per invoice and back to per line | No change for EUR |
| 2026-11-09 14:45 | Tom Reyes | Offered workaround: per-invoice rounding | Customer rejected it (auditors), 15:30 |
| 2026-11-10 09:10 | Tom Reyes | Asked CSM Owen Pryce to go through service-level terms with customer | Result not recorded |
| 2026-11-10 14:20 | Tom Reyes | Escalated to Tier 2 | Escalated; asks listed in escalation note |
Not yet run (not in the thread): checking whether the 13 matching EUR invoices simply have no rounding gap, a check of the other 130 or so issued invoices, and comparison against pre-8.2.4 behaviour.

## Commitments to the customer
| When | Made by | Verbatim commitment | Status (met / pending / overdue) | Policy note |
|------|---------|---------------------|----------------------------------|-------------|
| 2026-11-10 09:10 | Tom Reyes | "I'm escalating the fault to our Product Engineering Support team today." | met (escalated 2026-11-10 14:20) | Policy not supplied |
| 2026-11-10 09:10 | Tom Reyes | "I'll ask engineering whether a fix would recalculate invoices already issued." | pending (listed as an open ask in the escalation note; no answer recorded) | Policy not supplied |
| 2026-11-10 09:10 | Tom Reyes | "I'll send you a written summary of what we've reproduced, including the sandbox example, by 17:00 UK time today (Tuesday 10 November)." | pending; not sent as of 14:20 (escalation note: "haven't sent yet"); due 17:00 UK time = 17:00 UTC (UK is on GMT in November), 2 h 40 min from now | Policy not supplied |
Not commitments: Tom's statements "I can't give you a fix date" and "I can't promise that it will [recalculate]" are disclaimers. The 24-hour fix is the customer's claim about the contract, not a promise in the thread.

## Service level
- Clause: not available. The policy was not supplied; the account record says only "Enterprise (terms in Master Services Agreement, Schedule 3)".
- Clock: resolution, claimed by the customer as 24 hours ("you are required to fix this within 24 hours"); business or calendar hours unknown. Started: ticket created 2026-11-09 10:47 UTC (priority P2).
- Deadline: if the claim is right and the clock is calendar hours, 2026-11-10 10:47 UTC (10:47 + 24 h), already passed by 3 h 33 min. If business hours, it could still be open. Not computable without the clause.
- Status: cannot determine; missing terms: Schedule 3 text (clock types and durations, whether P2 has a 24-hour resolution target, business-hours definition and time zone, credit rules). First response and update interval clocks are likewise undeterminable; first response was given 2026-11-09 11:20 UTC, 33 minutes after creation.

## Open questions
- Does the contract require a fix within 24 hours, and does it apply to P2? (asked by Marta Kowalczyk, 2026-11-09 10:47 and 15:30; Tom Reyes has asked Owen Pryce to go through the terms, no answer recorded)
- Will a fix recalculate or correct invoices already issued, or must the customer raise a credit note for each? (Marta Kowalczyk, 2026-11-09 15:30)
- When will the bug be fixed? (Marta Kowalczyk, 2026-11-09 15:30; Tom said he cannot give a date)
- Written confirmation of findings for the auditors (Marta Kowalczyk, 2026-11-09 15:30; see commitment above)
- Is 8.2.4 the cause? (not asked by anyone explicitly; raised by Tom Reyes as unconfirmed, 2026-11-09 14:30)

## Recommended next action
Send the written summary of reproduced findings, including the sandbox example (3 x EUR 10.33 at 20%: line VAT sum 6.21, invoice VAT 6.20; GBP 6.21; sample counts; the per-invoice toggle test), to Marta Kowalczyk, owner Tom Reyes, by 17:00 UTC (17:00 UK time) on 2026-11-10. Keep suspected causes labelled as suspected and make no fix date or recalculation promise. Tier 2 should in parallel decide whether to confirm the 8.2.4 link and answer the recalculation question before the auditors arrive Thursday 12 Nov. Rests on: the 2026-11-10 09:10 commitment, the 14:20 escalation note ("haven't sent yet"), and the 2026-11-10 13:55 customer message.
