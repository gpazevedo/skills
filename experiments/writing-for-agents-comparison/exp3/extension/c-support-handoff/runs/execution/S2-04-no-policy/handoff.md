Clarifying question:
1. The support policy (the Enterprise service-level terms, "Master Services Agreement, Schedule 3" per the account record) was not supplied with the case. Can you provide it?
2. What is the current date, time and time zone, so the commitment and service-level clocks can be measured?

No answer was available; the handoff below records both as gaps and gives time-dependent statuses conditionally.

# Escalation handoff: QB-203977 Per-line VAT rounding not applied to some EUR invoices (invoice VAT total off by EUR 0.01)

**Customer:** Lindqvist Marine Supplies Ltd, account LMS-0855, plan "Quillbill Trade (annual subscription)", support level "Enterprise (terms in Master Services Agreement, Schedule 3)" (account record: Plan, Support level)   **Severity/priority:** P2 (ticket event 2026-11-09 10:47 UTC "Priority: P2"; unchanged at escalation event 2026-11-10 14:20 UTC). What P2 means under the policy: Not determinable (policy not supplied).
**Most urgent deadline:** Written summary for the customer's auditors, promised "by 17:00 UK time today (Tuesday 10 November)" = 2026-11-10 17:00 UTC (UK is on GMT in November, so UK time = UTC). Promised by Tom Reyes, 2026-11-10 09:10 UTC; not sent as of the last thread entry (escalation note, 2026-11-10 14:20 UTC). The customer's external audit is on site 12 to 13 November 2026 (account record, Account flags).

## Problem as currently understood
Since about 2 November 2026, some EUR invoices on an account set to per-line VAT rounding show an invoice VAT total EUR 0.01 different from the sum of the line VAT; support has confirmed this on 7 of 20 sampled EUR invoices and reproduced it in the customer's sandbox, but found no differences on sampled NOK or GBP invoices. Tier 1's untested explanation is that per-line rounding is not applied to EUR invoices (VAT is computed on the invoice total), possibly introduced by release 8.2.4 (deployed 2 Nov). The customer cannot use per-invoice rounding because of its auditors, and is asking for a fix, an answer on whether issued invoices will be corrected, and a written summary for an audit on 12 November.

| Fact | Status | How established / cite |
|---|---|---|
| Account is set to per-line VAT rounding ("VAT rounding: per line"), last changed 14 March 2026 | Verified | Tom Reyes checked the account setting, internal note 2026-11-09 14:30 UTC; also account record, VAT settings: "VAT rounding per line" |
| Account base currency is GBP; invoice currencies enabled are GBP, EUR, NOK | Verified | Account record, Base currency and Invoice currencies enabled |
| Invoices INV-LM-11402, INV-LM-11417, INV-LM-11431 (all EUR) each have an invoice VAT total EUR 0.01 lower than the sum of line VAT | Verified | Tom Reyes checked the three invoices, internal note 2026-11-09 14:30 UTC ("Confirmed"); invoice numbers from Marta Kowalczyk, 2026-11-09 12:05 UTC |
| Of 20 EUR invoices issued 2 to 9 Nov, 7 show a 0.01 difference (5 lower, 2 higher) and 13 match | Verified | Tom Reyes sample, internal note 2026-11-09 14:30 UTC |
| All 9 NOK invoices issued 2 to 9 Nov show no difference | Verified | Tom Reyes check, internal note 2026-11-09 14:30 UTC |
| 11 sampled GBP invoices show no difference | Verified | Tom Reyes sample, internal note 2026-11-09 14:30 UTC |
| Sandbox reproduction: new EUR invoice, 3 lines of EUR 10.33 at 20% VAT; line VAT 2.07 each, sum 6.21; invoice VAT total shows 6.20 (20% of 30.99 rounded). Same invoice in GBP: VAT total 6.21 | Verified | Reproduced by Tom Reyes in the customer's sandbox ("copy of production settings"), internal note 2026-11-09 14:30 UTC |
| In the sandbox, switching rounding to "per invoice" and back to "per line" made no change for EUR | Verified | Tom Reyes test, internal note 2026-11-09 14:30 UTC |
| Release notes for 8.2.4, deployed 2 Nov, say "Improved currency conversion precision for non-base-currency invoices." | Verified | Tom Reyes read the release notes, internal note 2026-11-09 14:30 UTC |
| Per-line rounding is not applied to EUR invoices; VAT total is calculated on the invoice total | Hypothesis | Tom Reyes, internal note 2026-11-09 14:30 UTC ("Looks like..."); stated to customer as "seems to be" 2026-11-09 14:45 UTC. Untested beyond the one sandbox case; does not yet explain why 13 of 20 EUR invoices match or why NOK (also non-base) is unaffected |
| The fault was introduced by release 8.2.4 | Hypothesis | Tom Reyes, internal note 2026-11-09 14:30 UTC ("Possible link; not confirmed"). The escalation note 2026-11-10 14:20 UTC states "since 8.2.4 (2 Nov)" as if established; no test is recorded |
| The problem started "since your update last week" / since 2 November | Reported | Marta Kowalczyk, 2026-11-09 10:47 UTC. Support sampled only invoices issued 2 to 9 Nov; no pre-2 Nov invoices were checked |
| "Every multi-currency invoice we issue has the wrong VAT total" | Reported | Marta Kowalczyk, 2026-11-09 10:47 UTC. Contradicted by support's sample (see disagreements) |
| About 140 invoices issued in EUR and NOK since 2 November | Reported | Marta Kowalczyk, 2026-11-09 10:47 UTC. Not counted by support |
| The customer's auditors require VAT rounded line by line; per-invoice rounding is not acceptable to them | Reported | Marta Kowalczyk, 2026-11-09 10:47 UTC and 15:30 UTC |
| Impact: customer has "no confidence in any of" the invoices issued since 2 Nov | Reported | Marta Kowalczyk, 2026-11-09 10:47 UTC |
| Customer's auditors are on site Thursday 12 November | Verified | Account record, Account flags: "External audit on site 12 to 13 November 2026 (noted by CSM)"; also Marta Kowalczyk, 2026-11-10 13:55 UTC |
| The Enterprise contract requires a fix within 24 hours | Reported | Marta Kowalczyk, 2026-11-09 10:47 UTC, repeated 15:30 UTC. Not confirmed by support (Tom Reyes, 2026-11-10 09:10 UTC); cannot be checked because the policy was not supplied |
| Prior ticket QB-196320 (P3, NOK currency formatting on PDF invoices) resolved 21 August 2026 | Verified | Account record, Recent tickets |

