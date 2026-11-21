Clarifying question: Please supply the support policy that applies to this account (the account record points to Master Services Agreement, Schedule 3, for Enterprise support terms). Without it no service-level target, clock rule or priority definition can be applied, and the customer's "24 hours" claim cannot be checked.

# Escalation handoff: QB-203977 | Lindqvist Marine Supplies Ltd | Per-line VAT rounding not applied to some EUR invoices

**Service level:** Not determined: no policy supplied | Nearest known time limit is a support-side commitment, not a policy term: written summary promised by 17:00 UK time (17:00 UTC) on Tuesday 10 November 2026, Outstanding, 2 h 40 min left as of the latest thread timestamp.

## Problem as currently understood
On some EUR invoices issued since 2 November 2026, the invoice VAT total differs by EUR 0.01 from the sum of the line VAT, even though the account is set to per-line VAT rounding (Verified, Tom Reyes, 2026-11-09 14:30 UTC). Tom Reyes reproduced it in the customer's sandbox, where the EUR invoice VAT total matches VAT calculated on the invoice total rather than per line, while the same invoice in GBP is correct (Verified). No differences were found in sampled NOK or GBP invoices, which contradicts the customer's report that every multi-currency invoice is affected (Verified sample vs Reported claim). The link to release 8.2.4, deployed 2 November, is Suspected and untested.

| Statement | Label | Source (author, timestamp) |
| --- | --- | --- |
| Every multi-currency invoice issued since "your update last week" has the wrong VAT total; invoice VAT does not equal the sum of line VAT | Reported | Marta Kowalczyk, 2026-11-09 10:47 UTC |
| About 140 invoices issued in EUR and NOK since 2 November | Reported | Marta Kowalczyk, 2026-11-09 10:47 UTC |
| The customer's auditors require line-by-line VAT rounding; per-invoice rounding is not acceptable to them | Reported | Marta Kowalczyk, 2026-11-09 10:47 UTC and 15:30 UTC |
| Account setting "VAT rounding: per line" is on; last changed 14 March 2026 | Verified | Tom Reyes, internal note, 2026-11-09 14:30 UTC |
| INV-LM-11402, INV-LM-11417 and INV-LM-11431 (EUR) each have an invoice VAT total EUR 0.01 lower than the sum of line VAT | Verified | Tom Reyes, internal note, 2026-11-09 14:30 UTC (invoice numbers from Marta Kowalczyk, 12:05 UTC) |
| Of 20 EUR invoices issued 2 to 9 November, 7 differ by EUR 0.01 (5 lower, 2 higher) and 13 match | Verified | Tom Reyes, internal note, 2026-11-09 14:30 UTC |
| All 9 NOK invoices issued 2 to 9 November and 11 sampled GBP invoices show no difference | Verified | Tom Reyes, internal note, 2026-11-09 14:30 UTC |
| Sandbox reproduction: EUR invoice, 3 lines of EUR 10.33 at 20% VAT; line VAT 2.07 each, sum 6.21; invoice VAT total 6.20 (20% of 30.99 rounded). Same invoice in GBP: VAT total 6.21 | Verified | Tom Reyes, internal note, 2026-11-09 14:30 UTC |
| Per-line rounding is not applied to EUR invoices (VAT calculated on invoice total) | Suspected (explanation drawn from the sandbox case; not tested beyond it, and does not yet explain why only some EUR invoices and no NOK invoices differ) | Tom Reyes, 2026-11-09 14:30 UTC and 14:45 UTC |
| Cause is release 8.2.4 (deployed 2 November), release note: "Improved currency conversion precision for non-base-currency invoices." | Suspected (Tom Reyes wrote "Possible link; not confirmed"; the escalation note states "since 8.2.4" without new evidence) | Tom Reyes, 2026-11-09 14:30 UTC and 2026-11-10 14:20 UTC |

## What has been tried
| Action | By | When | Result | Label |
| --- | --- | --- | --- | --- |
| Checked account VAT rounding setting | Tom Reyes (Tier 1) | 2026-11-09 14:30 UTC | "Per line" is on, last changed 14 March 2026 | Verified |
| Checked the three customer-supplied EUR invoices | Tom Reyes (Tier 1) | 2026-11-09 14:30 UTC | Each invoice VAT total EUR 0.01 below the sum of line VAT | Verified |
| Sampled invoices issued 2 to 9 November (20 EUR, 9 NOK, 11 GBP) | Tom Reyes (Tier 1) | 2026-11-09 14:30 UTC | EUR: 7 of 20 differ by EUR 0.01 (5 lower, 2 higher). NOK and GBP: none differ | Verified |
| Reproduced in customer's sandbox with a new 3-line EUR invoice, and the same invoice in GBP | Tom Reyes (Tier 1) | 2026-11-09 14:30 UTC | EUR VAT total 6.20 vs line sum 6.21; GBP VAT total 6.21 | Verified |
| In sandbox, switched rounding to "per invoice" and back to "per line" | Tom Reyes (Tier 1) | 2026-11-09 14:30 UTC | No change for EUR | Verified |
| Reviewed 8.2.4 release notes | Tom Reyes (Tier 1) | 2026-11-09 14:30 UTC | Note on currency conversion precision for non-base-currency invoices; possible link, not confirmed | Suspected |
| Offered workaround: switch to per-invoice rounding | Tom Reyes (Tier 1) | 2026-11-09 14:45 UTC | Rejected by customer at 15:30 UTC (auditors require per-line rounding) | Reported |
| Escalated to Tier 2 (Product Engineering Support) | Tom Reyes (Tier 1) | 2026-11-10 14:20 UTC | Status Open to Escalated; priority kept at P2 | Verified |

