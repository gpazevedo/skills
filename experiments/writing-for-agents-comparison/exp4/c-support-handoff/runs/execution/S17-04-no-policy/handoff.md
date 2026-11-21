# Handoff: QB-203977, Lindqvist Marine Supplies Ltd (LMS-0855)

As-of: 2026-11-10 14:20 UTC (export time). Escalated to Tier 2 (Product Engineering Support), P2.

## Ledger (every message)

| # | Time (UTC) | Author | Claims / actions / promises |
|---|---|---|---|
| 1 | 11-09 10:47 | Marta Kowalczyk (customer) | Ticket opened by email, P2. Claims: since last week's update every multi-currency invoice has wrong VAT total (total not equal to sum of line VAT); auditors need line-by-line rounding and the account is set that way; about 140 EUR and NOK invoices issued since 2 Nov; contract requires a fix within 24 hours. Asks for confirmation today. |
| 2 | 11-09 11:20 | Tom Reyes (T1) | Assigned, status New to Open. Says he has started looking. Asks for 2 or 3 invoice numbers. |
| 3 | 11-09 12:05 | Marta | Gives INV-LM-11402, INV-LM-11417, INV-LM-11431, all EUR. |
| 4 | 11-09 14:30 | Tom, internal note | Setting "VAT rounding: per line" on, last changed 14 Mar 2026. The three invoices each have invoice VAT EUR 0.01 below line-VAT sum. Sample of 20 EUR invoices (2 to 9 Nov): 7 differ by 0.01 (5 lower, 2 higher), 13 match. 9 NOK: none differ. 11 GBP: none differ. Sandbox reproduction: 3 lines of EUR 10.33 at 20%, line VAT 2.07 each (sum 6.21), invoice total 6.20; same in GBP gives 6.21. Toggled sandbox to per invoice and back: no change for EUR. 8.2.4 (deployed 2 Nov) release note "Improved currency conversion precision for non-base-currency invoices": possible link, not confirmed. |
| 5 | 11-09 14:45 | Tom to customer | Repeats the three-invoice finding, the 7 of 20 EUR, none in NOK (9) or GBP (11), the sandbox reproduction; says EUR VAT total "seems to be calculated on the invoice total rather than line by line". Mentions per-invoice rounding as workaround, noting auditors will not accept it. |
| 6 | 11-09 15:30 | Marta | Per-invoice rounding not acceptable. Asks: (1) fix the bug; (2) will issued invoices be corrected or must she raise a credit note for each; (3) written confirmation of findings for auditors. Asks again for 24-hour confirmation. |
| 7 | 11-10 09:10 | Tom to customer | (1) Escalating to Product Engineering Support today, cannot give a fix date. (2) Will ask engineering whether a fix recalculates issued invoices; cannot promise it will. (3) Will send written summary incl. sandbox example by 17:00 UK time today, Tuesday 10 Nov. Cannot confirm contract terms; says he has asked CSM Owen Pryce to go through the service-level terms with her. |
| 8 | 11-10 13:55 | Marta | "Fine." Wants summary to arrive today; auditors in on Thursday. |
| 9 | 11-10 14:20 | Tom, event + escalation note | Escalated to Tier 2, status Escalated, P2. Note: per-line rounding not applied to some EUR invoices since 8.2.4; open asks are fix, whether issued invoices are recalculated, and the written summary promised for 17:00 UK today, not yet sent. Auditors on site Thursday 12 Nov. |

## 1. Problem and evidence

**Problem:** Since release 8.2.4 (2 Nov), some EUR invoices on this account show an invoice VAT total that differs by EUR 0.01 from the sum of the line VAT, although the account is set to per-line VAT rounding. NOK and GBP samples showed no difference. Cause is not confirmed.

