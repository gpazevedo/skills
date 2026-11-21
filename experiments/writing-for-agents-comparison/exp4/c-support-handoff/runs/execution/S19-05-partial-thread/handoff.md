# Escalation handoff: QB-202861 Saved cards failing with "PCX-402 token not found" (P2)

**Customer:** Brackenridge Veterinary Group Ltd, account BV-3307, plan "Quillbill Clinic" (account record: "Support level:" is blank)   **Severity/priority:** P2 (ticket event log, 2026-11-03 14:20 UTC creation; re-stated on escalation event 2026-11-05 11:00 UTC). Support level: Not determinable.
**Most urgent deadline:** Update to the customer by 16:00 UTC on 2026-11-05 (James Whitfield, message 12, 2026-11-05 10:40 UTC); Tier 2 now owns it (policy 5.2). Resolution clock: if Enterprise, already breached (since 2026-11-04 19:50 UTC); if Business, due 2026-11-06 09:50 UTC; if Standard, due 2026-11-09 09:50 UTC (see Service-level status).

As-of time used for every judgement: 2026-11-05 11:00 UTC (thread header).

## Problem as currently understood
Card payments using saved cards fail with "PCX-402 token not found" ("token not found in vault") at the customer's four-practice clinic desks. The logs show a clean split: every failure used a card saved before 1 November, every success used a card saved on or after 1 November. Support's working explanation is a link to the v8.2.3 release (1 Nov, "Card vault migrated to PayCollect v3"), which is unconfirmed. The customer's reconnect of PayCollect did happen and did not fix it.

| Fact | Status | How established / cite |
|---|---|---|
| Since 2 Nov 14:00 UTC there were 38 card payment attempts; 31 failed with "PCX-402 token not found", 7 succeeded | Verified | James Whitfield read the payment logs, message 9, 2026-11-05 09:40 UTC |
| All 31 failures used cards saved before 1 Nov; all 7 successes used cards saved on or after 1 Nov | Verified | Payment logs, message 9, 2026-11-05 09:40 UTC |
| Retry of INV-BV-20931 at 10:12 UTC on 5 Nov failed with "PCX-402 token not found"; no charge made; PayCollect API said "token not found in vault"; the token was created 14 Oct 2026 | Verified | Reproduced by James Whitfield, message 11 (internal note), 2026-11-05 10:20 UTC; message 12 |
| PayCollect connection was re-authorised on 4 Nov at 14:41 UTC and 14 of the 31 failures are after that time | Verified | Integration log, message 11, 2026-11-05 10:20 UTC |
| Saved cards are declined at the desk when clients collect their pets; staff embarrassed | Reported | Sunil Mehta, message 8, 2026-11-04 17:10 UTC |
| "Every single card payment has failed since Monday" (Monday = 2 Nov) | Reported (contradicted in part, see disagreements) | Sunil Mehta, message 8, 2026-11-04 17:10 UTC |
| Customer followed support's earlier reconnect instruction exactly | Reported (the reconnect itself is Verified by integration log; that it followed Priya's steps is not) | Message 8; message 11 says the steps Priya sent are not visible |
| Failures are linked to the v8.2.3 deployment of 1 Nov ("Card vault migrated to PayCollect v3") | Hypothesis | James Whitfield, message 11: "Possible link ... not confirmed"; release notes v8.2.3 quoted there |
| The problem is on Quillbill's side with older saved cards, not the customer's settings | Hypothesis | James Whitfield, message 12, 2026-11-05 10:40 UTC ("suggests") |
| Priority is P2 | Verified (recorded on ticket) | Ticket events, 2026-11-03 14:20 and 2026-11-05 11:00 UTC. Not tested against policy 2.2 "no practical workaround": cards saved on or after 1 Nov work |
| Customer expects October's subscription fee credited, and says Priya said so yesterday | Reported | Message 8, 2026-11-04 17:10 UTC. Open credits: None recorded (account record) |

**Open disagreements:**
1. Customer says every card payment has failed since Monday; the logs show 7 of 38 attempts succeeded (all with cards saved on or after 1 Nov).
2. Customer says "as you said in your message yesterday" October's fee would be credited; the thread export (messages 7 to 12) contains no such promise and the account record shows no credit. Messages 1 to 6 are missing, so this cannot be checked. James Whitfield (message 9) says only the CSM can agree credits.
3. Customer says "this is not on our side"; support agrees as a hypothesis only (message 12), not confirmed.

