# Escalation handoff: QB-202861 Card payments with cards saved before 1 Nov fail with "PCX-402 token not found"

Reference time ("now"): 2026-11-05 10:40 UTC (last thread message, message 12; the escalation event at 11:00 UTC follows it)
Inputs missing: none of the three inputs is absent, but two parts are: the thread is a partial export (messages 1 to 6, 2026-11-03 14:20 to 2026-11-04 15:00 UTC, are not included; the event log is complete), and the account record's "Support level" field is blank.

## Problem as currently understood
Saved-card payments for Brackenridge Veterinary Group (BV-3307) through the PayCollect integration are failing with "PCX-402 token not found". Support's logs show every failure since 2 Nov 14:00 UTC used a card saved before 1 Nov, and every success used a card saved on or after 1 Nov. The customer's PayCollect reconnect did happen and did not stop the failures. Support suspects the card vault migration to PayCollect v3 in release v8.2.3 (deployed 1 Nov); nothing has confirmed it.
- Every card payment has failed since Monday (2 Nov) [reported] (Sunil Mehta, message 8, 2026-11-04 17:10 UTC)
- Clients' saved cards are declined at the front desk when they collect their pets [reported] (Sunil Mehta, message 8, 2026-11-04 17:10 UTC)
- Since 2 Nov 14:00 UTC: 38 card payment attempts, 31 failed with "PCX-402 token not found", 7 succeeded [verified] (James Whitfield, payment logs, message 9, 2026-11-05 09:40 UTC)
- All 31 failures used cards saved before 1 Nov; all 7 successes used cards saved on or after 1 Nov [verified] (James Whitfield, payment logs, message 9, 2026-11-05 09:40 UTC)
- Retry on INV-BV-20931 failed with "PCX-402 token not found"; that invoice's card token was created 14 Oct 2026; the PayCollect API response says "token not found in vault"; no charge was made [verified] (James Whitfield, message 11, 2026-11-05 10:20 UTC, and message 12, 10:40 UTC)
- The customer reconnected PayCollect as support's earlier message instructed [reported] (Sunil Mehta, message 8, 2026-11-04 17:10 UTC); the integration log shows the PayCollect connection was re-authorised on 4 Nov at 14:41 UTC [verified] (James Whitfield, message 11, 2026-11-05 10:20 UTC)
- 14 of the 31 failures happened after the 4 Nov 14:41 UTC re-authorisation [verified] (James Whitfield, message 11, 2026-11-05 10:20 UTC)
- Release v8.2.3, deployed 1 Nov, has the release note "Card vault migrated to PayCollect v3" [verified] (James Whitfield, message 11, 2026-11-05 10:20 UTC)
- Cause: the v8.2.3 vault migration is linked to the failures of tokens saved before 1 Nov [suspected] (James Whitfield, message 11, 2026-11-05 10:20 UTC: "Possible link ... not confirmed")
- Cause: a problem on Quillbill's side with older saved cards, not the customer's settings [suspected] (James Whitfield, message 12, 2026-11-05 10:40 UTC); the customer says "this is not on our side" [reported] (Sunil Mehta, message 8, 2026-11-04 17:10 UTC)
- Account uses Quillbill Invoicing (cloud), PayCollect card payments integration (saved cards, desk payments) and the Clinic front-desk add-on (4 practices); data region UK [verified] (account record)
- Priority P2, set at ticket creation and unchanged at escalation [verified] (event log, 2026-11-03 14:20 UTC and 2026-11-05 11:00 UTC)
- Support promised a credit of October's subscription fee in a message on 3 Nov [reported] (Sunil Mehta, message 8, 2026-11-04 17:10 UTC); the message it refers to is in the missing messages 1 to 6, and the account record shows "Open credits: None recorded" [verified] (account record)

Conflicts:
- Scope: the customer says every card payment has failed since Monday [reported] (Sunil Mehta, message 8); the logs show 7 of 38 attempts since 2 Nov 14:00 UTC succeeded, all with cards saved on or after 1 Nov [verified] (James Whitfield, message 9).
- Credit: the customer says support promised an October credit [reported] (Sunil Mehta, message 8); no such promise appears in messages 7 to 12, and the account record records no credit [verified] (account record). The message it would be in is not in this export.

