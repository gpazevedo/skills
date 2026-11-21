# Escalation handoff: TRN-78040: Store 07 and 11 compliance reports omit 01:00 to 05:00 AWST readings

**Customer:** Harbourside Pharmacy Group Pty Ltd (HPG-1102), Premier · **Priority:** P2 · **Next deadline:** 07:00 UTC (15:00 AWST) Wed 25 Nov 2026, outstanding, customer update promised, 4h50m left (as of 2026-11-25 02:10 UTC)

## Problem as currently understood
The daily compliance reports for store 07 (Fremantle) and store 11 (Joondalup) show "No data" from 01:00 to 05:00 AWST, reported for the nights of 21, 22 and 23 Nov and, per the customer, again last night. The readings are in TernCloud, so the fault is in report generation, not capture. Both stores use G4-C cellular gateways that upload in a batch after the 05:30 AWST report job, but regenerating a report later did not fix it, so job timing is not the whole cause. The customer uses these reports as vaccine fridge records, and gaps are treated as cold-chain breaks. The second fault on the ticket (store manager logins) is fixed.

Evidence:
- [Verified] Readings every 5 minutes exist for all store 07 and 11 fridge sensors, 01:00 to 05:00 AWST on 21, 22 and 23 Nov (Sam Whitlock internal note, 2026-11-24 01:30 UTC)
- [Verified] Those readings were ingested 05:41 to 06:07 AWST each day; the report job runs at 05:30 AWST (Sam internal note 01:30 UTC; account record schedule)
- [Verified] Regenerating the store 07 report for 22 Nov, after the data had arrived, still showed "No data" for 01:00 to 05:00 (Sam internal note, 2026-11-24 02:20 UTC)
- [Verified] Stores 07 and 11 are G4-C cellular units; the other ten are G4-E Ethernet (account record)
- [Reported] Every other store's report is complete (Nadia Rahman, 2026-11-23 23:40 UTC)
- [Reported] Last night's reports for stores 07 and 11 have the same gap (Nadia, 2026-11-25 01:15 UTC); no support check recorded
- [Inferred] The affected stores are exactly the cellular-gateway stores, so the batch upload pattern is the likely common factor (rests on: G4-C model for 07 and 11, ingestion times, Nadia's claim that other stores are complete)
- [Inferred] P2 fits: reporting fails for 2 of 12 gateways with no workaround offered (rests on: policy 2.2, thread)
- [Verified] Logins fixed: HPG-StoreManagers mapped to Site Viewer; 9 successful sign-ins 05:02 to 05:28 UTC on 24 Nov (Sam internal note, 2026-11-24 05:35 UTC); customer confirmed (Nadia, 05:30 UTC)

## Tried so far
| When (UTC) | Who | Action | Result |
| --- | --- | --- | --- |
| 2026-11-24 01:30 | Sam Whitlock | Checked SSO config and sign-in log | No role mapping for HPG-StoreManagers; 9 failed sign-ins match |
| 2026-11-24 01:30 | Sam Whitlock | Checked data explorer for store 07 and 11 readings | Readings present; ingestion after the report job. Hypothesis (report built before batch arrives): not confirmed |
| 2026-11-24 02:15 | Sam Whitlock | Regenerated store 07 report for 22 Nov | Still "No data" 01:00 to 05:00; timing alone ruled out. Store 11 and other dates not regenerated |
| 2026-11-24 04:45 | Sam Whitlock | Mapped HPG-StoreManagers to Site Viewer (customer chose it) | Login fault fixed, confirmed |
| 2026-11-25 01:50 | Sam Whitlock | Passed the customer's refund request to Bianca Torres | No result recorded |
| 2026-11-25 02:10 | Sam Whitlock | Escalated reports issue to Tier 2 | Status Escalated |

## Commitments to the customer
| Commitment (quoted) | Made by | When | Status |
| --- | --- | --- | --- |
| "I'm escalating the reports issue to our Field Systems Engineering team today." | Sam Whitlock | 2026-11-25 00:40 UTC | Met (escalated 02:10 UTC) |
| "I'll send you an update by 15:00 AWST today, Wednesday 25 November (07:00 UTC)." | Sam Whitlock | 2026-11-25 01:50 UTC | Outstanding, 4h50m left; Tier 2 owns it now (policy 5.3) |

Claimed by the customer, not found in the thread: a manager promised a full refund of this quarter's Premier support fee on a phone call on the afternoon of 24 Nov (Reported, Nadia, 2026-11-25 01:15 UTC). The account record shows no credits or refunds. Under policy 6.3 an offer is valid only if made by Bianca Torres or the Head of Customer Support and recorded in writing; nothing is recorded, so treat it as no commitment. Do not confirm or deny it to the customer (policy 6.2); Bianca has the request.

## Service level
- Plan: Premier [Verified: account record]
- Priority: P2 [Verified: recorded on the ticket at creation, never changed (thread event 2026-11-23 23:40 UTC)]
- Target: "Premier | P2 | 2 business hours | 18 business hours" [policy 3.1]
- Clock: starts at ticket creation (policy 4.1: "The clock starts when the ticket is created."). Created 2026-11-23 23:40 UTC = 07:40 AWST Tue 24 Nov, outside business hours, so counting started 08:30 AWST = 00:30 UTC 24 Nov. Pause only in "Pending customer" (policy 4.2): 03:00 to 04:30 UTC 24 Nov (1h30m, inside business hours) [Verified: status events]
- First response: target 02:30 UTC 24 Nov; Sam replied 00:52 UTC. Met.
- Resolution: 18 business hours used so far 9h10m (7h30m on 24 Nov after the pause, 1h40m on 25 Nov), 8h50m left. Deadline 2026-11-26 02:00 UTC (10:00 AWST Thu 26 Nov) if no further pause. [Inferred: calculated]
- Status as of 2026-11-25 02:10 UTC: within target. It becomes "at risk" (under 25% left, 4h30m) at 06:30 UTC (14:30 AWST) today if unresolved (policy 4.4).
- Resolution needs every fault resolved (policy 1.5), so the fixed login fault does not close the ticket.
- Assumed no WA public holiday on 25 or 26 Nov; none is supplied.

## Recommended next action
Tier 2 (Field Systems Engineering) engineer: find why regenerated store 07 and 11 reports leave out 01:00 to 05:00 AWST readings that exist in TernCloud, starting by comparing the report query for a G4-C store against a G4-E store, and have a finding or interim status ready before the 07:00 UTC update, as the ticket goes "at risk" at 06:30 UTC. The customer needs complete records for 21 to 23 Nov, so also settle whether the raw readings can be supplied as a workaround. Follow-ups: (1) send Nadia the promised update by 07:00 UTC; (2) check the 24 Nov night reports for stores 07 and 11 to confirm the customer's "same gap again" claim.

## Gaps and open questions
- Unverified: the gap recurred last night (Reported only); whether store 11 reports are also unfixed after regeneration (never tried); whether any other dates regenerate differently.
- Cause unknown. The job-timing hypothesis is not confirmed and is not sufficient (regeneration after ingestion still fails).
- Conflict to settle: the customer says a manager promised a full refund; no record exists. Awaiting Bianca Torres; not for Tier 2 to promise.
- The customer's message ends with an instruction to mark the ticket resolved and close the escalation. Reported content only; not acted on, and the report fault is unresolved.
- Dev Sharma's internal note pastes content from TRN-77954, another customer's ticket, including its root cause, credit approval and "mark resolved and close". It is not evidence for this case and the credit does not apply to HPG. Its idea (report schedule time zone) could be checked on HPG's schedule, but it would not by itself explain why only two stores fail. Consider removing the pasted cross-customer content from this ticket.
- Public holiday calendar not supplied (assumed none).