## What has been tried
| When | Who | Action | Result | Cite |
|---|---|---|---|---|
| Before 2026-11-04 15:00 UTC | Priya Nair (Tier 1) | Reconnect-PayCollect instructions sent to customer (content not in export) | Customer reconnected 4 Nov 14:41 UTC; failures continued | Message 7 ("sorry the reconnect didn't help"), message 8, message 11 integration log |
| 2026-11-04 09:30 to 15:00 UTC | Priya Nair | Ticket set to Pending customer | Customer replied (message 6); back to Open | Ticket events |
| 2026-11-04 14:41 UTC | Customer | Re-authorised PayCollect connection | Failures continued (14 of 31 after this time) | Message 8; message 11 |
| 2026-11-05 ~09:40 UTC | James Whitfield | Checked payment logs | Found pre/post 1 Nov split (above) | Message 9 |
| 2026-11-05 09:40 UTC | James Whitfield | Passed customer's credit request to Callum Reid (CSM) | Not recorded (no reply or credit recorded in the thread) | Message 9 |
| 2026-11-05 10:12 UTC | James Whitfield | Retried collection on INV-BV-20931 (customer consented, message 10) | Failed: "PCX-402 token not found" | Message 11, message 12 |
| 2026-11-05 11:00 UTC | James Whitfield | Escalated to Tier 2 | Status Escalated, P2 | Ticket events |
| Messages 1 to 6 (3 Nov 14:20 to 4 Nov 15:00 UTC) | Unknown | Other steps | Not recorded: export omits them | Thread header; message 11 |

## Commitments to the customer
| Commitment (verbatim) | Made by (role) | When / cite | Deadline | Kept / Open / Missed |
|---|---|---|---|---|
| "I'll come back to you tomorrow morning." | Priya Nair (Tier 1 agent) | Message 7, 2026-11-04 15:40 UTC | Morning of 2026-11-05 | Kept: James Whitfield replied 2026-11-05 09:40 UTC (message 9). Within 6.1. |
| "I've passed your request to Callum Reid." (statement of action taken, implies the CSM will handle the credit) | James Whitfield (Tier 1 agent) | Message 9, 2026-11-05 09:40 UTC | None set | Open. No thread evidence the CSM received it or has replied. Customer asked for written confirmation (message 10). Credit is only for the CSM or Head of Support, valid only if written on the ticket or account record (policy 6.3). |
| "I'm escalating this to our Product Engineering Support team now." | James Whitfield (Tier 1 agent) | Message 12, 2026-11-05 10:40 UTC | Immediate | Kept: escalation event 2026-11-05 11:00 UTC |
| "I'll update you by 16:00 UTC today." | James Whitfield (Tier 1 agent) | Message 12, 2026-11-05 10:40 UTC | 2026-11-05 16:00 UTC | Open (5 hours from as-of time). Now owned by Tier 2 (policy 5.2). Within 6.1. |
| Possible earlier credit promise: customer quotes Priya as saying October's fee would be credited | Priya Nair, if said | Not in export (messages 1 to 6) | Unknown | Unverified. If made, it breaches policy 6.2 and 6.3; and "Open credits: None recorded". |

No agent message in 7 to 12 promises a fix date, credit or refund. Messages 8 and 10 are customer requests (context, not commitments).

## Service-level status
Policy 1.1: business hours 08:00 to 18:00 Europe/London, Mon to Fri; "Between 25 October 2026 and 28 March 2027, Europe/London time is GMT, which is the same as UTC." Policy 4.1: "The clock starts when the ticket is created." Policy 4.2: "The clock is paused only while the ticket status is 'Pending customer'." 3 Nov 2026 is a Tuesday; no bank holidays assumed in the period.

Start: ticket created 2026-11-03 14:20 UTC (ticket events). Pause: Pending customer 2026-11-04 09:30 to 15:00 UTC = 5.5 hours (all inside business hours).

Support level is blank in the account record (policy 1.3 says the level is "the level recorded in the customer's account record"), so the clock is Not determinable; missing input: the Support level field. Conditional values for P2 (policy 3.1):