**Open disagreements:**
- Scope: the customer reports "every multi-currency invoice" (about 140 in EUR and NOK) has the wrong VAT total; support found 7 of 20 EUR invoices affected and 0 of 9 NOK invoices (2026-11-09 14:30 UTC internal note; told to customer 14:45 UTC). The customer has not responded to this finding directly.
- Contract terms: the customer states the Enterprise contract requires a fix within 24 hours; support has not confirmed it (Tom Reyes, 2026-11-10 09:10 UTC), and the policy is not available to check.
- Internal: Tom's 14:30 UTC note calls the 8.2.4 link "not confirmed"; his escalation note at 14:20 UTC on 10 Nov states it as the onset without a recorded test.

## What has been tried
| When | Who | Action | Result | Cite |
|---|---|---|---|---|
| 2026-11-09 11:20 UTC | Tom Reyes (Tier 1) | Asked the customer for two or three affected invoice numbers | Customer supplied INV-LM-11402, INV-LM-11417, INV-LM-11431 (all EUR) | Tom Reyes 11:20 UTC; Marta Kowalczyk 12:05 UTC |
| By 2026-11-09 14:30 UTC | Tom Reyes | Checked account VAT rounding setting | "per line" is on; last changed 14 March 2026 | Internal note 2026-11-09 14:30 UTC |
| By 2026-11-09 14:30 UTC | Tom Reyes | Checked the three customer invoices | Each invoice VAT total EUR 0.01 lower than sum of line VAT | Internal note 2026-11-09 14:30 UTC |
| By 2026-11-09 14:30 UTC | Tom Reyes | Sampled invoices issued 2 to 9 Nov: 20 EUR, all 9 NOK, 11 GBP | EUR: 7 differ by 0.01 (5 lower, 2 higher), 13 match. NOK: none differ. GBP: none differ | Internal note 2026-11-09 14:30 UTC |
| By 2026-11-09 14:30 UTC | Tom Reyes | Reproduced in customer sandbox: EUR invoice, 3 lines of EUR 10.33 at 20%; same invoice in GBP | EUR VAT total 6.20 vs line sum 6.21; GBP VAT total 6.21 | Internal note 2026-11-09 14:30 UTC |
| By 2026-11-09 14:30 UTC | Tom Reyes | In sandbox, switched rounding to "per invoice" and back to "per line" | No change for EUR | Internal note 2026-11-09 14:30 UTC |
| By 2026-11-09 14:30 UTC | Tom Reyes | Reviewed release notes for 8.2.4 | Possible link to "Improved currency conversion precision for non-base-currency invoices"; not confirmed | Internal note 2026-11-09 14:30 UTC |
| 2026-11-09 14:45 UTC | Tom Reyes | Offered workaround: switch to per-invoice rounding | Rejected by customer: "per-invoice rounding isn't acceptable to our auditors" | Tom Reyes 14:45 UTC; Marta Kowalczyk 15:30 UTC |
| Before 2026-11-10 09:10 UTC | Tom Reyes | Asked CSM Owen Pryce to go through the contract's service-level terms with the customer | Not recorded | Tom Reyes 2026-11-10 09:10 UTC ("I've asked your Customer Success Manager...") |
| 2026-11-10 14:20 UTC | Tom Reyes | Escalated to Tier 2 (Product Engineering Support), with open asks: fix; whether issued invoices will be recalculated; written summary | Status Open → Escalated; no Tier 2 response recorded | Event and escalation note 2026-11-10 14:20 UTC |

