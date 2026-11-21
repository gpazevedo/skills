Clarifying question: (1) What is the current time and time zone? Service-level statuses below are measured as of 2026-11-05 11:00 UTC, the last event in the thread, because no current time was supplied. (2) What is Brackenridge's support level (Standard, Business or Enterprise)? The account record's "Support level" field is blank. (3) Can you supply messages 1 to 6 of QB-202861? They are missing from the export.

# Escalation handoff: QB-202861 Card payments with cards saved before 1 Nov 2026 fail with "PCX-402 token not found"

**Customer:** Brackenridge Veterinary Group Ltd, account BV-3307, plan "Quillbill Clinic (annual subscription, billed monthly)", support level Not determinable (account record field "Support level:" is blank)   **Severity/priority:** P2 (ticket events 2026-11-03 14:20 UTC "Priority: P2" and 2026-11-05 11:00 UTC "Priority: P2")
**Most urgent deadline:** Customer update promised "by 16:00 UTC today", i.e. 2026-11-05 16:00 UTC (message 12, James Whitfield, 2026-11-05 10:40 UTC). Tier 2 now owns this commitment (policy 5.2). If the support level is Enterprise, the resolution target was already breached at 2026-11-04 19:50 UTC (see Service-level status).

## Problem as currently understood
Since about 2 November 2026, PayCollect card payments on BV-3307 fail with "PCX-402 token not found" whenever the saved card was stored before 1 November; cards saved on or after 1 November charge successfully. The customer's PayCollect reconnect did not stop the failures. Support's untested explanation is that the "Card vault migrated to PayCollect v3" change in v8.2.3 (deployed 1 Nov) left pre-1 Nov card tokens missing from the vault.

| Fact | Status | How established / cite |
|---|---|---|
| Card payments fail with error "PCX-402 token not found" | Verified | James Whitfield checked payment logs (message 9, 2026-11-05 09:40 UTC) |
| Since 2 Nov 14:00 UTC: 38 card payment attempts, 31 failed with "PCX-402 token not found", 7 succeeded | Verified | Payment logs, message 9 (James Whitfield, 2026-11-05 09:40 UTC) |
| All 31 failures used cards saved before 1 Nov; all 7 successes used cards saved on or after 1 Nov | Verified | Payment logs, message 9 (James Whitfield, 2026-11-05 09:40 UTC) |
| "every single card payment has failed since Monday" (Monday = 2 Nov) | Reported | Sunil Mehta, message 8 (2026-11-04 17:10 UTC); contradicted in part by logs (7 successes), see disagreements |
| Clients collecting pets have saved cards declined at the desk; staff embarrassed | Reported | Sunil Mehta, message 8 (2026-11-04 17:10 UTC) |
| Customer reconnected PayCollect | Verified | Customer report in message 8 confirmed by integration log: "PayCollect connection was re-authorised on 4 Nov at 14:41 UTC" (internal note, message 11, 2026-11-05 10:20 UTC) |
| Failures continued after the reconnect: 14 of the 31 failures are after 14:41 on 4 Nov | Verified | Integration and payment logs, internal note message 11 (James Whitfield, 2026-11-05 10:20 UTC) |
| Retry of INV-BV-20931 at 10:12 on 5 Nov failed with "PCX-402 token not found"; no charge was made | Verified | Retry performed and result read by James Whitfield, internal note message 11 (2026-11-05 10:20 UTC); reported to customer in message 12 (2026-11-05 10:40 UTC) |
| Card token on INV-BV-20931 was created 14 Oct 2026; PayCollect API response says "token not found in vault" | Verified | API response and token record read by James Whitfield, internal note message 11 (2026-11-05 10:20 UTC) |
| Release notes for v8.2.3 (deployed 1 Nov) say "Card vault migrated to PayCollect v3." | Verified | Release notes read by James Whitfield, internal note message 11 (2026-11-05 10:20 UTC) |
| The v8.2.3 vault migration is linked to the failures of tokens saved before 1 Nov | Hypothesis | James Whitfield: "Possible link with tokens saved before 1 Nov; not confirmed." (internal note message 11, 2026-11-05 10:20 UTC); not tested |
| The fault is "a problem on our side with older saved cards rather than with your settings" | Hypothesis | James Whitfield, message 12 (2026-11-05 10:40 UTC); inference from the saved-date pattern, not tested |
| Customer uses PayCollect saved cards and desk payments, with the Clinic front-desk add-on across 4 practices | Verified | Account record, "Products" field |
| Which of the 4 practices are affected | Not established | No source states this; see Gaps |
| Priority P2 | Verified | Ticket events 2026-11-03 14:20 UTC and 2026-11-05 11:00 UTC |
| Priya Nair said in a message on 3 Nov that October's subscription fee would be credited | Reported | Sunil Mehta, message 8 (2026-11-04 17:10 UTC): "as you said in your message yesterday, we'll be expecting October's subscription fee to be credited"; the referenced message is in messages 1 to 6, which are missing |

