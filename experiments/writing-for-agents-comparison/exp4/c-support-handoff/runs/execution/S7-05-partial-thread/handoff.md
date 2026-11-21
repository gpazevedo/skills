# Handoff: QB-202861, card payments failing with "PCX-402" (Brackenridge Veterinary Group Ltd, BV-3307)

## Problem as understood
Saved-card payments on the customer's PayCollect integration fail with "PCX-402 token not found". The failures line up with cards saved before 1 November, the date of release v8.2.3 ("Card vault migrated to PayCollect v3"). The link to that release is a hypothesis, not confirmed. The customer's reconnect did not fix it. Priority is P2.
- Verified: Since 2 Nov 14:00 UTC, 38 card payment attempts: 31 failed with PCX-402, 7 succeeded (evidence: payment logs, James Whitfield, msg 9, 5 Nov).
- Verified: All 31 failures used cards saved before 1 Nov; all 7 successes used cards saved on or after 1 Nov (evidence: payment logs, msg 9).
- Verified: Retry of INV-BV-20931 at 10:12 UTC on 5 Nov failed with the same error; PayCollect API said "token not found in vault"; the token was created 14 Oct 2026 (evidence: retry result and API response, msg 11).
- Verified: PayCollect was re-authorised on 4 Nov at 14:41 UTC, and 14 of the 31 failures came after that (evidence: integration log, msg 11).
- Verified: v8.2.3 was deployed 1 Nov with the note "Card vault migrated to PayCollect v3" (evidence: release notes, msg 11). Causal link: not confirmed.
- Reported: Every card payment has failed since Monday (customer, 4 Nov). The logs show 7 successes, so this is not accurate as stated.
- Reported: Clients' saved cards are declined at the front desk (customer, 4 Nov).
- Reported: The customer followed the reconnect instructions in an earlier message, which we cannot see (customer, 4 Nov). The re-authorisation event supports that a reconnect happened, but not which steps were followed.

## Tried so far
- Reconnect of PayCollect, steps sent by Priya Nair (Tier 1) in messages 1 to 6, which are not in the export; done by the customer, 4 Nov, re-authorised 14:41 UTC: failures continued.
- Payment log review, by James Whitfield, 5 Nov 09:40: found the pre-1-Nov card pattern above.
- Retry of INV-BV-20931 with customer consent (msg 10), by James Whitfield, 5 Nov 10:12: failed with PCX-402, no charge made.
- Other actions in messages 1 to 6: not known.

## Commitments to the customer
- Next-step log check and a reply "tomorrow morning", by Priya Nair, 4 Nov 15:40: "I'll come back to you tomorrow morning." James followed up at 09:40 UTC on 5 Nov, so this appears met.
- Update by 16:00 UTC on 5 Nov, by James Whitfield, 5 Nov 10:40: "I'll update you by 16:00 UTC today." Open. Tier 2 owns it from escalation (policy 5.2).
- Request passed to Callum Reid (Customer Success Manager), by James Whitfield, 5 Nov 09:40: "I've passed your request to Callum Reid." This is not a credit offer. James stated "I'm not able to agree credits."
- Credit: no offer or promise of a credit appears in messages 7 to 12. The customer says Priya said so ("as you said in your message yesterday", 4 Nov 17:10). That is Reported only, and could be in messages 1 to 6. Policy 6.2 and 6.3 bar agents from promising credits; only the named Customer Success Manager or the Head of Support can offer one, in writing. The customer wants written confirmation (msg 10).

## Service level
Tier: not determined (the account record's "Support level" field is blank). Target: not determined (policy section 3.1 needs the support level). Clock started: 2026-11-03 14:20 UTC (ticket created, policy 4.1). Pause: 4 Nov 09:30 to 15:00 UTC, "Pending customer", does not count (policy 4.2). Deadline: not determined. Status: not determined. Do not assume a tier. The priority is P2 and the as-of time is 2026-11-05 11:00 UTC.

## Recommended next action
Ask the Customer Success Manager, Callum Reid, or the account record owner to confirm the customer's support level, and meanwhile have Tier 2 investigate whether pre-1-Nov saved tokens were lost in the v8.2.3 vault migration, and send the customer the update promised by 16:00 UTC. Reason: the failures match the cutoff exactly, and the 16:00 update is a live commitment. Open question: what support level is the customer on? That sets the deadline and whether the ticket is at risk, and decides whether the Support Duty Manager must be told (policy 5.3, if the P2 is breached).

Alternatives:
- Pull the full messages 1 to 6 to see what Priya sent and promised, in particular any credit wording.
- Ask Tier 2 for a workaround, such as having customers re-save cards, but only if engineering confirms the vault cause. No workaround has been offered so far.

## Gaps
- Account record "Support level" is blank, so no service-level terms or deadline are given.
- Messages 1 to 6 are missing: the reconnect steps, the first-response content, the original problem report and any credit remark by Priya are unseen.
- The customer's "since Monday" and "every payment" claims conflict with the logs (7 successes, failures from 2 Nov 14:00 UTC, which is a Monday).
- The v8.2.3 link is not confirmed.
- To request: the customer's support level; messages 1 to 6; Tier 2 confirmation of the vault cause.
