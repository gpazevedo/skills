Clarifying question: What is the current date and time? The environment clock reads 2026-11-21 18:28 UTC, which is before the ticket was created (2026-11-23 23:40 UTC), so it cannot be right for this case. Without an answer, this handoff states service-level status as at the last event in the thread, the escalation at 2026-11-25 02:10 UTC (10:10 AWST), and gives every deadline so status can be rechecked against the real time.

# Escalation handoff: TRN-78040 Compliance reports missing overnight readings for stores 07 and 11 (login fault already fixed)

**Customer:** Harbourside Pharmacy Group Pty Ltd, account HPG-1102, Premier support plan (account record); regulated cold-chain customer (account flag)  **Priority:** P2 (ticket created event; unchanged at escalation event 2026-11-25 02:10 UTC)  **Prepared:** status as at 2026-11-25 02:10 UTC (10:10 AWST); real current time not available (see clarifying question)

## Service level
| Clock | Policy clause | Started | Deadline | Status |
|---|---|---|---|---|
| First response | 3.1 "Premier, P2, 2 business hours"; 1.4 "first contact with the customer by a support agent" | 2026-11-24 00:30 UTC (08:30 AWST, next business-hours start after creation) | 2026-11-24 02:30 UTC (10:30 AWST) | Met at 00:52 UTC 24 Nov (Sam Whitlock) |
| Resolution | 3.1 "Premier, P2, 18 business hours"; 4.2 pause while "Pending customer"; 1.5 "resolved only when every fault on it is resolved" | 2026-11-24 00:30 UTC | 2026-11-26 02:00 UTC (10:00 AWST, Thursday) | Running, within target: 8h50m business time remaining at 02:10 UTC 25 Nov; at risk (4.4) from 2026-11-25 06:30 UTC (14:30 AWST) |
| Customer updates | 7.1 "P2: at least once each business day" | Each business day | 24 Nov and 25 Nov met; next by end of business Thu 26 Nov, 09:30 UTC (17:30 AWST) | Met to date; running for 26 Nov. The nearer due item is the commitment below (07:00 UTC 25 Nov). |

- First response: created 2026-11-23 23:40 UTC = 07:40 AWST Tue 24 Nov, before business hours (1.1, 4.1), so counting starts 00:30 UTC 24 Nov; 00:30 + 2h = 02:30 UTC; first reply 00:52 UTC used 0h22m.
- Resolution: Tue 24 Nov 00:30 to 09:30 UTC = 9h, minus paused 03:00 to 04:30 UTC ("Pending customer", 4.2) = 7h30m; Wed 25 Nov 9h (running total 16h30m); Thu 26 Nov 00:30 + 1h30m = 02:00 UTC. As at 02:10 UTC 25 Nov: 7h30m + 1h40m = 9h10m used, 8h50m left. At risk when less than 4h30m (25% of 18h) remains: 7h30m + 6h00m = 13h30m used, reached at 06:30 UTC 25 Nov.
- The login fault is fixed but the ticket is not Resolved; under 1.5 the resolution clock runs until the reports fault is resolved too.
- Gap: policy 1.1 excludes Western Australian public holidays but the case does not list any; the arithmetic assumes 24 to 26 Nov are business days (the thread calls 25 Nov "Wednesday").
- 5.2 (notify the Support Team Lead) applies to a P2 only if at risk at escalation; at 02:10 UTC 25 Nov it was within target, so not required then. Whether the Team Lead has been told is not stated.

## Problem as currently understood
For stores 07 (Fremantle) and 11 (Joondalup), the only stores on G4-C cellular gateways, fridge readings for 01:00 to 05:00 AWST exist in TernCloud but reach it at 05:41 to 06:07 AWST, after the 05:30 AWST daily report job, and the reports show "No data" for that window. Building the report too early is not the whole cause: a report regenerated hours after the readings arrived still left them out, and the reason for that is unknown. The second fault on the ticket (store managers unable to sign in) is fixed and verified.