**Open disagreements:**
- Scope: the customer says "every single card payment has failed since Monday" (message 8); the payment logs show 7 of 38 attempts since 2 Nov 14:00 UTC succeeded, all with cards saved on or after 1 Nov (message 9).
- Credit: the customer says Priya Nair promised an October credit (message 8). This cannot be checked because messages 1 to 6 are missing. Policy 6.2 says support agents "must not promise ... a service credit or a refund" and 6.3 says an offer "is valid only when it is recorded in writing on the ticket or in the account record"; the account record shows "Open credits: None recorded".

## What has been tried
| When | Who | Action | Result | Cite |
|---|---|---|---|---|
| Between 2026-11-03 14:20 and 2026-11-04 15:00 UTC (exact message not available) | Priya Nair (Tier 1) | Advised the customer to reconnect PayCollect | Customer followed it; see next row | Message 7 ("sorry the reconnect didn't help"); message 8 ("We did exactly what your earlier message said and reconnected PayCollect") |
| 2026-11-04 14:41 UTC | Customer (Brackenridge) | Reconnected / re-authorised PayCollect | Failures continued: 14 of 31 failures occurred after 14:41 on 4 Nov | Integration log, internal note message 11; message 7 |
| Messages 1 to 6 | Unknown | Any other steps | Not recorded (messages missing from export) | Internal note message 11: "I can't see in my view which reconnect steps Priya sent or what else was tried in messages 1 to 6." |
| 2026-11-05, before 09:40 UTC | James Whitfield (Tier 1) | Checked payment logs since 2 Nov 14:00 UTC | 38 attempts: 31 failed "PCX-402 token not found" (all pre-1 Nov cards), 7 succeeded (all cards saved on or after 1 Nov) | Message 9 |
| 2026-11-05 09:40 UTC | James Whitfield (Tier 1) | Passed customer's October credit request to Callum Reid (Customer Success Manager) | Not recorded | Message 9 |
| 2026-11-05 10:12 UTC | James Whitfield (Tier 1) | Retried collection on INV-BV-20931 (customer approved in message 10) | Failed: "PCX-402 token not found"; API "token not found in vault"; no charge made | Internal note message 11; message 12 |
| 2026-11-05, before 10:20 UTC | James Whitfield (Tier 1) | Checked integration log and v8.2.3 release notes | Reconnect confirmed at 4 Nov 14:41 UTC; release notes say "Card vault migrated to PayCollect v3." | Internal note message 11 |
| 2026-11-05 11:00 UTC | James Whitfield (Tier 1) | Escalated to Tier 2 (Product Engineering Support) | Status Open → Escalated, priority P2 | Ticket event 2026-11-05 11:00 UTC |

