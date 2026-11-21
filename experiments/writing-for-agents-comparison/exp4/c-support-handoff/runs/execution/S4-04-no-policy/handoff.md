Clarifying question: The support policy (and the contract's Schedule 3 terms) was not supplied. Please send it so the service-level section can be completed; the customer's claimed 24-hour fix term cannot be checked without it.

# Escalation handoff: QB-203977, Lindqvist Marine Supplies Ltd (LMS-0855)

**Summary:** Per-line VAT rounding is not applied to some EUR invoices since release 8.2.4 (2 Nov), reproduced in the customer's sandbox. The most urgent deadline is the written summary promised to the customer by 17:00 UK time (17:00 UTC) today, 10 Nov, with auditors on site Thursday 12 Nov.
**Reference time:** 2026-11-10 14:20 UTC (latest thread entry; it matches the as-of time stated in the export)

## Problem as currently understood
Since 8.2.4 (deployed 2 Nov), the invoice VAT total on some EUR invoices differs by EUR 0.01 from the sum of the line VAT, although the account is set to per-line rounding. In the sandbox the EUR invoice VAT total appears to be calculated on the invoice total rather than per line, and GBP is unaffected. The cause is not confirmed.
- [Verified] Account setting "VAT rounding: per line" is on, last changed 14 March 2026 (Tom Reyes internal note, 2026-11-09 14:30)
- [Verified] INV-LM-11402, 11417, 11431 (EUR): each invoice VAT total is EUR 0.01 below the sum of line VAT (Tom Reyes, 2026-11-09 14:30)
- [Verified] Sample of 20 EUR invoices issued 2 to 9 Nov: 7 differ by 0.01 (5 lower, 2 higher), 13 match. 9 of 9 NOK and 11 of 11 GBP sampled invoices show no difference (Tom Reyes, 2026-11-09 14:30)
- [Verified] Sandbox repro: EUR invoice, 3 lines of 10.33 at 20%. Line VAT 2.07 each (sum 6.21), invoice VAT total 6.20. The same invoice in GBP gives 6.21. Switching rounding to per invoice and back made no change for EUR (Tom Reyes, 2026-11-09 14:30)
- [Verified] Release notes for 8.2.4 (deployed 2 Nov) say: "Improved currency conversion precision for non-base-currency invoices." Tom records the link to this fault as "Possible link; not confirmed." (Tom Reyes, 2026-11-09 14:30)
- [Reported] About 140 invoices in EUR and NOK issued since 2 Nov (Marta Kowalczyk, 2026-11-09 10:47). This is not checked, and the checked samples show no NOK differences.
- [Reported] "Every multi-currency invoice" has the wrong VAT total (Marta, 2026-11-09 10:47). The recorded sample contradicts this: 13 of 20 EUR invoices match, and the sample shows no NOK or GBP differences. The recorded check governs.
- [Reported] Auditors require per-line rounding and will not accept per-invoice rounding (Marta, 2026-11-09 10:47 and 15:30); auditors are in on Thursday (Marta, 2026-11-10 13:55). The account record also notes an external audit on site 12 to 13 Nov (account record, noted by CSM).
Open questions:
- Is the 8.2.4 change the cause, and why do only some EUR invoices differ (possibly rounding-dependent amounts)?
- Why are NOK invoices unaffected if they are also non-base-currency?
- Is the full population of EUR and NOK invoices since 2 Nov affected, and how many are wrong? Only 20 EUR and 9 NOK were sampled.
- Can a fix recalculate invoices already issued, or must the customer raise credit notes?

## Tried so far
- Asked customer for example invoice numbers, by Tom Reyes, 2026-11-09 11:20: customer supplied three EUR invoices at 12:05 (Reported by customer, then checked by Tom)
- Checked the account rounding setting, by Tom Reyes, 2026-11-09 14:30: per line, on
- Checked the 3 invoices and sampled 20 EUR, 9 NOK and 11 GBP invoices, by Tom Reyes, 2026-11-09 14:30: results as above
- Reproduced in the sandbox, by Tom Reyes, 2026-11-09 14:30: reproduced for EUR, not for GBP
- Toggled the sandbox rounding setting to per invoice and back, by Tom Reyes, 2026-11-09 14:30: no change for EUR
- Per-invoice rounding offered as a workaround, by Tom Reyes, 2026-11-09 14:45: customer rejected it (Reported, auditors)
- Escalated to Tier 2, by Tom Reyes, 2026-11-10 14:20: done
- Not tried and not recorded: investigation of 8.2.4 code or logs, checks on production data beyond the sample.

## Commitments to the customer
- "I'm escalating the fault to our Product Engineering Support team today.", Tom Reyes, 2026-11-10 09:10: met (escalated 2026-11-10 14:20)
- "I'll ask engineering whether a fix would recalculate invoices already issued.", Tom Reyes, 2026-11-10 09:10: unclear: the escalation note lists it as an open ask, but no recorded answer or request to engineering exists. It now falls to Tier 2.
- "I'll send you a written summary of what we've reproduced, including the sandbox example, by 17:00 UK time today (Tuesday 10 November).", Tom Reyes, 2026-11-10 09:10: outstanding (not sent at 14:20 per the escalation note; 17:00 UK is 17:00 UTC in November, so 2h40m remain)
- "I've asked your Customer Success Manager, Owen Pryce, to go through the service-level terms in your contract with you.", Tom Reyes, 2026-11-10 09:10: unclear: no entry shows Owen contacted the customer, and no timing was promised
- Claimed by customer, not found in thread: "Under our Enterprise contract you are required to fix this within 24 hours. Please confirm today." (Marta, 2026-11-09 10:47). Tom declined to confirm it (2026-11-10 09:10). The policy was not supplied, so this cannot be checked.

## Service level
- Tier: Enterprise (account record; terms in MSA Schedule 3) | Priority: P2 (ticket, recorded 2026-11-09 10:47 and 2026-11-10 14:20)
- Target: Not determinable. The support policy was not supplied, and the MSA Schedule 3 is not in the inputs. No industry-typical target is substituted.
- Deadline: Not determinable, for the same reason. For information only, 24 hours from ticket creation (10:47 on 9 Nov) would be 2026-11-10 10:47 UTC. That is the customer's claim, not a policy term.
- Status: Not determinable

## Recommended next action
Get Tier 2 to send the customer the written summary (the sandbox repro with the 3 x 10.33 example, sample results, and the unconfirmed 8.2.4 link, stating what is not yet known) before 17:00 UTC today. In parallel, have engineering check whether 8.2.4 broke per-line rounding for non-base-currency EUR invoices, and whether issued invoices can be recalculated. The reason is that the repro is verified, the cause is unconfirmed, and the auditors are in on 12 Nov. Serves: Tom's 17:00 UK summary commitment and the customer's audit on 12 to 13 Nov.
Tell the customer: if Tier 2 cannot send the summary by 17:00 UTC, tell Marta before then, with a new time. Say the cause is still being confirmed and give no fix date or invoice-recalculation promise, since none exists. Direct the contract-term question to Owen Pryce.

## Blocked
Support policy missing (and Schedule 3 terms not supplied): blocks the service-level target, deadline and status.
