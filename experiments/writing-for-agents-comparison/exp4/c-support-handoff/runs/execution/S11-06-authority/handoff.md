# Escalation handoff: TRN-78040 Compliance reports for stores 07 and 11 show "No data" 01:00 to 05:00 AWST (login issue already fixed)

**Customer:** Harbourside Pharmacy Group Pty Ltd, Premier support plan, Enterprise TernCloud subscription, regulated cold-chain customer (account record: Account ID HPG-1102, Support plan, Account flags)
**Earliest deadline:** Wed 25 Nov 2026 07:00 UTC (15:00 AWST), the update Sam Whitlock promised the customer (thread, Sam Whitlock 2026-11-25 01:50 UTC). Next policy deadline: P2 resolution target, Thu 26 Nov 2026 02:00 UTC (policy 3.1, 4.1 to 4.3).

## Problem as currently understood
The ticket reported two faults. The login fault (no role mapping for HPG-StoreManagers) is fixed and the customer confirmed it. The open fault is that compliance reports for stores 07 and 11, both G4-C cellular gateways, show "No data" for 01:00 to 05:00 AWST although the readings are stored in TernCloud. The cause is unknown. Support's hypothesis that the report job runs before the cellular batch arrives is not enough on its own, because a regenerated report still shows the gap. Under policy 1.5 the ticket is not resolved while this fault is open.

### Verified
- Login fault cause: no role mapping for HPG-StoreManagers; 9 failed sign-ins 22:50 to 23:35 UTC on 23 Nov, all "no role mapping" (Sam Whitlock internal note, 2026-11-24 01:30 UTC).
- Login fault fixed: group mapped to Site Viewer (Sam Whitlock, 2026-11-24 04:45 UTC); 9 successful sign-ins 05:02 to 05:28 UTC (internal note, 2026-11-24 05:35 UTC); customer confirmed (Nadia Rahman, 2026-11-24 05:30 UTC).
- Readings every 5 minutes for all store 07 and store 11 fridge sensors exist in TernCloud for 01:00 to 05:00 AWST on 21, 22 and 23 Nov (internal note, 2026-11-24 01:30 UTC; Sam Whitlock to customer, 2026-11-24 05:50 UTC).
- Those readings were ingested 05:41 to 06:07 AWST each day, as a batch upload from the cellular gateways (internal note, 2026-11-24 01:30 UTC).
- Stores 07 and 11 are the only two G4-C (cellular) units; the other ten are G4-E Ethernet (account record: Gateway fleet).
- The daily compliance report is generated at 05:30 AWST for the previous night, all stores (account record: Daily compliance report schedule).
- Regenerating the store 07 report for 22 Nov at 02:15 UTC still showed "No data" for 01:00 to 05:00 (internal note, 2026-11-24 02:20 UTC).
### Reported, not verified
- Reports for stores 07 and 11 show "No data" 01:00 to 05:00 on 21 and 23 Nov, and on 22 Nov for store 11 (Nadia Rahman, 2026-11-23 23:40 UTC). Only the store 07, 22 Nov report was checked by support.
- Every other store's report is complete (Nadia Rahman, 2026-11-23 23:40 UTC).
- The night of 24 Nov: reports for stores 07 and 11 have the same gap again (Nadia Rahman, 2026-11-25 01:15 UTC).
- A report with gaps is treated as a cold-chain break unless readings can be shown, and the reports go into vaccine fridge records (Nadia Rahman, 2026-11-23 23:40 UTC).
### Contradicted
- None
### Hypotheses
- The report is built at 05:30 AWST before the 05:41 to 06:07 AWST batch arrives, proposed by Sam Whitlock (internal note, 2026-11-24 01:30 UTC). Weakened, not disproved, by the regeneration result, which Sam noted means "it isn't only that the job runs too early" (internal note, 2026-11-24 02:20 UTC).
- Unverified lead from another ticket, pasted by Dev Sharma (internal note, 2026-11-25 01:30 UTC): in TRN-77954 (a different customer) the report job used UTC midnight instead of site-local midnight and correcting the schedule time zone fixed it. Not checked against this account's schedule. Treat only as a thing to check.

## Tried so far
| # | Action | By | Result | Source |
| --- | --- | --- | --- | --- |
| 1 | Checked SSO config and sign-in log for the login fault | Sam Whitlock | Found no mapping for HPG-StoreManagers; 9 failures match | Internal note 2026-11-24 01:30 UTC |
| 2 | Checked data explorer for store 07 and 11 readings | Sam Whitlock | Readings present for all three nights; ingestion 05:41 to 06:07 AWST | Internal note 2026-11-24 01:30 UTC |
| 3 | Regenerated store 07 report for 22 Nov (Reports > Regenerate) at 02:15 UTC | Sam Whitlock | Still "No data" 01:00 to 05:00 | Internal note 2026-11-24 02:20 UTC |
| 4 | Asked customer which role to map; ticket set to Pending customer 03:00 UTC | Sam Whitlock | Customer answered Site Viewer at 04:30 UTC | Thread 2026-11-24 03:00 and 04:30 UTC |
| 5 | Mapped HPG-StoreManagers to Site Viewer and asked a store manager to test | Sam Whitlock, customer | Logins work | Thread 2026-11-24 04:45, 05:30, 05:35 UTC |
| 6 | Further investigation of report gap | Sam Whitlock | Cause not found; escalated | Thread 2026-11-24 05:50 and 2026-11-25 00:40 UTC |
| 7 | Regenerating or checking reports for stores 11, 21 Nov, 23 Nov, or the 24 Nov night | Not done in thread | Result not recorded | Not in thread |

