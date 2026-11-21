# Handoff: QB-202861, Brackenridge Veterinary Group (BV-3307), card payments failing "PCX-402"

As-of 2026-11-05 11:00 UTC. Escalated to Tier 2 (P2). Export is partial: messages 1 to 6 not seen.

## 1. Problem as understood

Card payments through PayCollect fail with "PCX-402 token not found" for cards saved before 1 November 2026; cards saved on or after 1 November work. A PayCollect card vault migration shipped in v8.2.3 on 1 November and is a possible cause, not confirmed. The customer's reconnect did not fix it. Clients are being declined at the desk.

Evidence:
- Customer states every card payment has failed since Monday (2 Nov) and desk payments with saved cards are declined. Reported, Sunil Mehta, msg 8, 2026-11-04 17:10. The log check below covers the failure pattern but only from 2 Nov 14:00.
- 38 attempts since 2 Nov 14:00 UTC: 31 failed with PCX-402, 7 succeeded. Verified, James Whitfield, payment logs, msg 9, 2026-11-05 09:40.
- All 31 failures used cards saved before 1 Nov; all 7 successes used cards saved on or after 1 Nov. Verified, James Whitfield, msg 9.
- Retry of INV-BV-20931 at 10:12 failed with the same error; API says "token not found in vault"; token created 14 Oct 2026. Verified, James Whitfield, internal note msg 11. No charge was made (msg 12).
- PayCollect was re-authorised 4 Nov 14:41 UTC; 14 of the 31 failures came after it. Verified, James Whitfield, integration log, msg 11.
- v8.2.3 (deployed 1 Nov) release note: "Card vault migrated to PayCollect v3." Verified as the release note text; link to the failures is not confirmed (msg 11).
- Customer states they followed support's earlier reconnect instructions. Reported; the integration log confirms a reconnect happened, but the instructions given in messages 1 to 6 are not visible to us (msg 11).
- Contradiction: James's "problem on our side" (msg 12) is an inference from the pattern, not a confirmed root cause.
- Gap: the log check starts at 2 Nov 14:00 UTC; the customer says failures began Monday (2 Nov). Earlier failures were not checked.

## 2. Tried and result

- Priya Nair: reconnect of PayCollect, per the customer; exact steps unknown (msgs 1 to 6 not seen). Result: failed (failures continue after 14:41 re-authorisation).
- Priya Nair: promised to look at payment logs on 4 Nov (msg 7). Result: no response recorded; James did it on 5 Nov.
- James Whitfield: checked payment logs, 5 Nov 09:40. Result: pattern found (pre-1 Nov cards).
- James Whitfield: retried INV-BV-20931 with customer consent (msg 10), 5 Nov 10:12. Result: failed, same error.
- James Whitfield: passed the credit request to Callum Reid (msg 9). Result: unknown, no reply on the ticket.
- Ruled out: customer-side connection or authorisation (reconnect confirmed, failures persist). Not ruled out: the v8.2.3 vault migration; whether those tokens exist in the v3 vault; whether other pre-1 Nov cards on other practices behave the same.

## 3. Commitments to the customer

- James Whitfield, 2026-11-05 10:40 (msg 12): "I'll update you by 16:00 UTC today." Due 2026-11-05 16:00 UTC. Tier 2 owns it (policy 5.2).
- James Whitfield, 2026-11-05 09:40 (msg 9): passed the credit request to Callum Reid. This is an action taken, not a promise of a credit or of a reply date.
- Priya Nair, 2026-11-04 15:40 (msg 7): "I'll come back to you tomorrow morning." The next customer-facing message was James's at 09:40 on 5 Nov, which gave log findings. Treat as met.
- Unconfirmed, customer's claim only (msg 8): that October's subscription fee would be credited, said to have come from Priya "yesterday" (3 Nov). The message is in messages 1 to 6, which we do not have. No named agent's promise is visible. Policy 6.2 and 6.3 bar support agents from promising credits; only Callum Reid (named in the account record) or the Head of Support may offer one, in writing. No credit is recorded in the account record ("Open credits: None recorded"). Do not confirm or deny it until messages 1 to 6 are checked.
- Customer demand (msg 10), not a commitment: credit confirmed in writing.

