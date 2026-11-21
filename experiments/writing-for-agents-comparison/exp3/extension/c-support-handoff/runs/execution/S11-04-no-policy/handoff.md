Clarifying question: Can you supply the support policy (service-level targets per plan and priority, and the clock rules), and the Service Level terms in Schedule 3 of Lindqvist Marine's Master Services Agreement? Without them the P2 target and deadline cannot be worked out, and the customer's "fix within 24 hours" claim cannot be checked.

# Escalation handoff: QB-203977: Per-line VAT rounding not applied to some EUR invoices since 2 Nov

**Customer:** Lindqvist Marine Supplies Ltd (LMS-0855), Quillbill Trade, Enterprise support · **Priority:** P2 · **Next deadline:** service level cannot determine: support policy not supplied; nearest commitment (written summary for auditors, due 2026-11-10 17:00 UTC) overdue by 11 d 1 h 31 min if not sent after the export ends (as of 2026-11-21 18:31 UTC)

## Problem as currently understood
On some EUR invoices issued since 2 November, the invoice VAT total differs by EUR 0.01 from the sum of the line VAT, although the account is set to per-line VAT rounding. Support confirmed this on the three invoices the customer sent, in a sample (7 of 20 EUR invoices), and in the customer's sandbox, where the EUR VAT total equals VAT on the invoice net total rather than the sum of rounded line VAT; the same invoice in GBP is correct. No differences were found in the sampled NOK or GBP invoices. The leading explanation is release 8.2.4 (deployed 2 Nov, "Improved currency conversion precision for non-base-currency invoices"), but that link is not confirmed. The customer cannot use per-invoice rounding as a workaround because of their auditors.