## Commitments to the customer
| Commitment (verbatim) | Made by (role) | When / cite | Deadline | Kept / Open / Missed |
|---|---|---|---|---|
| "I'm escalating the fault to our Product Engineering Support team today." | Tom Reyes (Support Agent, Tier 1) | 2026-11-10 09:10 UTC | End of 2026-11-10 | Kept: escalated 2026-11-10 14:20 UTC (event) |
| "I'll ask engineering whether a fix would recalculate invoices already issued." | Tom Reyes (Tier 1) | 2026-11-10 09:10 UTC | None set | Kept as to asking: the question is in the escalation note to Tier 2, 2026-11-10 14:20 UTC. No answer has gone back to the customer |
| "I'll send you a written summary of what we've reproduced, including the sandbox example, by 17:00 UK time today (Tuesday 10 November)." | Tom Reyes (Tier 1) | 2026-11-10 09:10 UTC | 2026-11-10 17:00 UTC (GMT = UTC) | Not sent as of 2026-11-10 14:20 UTC (escalation note: "haven't sent yet"). Open if the current time is before 2026-11-10 17:00 UTC; Missed if after and no later message shows it sent. Current time not supplied. Customer reinforced it: "Please make sure the summary arrives today" (2026-11-10 13:55 UTC) |
| "I've asked your Customer Success Manager, Owen Pryce, to go through the service-level terms in your contract with you." | Tom Reyes (Tier 1) | 2026-11-10 09:10 UTC | None set | Open: no record that Owen Pryce has contacted the customer |

Whether any of these exceeds what the policy allows a Tier 1 agent: Not determinable (policy not supplied). Tom explicitly declined to commit to a fix date ("I can't give you a fix date"), to recalculation ("I can't promise that it will"), and to the 24-hour term ("I'm not able to confirm contract terms myself"), all 2026-11-10 09:10 UTC.

## Service-level status
| Clock | Policy clause (quoted) | Started | Deadline (with arithmetic) | Status |
|---|---|---|---|---|
| All clocks (first response, update interval, resolution, or whatever the policy defines) | Not determinable: support policy ("Master Services Agreement, Schedule 3") not supplied | Ticket created 2026-11-09 10:47 UTC (event); first reply to customer 2026-11-09 11:20 UTC (33 minutes after creation); last update to customer 2026-11-10 09:10 UTC | Not determinable: missing the policy's clock definitions and P2 targets for Enterprise, and any pause or business-hours rule | Not determinable: also missing the current time |

## Recommended next action
Test the two Hypotheses that the fix depends on: run Tom's sandbox case (3 lines of 10.33 at 20% VAT, per-line rounding) in EUR, NOK and GBP on a build before 8.2.4 and on 8.2.4, and inspect what 8.2.4 changed in the VAT-total calculation for non-base-currency invoices.

Evidence: EUR invoices on a per-line account show invoice VAT totals off by 0.01 since about 2 Nov (Verified, 7 of 20 sampled, sandbox reproduction); GBP does not (Verified); 8.2.4, deployed 2 Nov, changed "currency conversion precision for non-base-currency invoices" (Verified release note text); but the causal link and the "computed on invoice total" mechanism are only Hypothesis, and NOK, also non-base, showed no differences in 9 invoices.

What it settles: whether 8.2.4 caused the fault; whether it affects all non-base currencies or only EUR; and therefore which issued invoices are affected (needed for the customer's question on recalculation versus credit notes) and what the fix must change.

Deadline to beat: the written summary promised by 2026-11-10 17:00 UTC (Tom Reyes, 2026-11-10 09:10 UTC), which covers what has already been reproduced and does not need to wait for this test; and the customer's audit on site from 12 November 2026 (account record, Account flags), before which the customer wants the summary and an answer on correcting issued invoices.

## Gaps
- Support policy missing: the Enterprise terms ("Master Services Agreement, Schedule 3") were not supplied, so every service-level clock, the meaning of P2, and whether any commitment exceeds Tier 1 authority are Not determinable. Closed by obtaining Schedule 3. If it confirms the customer's reported 24-hour fix term starting at ticket creation, that deadline would have been 2026-11-09 10:47 UTC + 24 h = 2026-11-10 10:47 UTC, already past at escalation; this is conditional on an unconfirmed customer claim.
- Current time and time zone not supplied: the written-summary commitment cannot be marked Open or Missed. Closed by the current time plus any thread entries after 2026-11-10 14:20 UTC.
- Written summary: no record it was sent. Closed by checking outbound messages after 2026-11-10 14:20 UTC.
- CSM follow-up: no record that Owen Pryce was asked or has contacted the customer about service-level terms. Closed by confirming with Owen Pryce.
- Tier 2 response: none recorded since escalation at 2026-11-10 14:20 UTC.
- Full scope unknown: only 20 of the EUR invoices since 2 Nov were checked; the customer's figure of about 140 EUR and NOK invoices is unverified, and no invoices before 2 Nov were checked to confirm onset. Closed by checking every EUR and NOK invoice issued since 2 Nov (and a sample before it) for line-VAT sum versus invoice VAT total.
- NOK not tested in the sandbox: NOK's clean result rests on 9 production invoices only.
- Recalculation question unanswered: whether a fix would recalculate issued invoices, or the customer must raise credit notes, is with engineering.
