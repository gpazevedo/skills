Clarifying question: Two inputs are incomplete. The account record's "Support level" field is blank (account.md line 5), which blocks the resolution target and service-level status, and the thread export contains only messages 7 to 12 (thread.md line 7), which blocks the fact list, attempt log and commitment check for messages 1 to 6. Can you supply the customer's support level (Standard, Business or Enterprise) and the full thread? No answer was available, so the handoff below marks those gaps "Not determinable" and continues.

# Escalation handoff: QB-202861 Saved-card payments failing with "PCX-402 token not found" for cards saved before 1 Nov

**Customer:** Brackenridge Veterinary Group Ltd (BV-3307), plan Quillbill Clinic; support level Not determinable: field blank in account record | **Priority:** P2 (set by: not recorded; present at ticket creation via portal, 2026-11-03 14:20 UTC, and kept at P2 by James Whitfield at escalation, 2026-11-05 11:00 UTC)
**Service level:** Not determinable: support level not supplied. Resolution deadline is 2026-11-04 19:50 UTC (breached, overdue by 15h10m) if Enterprise, 2026-11-06 09:50 UTC (within target, 8h50m business time left) if Business, 2026-11-10 09:50 UTC (within target, 28h50m business time left) if Standard. First response met at every level. Next fixed deadline: P2 daily update, due by end of business 2026-11-06.
**Open commitments:** 1, earliest due 2026-11-05 16:00 UTC (5h00m remaining at reference time). Commitments in messages 1 to 6: Not determinable, messages not supplied.

## Problem as currently understood
Since at least 2 Nov 14:00 UTC, card payments on this account that use cards saved before 1 Nov fail with "PCX-402 token not found", while cards saved on or after 1 Nov succeed (Verified, James Whitfield, payment logs, message 9). A retry on INV-BV-20931 reproduced the failure, and the PayCollect API returned "token not found in vault" for a token created 14 Oct 2026 (Verified, James Whitfield, message 11). The customer's PayCollect reconnect did happen and did not help (Verified, integration log, message 11). Hypothesis (James Whitfield, messages 11 and 12): the v8.2.3 release on 1 Nov, which "migrated" the card vault to PayCollect v3, did not carry over tokens saved before 1 Nov; not confirmed.

| Fact | Tag | Source |
|---|---|---|
| Every single card payment has failed since Monday (2 Nov) | Reported (contradicted by the log figures below: 7 of 38 succeeded) | Sunil Mehta, message 8 |
| Clients collecting pets have had their saved card declined at the desk; staff embarrassed | Reported | Sunil Mehta, message 8 |
| Customer reconnected PayCollect as an earlier support message instructed | Reported | Sunil Mehta, message 8; Priya Nair, message 7 ("sorry the reconnect didn't help") |
| PayCollect connection was re-authorised on 4 Nov at 14:41 UTC | Verified, James Whitfield, integration log | Message 11 |
| 38 card payment attempts since 2 Nov 14:00 UTC: 31 failed with "PCX-402 token not found", 7 succeeded | Verified, James Whitfield, payment logs | Message 9 |
| All 31 failures used cards saved before 1 Nov; all 7 successes used cards saved on or after 1 Nov | Verified, James Whitfield, payment logs | Message 9 |
| 14 of the 31 failures occurred after the 4 Nov 14:41 UTC re-authorisation | Verified, James Whitfield, integration log | Message 11 |
| Retry of INV-BV-20931 at 10:12 UTC on 5 Nov failed with "PCX-402 token not found"; no charge made | Verified, James Whitfield | Messages 11 and 12 |
| Card token on INV-BV-20931 was created 14 Oct 2026; PayCollect API response "token not found in vault" | Verified, James Whitfield | Message 11 |
| v8.2.3 deployed 1 Nov; release notes: "Card vault migrated to PayCollect v3." | Verified, James Whitfield, release notes | Message 11 |
| Failures are linked to the v3 vault migration for tokens saved before 1 Nov | Hypothesis, James Whitfield ("Possible link ... not confirmed") | Message 11 |
| Problem is "on our side with older saved cards rather than with your settings" | Hypothesis, James Whitfield | Message 12 |
| Products: Quillbill Invoicing (cloud), PayCollect integration (saved cards, desk payments), Clinic front-desk add-on (4 practices); data region UK | Verified, account record | account.md lines 7 to 11 |