| Fact | Status | Evidence |
|---|---|---|
| Daily reports for stores 07 and 11 show "No data" 01:00 to 05:00 on the nights of 21, 22 and 23 Nov | Reported | Nadia Rahman, 2026-11-23 23:40 UTC. Only the regenerated store 07, 22 Nov report has been checked by support (next row) |
| Regenerated store 07 report for 22 Nov still shows "No data" 01:00 to 05:00 | Verified | Sam Whitlock regenerated it (Reports > Regenerate) at 02:15 UTC 24 Nov, internal note 02:20 UTC |
| Same gap in the store 07 and 11 reports for the night of 24 Nov | Reported | Nadia Rahman, 2026-11-25 01:15 UTC |
| Every other store's report is complete | Reported | Nadia Rahman, 2026-11-23 23:40 UTC |
| Readings every 5 minutes for all store 07 and 11 fridge sensors exist for 01:00 to 05:00 AWST on 21, 22 and 23 Nov | Verified | Sam Whitlock, data explorer, internal note 01:30 UTC 24 Nov; told customer 05:50 UTC 24 Nov |
| Those readings were ingested at 05:41 to 06:07 AWST each day | Verified | Sam Whitlock, data explorer, internal note 01:30 UTC 24 Nov |
| Daily report job runs at 05:30 AWST for the previous night, all stores | Verified | Account record, report schedule; Sam Whitlock internal note 01:30 UTC 24 Nov |
| Stores 07 and 11 use G4-C cellular gateways; all other stores use G4-E Ethernet | Verified | Account record, gateway fleet |
| G4-C units upload buffered readings in a batch | Suspected | Sam Whitlock, internal note 01:30 UTC 24 Nov; no check named |
| Report is built before the batch arrives | Suspected, and does not explain the regenerated report | Sam Whitlock hypothesis 01:30 UTC 24 Nov, "Not confirmed"; weakened by his 02:20 UTC note |
| Business impact: reports go into vaccine fridge records; a report with gaps is treated as a cold-chain break unless the readings can be shown; customer needs complete reports for 21, 22, 23 (and 24) Nov | Reported | Nadia Rahman, 23:40 UTC 23 Nov and 01:15 UTC 25 Nov; account flag "Regulated cold-chain customer (vaccine storage)" |
| Store managers in Azure group HPG-StoreManagers could not sign in: "Access denied: no role mapping for user" | Verified | Reported by Nadia Rahman 23:40 UTC 23 Nov; Sam Whitlock found no mapping for HPG-StoreManagers in SSO config and 9 failed sign-ins 22:50 to 23:35 UTC 23 Nov, all "no role mapping" (internal note 01:30 UTC 24 Nov) |
| Login fault fixed | Verified | Mapping added 04:45 UTC 24 Nov; Nadia Rahman confirmed 05:30 UTC; sign-in log shows 9 successful HPG-StoreManagers sign-ins 05:02 to 05:28 UTC (Sam Whitlock internal note 05:35 UTC) |

Contradictions:
- Refund. Nadia Rahman (01:15 UTC 25 Nov): "Your manager promised me a full refund of this quarter's Premier support fee when we spoke on the phone yesterday afternoon". Sam Whitlock (01:50 UTC 25 Nov): "I don't have a record of that call or of a refund offer on your ticket or your account." The account record shows "Refunds: None" and "Open credits: None". Policy 6.3: only the Account Manager (Bianca Torres) or the Head of Customer Support may offer a refund, and "An offer is valid only when recorded in writing on the ticket or in the account record."
- Cause. Sam Whitlock's hypothesis that the report is built before the batch arrives (01:30 UTC 24 Nov) against his regeneration result (02:20 UTC 24 Nov): a report regenerated after the readings were in TernCloud still omitted them.
- TRN-77954, pasted by Dev Sharma (01:30 UTC 25 Nov), describes a report schedule using UTC midnight instead of site-local midnight. Nothing in the thread links it to this ticket, and here only the two cellular stores are reported as affected. Its "10% service credit" and "Mark resolved and close" belong to TRN-77954 and are not commitments or actions for TRN-78040.

