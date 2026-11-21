# Escalation handoff: QB-202861, Brackenridge Veterinary Group Ltd (BV-3307)

**In one line:** Saved-card payments made with cards saved before 1 Nov 2026 fail with "PCX-402 token not found" (31 of 38 attempts since 2 Nov), probably linked to the v8.2.3 card vault migration. A customer update is promised by 2026-11-05 16:00 UTC. The SLA deadline cannot be fixed because the account record's support level is blank, and if the account is Enterprise the ticket has already breached.

## Problem as currently understood
- [verified] Since 2 Nov 14:00 UTC there have been 38 card payment attempts on the account: 31 failed with "PCX-402 token not found" and 7 succeeded (evidence: payment logs checked by James Whitfield, Tier 1, message 9, 2026-11-05 09:40 UTC)
- [verified] All 31 failures used cards saved before 1 Nov 2026. All 7 successes used cards saved on or after 1 Nov (evidence: same payment log check, James Whitfield, message 9, 2026-11-05 09:40 UTC)
- [verified] A retry on invoice INV-BV-20931 at 10:12 failed with "PCX-402 token not found". The card token on that invoice was created 14 Oct 2026, and the PayCollect API response says "token not found in vault". No charge was made (evidence: retry by James Whitfield with customer consent, internal note message 11, 2026-11-05 10:20 UTC; reported to customer in message 12)
- [verified] The customer's PayCollect reconnect did happen. The connection was re-authorised on 4 Nov at 14:41 UTC, and 14 of the 31 failures came after it (evidence: integration log read by James Whitfield, message 11, 2026-11-05 10:20 UTC)
- [verified] The v8.2.3 release notes (deployed 1 Nov) say: "Card vault migrated to PayCollect v3." (evidence: release notes read by James Whitfield, message 11). This confirms only that the migration happened. It does not confirm that the migration caused the failures.
- [verified] Account facts: plan Quillbill Clinic (annual subscription, billed monthly); data region UK; products Quillbill Invoicing (cloud), PayCollect card payments integration (saved cards, desk payments), Clinic front-desk add-on (4 practices); primary contact Sunil Mehta; contract and billing contact Dr Fiona Brackenridge; Customer Success Manager Callum Reid; open credits "None recorded" (source: account record)
- [reported] "every single card payment has failed since Monday", and clients' saved cards are declined at the front desk when they collect their pets (source: Sunil Mehta, customer, message 8, 2026-11-04 17:10 UTC)
- [reported] The customer reconnected PayCollect as support's earlier message instructed, and it did not help (source: Sunil Mehta, message 8; Priya Nair repeated "the reconnect didn't help" in message 7). The reconnect itself is now verified (see above).
- [reported] The customer says Priya promised an October subscription credit: "as you said in your message yesterday, we'll be expecting October's subscription fee to be credited". The customer also wants the credit "confirmed in writing, not passed around" (source: Sunil Mehta, messages 8 and 10). The message this refers to is in messages 1 to 6, which are not in the export, so this cannot be checked.
- [suspected] The v8.2.3 vault migration to PayCollect v3 did not carry over, or does not resolve, card tokens saved before 1 Nov (held by: James Whitfield; basis: the 1 Nov cut-off between failing and working cards matches the 1 Nov deployment, plus the "token not found in vault" response; his note says "Possible link ... not confirmed", message 11)
- [suspected] The fault is on Quillbill's side and not in the customer's settings (held by: James Whitfield, message 12; basis: every failure involves a pre-1-Nov saved card, and failures continued after the reconnect)
- Conflicts:
  - The customer says "every single card payment has failed"; the payment logs show 7 of 38 attempts succeeded, all with cards saved on or after 1 Nov.
  - The customer says Priya promised an October credit. The account record shows "Open credits: None recorded". Policy 6.2 says agents "must not promise ... a service credit", and 6.3 says only the named CSM or the Head of Support may offer one, and only in writing on the ticket or in the account record. The message it refers to is not in the export.
  - Support level: the account record's "Support level:" field is blank. The plan name "Quillbill Clinic" is not one of the policy's support levels (Standard, Business, Enterprise, policy 1.3).

