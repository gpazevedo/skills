# Escalation handoff: QB-202861 - Card payments with saved cards from before 1 Nov fail with "PCX-402 token not found"

Customer: Brackenridge Veterinary Group Ltd (BV-3307) | Tier: Not determinable (the account record's "Support level" field is blank) | Priority: P2, set on ticket (event log, 2026-11-03 14:20 UTC; reconfirmed at escalation, 2026-11-05 11:00 UTC) | Prepared: as of 2026-11-05 11:00 UTC (escalation event, latest timestamp in the case; the actual current time is not given in the case, so recompute status when you read this)

## Service level
Resolution target: Not determinable. Policy 3.1 sets P2 targets by support level, and the account record leaves the support level blank (policy 1.3: the level is "the level recorded in the customer's account record").
Arithmetic that does not depend on tier: clock start 2026-11-03 14:20 UTC (ticket created; policy 4.1). Paused 2026-11-04 09:30 to 15:00 UTC, 5h30m in Pending customer (policy 4.2). Business hours 08:00-18:00 Mon-Fri, GMT = UTC (policy 1.1). Business hours counted by 11:00 on 5 Nov: 3h40m (3 Nov) + 1h30m + 3h00m (4 Nov) + 3h00m (5 Nov) = 11h10m.
Deadline depends on the level, so here is each one for reference only: Business "20 business hours" gives Fri 2026-11-06 09:50 UTC (8h50m left at 11:00 on 5 Nov, 44%, within target). Standard "40 business hours" gives Tue 2026-11-10 09:50 UTC. Enterprise "24 hours, 24x7" gives Wed 2026-11-04 19:50 UTC, which would already be breached by 15h10m at escalation and would require telling the Support Duty Manager (policy 5.3).
First response: Met at every level. Sent 2026-11-03 15:02 UTC, 42 minutes after creation (event log); the shortest P2 first-response target is Enterprise "2 hours, 24x7".

## Problem as currently understood
Since about 2 Nov, card payments through the PayCollect integration fail with "PCX-402 token not found" when the saved card was stored before 1 November; cards saved on or after 1 November succeed. The pattern lines up with v8.2.3 (deployed 1 Nov, "Card vault migrated to PayCollect v3"), but nobody has confirmed the link. The customer says every card payment has failed; the logs show 7 of 38 succeeded.
- [Verified] Since 2 Nov 14:00 UTC: 38 card payment attempts, 31 failed with "PCX-402 token not found", 7 succeeded (James Whitfield, checked payment logs, msg 9, 2026-11-05 09:40 UTC)
- [Verified] All 31 failures used cards saved before 1 Nov; all 7 successes used cards saved on or after 1 Nov (James Whitfield, msg 9, 2026-11-05 09:40 UTC)
- [Verified] Retry on INV-BV-20931 failed with the same error; its card token was created 14 Oct 2026; the PayCollect API response says "token not found in vault" (James Whitfield, internal note msg 11, 2026-11-05 10:20 UTC)
- [Verified] v8.2.3 release notes (deployed 1 Nov): "Card vault migrated to PayCollect v3." James calls the link "Possible ... not confirmed" (James Whitfield, msg 11, 2026-11-05 10:20 UTC)
- [Reported] "every single card payment has failed since Monday"; saved cards declined at the desk when clients collect pets (Sunil Mehta, customer, msg 8, 2026-11-04 17:10 UTC). The logs in msg 9 contradict "every single".

## What has been tried
1. Steps in messages 1-6 (2026-11-03 14:20 to 2026-11-04 15:00 UTC) - Priya Nair and customer - Unknown: no result recorded. Those messages are not in the export, and James notes he cannot see them (msg 11).
2. Reconnect of PayCollect, following Priya's earlier instructions - customer; [Reported] by Sunil Mehta (msg 8, 2026-11-04 17:10 UTC); [Verified] re-authorisation at 2026-11-04 14:41 UTC in the integration log (James Whitfield, msg 11, 2026-11-05 10:20 UTC) - No change: 14 of the 31 failures came after 14:41 on 4 Nov (James Whitfield, msg 11).
3. Payment log review - James Whitfield, 2026-11-05, before 09:40 UTC - Partial: found the before/after 1 Nov saved-card pattern; no fix (msg 9).
4. Retry of collection on INV-BV-20931, with customer consent (Sunil Mehta, msg 10, 09:55 UTC) - James Whitfield, 2026-11-05 10:12 UTC - No change: failed again with "PCX-402 token not found"; no charge made (msg 11, msg 12).

## Commitments to the customer
Tier 2 now owns these (policy 5.2).
- "the next step is for me to look at the payment logs on our side. I'll come back to you tomorrow morning." - Priya Nair, 2026-11-04 15:40 UTC (msg 7) - due 2026-11-05 morning - met (James Whitfield checked the logs and replied at 2026-11-05 09:40 UTC, msg 9)
- "I'd like to retry the collection on one failed invoice, INV-BV-20931" - James Whitfield, 2026-11-05 09:40 UTC (msg 9) - due none stated - met (retried 10:12 UTC, result sent 10:40 UTC, msgs 11-12)
- "I've passed your request to Callum Reid." - James Whitfield, 2026-11-05 09:40 UTC (msg 9) - due none stated - met as stated; no reply from Callum Reid appears in the thread
- "I'm escalating this to our Product Engineering Support team now." - James Whitfield, 2026-11-05 10:40 UTC (msg 12) - due immediately - met (escalation event 11:00 UTC)
- "I'll update you by 16:00 UTC today." - James Whitfield, 2026-11-05 10:40 UTC (msg 12) - due 2026-11-05 16:00 UTC - open

Claimed by customer, not found in thread: Credit of October's subscription fee, "as you said in your message yesterday" (Sunil Mehta, msg 8, 2026-11-04 17:10 UTC). "Yesterday" points to Priya's messages of 3 Nov, which are in the missing messages 1-6, so this cannot be checked against the export. Note: policy 6.2 bars support agents from promising a service credit, policy 6.3 makes an offer valid only from the Customer Success Manager (Callum Reid) or Head of Support and only when recorded in writing, and the account record shows "Open credits: None recorded". The customer has asked for written confirmation (msg 10, 09:55 UTC).

## Open questions
- What support level is BV-3307 on? (Account record field is blank; this sets the resolution deadline.)
- What did messages 1-6 say: the original problem report, Priya's reconnect steps, and whether any credit wording was used?
- Did the v8.2.3 vault migration to PayCollect v3 carry over tokens created before 1 Nov for this account, and are other accounts with older saved cards seeing PCX-402?
- How many saved cards on BV-3307 (across its 4 practices) were created before 1 Nov, and so are likely to fail?
- Is re-saving a card a usable workaround? The 7 successes used cards saved on or after 1 Nov, but no one has tested re-saving a failing card.
- Has Callum Reid responded on the credit request?

## Recommended next action
Check the PayCollect v3 vault for account BV-3307: look up the token on INV-BV-20931 (created 14 Oct 2026) and compare the v8.2.3 migration record with the vault for tokens created before 1 Nov. Why: all 31 failures, and only those, use cards saved before 1 Nov; the API says "token not found in vault"; the vault migration shipped on 1 Nov; reconnecting changed nothing (msgs 9 and 11). Deadline: send the customer update promised for 2026-11-05 16:00 UTC, which is the nearest deadline, with whatever this check has found by then.
Follow-ups: (1) If the tokens were not migrated, say whether they can be restored or whether the cards must be saved again, so support can offer a workaround and close the target. (2) Get the support level for BV-3307 to fix the resolution deadline (it would be 2026-11-06 09:50 UTC on Business); if it is Enterprise, the ticket is already breached and the Support Duty Manager must be told (policy 5.3).

---
Missing input: the account record is supplied, but its support level is blank. With it, the resolution deadline and status could be stated. Messages 1-6 of the thread are also missing; with them, the earlier attempts and the October credit claim could be checked.
