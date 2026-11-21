Clarifying question: Can you supply messages 1 to 6 of QB-202861 (2026-11-03 14:20 to 2026-11-04 15:00 UTC) and Brackenridge's support level (Standard, Business or Enterprise)? The export leaves both out, so the reconnect steps Priya sent, whether she mentioned a credit, and which service-level row applies are all unknown below.

# Escalation handoff: QB-202861 Card payments failing with "PCX-402" on cards saved before 1 Nov

**Customer:** Brackenridge Veterinary Group Ltd, account BV-3307, plan Quillbill Clinic (annual subscription, billed monthly); support level: not stated (account record field "Support level:" is blank)  **Priority:** P2 (set at creation 2026-11-03 14:20 UTC; unchanged at escalation 2026-11-05 11:00 UTC)  **Prepared:** 2026-11-21 18:31 UTC (Saturday; environment clock)

Inputs: thread is a partial export (messages 7 to 12 of 12 plus the complete event log up to 2026-11-05 11:00 UTC); messages 1 to 6 not supplied. Account record and policy (v4.2) supplied. The export records nothing after 2026-11-05 11:00 UTC, so every "now" status below assumes nothing has happened on the ticket since then.

## Service level

Policy 1.3: "A customer's support level (Standard, Business or Enterprise) is the level recorded in the customer's account record." The record has no level, so each clock is given under all three readings.

| Clock | Policy clause | Started | Deadline | Status |
|---|---|---|---|---|
| First response (Enterprise P2) | 3.1 "Enterprise, P2, First response: 2 hours, 24x7" | 2026-11-03 14:20 UTC (ticket created, 4.1) | 2026-11-03 16:20 UTC | Met at 15:02 UTC (message 2, event log) |
| First response (Business P2) | 3.1 "Business, P2, First response: 4 business hours" | 2026-11-03 14:20 UTC | 2026-11-04 08:20 UTC | Met at 2026-11-03 15:02 UTC |
| First response (Standard P2) | 3.1 "Standard, P2, First response: 8 business hours" | 2026-11-03 14:20 UTC | 2026-11-04 12:20 UTC | Met at 2026-11-03 15:02 UTC |
| Resolution (Enterprise P2) | 3.1 "Enterprise, P2, Resolution: 24 hours, 24x7" | 2026-11-03 14:20 UTC | 2026-11-04 19:50 UTC | Breached, 16 d 22 h 41 min ago |
| Resolution (Business P2) | 3.1 "Business, P2, Resolution: 20 business hours" | 2026-11-03 14:20 UTC | 2026-11-06 09:50 UTC | Breached, 108 h 10 min business hours ago (15 d 8 h 41 min calendar) |
| Resolution (Standard P2) | 3.1 "Standard, P2, Resolution: 40 business hours" | 2026-11-03 14:20 UTC | 2026-11-10 09:50 UTC | Breached, 88 h 10 min business hours ago (11 d 8 h 41 min calendar) |
| Customer update (any level) | 7.1 "P2 tickets: an update at least once each business day." | 2026-11-05 10:40 UTC (last customer update, message 12) | 2026-11-06 18:00 UTC (end of next business day, 1.1) | Breached, 15 d 0 h 31 min ago, if no update was sent after message 12 |

Rules used: business hours 08:00 to 18:00 Europe/London, Mon to Fri, no bank holidays in England in this period, and Europe/London = UTC from 25 Oct 2026 (1.1); "24x7" targets run on calendar time (3.3); clock paused only while "Pending customer" (4.2, 4.3), which the event log shows from 2026-11-04 09:30 to 15:00 UTC (5 h 30 min).

- First response, Enterprise: 14:20 + 2 h = 16:20 on 3 Nov. Business: 3 Nov 14:20 to 18:00 = 3 h 40; + 20 min on 4 Nov = 08:20. Standard: 3 h 40 + 4 h 20 on 4 Nov = 12:20 (no pause before the response, which came at 15:02 on 3 Nov after 42 min).
- Resolution, Enterprise: 3 Nov 14:20 + 24 h = 4 Nov 14:20, + 5 h 30 paused = 4 Nov 19:50.
- Resolution, Business: 3 Nov 3 h 40 + 4 Nov (08:00 to 09:30 = 1 h 30, 15:00 to 18:00 = 3 h) + 5 Nov 10 h = 18 h 10; remaining 1 h 50 on Fri 6 Nov = 09:50. Since breach: 6 Nov 8 h 10 + 9 to 13 Nov 50 h + 16 to 20 Nov 50 h = 108 h 10.
- Resolution, Standard: 18 h 10 by end of 5 Nov + 6 Nov 10 h + 9 Nov 10 h = 38 h 10; remaining 1 h 50 on Tue 10 Nov = 09:50. Since breach: 10 Nov 8 h 10 + 11 to 13 Nov 30 h + 16 to 20 Nov 50 h = 88 h 10.
- At escalation (2026-11-05 11:00 UTC) the resolution clock was already breached under Enterprise; under Business 8 h 50 of 20 h remained (44%, "within target" per 4.5); under Standard 28 h 50 of 40 h remained (72%, within target).
- Update clock: 7.1 does not say when in the day an update is due; end of business hours (18:00 UTC) is the reading used here.
- Obligations triggered: 5.2 "From escalation, Tier 2 owns the ticket, including customer updates and any commitments already made to the customer." 5.3 "The Support Duty Manager must be told of every P2 ticket that is breached." Whether the Duty Manager has been told: not stated.