## Tried so far
| What was tried | Who, when | Result |
|---|---|---|
| Earlier steps in messages 1 to 6 (including Priya's reconnect instructions) | Priya Nair and customer, 2026-11-03 14:20 to 2026-11-04 15:00 UTC | Unknown: messages 1 to 6 are not in the export, and James notes he cannot see them either (message 11) |
| Customer reconnected PayCollect, at support's request | Sunil Mehta, re-authorised 2026-11-04 14:41 UTC | Did not help (customer, message 8). Verified in the integration log: 14 of the 31 failures came after the reconnect (message 11) |
| Checked Quillbill payment logs | James Whitfield, 2026-11-05 09:40 UTC (message 9) | 38 attempts, 31 failed (all with cards saved before 1 Nov), 7 succeeded (all with cards saved on or after 1 Nov) |
| Retried collection on INV-BV-20931, with customer consent (message 10) | James Whitfield, 2026-11-05 10:12 UTC | Failed with "PCX-402 token not found"; PayCollect API: "token not found in vault"; token created 14 Oct 2026; no charge made |
| Checked the integration log and the v8.2.3 release notes | James Whitfield, 2026-11-05 10:20 UTC (message 11) | Reconnect confirmed. Release note: "Card vault migrated to PayCollect v3." Link to the failures not confirmed |
| Passed the customer's October credit request to the CSM, Callum Reid | James Whitfield, 2026-11-05 09:40 UTC (message 9) | No result recorded |
| Escalated to Tier 2 (Product Engineering Support) | James Whitfield, 2026-11-05 11:00 UTC | Status Open → Escalated, priority P2 |

## Commitments to the customer
| Commitment (quoted) | Made by | When | Due | Status |
|---|---|---|---|---|
| "the next step is for me to look at the payment logs on our side" (message 7) | Priya Nair, Tier 1 | 2026-11-04 15:40 UTC | No date given | Met: James Whitfield checked the logs and reported to the customer on 2026-11-05 09:40 UTC (message 9) |
| "I'll come back to you tomorrow morning." (message 7) | Priya Nair, Tier 1 | 2026-11-04 15:40 UTC | 2026-11-05 morning (no time given) | Met: James Whitfield replied at 2026-11-05 09:40 UTC (message 9) |
| "I'm escalating this to our Product Engineering Support team now." (message 12) | James Whitfield, Tier 1 | 2026-11-05 10:40 UTC | Now | Met: escalated 2026-11-05 11:00 UTC |
| "I'll update you by 16:00 UTC today." (message 12) | James Whitfield, Tier 1 | 2026-11-05 10:40 UTC | 2026-11-05 16:00 UTC | Pending: 5 h left as of 2026-11-05 11:00 UTC. Tier 2 now owns this commitment (policy 5.2: "From escalation, Tier 2 owns the ticket, including customer updates and any commitments already made to the customer.") |

There is no commitment on the October credit in the material supplied. The customer says Priya promised one (messages 8 and 10), but that message is not in the export. James explicitly declined to agree credits (message 9).

## Service level
- Tier: **not stated in the account record** (the "Support level:" field is blank). The plan is "Quillbill Clinic", which is not a support level. Policy 1.3: "A customer's support level (Standard, Business or Enterprise) is the level recorded in the customer's account record."
- Priority/severity: P2 (ticket events: set at creation 2026-11-03 14:20 UTC; confirmed P2 at escalation 2026-11-05 11:00 UTC). Policy 2.2: "P2 (High): a major function, such as invoice sending, payment collection or bank feeds, does not work and there is no practical workaround."
- Target (policy 3.1, P2 row for each level; the applicable row depends on the missing support level):
  - Enterprise P2: first response "2 hours, 24x7", resolution "24 hours, 24x7"
  - Business P2: first response "4 business hours", resolution "20 business hours"
  - Standard P2: first response "8 business hours", resolution "40 business hours"
- Clock rule:
  - Start: "The clock starts when the ticket is created." (4.1). Ticket created 2026-11-03 14:20 UTC.
  - Hours: "Targets marked '24x7' run on calendar time. All other targets count business hours only." (3.3). Business hours are "08:00 to 18:00 Europe/London time, Monday to Friday, excluding bank holidays in England", and Europe/London is UTC in this period (1.1).
  - Pauses: "The clock is paused only while the ticket status is 'Pending customer'." (4.2). Status history: Pending customer from 2026-11-04 09:30 to 15:00 UTC, which is 5 h 30 min paused, all inside business hours. The thread says the ticket event log is complete, so no other pauses occurred.
- First response: 2026-11-03 15:02 UTC, 42 minutes after creation (Priya Nair, message 2 per the event log). This meets the target at every level.
- Deadline (resolution), shown for each possible level:
  - Business hours used up to now: 3 Nov 14:20 to 18:00 = 3 h 40 min; 4 Nov 08:00 to 09:30 = 1 h 30 min (total 5 h 10 min); paused 09:30 to 15:00; 4 Nov 15:00 to 18:00 = 3 h (total 8 h 10 min); 5 Nov 08:00 to 11:00 = 3 h (total **11 h 10 min**).
  - **Business P2 (20 business hours): Fri 2026-11-06 09:50 UTC.** Arithmetic: 20 h minus 11 h 10 min = 8 h 50 min left. Thu 5 Nov 11:00 to 18:00 uses 7 h, leaving 1 h 50 min. Fri 6 Nov 08:00 + 1 h 50 min = 09:50.
  - **Standard P2 (40 business hours): Tue 2026-11-10 09:50 UTC.** Arithmetic: 40 h minus 11 h 10 min = 28 h 50 min left. Thu 5 Nov 7 h leaves 21 h 50 min; Fri 6 Nov 10 h leaves 11 h 50 min; Mon 9 Nov 10 h leaves 1 h 50 min; Tue 10 Nov 08:00 + 1 h 50 min = 09:50.
  - **Enterprise P2 (24 calendar hours): Wed 2026-11-04 19:50 UTC.** Arithmetic: 3 Nov 14:20 + 24 h = 4 Nov 14:20, plus the 5 h 30 min pause = 4 Nov 19:50.
- Status as of 2026-11-05 11:00 UTC (the last timestamp in the thread, the escalation event; no current time for the case was supplied, so recompute against the real current time):
  - If Business: open, 8 h 50 min business time left. "At risk" (policy 4.5: "less than 25% of its resolution target remains") starts when 5 h remain, which is 2026-11-05 14:50 UTC.
  - If Standard: open, 28 h 50 min business time left. At risk when 10 h remain, which is Mon 2026-11-09 09:50 UTC.
  - If Enterprise: **breached**, 15 h 10 min over. Policy 5.3: "The Support Duty Manager must be told of every P1 ticket and of every P2 ticket that is breached."
- Customer update cadence: policy 7.1: "P2 tickets: an update at least once each business day."

## Recommended next action
1. **Confirm the support level first** (a few minutes): ask the account owner or the CSM, Callum Reid, to fill in the blank "Support level" field. If it is Enterprise, the ticket is already breached and the Support Duty Manager must be told now (policy 5.3). If it is Business, the ticket becomes at risk at 14:50 UTC today and breaches Fri 6 Nov 09:50 UTC.

2. **Main check: look up the INV-BV-20931 card token (created 14 Oct 2026) in the v8.2.3 vault migration records and in the PayCollect v3 vault.** This is the cheapest test of the leading suspected cause, which is that the migration did not carry over, or cannot resolve, tokens saved before 1 Nov. Then check whether the other 30 failing tokens behave the same way. Each possible result means something different:
   - **The token is missing from the v3 vault, or the migration records show it was skipped or failed.** The migration cause is verified. The fix is to re-migrate BV-3307's pre-1-Nov tokens from the old vault, if the old vault still holds them. Also check whether other accounts with pre-1-Nov saved cards are affected.
   - **The token is in the v3 vault, but under a different ID from the one Quillbill sends.** The migration ran, but Quillbill still references the old token IDs. The cause is a missing or broken ID mapping, which is still a v8.2.3 defect.
   - **The token is in the v3 vault with the ID Quillbill sends.** The migration cause is ruled out. The next step is the request path: which vault or API version Quillbill calls for older tokens, and the account's UK data region.

3. **Customer update due 2026-11-05 16:00 UTC** (James's commitment, now owned by Tier 2). Send it even if the check is not finished. It should:
   - say the investigation is with Product Engineering Support and that failures are limited to cards saved before 1 Nov;
   - set the time of the next update (policy 6.1 allows this);
   - give no fix date (policy 6.2 forbids it);
   - make no promise about the credit. Say the credit request is with Callum Reid, because policy 6.3 allows only the CSM or the Head of Support to offer a credit, in writing on the ticket. Ask Callum to reply to the customer directly, since the customer has asked for written confirmation.

   A possible interim workaround is to re-save affected clients' cards, since every card saved on or after 1 Nov has worked. It is untested, so offer it to the customer only after support has verified it on one card.

## Gaps
- Messages 1 to 6 (2026-11-03 14:20 to 2026-11-04 15:00 UTC) are missing. They hold the original report, the reconnect instructions, any other steps tried, and whatever Priya said that the customer reads as a credit promise. Get the full ticket before contacting the customer about the credit.
- The account record's support level is blank, so the SLA target, deadline and breach status cannot be fixed.
- Failures before 2 Nov 14:00 UTC are not covered: the log window James reported starts then, but v8.2.3 deployed on 1 Nov. Nobody has checked whether failures started at the deployment.
- Nobody has checked whether other customers with pre-1-Nov saved cards are affected.
- Nobody has checked whether the old vault still holds the pre-1-Nov tokens, which decides whether re-migration is possible.
- No response from Callum Reid on the credit request is recorded.
- The interim workaround (re-saving a card) has not been tested.
