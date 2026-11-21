# Handoff: ticket QB-202861 (Brackenridge Veterinary Group Ltd, BV-3307)

Inputs: thread (partial export, messages 7 to 12 only; messages 1 to 6 not provided), account record, policy v4.2. As-of time 2026-11-05 11:00 UTC.

## 1. Summary
Since about 2 November, card payments on saved cards fail with "PCX-402 token not found" at all of the customer's practices; the ticket is P2 and was escalated to Tier 2 at 11:00 UTC on 5 Nov. Urgency is high: the SLA status cannot be settled because the account record has no support level, and a customer update is due by 16:00 UTC today.

## 2. Problem as understood
Reported (customer or support assertion, no check shown):
- "Every single card payment has failed since Monday" (Sunil, msg 8). The log shows 7 successes, so "every" is not accurate.
- Clients' saved cards are declined at the desk (msg 8).
- The customer says they followed support's earlier reconnect instructions (msg 8). Those instructions are in messages 1 to 6, which were not provided.
- Priya says she told the customer the next step was to check payment logs (msg 7). This is in an earlier message that was not provided.
- The failures are "a problem on our side with older saved cards" (James, msg 12). This is an inference.
- v8.2.3 may be linked to the failures (msg 11: "not confirmed").

Verified (source):
- Since 2 Nov 14:00 UTC: 38 card payment attempts, 31 failed with "PCX-402 token not found", 7 succeeded (payment logs, msg 9).
- All 31 failures used cards saved before 1 Nov; all 7 successes used cards saved on or after 1 Nov (payment logs, msg 9).
- Retry of INV-BV-20931 at 10:12 UTC on 5 Nov failed with the same error; the token was created 14 Oct 2026; the PayCollect API says "token not found in vault" (internal note, msg 11). No charge was made (msg 12).
- PayCollect was re-authorised on 4 Nov at 14:41 UTC; 14 of the 31 failures are after that time (integration log, msg 11). The reconnect did happen and did not fix it.
- v8.2.3 was deployed on 1 Nov; release notes say "Card vault migrated to PayCollect v3." (release notes, msg 11).
- Ticket created 3 Nov 14:20 UTC as P2 by Sunil Mehta (ticket event log).
- Account has no open credits and no flags (account record).

## 3. Tried so far
| Action | By | Result |
| --- | --- | --- |
| Reconnect PayCollect (instructions in messages 1 to 6, not seen) | Customer, per Priya's instructions | Failed. Re-authorisation logged 4 Nov 14:41 UTC; failures continue (14 after it). |
| Other steps in messages 1 to 6 | Priya Nair | Unknown. Not visible to James or in this export. |
| Check payment logs | James Whitfield, 5 Nov 09:40 | Worked as diagnosis: found the pre-1 Nov token pattern. |
| Retry collection on INV-BV-20931 (customer consented, msg 10) | James Whitfield, 10:12 | Failed, same error. Confirms the error is reproducible on a pre-1 Nov token. |
| Check integration log | James Whitfield | Confirmed the reconnect happened; inconclusive on cause. |
| Request for October credit passed to Callum Reid | James Whitfield, msg 9 | Unknown. No reply from Callum in the material. |
| Escalation to Tier 2 | James Whitfield, 11:00 | Done. |

## 4. Commitments to the customer
Tier 2 owns these from escalation (policy 5.2).
- "I'll update you by 16:00 UTC today." James Whitfield, 5 Nov 10:40 (msg 12). Valid under policy 6.1. Due 16:00 UTC 5 Nov; Tier 2 must send it.
- "I've passed your request to Callum Reid." James Whitfield, 5 Nov 09:40 (msg 9). An action by James, not a promise of a credit. Nothing shows Callum has acted. The customer asked for written confirmation (msg 10).
- "I'll come back to you tomorrow morning." Priya Nair, 4 Nov 15:40 (msg 7), meaning 5 Nov morning. James's 09:40 reply, after reassignment, arguably meets it; unclear whether the customer sees it that way.
- Customer asserts: "as you said in your message yesterday, we'll be expecting October's subscription fee to be credited" (msg 8). The customer attributes this to a message from 4 Nov or earlier. The source message is not in the export, so whether any agent promised a credit is unclear. Quote the customer's text, not an agent promise. Policy 6.2 and 6.3 bar agents from promising a credit; only Callum Reid (CSM in the account record) or the Head of Support may offer one, in writing on the ticket or account record. No credit is recorded (account record "Open credits: None recorded").
- Do not promise a fix date, release date, credit or refund (policy 6.2).