Evidence:
- [Verified] Account setting "VAT rounding: per line" is on, last changed 14 March 2026 (Tom Reyes internal note, 2026-11-09 14:30 UTC; account record, VAT settings)
- [Verified] INV-LM-11402, INV-LM-11417 and INV-LM-11431 each have an invoice VAT total EUR 0.01 lower than the sum of line VAT (Tom Reyes internal note, 2026-11-09 14:30 UTC)
- [Verified] Sample 2 to 9 Nov: 7 of 20 EUR invoices differ by 0.01 (5 lower, 2 higher), 13 match; 0 of 9 NOK invoices differ; 0 of 11 sampled GBP invoices differ (Tom Reyes internal note, 2026-11-09 14:30 UTC)
- [Verified] Sandbox reproduction: EUR invoice, 3 lines of EUR 10.33 at 20%; line VAT 2.07 each, sum 6.21; invoice VAT total 6.20 (20% of 30.99, rounded). Same invoice in GBP: 6.21 (Tom Reyes internal note, 2026-11-09 14:30 UTC)
- [Verified] In the sandbox, switching rounding to "per invoice" and back to "per line" made no change for EUR (Tom Reyes internal note, 2026-11-09 14:30 UTC)
- [Verified] Release 8.2.4 deployed 2 Nov; release note reads "Improved currency conversion precision for non-base-currency invoices"; link to this fault not confirmed (Tom Reyes internal note, 2026-11-09 14:30 UTC)
- [Verified] Account base currency is GBP; invoice currencies enabled are GBP, EUR, NOK (account record)
- [Verified] External audit on site 12 to 13 November 2026 (account record, account flags)
- [Reported] The fault started "since your update last week" and affects "every multi-currency invoice" (customer, 2026-11-09 10:47 UTC)
- [Reported] About 140 invoices issued in EUR and NOK since 2 November (customer, 2026-11-09 10:47 UTC)
- [Reported] Their auditors require line-by-line VAT rounding; per-invoice rounding is not acceptable (customer, 2026-11-09 10:47 and 15:30 UTC)
- [Inferred] For EUR, VAT is being calculated on the invoice net total and rounded once, so the per-line setting is ignored (rests on: sandbox figures, 6.20 = 20% of 30.99; differences in both directions in the sample; no change when the setting is toggled)
- [Inferred] "Every multi-currency invoice" overstates the fault: about a third of sampled EUR invoices and no sampled NOK invoices differ (rests on: customer claim vs. Tom's sample)
- [Inferred] NOK is not shown to be unaffected: only 9 invoices were checked and no NOK sandbox reproduction is recorded, and the 8.2.4 note covers all non-base currencies (rests on: sample size; sandbox test was EUR and GBP only; release note wording)
- [Inferred] Onset at 8.2.4 is not established: no EUR invoices from before 2 Nov were checked (rests on: sample covers 2 to 9 Nov only)

## Tried so far
| When (UTC) | Who | Action | Result |
|---|---|---|---|
| 2026-11-09 11:20 | Tom Reyes (Tier 1) | Asked customer for example invoice numbers | Customer sent INV-LM-11402, -11417, -11431 (12:05) |
| 2026-11-09 14:30 | Tom Reyes | Checked account rounding setting | Per line, last changed 14 Mar 2026; recent setting change ruled out as cause |
| 2026-11-09 14:30 | Tom Reyes | Checked the three invoices | Each EUR 0.01 below sum of line VAT |
| 2026-11-09 14:30 | Tom Reyes | Sampled invoices 2 to 9 Nov | EUR 7/20 differ; NOK 0/9; GBP 0/11 |
| 2026-11-09 14:30 | Tom Reyes | Reproduced in customer sandbox, EUR and GBP | EUR wrong (6.20 vs 6.21); GBP correct |
| 2026-11-09 14:30 | Tom Reyes | Toggled rounding setting per invoice and back in sandbox | No change for EUR; stale setting ruled out |
| 2026-11-09 14:30 | Tom Reyes | Read 8.2.4 release notes | Possible link; not confirmed |
| 2026-11-09 14:45 | Tom Reyes | Offered per-invoice rounding as workaround | Rejected by customer (auditors), 15:30 |
| 2026-11-10 14:20 | Tom Reyes | Escalated to Tier 2 (Product Engineering Support), P2 | Pending; no Tier 2 result recorded |

## Commitments to the customer
| Commitment (quoted) | Made by | When (UTC) | Status as of 2026-11-21 18:31 UTC |
|---|---|---|---|
| "I'm escalating the fault to our Product Engineering Support team today." | Tom Reyes (Tier 1) | 2026-11-10 09:10 | Met: escalated 2026-11-10 14:20 |
| "I'll ask engineering whether a fix would recalculate invoices already issued. I can't promise that it will" | Tom Reyes | 2026-11-10 09:10 | Question passed to Tier 2 in escalation note 14:20; no answer recorded or given to customer; no time stated |
| "I'll send you a written summary of what we've reproduced, including the sandbox example, by 17:00 UK time today (Tuesday 10 November)." [Inferred: 2026-11-10 17:00 UTC, UK on GMT in November] | Tom Reyes | 2026-11-10 09:10 | Not sent as of 14:20 per escalation note ("haven't sent yet"); export ends there. Overdue by 11 d 1 h 31 min unless sent after the export. Customer stressed it twice (13:55) |
| "I've asked your Customer Success Manager, Owen Pryce, to go through the service-level terms in your contract with you." | Tom Reyes | 2026-11-10 09:10 | Outstanding; no time stated; no contact from Owen Pryce in the thread |

Claimed by the customer, not found in the thread: none. (The customer's "fix within 24 hours" is a claimed contract term, not a promise by support; see Service level.)

## Service level
- Plan: Quillbill Trade (annual subscription), support level Enterprise, terms in Master Services Agreement Schedule 3 [Verified] (account record: Plan, Support level)
- Priority: P2 [Verified] (ticket events 2026-11-09 10:47 UTC and 2026-11-10 14:20 UTC)
- Customer's claim: "Under our Enterprise contract you are required to fix this within 24 hours" [Reported] (customer, 2026-11-09 10:47 UTC; repeated 15:30). Not checked: Schedule 3 not supplied, and Tom Reyes declined to confirm it (2026-11-10 09:10 UTC). It does not set the clock.
- Target: cannot determine: support policy not supplied
- Clock: case opened 2026-11-09 10:47 UTC [Verified] (ticket created event); first support reply 2026-11-09 11:20 UTC [Verified] (Tom Reyes). Policy start event and business-hours or pause rules unknown. Elapsed since case opened: 12 d 7 h 44 min as of 2026-11-21 18:31 UTC (1 d 3 h 33 min at escalation).
- Deadline and status: cannot determine: support policy not supplied

## Recommended next action
Tom Reyes (Tier 1, owner of the promise) confirms whether the written summary for the auditors was sent and, if not, sends it now: it was due 2026-11-10 17:00 UTC, before the audit on 12 to 13 Nov, and it rests entirely on findings already Verified above.

Follow-ups:
1. Tier 2 engineer: confirm the cause in 8.2.4 by repeating the sandbox example in NOK and checking EUR invoices from before 2 Nov, then answer whether a fix will recalculate issued invoices or the customer must raise credit notes.
2. Owen Pryce (CSM): obtain MSA Schedule 3 and the support policy so the P2 target and deadline can be set and the 24-hour claim answered.

## Gaps and open questions
- Missing input: support policy. Service-level target, clock rules and deadline cannot be determined.
- Missing input: MSA Schedule 3 (Enterprise terms). The customer's 24-hour fix claim is unverified; if the customer holds to it, they will treat it as passed on 2026-11-10 10:47 UTC.
- The thread export ends 2026-11-10 14:20 UTC; anything after (summary sent, CSM contact, Tier 2 findings) is not visible.
- Link to release 8.2.4 is unconfirmed; no pre-2 Nov baseline checked.
- NOK exposure unknown: 9-invoice sample, no sandbox test, though the customer says about 140 EUR and NOK invoices may be affected.
- Conflict: customer says every multi-currency invoice is wrong; support's sample shows 7 of 20 EUR and 0 of 9 NOK.
- Open: whether a fix will recalculate issued invoices or credit notes are needed; affected invoice count across all EUR (and NOK) invoices since 2 Nov.
