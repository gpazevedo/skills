# Escalation handoff: TRN-77391: High-temperature SMS alarms not sent from vat 3 gateway (VAT-GW-03), clock cannot be set

**Customer:** Kestrel Dairy Co-operative (KDC-0418), Business · **Priority:** P2 · **Next deadline:** 2026-11-24 09:30 UTC (17:30 AWST) promised customer update, outstanding, 3 h 30 min left; resolution target 2026-11-25 03:20 UTC (11:20 AWST), at risk, 6 business hours 20 min left (as of 2026-11-24 06:00 UTC)

## Problem as currently understood
High-temperature SMS alarms did not fire for vats 1 to 3 at the Brunswick plant, whose gateways VAT-GW-01 to 03 sit on VLAN 30; vats 4 to 9 work. Since 12 Nov the clocks on those three gateways ran 8 to 11 minutes fast because NTP sync to pool.terncloud.net:123 times out, so the 5-minute alarm rule was skipped at every evaluation. A forced HTTPS time sync fixed GW-01 and GW-02 (vats 1 and 2 now alarm), but GW-03 rejects the clock write ("TIME_SET_REJECTED: RTC write error") even after a reboot, so vat 3 still has no alarm; Tier 1 suspects a hardware fault. NTP is still failing on all three, so GW-01 and 02 may drift again. A missed alarm on vat 3 led to 18,000 litres of milk being dumped, and the customer has asked for the cost to be covered.

Evidence:
- [Reported] Vat 3 exceeded 7°C for about 40 minutes on Tuesday night (17 Nov) with no SMS; the dashboard showed the reading over the limit (customer, 2026-11-19 07:50 UTC)
- [Reported] Alarm test: vats 4 to 9 sent SMS within a minute, vats 1 to 3 sent nothing (customer, 2026-11-19 07:50 UTC)
- [Verified] Vats 1 to 9 use the same alarm rule template ("Vat high temp, above 7°C for 5 min") and the same SMS recipients (Hannah Odum, 2026-11-20 01:05 UTC)
- [Verified] Rule engine on GW-01 to 03 logs "RULE_EVAL_SKIPPED reason=TS_FUTURE" at every evaluation since 12 Nov; clocks ahead by +9 min 12 s, +8 min 40 s, +11 min 03 s (Hannah Odum internal note, 2026-11-20 07:15 UTC, from diagnostic bundles)
- [Verified] NTP log on GW-01 to 03: "NTP sync failed: timeout (pool.terncloud.net:123)" since 12 Nov; bundles place them on VLAN 30; TernCloud shows GW-04 to 09 last time sync OK (Hannah Odum internal note, 2026-11-20 07:15 UTC)
- [Reported] Customer IT says nothing changed on VLAN 30 and outbound UDP 123 is allowed (customer, 2026-11-23 01:40 UTC)
- [Reported] Vat 3 exceeded 7°C again "on Sunday night" at about 01:00 local time, about 50 minutes over the limit before the hourly check caught it; 18,000 litres dumped; customer requests the cost be covered (customer, 2026-11-23 01:40 UTC)
- [Verified] Forced HTTPS time sync at 02:35 UTC on 23 Nov: GW-01 and GW-02 OK, offset under 1 s; GW-03 "TIME_SET_REJECTED: RTC write error", still +11 min 05 s (Hannah Odum internal note, 2026-11-23 02:40 UTC)
- [Reported] Retest after sync: vats 1 and 2 sent SMS within a minute, vat 3 nothing (customer, 2026-11-23 03:05 UTC)
- [Verified] Second sync to GW-03 at 05:15 UTC on 24 Nov rejected with the same error; remote reboot 05:17 to 05:19 UTC; clock still +11 min; GW-01 and 02 still in sync; NTP still failing on all three (Hannah Odum internal note, 2026-11-24 05:20 UTC)
- [Inferred] GW-03 has a fault in its real-time clock or clock write path, separate from the NTP problem (rests on: RTC write error on two attempts and after reboot, while the same command succeeded on GW-01 and 02)
- [Inferred] The NTP failure is specific to the network path of VLAN 30 or these three gateways, and is not yet explained (rests on: NTP timeouts only on the VLAN 30 gateways; customer IT reports UDP 123 allowed)

