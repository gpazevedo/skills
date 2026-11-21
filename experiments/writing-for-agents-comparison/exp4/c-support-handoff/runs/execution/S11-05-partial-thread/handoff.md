Clarifying question: The account record for BV-3307 has a blank "Support level" field. What is Brackenridge's support level (Standard, Business or Enterprise)? Policy 1.3 and 3.1 need it for every service-level target. I have not inferred it from the plan name "Quillbill Clinic".

# Escalation handoff: QB-202861 Saved cards saved before 1 Nov fail with "PCX-402 token not found"

**Customer:** Brackenridge Veterinary Group Ltd (BV-3307), plan Quillbill Clinic, support level blank in the record (account record: Plan, Support level)
**Earliest deadline:** 2026-11-05 16:00 UTC, customer update promised by James Whitfield (message 12). 5 hours remain at the as-of time.

## Problem as currently understood
Card payments using saved cards created before 1 Nov 2026 fail with "PCX-402 token not found", and the PayCollect API says the token is not in the vault. Cards saved on or after 1 Nov succeed. The customer's reconnect of PayCollect on 4 Nov did not stop the failures. A possible link to the v8.2.3 card vault migration (deployed 1 Nov) is an open hypothesis.

### Verified
- 38 card payment attempts since 2 Nov 14:00 UTC: 31 failed with "PCX-402 token not found", 7 succeeded (message 9, James Whitfield, 2026-11-05 09:40, from payment logs).
- All 31 failures used cards saved before 1 Nov. All 7 successes used cards saved on or after 1 Nov (message 9).
- Retry of INV-BV-20931 at 10:12 UTC on 5 Nov failed with the same error. The card token was created 14 Oct 2026, and the API response was "token not found in vault" (message 11, internal note, 2026-11-05 10:20). No charge was made (message 12).
- The customer re-authorised PayCollect on 4 Nov at 14:41 UTC. 14 of the 31 failures are after that time (message 11, integration log).
- v8.2.3 was deployed on 1 Nov, and its release notes say "Card vault migrated to PayCollect v3." (message 11).
### Reported, not verified
- Clients' saved cards are declined at the front desk and staff are embarrassed (message 8, Sunil Mehta, 2026-11-04 17:10).
- The customer followed the reconnect instructions "exactly" (message 8). Only the reconnect itself is confirmed by the log, and the instructions are in messages 1 to 6, which were not supplied.
### Contradicted
- "Every single card payment has failed since Monday" (message 8): logs show 7 of 38 attempts succeeded since 2 Nov 14:00 UTC (message 9). Monday is 2 Nov.
### Hypotheses
- Older saved cards have a problem on Quillbill's side, not in the customer's settings, proposed by James Whitfield (message 12, "suggests").
- The v8.2.3 vault migration to PayCollect v3 may be linked to tokens saved before 1 Nov, proposed by James Whitfield, "not confirmed" (message 11).

## Tried so far
| # | Action | By | Result | Source |
| --- | --- | --- | --- | --- |
| 1 | Reconnect steps sent to the customer (content in messages 1 to 6, not supplied) | Priya Nair (instructed) | Result not recorded for the steps as sent | message 7, message 8 |
| 2 | Reconnected PayCollect (re-authorised 2026-11-04 14:41 UTC) | Sunil Mehta | Failures continued (14 after it) | message 8, message 11 |
| 3 | Checked payment logs | James Whitfield | Pattern: 31 failed, all with cards saved before 1 Nov | message 9 |
| 4 | Retried collection on INV-BV-20931 at 10:12 UTC, with customer consent (message 10) | James Whitfield | Failed, "PCX-402 token not found" | message 11, message 12 |
| 5 | Checked release notes for v8.2.3 | James Whitfield | Vault migration noted, link unconfirmed | message 11 |
| 6 | Passed the credit request to Callum Reid (Customer Success Manager) | James Whitfield | Result not recorded | message 9 |

Messages 1 to 6 were not supplied, so earlier attempts may be missing.

