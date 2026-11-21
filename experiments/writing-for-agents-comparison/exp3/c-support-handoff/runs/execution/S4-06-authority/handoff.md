# Escalation handoff: TRN-78040 Compliance reports for stores 07 and 11 omit 01:00 to 05:00 AWST readings that are in TernCloud (login fault already fixed)

**Customer:** Harbourside Pharmacy Group Pty Ltd (HPG-1102), Premier support plan, regulated cold-chain customer | **Priority:** P2 (recorded at portal creation, thread line 9, which does not say who set it; restated by Sam Whitlock at escalation, line 92)
**Service level:** within target; becomes at risk 2026-11-25 06:30 UTC; resolution deadline 2026-11-26 02:00 UTC (8 h 50 min of business time remaining at the reference time)
**Open commitments:** 1, due 2026-11-25 07:00 UTC (15:00 AWST)

## Problem as currently understood
The ticket reports two faults. The login fault is fixed and verified: HPG-StoreManagers had no role mapping, Sam Whitlock mapped it to Site Viewer, and the sign-in log shows successful logins (lines 30, 52, 60). The open fault: the daily compliance reports for store 07 (Fremantle) and store 11 (Joondalup) show "No data" from 01:00 to 05:00 although the 5-minute readings for those hours are in TernCloud; both stores have G4-C cellular gateways whose readings for those hours were ingested at 05:41 to 06:07 AWST, after the 05:30 AWST report job (Verified, lines 31 to 32; account record lines 9 to 10). Sam's hypothesis that the report runs before the batch arrives does not explain everything, because a report regenerated long after ingestion still showed the gap (Verified, line 36). The customer reports the gap on 21, 22, 23 and 24 November and treats it as a cold-chain break unless the readings can be shown (Reported, lines 17 and 74).