## 4. Service-level status and deadline

Not determinable: support level not supplied. The account record's "Support level:" field is blank, and "Quillbill Clinic" is a plan name, not a level. Policy 1.3 takes the level from that field, so I have not inferred one.

Facts that do hold:
- Priority P2 (policy 2.2; set at creation, still P2 at escalation). Clock start 2026-11-03 14:20 UTC (policy 4.1). Timestamps are UTC and Europe/London is GMT in this period (1.1, 1.2). No priority change recorded, so 4.4 does not apply.
- Pause: "Pending customer" 2026-11-04 09:30 to 15:00 UTC, 5.5 hours, excluded (4.2, 4.3).
- Business hours are 08:00 to 18:00 Monday to Friday (1.1). Policy is silent on bank holidays beyond England; 3 to 5 Nov 2026 has none that I know of, which is my assumption.
- Elapsed business hours at 11:00 on 5 Nov: 3 Nov 14:20 to 18:00 = 3h40; 4 Nov 08:00 to 09:30 = 1h30; 4 Nov 15:00 to 18:00 = 3h00; 5 Nov 08:00 to 11:00 = 3h00. Total 11h10.
- Elapsed calendar time: 3 Nov 14:20 to 5 Nov 11:00 = 44h40, minus 5h30 pause = 39h10.
- First response: 3 Nov 15:02 UTC, 42 minutes after creation (policy 1.4; message 2 from Priya, an agent reply). Whether it met the target depends on the level.

What each level would mean (conditional, not a determination; policy 3.1, 4.5):
- Enterprise P2: resolution 24 hours, 24x7. Elapsed 39h10, so breached since about 3 Nov 14:20 + 24h + 5h30 = 5 Nov 07:50 UTC, if the level is Enterprise.
- Business P2: resolution 20 business hours. 11h10 used, 8h50 remaining (44%), so within target; deadline 2026-11-06 09:50 UTC (7h on 5 Nov from 11:00, then 1h50 from 08:00 on Fri 6 Nov). It would be at risk below 5 business hours remaining.
- Standard P2: 40 business hours. 28h50 remaining, within target.
Policy 5.3: if the ticket is breached, the Support Duty Manager must be told. This depends on the level.

## 5. Recommended next action

Primary action: Tier 2 (Product Engineering Support engineer) checks whether card tokens created before 1 Nov 2026, starting with the token on INV-BV-20931 (created 14 Oct), exist in the PayCollect v3 vault after the v8.2.3 migration. If they are missing, the migration dropped them; engineering then decides the repair route. If they exist, the failure lies in the lookup, so check the v8.2.3 integration code. Serves the 16:00 UTC update on 5 Nov.

Rationale: the failures split exactly on 1 Nov (evidence items 2, 3), and the error says the token is missing from the vault (item 4), which fits the migration (item 6) but is not confirmed.

Also, today:
- Someone (Tier 2 or the Support Duty Manager) confirms the account's support level from the contract or Callum Reid, then applies section 4. If it is Enterprise, tell the Support Duty Manager now.
- Pull messages 1 to 6 to see what Priya said about reconnecting and about any credit.
- Tell the customer by 16:00 UTC on 5 Nov, whatever the status: what is confirmed (older saved cards affected, vault migration under investigation), and that new cards saved since 1 Nov work (this may allow a desk workaround, which engineering should confirm first). Do not promise a fix date, release date or credit (6.2). Say that the credit request is with Callum Reid; ask Callum to reply in writing on the ticket.

Missing input to request after this handoff: the account's support level (blank in the account record), and ticket messages 1 to 6.
