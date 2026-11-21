# Escalation handoff: QB-203977, Lindqvist Marine Supplies Ltd

**Service level:** Undetermined, deadline Undetermined, target Undetermined: the support policy (Master Services Agreement, Schedule 3, per the account record) was not supplied, so no target, clock rule or priority criteria can be quoted.
**Next action:** Get the written summary of reproduced findings to Marta Kowalczyk before 17:00 UK time (17:00 UTC) today, Tuesday 10 November; Tom Reyes promised it and the escalation note says it has not been sent.

## Problem as currently understood
Per-line VAT rounding is not applied to some EUR invoices on an account set to per-line rounding: the invoice VAT total appears to be calculated on the invoice total instead of summed from line VAT, giving EUR 0.01 differences in either direction. It possibly began with release 8.2.4 (2 Nov), not confirmed. This is narrower than the opening report, which said every multi-currency invoice (EUR and NOK) was wrong; Tom's sampling found the fault in 7 of 20 EUR invoices and in no NOK or GBP invoices.

Evidence:
- [Verified] Account setting "VAT rounding: per line" is on, last changed 14 March 2026 (Tom Reyes, account settings, internal note 2026-11-09 14:30 UTC; account record also shows "VAT rounding per line")
- [Verified] INV-LM-11402, INV-LM-11417 and INV-LM-11431 each have an invoice VAT total EUR 0.01 lower than the sum of line VAT (Tom Reyes, checked the invoices, 2026-11-09 14:30 UTC)
- [Verified] Of 20 EUR invoices issued 2 to 9 Nov, 7 show a EUR 0.01 difference (5 lower, 2 higher) and 13 match; all 9 NOK invoices in the period match; 11 sampled GBP invoices match (Tom Reyes, invoice sample, 2026-11-09 14:30 UTC)
- [Verified] Reproduced in the customer's sandbox (copy of production settings): EUR invoice, 3 lines of EUR 10.33 at 20% VAT; line VAT 2.07 each, sum 6.21; invoice VAT total 6.20, which is 20% of 30.99 rounded. Same invoice in GBP gives 6.21 (Tom Reyes, sandbox reproduction, 2026-11-09 14:30 UTC)
- [Verified] In the sandbox, switching rounding to "per invoice" and back to "per line" made no change for EUR (Tom Reyes, sandbox, 2026-11-09 14:30 UTC)
- [Verified] Release notes for 8.2.4, deployed 2 Nov, say "Improved currency conversion precision for non-base-currency invoices." The link to this fault is not confirmed (Tom Reyes, release notes, 2026-11-09 14:30 UTC)
- [Verified] External audit on site 12 to 13 November 2026 (account record, flag noted by CSM Owen Pryce)
- [Reported] "Since your update last week, every multi-currency invoice we issue has the wrong VAT total" (Marta Kowalczyk, 2026-11-09 10:47 UTC)
- [Reported] About 140 invoices issued in EUR and NOK since 2 November (Marta Kowalczyk, 2026-11-09 10:47 UTC)
- [Reported] Auditors require VAT rounded line by line; per-invoice rounding is not acceptable to them (Marta Kowalczyk, 2026-11-09 10:47 and 15:30 UTC)
- [Reported] "Under our Enterprise contract you are required to fix this within 24 hours" (Marta Kowalczyk, 2026-11-09 10:47 UTC); not checked against the contract
- [Reported] Auditors are in on Thursday (Marta Kowalczyk, 2026-11-10 13:55 UTC); consistent with the account flag above
- Conflict: the customer reports every multi-currency invoice wrong, including NOK; the sample found 7 of 20 EUR invoices wrong and 0 of 9 NOK. The 140-invoice figure is therefore not a count of affected invoices; how many of the EUR invoices since 2 Nov are affected is not yet known.
- Conflict: the customer reports a contractual 24-hour fix term; no policy text was supplied to confirm or refute it, and Tom declined to confirm it (2026-11-10 09:10 UTC).

