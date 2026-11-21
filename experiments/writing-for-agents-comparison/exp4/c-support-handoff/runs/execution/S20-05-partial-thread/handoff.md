Clarifying question: The account record's "Support level" field is blank, and the thread export omits messages 1 to 6. What is Brackenridge's support level (Standard, Business or Enterprise), and what do messages 1 to 6 say? Policy 1.3 takes the level from the account record, so without it no service-level target can be fixed. Proceeding without an answer: service-level terms are marked "Not determinable" and shown conditionally per level.

# Escalation handoff: QB-202861 Card payments failing with "PCX-402 token not found" for cards saved before 1 Nov

**Customer:** Brackenridge Veterinary Group Ltd (BV-3307), Quillbill Clinic plan, support level Not determinable: support level blank in account record | **Priority:** P2 (shown as P2 at ticket creation via portal by Sunil Mehta and again in the 2026-11-05 11:00 escalation event; the export does not say which agent confirmed it)
**Service level:** Not determinable: support level blank. Conditional on level: Enterprise = breached (resolution deadline passed 2026-11-04 19:50 UTC, overdue 15h10m); Business = within target, resolution deadline 2026-11-06 09:50 UTC; Standard = within target, resolution deadline 2026-11-10 09:50 UTC.
**Open commitments:** 1, earliest due 2026-11-05 16:00 UTC (5h from the as-of time)

## Problem as currently understood
Card payments on saved cards are failing with "PCX-402 token not found". Verified in the payment logs: 31 of 38 attempts since 2 Nov 14:00 UTC failed, and every failure used a card saved before 1 Nov, while all 7 successes used cards saved on or after 1 Nov. The customer's reconnect of PayCollect (4 Nov 14:41 UTC) did not stop the failures. James Whitfield's hypothesis is that the v8.2.3 deployment of 1 Nov ("Card vault migrated to PayCollect v3") left older tokens missing from the vault; this is unconfirmed. The customer reports that every card payment has failed since Monday and that the October credit was promised earlier; neither claim is supported by the logs or the available thread.

| Fact | Tag | Source |
|---|---|---|
| 38 card payment attempts since 2 Nov 14:00 UTC; 31 failed with "PCX-402 token not found", 7 succeeded | Verified (James Whitfield, payment logs) | Message 9, 2026-11-05 09:40 |
| All 31 failures used cards saved before 1 Nov; all 7 successes used cards saved on or after 1 Nov | Verified (James Whitfield, payment logs) | Message 9 |
| Retry of INV-BV-20931 at 10:12 UTC on 5 Nov failed with "PCX-402 token not found"; no charge made | Verified (James Whitfield) | Messages 11 and 12 |
| Token on INV-BV-20931 was created 14 Oct 2026; PayCollect API says "token not found in vault" | Verified (James Whitfield, API response) | Message 11 |
| PayCollect connection was re-authorised 4 Nov 14:41 UTC; 14 of the 31 failures are after that time | Verified (James Whitfield, integration log) | Message 11 |
| v8.2.3 was deployed 1 Nov with release note "Card vault migrated to PayCollect v3" | Verified as a release-note entry (James Whitfield read it); exact deployment time not given | Message 11 |
| The vault migration in v8.2.3 caused the failures for pre-1 Nov tokens | Hypothesis (James Whitfield: "Possible link ... not confirmed"; repeated in message 12 as "suggests a problem on our side") | Messages 11, 12 |
| Every card payment has failed since Monday | Reported (Sunil Mehta); logs show 7 successes, so the "every" is contradicted for the period from 2 Nov 14:00 | Message 8 |
| Clients' saved cards declined at the front desk | Reported (Sunil Mehta) | Message 8 |
| Customer reconnected PayCollect as instructed in an earlier message | Reported (Sunil Mehta); the reconnect itself is Verified by the integration log above | Message 8 |
| Customer says Priya Nair said, in an earlier message, that October's subscription fee would be credited | Reported (Sunil Mehta); not verifiable, messages 1 to 6 not in export | Message 8 |
| Failures began before 2 Nov 14:00, or only then | Not determinable: the log window James queried starts at 2 Nov 14:00 | Message 9 |