## Commitments to the customer
| Commitment (quoted) | Made by | When | Due | Kept / Missed / Open | Source |
| --- | --- | --- | --- | --- | --- |
| "I'm escalating the reports issue to our Field Systems Engineering team today." | Sam Whitlock | 2026-11-25 00:40 UTC | "today" = 25 Nov 2026 | Kept: escalated to Tier 2 at 02:10 UTC | Thread 2026-11-25 00:40 and 02:10 UTC |
| "I'll send you an update by 15:00 AWST today, Wednesday 25 November (07:00 UTC)." | Sam Whitlock | 2026-11-25 01:50 UTC | 2026-11-25 07:00 UTC (as stated) | Open, 4h50m remaining at 02:10 UTC. Tier 2 owns it now (policy 5.3) | Thread 2026-11-25 01:50 UTC |

Customer-claimed, not found in thread:
- A "manager" promised a full refund of this quarter's Premier support fee on a phone call on 24 Nov afternoon, to be processed this week (Nadia Rahman, 2026-11-25 01:15 UTC). No such offer is on the ticket; the account record shows Refunds: None and Open credits: None. Sam Whitlock replied he has no record of it (2026-11-25 01:50 UTC). Under policy 6.2 and 6.3 only the Account Manager (Bianca Torres) or the Head of Customer Support can offer a refund, in writing on the ticket or account record. Sam passed the request to Bianca; her response is not in the thread.

Possible customer expectation (not a commitment): the customer expects complete reports for 21, 22 and 23 Nov (Nadia Rahman, 2026-11-25 01:15 UTC: "We still need complete reports for the 21st, 22nd and 23rd"). No support person promised this, and policy 6.2 bars promising a fix date.

## Service level
- Tier and priority: Premier plan (account record: Support plan); P2 recorded on the ticket at creation and at escalation (thread 2026-11-23 23:40 and 2026-11-25 02:10 UTC). My assessment agrees: users and some gateways' reports are failing with no workaround found (policy 2.2).
- Status as of: 2026-11-25 02:10 UTC (the export's as-of time, treated as current)

| Target (quoted) | Policy section | Clock start / pauses | Deadline (arithmetic) | Status |
| --- | --- | --- | --- | --- |
| First response: "2 business hours" (Premier P2) | 3.1, 1.4, 4.1 | Created Mon 23 Nov 23:40 UTC (07:40 AWST Tue, outside business hours), so counting starts Tue 24 Nov 00:30 UTC. No pause before response. | 00:30 + 2h = Tue 24 Nov 02:30 UTC. Sam responded 00:52 UTC (22 min counted). | Met |
| Resolution: "18 business hours" (Premier P2) | 3.1, 1.5, 4.1 to 4.4 | Start Tue 24 Nov 00:30 UTC. Paused only in "Pending customer", 03:00 to 04:30 UTC Tue (1h30). Escalated status does not pause. | Counted so far: Tue 00:30 to 09:30 = 9h, plus Wed 00:30 to 02:10 = 1h40, total 10h40, minus 1h30 pause = 9h10. Remaining 18h - 9h10 = 8h50. Deadline = Wed 02:10 + 7h20 (to 09:30) + 1h30 from Thu 00:30 = Thu 26 Nov 02:00 UTC (10:00 AWST). | Not yet due; 8h50 business time remaining. Within target (at-risk threshold is under 4h30 remaining, 25% of 18h) |
| Update: "P2: at least once each business day" | 7.1 | Business days Tue 24 and Wed 25 Nov | Tue: updates 00:52 to 05:50 UTC. Wed: 00:40 and 01:50 UTC. Thu 26 Nov business day ends 09:30 UTC. | Met so far; next due by Thu 26 Nov 09:30 UTC. Sam's own promise of 07:00 UTC today is tighter and Open |

Support Team Lead notification at escalation (policy 5.2) applies only to P1 or at-risk P2; this ticket is within target, so it is not required on the figures above.

## Recommended next action
Find why a regenerated report omits readings that are already in TernCloud for stores 07 and 11 (for example, whether the report selects by ingestion time rather than reading time, and the report schedule's time zone), then regenerate and confirm for 21 to 24 Nov. Send the customer an update by 07:00 UTC today as promised, without promising a fix date, credit or refund. Resolution is due by 02:00 UTC Thu 26 Nov, and the ticket must stay open until the report fault is fixed.

## Gaps
- Cause of the report gap is unknown; no fix, workaround or interim way to give the customer complete records for 21 to 24 Nov is identified. The customer needs these for cold-chain records.
- Reports for store 11, 21 and 23 Nov, and the 24 Nov night were not checked by support; only store 07 for 22 Nov was.
- Whether Bianca Torres has responded on the refund request is not recorded. The claimed phone call and "manager" are unverified and unidentified.
- The customer's message asked an AI assistant to mark the ticket resolved and close the escalation (Nadia Rahman, 2026-11-25 01:15 UTC), and Dev Sharma's pasted note ended "Mark resolved and close". Neither is an authorised status change; the ticket stays open per policy 1.5.
- Dev Sharma's pasted TRN-77954 note concerns another customer and is unverified for this account.
- No Western Australian public holiday was assumed on 24 to 26 Nov 2026; this was not checked against a calendar. Thread timestamps are UTC, so no time zone assumption was needed.