Evidence:
- Verified (Tom's internal note, 11-09 14:30, invoice records): INV-LM-11402, -11417, -11431 (EUR) each have invoice VAT EUR 0.01 below the line-VAT sum.
- Verified (same note, sample): 7 of 20 EUR invoices issued 2 to 9 Nov differ by 0.01 (5 lower, 2 higher); 13 match.
- Verified (same note): 0 of 9 NOK and 0 of 11 GBP sampled invoices differ.
- Verified (sandbox reproduction, same note): 3 lines of EUR 10.33 at 20% give line VAT 2.07 x 3 = 6.21, invoice total 6.20 (20% of 30.99). Same invoice in GBP gives 6.21.
- Verified (sandbox test): switching rounding to per invoice and back to per line does not change the EUR result.
- Verified (account record / note): setting "VAT rounding: per line" is on, last changed 14 March 2026, so it was not changed around the update.
- Verified (note): 8.2.4 deployed 2 Nov with release note about currency conversion precision for non-base-currency invoices. The link to the fault is a hypothesis (the note itself says not confirmed), so the link is unverified.
- Reported (Marta, 11-09 10:47): "every" multi-currency invoice is wrong; about 140 EUR and NOK invoices issued since 2 Nov. Not verified.
- Reported (Marta): auditors require line-by-line rounding; per-invoice rounding not acceptable (11-09 15:30). Not verified; the account setting is consistent with it.
- Reported (Marta): fault began with the update "last week". Timing matches 2 Nov, but no pre-2 Nov EUR invoices were checked in the supplied notes.
- Tom's statement to the customer that the VAT total "seems to be calculated on the invoice total" is an inference from the sandbox result (6.20 equals 20% of the total), not a code or log observation.

Conflicts:
- Marta says every multi-currency invoice is wrong and includes NOK; the sample shows 7 of 20 EUR affected and 0 of 9 NOK.
- Marta's examples all have invoice VAT lower than the line sum; the sample has 2 of 7 higher. Tom's customer message (11-09 14:45) described the difference only as "EUR 0.01" without the 5 lower / 2 higher split.
- The 7 of 20 rate against about 140 invoices is not extrapolated here; affected count is unknown.

## 2. Tried and results

| Who | When (UTC) | What | Result |
|---|---|---|---|
| Tom | 11-09 14:30 | Checked account VAT setting | Per line, last changed 14 Mar 2026. No setting change found. |
| Tom | 11-09 14:30 | Checked three customer invoices | Confirmed 0.01 lower on each. |
| Tom | 11-09 14:30 | Sampled 20 EUR, 9 NOK, 11 GBP invoices | 7 EUR differ; NOK, GBP none. |
| Tom | 11-09 14:30 | Sandbox reproduction (3 x EUR 10.33 at 20%) | Reproduced for EUR; GBP correct. |
| Tom | 11-09 14:30 | Sandbox toggle per invoice and back to per line | No change for EUR (failed as a fix or workaround test). |
| Tom | 11-09 14:30 | Reviewed 8.2.4 release notes | Possible link, not confirmed. |
| Tom | 11-09 14:45 | Offered per-invoice rounding workaround | Customer rejected it (auditors). Not applied. Note the sandbox test shows it may not have fixed EUR anyway. |
| Tom | 11-10 09:10 | Asked CSM Owen Pryce to go through service-level terms with customer | No result recorded; no reply from Owen in the thread. |
| Tom | 11-10 14:20 | Escalated to Tier 2 | Done. |

No code, log, or release-version comparison was done. Whether the sandbox, which is a copy of production settings refreshed monthly, matches production behaviour beyond settings is not stated.

## 3. Commitments to the customer

1. Escalation. Tom Reyes, 11-10 09:10: "I'm escalating the fault to our Product Engineering Support team today." Status: done at 11-10 14:20.
2. Ask engineering about issued invoices. Tom, 11-10 09:10: "I'll ask engineering whether a fix would recalculate invoices already issued." Status: not shown as done in the thread, now falls to Tier 2 to answer. He added "I can't promise that it will", so no commitment that invoices are recalculated.
3. Written summary. Tom, 11-10 09:10: "I'll send you a written summary of what we've reproduced, including the sandbox example, by 17:00 UK time today (Tuesday 10 November)." Not sent as of 14:20 (escalation note: "haven't sent yet"). Customer has stressed it must arrive today (13:55) and that auditors are in Thursday.
4. CSM review of terms. Tom, 11-10 09:10: "I've asked your Customer Success Manager, Owen Pryce, to go through the service-level terms in your contract with you." Ambiguous: this is stated as a completed action, not as a promise that Owen will do it by a time. Listed because the customer may expect it.

Not commitments: "I can't give you a fix date" and "I can't promise that it will"; no one confirmed the 24-hour fix (customer's claim, items 1 and 6 in ledger; support never accepted it).

## 4. Service level and deadline

**Not determinable from the supplied policy.** No support policy or MSA Schedule 3 was supplied. The account record gives the support level as "Enterprise (terms in Master Services Agreement, Schedule 3)". Needed: Schedule 3 with the Enterprise response and resolution targets, which priority they apply to (ticket is P2), the clock start rule (ticket created 11-09 10:47 UTC, or another trigger) and any pause or exclusion rules.

Inputs for whoever has the clause:
- Ticket created 2026-11-09 10:47 UTC; as-of 2026-11-10 14:20 UTC; elapsed 27 h 33 min.
- Marta's "24 hours" is reported only, not a verified contract term. If it were a resolution target running from creation, the nominal point would be 2026-11-10 10:47 UTC, already passed. This is shown only to indicate urgency, not as a determined breach.
- No pause or exclusion rule is applied, since none is supplied.

Separate self-imposed deadline (a commitment, not a policy term): written summary due 17:00 UK time 2026-11-10. UK is on GMT in November (UTC+0, so 17:00 UTC; from the stated UK timezone assumption). Remaining from 14:20: 2 h 40 min.
Customer audit date: Thursday 2026-11-12 (account flag: on site 12 to 13 November 2026, noted by CSM).

## 5. Recommended next action

**Tier 2 (Product Engineering Support) should take ownership and determine whether 8.2.4 changed the rounding path for non-base-currency invoices.** Reason: the fault is reproducible in the sandbox for EUR only, per-line setting is on and unchanged since March, and the only recent change identified is 8.2.4, which touched non-base-currency conversion. The setting toggle did not help, which points to code rather than configuration. NOK also is non-base-currency and was clean in the sample, so the cause may depend on currency or rate.

First check: run the sandbox reproduction (3 x EUR 10.33 at 20%) and a NOK equivalent against 8.2.4 and the previous release, and compare how the VAT total is computed.

Time constraint: Tom's written summary is due 17:00 UTC today; Tier 2 should agree with Tom today who sends it, using the sandbox example above, and should state what is verified and what is not.

Questions for the customer:
- Full list of invoice numbers affected, or permission to scan all invoices issued since 2 Nov, since Marta's count is about 140 and the sample is 20.
- Whether any pre-2 Nov EUR invoices show the problem.
- Whether she has seen any NOK invoice with a difference (her message says NOK; samples show none).

Questions for engineering:
- Does the 8.2.4 change cause this, and why EUR and not NOK?
- Which invoice lines or amounts trigger it (13 of 20 EUR matched)?
- Will a fix recalculate or reissue issued invoices, or is a credit note per invoice needed? (Promised to be asked.)
- Is there a safe interim workaround that keeps per-line rounding?
- Can the fix or an answer be available before Thursday 12 Nov?

## 6. Gaps

- Missing input: support policy / MSA Schedule 3 (response and resolution targets, clock start, pauses). Service level not determinable.
- Missing: any message from CSM Owen Pryce; unknown whether he has contacted Marta.
- Unverified: link between 8.2.4 and the fault; Tom's "calculated on the invoice total" description; customer's 140 invoices and "every invoice"; NOK being affected (sample says no); auditors' rules.
- Not checked: pre-2 Nov invoices, code or logs, production reproduction (only sandbox), other currencies.
- Conflict: customer says all multi-currency invoices wrong versus sample of 7 of 20 EUR, 0 of 9 NOK.
- Assumption: 17:00 UK time equals 17:00 UTC (GMT in November).
- Priority is P2; the ticket does not say whether Enterprise terms treat it differently.
