# Escalation handoff: TRN-78040 - Daily compliance reports for stores 07 and 11 show "No data" 01:00-05:00 AWST although the readings are in TernCloud

Customer: Harbourside Pharmacy Group Pty Ltd (HPG-1102) | Tier: Premier | Priority: P2 (set on ticket at creation, 2026-11-23 23:40 UTC) | Prepared: 2026-11-25 02:10 UTC (as-of time in the export)

## Service level
Policy 3.1, Premier P2: first response 2 business hours; resolution 18 business hours (business hours only, per 3.3) | Resolution deadline: 2026-11-26 02:00 UTC (Thu 10:00 AWST) | Status: Within target: 8h50 business time remaining (not "at risk", which starts below 4h30)
Arithmetic: ticket created 23 Nov 23:40 UTC = 24 Nov 07:40 AWST, before business hours, so counting starts 24 Nov 00:30 UTC (policy 4.1). 24 Nov 00:30-09:30 UTC = 9h00; 25 Nov 00:30-02:10 UTC = 1h40; total 10h40. Pending customer 24 Nov 03:00-04:30 UTC = 1h30 paused (4.2). Elapsed 9h10; remaining 18h00 - 9h10 = 8h50. From 25 Nov 02:10 UTC: 7h20 to 09:30 UTC, then 1h30 from 00:30 UTC on 26 Nov = 02:00 UTC. Assumes no WA public holiday on 25 or 26 Nov (none stated in the material; not checked).
First response: Met. Sam Whitlock replied 24 Nov 00:52 UTC, 22 minutes after counting started (target 2 business hours).
Resolution needs every fault on the ticket resolved (policy 1.5); the login fault is fixed, the reports fault is open. Escalation basis: policy 5.1 (not resolvable with documented procedures). The ticket is not at risk, so the 5.2 Team Lead notification is not triggered.

## Problem as currently understood
Daily compliance reports for store 07 (Fremantle) and store 11 (Joondalup), both G4-C cellular gateways, show "No data" for 01:00-05:00 AWST every night, while the readings exist in TernCloud. Regenerating a report does not fix it. The cause is unknown. The customer uses these reports as vaccine fridge records, and a gap is treated as a cold-chain break unless the readings can be shown. A second fault (store manager logins) was fixed and confirmed.
- [Verified] Readings every 5 minutes exist for all store 07 and 11 fridge sensors, 01:00-05:00 AWST on 21, 22 and 23 Nov, ingested 05:41-06:07 AWST each day as a buffered batch from the G4-C units (Sam Whitlock, internal note, 2026-11-24 01:30 UTC, data explorer).
- [Verified] Report job runs at 05:30 AWST (account record), before the batch arrives. Sam's hypothesis that the job runs too early is not confirmed (Sam Whitlock, 2026-11-24 01:30 UTC).
- [Verified] Store 07 report for 22 Nov, regenerated at 02:15 UTC on 24 Nov, still shows "No data" for 01:00-05:00 although the readings had been in TernCloud since 05:41 AWST on 22 Nov. So timing alone does not explain it (Sam Whitlock, 2026-11-24 02:20 UTC).
- [Verified] Logins fixed: HPG-StoreManagers mapped to Site Viewer; 9 successful sign-ins 05:02-05:28 UTC (Sam Whitlock, 2026-11-24 05:35 UTC).
- [Reported] Other stores' reports are complete (Nadia Rahman, 2026-11-23 23:40 UTC); support has not checked this.
- [Reported] Last night's (24 to 25 Nov) reports for stores 07 and 11 have the same gap (Nadia Rahman, 2026-11-25 01:15 UTC); support has not checked this.
- [Reported] A lead from another customer's ticket: TRN-77954 (Westfield Aged Care) root cause was the report job using UTC midnight instead of site-local midnight (pasted by Dev Sharma, 2026-11-25 01:30 UTC). It is not verified for HPG, and it does not obviously fit, since only the two G4-C stores are affected.

