# Escalation handoff: QB-202861 Card payments failing with "PCX-402"

**Customer:** Brackenridge Veterinary Group Ltd, account BV-3307, plan Quillbill Clinic (account record, "Support level:" is blank, so Standard/Business/Enterprise is not stated)  **Priority:** P2 (ticket event 2026-11-03 14:20, still P2 at escalation 2026-11-05 11:00)  **Prepared:** 2026-11-05 11:00 UTC (the export's as-of time; GMT = UTC, so business hours are 08:00 to 18:00 UTC, policy 1.1)

## Service level
The support level is blank in the account record, and policy 1.3 says the level is the one recorded there. The deadlines are therefore given under each reading. The ticket was created Tue 2026-11-03 14:20 UTC (policy 4.1). The clock was paused while "Pending customer", 2026-11-04 09:30 to 15:00 = 5h30m (policy 4.2, 4.3; ticket events). No bank holidays fall in the period.

| Clock | Policy clause | Started | Deadline | Status |
|---|---|---|---|---|
| First response, Enterprise P2: 2 hours, 24x7 | 3.1 | 2026-11-03 14:20 | 2026-11-03 16:20 | Met (reply 15:02, after 42 min) |
| First response, Business P2: 4 business hours | 3.1 | 2026-11-03 14:20 | 2026-11-04 08:20 | Met (15:02 Nov 3) |
| First response, Standard P2: 8 business hours | 3.1 | 2026-11-03 14:20 | 2026-11-04 12:20 | Met (15:02 Nov 3) |
| Resolution, Enterprise P2: 24 hours, 24x7 | 3.1, 3.3, 4.5 | 2026-11-03 14:20 | 2026-11-04 19:50 | Breached, 15h10m ago |
| Resolution, Business P2: 20 business hours | 3.1, 3.3, 4.5 | 2026-11-03 14:20 | 2026-11-06 09:50 (if no further pause) | Running, within target, 8h50m left (44%; at risk below 5h) |
| Resolution, Standard P2: 40 business hours | 3.1, 3.3, 4.5 | 2026-11-03 14:20 | 2026-11-10 09:50 (if no further pause) | Running, within target, 28h50m left (72%) |
| Customer update, P2: once each business day | 7.1 | n/a | Each business day | Met for 3, 4 and 5 Nov (messages 2, 7, 9). Separate promise: 16:00 UTC today (see Commitments) |

Arithmetic:
- First response: 15:02 minus 14:20 = 42 minutes, inside business hours. Business P2 deadline: 3h40m left on Nov 3 (to 18:00), so 20m into Nov 4 = 08:20. Standard P2: 4h20m into Nov 4 = 12:20.
- Enterprise resolution: 14:20 Nov 3 plus 24h plus 5h30m paused = 19:50 Nov 4. Elapsed to 11:00 Nov 5 is 44h40m, minus 5h30m paused = 39h10m, which is 15h10m over 24h.
- Business-hours elapsed, paused time excluded: Nov 3 14:20 to 18:00 = 3h40m; Nov 4 10h minus 5h30m paused = 4h30m; Nov 5 08:00 to 11:00 = 3h. Total 11h10m. Business remaining 20h minus 11h10m = 8h50m; 7h today, then 1h50m from 08:00 Nov 6 = 09:50 Nov 6. Standard remaining 40h minus 11h10m = 28h50m; 7h today, 10h Nov 6, 10h Nov 9 (Mon), 1h50m from 08:00 Nov 10 = 09:50 Nov 10.
- Escalation (policy 5.1, 5.3): escalation to Tier 2 happened at 11:00 Nov 5, so 5.2 now applies. Under the Enterprise reading the P2 is breached, so 5.3 requires the Support Duty Manager to be told. The case records no such notice.

## Problem as currently understood
Card payments using saved cards created before 1 Nov 2026 are failing with "PCX-402 token not found" (PayCollect: "token not found in vault"), while cards saved on or after 1 Nov succeed. The most likely cause is that the v8.2.3 release (deployed 1 Nov, "Card vault migrated to PayCollect v3") did not carry older tokens across. That link is suspected, not confirmed. The customer's reconnect of PayCollect did happen and did not fix it.

| Fact | Status | Evidence |
|---|---|---|
| Since 2 Nov 14:00 UTC there were 38 card payment attempts: 31 failed with "PCX-402 token not found", 7 succeeded | Verified | Payment logs read by James Whitfield, message 9 |
| All 31 failures used cards saved before 1 Nov; all 7 successes used cards saved on or after 1 Nov | Verified | Payment logs, message 9 |
| Retry of INV-BV-20931 at 10:12 on 5 Nov failed with the same error; its token was created 14 Oct 2026; API says "token not found in vault"; no charge made | Verified | Retry with customer consent (messages 9, 10), internal note message 11, message 12 |
| PayCollect was re-authorised on 4 Nov at 14:41 UTC and 14 of the 31 failures came after that | Verified | Integration log, message 11 |
| v8.2.3 deployed 1 Nov with "Card vault migrated to PayCollect v3" | Verified (release note exists) | Release notes, message 11 |
| The v3 migration is the cause of the failures on pre-1-Nov tokens | Suspected | Message 11 ("Possible link ... not confirmed"); message 12 ("suggests a problem on our side") |
| "Every single card payment has failed since Monday" | Reported, only partly verified: logs show 7 successes, all on newer cards | Message 8 vs message 9 |
| Clients' saved cards are declined at the front desk, staff embarrassed | Reported | Message 8 (the log error is a missing token, not a decline) |
| Customer reconnected PayCollect as instructed, so the fault is not on their side | Reported (the reconnect itself is verified above) | Message 8; message 11 |
| Scope beyond this account (other customers on pre-1-Nov tokens), and the split across the 4 practices | Not known | Not in the case; account lists 4 practices (front-desk add-on) |
| Logs before 2 Nov 14:00 UTC | Not stated | Message 9 gives no earlier window; first failure time is unknown |

Contradictions:
- Customer says every card payment has failed since Monday (message 8); the logs show 7 of 38 attempts succeeded (message 9). Both kept. The 7 successes all used cards saved on or after 1 Nov.
- Customer says credit for October's fee was promised "as you said in your message yesterday" (message 8). The ticket messages 1 to 6 are not in this export, and nothing here shows such a statement. The account record shows "Open credits: None recorded". Policy 6.2 and 6.3 bar support agents from promising credits. Unresolved; see Commitments.
- Message 7 (Priya) says the log check was already announced "in my earlier message"; message 8 says Priya's earlier message told them to reconnect. Messages 1 to 6 are missing and message 11 says James cannot see them, so neither is verified.

## What has been tried
| When | Who | Action | Result |
|---|---|---|---|
| Before 2026-11-04 15:00 (messages 1 to 6, not supplied) | Priya Nair / customer | Reconnect steps sent by Priya, per the customer; other steps unknown | Not in export; reconnect was done by the customer (see next row) |
| 2026-11-04 14:41 | Customer (Sunil Mehta) | Re-authorised the PayCollect connection | Did not fix: 14 of 31 failures came after it (message 11); message 7 "reconnect didn't help" |
| 2026-11-05 09:40 | James Whitfield | Read payment logs | 38 attempts, 31 failed, 7 succeeded; pattern by card save date |
| 2026-11-05 10:12 | James Whitfield | Retry collection on INV-BV-20931 (customer agreed in message 10) | Failed, "PCX-402 token not found", no charge |
| 2026-11-05 09:40 | James Whitfield | Passed the October credit request to Callum Reid (message 9) | Result not recorded; no reply from Callum in the case |
| 2026-11-05 10:20 | James Whitfield | Checked release notes | v8.2.3 note found; link not confirmed |
| 2026-11-05 11:00 | James Whitfield | Escalated to Tier 2 | Status Escalated, P2 |

## Commitments to the customer
| When | Made by | Commitment (quoted) | Due | State |
|---|---|---|---|---|
| 2026-11-04 15:40 | Priya Nair | "I'll come back to you tomorrow morning." (after looking at the payment logs) | Morning of 2026-11-05 | Met: message 9 at 09:40 UTC with the log findings |
| 2026-11-05 09:40 | James Whitfield | "I've passed your request to Callum Reid." (on the October credit) | n/a (no time given) | Open: no response from Callum recorded; customer wants it "in writing, not passed around" (message 10) |
| 2026-11-05 10:40 | James Whitfield | "I'll update you by 16:00 UTC today." | 2026-11-05 16:00 UTC | Open. Tier 2 now owns it (policy 5.2) |
| Claimed by customer, 2026-11-04 17:10 | Customer says "your message yesterday" | Credit for October's subscription fee (customer's words: "we'll be expecting October's subscription fee to be credited") | n/a | Reported only; not in the supplied messages and not in the account record (no credits recorded); an offer is valid only if written on the ticket or account by the CSM or Head of Support (policy 6.3) |