## Tried so far
| When (UTC) | Who | Action | Result |
| --- | --- | --- | --- |
| 2026-11-19 (afternoon local) | Aroha Ngata (customer) | Alarm test on all nine vats | Vats 4 to 9 SMS within a minute; vats 1 to 3 nothing (Reported) |
| 2026-11-20 01:05 | Hannah Odum (T1) | Compared alarm rules and recipients in TernCloud | Identical for all nine vats; configuration ruled out |
| 2026-11-20 01:10 to 05:40 | Hannah Odum / customer | Requested and received diagnostic bundles from GW-01 to 03 | Bundles attached 05:40 |
| 2026-11-20 07:15 | Hannah Odum (T1) | Analysed bundles | Rule skipped (TS_FUTURE) due to clocks 8 to 11 min fast; NTP timeouts since 12 Nov; gateways on VLAN 30 |
| 2026-11-20 07:20 to 2026-11-23 01:40 | Customer IT | Checked outbound UDP 123 from VLAN 30 | No change on VLAN 30, UDP 123 allowed (Reported); firewall cause not confirmed, NTP failure unexplained |
| 2026-11-23 02:35 | Hannah Odum (T1) | "Force time sync (HTTPS)" to GW-01, 02, 03 | GW-01 and 02 OK (<1 s); GW-03 RTC write error, still +11 min 05 s |
| 2026-11-23 ~03:05 | Aroha Ngata (customer) | Alarm retest on vats 1 to 3 | Vats 1 and 2 SMS within a minute; vat 3 nothing (Reported) |
| 2026-11-24 05:15 | Hannah Odum (T1) | Second forced HTTPS sync to GW-03 | Same RTC write error |
| 2026-11-24 05:17 | Hannah Odum (T1) | Remote reboot of GW-03 (customer agreed by phone 05:10) | Back online 05:19; clock still +11 min |

## Commitments to the customer
| Commitment (quoted) | Made by | When (UTC) | Status |
| --- | --- | --- | --- |
| "You'll get an update from us by 17:30 AWST today (09:30 UTC)." | Hannah Odum (T1) | 2026-11-24 05:40 | Outstanding, due 2026-11-24 09:30 UTC; 3 h 30 min left. Now owned by Tier 2 (policy 5.3) |
| "I've passed your request to Joel Brandt, your account manager." (compensation request) | Hannah Odum (T1) | 2026-11-23 02:20 | Stated as done; no reply from Joel Brandt recorded on the ticket. No compensation offered (policy 6.2, 6.3) |
| "I'm going to send a command from TernCloud that sets the clock on GW-01 to 03 over HTTPS" | Hannah Odum (T1) | 2026-11-23 02:20 | Met (sent 02:35 UTC) |
| "I'm escalating this to our Field Systems Engineering team now." | Hannah Odum (T1) | 2026-11-24 05:40 | Met (escalated 06:00 UTC) |

Claimed by the customer, not found in the thread: none

