Clarifying question: Please supply the support policy, and the Enterprise service-level terms in the Master Services Agreement, Schedule 3, for account LMS-0855. Also, is this thread export complete, given that its last entry is 10 Nov 14:20 UTC? In particular, was the written summary promised for 10 Nov sent?

## Escalation handoff: QB-203977 Per-line VAT rounding not applied to some EUR invoices since about 2 Nov
As of: 2026-11-21 15:22 UTC (environment clock). The thread export's last entry is 2026-11-10 14:20 UTC.
Customer: Lindqvist Marine Supplies Ltd (LMS-0855). Plan Quillbill Trade (annual), support level Enterprise (MSA Schedule 3). Quillbill Invoicing (cloud), UK data region, plus a sandbox refreshed monthly from production settings. Base currency GBP; GBP, EUR and NOK enabled; VAT rounding per line (account record).

### Problem as currently understood
On some EUR invoices, the invoice VAT total does not equal the sum of the line VAT, even though the account is set to per-line rounding. Support reproduced it in the sandbox: on EUR invoices the VAT total appears to be calculated on the invoice net total, but GBP invoices are correct. About a third of the sampled EUR invoices are affected (7 of 20). No NOK or GBP invoices in the samples were affected. Support suspects release 8.2.4 (deployed 2 Nov), but has not confirmed the link. Confidence is high on the symptom and low on the cause.
Evidence:
- [Verified] Account setting "VAT rounding: per line" is on, last changed 14 March 2026 (Tom Reyes, 9 Nov 14:30; account record)
- [Verified] INV-LM-11402, -11417 and -11431 (EUR) each have an invoice VAT total EUR 0.01 below the sum of their line VAT (Tom Reyes, 9 Nov 14:30)
- [Verified] Sample of EUR invoices issued 2 to 9 Nov: 7 of 20 differ by 0.01 (5 lower, 2 higher) and 13 match. All 9 NOK invoices match, and all 11 sampled GBP invoices match (Tom Reyes, 9 Nov 14:30)
- [Verified] Sandbox repro: a EUR invoice with 3 lines of 10.33 at 20% VAT has line VAT of 2.07 each, summing to 6.21. The invoice VAT total shows 6.20, which is 20% of 30.99. The same invoice in GBP shows 6.21 (Tom Reyes, 9 Nov 14:30)
- [Verified] The 8.2.4 release notes, for the release deployed 2 Nov, say "Improved currency conversion precision for non-base-currency invoices". The causal link is not confirmed (Tom Reyes, 9 Nov 14:30)
- [Reported] "Every multi-currency invoice" has the wrong VAT total since last week's update. The samples contradict "every": NOK showed no difference and most EUR invoices matched (Marta Kowalczyk, 9 Nov 10:47)
- [Reported] About 140 EUR and NOK invoices issued since 2 Nov (Marta Kowalczyk, 9 Nov 10:47)
- [Reported] The customer's auditors require per-line rounding, so per-invoice rounding is not acceptable (Marta Kowalczyk, 9 Nov 10:47 and 15:30)

### Tried so far
- 9 Nov 14:30 Tom Reyes: checked the account rounding setting → per line, unchanged since 14 Mar [Verified]
- 9 Nov 14:30 Tom Reyes: checked the 3 customer invoices and sampled the EUR, NOK and GBP invoices → results above [Verified]
- 9 Nov 14:30 Tom Reyes: reproduced the problem in the sandbox (EUR wrong, GBP right) [Verified]
- 9 Nov 14:30 Tom Reyes: in the sandbox, switched rounding to "per invoice" and back to "per line" → no change for EUR [Verified]
- 9 Nov 14:45 Tom Reyes: offered per-invoice rounding as a workaround → customer rejected it because of auditor requirements [Reported]

### Commitments to the customer
- Written summary of findings, including the sandbox example, for the auditors ("by 17:00 UK time today (Tuesday 10 November)") | made by Tom Reyes, Support Agent Tier 1, on 10 Nov 09:10 UTC | due 10 Nov 17:00 UTC (UK is on GMT) | missed per the thread. At 14:20 the escalation note says "haven't sent yet", and the thread records no later send.
- Escalate the fault to Product Engineering Support "today" | made by Tom Reyes, Tier 1, on 10 Nov 09:10 UTC | due 10 Nov | met (escalated 10 Nov 14:20 UTC)
- "I'll ask engineering whether a fix would recalculate invoices already issued" (explicitly no promise that it will) | made by Tom Reyes, Tier 1, on 10 Nov 09:10 UTC | no time given | engineering was asked in the escalation note. No answer has been given to the customer, so this is open.
- The CSM, Owen Pryce, will "go through the service-level terms in your contract with you" | stated by Tom Reyes, Tier 1, on 10 Nov 09:10 UTC | no time given | open. Nothing in the thread shows it happened.
- Explicitly not promised: a fix date ("I can't give you a fix date") and the 24-hour fix (Tom Reyes, 10 Nov 09:10).

### Service level
Policy not supplied: no deadline computed.
- Priority P2 is set in the thread. It cannot be checked against policy definitions because the policy is not supplied.
- Plan Quillbill Trade, support level Enterprise, with custom terms in MSA Schedule 3. Those terms are not supplied, so every target is not computable.

### Recommended next action
Today (21 Nov), Tom Reyes (Tier 1) should confirm whether the written summary promised for 10 Nov 17:00 UTC was sent. If it was not, he should send it now with an apology, because that commitment is 10+ days overdue per the thread and the auditors' visit on 12 to 13 Nov has passed (account record).
Then:
- The engineer should find out why the per-line setting is ignored for EUR but not for GBP, and confirm or rule out 8.2.4 by checking EUR invoices issued before 2 Nov. The sandbox repro gives a deterministic test case. Also explain why NOK samples are unaffected.
- The engineer should answer whether a fix would recalculate invoices already issued, so the customer can decide on credit notes. Tom Reyes passes the answer to the customer.

### Gaps
- Support policy not supplied: no service-level targets, deadlines or statuses computed, and priority P2 not checked against policy definitions.
- MSA Schedule 3 (Enterprise service-level terms) not supplied.
- [Reported] commitment, not found in thread: the customer says the Enterprise contract requires a fix "within 24 hours" (Marta Kowalczyk, 9 Nov 10:47 and 15:30). This is unverified, and support declined to confirm it.
- Customer asks not agreed to: correction of issued invoices, and a fix date.
- The thread export ends 10 Nov 14:20 UTC, 11 days before the as-of time. Later contact, including whether the summary was sent and whether the CSM reviewed the terms, may be missing.
- Not verified: the link to 8.2.4, whether any affected invoices predate 2 Nov, the 140-invoice count, and whether any NOK invoices outside the sample are affected.