## 5. Service level
Status: undetermined.
- Account record "Support level:" is blank. Policy 1.3 says the level is the one recorded in the account record, so the target is "not stated in provided material". Needed: the support level for BV-3307 (from Callum Reid, Dr Fiona Brackenridge's contract, or the account system).
- Priority: P2, as created and still P2 (event log, policy 2.2). Clock starts at ticket creation (policy 4.1): 2026-11-03 14:20 UTC. Paused only in "Pending customer" (4.2): 4 Nov 09:30 to 15:00 UTC = 5h30m.
- Business hours are 08:00 to 18:00 London time, Mon to Fri; London is GMT=UTC in November (policy 1.1). No bank holiday falls in the period.
- Elapsed business time, 3 Nov 14:20 to 5 Nov 11:00: 3 Nov 14:20 to 18:00 = 3h40m; 4 Nov 08:00 to 09:30 = 1h30m (paused after 09:30 until 15:00); 4 Nov 15:00 to 18:00 = 3h; 5 Nov 08:00 to 11:00 = 3h. Total 11h10m.
- Elapsed calendar time excluding the pause: 3 Nov 14:20 to 5 Nov 11:00 = 44h40m, minus 5h30m = 39h10m.
- Conditional on each level (P2 resolution, policy 3.1 and 3.3):
  - Standard, 40 business hours: 28h50m remain (72%). Within target. Deadline: 7h on 5 Nov, 10h on 6 Nov, 10h on 9 Nov = 27h; 1h50m more on 10 Nov, so 09:50 UTC 10 Nov (if no further pause).
  - Business, 20 business hours: 8h50m remain (44%, above the 25% threshold in 4.5). Within target. Deadline: 7h on 5 Nov, then 1h50m on 6 Nov, so 09:50 UTC 6 Nov (if no further pause).
  - Enterprise, 24 hours 24x7 calendar: 39h10m elapsed exceeds 24h. Breached; the deadline passed about 15h10m ago. At 24h elapsed the clock reached 24h at 3 Nov 14:20 + 24h + 5h30m pause = 5 Nov 01:50 UTC.
- First response: 3 Nov 15:02, 42 minutes after creation (event log). This is within any level's P2 first-response target (Enterprise 2h, Business 4 business hours, Standard 8 business hours).
- Escalation: policy 5.1 allows escalation of a P2; the Duty Manager must be told if a P2 is breached (5.3). Under the Enterprise case that applies.
- Customer updates: P2 needs an update at least once each business day (7.1). Updates were sent 4 Nov (msg 7) and 5 Nov (msgs 9, 12).

## 6. Recommended next action
Work first on the root cause: investigate why saved tokens created before 1 Nov are "not found in vault" after the v8.2.3 Card vault migration to PayCollect v3 (deployed 1 Nov), and whether the old tokens can be migrated or re-pointed to the v3 vault. Reasons: all 31 failures involve pre-1 Nov tokens, all 7 successes involve later ones, the failures continue after the customer's re-authorisation, and the retry reproduced the error. This is a product-side fault with no practical workaround for saved cards (which fits P2). Check whether other customers' pre-1 Nov tokens are affected, and consider whether that raises the priority (P1 if payment data is judged lost; policy 2.1, set only by an agent recording it, 2.5).

Before the deadline and today:
1. Look up the BV-3307 support level (ask Callum Reid or check the contract) and record it on the ticket. Then the SLA status in section 5 can be settled; if Enterprise, tell the Support Duty Manager now (5.3).
2. Send the customer an update by 16:00 UTC today (own commitment from msg 12), even if only to say what is being checked. Do not give a fix date.
3. Ask Callum Reid to answer the credit request in writing on the ticket or the account record; the customer demanded written confirmation. Only he or the Head of Support may offer it.
4. Possible interim workaround to check with the customer: re-saving the card (new tokens saved on or after 1 Nov all succeeded, 7 of 7). This is an inference from the log, not tested; confirm before suggesting it, and note the customer is embarrassed at the desk.

Questions for the customer, only if they block progress: which reconnect steps were followed, and whether any client's card re-saved after 1 Nov has succeeded.

## 7. Gaps
- Messages 1 to 6 (3 Nov 14:20 to 4 Nov 15:00 UTC) are missing. This hides the reconnect instructions, the attempts by Priya, and the "message yesterday" the customer claims promised a credit.
- Account record has no support level, so targets and SLA status cannot be settled.
- No reply from Callum Reid on the credit request.
- Link between v8.2.3 and the failures is not confirmed.
- Customer says every payment has failed; the log shows 7 of 38 succeeded. Impact on desk payments versus online payments is not broken down.
- Whether other customers are affected is unknown.
- Support-level, bank-holiday and pause assumptions: no further pause after 11:00 on 5 Nov is assumed; status is Escalated.