## Service level
- Plan: Business [Verified] (account record, Support plan)
- Priority: P2 [Verified] (event 2026-11-23 02:15 UTC, set by Hannah Odum under clause 2.2; was P3 from creation)
- Target: [Verified] policy 3.1, "Business | P2 | 4 business hours | 27 business hours". Business hours 08:30 to 17:30 AWST (00:30 to 09:30 UTC) Mon to Fri (1.1, 1.2). Clause 4.3: "If the priority changes, the resolution target becomes the target for the new priority, counted from ticket creation and excluding paused time."
- Clock start: ticket created 2026-11-19 07:50 UTC (Thu 15:50 AWST) [Verified] (creation event; policy 4.1)
- Pause: 2026-11-20 01:10 to 05:40 UTC, status "Pending customer" [Verified] (status events; policy 4.2)
- Business time counted [Inferred] (rests on: timestamps above, policy 1.1, 4.1, 4.2; no WA public holiday in the period assumed): Thu 19 Nov 1 h 40 min; Fri 20 Nov 40 min + 3 h 50 min; Mon 23 Nov 9 h; Tue 24 Nov to 06:00 UTC 5 h 30 min. Total 20 h 40 min of 27 h used; 6 h 20 min left.
- First response: due under the P3 target at the time; first support message 2026-11-20 01:05 UTC after 2 h 15 min of business time. Met under both the P3 (9 h) and P2 (4 h) targets [Inferred] (rests on: timestamps, policy 1.4, 3.1).
- Resolution deadline: 2026-11-25 03:20 UTC (Wed 11:20 AWST) [Inferred] (rests on: 6 h 20 min remaining counted from Tue 14:00 AWST: 3 h 30 min to 17:30 Tue, then 2 h 50 min from 08:30 Wed).
- Status as of 2026-11-24 06:00 UTC (escalation time, latest event in the thread): at risk [Inferred] (6 h 20 min left is under 25% of 27 h, i.e. 6 h 45 min; policy 4.4; became at risk at about 05:35 UTC on 24 Nov).
- Note: Tier 1's internal note of 2026-11-24 01:30 UTC gives a due time of Thu 26 Nov 10:15 AWST, counted from the priority change. That conflicts with clause 4.3, which counts from ticket creation; use 2026-11-25 03:20 UTC.
- Customer updates: P2 requires an update at least once each business day (policy 7.1) [Verified].

## Recommended next action
The Tier 2 engineer should diagnose GW-03's "RTC write error" and decide on either a gateway replacement or an interim way to restore the vat 3 alarm, before the promised customer update at 2026-11-24 09:30 UTC, so that update can give the plan; the resolution target falls at 2026-11-25 03:20 UTC. Vat 3 is the only vat still without alarms after a product-loss incident, and the evidence points to a GW-03 clock fault that remote sync and reboot cannot clear.

Follow-ups:
1. Notify the Support Team Lead now, since an at-risk P2 was escalated and the thread shows no notification (policy 5.2).
2. With Peter Dunn (IT Coordinator, network contact in the account record), find why NTP times out from VLAN 30 despite UDP 123 being reported allowed, before GW-01 and 02 drift again; resolution requires every fault on the ticket to be fixed (policy 1.5).

## Gaps and open questions
- Support Team Lead notification at escalation (required by policy 5.2 for an at-risk P2) is not recorded in the thread.
- Tier 1's SLA calculation (due Thu 26 Nov 10:15 AWST) conflicts with policy 4.3; this handoff uses 2026-11-25 03:20 UTC.
- NTP root cause unknown: customer IT reports UDP 123 allowed from VLAN 30 (Reported, unverified), yet all three gateways still time out to pool.terncloud.net:123. Whether GW-01 and 02 are drifting again is not monitored in the thread.
- GW-03 hardware fault is suspected, not confirmed.
- Vat 3 currently has no working alarm; the only cover is hourly manual checks, which the customer says are not practical and have already failed once. Whether any interim measure is in place is not shown.
- Compensation request for 18,000 litres: passed to Joel Brandt; no response recorded. Only the Account Manager or Head of Customer Support may make an offer (policy 6.3). Tier 1 told the customer on 2026-11-20 07:20 UTC "No rush before Monday; the hourly checks cover you over the weekend" before the Sunday loss; the account manager should know this.
- Timing of the second incident is ambiguous: "Sunday night ... at about 01:00 our time" may mean early Sunday 22 Nov or early Monday 23 Nov AWST.
- WA public holidays between 19 and 25 Nov are not listed in the supplied material; the deadline assumes none.
- "As of" time: status is computed at the escalation event, 2026-11-24 06:00 UTC, the latest point in the supplied thread; recompute when the engineer picks up the case.