## Commitments to the customer
| Commitment (verbatim) | Made by (role) | When / cite | Deadline | Kept / Open / Missed |
|---|---|---|---|---|
| "the next step is for me to look at the payment logs on our side. I'll come back to you tomorrow morning." | Priya Nair (Support Agent, Tier 1) | Message 7, 2026-11-04 15:40 UTC | Morning of 2026-11-05 (no exact time given) | Kept, by James Whitfield after reassignment: logs checked and reply sent 2026-11-05 09:40 UTC (message 9) |
| "I'd like to retry the collection on one failed invoice, INV-BV-20931, to see whether the error repeats. ... May I go ahead?" | James Whitfield (Support Agent, Tier 1) | Message 9, 2026-11-05 09:40 UTC | None stated; conditional on customer consent (given in message 10) | Kept: retried 10:12 UTC, result reported in message 12 |
| "I'm escalating this to our Product Engineering Support team now." | James Whitfield (Support Agent, Tier 1) | Message 12, 2026-11-05 10:40 UTC | Immediate | Kept: ticket event 2026-11-05 11:00 UTC "Escalated to Tier 2" |
| "I'll update you by 16:00 UTC today." | James Whitfield (Support Agent, Tier 1) | Message 12, 2026-11-05 10:40 UTC | 2026-11-05 16:00 UTC | Open as of the last thread event (2026-11-05 11:00 UTC); Missed if 16:00 UTC on 5 Nov has passed with no update. Owned by Tier 2 from escalation (policy 5.2: "Tier 2 owns the ticket, including customer updates and any commitments already made to the customer") |

Not in the table: the October credit the customer says Priya Nair promised (message 8) cannot be quoted verbatim because the message it is said to be in is missing. If it was said, it exceeds policy 6.2 ("Support agents must not promise ... a service credit or a refund") and 6.3 ("Only the Customer Success Manager named in the customer's account record, or the Head of Support, may offer a service credit or refund"); the named Customer Success Manager is Callum Reid (account record). The customer has asked for the credit "confirmed in writing, not passed around" (message 10); that is a request, not a commitment.

## Service-level status
Inputs: ticket created 2026-11-03 14:20 UTC (Tuesday); paused (status "Pending customer") 2026-11-04 09:30 to 15:00 UTC = 5 h 30 min, all inside business hours. Policy 1.1: "Business hours are 08:00 to 18:00 Europe/London time, Monday to Friday"; between 25 Oct 2026 and 28 Mar 2027 "Europe/London time is GMT, which is the same as UTC". Policy 4.2: "The clock is paused only while the ticket status is 'Pending customer'." Support level is Not determinable (account record field blank; policy 1.3: support level "is the level recorded in the customer's account record"), so each clock is given conditionally for each level. Statuses are as of 2026-11-05 11:00 UTC (last thread event); current time not supplied. Policy 4.5: "'breached' if its resolution target has passed and it is not resolved, and 'at risk' if less than 25% of its resolution target remains".

Business hours counted for the business-hours clocks: 3 Nov 14:20 to 18:00 = 3 h 40 min; 4 Nov 08:00 to 09:30 = 1 h 30 min plus 15:00 to 18:00 = 3 h (pause excluded); cumulative 8 h 10 min at end of 4 Nov; 5 Nov full day = 10 h (cumulative 18 h 10 min); 6 Nov (Fri) = 10 h (28 h 10 min); 9 Nov (Mon) = 10 h (38 h 10 min).