**Open questions:**
- Did the v8.2.3 vault migration drop or fail to migrate tokens saved before 1 Nov, and can they be restored or re-created?
- Is there a workaround for the customer (for example re-saving cards or taking payment another way)? None is recorded.
- What did messages 1 to 6 say, including the reconnect steps Priya sent and whether any credit was mentioned?
- When did failures start, and are other customers affected? No evidence on scope beyond this account.
- What is the account's support level?

## What has been tried
| Action | By | When | Result |
|---|---|---|---|
| Reconnect of PayCollect (steps sent by Priya Nair in messages 1 to 6, content not visible to James) | Customer, on Priya's instruction | Re-authorised 2026-11-04 14:41 UTC | Failures continued (14 of 31 after it) |
| Other troubleshooting in messages 1 to 6 | Not determinable | 2026-11-03 14:20 to 2026-11-04 15:00 | Not determinable: messages not in export |
| Ticket set Pending customer, then back to Open on customer reply | Priya Nair | 2026-11-04 09:30 to 15:00 | n/a |
| Priya's planned payment log check (message 7) | Priya Nair | Promised for 5 Nov morning | Done instead by James Whitfield, see next row |
| Checked payment logs on Quillbill side | James Whitfield | 2026-11-05 ~09:40 | 31 of 38 failed, pattern by token save date |
| Retried collection on INV-BV-20931 (customer consented in message 10) | James Whitfield | 2026-11-05 10:12 | Failed, "PCX-402 token not found" |
| Checked integration log and v8.2.3 release notes | James Whitfield | Before 2026-11-05 10:20 | Reconnect confirmed; possible link to v8.2.3, not confirmed |
| Passed customer's credit request to Callum Reid (Customer Success Manager) | James Whitfield | By 2026-11-05 09:40 | Stated as done; no response from Callum recorded |
| Escalated to Tier 2 | James Whitfield | 2026-11-05 11:00 | Status Escalated |

## Commitments to the customer
| Commitment (quoted) | Made by | When | Status |
|---|---|---|---|
| "I'll come back to you tomorrow morning." (to look at the payment logs and report) | Priya Nair | 2026-11-04 15:40 | Met: James Whitfield replied with log findings at 2026-11-05 09:40 |
| "I've passed your request to Callum Reid." (commitment to pass on the credit request only) | James Whitfield | 2026-11-05 09:40 | Met per James's statement; no evidence Callum has acted |
| "I'm escalating this to our Product Engineering Support team now." | James Whitfield | 2026-11-05 10:40 | Met: escalation event at 11:00 |
| "I'll update you by 16:00 UTC today." | James Whitfield | 2026-11-05 10:40 | Open, due 2026-11-05 16:00 UTC. Under policy 5.2, Tier 2 now owns this commitment |

**Requested, not committed:**
- Credit of October's subscription fee, requested by Sunil in message 8 and repeated as "confirmed in writing" in message 10. James said "I'm not able to agree credits" (message 9). No offer is recorded; account shows "Open credits: None recorded". Policy 6.3: only the Customer Success Manager (Callum Reid) or the Head of Support may offer one, in writing on the ticket or account record. Policy 6.2: agents must not promise credits.
- Sunil's claim that Priya earlier said the credit would be given: cannot be checked, messages 1 to 6 missing. Whoever reads messages 1 to 6 should check for it, because any such promise would breach policy 6.2 and the customer will cite it.

## Service level
Measured at 2026-11-05 11:00 UTC (the as-of time in the export). Readings used for ambiguous terms: Europe/London is GMT from 25 Oct 2026 (policy 1.1), so business hours 08:00 to 18:00 are the same in UTC; 3 Nov to 5 Nov 2026 are Tuesday to Thursday with no bank holiday; the first agent response (event at 15:02, message 2) is read as not automated, as the log says "First agent response sent". Priority P2 used throughout (policy 4.4: if support changes it, resolution recounts from creation).

Support level: Not determinable (account record "Support level:" is blank; policy 1.3 says the level is the one recorded there). The table gives each level's policy target as a conditional so Tier 2 can read off the right row once the level is known. Do not treat any row as the actual target.