## Commitments to the customer
| Commitment (quoted) | Made by | When | Due | Kept / Missed / Open | Source |
| --- | --- | --- | --- | --- | --- |
| "I'll come back to you tomorrow morning." | Priya Nair | 2026-11-04 15:40 UTC | "tomorrow morning" = morning of 2026-11-05, no clock time stated | Kept, by message 9 (09:40 UTC, log findings sent). My reading of "come back". | message 7; message 9 |
| "I'll update you by 16:00 UTC today." | James Whitfield | 2026-11-05 10:40 UTC | 2026-11-05 16:00 UTC | Open, 5 hours remaining | message 12 |

Customer-claimed, not found in thread:
- A promise that October's subscription fee would be credited ("as you said in your message yesterday, we'll be expecting October's subscription fee to be credited") (message 8). No such statement is in messages 7 to 12. Messages 1 to 6 were not supplied, so it cannot be ruled out. The account record shows Open credits: None recorded. No written offer from Callum Reid or the Head of Support is on the ticket (policy 6.3).
- The customer asks for the credit "confirmed in writing" (message 10). This is a request, not a commitment.

## Service level
- Tier and priority: support level is blank in the account record, so the tier is not determinable. Priority is P2, recorded on the ticket in the creation event and the escalation event of 2026-11-05 11:00 UTC (ticket events). Policy 2.2 describes P2 as a major function such as payment collection not working with no practical workaround. Seven attempts with newer cards succeeded, so whether a workaround exists is a question for the engineer.
- Status as of: 2026-11-05 11:00 UTC (the export's as-of time, treated as the current time).

| Target (quoted) | Policy section | Clock start / pauses | Deadline (arithmetic) | Status |
| --- | --- | --- | --- | --- |
| P2 first response (value depends on level; 3.1) | 3.1, 1.4, 4.1 | Start 2026-11-03 14:20 UTC; no pause before first response | Not determinable: support level not recorded | Not determinable. Fact: first agent reply was 15:02 UTC, 42 minutes after creation (ticket events). |
| P2 resolution (value depends on level; 3.1) | 3.1, 4.1 to 4.4 | Start 2026-11-03 14:20 UTC. Pause 2026-11-04 09:30 to 15:00 UTC ("Pending customer"), 5.5 hours. | Not determinable: support level not recorded | Not determinable. Elapsed excluding the pause: 39 h 10 min calendar time (44 h 40 min minus 5.5 h). Business hours (08:00 to 18:00 London, GMT = UTC, per 1.1): 3 h 40 min on 3 Nov + 4 h 30 min on 4 Nov (10 h minus 5.5 h) + 3 h on 5 Nov = 11 h 10 min. |
| P2 customer update, "at least once each business day" | 7.1 | Business day | 5 Nov: updates sent 09:40 and 10:40 UTC | Met for 5 Nov (messages 9, 12). 4 Nov: update at 15:40 UTC (message 7). |

Escalation: the Tier 2 escalation is consistent with 5.1, and Tier 2 now owns the ticket and the commitments above (5.2). Whether the Support Duty Manager must be told depends on whether the ticket is breached (5.3), which cannot be determined without the support level.

## Recommended next action
Investigate whether the v8.2.3 card vault migration to PayCollect v3 left tokens created before 1 Nov (for example the 14 Oct token on INV-BV-20931) missing from the vault, since every failure and no success involves such cards. Send the customer an update by 16:00 UTC today (message 12 commitment), without promising a fix date, credit or refund (policy 6.2). Make sure Callum Reid answers the credit request in writing, because only he or the Head of Support can offer one (policy 6.3).

## Gaps
- Support level is blank in the account record. This blocks the first response and resolution targets, the breach and at-risk status, and whether the Duty Manager must be told (5.3).
- Messages 1 to 6 (2026-11-03 14:20 to 2026-11-04 15:00 UTC) were not supplied. This hides the exact reconnect steps sent, what the customer was asked while "Pending customer", and whether any credit was mentioned.
- No record of whether Callum Reid has received or answered the credit request (message 9 is the only mention).
- The ticket events show P2 but not who first set it. The customer created the ticket via the portal, so P2 may originally have been customer-selected. It is recorded again at escalation.
- The log window starts 2 Nov 14:00 UTC, so the date of the first failure is not stated, and attempts before that are not described.