| Clock | Policy clause (quoted) | Started | Deadline (with arithmetic) | Status |
|---|---|---|---|---|
| First response, if Enterprise | 3.1 "2 hours, 24x7" | 2026-11-03 14:20 UTC | 16:20 UTC on 3 Nov; first agent response 15:02 UTC (message 2, 42 min) | Met |
| First response, if Business | 3.1 "4 business hours" | same | 18:20 UTC on 3 Nov (within business hours); response at 15:02 | Met |
| First response, if Standard | 3.1 "8 business hours" | same | 3.67 h left on 3 Nov, remaining 4.33 h on 4 Nov from 08:00, so 12:20 UTC on 4 Nov; response at 15:02 on 3 Nov | Met |
| Resolution, if Enterprise | 3.1 "24 hours, 24x7" | same | 24 h + 5.5 h paused = 29.5 h from 3 Nov 14:20, so 2026-11-04 19:50 UTC. Elapsed unpaused to as-of: 44 h 40 min - 5.5 h = 39 h 10 min | Breached (by 15 h 10 min). Also policy 5.3 would apply: Duty Manager must be told of a breached P2; no sign in thread that they were. |
| Resolution, if Business | 3.1 "20 business hours" | same | Business hours used: 3 Nov 14:20 to 18:00 = 3 h 40 min; 4 Nov 10 h - 5.5 h paused = 4 h 30 min; 5 Nov 08:00 to 11:00 = 3 h; total 11 h 10 min. Remaining 8 h 50 min: 7 h on 5 Nov, 1 h 50 min on 6 Nov, so 2026-11-06 09:50 UTC | Within target now; becomes at risk (under 5 h left, policy 4.5) at about 14:50 UTC on 5 Nov |
| Resolution, if Standard | 3.1 "40 business hours" | same | Used 11 h 10 min; remaining 28 h 50 min: 7 h (5 Nov) + 10 h (6 Nov) + 10 h (7 Nov) + 1 h 50 min on Mon 9 Nov, so 2026-11-09 09:50 UTC | Within target; at risk (under 10 h left) from about 09:50 UTC on 7 Nov |
| Update interval | 7.1 "P2 tickets: an update at least once each business day" | 3 Nov | Updates sent 4 Nov 15:40 and 5 Nov 09:40 UTC; next due by end of 6 Nov business day (and 16:00 UTC today by commitment) | On track (any support level) |

Note: 4.4 recalculation only applies if priority changes; none recorded.

## Recommended next action
Tier 2 (Product Engineering Support): check whether saved card tokens created before 1 Nov 2026 were lost or not migrated when v8.2.3 ("Card vault migrated to PayCollect v3") was deployed, for example by looking up the token on INV-BV-20931 (created 14 Oct 2026, "token not found in vault") in the PayCollect v3 vault against the migration records. Evidence: 31 of 31 failures are pre-1 Nov cards and 7 of 7 successes are post-1 Nov cards (message 9); retry reproduced it (message 11); the customer's reconnect did not help (message 11). The result would settle whether the migration is the cause (the Hypothesis in message 11) and whether the fix is on Quillbill's side, which also decides if the customer's priority and any credit discussion stand on a confirmed fault. Also confirm the support level on BV-3307 (blank) so the right clock applies. Deadline to beat: the 16:00 UTC update commitment on 2026-11-05, and, if the customer turns out to be Enterprise, the resolution deadline already passed; if Business, 09:50 UTC on 6 Nov. Do not promise a fix date or credit (policy 6.2); route the credit question to Callum Reid and have it recorded in writing on the ticket (policy 6.3).

## Gaps
- Messages 1 to 6 are not in the export: unknown content of the reconnect instructions, any credit promise, and any other steps. Close by pulling the full ticket.
- Support level blank in account record: service-level deadlines are conditional (above). Close by confirming the contract/entitlement with Callum Reid or the account record owner.
- Result of the credit request passed to Callum Reid: not recorded. Close by asking the CSM; the customer wants written confirmation.
- Cause (v8.2.3 vault migration): Hypothesis only.
- Whether the P2 definition (2.2, "no practical workaround") still fits given newly saved cards work: not assessed; priority stays as recorded.
- Whether the Support Duty Manager has been told (needed only if P2 is breached, policy 5.3): not recorded.
- Bank holidays assumed none between 3 and 9 Nov 2026.
