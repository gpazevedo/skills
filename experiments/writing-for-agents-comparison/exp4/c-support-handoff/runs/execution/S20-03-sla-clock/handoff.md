# Escalation handoff: TRN-77391 High-temperature SMS alarms not received from vat gateways (GW-03 clock cannot be set)

**Customer:** Kestrel Dairy Co-operative (KDC-0418), Business plan | **Priority:** P2 (set by Hannah Odum, Tier 1, 2026-11-23 02:15 UTC; was P3 at creation)
**Service level:** At risk (resolution), next deadline 2026-11-24 09:30 UTC, the customer update (3h30 remaining at 06:00 UTC); resolution deadline 2026-11-25 03:20 UTC (21h20 of calendar time away, 6h20 of business hours remaining)
**Open commitments:** 1, earliest due 2026-11-24 09:30 UTC (17:30 AWST)

## Problem as currently understood
Vat high-temperature SMS alarms did not fire for VAT-GW-01, 02 and 03 (Brunswick, VLAN 30). Verified from the diagnostic bundles: those three gateways' clocks run 8 to 11 minutes ahead and their rule engine logs RULE_EVAL_SKIPPED (TS_FUTURE), while NTP sync fails with a timeout on all three. Setting the clock over HTTPS fixed GW-01 and GW-02 (customer reports their alarm tests now pass), but GW-03 rejected the time set twice with "RTC write error" and a reboot did not help; the customer reports vat 3 still sends nothing. Hannah's hypotheses are that UDP 123 is blocked on VLAN 30 (the customer's IT says it is allowed) and that GW-03 may have a hardware fault. The customer reports a missed vat 3 alarm on Sunday night that led to 18,000 litres of milk being dumped, and has asked for the cost to be covered.

| Fact | Tag | Source |
|---|---|---|
| Vat 3 went above 7°C for about 40 min on Tuesday night with no SMS; dashboard shows the reading | Reported | Aroha Ngata, 2026-11-19 07:50 |
| In the customer's all-vat alarm test, vats 4 to 9 sent SMS within a minute; vats 1, 2, 3 sent nothing | Reported | Aroha Ngata, 2026-11-19 07:50 |
| Vats 1 to 9 use the same rule template ("Vat high temp, above 7°C for 5 min") and same SMS recipients | Verified (Hannah Odum read the TernCloud rules) | Hannah Odum, 2026-11-20 01:05 |
| GW-01, 02, 03 log "RULE_EVAL_SKIPPED reason=TS_FUTURE" at every evaluation since 12 Nov | Verified (Hannah Odum, from diagnostic bundles) | Internal note, 2026-11-20 07:15 |
| Clock offsets: GW-01 +9 min 12 s, GW-02 +8 min 40 s, GW-03 +11 min 03 s | Verified (Hannah Odum, bundles) | Internal note, 2026-11-20 07:15 |
| NTP log on all three: "NTP sync failed: timeout (pool.terncloud.net:123)" since 12 Nov | Verified (Hannah Odum, bundles) | Internal note, 2026-11-20 07:15 |
| GW-01 to 03 are on VLAN 30 (per bundles); TernCloud shows GW-04 to 09 last time sync OK | Verified (Hannah Odum, bundles and TernCloud) | Internal note, 2026-11-20 07:15 |
| The clock skew stops the 5-minute window filling, so the rule is skipped | Hypothesis (Hannah Odum's reading of the log; no test isolates it) | Internal note, 2026-11-20 07:15 |
| UDP 123 is blocked for VLAN 30 | Hypothesis (Hannah Odum, "Not confirmed"); contradicted by the customer's IT report below | Internal note, 2026-11-20 07:15 |
| Customer IT says nothing changed on VLAN 30 and outbound UDP 123 is allowed | Reported (relayed by Aroha Ngata from IT) | Aroha Ngata, 2026-11-23 01:40 |
| Vat 3 went over 7°C again on Sunday night (about 01:00 customer time), no SMS, about 50 min over limit, 18,000 L dumped | Reported | Aroha Ngata, 2026-11-23 01:40 |
| "Force time sync (HTTPS)" at 02:35: GW-01 and GW-02 OK, offset under 1 s | Verified (Hannah Odum, result in TernCloud) | Internal note, 2026-11-23 02:40 |
| Same command to GW-03: "TIME_SET_REJECTED: RTC write error", clock still +11 min 05 s | Verified (Hannah Odum) | Internal note, 2026-11-23 02:40 |
| After the alarm test, vats 1 and 2 sent SMS within a minute; vat 3 nothing | Reported | Aroha Ngata, 2026-11-23 03:05 |
| Second force time sync to GW-03 at 05:15 gave the same RTC write error; reboot at 05:17, back online 05:19, clock still +11 min | Verified (Hannah Odum) | Internal note, 2026-11-24 05:20 |
| GW-01 and GW-02 still within 1 s, but NTP still failing on all three | Verified (Hannah Odum) | Internal note, 2026-11-24 05:20 |
| GW-01 and GW-02 may drift again | Hypothesis (Hannah Odum) | Internal note, 2026-11-24 05:20 |
| GW-03 may have a hardware fault | Hypothesis (Hannah Odum) | Hannah Odum, 2026-11-24 05:40 |
| Night staff are checking the dashboard hourly as an interim measure | Reported | Aroha Ngata, 2026-11-19 07:50 |

**Open questions:**
- Why does NTP time out if UDP 123 is allowed (DNS for pool.terncloud.net, firewall path, or another cause)? The thread has no network-side evidence, only the customer's IT statement.
- Is the RTC write error on GW-03 a hardware fault, and does GW-03 need repair or replacement?
- Was the Sunday miss on vat 3 caused by the same GW-03 clock fault? The thread does not record GW-03's offset or rule log at that time.
- Will GW-01 and GW-02 stay in sync while NTP keeps failing?
- What interim cover exists for vat 3? Hourly checks have already failed once, per the customer.

## What has been tried
| Action | By | When | Result |
|---|---|---|---|
| Checked TernCloud alarm rules for vats 1 to 9 | Hannah Odum | 2026-11-20 01:05 | Same template and recipients, so config does not explain it |
| Requested diagnostic bundles from GW-01, 02, 03 | Hannah Odum | 2026-11-20 01:10 | Customer supplied all three at 05:40 |
| Analysed bundles | Hannah Odum | 2026-11-20 07:15 | Clock skew, RULE_EVAL_SKIPPED, NTP timeouts (see facts) |
| Asked customer IT to check outbound UDP 123 from VLAN 30 | Hannah Odum (request), customer IT | 2026-11-20 07:20 | IT reports allowed and nothing changed (Reported) |
| Force time sync (HTTPS) to GW-01, 02, 03 | Hannah Odum | 2026-11-23 02:35 | GW-01, 02 OK; GW-03 RTC write error |
| Customer alarm test on vats 1 to 3 | Aroha Ngata | 2026-11-23 03:05 | Vats 1, 2 sent SMS; vat 3 did not (Reported) |
| Second force time sync to GW-03 | Hannah Odum | 2026-11-24 05:15 | Same RTC write error |
| Remote reboot of GW-03 (customer agreed by phone at 05:10) | Hannah Odum | 2026-11-24 05:17 | Back online 05:19; clock still +11 min. Alarm test on vat 3 after the reboot: result not recorded |
| Passed compensation request to Joel Brandt | Hannah Odum | 2026-11-23 02:20 | Result not recorded |
| Escalated to Tier 2 | Hannah Odum | 2026-11-24 06:00 | Status Escalated, P2 |

## Commitments to the customer
| Commitment (quoted) | Made by | When | Status |
|---|---|---|---|
| "I've passed your request to Joel Brandt, your account manager." (commitment is to pass it on, not to any credit) | Hannah Odum | 2026-11-23 02:20 | Met as stated; no acknowledgement or decision from Joel Brandt is recorded |
| "I'm going to send a command from TernCloud that sets the clock on GW-01 to 03 over HTTPS" | Hannah Odum | 2026-11-23 02:20 | Met (sent 02:35, internal note 02:40) |
| "I'm escalating this to our Field Systems Engineering team now." | Hannah Odum | 2026-11-24 05:40 | Met (escalated 06:00) |
| "You'll get an update from us by 17:30 AWST today (09:30 UTC)." | Hannah Odum | 2026-11-24 05:40 | Open, due 2026-11-24 09:30 UTC; Tier 2 now owns it (policy 5.3) |

**Requested, not committed:** Customer's request that the cost of the dumped milk (18,000 L) be covered (Aroha Ngata, 2026-11-23 01:40). Hannah said "I'm not able to offer compensation myself". Policy 6.3: only the Account Manager (Joel Brandt) or the Head of Customer Support may offer it, in writing on the ticket or account record; nothing is recorded. Also, the customer's statement that hourly checks are not sustainable has no agreed response.

## Service level
Measured at 2026-11-24 06:00 UTC (the as-of time of the export; 14:00 AWST Tuesday). Readings used for ambiguous terms:
- Business hours are 00:30 to 09:30 UTC Monday to Friday (policy 1.2). No WA public holiday falls in the period; none is mentioned in the inputs.
- Priority change P3 to P2: policy 4.3 quoted below says the resolution clock counts from ticket creation, so I used creation (2026-11-19 07:50 UTC), not the priority change. Policy 4.3 speaks only of the resolution target; the first-response result below is the same under P2 or P3.
- Business-hours counting for 2026-11-19 starts at creation (07:50 is inside business hours).

| Target (policy quote) | Clock start | Deadline (arithmetic) | Status |
|---|---|---|---|
| Resolution, Business P2: "27 business hours" (3.1); P3 would have been "72 business hours"; 4.3: "the resolution target becomes the target for the new priority, counted from ticket creation and excluding paused time" | Ticket creation, Thu 2026-11-19 07:50 UTC (4.1) | Business time used by 06:00 on 24 Nov: Thu 07:50 to 09:30 = 1h40; Fri 00:30 to 01:10 = 0h40 and 05:40 to 09:30 = 3h50 (01:10 to 05:40 paused); Sat, Sun = 0; Mon 00:30 to 09:30 = 9h00; Tue 00:30 to 06:00 = 5h30. Total 20h40. Remaining 27h00 - 20h40 = 6h20, which runs out 3h30 on Tuesday (to 09:30) plus 2h50 on Wednesday from 00:30 = Wed 2026-11-25 03:20 UTC (11:20 AWST) | At risk: 4.4 "less than 25% of its resolution target remains" and 25% of 27h = 6h45; 6h20 is less than 6h45. Not breached |
| First response, Business P2: "4 business hours" (3.1); P3 "9 business hours" | Ticket creation, 2026-11-19 07:50 UTC | First response 2026-11-20 01:05 UTC. Elapsed: Thu 1h40 + Fri 00:30 to 01:05 = 0h35, total 2h15 | Met under both P2 (4h) and P3 (9h) |
| Customer updates, P2: "at least once each business day" (7.1) | P2 recorded 2026-11-23 02:15 UTC | Updates sent Mon 23 Nov 02:20 and Tue 24 Nov 05:40 UTC. Next due by end of business day Wed 2026-11-25 09:30 UTC | Within target; separate open update commitment due 2026-11-24 09:30 UTC |

Pauses: "The clock is paused only while the ticket status is 'Pending customer'" (4.2). One pause in the thread: Pending customer 2026-11-20 01:10 to 05:40 UTC (4h30, all inside business hours).

Note: Hannah's internal note of 2026-11-24 01:30 UTC counts 27 business hours from the priority change (Mon 10:15 AWST), giving Thu 26 Nov 10:15 AWST, and says "Plenty of time". That contradicts policy 4.3. Under creation-based counting the deadline is Wed 25 Nov 11:20 AWST and the ticket is at risk.

Escalation rules: policy 5.1 allows Tier 2 escalation when a P2 is at risk, and 5.2 says "the Support Team Lead must be notified at escalation" for an at-risk P2. The thread records no Team Lead notification. Policy 5.3: Tier 2 owns the ticket including customer updates and commitments already made. The Business plan has no first-response or update terms beyond the above; Policy does not state any rule on how a stopped RTC fault should be classed.

## Recommended next action
This is my own recommendation. Tier 2 Field Systems Engineering to decide the GW-03 route (RTC fault confirmation and a hardware repair or replacement, or another way to give vat 3 working alarms), and send the customer the committed update by 2026-11-24 09:30 UTC without promising a fix date or any credit (policy 6.2), owner Tier 2 Field Systems Engineering (on-call engineer), by 2026-11-24 09:30 UTC, because the update commitment is due then and the resolution target runs out about 2026-11-25 03:20 UTC with the fix path still unknown. In the same step: notify the Support Team Lead (policy 5.2, at-risk P2, no notification recorded), confirm with Joel Brandt that the compensation request was received and who answers the customer (6.3), and ask the customer whether vat 3 now has interim cover beyond hourly checks.