## Tried so far
| When | Who | What | Result |
|------|-----|------|--------|
| Messages 1 to 6 (2026-11-03 14:20 to 2026-11-04 15:00 UTC) | Unknown | Anything tried in messages 1 to 6 other than the reconnect below | Not in this export; James Whitfield could not see it either (message 11) |
| 2026-11-04 14:41 UTC (integration log) | Customer (Sunil Mehta's team), following Priya Nair's earlier instructions | Reconnected (re-authorised) PayCollect | Failures continued: 14 of the 31 failures are after it (message 11); "the reconnect didn't help" (Priya Nair, message 7) |
| 2026-11-05, by 09:40 UTC | James Whitfield | Checked payment logs since 2 Nov 14:00 UTC | 38 attempts, 31 failed "PCX-402 token not found", 7 succeeded; failures all pre-1-Nov cards, successes all on-or-after-1-Nov cards (message 9) |
| 2026-11-05, by 09:40 UTC | James Whitfield | Passed the customer's October credit request to CSM Callum Reid | Result not recorded |
| 2026-11-05 10:12 UTC | James Whitfield, with customer consent (message 10) | Retried collection on INV-BV-20931 (token created 14 Oct 2026) | Failed: "PCX-402 token not found"; API: "token not found in vault"; no charge made (messages 11, 12) |
| 2026-11-05, by 10:20 UTC | James Whitfield | Checked integration log for the reconnect | Re-authorisation confirmed at 2026-11-04 14:41 UTC (message 11) |
| 2026-11-05, by 10:20 UTC | James Whitfield | Read v8.2.3 release notes | "Card vault migrated to PayCollect v3", deployed 1 Nov; link not confirmed (message 11) |
| 2026-11-05 11:00 UTC | James Whitfield | Escalated to Tier 2 (Product Engineering Support) | Status Open to Escalated, priority P2 (event log) |

## Commitments to the customer
Policy 5.2: "From escalation, Tier 2 owns the ticket, including customer updates and any commitments already made to the customer."

| When | Made by | Verbatim commitment | Status (met / pending / overdue) | Policy note |
|------|---------|---------------------|----------------------------------|-------------|
| 2026-11-04 15:40 UTC (message 7) | Priya Nair | "the next step is for me to look at the payment logs on our side. I'll come back to you tomorrow morning." | Met: James Whitfield checked the logs and replied 2026-11-05 09:40 UTC (message 9) after reassignment | 6.1: "Support agents may commit to the time of the next update and to actions they will take themselves." |
| 2026-11-05 09:40 UTC (message 9) | James Whitfield | "I'd like to retry the collection on one failed invoice, INV-BV-20931, to see whether the error repeats. ... May I go ahead?" | Met: customer agreed (message 10), retried 10:12 UTC, result reported 10:40 UTC (messages 11, 12) | 6.1, as above |
| 2026-11-05 10:40 UTC (message 12) | James Whitfield | "I'm escalating this to our Product Engineering Support team now." | Met: escalated 2026-11-05 11:00 UTC (event log) | 6.1, as above |
| 2026-11-05 10:40 UTC (message 12) | James Whitfield | "I'll update you by 16:00 UTC today." | Pending: due 2026-11-05 16:00 UTC; now owned by Tier 2 | 6.1, as above; 5.2 |

Not a commitment: the October subscription credit. The customer attributes a credit promise to a message of 3 Nov (message 8, [reported]); the words that would make it are not in this export. James Whitfield declined to agree it (message 9). Policy 6.2: "Support agents must not promise a fix date for a product defect, a release date, a service credit or a refund." Policy 6.3: "Only the Customer Success Manager named in the customer's account record, or the Head of Support, may offer a service credit or refund. An offer is valid only when it is recorded in writing on the ticket or in the account record." The named CSM is Callum Reid (account record).

## Service level
Missing term for every resolution computation: support level. Policy 1.3: "A customer's support level (Standard, Business or Enterprise) is the level recorded in the customer's account record." The account record's "Support level:" field is blank.

Shared facts: ticket created 2026-11-03 14:20 UTC (Tuesday), priority P2 (event log). Paused while "Pending customer" from 2026-11-04 09:30 to 15:00 UTC, 5 h 30 min (event log; policy 4.2, 4.3). Business hours 08:00 to 18:00 Europe/London, Monday to Friday, which is UTC in this period (policy 1.1). No English bank holiday falls in the dates below.

**First response**
- Clause: "Enterprise | P2 | 2 hours, 24x7"; "Business | P2 | 4 business hours"; "Standard | P2 | 8 business hours" (policy 3.1)
- Clock: first response; calendar hours (Enterprise) or business hours (Business, Standard); started at ticket creation, 2026-11-03 14:20 UTC (policy 4.1)
- Deadline: Enterprise 2026-11-03 16:20 UTC (14:20 + 2 h); Business 2026-11-04 08:20 UTC (3 h 40 min on 3 Nov to 18:00, plus 20 min from 08:00 on 4 Nov); Standard 2026-11-04 17:50 UTC (3 h 40 min on 3 Nov, plus 1 h 30 min from 08:00 to 09:30 on 4 Nov, total 5 h 10 min; pause to 15:00; plus 2 h 50 min)
- Status: met under every support level. First response 2026-11-03 15:02 UTC (event log), 42 minutes after creation. Missing terms: support level (does not change the status)

**Resolution**
- Clause: "Enterprise | P2 | ... | 24 hours, 24x7"; "Business | P2 | ... | 20 business hours"; "Standard | P2 | ... | 40 business hours" (policy 3.1); "A ticket is "breached" if its resolution target has passed and it is not resolved, and "at risk" if less than 25% of its resolution target remains, measured on the same basis (calendar hours or business hours) as the target. Otherwise it is "within target"." (policy 4.5)
- Clock: resolution; calendar hours (Enterprise) or business hours (Business, Standard); started at ticket creation, 2026-11-03 14:20 UTC; paused 2026-11-04 09:30 to 15:00 UTC
- Deadline:
  - Enterprise: 2026-11-04 19:50 UTC (14:20 on 3 Nov + 24 h = 14:20 on 4 Nov, + 5 h 30 min pause)
  - Business: 2026-11-06 09:50 UTC (3 Nov 14:20 to 18:00 = 3 h 40 min; 4 Nov 08:00 to 09:30 and 15:00 to 18:00 = 4 h 30 min, total 8 h 10 min; 5 Nov 08:00 to 18:00 = 10 h, total 18 h 10 min; 6 Nov 08:00 + 1 h 50 min)
  - Standard: 2026-11-10 09:50 UTC (18 h 10 min by end of 5 Nov; 6 Nov 10 h, total 28 h 10 min; 9 Nov 10 h, total 38 h 10 min; 10 Nov 08:00 + 1 h 50 min)
- Status: cannot determine. Under Enterprise it is breached (passed 14 h 50 min before now). Under Business it is within target, 9 h 10 min business hours remaining at now (elapsed 8 h 10 min + 2 h 40 min on 5 Nov = 10 h 50 min of 20 h), and becomes "at risk" at 2026-11-05 14:50 UTC when under 5 h remain. Under Standard it is within target, 29 h 10 min business hours remaining at now, "at risk" from 2026-11-09 09:50 UTC when under 10 h remain. Missing terms: support level
- Note: if the support level is Enterprise, policy 5.3 applies: "The Support Duty Manager must be told of every P1 ticket and of every P2 ticket that is breached."

**Customer updates**
- Clause: "P2 tickets: an update at least once each business day." (policy 7.1)
- Clock: update interval; business days; started at ticket creation, 2026-11-03 14:20 UTC
- Deadline: next update due by end of business day 2026-11-05 is already met (message 9 at 09:40, message 12 at 10:40 UTC); the following one is due by 2026-11-06 18:00 UTC (end of Friday's business hours). The 16:00 UTC commitment above comes sooner.
- Status: met so far (updates on 3 Nov 15:02, 4 Nov 15:40, 5 Nov 09:40 and 10:40 UTC); missing terms: none

## Open questions
- Will the October subscription fee be credited? The customer asked for confirmation, then for it "in writing, not passed around" (asked by Sunil Mehta, 2026-11-04 17:10 UTC, message 8, and 2026-11-05 09:55 UTC, message 10). Passed to CSM Callum Reid (message 9); no answer recorded.
- What reconnect steps did Priya Nair send, and what else was tried, in messages 1 to 6? (asked by James Whitfield, internal note, 2026-11-05 10:20 UTC, message 11). This also decides whether a credit was promised in a 3 Nov message.

## Recommended next action
Check whether the INV-BV-20931 card token (created 14 Oct 2026) exists in the PayCollect v3 vault and in the v8.2.3 vault migration records for account BV-3307, and compare it with the token of one of the 7 successful payments (card saved on or after 1 Nov). This tests the suspected migration cause directly: the API already says "token not found in vault", and the reconnect and retry have not explained it. Owner: Tier 2 (Product Engineering Support), which owns the ticket from escalation (policy 5.2). By: 2026-11-05 16:00 UTC, so the result can go into the update James Whitfield committed to for that time. Rests on: logs splitting failures and successes at the 1 Nov save date (message 9); retry failure with "token not found in vault" on a 14 Oct token (message 11); v8.2.3 release note "Card vault migrated to PayCollect v3", deployed 1 Nov (message 11); reconnect confirmed with failures continuing after it (message 11); pending 16:00 UTC update commitment (message 12).