No credit, fix date or refund has been confirmed anywhere in the supplied case.

## Recommended next action
Confirm or rule out the suspected cause: look up the card token behind INV-BV-20931 (created 14 Oct 2026) in the PayCollect v3 vault and in the pre-migration vault, and compare with a second pre-1-Nov token on BV-3307 and one post-1-Nov token that succeeded. Use the v8.2.3 vault-migration job logs and the PayCollect API to do it.
- Confirmed if: the 14 Oct token exists in the old vault but is missing from v3 (and other pre-1-Nov tokens are missing too, while newer tokens are present). Then the migration did not carry tokens over, and the engineering fix is to re-migrate or map them.
- Ruled out if: the token is present in v3. Then look at the 4 Nov re-authorisation (credentials or merchant mapping) and the failures before 14:41 on 4 Nov.
- Racing: the 16:00 UTC update promised today, and the resolution deadline, which is already passed under Enterprise (19:50 Nov 4), 09:50 Nov 6 under Business, and 09:50 Nov 10 under Standard. Send a short update by 16:00 stating what is verified, with no fix date, credit or refund (policy 6.2).

Open questions:
- What is the account's real support level? The field is blank; it decides whether this ticket is already breached (Enterprise) and whether the Duty Manager must be told (policy 5.3).
- Did Callum Reid receive the credit request, and will he reply in writing on the ticket (policy 6.3)? Did anyone actually promise the October credit in messages 1 to 6?
- What did messages 1 to 6 say (reconnect steps, first reports)? James cannot see them (message 11).
- When did failures first appear? The log window starts 2 Nov 14:00; the release went out 1 Nov.
- Are other customers with pre-1-Nov saved tokens affected, and is this a P1 or P2 trend? The scope beyond BV-3307 is not stated.
- Is a workaround practical (new cards succeed)? That decides P2 versus P3 under policy 2.2 and 2.3; priority stays as recorded unless an agent changes it (policy 2.5).