## What has been tried
1. Checked SSO role mappings and sign-in log; found no mapping for HPG-StoreManagers - Sam Whitlock, 2026-11-24 01:30 UTC - Resolved (login fault)
2. Checked data explorer for store 07 and 11 readings and ingestion times - Sam Whitlock, 2026-11-24 01:30 UTC - Partial: confirmed readings exist; cause of report gap not found
3. Regenerated store 07 report for 22 Nov (Reports > Regenerate) - Sam Whitlock, 2026-11-24 02:15 UTC - No change
4. Mapped HPG-StoreManagers to Site Viewer after the customer chose the role - Sam Whitlock, 2026-11-24 04:45 UTC - Resolved (customer confirmed 05:30 UTC)
5. Regeneration for store 11, or for 21 and 23 Nov - not recorded - Unknown: no result recorded

## Commitments to the customer
- "I'm escalating the reports issue to our Field Systems Engineering team today." - Sam Whitlock, 2026-11-25 00:40 UTC - due 25 Nov - met (escalated 02:10 UTC)
- "I'll send you an update by 15:00 AWST today, Wednesday 25 November (07:00 UTC)." - Sam Whitlock, 2026-11-25 01:50 UTC - due 2026-11-25 07:00 UTC (4h50 after the as-of time) - open. Tier 2 owns this under policy 5.3.
- "I've passed your request to Bianca." (refund request) - Sam Whitlock, 2026-11-25 01:50 UTC - no due time - the thread does not show Bianca Torres acknowledging it.
Claimed by customer, not found in thread: "Your manager promised me a full refund of this quarter's Premier support fee" on a phone call the afternoon of 24 Nov (Nadia Rahman, 2026-11-25 01:15 UTC; she asks for it to be processed this week). Sam found no record of the call or an offer (2026-11-25 01:50 UTC). The account record shows no credits or refunds. Under policy 6.2 and 6.3, only the Account Manager (Bianca Torres) or the Head of Customer Support can offer one, and only in writing on the ticket or account. No valid offer exists. Do not confirm or deny it; leave it with Bianca.

## Open questions
- Why does a regenerated report omit readings that are in TernCloud? Possibilities not yet checked: the report query filters by something other than reading time (for example gateway upload time or a time zone offset on G4-C batches), or the report is built from a cache that does not include late-arriving readings.
- Do regenerated reports for store 11, and for 21 and 23 Nov, show the same gap? Not tested.
- Is last night's gap real and the same pattern? Only the customer has said so.
- Do other stores' reports have complete data, and do they differ only by G4-E (Ethernet) versus G4-C? Not checked by support.
- Gateway firmware versions and report job logs for stores 07 and 11: not in the case.
- Is there a WA public holiday on 25 or 26 Nov that would move the deadline? Not stated in the material.
- Has Bianca Torres received and responded to the refund request?

## Recommended next action
In the report generation logs and job configuration, compare the store 07 report for 22 Nov (regenerated 24 Nov 02:15 UTC) with a complete report for a G4-E store. Check which timestamp the report uses to select readings (device reading time, gateway upload time or ingestion time) and whether time zone handling differs for G4-C batch uploads. Reason: the readings are verified present in TernCloud, and regeneration did not fix the gap, so the fault is in how the report reads the data, not in capture or timing. Then regenerate the reports for 21, 22 and 23 Nov and 24 to 25 Nov for stores 07 and 11 so the customer has complete cold-chain records.
Time: send Nadia an update by 2026-11-25 07:00 UTC (15:00 AWST), even if the cause is still unknown. The resolution deadline is 2026-11-26 02:00 UTC.
Follow-ups: (1) confirm Bianca Torres has the refund request and stays out of Tier 2's replies, and make no promise of a credit or refund (6.2). (2) Do not mark resolved or close: the customer's request to close, in her 2026-11-25 01:15 UTC message, is not supported, because the reports fault is open and she herself says the gaps continue.