## Commitments to the customer
| Commitment (quoted) | Made by (name, role) | When | Due | Status |
| --- | --- | --- | --- | --- |
| "I've started looking at this." | Tom Reyes, Support Agent, Tier 1 | 2026-11-09 11:20 UTC | No date given | Kept (investigation recorded at 14:30 UTC) |
| "I'm escalating the fault to our Product Engineering Support team today." | Tom Reyes, Support Agent, Tier 1 | 2026-11-10 09:10 UTC | 2026-11-10 ("today") | Kept (escalated 2026-11-10 14:20 UTC) |
| "I'll ask engineering whether a fix would recalculate invoices already issued." | Tom Reyes, Support Agent, Tier 1 | 2026-11-10 09:10 UTC | No date given | Outstanding (listed as an open ask in the escalation note) |
| "I'll send you a written summary of what we've reproduced, including the sandbox example, by 17:00 UK time today (Tuesday 10 November)." | Tom Reyes, Support Agent, Tier 1 | 2026-11-10 09:10 UTC | 2026-11-10 17:00 UK time (17:00 UTC, UK on GMT) | Outstanding (escalation note at 14:20 UTC: "haven't sent yet") |
| "I've asked your Customer Success Manager, Owen Pryce, to go through the service-level terms in your contract with you." | Tom Reyes, Support Agent, Tier 1 | 2026-11-10 09:10 UTC | No date given | Outstanding (no record in the thread that Owen Pryce has contacted the customer) |

Claimed by the customer but not found in the thread: that under the Enterprise contract support is "required to fix this within 24 hours" (Marta Kowalczyk, 2026-11-09 10:47 UTC, repeated 15:30 UTC). No support-side message confirms it; Tom Reyes declined to confirm contract terms (2026-11-10 09:10 UTC). Tom Reyes also stated "I can't give you a fix date" and "I can't promise that it will [recalculate issued invoices]"; these are explicitly not commitments.

## Service level
- Tier: Enterprise support level, Quillbill Trade plan (account record LMS-0855; terms in Master Services Agreement, Schedule 3, not supplied)
- Priority: P2 (recorded at creation 2026-11-09 10:47 UTC and at escalation 2026-11-10 14:20 UTC)
- Targets: Not determined: no policy supplied. The only deadline in the thread, "fix this within 24 hours", is a statement by the customer (Marta Kowalczyk, 2026-11-09 10:47 UTC), not a verified term.
- Time zones: all thread timestamps are UTC (stated in the export header).
- Status as of: 2026-11-10 14:20 UTC (latest timestamp in the thread)

## Recommended next action
The Tier 2 engineer should confirm with Tom Reyes (Tier 1) that the promised written summary goes to Marta Kowalczyk before 17:00 UTC today, limited to the Verified findings above and stating that the 8.2.4 link is unconfirmed, because it is the nearest outstanding commitment and the customer's auditors arrive Thursday 12 November. If the summary has already been sent, the next step is for Tier 2 to test the Suspected 8.2.4 cause by running the sandbox EUR example on a pre-8.2.4 build and finding why some EUR invoices differ while NOK invoices do not.

## Open questions
- Support policy missing: please supply the policy (MSA Schedule 3, Enterprise terms) so service-level targets, clock rules and the meaning of P2 can be applied. All service-level deadlines are blocked until then.
- Customer claims a contractual 24-hour fix requirement (Marta Kowalczyk, 2026-11-09 10:47 UTC and 15:30 UTC). Not confirmed by any authoritative source; check against MSA Schedule 3. Tom Reyes passed this to CSM Owen Pryce (2026-11-10 09:10 UTC); outcome not recorded.
- Priority P2 vs customer impact: cannot check whether P2 matches the policy's priority definitions without the policy. Relevant evidence: about 140 EUR/NOK invoices (Reported), 7 of 20 sampled EUR invoices wrong (Verified), external audit on site 12 to 13 November 2026 (account flag, CSM; and customer, 2026-11-10 13:55 UTC).
- Scope conflict: customer reports every multi-currency invoice is wrong, including NOK; support's sample found no NOK or GBP differences and 13 of 20 EUR invoices correct. Not yet explained why EUR is affected and NOK is not, or why only some EUR invoices differ.
- Escalation note states the fault dates "since 8.2.4 (2 Nov)" as fact; the thread only supports this as a possible, unconfirmed link.
- Customer asks whether issued invoices will be corrected or whether they must raise a credit note for each one (2026-11-09 15:30 UTC). Awaiting engineering answer; no fix date given.
- Customer requests written confirmation of findings for auditors; due 17:00 UTC 2026-11-10 and not sent as of the latest thread entry.
- Full count of affected invoices since 2 November is not established (only a sample of 20 EUR invoices was checked).