**Open questions:**
- Are tokens saved before 1 Nov missing from the PayCollect v3 vault, or present but not mapped? Is this account-specific or affecting every customer with pre-1 Nov saved cards?
- Did failures start at the 1 Nov deploy? The log window quoted begins 2 Nov 14:00 UTC (message 9); payments between 1 Nov and 2 Nov 14:00 UTC were not reported.
- Is there a workaround (for example, re-saving an affected card)? Not tested in the thread. This bears on priority: policy 2.2 defines P2 as payment collection not working "and there is no practical workaround".
- If tokens were lost in the migration, does policy 2.1 P1 ("invoice or payment data has been lost or corrupted") apply? Priority has not been reviewed against this (my observation, not a finding in the thread).
- What happened in messages 1 to 6: symptoms first reported, the reconnect steps Priya sent, other troubleshooting, and any statement about a credit. James could not see them either (message 11).
- Customer's support level: blank in the account record.

## What has been tried
| Action | By | When | Result |
|---|---|---|---|
| Actions in messages 1 to 6 (2026-11-03 14:20 to 2026-11-04 15:00 UTC) | Not determinable: messages not supplied | Not determinable | Not determinable |
| Reconnect / re-authorise PayCollect, on instructions in an earlier support message | Customer (instructed by Priya Nair, per messages 7 and 8) | Re-authorised 2026-11-04 14:41 UTC (message 11) | Failures continued: 14 of 31 after it (message 11) |
| Reviewed payment logs since 2 Nov 14:00 UTC | James Whitfield | 2026-11-05, by 09:40 UTC (message 9) | 31 failed / 7 succeeded; failures all pre-1 Nov saved cards |
| Retried collection on INV-BV-20931 (customer consent, message 10) | James Whitfield | 2026-11-05 10:12 UTC (message 11) | Failed, "PCX-402 token not found"; API "token not found in vault"; no charge |
| Checked integration log for the reconnect | James Whitfield | 2026-11-05, by 10:20 UTC (message 11) | Re-authorisation confirmed at 4 Nov 14:41 UTC |
| Checked v8.2.3 release notes | James Whitfield | 2026-11-05, by 10:20 UTC (message 11) | "Card vault migrated to PayCollect v3"; possible link, not confirmed |
| Passed October credit request to Customer Success Manager Callum Reid | James Whitfield | 2026-11-05, by 09:40 UTC (message 9) | Result not recorded |
| Escalated to Tier 2 (Product Engineering Support) | James Whitfield | 2026-11-05 11:00 UTC (event) | Status Open → Escalated, priority P2 |

## Commitments to the customer
| Commitment (quoted) | Made by | When | Status |
|---|---|---|---|
| "the next step is for me to look at the payment logs on our side. I'll come back to you tomorrow morning." | Priya Nair | 2026-11-04 15:40 UTC, message 7 | Met: logs checked and customer updated by James Whitfield, 2026-11-05 09:40 UTC (message 9) |
| "I'd like to retry the collection on one failed invoice, INV-BV-20931 ... May I go ahead?" (customer agreed, message 10) | James Whitfield | 2026-11-05 09:40 UTC, message 9 | Met: retried 10:12 UTC, result reported 10:40 UTC (messages 11, 12) |
| "I'm escalating this to our Product Engineering Support team now." | James Whitfield | 2026-11-05 10:40 UTC, message 12 | Met: escalated 11:00 UTC (event) |
| "I'll update you by 16:00 UTC today." | James Whitfield | 2026-11-05 10:40 UTC, message 12 | Open, due 2026-11-05 16:00 UTC. Tier 2 now owns it: "From escalation, Tier 2 owns the ticket, including customer updates and any commitments already made to the customer" (policy 5.2) |
| Commitments in messages 1 to 6 | Not determinable: messages not supplied | | |

**Requested, not committed:**
- Credit of October's subscription fee (Sunil Mehta, message 8), and written confirmation of it "not passed around" (message 10). The customer says a support message on 3 Nov ("as you said in your message yesterday", message 8) promised it; that message is in the unsupplied range, so this is Reported only. James did not agree it and referred it to the CSM: "I'm not able to agree credits ... I've passed your request to Callum Reid" (message 9). Policy 6.2: agents "must not promise ... a service credit"; policy 6.3: only the named CSM or Head of Support may offer one, and "An offer is valid only when it is recorded in writing on the ticket or in the account record". Account record: "Open credits: None recorded" (account.md line 16). Owner: Callum Reid (CSM, account.md line 15).

## Service level
Measured at 2026-11-05 11:00 UTC (escalation event, the latest timestamp in the thread). Readings used for ambiguous terms:
- "Business hours are 08:00 to 18:00 Europe/London time, Monday to Friday" and "Between 25 October 2026 and 28 March 2027, Europe/London time is GMT, which is the same as UTC" (policy 1.1): read as 08:00 to 18:00 UTC. 3 to 10 Nov 2026 are read as containing no bank holidays in England (the policy does not list them).
- Support level: "the level recorded in the customer's account record" (policy 1.3), and that field is blank (account.md line 5). Resolution targets are shown for each level as conditional rows; which applies is Not determinable.
- Clock: "starts when the ticket is created" (policy 4.1) = 2026-11-03 14:20 UTC. Paused 2026-11-04 09:30 to 15:00 UTC while "Pending customer" (events; policy 4.2) = 5h30m.