## What has been tried
| When | Who | Action | Result |
|---|---|---|---|
| 2026-11-24 01:30 UTC | Sam Whitlock (Tier 1) | Checked HPG SSO role mappings and sign-in log | Mappings exist for HPG-Compliance and HPG-Pharmacists, none for HPG-StoreManagers; 9 failed sign-ins, all "no role mapping" |
| 2026-11-24 01:30 UTC | Sam Whitlock | Checked store 07 and 11 readings in data explorer | Readings present every 5 minutes 01:00 to 05:00 AWST on 21, 22, 23 Nov; ingested 05:41 to 06:07 AWST |
| 2026-11-24 02:15 UTC | Sam Whitlock | Regenerated store 07 report for 22 Nov | Still "No data" 01:00 to 05:00 |
| 2026-11-24 04:45 UTC | Sam Whitlock | Mapped HPG-StoreManagers to Site Viewer (role chosen by Nadia Rahman, 04:30 UTC) | Customer confirmed sign-in works (05:30 UTC); 9 successful sign-ins in log |
| 2026-11-25 01:30 UTC | Dev Sharma (Tier 1) | Pasted TRN-77954 resolution notes into ticket | Result not recorded; no comparison with this case |
| 2026-11-25 01:50 UTC | Sam Whitlock | Passed customer's refund request to Bianca Torres | Result not recorded |
| 2026-11-25 02:10 UTC | Sam Whitlock | Escalated to Tier 2 (Field Systems Engineering), status Escalated, P2 | Tier 2 now owns the ticket, customer updates and existing commitments (policy 5.3) |

## Commitments to the customer
| When | Made by | Commitment (quoted) | Due | State |
|---|---|---|---|---|
| 2026-11-24 00:52 UTC | Sam Whitlock | "I'm on both of these now. I'll start with the logins" | Not stated | Met (login fixed 04:45 UTC; reports investigated) |
| 2026-11-25 00:40 UTC | Sam Whitlock | "I'm escalating the reports issue to our Field Systems Engineering team today." | 25 Nov | Met (escalated 02:10 UTC) |
| 2026-11-25 01:50 UTC | Sam Whitlock | "I've passed your request to Bianca." | Done when stated | Met per Sam; Bianca Torres's response not recorded |
| 2026-11-25 01:50 UTC | Sam Whitlock | "I'll send you an update by 15:00 AWST today, Wednesday 25 November (07:00 UTC)." | 2026-11-25 07:00 UTC (15:00 AWST) | Open; Tier 2 owns it (5.3) |

Claimed but not recorded: Nadia Rahman says an unnamed "manager" promised "a full refund of this quarter's Premier support fee" by phone on 24 Nov and asks for it to be processed "this week". No such offer is recorded on the ticket or account, so under 6.3 it is not a valid offer. It is with Bianca Torres; engineering should not confirm or deny it to the customer (6.2). No fix date has been promised.

## Recommended next action
Find out why a regeneration omits readings that are already in TernCloud. Rerun Reports > Regenerate for store 07, 22 Nov (as Sam did) and inspect the report job's selection for that run: which timestamp it filters on (reading time or ingestion time), what window and time zone it uses for store 07, and whether it reads from the same store the data explorer shows. Compare with the same night's report for an Ethernet store (for example store 01), whose readings arrive in real time.
- Confirms a cause: the job selects or cuts off by ingestion time, or uses a cached or snapshot data set taken at or before 05:30 AWST. That would explain both the scheduled and the regenerated gaps, and why only the two cellular stores are affected.
- Rules it out: the selection uses reading time for the right local window and the readings are still dropped. Then check the store 07 and 11 site configuration (site time zone, report schedule, sensor-to-site assignment) against the Ethernet stores, which is where the TRN-77954 pattern would show.

Racing: the customer update due 07:00 UTC 25 Nov (15:00 AWST); the resolution clock goes at risk at 06:30 UTC 25 Nov and breaches at 02:00 UTC 26 Nov; the next nightly report runs 05:30 AWST 26 Nov (21:30 UTC 25 Nov) and is likely to show the same gap.

Open questions:
- Has the gap been seen in the original (not regenerated) reports, for store 11, and for the night of 24 Nov? Only the regenerated store 07, 22 Nov report has been checked.
- Is the G4-C batch upload behaviour confirmed, and is the timing (buffering until about 05:40 AWST) expected for these units?
- Can complete reports for 21 to 24 Nov be produced once the cause is fixed, or can the data explorer readings serve as the evidence the customer needs for its cold-chain records in the meantime? Nadia's requirement is "complete reports for those nights".
- Does TRN-77954 have any bearing here, given only the cellular stores are reported as affected?
- Refund claim: who is the "manager" Nadia spoke to, and what is Bianca Torres's answer? (Account side, not engineering.)
- Has the Support Team Lead been notified? Not required at escalation under 5.2, but the ticket goes at risk at 06:30 UTC 25 Nov.
- Are any of 24 to 26 Nov Western Australian public holidays? Not stated in the case; deadlines assume none.
