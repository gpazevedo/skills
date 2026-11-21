Clarifying question: The account record's "Support level" field for BV-3307 is blank. What is Brackenridge Veterinary Group's support level (Standard, Business or Enterprise)? Also, can you supply messages 1 to 6 of ticket QB-202861?

# Escalation handoff: QB-202861 Saved-card payments failing with "PCX-402 token not found" for cards saved before 1 Nov

**Customer:** Brackenridge Veterinary Group Ltd, account BV-3307, plan Quillbill Clinic (annual subscription, billed monthly); support level blank in record (account record: Account ID, Plan, Support level)
**Earliest deadline:** 2026-11-05 16:00 UTC, customer update promised by James Whitfield (message 12). Tier 2 now owns this commitment (policy 5.2). Service-level deadlines cannot be determined until the support level is known.

## Problem as currently understood
Since at least 2 Nov 14:00 UTC, card payments on this account fail with "PCX-402 token not found" whenever the saved card was stored before 1 Nov. Cards saved on or after 1 Nov succeed. The failures continue after the customer re-authorised PayCollect. James Whitfield's open hypothesis is that the v8.2.3 card vault migration to PayCollect v3 (deployed 1 Nov) did not carry over older tokens. This is not confirmed.

### Verified
- Since 2 Nov 14:00 UTC there were 38 card payment attempts. 31 failed with "PCX-402 token not found" and 7 succeeded (message 9, James Whitfield, payment logs)
- All 31 failures used cards saved before 1 Nov. All 7 successes used cards saved on or after 1 Nov (message 9, payment logs)
- Retry of INV-BV-20931 at 10:12 on 5 Nov failed with "PCX-402 token not found", and no charge was made (message 11, message 12)
- The card token on INV-BV-20931 was created on 14 Oct 2026 (message 11)
- PayCollect API response for the retry: "token not found in vault" (message 11)
- PayCollect connection was re-authorised on 4 Nov at 14:41 UTC, so the customer's reconnect did happen (message 11, integration log)
- Failures continue after the reconnect: 14 of the 31 failures were after 14:41 on 4 Nov (message 11)
- Release v8.2.3 was deployed on 1 Nov with the release note "Card vault migrated to PayCollect v3" (message 11, release notes)

### Reported, not verified
- Failures started on Monday (2 Nov). The logs cover attempts from 2 Nov 14:00 UTC onward, which does not establish when the failures began (message 8, Sunil Mehta; log window in message 9)
- Clients collecting pets had their saved card declined at the desk, which embarrassed staff (message 8, Sunil Mehta)
- The customer followed the earlier reconnect instructions "exactly". The reconnect itself is verified, but the instructions are in messages 1 to 6, which are not supplied (message 8; message 11)
- "this is not on our side" (message 8, Sunil Mehta)

### Contradicted
- "every single card payment has failed since Monday": the logs show 7 of 38 attempts since 2 Nov 14:00 UTC succeeded, all on cards saved on or after 1 Nov (message 8; message 9)

### Hypotheses
- The fault is on Quillbill's side with older saved cards, not in the customer's settings. Proposed by James Whitfield (message 12)
- The v8.2.3 vault migration to PayCollect v3 is linked to failures on tokens saved before 1 Nov ("not confirmed"). Proposed by James Whitfield (message 11)

## Tried so far
| # | Action | By | Result | Source |
| --- | --- | --- | --- | --- |
| 1 | Anything tried in messages 1 to 6 | Unknown | Not determinable: messages 1 to 6 not supplied | thread header; message 11 |
| 2 | Reconnected PayCollect, following support's earlier instructions | Customer (Sunil Mehta / practice) | Re-authorised 4 Nov 14:41 UTC; failures continued (14 after reconnect) | messages 7, 8, 11 |
| 3 | Checked Quillbill payment logs | James Whitfield | 38 attempts, 31 failed with PCX-402 (all on cards saved before 1 Nov), 7 succeeded (all on cards saved on or after 1 Nov) | message 9 |
| 4 | Retried collection on INV-BV-20931 at 10:12 on 5 Nov, with the customer's consent | James Whitfield | Failed, "PCX-402 token not found"; API: "token not found in vault"; no charge | messages 10, 11, 12 |
| 5 | Checked the integration log for the reconnect | James Whitfield | Reconnect confirmed at 4 Nov 14:41 UTC | message 11 |
| 6 | Checked release notes | James Whitfield | v8.2.3 (1 Nov): "Card vault migrated to PayCollect v3" | message 11 |

## Commitments to the customer
| Commitment (quoted) | Made by | When | Due | Kept / Missed / Open | Source |
| --- | --- | --- | --- | --- | --- |
| "the next step is for me to look at the payment logs on our side" | Priya Nair | 2026-11-04 15:40 UTC | No time stated | Kept: James Whitfield checked the logs after the reassignment (message 9) | message 7 |
| "I'll come back to you tomorrow morning." | Priya Nair | 2026-11-04 15:40 UTC | "tomorrow morning" = morning of 2026-11-05 | Kept: James Whitfield replied at 09:40 UTC on 5 Nov (message 9) | message 7 |
| "I'm escalating this to our Product Engineering Support team now." | James Whitfield | 2026-11-05 10:40 UTC | "now" | Kept: escalated to Tier 2 at 11:00 UTC (event log) | message 12 |
| "I'll update you by 16:00 UTC today." | James Whitfield | 2026-11-05 10:40 UTC | "16:00 UTC today" = 2026-11-05 16:00 UTC | Open (as of 2026-11-05 11:00 UTC). Tier 2 owns it (policy 5.2) | message 12 |