Clock facts: started at creation 2026-11-03 14:20 (policy 4.1). Paused 2026-11-04 09:30 to 15:00 = 5h30m while "Pending customer" (4.2, 4.3). Calendar time elapsed to 11-05 11:00 = 44h40m; minus 5h30m pause = 39h10m. Business-hours elapsed excluding pause: 3 Nov 14:20 to 18:00 = 3h40m; 4 Nov 08:00 to 09:30 = 1h30m plus 15:00 to 18:00 = 3h, total 4h30m; 5 Nov 08:00 to 11:00 = 3h. Sum = 11h10m.

| Target (policy quote) | Clock start | Deadline (arithmetic) | Status |
|---|---|---|---|
| Enterprise P2 first response: "2 hours, 24x7" | 11-03 14:20 | 14:20 + 2h = 11-03 16:20; reply at 15:02 (42 min) | Met |
| Business P2 first response: "4 business hours" | 11-03 14:20 | 3h40m to 18:00, 20m more on 11-04 from 08:00 = 11-04 08:20; reply at 15:02 | Met |
| Standard P2 first response: "8 business hours" | 11-03 14:20 | 11-04 12:20 (3h40m + 4h20m); reply at 15:02 on 11-03 | Met |
| Enterprise P2 resolution: "24 hours, 24x7" | 11-03 14:20 | 14:20 + 24h + 5h30m pause = 11-04 19:50. Elapsed 39h10m exceeds 24h | Breached, overdue 15h10m (11-05 11:00 minus 11-04 19:50) |
| Business P2 resolution: "20 business hours" | 11-03 14:20 | Used 11h10m; remaining 8h50m (44%, above 25%). 7h left on 11-05 to 18:00, 1h50m more from 11-06 08:00 = 11-06 09:50 | Within target |
| Standard P2 resolution: "40 business hours" | 11-03 14:20 | Used 11h10m; remaining 28h50m (72%). 7h on 11-05, 10h on 11-06, 10h on 11-09, 1h50m on 11-10 = 11-10 09:50 | Within target |
| P2 update cadence (policy 7.1): "an update at least once each business day" | n/a | Updates on 11-04 15:40 and 11-05 09:40/10:40; next required by end of 11-05 business day (18:00) and in any case by the 16:00 commitment | Met so far; the 16:00 update is open |

The "at risk" threshold (under 25% of target remaining, policy 4.5) is not reached at Business or Standard at the as-of time. For Business it is reached when under 5h remain, i.e. after 15h of business time used, which is 11-05 14:50 UTC (11h10m used at 11:00, plus 3h50m).

Policy duty if Enterprise: 5.3 says the Support Duty Manager "must be told of every P2 ticket that is breached"; no record in the thread that this was done.
Policy 5.1 escalation basis: cannot be resolved with documented procedures; escalation to Tier 2 occurred at 11:00.

Pauses: "The clock is paused only while the ticket status is 'Pending customer'" (policy 4.2). One pause applied: 11-04 09:30 to 15:00 (5h30m). Policy does not state how pause time interacts with the business-hours window beyond 4.3 ("Paused time does not count toward any target"); the pause is wholly inside business hours (09:30 to 15:00) so the answer is the same either way.

## Recommended next action
Tier 2 engineer on Product Engineering Support (owner to be assigned; the ticket is now Tier 2's per policy 5.2) checks whether the v8.2.3 card vault migration to PayCollect v3 failed to carry over tokens saved before 1 Nov, starting with the INV-BV-20931 token (created 14 Oct), and states whether the tokens can be restored; by 2026-11-05 15:30 UTC, so the result can go into the 16:00 UTC update owed to the customer. In the same pass: (a) confirm the support level with Callum Reid or the account owner and apply the right target (if Enterprise, tell the Support Duty Manager under 5.3); (b) retrieve messages 1 to 6 to check for any credit promise and the reconnect steps given; (c) ask Callum Reid to answer the October credit request in writing on the ticket (policy 6.3). Reason: the log pattern ties all 31 failures to pre-1 Nov tokens and there is no workaround on record, while a customer update is due at 16:00 and the payment failures are visible at client desks.