| Target (policy quote) | Clock start | Deadline (arithmetic) | Status |
|---|---|---|---|
| First response, Enterprise P2: "2 hours, 24x7" (3.1) | 2026-11-03 14:20 UTC | 14:20 + 2h = 2026-11-03 16:20 UTC. First agent response 15:02 UTC (event) = 42m | Met |
| First response, Business P2: "4 business hours" (3.1) | 2026-11-03 14:20 UTC | 14:20 + 4 bh = 2026-11-03 18:00 UTC. Response at 15:02 = 42m | Met |
| First response, Standard P2: "8 business hours" (3.1) | 2026-11-03 14:20 UTC | 3 Nov 14:20-18:00 = 3h40m; 4 Nov 08:00-09:30 = 1h30m (5h10m); paused to 15:00; remaining 2h50m → 2026-11-04 17:50 UTC. Response at 15:02 on 3 Nov = 42m | Met |
| Resolution, Enterprise P2: "24 hours, 24x7" (3.1) | 2026-11-03 14:20 UTC | Elapsed to pause: 14:20 3 Nov → 09:30 4 Nov = 19h10m; remaining 4h50m from resume 15:00 → 2026-11-04 19:50 UTC. At reference: 44h40m − 5h30m paused = 39h10m elapsed | If Enterprise: Breached, overdue by 15h10m |
| Resolution, Business P2: "20 business hours" (3.1) | 2026-11-03 14:20 UTC | Elapsed business time: 3 Nov 14:20-18:00 = 3h40m; 4 Nov 08:00-09:30 = 1h30m and 15:00-18:00 = 3h00m; 5 Nov 08:00-11:00 = 3h00m; total 11h10m. Remaining 8h50m: 7h00m on 5 Nov to 18:00, then 1h50m from 08:00 Fri 6 Nov → 2026-11-06 09:50 UTC. At risk when under 25% (5h) remains: 2026-11-05 14:50 UTC | If Business: Within target (8h50m left); at risk from 2026-11-05 14:50 UTC |
| Resolution, Standard P2: "40 business hours" (3.1) | 2026-11-03 14:20 UTC | Elapsed 11h10m (as above). Remaining 28h50m: 7h00m on 5 Nov, 10h on 6 Nov, 10h on 9 Nov = 27h, then 1h50m on Tue 10 Nov → 2026-11-10 09:50 UTC. At risk when under 25% (10h) remains, after 18h50m more: 7h on 5 Nov + 10h on 6 Nov + 1h50m on 9 Nov → 2026-11-09 09:50 UTC | If Standard: Within target (28h50m left) |
| Update cadence, P2: "an update at least once each business day" (7.1) | Each business day | 3 Nov: message 2 (15:02 UTC, event); 4 Nov: message 7 (15:40 UTC); 5 Nov: messages 9 and 12. Next due: by 18:00 UTC on Fri 2026-11-06 (end of business day, my reading), and the 16:00 UTC 5 Nov commitment comes first | Met to date |

Pauses: "The clock is paused only while the ticket status is "Pending customer". It resumes when the status leaves "Pending customer"." (policy 4.2); "Paused time does not count toward any target." (policy 4.3)

Further policy terms that depend on the outcome: "The Support Duty Manager must be told of every P1 ticket and of every P2 ticket that is breached." (policy 5.3). If the support level is Enterprise, this ticket is breached and the Duty Manager must be told now. If priority is changed, "the resolution target becomes the target for the new priority, counted from ticket creation and excluding paused time" (policy 4.4); against 39h10m calendar / 11h10m business time elapsed at reference, Enterprise P1 "8 hours, 24x7" and Business P1 "12 hours, 24x7" would be breached, and Standard P1 "20 business hours" would leave 8h50m (within target; at risk under 5h).

## Recommended next action
Look up the INV-BV-20931 token (created 14 Oct 2026) and a sample of the other 30 failed pre-1 Nov tokens in the PayCollect v3 vault and in the v8.2.3 vault-migration records, to confirm or rule out that pre-1 Nov tokens were not migrated, and check whether other customers show the same PCX-402 pattern since 1 Nov. Owner: Tier 2 Product Engineering Support (ticket owner from escalation, policy 5.2). By 2026-11-05 16:00 UTC, so the open commitment ("I'll update you by 16:00 UTC today", message 12) can be met with a finding, and before the Business-level resolution deadline goes at risk (14:50 UTC) if that is the customer's level. In the same window, Tier 2 should get the support level confirmed (to settle the breach status and the Duty Manager notice under policy 5.3) and read messages 1 to 6 for the credit claim before replying to the customer. This recommendation is my own, built on the evidence above.