| Clock | Policy clause (quoted) | Started | Deadline (with arithmetic) | Status |
|---|---|---|---|---|
| First response, if Enterprise | 3.1 "Enterprise / P2 / 2 hours, 24x7" | 2026-11-03 14:20 UTC (creation, 4.1) | 14:20 + 2 h = 2026-11-03 16:20 UTC | Met: first agent response 2026-11-03 15:02 UTC (ticket event), 42 min |
| First response, if Business | 3.1 "Business / P2 / 4 business hours" | 2026-11-03 14:20 UTC | 3 h 40 min on 3 Nov + 20 min on 4 Nov = 2026-11-04 08:20 UTC | Met: 2026-11-03 15:02 UTC |
| First response, if Standard | 3.1 "Standard / P2 / 8 business hours" | 2026-11-03 14:20 UTC | 3 h 40 min on 3 Nov + 1 h 30 min on 4 Nov to 09:30 (pause) + 2 h 50 min after 15:00 = 2026-11-04 17:50 UTC | Met: 2026-11-03 15:02 UTC |
| Resolution, if Enterprise | 3.1 "Enterprise / P2 / 24 hours, 24x7"; 3.3 "Targets marked '24x7' run on calendar time." | 2026-11-03 14:20 UTC | 14:20 3 Nov + 24 h + 5 h 30 min pause = 2026-11-04 19:50 UTC. At-risk point (6 h remaining) = 2026-11-04 13:50 UTC | Breached (unresolved at 2026-11-05 11:00 UTC) |
| Resolution, if Business | 3.1 "Business / P2 / 20 business hours" | 2026-11-03 14:20 UTC | 8 h 10 min by end of 4 Nov + 10 h on 5 Nov = 18 h 10 min; remaining 1 h 50 min from 08:00 6 Nov = 2026-11-06 09:50 UTC. At-risk point (5 h remaining, 15 h used) = 2026-11-05 14:50 UTC | Within target at 2026-11-05 11:00 UTC (11 h 10 min used, 8 h 50 min left); becomes at risk 2026-11-05 14:50 UTC |
| Resolution, if Standard | 3.1 "Standard / P2 / 40 business hours" | 2026-11-03 14:20 UTC | 38 h 10 min by end of 9 Nov; remaining 1 h 50 min from 08:00 10 Nov = 2026-11-10 09:50 UTC. At-risk point (10 h remaining, 30 h used) = 2026-11-09 09:50 UTC | Within target at 2026-11-05 11:00 UTC (11 h 10 min used) |
| Customer update interval (all levels) | 7.1 "P2 tickets: an update at least once each business day." | Ticket creation 2026-11-03 | Updates sent 3 Nov (first response 15:02, ticket event), 4 Nov (message 7, 15:40), 5 Nov (message 9 09:40, message 12 10:40). Next due: during business day 6 Nov, by 18:00 UTC | Met for 3, 4 and 5 Nov; on track for 6 Nov |

Policy 5.3: "The Support Duty Manager must be told of every ... P2 ticket that is breached." This applies now if the level is Enterprise, from 2026-11-06 09:50 UTC if Business, and from 2026-11-10 09:50 UTC if Standard (if still unresolved).

## Recommended next action
Look up the INV-BV-20931 card token (created 14 Oct 2026) in the PayCollect v3 vault and in the v8.2.3 vault-migration records, and check whether BV-3307's pre-1 Nov tokens were migrated. Evidence: every one of the 31 failures used a card saved before 1 Nov and every one of the 7 successes used a card saved on or after 1 Nov (message 9); the API says "token not found in vault" (message 11); v8.2.3 deployed 1 Nov "Card vault migrated to PayCollect v3" (message 11); the reconnect changed nothing (message 11). The link to the migration is only a Hypothesis (messages 11 and 12), so confirming it is the action itself. The result settles whether the fix is on Quillbill's side (re-migrating or re-mapping the missing tokens) or whether saved cards must be re-entered, and whether a workaround exists that would bear on the P2 rating (policy 2.2, "no practical workaround"). Deadline to beat: the promised customer update at 2026-11-05 16:00 UTC (message 12), then the resolution target if Business (2026-11-06 09:50 UTC); if Enterprise the resolution target is already breached and the Support Duty Manager must be told (policy 5.3).

## Gaps
- Messages 1 to 6 (2026-11-03 14:20 to 2026-11-04 15:00 UTC) are missing from the export. This hides what Priya Nair advised, what else was tried, and whether she said anything about a credit. Close by pulling the full ticket.
- Support level is Not determinable: account record field "Support level:" is blank. Close by confirming the level with the account record owner or Callum Reid (Customer Success Manager); it decides which deadlines above apply and whether policy 5.3 is already triggered.
- Current time not supplied: statuses are measured at 2026-11-05 11:00 UTC. Close by re-measuring against the current time, in particular whether the 16:00 UTC update on 5 Nov was sent.
- October credit: the customer's claim that Priya promised it is unverified (messages 1 to 6 missing); the outcome of James's referral to Callum Reid (message 9) is not recorded. Close by reading messages 1 to 6 and getting Callum Reid's decision recorded in writing on the ticket (policy 6.3).
- Which of the customer's 4 practices are affected, and whether failures began before 2 Nov 14:00 UTC (the log query window started then), are not recorded. Close with a payment log query by practice from 1 Nov 00:00 UTC.
- Whether other customers with pre-1 Nov tokens are failing in the same way is not recorded. Close with a cross-account query for "PCX-402 token not found" since 1 Nov.
