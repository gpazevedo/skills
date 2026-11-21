Clarifying question: What is the support level (Standard, Business or Enterprise) for account BV-3307? The account record's "Support level" field is blank, and the resolution status depends on it. Continuing without an answer.

# Escalation handoff: QB-202861 Card payments with cards saved before 1 Nov fail with "PCX-402 token not found"

Reference time ("now"): 2026-11-05 11:00 UTC (given by the thread export header, which says to treat the export time as the current time; it matches the escalation event)
Inputs missing: Messages 1 to 6 of the thread (2026-11-03 14:20 to 2026-11-04 15:00 UTC) are not in the export; the ticket event log is complete. The account record is supplied but its "Support level" field is blank. Thread, account record and policy were otherwise supplied.

## Problem as currently understood
Brackenridge Veterinary Group (BV-3307, Quillbill Invoicing with PayCollect saved-card payments) cannot collect card payments on saved cards. Logs show a split on the date the card was saved: cards saved before 1 Nov fail with "PCX-402 token not found" and cards saved on or after 1 Nov succeed. The customer's PayCollect reconnect did not help. The leading hypothesis is that the v8.2.3 card vault migration (deployed 1 Nov) did not carry over older tokens; that is not confirmed.
- Since 2 Nov 14:00 UTC there were 38 card payment attempts: 31 failed with "PCX-402 token not found", 7 succeeded [verified] (James Whitfield, message 9, 2026-11-05 09:40)
- All 31 failures used cards saved before 1 Nov; all 7 successes used cards saved on or after 1 Nov [verified] (James Whitfield, message 9, 2026-11-05 09:40)
- Retry of INV-BV-20931 at 10:12 failed with "PCX-402 token not found"; the token was created 14 Oct 2026; the PayCollect API says "token not found in vault"; no charge was made [verified] (James Whitfield, internal note message 11, 2026-11-05 10:20, and message 12, 10:40)
- PayCollect connection was re-authorised on 4 Nov at 14:41 UTC, and 14 of the 31 failures are after that time [verified] (James Whitfield, message 11, integration log)
- Release v8.2.3 (deployed 1 Nov) notes: "Card vault migrated to PayCollect v3." [verified] that the release note says this (James Whitfield, message 11); its link to the failures is [suspected] (James Whitfield, message 11, "not confirmed")
- Cause is a problem on Quillbill's side with older saved cards, not the customer's settings [suspected] (James Whitfield, message 12, 2026-11-05 10:40, "suggests")
- Customer-facing impact: clients' saved cards are declined at the desk [reported] (Sunil Mehta, message 8, 2026-11-04 17:10)
- Every card payment has failed since Monday [reported] (Sunil Mehta, message 8, 2026-11-04 17:10)
- The customer did exactly what the earlier message said and reconnected PayCollect [reported] (Sunil Mehta, message 8); that a reconnect happened on 4 Nov 14:41 is [verified] (integration log, message 11); which steps were sent is not visible (messages 1 to 6 missing)
- Plan Quillbill Clinic, UK data region, 4 practices on the front-desk add-on, CSM Callum Reid [verified] (account record)
Conflicts: Customer says every card payment has failed since Monday [reported] (Sunil Mehta, message 8); support's logs show 7 of 38 attempts succeeded since 2 Nov 14:00, all on cards saved on or after 1 Nov [verified] (James Whitfield, message 9). Customer says the problem is not on their side [reported]; support's view that it is on Quillbill's side is only [suspected].

