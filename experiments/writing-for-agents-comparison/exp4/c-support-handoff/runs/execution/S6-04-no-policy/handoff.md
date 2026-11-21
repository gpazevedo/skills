## Escalation handoff: QB-203977 Per-line VAT rounding not applied to some EUR invoices since 8.2.4
As of: 2026-11-10 14:20 UTC (UK is on GMT, so 14:20 UK time)
Customer: Lindqvist Marine Supplies Ltd (LMS-0855), plan Quillbill Trade (annual), support level Enterprise (terms in MSA Schedule 3, not supplied), Quillbill Invoicing (cloud), UK data region, base currency GBP, EUR/NOK enabled, VAT rounding "per line" (account record). Sandbox is a monthly copy of production settings. Contact: Marta Kowalczyk, Finance Controller. CSM: Owen Pryce. Account flag: external audit on site 12-13 Nov 2026 (noted by CSM).

### Problem as currently understood
Some EUR invoices issued since 2 Nov have an invoice VAT total EUR 0.01 different from the sum of line VAT, although the account is set to per-line rounding. The leading explanation is that EUR invoices compute VAT on the invoice total rather than per line, possibly caused by release 8.2.4 (2 Nov). That link is unconfirmed. Confidence: symptom high, cause low.
Evidence:
- [Verified] INV-LM-11402, -11417, -11431 (EUR) each have invoice VAT total EUR 0.01 below the sum of line VAT (Tom Reyes, 9 Nov 14:30)
- [Verified] Sample of 20 EUR invoices issued 2-9 Nov: 7 differ by 0.01 (5 lower, 2 higher), 13 match (Tom Reyes, 9 Nov 14:30)
- [Verified] 9 NOK and 11 GBP invoices sampled: none differ (Tom Reyes, 9 Nov 14:30)
- [Verified] Reproduced in customer sandbox: EUR invoice, 3 lines of EUR 10.33 at 20% VAT; line VAT 2.07 each (sum 6.21), invoice VAT 6.20; same invoice in GBP gives 6.21 (Tom Reyes, 9 Nov 14:30)
- [Verified] Toggling the sandbox to "per invoice" and back to "per line" made no change for EUR (Tom Reyes, 9 Nov 14:30)
- [Verified] Account setting "VAT rounding: per line" is on, last changed 14 Mar 2026 (Tom Reyes, 9 Nov 14:30; account record)
- [Verified] 8.2.4 release note, deployed 2 Nov: "Improved currency conversion precision for non-base-currency invoices" (Tom Reyes, 9 Nov 14:30). That it caused the fault is [Reported] by support as a possibility, not confirmed.
- [Reported] About 140 EUR and NOK invoices issued since 2 Nov, and the customer claims every multi-currency invoice is wrong (Marta Kowalczyk). Support's sample found 7 of 20 EUR wrong and no NOK wrong, so this overstates it.
- [Reported] Customer's auditors require per-line rounding, so per-invoice rounding is not acceptable; auditors are in on Thursday 12 Nov (Marta Kowalczyk, 9 Nov 15:30 and 10 Nov 13:55)

### Tried so far
- 9 Nov Tom Reyes: checked the 3 named invoices → 0.01 difference confirmed [Verified]
- 9 Nov Tom Reyes: sampled 20 EUR, 9 NOK, 11 GBP invoices → 7 EUR differ, others none [Verified]
- 9 Nov Tom Reyes: reproduced in sandbox → reproduced on EUR, not GBP [Verified]
- 9 Nov Tom Reyes: toggled rounding setting per invoice and back in sandbox → no change for EUR [Verified]
- 9 Nov Tom Reyes: offered per-invoice rounding as a workaround → customer refused (auditors) [Reported by customer]
- Not recorded: whether the 8.2.4 change was checked in code or logs, why 13 of 20 EUR invoices are unaffected, or how many production invoices are affected in total.

### Commitments to the customer
- Escalate the fault to Product Engineering Support "today" | Tom Reyes, Tier 1 agent, 10 Nov 09:10 | due 10 Nov | met (escalated 14:20 UTC)
- Ask engineering whether a fix would recalculate issued invoices ("I can't promise that it will") | Tom Reyes, Tier 1 agent, 10 Nov 09:10 | no time given | open (question not yet put to engineering in the thread)
- Written summary of what has been reproduced, including the sandbox example | Tom Reyes, Tier 1 agent, 10 Nov 09:10 | due 17:00 UK time, Tue 10 Nov (17:00 UTC) | open, not yet sent, 2h40m remaining
- Ask CSM Owen Pryce to go through the contract service-level terms with the customer ("I've asked your Customer Success Manager") | Tom Reyes, Tier 1 agent, 10 Nov 09:10 | no time given | open, no reply from Owen in the thread
- Not a commitment: Tom did not confirm the 24-hour fix ("I can't give you a fix date"; "not able to confirm contract terms myself").

### Service level
- Policy not supplied: no deadline computed. The support policy was not supplied, and the account record points to MSA Schedule 3 for Enterprise terms, which is also not supplied.
- Priority is P2, set at ticket creation and unchanged. It cannot be checked against policy definitions.
- Customer claim, [Reported] and unchecked: "Under our Enterprise contract you are required to fix this within 24 hours" (Marta Kowalczyk, 9 Nov 10:47). Do not treat it as a deadline until the terms are seen. If it were true, 24h from 9 Nov 10:47 would already be past, so it matters which terms apply.
- Only dated deadline: the 17:00 UK summary above, which is our own promise and not a policy deadline.

### Recommended next action
Tom Reyes sends the customer the written summary by 17:00 UK time today (10 Nov), limited to the [Verified] findings above (sandbox example, sample results, no cause stated beyond "under investigation"). It is the only dated promise, auditors arrive in two days, and it needs no engineering answer. If Tier 2 wants anything changed in the wording, they need to say so before about 16:30.
Then: (1) Tier 2 engineer checks whether 8.2.4 changed per-line VAT handling for non-base-currency invoices, and why only some EUR invoices are affected; (2) Tier 2 gives Tom an answer on recalculating issued invoices, and a customer update, before the audit on 12 Nov.

### Gaps
- Support policy not supplied: priority definitions, response, update and resolution targets and clock rules unknown; no deadline computed.
- MSA Schedule 3 (Enterprise terms) not supplied; the 24-hour claim cannot be checked. Owen Pryce has not yet confirmed the terms to the customer.
- Cause is unconfirmed; the 8.2.4 link is a possibility only.
- Total number of affected production invoices is unknown (customer says about 140; support sampled only 20 EUR).
- Whether a fix would recalculate issued invoices, and how the customer would otherwise correct them (credit notes were raised by the customer as a question), is unanswered.
- Priority P2 not validated; customer impact (audit on 12 Nov) may be relevant to it once the policy is seen.
