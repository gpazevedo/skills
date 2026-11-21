Clarifying question: The support policy was not supplied, and the account record says the Enterprise terms are in "Master Services Agreement, Schedule 3", which was not supplied either. Can you provide the support policy or MSA Schedule 3 so the service-level target, clock rule and deadline can be filled in? (No answer was available; the handoff below marks every service-level term as not stated.)

# Escalation handoff: QB-203977, Lindqvist Marine Supplies Ltd (LMS-0855)

**In one line:** Since release 8.2.4 (2 Nov), some EUR invoices show an invoice VAT total that is 0.01 off the sum of line VAT, even though the account uses per-line rounding. The most urgent constraint is Tom Reyes's promised written summary for the customer's auditors, due 17:00 UK time (17:00 UTC) on Tue 10 Nov and not yet sent at escalation. The auditors are on site 12 to 13 Nov.

## Problem as currently understood
- [verified] Account VAT rounding is set to "per line" (evidence: Tom Reyes checked the account setting, internal note 2026-11-09 14:30 UTC: "VAT rounding: per line", last changed 14 March 2026; account record: "VAT rounding per line").
- [verified] Base currency is GBP; invoice currencies enabled are GBP, EUR, NOK (account record).
- [verified] Invoices INV-LM-11402, INV-LM-11417 and INV-LM-11431 (all EUR) each have an invoice VAT total EUR 0.01 lower than the sum of their line VAT (evidence: Tom Reyes examined the three invoices, internal note 2026-11-09 14:30 UTC, "Confirmed").
- [verified] In a sample of 20 EUR invoices issued 2 to 9 Nov, 7 show a 0.01 difference (5 lower, 2 higher) and 13 match. All 9 NOK invoices in the same period match. 11 sampled GBP invoices match (evidence: Tom Reyes sample, internal note 2026-11-09 14:30 UTC).
- [verified] Reproduced in the customer's sandbox (copy of production settings): new EUR invoice, 3 lines of EUR 10.33 at 20% VAT. Line VAT 2.07 each, sum 6.21. Invoice VAT total shows 6.20, which equals 20% of 30.99 rounded. The same invoice in GBP shows 6.21 (evidence: Tom Reyes, internal note 2026-11-09 14:30 UTC).
- [verified] In the sandbox, switching the rounding setting to "per invoice" and back to "per line" made no change for EUR (evidence: Tom Reyes, internal note 2026-11-09 14:30 UTC).
- [verified] Release 8.2.4 was deployed 2 Nov; its release notes say "Improved currency conversion precision for non-base-currency invoices." (evidence: Tom Reyes read the release notes, internal note 2026-11-09 14:30 UTC).
- [reported] The problem started "since your update last week" and "every multi-currency invoice we issue has the wrong VAT total" (source: Marta Kowalczyk, customer, 2026-11-09 10:47 UTC).
- [reported] About 140 invoices in EUR and NOK issued since 2 November (source: Marta Kowalczyk, 2026-11-09 10:47 UTC). Not checked by support.
- [reported] The customer's auditors require per-line VAT rounding, so per-invoice rounding is not an acceptable workaround (source: Marta Kowalczyk, 2026-11-09 10:47 and 15:30 UTC).
- [reported] "Under our Enterprise contract you are required to fix this within 24 hours." (source: Marta Kowalczyk, 2026-11-09 10:47 UTC). Not confirmed by support; see Service level.
- [verified] External audit on site 12 to 13 November 2026 (account record flag, noted by CSM; customer also says "Our auditors are in on Thursday", 2026-11-10 13:55 UTC).
- [suspected] On EUR invoices the VAT total is calculated on the invoice total rather than line by line, ignoring the per-line setting (held by: Tom Reyes; basis: sandbox reproduction where the total equals invoice-level rounding, and the mixed 5 lower / 2 higher differences, which fit invoice-level rounding).
- [suspected] The fault was introduced by 8.2.4's currency-conversion change (held by: Tom Reyes, "Possible link; not confirmed"; basis: timing matches the customer's report and the release note mentions non-base-currency invoices). Unexplained: NOK is also a non-base currency but none of the 9 NOK invoices differ.
- Conflicts:
  - Customer says "every multi-currency invoice" is wrong; Tom's sample found 7 of 20 EUR invoices wrong and 0 of 9 NOK.
  - Customer says "Enterprise contract" with a 24-hour fix obligation; account record says plan "Quillbill Trade", support level "Enterprise (terms in Master Services Agreement, Schedule 3)". The 24-hour term cannot be checked because neither the policy nor Schedule 3 was supplied.