## Tried so far
| When | Who | What | Result |
|------|-----|------|--------|
| 2026-11-03 to 2026-11-04 15:00 | Priya Nair / customer | Steps in messages 1 to 6, including whatever reconnect instructions were sent | Not visible in this export; result not recorded |
| By 2026-11-04 14:41 | Customer (Sunil Mehta) | Reconnected (re-authorised) PayCollect | Failures continued afterwards (14 of 31 after 14:41); message 7 also says the reconnect did not help |
| 2026-11-05 09:40 | James Whitfield | Reviewed payment logs on Quillbill's side | Found the 31 failed / 7 succeeded split by card save date (see above) |
| 2026-11-05 10:12 | James Whitfield | Retried collection on INV-BV-20931 (customer consented, message 10) | Failed again with "PCX-402 token not found"; no charge made |
| 2026-11-05 10:20 | James Whitfield | Checked integration log and release notes | Reconnect confirmed; v8.2.3 vault migration noted as a possible link, not confirmed |

## Commitments to the customer
| When | Made by | Verbatim commitment | Status (met / pending / overdue) | Policy note |
|------|---------|---------------------|----------------------------------|-------------|
| 2026-11-04 15:40 | Priya Nair | "I'll come back to you tomorrow morning." (message 7; "look at the payment logs on our side") | met: James Whitfield replied with the log findings at 2026-11-05 09:40 | 6.1: "Support agents may commit to the time of the next update and to actions they will take themselves." |
| 2026-11-05 09:40 | James Whitfield | "I've passed your request to Callum Reid." (message 9; about the October credit) | Statement of a past action; no record in the case that Callum Reid received it or has replied, so cannot verify. Treat as pending | 6.3: "Only the Customer Success Manager named in the customer's account record, or the Head of Support, may offer a service credit or refund. An offer is valid only when it is recorded in writing on the ticket or in the account record." |
| 2026-11-05 10:40 | James Whitfield | "I'll update you by 16:00 UTC today." (message 12) | pending; 5 hours remaining at now; owned by Tier 2 from escalation | 5.2: "From escalation, Tier 2 owns the ticket, including customer updates and any commitments already made to the customer." |

Not a commitment: the customer says "as you said in your message yesterday, we'll be expecting October's subscription fee to be credited" (Sunil Mehta, message 8). This is a customer claim [reported] about a promise attributed to Quillbill. Message 7 (the only Priya message in the export from 4 Nov) contains no credit promise; the earlier message could be one of messages 1 to 6, which are missing, so it cannot be checked. The account record shows "Open credits: None recorded". James told the customer he is "not able to agree credits" (message 9). Policy 6.2: "Support agents must not promise a fix date for a product defect, a release date, a service credit or a refund." The customer has asked twice for written confirmation (messages 8 and 10); none exists.

## Service level
Missing term: the account record's "Support level" is blank, so the applicable row of policy 3.1 cannot be selected. Priority is P2 (event log; matches definition 2.2, payment collection with no practical workaround). Elapsed time at now: created Tue 2026-11-03 14:20, paused as "Pending customer" 2026-11-04 09:30 to 15:00 (5.5 hours, all inside business hours). Nov 1 to 5 2026 contains no bank holiday; London time is GMT (policy 1.1) so UTC equals local time.

First-response clock (the same under every support level: met)
- Clause: "Enterprise / P2 / 2 hours, 24x7"; "Business / P2 / 4 business hours"; "Standard / P2 / 8 business hours" (3.1); first response excludes automated acknowledgements (1.4)
- Clock: first response, calendar (Enterprise) or business (Business, Standard) hours, started ticket creation 2026-11-03 14:20
- Deadline: Enterprise 16:20 on 3 Nov; Business 4 business hours = 18:00 on 3 Nov is 3h40, then 00h20 more, so 08:20 on 4 Nov; Standard 8 business hours = 3h40 + 4h20, so 12:20 on 4 Nov
- Status: met. Agent response sent 2026-11-03 15:02, 42 minutes after creation; inside all three deadlines. Missing terms: support level, but the status is the same under each value

