# Escalation handoff: QB-202861 - Card payments failing with "PCX-402 token not found" for cards saved before 1 Nov 2026

Customer: Brackenridge Veterinary Group Ltd (BV-3307) | Tier: Not determinable (support level blank in account record) | Priority: P2 (set on ticket at creation, event log 2026-11-03 14:20 UTC) | Prepared: 2026-11-05 11:00 UTC (export as-of time)

## Service level
Target: Not determinable. Policy 3.1 sets targets by support level (Standard, Business, Enterprise) and policy 1.3 says the level is the one in the account record. The "Support level:" field in the account record is empty (the plan name "Quillbill Clinic" is not a support level). Do not assume one. | Deadline: not determinable | Status: not determinable
Clock facts that do apply (policy 4.1, 4.2, 1.1): clock started at ticket creation 2026-11-03 14:20 UTC; paused while "Pending customer", 2026-11-04 09:30 to 15:00 UTC (5h30m); hours are Europe/London = UTC (GMT) in this period, business hours 08:00-18:00 Mon-Fri.
Time used so far at 11:00 on 5 Nov, excluding the pause: 11h10m business hours (3h40m on 3 Nov, 1h30m + 3h00m on 4 Nov, 3h00m on 5 Nov) or 39h10m calendar hours (44h40m elapsed minus 5h30m). Table lookup for P2 resolution once the level is known: Standard 40 business hours, Business 20 business hours, Enterprise 24 calendar hours (policy 3.1). If Business, it would be breached by 8h50m of business time; if Enterprise, 24 calendar hours already passed (breached); if Standard, 28h50m business hours remain. Confirm the level with the Customer Success Manager or account owner before relying on any of this. Policy 5.3: the Support Duty Manager must be told if a P2 is breached.

## Problem as currently understood
Card payments through the PayCollect integration fail with "PCX-402 token not found" for saved cards, and the customer cannot take payment at the desk. Support's current working view is that cards saved before 1 Nov fail and cards saved on or after 1 Nov succeed, possibly linked to the v8.2.3 release (1 Nov, "Card vault migrated to PayCollect v3"); the link is not confirmed. The customer says all card payments have failed since Monday 2 Nov and that it is not on their side; the logs show a mix of failures and successes, so the customer's "every payment" is broader than the logs.
- [Verified] 38 card payment attempts since 2 Nov 14:00 UTC: 31 failed with "PCX-402 token not found", 7 succeeded (James Whitfield, 2026-11-05 09:40, message 9; checked payment logs)
- [Verified] All 31 failures used cards saved before 1 Nov; all 7 successes used cards saved on or after 1 Nov (James Whitfield, 2026-11-05 09:40, message 9)
- [Verified] Retry of INV-BV-20931 at 10:12 failed again; PayCollect API response "token not found in vault"; token created 14 Oct 2026; no charge made (James Whitfield, 2026-11-05 10:20 internal note, message 11, and 10:40, message 12)
- [Verified] PayCollect connection was re-authorised 4 Nov 14:41 UTC; 14 of the 31 failures occurred after that (James Whitfield, 2026-11-05 10:20, message 11, from integration log)
- [Verified] Release v8.2.3 deployed 1 Nov with note "Card vault migrated to PayCollect v3" (James Whitfield, 2026-11-05 10:20, message 11, from release notes); link to the failures is not confirmed (his words)
- [Reported] Every card payment has failed since Monday; saved cards declined at the desk; customer reconnected PayCollect as instructed (Sunil Mehta, 2026-11-04 17:10, message 8). The reconnect itself is verified by the integration log above.
- [Reported] Customer's client cards declined at the front desk in practices (Sunil Mehta, 2026-11-04 17:10)

## What has been tried
1. Customer reconnected PayCollect following Priya's earlier instructions (content of messages 1-6 not in export) - Sunil Mehta (Reported, message 8); re-authorisation at 4 Nov 14:41 UTC confirmed by integration log (message 11) - No change (failures continued)
2. Priya Nair said she would look at payment logs - 2026-11-04 15:40 (message 7) - Unknown: no result recorded from her
3. Payment log review - James Whitfield, 2026-11-05 09:40 - Partial: identified the pre-1 Nov saved-card pattern, cause not found
4. Retry collection of INV-BV-20931, with customer consent (message 10, 09:55) - James Whitfield, 2026-11-05 10:12 - No change (same error, no charge made)
5. Other steps in messages 1-6 - Unknown: messages 1 to 6 not in the export; James notes he cannot see them (message 11)

## Commitments to the customer
- "I'll come back to you tomorrow morning." - Priya Nair, 2026-11-04 15:40 (message 7) - due morning of 2026-11-05 - met by James's reply at 09:40 (message 9), though that reply was an update on the log check, not a result
- "I've passed your request to Callum Reid." (about the October credit) - James Whitfield, 2026-11-05 09:40 (message 9) - an action already stated as done; no record on the ticket of the hand-off to Callum Reid, so unverified. James also said "I'm not able to agree credits", and no credit has been offered
- "I'll update you by 16:00 UTC today." - James Whitfield, 2026-11-05 10:40 (message 12) - due 2026-11-05 16:00 UTC - open. Under policy 5.2 Tier 2 now owns this.
- "If it succeeds, your client's card will be charged for that invoice. May I go ahead?" - conditional statement, not a promise of outcome; no charge was made.
Claimed by customer, not found in thread: Sunil says Priya said "yesterday" (4 Nov) that October's subscription fee would be credited ("as you said in your message yesterday, we'll be expecting October's subscription fee to be credited"). No such statement in messages 7 to 12; messages 1 to 6 (to 4 Nov 15:00) are not in the export, so it cannot be checked. Also customer demands the credit "confirmed in writing" (message 10). Under policy 6.2 and 6.3 agents may not promise a credit, and only the Customer Success Manager (Callum Reid per account record) or the Head of Support may offer one, in writing on the ticket or account record. Account record shows no open credits.

## Open questions
- What is the customer's support level? The account record field is blank; it decides the service-level target and whether the ticket is already breached.
- What did messages 1 to 6 say (Priya's reconnect steps, any credit wording, any commitment)? Retrieve the full ticket.
- Did the v8.2.3 / PayCollect v3 vault migration drop or fail to migrate tokens saved before 1 Nov? Are other customers affected?
- Exact error, versions and the PayCollect v3 side details are not recorded beyond the above; how many of the customer's 4 practices are affected is not stated.
- Has Callum Reid actually received the credit request, and has the customer received a written answer?
- Are the 7 successful payments consistent with the pre/post 1 Nov pattern for all practices (only counts given)?
- Has the Support Duty Manager been told (policy 5.3, needed if breached)? Not recorded.

## Recommended next action
Check with the PayCollect v3 card vault migration (release v8.2.3, 1 Nov) whether tokens created before 1 Nov, for example the one on INV-BV-20931 (created 14 Oct), exist in the vault, and whether other accounts show the same "PCX-402 token not found" pattern. Reason: the 31 of 31 failures involve pre-1 Nov cards and all 7 successes involve later cards, and the reconnect did not help. In parallel, first confirm the support level on BV-3307 (Customer Success Manager Callum Reid or account owner) to establish the deadline and whether the Duty Manager must be told. Send the customer an update by 2026-11-05 16:00 UTC, the open commitment, and tell them the credit decision belongs to Callum Reid; make no credit promise.
Follow-ups: (1) ask Callum Reid to respond in writing to the credit request on the ticket; (2) retrieve messages 1 to 6 to check the customer's credit claim.