Customer-claimed, not found in thread:
- A credit of October's subscription fee, which the customer says support promised: "as you said in your message yesterday, we'll be expecting October's subscription fee to be credited". The message it refers to (3 Nov) falls in messages 1 to 6, which are not supplied, so the claim cannot be checked against the thread (message 8)
- Context for the claim above: James Whitfield said he cannot agree credits and passed the request to CSM Callum Reid (message 9). The customer asked for it "confirmed in writing, not passed around" (message 10). The account record shows "Open credits: None recorded" and CSM Callum Reid (account record). Under policy, support agents must not promise a service credit (6.2). Only the named CSM or the Head of Support may offer one, and the offer is valid only in writing on the ticket or account record (6.3)

## Service level
- Tier and priority: support level not determinable, because the "Support level" field in the account record is blank (account record; policy 1.3). Priority P2, set at ticket creation and confirmed at escalation (event log 2026-11-03 14:20 and 2026-11-05 11:00 UTC)
- Status as of: 2026-11-05 11:00 UTC, the last thread timestamp. The supplied material does not give the current time
- Time zone: thread timestamps are UTC, and Europe/London is GMT = UTC between 25 Oct 2026 and 28 Mar 2027 (thread header; policy 1.1, 1.2). No assumption needed. 2 Nov 2026 is a Monday and there are no English bank holidays in the period
- Clock: started 2026-11-03 14:20 UTC (ticket created, policy 4.1). Paused 2026-11-04 09:30 to 15:00 UTC (Pending customer, 5 h 30 m, policy 4.2 to 4.3) (event log)
- Elapsed as of 2026-11-05 11:00 UTC: business hours 3 h 40 m (3 Nov 14:20 to 18:00) + 1 h 30 m (4 Nov 08:00 to 09:30) + 3 h (4 Nov 15:00 to 18:00) + 3 h (5 Nov 08:00 to 11:00) = 11 h 10 m. Calendar 44 h 40 m − 5 h 30 m paused = 39 h 10 m

| Target (quoted) | Policy section | Clock start / pauses | Deadline (arithmetic) | Status |
| --- | --- | --- | --- | --- |
| First response, P2 (value depends on support level) | 3.1, 1.4 | Start 2026-11-03 14:20 UTC; first response sent 15:02 UTC (message 2, event log) | Not determinable: support level missing. Response came 42 min after creation | Not determinable. Assessment: 42 min is within every P2 first-response value in 3.1 (shortest is Enterprise, 2 hours 24x7) |
| Resolution, P2 (value depends on support level) | 3.1, 3.3, 4.5 | Start 2026-11-03 14:20 UTC; paused 5 h 30 m | Not determinable: support level missing. See the conditional lines below | Not determinable |
| "P2 tickets: an update at least once each business day." | 7.1 | Last customer update 2026-11-05 10:40 UTC (message 12) | Update for 5 Nov sent at 10:40. Next due by end of business day Fri 6 Nov = 2026-11-06 18:00 UTC (policy 1.1) | Met for 5 Nov. Not yet due for 6 Nov (31 h remaining in calendar time from 11:00 on 5 Nov) |

Resolution deadline for each possible support level. This is for planning only and is not a status, because the customer's level is unknown:
- Enterprise P2 "24 hours, 24x7": 2026-11-03 14:20 + 24 h + 5 h 30 m paused = 2026-11-04 19:50 UTC. Would be breached by 15 h 10 m, which would require telling the Support Duty Manager (policy 5.3)
- Business P2 "20 business hours": 20 h − 11 h 10 m = 8 h 50 m remaining. 7 h on 5 Nov (to 18:00), then 1 h 50 m on 6 Nov = 2026-11-06 09:50 UTC. Within target now; "at risk" once less than 5 h remains, from 2026-11-05 15:00 UTC (policy 4.5)
- Standard P2 "40 business hours": 40 h − 11 h 10 m = 28 h 50 m remaining. 7 h (5 Nov) + 10 h (6 Nov) + 10 h (9 Nov) + 1 h 50 m (10 Nov) = 2026-11-10 09:50 UTC. Within target now; at risk once less than 10 h remains, from 2026-11-09 08:00 UTC (policy 4.5)

## Recommended next action
Check whether card tokens saved for BV-3307 before 1 Nov were carried into the PayCollect v3 vault in the v8.2.3 migration, starting with the 14 Oct token on INV-BV-20931 that returns "token not found in vault". All 31 failures are on tokens from before 1 Nov and all 7 successes are on newer tokens, and the reconnect has already been verified and ruled out. Send the customer the update James Whitfield promised by 2026-11-05 16:00 UTC, and confirm the support level now, since under Enterprise terms the ticket would already be breached and the Duty Manager would need to be told.

## Gaps
- Account record "Support level" is blank. This blocks the first-response and resolution targets, the breach and at-risk status, and whether the Duty Manager must be told (policy 5.3). It also leaves open whether the customer has the active support agreement the policy requires (policy preamble)
- Messages 1 to 6 are not supplied. They hold the original report, the reconnect instructions, anything else tried, and the 3 Nov message where the customer says a credit was promised. James Whitfield cannot see them either (message 11)
- Current time is not in the supplied material. All statuses are as of 2026-11-05 11:00 UTC. If it is now past 16:00 UTC on 5 Nov and no update was sent, the update commitment is Missed
- Credit request: passed to CSM Callum Reid (message 9). No response is recorded in the thread, and the account record shows no open credits
- Failure onset before 2 Nov 14:00 UTC is not covered by the log figures given (message 9)