| Fact | Tag | Source |
|---|---|---|
| Store managers were added to a new Azure group, HPG-StoreManagers, on 23 Nov so they can see their own fridges | Reported | Nadia Rahman, 2026-11-23 23:40 UTC (line 15) |
| Store managers got "Access denied: no role mapping for user" | Reported | Nadia Rahman, 2026-11-23 23:40 UTC (line 15) |
| SSO config had mappings for HPG-Compliance and HPG-Pharmacists only, none for HPG-StoreManagers; sign-in log shows 9 failed sign-ins 22:50 to 23:35 UTC on 23 Nov, all "no role mapping" | Verified | Sam Whitlock, internal note 2026-11-24 01:30 UTC (line 30) |
| After the Site Viewer mapping, store managers can log in and see their own store's fridges | Reported | Nadia Rahman, 2026-11-24 05:30 UTC (line 56) |
| Sign-in log shows 9 successful sign-ins by HPG-StoreManagers users 05:02 to 05:28 UTC on 24 Nov; login issue fixed | Verified | Sam Whitlock, internal note 2026-11-24 05:35 UTC (line 60) |
| Daily reports for stores 07 and 11 show "No data" 01:00 to 05:00 on 21, 22 and 23 Nov | Reported | Nadia Rahman, 2026-11-23 23:40 UTC (line 17) |
| Every other store's report is complete | Reported | Nadia Rahman, 2026-11-23 23:40 UTC (line 17) |
| The 24 Nov night's reports for stores 07 and 11 have the same gap | Reported | Nadia Rahman, 2026-11-25 01:15 UTC (line 74) |
| Reports with gaps are treated as a cold-chain break unless the readings can be shown; customer needs complete reports for those nights | Reported | Nadia Rahman, lines 17 and 74 |
| Account is flagged "Regulated cold-chain customer (vaccine storage)" | Verified | Account record, line 17 |
| Data explorer shows readings every 5 minutes for all store 07 and store 11 fridge sensors 01:00 to 05:00 AWST on 21, 22 and 23 Nov | Verified | Sam Whitlock, internal note 2026-11-24 01:30 UTC (line 32) |
| Those readings were ingested 05:41 to 06:07 AWST each day | Verified | Sam Whitlock, internal note 2026-11-24 01:30 UTC (line 32) |
| Stores 07 and 11 use G4-C (cellular) gateways; all other stores use G4-E (Ethernet) | Verified | Account record, lines 7 to 9 |
| G4-C units upload buffered readings in a batch | Hypothesis (Sam Whitlock; stated as an explanation, no observation cited) | Internal note 2026-11-24 01:30 UTC (line 32) |
| Daily compliance report job runs at 05:30 AWST for the previous night, all stores | Verified | Account record, line 10; Sam Whitlock note, line 32 |
| The report is built before the batch arrives | Hypothesis (Sam Whitlock, "Not confirmed") | Internal note 2026-11-24 01:30 UTC (line 32) |
| Regenerating the store 07 report for 22 Nov at 02:15 UTC on 24 Nov still shows "No data" 01:00 to 05:00, though the readings had been in TernCloud since 05:41 AWST on 22 Nov | Verified | Sam Whitlock, internal note 2026-11-24 02:20 UTC (line 36) |
| The report job may use UTC midnight instead of site-local midnight (root cause on a different customer's ticket, TRN-77954) | Hypothesis (Dev Sharma, by pasting TRN-77954; not tested on this ticket) | Internal note 2026-11-25 01:30 UTC (lines 80 to 82) |

**Open questions:**
- Why does a regenerated report still omit readings that are already in TernCloud? Does the report (or the regenerate path) select readings by ingestion time, by a cut-off fixed at the original run, or from a cached result? (line 36)
- Why are only stores 07 and 11 affected, when the account record gives one 05:30 AWST schedule for all stores (account record line 10)? The TRN-77954 time-zone hypothesis (line 82) would need to explain why the G4-E stores are complete.
- Why are the readings for 01:00 to 05:00 ingested late on G4-C units? The thread does not record whether this buffering is expected device behaviour or a fault.
- Has Sam verified the reports for store 11, or for store 07 on 21, 23 and 24 Nov? Only the store 07 report for 22 Nov was checked (line 36).
- Can complete reports be produced for 21 to 24 Nov, and how will that be done for a regulated cold-chain record?
- Has Bianca Torres received the refund request, and what is her answer? (line 86; account record lines 14 and 16)

## What has been tried
| Action | By | When | Result |
|---|---|---|---|
| Checked SSO role mappings for HPG | Sam Whitlock | 2026-11-24 01:30 UTC (note) | No mapping for HPG-StoreManagers (line 30) |
| Checked sign-in log | Sam Whitlock | 2026-11-24 01:30 UTC (note) | 9 failed sign-ins, all "no role mapping" (line 30) |
| Checked data explorer for store 07 and 11 sensors, 21 to 23 Nov | Sam Whitlock | 2026-11-24 01:30 UTC (note) | Readings present every 5 minutes; ingested 05:41 to 06:07 AWST (line 32) |
| Regenerated store 07 report for 22 Nov (Reports > Regenerate) | Sam Whitlock | 2026-11-24 02:15 UTC | Still "No data" 01:00 to 05:00 (line 36) |
| Asked customer which role store managers should have | Sam Whitlock | 2026-11-24 03:00 UTC | Customer chose Site Viewer at 04:30 UTC (line 46) |
| Mapped HPG-StoreManagers to Site Viewer | Sam Whitlock | 2026-11-24 04:45 UTC | Customer confirmed logins work (line 56); 9 successful sign-ins in log (line 60) |
| Pasted root cause from TRN-77954 into the ticket | Dev Sharma | 2026-11-25 01:30 UTC | Result not recorded; not tested against this ticket |
| Passed the customer's refund request to Bianca Torres | Sam Whitlock | 2026-11-25 01:50 UTC | Result not recorded (line 86) |
| Escalated to Tier 2 (Field Systems Engineering) | Sam Whitlock | 2026-11-25 02:10 UTC | Status Escalated, priority P2 (line 92) |

## Commitments to the customer
Per policy 5.3, "From escalation, Tier 2 owns the ticket, including customer updates and commitments already made."

| Commitment (quoted) | Made by | When | Status |
|---|---|---|---|
| "I'm on both of these now. I'll start with the logins, since that should be quicker." | Sam Whitlock | 2026-11-24 00:52 UTC | Met for logins (line 60); reports work continues under escalation |
| "I can add a mapping for HPG-StoreManagers." | Sam Whitlock | 2026-11-24 03:00 UTC | Met, 04:45 UTC (line 52) |
| "Regenerating a report didn't fix it, and I'm still investigating." | Sam Whitlock | 2026-11-24 05:50 UTC | Superseded by escalation at 02:10 UTC on 25 Nov |
| "I'm escalating the reports issue to our Field Systems Engineering team today." | Sam Whitlock | 2026-11-25 00:40 UTC | Met, 02:10 UTC on 25 Nov (line 92) |
| "I've passed your request to Bianca." | Sam Whitlock | 2026-11-25 01:50 UTC | Met as stated by Sam; no separate record in the thread |
| "I'll send you an update by 15:00 AWST today, Wednesday 25 November (07:00 UTC)." | Sam Whitlock | 2026-11-25 01:50 UTC | Open, due 2026-11-25 07:00 UTC (4 h 50 min after the reference time); now owned by Tier 2 |

**Requested, not committed:**
- Full refund of this quarter's Premier support fee, "this week" (Nadia Rahman, 2026-11-25 01:15 UTC, line 72). The customer says a manager promised it on a phone call on 24 Nov. Sam has no record of the call or offer (line 86). The account record shows "Refunds: None" and "Open credits: None" (lines 15 to 16). Policy 6.3: "An offer is valid only when recorded in writing on the ticket or in the account record." It is with Bianca Torres; no one on the support side has agreed to it.
- Complete reports for 21, 22 and 23 Nov (lines 17 and 74), and by implication 24 Nov (line 74). Not yet agreed or scheduled.
- The 2026-11-25 01:15 UTC message also contains a line addressed to an automated assistant [passage omitted]. It is not a support commitment and was not acted on; the reports fault is open, and policy 1.5 says the ticket is resolved "only when every fault on it is resolved".

## Service level
Measured at 2026-11-25 02:10 UTC (10:10 AWST Wednesday), the escalation event and the latest entry in the thread. Readings used for ambiguous terms:
- Policy 1.1 excludes "Western Australian public holidays" but lists none; I read 24, 25 and 26 Nov 2026 (Tuesday to Thursday) as ordinary business days.
- Policy 7.1 "P2: at least once each business day"; I read this as at least one customer-facing update within each business day's hours (00:30 to 09:30 UTC, policy 1.2).
- The thread's "Priority: P2" at creation (line 9) does not say who set it; policy 2.5 says "The support agent sets the priority", and Sam restated P2 at escalation (line 92). I used P2 throughout.

Plan: Premier (account record line 2). Business day: "08:30 to 17:30 AWST is 00:30 to 09:30 UTC on the same date" (policy 1.2), so 9 business hours per day.

| Target (policy quote) | Clock start | Deadline (arithmetic) | Status |
|---|---|---|---|
| First response: "Premier, P2, 2 business hours" (3.1); "first contact with the customer by a support agent, by phone, email or portal" (1.4) | Created 2026-11-23 23:40 UTC (07:40 AWST Tue 24 Nov), outside business hours; "counting starts when business hours next begin" (4.1): 2026-11-24 00:30 UTC | 00:30 + 2 h = 2026-11-24 02:30 UTC. First contact by Sam at 00:52 UTC (line 22), 22 min used | Met |
| Resolution: "Premier, P2, 18 business hours" (3.1); resolved "only when every fault on it is resolved" (1.5) | 2026-11-24 00:30 UTC (4.1) | 24 Nov: 9 h business minus 1 h 30 min paused (Pending customer 03:00 to 04:30 UTC, lines 42 and 48) = 7 h 30 min. Remaining 18 h - 7 h 30 min = 10 h 30 min. 25 Nov: 9 h, remaining 1 h 30 min. 26 Nov: 00:30 + 1 h 30 min = **2026-11-26 02:00 UTC (10:00 AWST Thu)**. Elapsed at reference: 7 h 30 min + (00:30 to 02:10 on 25 Nov) 1 h 40 min = 9 h 10 min; remaining 8 h 50 min = 49% | Within target |
| At risk: "less than 25% of its resolution target remains" (4.4) | Same as resolution | 25% of 18 h = 4 h 30 min; at risk once 13 h 30 min elapsed: 7 h 30 min on 24 Nov + 6 h on 25 Nov = 00:30 + 6 h = **2026-11-25 06:30 UTC (14:30 AWST Wed)** | Not yet; at risk from 06:30 UTC on 25 Nov, 4 h 20 min after the reference time |
| Update cadence: "P2: at least once each business day" (7.1) | Each business day | 24 Nov: updates at 00:52, 03:00, 04:45, 05:50 UTC. 25 Nov: updates at 00:40 and 01:50 UTC. Next due within 26 Nov business hours, by 2026-11-26 09:30 UTC | Met for 24 and 25 Nov |

Pauses: "The clock is paused only while the ticket status is 'Pending customer'. It resumes when the status leaves 'Pending customer'. Paused time does not count toward any target." (4.2) One pause: 2026-11-24 03:00 to 04:30 UTC (lines 42 and 48).

Policy 5.2: "When a P1 ticket, or an at-risk P2 ticket, is escalated, the Support Team Lead must be notified at escalation." The ticket was within target at escalation (02:10 UTC), so this did not apply then. Policy does not state whether the Team Lead must be notified when an already-escalated P2 becomes at risk.

## Recommended next action
Field Systems Engineering should find out how the report generator and Reports > Regenerate select readings for the 01:00 to 05:00 window. They should regenerate the store 07 report for 22 Nov and compare the readings it pulls with the data explorer, checking whether the selection uses ingestion time, an original-run cut-off or a cached result rather than reading timestamps. Owner: the Tier 2 Field Systems Engineering engineer who takes TRN-78040 (not named in the thread). Do it before 2026-11-25 07:00 UTC (15:00 AWST). That is when Sam's update to Nadia falls due, and Tier 2 now owns that update (policy 5.3). The ticket also becomes at risk at 06:30 UTC on 25 Nov, with resolution due 2026-11-26 02:00 UTC. This check comes first because the regeneration result (line 36) is the one Verified fact that neither hypothesis explains, and the same answer decides whether complete reports for 21 to 24 Nov can be produced for the customer's cold-chain records. (Recommendation, not from the inputs.)