## Tried so far
- 2026-11-09 11:20 UTC, Tom Reyes: asked customer for example invoice numbers -> three EUR invoices supplied at 12:05 UTC
- 2026-11-09 14:30 UTC, Tom Reyes: checked the account rounding setting -> per line, last changed 14 March 2026
- 2026-11-09 14:30 UTC, Tom Reyes: checked the three example invoices -> each EUR 0.01 below sum of line VAT
- 2026-11-09 14:30 UTC, Tom Reyes: sampled invoices 2 to 9 Nov -> EUR 7 of 20 differ; NOK 0 of 9; GBP 0 of 11
- 2026-11-09 14:30 UTC, Tom Reyes: reproduced in sandbox with 3 x EUR 10.33 at 20% -> EUR VAT total 6.20 vs 6.21 line sum; GBP 6.21
- 2026-11-09 14:30 UTC, Tom Reyes: toggled sandbox rounding per invoice and back to per line -> no change for EUR
- 2026-11-09 14:30 UTC, Tom Reyes: read 8.2.4 release notes -> possible link, not confirmed
- 2026-11-09 14:45 UTC, Tom Reyes: offered per-invoice rounding as a workaround -> rejected by customer at 15:30 UTC (auditors)
- 2026-11-10 14:20 UTC, Tom Reyes: escalated to Tier 2 (Product Engineering Support), priority P2 -> result not recorded

## Commitments to the customer
- "I'm escalating the fault to our Product Engineering Support team today." (Tom Reyes, 2026-11-10 09:10 UTC), due today (10 Nov), met: escalated 2026-11-10 14:20 UTC
- "I'll ask engineering whether a fix would recalculate invoices already issued." (Tom Reyes, 2026-11-10 09:10 UTC), due not stated, open: included as an open ask in the escalation note, no answer yet
- "I'll send you a written summary of what we've reproduced, including the sandbox example, by 17:00 UK time today (Tuesday 10 November)." (Tom Reyes, 2026-11-10 09:10 UTC), due 17:00 UK time today (Tuesday 10 November), open: not sent as of 14:20 UTC per the escalation note; the customer asked again at 13:55 UTC ("Please make sure the summary arrives today")
- "I've asked your Customer Success Manager, Owen Pryce, to go through the service-level terms in your contract with you." (Tom Reyes, 2026-11-10 09:10 UTC), due not stated, open: no record in the thread that Owen Pryce has contacted the customer
- No fix date was promised: "I can't give you a fix date." (Tom Reyes, 2026-11-10 09:10 UTC). The 24-hour fix is the customer's claim about the contract, not a support commitment.

## Service level
- Plan: Quillbill Trade (annual subscription); support level Enterprise, "terms in Master Services Agreement, Schedule 3" (account record)
- Priority: P2 (set at ticket creation 2026-11-09 10:47 UTC, unchanged at escalation 2026-11-10 14:20 UTC). Whether the reported impact fits P2 is Undetermined: the policy's priority criteria were not supplied.
- Target: Undetermined; missing input: the text of MSA Schedule 3 (first response, update cadence and resolution targets for Enterprise P2). The customer's reported "fix this within 24 hours" is not a policy clause and is not used here.
- Clock: Undetermined; missing input: the policy's start event, business-hours and time-zone rules, and pause rules.
- Deadline: Undetermined as of now = 2026-11-10 14:20 UTC (latest timestamp in the thread; no "now" was given). For reference only: if the customer's reported 24-hour fix term applied from ticket creation, it would have passed at 2026-11-10 10:47 UTC; this assumes the customer's reading and clock start at ticket creation; the policy does not state this.

## Recommended next action
Make sure the written summary reaches Marta before 17:00 UK time today (17:00 UTC; the UK is on GMT in November). It is the nearest dated commitment, it has not been sent, the customer has chased it, and her auditors are on site Thursday 12 Nov. Everything it needs is already verified in Tom's 2026-11-09 14:30 UTC note (setting, three invoices, sample counts, sandbox example). Confirm with Tom whether he is sending it; if not, send it. Then turn the possible 8.2.4 link into a verified cause: check whether 8.2.4 changed VAT total calculation for non-base-currency invoices, and why EUR is affected while NOK is not.

Open questions:
- Did 8.2.4 cause this, and what in the EUR path bypasses per-line rounding while NOK (also non-base) does not?
- How many of the EUR invoices issued since 2 Nov have a VAT total that differs from the line sum? (The sample suggests about a third.)
- Will a fix recalculate invoices already issued, or must the customer raise credit notes? (Promised answer to customer.)
- What are the Enterprise P2 targets in MSA Schedule 3, and does it contain the 24-hour fix term the customer cites? (Owen Pryce is to go through this with the customer.)
- Is there an interim option acceptable to the auditors, given per-invoice rounding is ruled out?

Next customer update due: 17:00 UK time (17:00 UTC), Tuesday 10 November 2026, from Tom Reyes's commitment. Policy update cadence: Undetermined (policy not supplied).