## Problem as currently understood

Since 2 November, card payments for BV-3307 that use cards saved before 1 November fail with "PCX-402 token not found", and the PayCollect API reports "token not found in vault"; cards saved on or after 1 November succeed. Release v8.2.3, deployed 1 November, "migrated" the card vault "to PayCollect v3", and the support agent suspects older tokens were not carried over; that link has not been confirmed. The customer's PayCollect reconnect on 4 November did not change the result.

| Fact | Status | Evidence |
|---|---|---|
| Card payments fail with error "PCX-402 token not found" | Verified | Customer report (message 8; ticket title); James Whitfield's payment-log check (message 9) and retry of INV-BV-20931 (message 11) |
| Since 2 Nov 14:00 UTC: 38 card payment attempts, 31 failed with PCX-402, 7 succeeded | Verified | James Whitfield, payment logs (message 9, 2026-11-05 09:40 UTC) |
| "every single card payment has failed since Monday" (2 Nov) | Reported; partly contradicted | Sunil Mehta (message 8). Logs confirm failures since 2 Nov but show 7 successes (message 9) |
| All 31 failures used cards saved before 1 Nov; all 7 successes used cards saved on or after 1 Nov | Verified | James Whitfield, payment logs (message 9) |
| Retry of INV-BV-20931 at 10:12 UTC on 5 Nov failed with "PCX-402 token not found"; that card token was created 14 Oct 2026; PayCollect API response "token not found in vault"; no charge made | Verified | James Whitfield, retry and API response (message 11, internal; message 12) |
| Customer reconnected PayCollect as Priya's earlier message instructed | Verified | Reported by Sunil Mehta (message 8); integration log shows re-authorisation 2026-11-04 14:41 UTC (message 11, internal) |
| Failures continue after the reconnect: 14 of the 31 failures are after 14:41 UTC on 4 Nov | Verified | James Whitfield, integration and payment logs (message 11, internal) |
| Release v8.2.3 deployed 1 Nov; release notes: "Card vault migrated to PayCollect v3." | Verified | James Whitfield read the release notes (message 11, internal) |
| The v8.2.3 vault migration caused the failures of tokens saved before 1 Nov | Suspected | James Whitfield: "Possible link with tokens saved before 1 Nov; not confirmed." (message 11); "suggests a problem on our side with older saved cards" (message 12) |
| Cause is "not on our side" (not the customer's settings) | Reported | Sunil Mehta (message 8); consistent with the suspected cause above but not confirmed |
| Business impact: clients collecting pets have their saved card declined at the desk, "embarrassing for our staff" | Reported | Sunil Mehta (message 8) |
| Environment: Quillbill Invoicing (cloud), PayCollect card payments integration (saved cards, desk payments), Clinic front-desk add-on (4 practices), data region UK | Verified | Account record, Products and Data region fields |
| Which of the 4 practices are affected | Not stated | Neither the thread nor the account record says |

Contradictions:
- Scope: Sunil Mehta says "every single card payment has failed since Monday" (message 8, 2026-11-04 17:10 UTC); the payment logs show 7 of 38 attempts since 2 Nov 14:00 UTC succeeded (message 9, 2026-11-05 09:40 UTC).
- October credit: Sunil Mehta says "as you said in your message yesterday, we'll be expecting October's subscription fee to be credited" (message 8), referring to a message from Priya Nair that is not in this export. The account record shows "Open credits: None recorded"; policy 6.2 says support agents "must not promise ... a service credit" and 6.3 says an offer "is valid only when it is recorded in writing on the ticket or in the account record". James Whitfield neither confirms nor denies that Priya said it (message 9).

## What has been tried

| When | Who | Action | Result |
|---|---|---|---|
| Between 2026-11-03 and 2026-11-04 (messages 1 to 6, not supplied) | Priya Nair | Sent reconnect steps for PayCollect (referred to in messages 7 and 8) | Steps not supplied; see next row |
| Messages 1 to 6 (not supplied) | Not stated | Anything else tried: James Whitfield "can't see ... what else was tried in messages 1 to 6" (message 11) | Not supplied |
| 2026-11-04 14:41 UTC | Customer (Sunil Mehta's team) | Reconnected (re-authorised) PayCollect | Failures continued: "sorry the reconnect didn't help" (message 7); 14 of 31 failures after 14:41 (message 11) |
| 2026-11-05, by 09:40 UTC | James Whitfield | Checked payment logs since 2 Nov 14:00 UTC | 31 of 38 failed with PCX-402, all on cards saved before 1 Nov; 7 succeeded, all on cards saved on or after 1 Nov (message 9) |
| 2026-11-05 10:12 UTC | James Whitfield, with customer consent (message 10) | Retried collection on INV-BV-20931 | Failed: "PCX-402 token not found"; API "token not found in vault"; token created 14 Oct 2026; no charge (messages 11, 12) |
| 2026-11-05, by 10:20 UTC | James Whitfield | Read integration log and v8.2.3 release notes | Reconnect confirmed at 2026-11-04 14:41 UTC; v8.2.3 "Card vault migrated to PayCollect v3" (message 11) |
| 2026-11-05, by 09:40 UTC | James Whitfield | Passed the customer's October credit request to CSM Callum Reid (message 9) | Result not recorded |
| 2026-11-05 11:00 UTC | James Whitfield | Escalated to Tier 2 (Product Engineering Support), status Escalated, priority P2 | Event log |

## Commitments to the customer

| When | Made by | Commitment (quoted) | Due | State |
|---|---|---|---|---|
| 2026-11-04 15:40 UTC (message 7) | Priya Nair | "the next step is for me to look at the payment logs on our side" | Not stated | Met: James Whitfield checked the logs (message 9) |
| 2026-11-04 15:40 UTC (message 7) | Priya Nair | "I'll come back to you tomorrow morning." | 2026-11-05 morning (no time stated) | Met: James Whitfield replied 2026-11-05 09:40 UTC (message 9) |
| Message 1 to 6 (not supplied), as reported by Sunil Mehta in message 8 | Priya Nair (per the customer) | Customer's words: "as you said in your message yesterday, we'll be expecting October's subscription fee to be credited for all this" | Not stated | Open and unconfirmed: Priya's wording not supplied; no credit recorded (account record); not valid unless recorded by the CSM or Head of Support (policy 6.3) |
| 2026-11-05 09:40 UTC (message 9) | James Whitfield | "I've passed your request to Callum Reid." | Not stated | Met as stated; Callum Reid's response not recorded. Customer replied: "I want the credit confirmed in writing, not passed around." (message 10) |
| 2026-11-05 09:40 UTC (message 9) | James Whitfield | "I'd like to retry the collection on one failed invoice, INV-BV-20931 ... May I go ahead?" | On consent (given message 10, 09:55 UTC) | Met: retried 10:12 UTC, result reported in message 12 |
| 2026-11-05 10:40 UTC (message 12) | James Whitfield | "I'm escalating this to our Product Engineering Support team now." | 2026-11-05 | Met: escalated 11:00 UTC (event log) |
| 2026-11-05 10:40 UTC (message 12) | James Whitfield | "I'll update you by 16:00 UTC today." | 2026-11-05 16:00 UTC | Overdue: no update recorded in this export. Tier 2 owns it (policy 5.2) |

Account record: no commitments recorded (no contract notes; "Open credits: None recorded").

## Recommended next action

Test the suspected cause directly on the one token already in hand: look up the INV-BV-20931 card token (created 14 Oct 2026, account BV-3307, UK data region) in the v8.2.3 card-vault migration records and in the PayCollect v3 vault, and check whether it, and the other pre-1-Nov tokens behind the 31 failures, exist in the pre-migration vault but not in v3.

- Confirms it: the token exists in the pre-migration vault or migration source, but is missing from the v3 vault, or the migration log shows BV-3307's tokens skipped or failed. Then query PCX-402 failures since 1 Nov across other accounts to size the defect.
- Rules it out: the token is present in the v3 vault under BV-3307. Then look at how Quillbill looks up tokens after the 4 Nov re-authorisation (account or vault mapping) instead.

This is racing: the 2026-11-05 16:00 UTC update James promised (overdue), the daily P2 update under 7.1 (overdue since 2026-11-06 18:00 UTC if none was sent), and the resolution target (breached under every reading). Send the customer the overdue update and tell the Support Duty Manager of the breach (5.3) before or alongside the check.

Open questions:
- What support level is BV-3307 on? The account record field is blank (policy 1.3).
- What did messages 1 to 6 say, in particular the reconnect steps and whether Priya Nair mentioned an October credit?
- Has Callum Reid (CSM) responded to the credit request, and is anything recorded in writing (policy 6.3)?
- The customer asks for October's fee to be credited, but the failures began on 2 November; which period is the request meant to cover?
- Did any PCX-402 failures occur between the v8.2.3 deployment on 1 Nov and 2 Nov 14:00 UTC, the start of the log window James checked?
- Which of the 4 front-desk practices are affected?
- Does re-saving a pre-1-Nov card make it work (all post-1-Nov cards succeeded)? If so, that could serve as a workaround; it has not been tested or offered.
- Has anything happened on the ticket since 2026-11-05 11:00 UTC (updates, status changes, a pause)? If so, the statuses above need recomputing.
