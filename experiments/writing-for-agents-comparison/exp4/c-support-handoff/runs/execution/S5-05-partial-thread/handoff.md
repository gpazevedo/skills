# Handoff: QB-202861 Card payments failing with "PCX-402" (Brackenridge Veterinary Group Ltd, BV-3307)

Note: the thread export holds messages 7 to 12 only. Messages 1 to 6 (2026-11-03 14:20 UTC to 2026-11-04 15:00 UTC) were not seen. The event log is complete. All times UTC. As-of 2026-11-05 11:00.

## Problem
- Saved-card payments through PayCollect fail with "PCX-402 token not found". [Verified: James Whitfield's log check, message 9; retry result, message 11]
- Between 2 Nov 14:00 and 5 Nov 09:40, 38 card payment attempts were made: 31 failed and 7 succeeded. [Verified: payment logs, message 9]
- All 31 failures used cards saved before 1 Nov. All 7 successes used cards saved on or after 1 Nov. [Verified: payment logs, message 9]
- Retry of INV-BV-20931 at 10:12 on 5 Nov failed with the same error. Its card token was created 14 Oct 2026, and the PayCollect API said "token not found in vault". [Verified: support-side retry, message 11]
- The customer re-authorised the PayCollect connection on 4 Nov at 14:41, and 14 of the 31 failures came after that. A reconnect therefore does not fix it. [Verified: integration log, message 11]
- Release v8.2.3 was deployed on 1 Nov with the note "Card vault migrated to PayCollect v3". [Verified: release notes, message 11] A link to the failures is possible but not confirmed. [Verified as unconfirmed: message 11]
- The customer says "every single card payment has failed since Monday". [Reported: message 8] CONFLICT: the logs show 7 successes in that period (message 9).
- Clients' saved cards are being declined at the front desk, and staff are embarrassed. [Reported: message 8]
- The customer says they did "exactly what your earlier message said" (reconnected PayCollect). [Reported: message 8] The reconnect itself is verified by the integration log. Which steps Priya sent is not visible in this export.
- Priority is P2. [Verified: ticket event log, set at creation and still P2 on escalation]

## Open questions
- Support level: the account record's "Support level" field is blank. Check with account administration or the contract (Dr Fiona Brackenridge is the contract contact). Without it the targets cannot be determined (see Service level).
- Contents of messages 1 to 6. Read the full ticket. This matters for the two points below.
  - What reconnect or other steps Priya sent, and whether any were tried.
  - Whether Priya said anything about a credit (see Commitments).
- Whether the v8.2.3 vault migration to PayCollect v3 causes the failures for tokens saved before 1 Nov. Check with the release or PayCollect integration owners, for example by testing a pre-1 Nov token against the v3 vault.
- Whether a practical workaround exists, such as re-saving cards (the 7 successes were all cards saved on or after 1 Nov). This affects whether P2 is the right priority (policy 2.2 and 2.3). It is untested. Test re-saving a card on a test or consenting account.
- Whether the Support Duty Manager has been told. Policy 5.3 requires it for a breached P2, and nothing in the thread shows it. Breach status is not determinable (see Service level).
- Whether Callum Reid actually received the credit request. James says he passed it on (message 9), but nothing in the export records it. Confirm with Callum.

## Attempts
1. Messages 1 to 6, by Priya Nair and the customer. Content not available. Known from the event log: first agent response at 2026-11-03 15:02; status Pending customer from 11-04 09:30 to 15:00; the customer replied at 15:00. Result: unknown. The reconnect did not help (per message 7).
2. Customer reconnected PayCollect (re-authorised 4 Nov 14:41, per integration log). Result: failed, failures continued.
3. Priya Nair, 4 Nov 15:40 (message 7): acknowledged the failed reconnect and said she would check payment logs on the support side. Result: no log check is recorded from her. James did the log check on 5 Nov.
4. James Whitfield, 5 Nov 09:40 (message 9): checked payment logs. Result: worked as diagnosis; findings above.
5. James Whitfield, 5 Nov 09:40 (message 9): passed the credit request to Callum Reid. Result: unknown, no confirmation in the thread.
6. James Whitfield, 5 Nov 10:12 (messages 9 to 12): retried collection on INV-BV-20931 with customer consent given at 09:55. Result: failed, same error, no charge made.
7. James Whitfield, 5 Nov 10:20 (message 11): checked the integration log and release notes. Result: reconnect confirmed; possible v8.2.3 link, unconfirmed.
8. James Whitfield, 5 Nov 11:00: escalated to Tier 2 (Product Engineering Support). Result: done, status Escalated.

## Commitments to the customer
| Commitment | Made by | When | Quote |
| --- | --- | --- | --- |
| Come back to the customer the next morning | Priya Nair, Support Agent Tier 1 | 2026-11-04 15:40 (message 7) | "I'll come back to you tomorrow morning." |
| Look at the payment logs | Priya Nair, Support Agent Tier 1 | 2026-11-04 15:40 (message 7), also referring to an earlier message | "the next step is for me to look at the payment logs on our side" |
| Pass the credit request to Callum Reid | James Whitfield, Support Agent Tier 1 | 2026-11-05 09:40 (message 9) | "I've passed your request to Callum Reid." |
| Escalate to Product Engineering Support | James Whitfield, Support Agent Tier 1 | 2026-11-05 10:40 (message 12) | "I'm escalating this to our Product Engineering Support team now." |
| Update the customer by 16:00 UTC on 5 Nov | James Whitfield, Support Agent Tier 1 | 2026-11-05 10:40 (message 12) | "I'll update you by 16:00 UTC today." |

Status of each:
- The "tomorrow morning" follow-up was effectively met by James's 09:40 message, which came from a different agent.
- The log check was done by James.
- The escalation is done.
- The credit pass-on is unconfirmed.
- The 16:00 update is open, and Tier 2 now owns it (policy 5.2).

Disputed, not a verified commitment: the customer says "as you said in your message yesterday, we'll be expecting October's subscription fee to be credited" (message 8, [Reported]). The credit was not offered in any message in this export, and messages 1 to 6 were not seen. The account record shows Open credits: None recorded. No credit has been validly offered: only Callum Reid (the CSM named in the account record) or the Head of Support may offer one, in writing (policy 6.3). Agents must not promise credits or fix dates (6.2). The customer demands written confirmation of the credit (message 10) and has had no answer. James told the customer that he cannot agree credits.

## Service level
Term: Not determinable: the account record's support level is blank, and the policy sets targets by support level (clause 3.1, with the priority definition at 2.2 and 3.3 for how hours are counted). The first-response and resolution targets cannot be stated.
Clock start: 2026-11-03 14:20 (ticket created, policy 4.1; ticket event log). Clock paused only during "Pending customer", 2026-11-04 09:30 to 15:00 (policy 4.2; ticket event log). Priority P2 (event log).
Deadline: Not determinable: support level missing. Business hours (08:00 to 18:00 London time, which is UTC from 25 Oct; policy 1.1) and the paused time would need to be applied once the level is known.
Status: Not determinable as of 2026-11-05 11:00 (breached, at risk or within target cannot be stated). First response was sent 2026-11-03 15:02, 42 minutes after creation (event log), but its target is also not determinable. Customer update rule for P2 is at least once each business day (policy 7.1); updates are shown on 3, 4 and 5 Nov.

## Recommended next action
Action: Tier 2 (Product Engineering Support) should check whether the v8.2.3 card vault migration to PayCollect v3 left pre-1 Nov saved-card tokens (such as the one on INV-BV-20931, created 14 Oct) missing from the vault. If it did, they should restore or re-migrate those tokens, or give a workaround. They should send the customer the promised update by 16:00 UTC on 5 Nov, even if it only says where the investigation stands.

Reason: logs show a clean split on 1 Nov (31 of 31 failures on older cards, 7 of 7 successes on newer ones), the customer's reconnect did not help, and the API says the token is not in the vault.

It must satisfy:
- The 16:00 UTC update commitment, which Tier 2 now owns (policy 5.2).
- The credit request. Confirm that Callum Reid has it, and tell the customer in writing, without promising a credit, that only Callum (or the Head of Support) can decide, and give the next update time (6.1 to 6.3). Do not promise a fix date.
- First settle the support level, so that the deadline and breach status can be determined. If the ticket is breached, tell the Support Duty Manager (5.3).
- The customer's unanswered impact (declined cards at the desk). Suggest a stopgap if one is found.

Assumptions and checks:
- The v8.2.3 link is unconfirmed. Check by testing a pre-1 Nov token against the v3 vault.
- Re-saving a card may work as a workaround (not tested).
- The credit promise made in messages 1 to 6, if any, is unknown. Read messages 1 to 6 before replying to the customer on credit.
- Priya's earlier reconnect instructions are unseen. Read messages 1 to 6 to avoid repeating them.