Resolution clock (cannot determine)
- Clause: "Enterprise / P2 / resolution 24 hours, 24x7"; "Business / P2 / 20 business hours"; "Standard / P2 / 40 business hours" (3.1); clock starts at creation and pauses only in "Pending customer" (4.1, 4.2); "breached" if the target has passed and the ticket is not resolved, "at risk" if less than 25% of the target remains (4.5)
- Clock: resolution, started 2026-11-03 14:20, excluding 5.5 hours paused
- Deadline, Enterprise (calendar): 24h from 14:20 on 3 Nov; 19h10 used by the pause at 09:30 on 4 Nov; 4h50 left after resume at 15:00; deadline 2026-11-04 19:50. Elapsed at now: 44h40 minus 5.5h = 39h10, so 15h10 past the deadline
- Deadline, Business (20 business hours): used at now = 3h40 (3 Nov) + 10h (4 Nov) + 3h (5 Nov 08:00 to 11:00) = 16h40, minus 5.5h = 11h10; 8h50 remain; 25% of 20 = 5h, so not at risk; deadline = 7h on 5 Nov (to 18:00) + 1h50 on 6 Nov = 2026-11-06 09:50
- Deadline, Standard (40 business hours): used 11h10; 28h50 remain; 25% of 40 = 10h, so not at risk; deadline = 7h (5 Nov) + 10h (6 Nov) + 10h (Mon 9 Nov) + 1h50 on 10 Nov = 2026-11-10 09:50
- Status: cannot determine. Enterprise: breached by 15h10 (breached P2 must be reported to the Support Duty Manager, 5.3). Business: within target, 8h50 business hours remaining. Standard: within target, 28h50 business hours remaining. Missing terms: support level (account record "Support level:" blank)

Update interval clock (met under every level)
- Clause: "P2 tickets: an update at least once each business day." (7.1)
- Clock: update interval, business-day basis, started 2026-11-03 14:20
- Deadline: each business day; updates on 3 Nov (15:02), 4 Nov (15:40) and 5 Nov (09:40 and 10:40)
- Status: met so far; next update promised by 16:00 UTC 5 Nov. Missing terms: none

## Open questions
- What support level applies to BV-3307? The account record is blank (found while building this handoff); it decides whether the resolution clock is breached (Enterprise) or within target (Business, Standard) and whether the Duty Manager must be told (5.3).
- Can the October credit be confirmed in writing? (asked by Sunil Mehta, 2026-11-04 17:10 and 2026-11-05 09:55); only Callum Reid or the Head of Support may offer it, in writing on the ticket or account record (6.3). Has Callum Reid received the request passed on in message 9?
- Did Priya Nair's earlier message (messages 1 to 6) say anything about a credit, and which reconnect steps did it give? (customer's assertion in message 8; James noted he cannot see these, message 11)
- Do the 31 failing tokens exist in the PayCollect v3 vault, and did the 1 Nov migration skip tokens saved before 1 Nov? (James Whitfield, message 11, "possible link ... not confirmed")
- Were there failures between the 1 Nov deploy and 2 Nov 14:00? The log window starts at 2 Nov 14:00 and the customer says failures began "Monday" (2 Nov); not examined.
- Has the Support Duty Manager been told (5.3)? Only relevant if the ticket is breached, which depends on the support level.

## Recommended next action
Check whether the PayCollect v3 vault contains the token for INV-BV-20931 (created 14 Oct 2026), and compare against a post-1 Nov token that succeeded, using the v8.2.3 migration records to see whether tokens saved before 1 Nov were migrated at all; owner: Tier 2 Product Engineering Support engineer (Tier 2 owns the ticket, 5.2), results by 15:30 UTC 2026-11-05 so the customer update promised by 16:00 UTC can be sent, plus confirmation of the support level to the Tier 2 lead. Rests on: the 31 failed / 7 succeeded split by save date; the failed retry with "token not found in vault"; the v8.2.3 release note "Card vault migrated to PayCollect v3" (the leading [suspected] cause, not yet tested); and the pending 16:00 UTC commitment (message 12). No fix date, release date or credit may be given to the customer (6.2, 6.3).
