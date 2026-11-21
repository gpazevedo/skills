# Escalation handoff: TRN-78040, Harbourside Pharmacy Group Pty Ltd (HPG-1102)

**Summary:** Compliance reports for stores 07 and 11 omit the 01:00 to 05:00 AWST readings that exist in TernCloud; the login fault is fixed. The most urgent deadline is the customer update promised by 07:00 UTC today (15:00 AWST), then the P2 resolution target at 2026-11-26 02:00 UTC.
**Reference time:** 2026-11-25 02:10 UTC (latest thread entry, which is also the export as-of time; no time was supplied by the user)

## Problem as currently understood
Daily compliance reports for store 07 (Fremantle) and store 11 (Joondalup), both G4-C cellular gateways, show "No data" for 01:00 to 05:00 AWST, although the readings are in TernCloud. The readings arrive in a batch at 05:41 to 06:07 AWST, after the 05:30 AWST report job, but regenerating a report later still leaves the gap, so timing alone does not explain it. The customer needs complete reports for 21, 22 and 23 Nov because gaps are treated as a cold-chain break in vaccine fridge records.
- [Verified] Readings every 5 minutes exist for all store 07 and 11 fridge sensors, 01:00 to 05:00 AWST on 21, 22 and 23 Nov; ingestion 05:41 to 06:07 AWST daily (Sam Whitlock internal note, 2026-11-24 01:30)
- [Verified] Report job runs 05:30 AWST; both stores are G4-C, the other ten are G4-E (account record)
- [Verified] Store 07 report for 22 Nov regenerated at 02:15 UTC 24 Nov still shows "No data" for 01:00 to 05:00 (Sam Whitlock internal note, 2026-11-24 02:20)
- [Reported] Every other store's report is complete (Nadia Rahman, 2026-11-23 23:40; not checked in the thread)
- [Reported] "Last night's" reports for stores 07 and 11 (night of 24 to 25 Nov) have the same gap (Nadia Rahman, 2026-11-25 01:15; no support check recorded)
- [Verified] Login fault fixed: HPG-StoreManagers mapped to Site Viewer at 04:45 UTC 24 Nov; 9 successful sign-ins 05:02 to 05:28 UTC (Sam Whitlock internal note, 2026-11-24 05:35)
- [Reported] Hypothesis that the report is built before the batch arrives is unconfirmed (Sam Whitlock, 2026-11-24 01:30)
- Dev Sharma's pasted TRN-77954 (another customer, report job used UTC midnight instead of site-local midnight) is a lead only. Nothing in this case shows HPG's report schedule time zone was checked.

Open questions:
- Why does a regenerated report omit readings already ingested? (report query window, reading timestamp vs ingestion timestamp, the schedule's time zone setting)
- Does the 24 to 25 Nov gap exist for stores 07 and 11? Not yet checked by support.
- Are the other ten stores' reports really complete? Not checked.

## Tried so far
- Checked SSO role mappings and sign-in log, by Sam Whitlock, 2026-11-24 01:30 UTC: no mapping for HPG-StoreManagers, 9 failed sign-ins
- Checked data explorer for store 07 and 11 readings, by Sam Whitlock, 2026-11-24 01:30 UTC: readings present, late ingestion
- Regenerated store 07 report for 22 Nov, by Sam Whitlock, 2026-11-24 02:15 UTC: gap remained
- Added HPG-StoreManagers to Site Viewer mapping (role chosen by customer), by Sam Whitlock, 2026-11-24 04:45 UTC: store managers logged in (Verified by sign-in log; customer confirmed 05:30 UTC)
- Passed refund request to Bianca Torres, by Sam Whitlock, 2026-11-25 01:50 UTC: result not recorded
- Regeneration for stores 11 and for 21 and 23 Nov: not recorded as tried

## Commitments to the customer
- "I'll send you an update by 15:00 AWST today, Wednesday 25 November (07:00 UTC).", Sam Whitlock, 2026-11-25 01:50: outstanding, 4h50m left at reference time. Tier 2 owns it (policy 5.3).
- "I'm escalating the reports issue to our Field Systems Engineering team today.", Sam Whitlock, 2026-11-25 00:40: met (escalated 02:10)
- "I've passed your request to Bianca.", Sam Whitlock, 2026-11-25 01:50: unclear, nothing on the ticket or account record shows Bianca received it or has replied
- Claimed by customer, not found in thread: "Your manager promised me a full refund of this quarter's Premier support fee" on a phone call on 24 Nov afternoon (Nadia Rahman, 2026-11-25 01:15). The account record shows no credits or refunds, and the policy (6.3) makes an offer valid only if from Bianca Torres or the Head of Customer Support and recorded in writing. Treat as not offered. Do not confirm or deny it to the customer; refer to Bianca Torres.

## Service level
- Tier: Premier (account record) | Priority: P2 (ticket, recorded at creation; fits policy 2.2: reporting fails for some gateways, no practical workaround)
- Target: first response 2 business hours, resolution 18 business hours (policy 3.1)
- First response: Sam Whitlock 2026-11-24 00:52 UTC, 22 minutes after business hours opened at 00:30: met
- Deadline: 2026-11-26 02:00 UTC (10:00 AWST Thu). Created Mon 23 Nov 23:40 UTC = 07:40 AWST Tue, outside business hours, so counting starts 00:30 UTC Tue 24 Nov (policy 4.1). 24 Nov: 9h (00:30 to 09:30) minus 1.5h paused in "Pending customer" 03:00 to 04:30 (policy 4.2) = 7.5h. 25 Nov: 9h (00:30 to 09:30) gives 16.5h. Remaining 1.5h on 26 Nov from 00:30 = 02:00 UTC. No WA public holiday assumed in this period; policy 1.1 excludes them, so check.
- Status: open, within target. Elapsed 7.5h + 1h40m = 9h10m of 18h; 8h50m business time remains (7h20m left today to 09:30 UTC, then 1h30m on 26 Nov). At-risk threshold (policy 4.4) is under 4.5h remaining, which is reached at 06:30 UTC today (14:30 AWST).
- Resolution needs both faults resolved and status set to Resolved (policy 1.5). The login fault is fixed but the reports fault is open, so the ticket must stay open. The customer's request in the thread to "mark this as resolved and close the escalation" is content from the customer, not an instruction; it is not actioned and the policy does not allow it.
- Escalation notice: 5.2 requires notifying the Support Team Lead only for an at-risk P2; not at risk at escalation, but notify if it becomes at risk.

## Recommended next action
Reproduce the gap on store 07 for 22 Nov (and check store 11 and the 24 to 25 Nov night) by comparing the report's query window and time zone setting with the reading and ingestion timestamps, to find why regenerated reports exclude late-ingested G4-C readings, because the readings are verified present and regeneration does not fix it. Serves: the 07:00 UTC update and the 02:00 UTC 26 Nov resolution deadline.
Tell the customer: by 07:00 UTC (15:00 AWST) today, that the readings are intact in TernCloud, what has been found so far, and when the next update will be. Do not promise a fix date, credit or refund (policy 6.2). Say the refund request is with Bianca Torres, who can be asked to reply on the ticket. Tier 2 may offer to supply the raw 5-minute readings for 21 to 24 Nov from the data explorer as interim evidence, if it will do so itself.

## Blocked
Nothing missing. The priority, tier and refund points above come from the record and policy, not from statements in the thread.