## Tried so far
| What was tried | Who, when | Result |
|---|---|---|
| Asked customer for example invoice numbers | Tom Reyes, 2026-11-09 11:20 UTC | Customer sent INV-LM-11402, INV-LM-11417, INV-LM-11431 (all EUR), 12:05 UTC |
| Checked account VAT rounding setting | Tom Reyes, by 2026-11-09 14:30 UTC | "Per line", last changed 14 March 2026 |
| Examined the three customer invoices | Tom Reyes, by 2026-11-09 14:30 UTC | Each invoice VAT total EUR 0.01 below sum of line VAT |
| Sampled invoices issued 2 to 9 Nov | Tom Reyes, by 2026-11-09 14:30 UTC | EUR: 7 of 20 differ (5 lower, 2 higher). NOK: 0 of 9. GBP: 0 of 11 |
| Reproduced in sandbox, EUR vs GBP | Tom Reyes, by 2026-11-09 14:30 UTC | EUR total 6.20 vs line sum 6.21; GBP total 6.21 |
| Toggled rounding setting per invoice and back in sandbox | Tom Reyes, by 2026-11-09 14:30 UTC | No change for EUR |
| Reviewed 8.2.4 release notes | Tom Reyes, by 2026-11-09 14:30 UTC | Currency conversion precision change for non-base-currency invoices; link not confirmed |
| Offered per-invoice rounding as workaround | Tom Reyes, 2026-11-09 14:45 UTC | Rejected by customer (auditors), 15:30 UTC |
| Asked CSM Owen Pryce to go through contract service-level terms with customer | Tom Reyes, by 2026-11-10 09:10 UTC | No result recorded |
| Escalated to Tier 2 (Product Engineering Support), P2 | Tom Reyes, 2026-11-10 14:20 UTC | Status Escalated; this handoff |

## Commitments to the customer
| Commitment (quoted) | Made by | When | Due | Status |
|---|---|---|---|---|
| "I'm escalating the fault to our Product Engineering Support team today." | Tom Reyes (Tier 1) | 2026-11-10 09:10 UTC | 2026-11-10 | Met (escalated 2026-11-10 14:20 UTC) |
| "I'll ask engineering whether a fix would recalculate invoices already issued. I can't promise that it will, so please don't hold off on anything your auditors need." | Tom Reyes (Tier 1) | 2026-11-10 09:10 UTC | No date given | No date given. The question is listed in the escalation note as an open ask; no answer yet |
| "I'll send you a written summary of what we've reproduced, including the sandbox example, by 17:00 UK time today (Tuesday 10 November)." | Tom Reyes (Tier 1) | 2026-11-10 09:10 UTC | 2026-11-10 17:00 UK time (17:00 UTC; UK is on GMT in November) | Pending as of 2026-11-10 14:20 UTC, 2 h 40 min remaining; escalation note says "haven't sent yet". Overdue if not sent by 17:00 UTC |
| "I've asked your Customer Success Manager, Owen Pryce, to go through the service-level terms in your contract with you." | Tom Reyes (Tier 1), on behalf of Owen Pryce (CSM) | 2026-11-10 09:10 UTC | No date given | No date given; no contact from Owen recorded |

Not commitments: Tom explicitly said "I can't give you a fix date" and "I'm not able to confirm contract terms myself" (2026-11-10 09:10 UTC). The customer's requests for a fix within 24 hours, for correction of issued invoices, and for confirmation of the 24 hours were not agreed to.

## Service level
- Tier: Enterprise (account record: "Support level: Enterprise (terms in Master Services Agreement, Schedule 3)")
- Priority/severity: P2 (ticket fields, 2026-11-09 10:47 UTC; unchanged at escalation 2026-11-10 14:20 UTC)
- Target: not stated in support policy (policy not supplied); account record points to MSA Schedule 3, not supplied. The customer's "within 24 hours" is reported only and was not confirmed by support.
- Clock rule: not stated in support policy (policy not supplied)
- Deadline: not determinable (no target or clock rule supplied)
- Status: not determinable, as of 2026-11-10 14:20 UTC (last thread timestamp, used as "now" because no current time was supplied; the session date is 2026-11-21, and if that is the real "now" the summary commitment above is overdue unless it was sent outside this thread)

## Recommended next action
First, before 17:00 UTC on 10 Nov: make sure Tom Reyes (or you) sends the promised written summary. Its content already exists in Tom's 2026-11-09 14:45 UTC message plus the sandbox example in the 14:30 UTC internal note. It should state what is verified and that the cause is not yet confirmed. The auditors arrive 12 Nov.

Then, the engineering check: in the customer's sandbox, create the same invoice Tom used (3 lines of 10.33 at 20% VAT) in NOK, and compare the invoice VAT total with the sum of line VAT (6.21).
- If NOK shows 6.20: the fault affects all non-base-currency invoices, which fits the 8.2.4 release note. The NOK sample was simply too small to hit a rounding edge, so the customer's NOK invoices are also at risk and the scope of "invoices already issued" grows. Next, diff the 8.2.4 non-base-currency VAT path against 8.2.3.
- If NOK shows 6.21: the fault is EUR-specific, which weakens the generic 8.2.4 theory. Next, look for EUR-specific handling (currency configuration, conversion rate precision for EUR) and check EUR invoices issued before 2 Nov for the same mismatch to test whether 8.2.4 is the trigger.

Either result also feeds the open question of whether a fix will recalculate issued invoices, which the customer needs before the audit.

## Gaps
- Support policy not supplied; MSA Schedule 3 not supplied. Target, clock rule, deadline and SLA status cannot be established. The customer's 24-hour claim is unverified; if it were a real term counted from ticket creation (2026-11-09 10:47 UTC), it would have elapsed at 2026-11-10 10:47 UTC, but nothing in the supplied material supports that term.
- No record of whether Owen Pryce has contacted the customer about contract terms.
- Customer's "about 140 invoices" not checked; the full count of affected EUR (and possibly NOK) invoices since 2 Nov is unknown.
- No check of invoices issued before 2 Nov, so the link to 8.2.4 is timing-based only.
- Why NOK shows no differences while also being a non-base currency is unexplained.
- No answer yet on whether a fix will recalculate issued invoices or whether the customer must raise credit notes.
- Erik Lindqvist (Director) is the contract contact per the account record; he has not been involved in the thread.
