# Escalation handoff: TRN-77391: High-temperature SMS alarms not firing on VAT-GW-01 to 03 (vat 3 still failing, gateway clock stuck fast)

**Customer:** Kestrel Dairy Co-operative (KDC-0418), Business · **Priority:** P2 · **Next deadline:** 2026-11-24 09:30 UTC (17:30 AWST), customer update promised, outstanding, 3h30m left (as of 2026-11-24 06:00 UTC). Resolution deadline: 2026-11-25 03:20 UTC (11:20 AWST), AT RISK.

## Problem as currently understood
High-temperature SMS alarms do not fire for vats 1 to 3 at the Brunswick plant. The leading explanation is that the gateway clocks run 8 to 11 minutes ahead of sensor timestamps because NTP has failed since 12 Nov, so the 5-minute rule window never fills and the rule is skipped. Time was forced via HTTPS on GW-01 and GW-02, and their alarms now work. GW-03 rejects the time set (RTC write error) even after a reboot, so vat 3 has no working alarm. The customer lost 18,000 litres of milk on the second missed event.

Evidence:
- [Verified] GW-01, 02 and 03 log "RULE_EVAL_SKIPPED reason=TS_FUTURE" at every evaluation since 12 Nov (Hannah Odum internal note, 2026-11-20 07:15 UTC)
- [Verified] Clock offsets in the bundles: GW-01 +9m12s, GW-02 +8m40s, GW-03 +11m03s; NTP log "sync failed: timeout (pool.terncloud.net:123)" since 12 Nov (Odum, 2026-11-20 07:15)
- [Verified] Vats 1 to 9 use the same rule template and SMS recipients (Odum, 2026-11-20 01:05); GW-04 to 09 show last time sync OK in TernCloud (Odum, 2026-11-20 07:15)
- [Verified] GW-01 and GW-02 offsets under 1 s after HTTPS time set at 02:35 UTC on 23 Nov (Odum internal note, 2026-11-23 02:40; reconfirmed 2026-11-24 05:20)
- [Verified] GW-03 returned "TIME_SET_REJECTED: RTC write error" on 23 Nov 02:35 and again 24 Nov 05:15; reboot at 05:17 did not fix it, clock still about +11 min (Odum, 2026-11-24 05:20)
- [Verified] NTP is still failing on GW-01 to 03, so GW-01 and 02 may drift again (Odum, 2026-11-24 05:20)
- [Reported] Vat 3 exceeded 7°C for about 40 min on Tuesday night (17 Nov) with no SMS; the dashboard showed the reading (Ngata, 2026-11-19 07:50)
- [Reported] Alarm test 19 Nov: vats 4 to 9 sent SMS, vats 1 to 3 did not (Ngata, 2026-11-19 07:50)
- [Reported] Vat 3 exceeded 7°C again about 01:00 AWST on Sunday night/Monday morning, no SMS, about 50 min over limit before an hourly check caught it; 18,000 L dumped (Ngata, 2026-11-23 01:40)
- [Reported] Customer IT says nothing changed on VLAN 30 and outbound UDP 123 is allowed (Ngata, 2026-11-23 01:40). This conflicts with the NTP timeouts and the VLAN-30 theory; not tested by support
- [Reported] After the HTTPS time set, vats 1 and 2 alarm test sent SMS; vat 3 did not (Ngata, 2026-11-23 03:05)
- [Inferred] GW-03 may have a hardware (RTC) fault (rests on: repeated RTC write error, reboot no effect; Odum said "may be a hardware fault", not confirmed)
- [Inferred] Root cause of the NTP failure is unknown. UDP 123 blocked on VLAN 30 is Odum's unconfirmed hypothesis and the customer denies it (rests on: NTP timeouts, GW-01 to 03 on VLAN 30, GW-04 to 09 syncing; the VLAN of GW-04 to 09 is not stated)

## Tried so far
| When (UTC) | Who | Action | Result |
| --- | --- | --- | --- |
| 2026-11-20 01:05 | Odum | Compared TernCloud alarm rules for vats 1 to 9 | Identical template and recipients; configuration ruled out |
| 2026-11-20 01:10 | Odum | Asked customer for diagnostic bundles from GW-01 to 03 (status Pending customer 01:10 to 05:40) | Bundles received 05:40; showed TS_FUTURE skips and NTP timeouts |
| 2026-11-20 07:20 | Odum | Asked customer IT to check outbound UDP 123 from VLAN 30 | Customer IT reports it is allowed (2026-11-23 01:40, Reported); not independently checked |
| 2026-11-23 02:35 | Odum | "Force time sync (HTTPS)" to GW-01, 02, 03 | GW-01 and 02 OK (offset under 1 s); GW-03 RTC write error |
| 2026-11-23 03:05 | Customer | Alarm test on vats 1 to 3 | Vats 1 and 2 sent SMS; vat 3 nothing (Reported) |
| 2026-11-24 05:15 | Odum | Second HTTPS time sync to GW-03 | Same RTC write error |
| 2026-11-24 05:17 | Odum | Remote reboot of GW-03 (customer agreed by phone 05:10) | Back online 05:19; clock still +11 min |
| 2026-11-24 06:00 | Odum | Escalated to Tier 2 | Status Escalated, P2 |

## Commitments to the customer
| Commitment (quoted) | Made by | When | Status |
| --- | --- | --- | --- |
| "You'll get an update from us by 17:30 AWST today (09:30 UTC)." | Hannah Odum | 2026-11-24 05:40 UTC | Outstanding, 3h30m left; due 2026-11-24 09:30 UTC. Tier 2 now owns it (policy 5.3) |
| "I've passed your request to Joel Brandt, your account manager." (the milk compensation request) | Hannah Odum | 2026-11-23 02:20 UTC | Action reported done; no reply, offer or note from Joel Brandt in the thread or account record. No credit or compensation has been promised (open credits: none) |
Claimed by the customer, not found in the thread: none. The customer has asked for the cost of the milk to be covered; no one has agreed.

## Service level
- Plan: Business (Verified, account record). Priority: P2 (Verified, set by Odum 2026-11-23 02:15 UTC; P3 before). Fits policy 2.2 (alarms fail for some gateways, no practical workaround); not P1 since fewer than half of 11 gateways are offline.
- Targets (policy 3.1): Business P2, first response "4 business hours", resolution "27 business hours". Clause 4.3: after a priority change the resolution target is the new one "counted from ticket creation and excluding paused time".
- Clock start: ticket creation, 2026-11-19 07:50 UTC (Thu 15:50 AWST), clause 4.1. Business hours 00:30 to 09:30 UTC, Mon to Fri. Pause only while "Pending customer": 2026-11-20 01:10 to 05:40 UTC (4.5 h, all inside business hours, clause 4.2). No public holidays assumed in the period (none known; not stated in the inputs).
- First response: met. First contact by Odum 2026-11-20 01:05 UTC, 2h15m of business time after creation, within 4 business hours.
- Resolution business hours used: Thu 1h40 + Fri 4h30 (9h minus 4h30 pause) + Mon 9h + Tue 5h30 (to 06:00 UTC) = 20h40m. Remaining 6h20m.
- Resolution deadline: 2026-11-25 03:20 UTC (Wed 11:20 AWST). Status: open, AT RISK (clause 4.4: 6h20m is below 25% of 27 h = 6h45m; the threshold was crossed at about 05:35 UTC today). It becomes breached at the deadline if unresolved.
- Note: Odum's internal note of 2026-11-24 01:30 UTC gives "Thu 26 Nov 10:15 AWST" and "plenty of time". That is wrong: it counts from the priority change and ignores that 4.3 counts from creation. Use the deadline above.
- Policy 5.2: an at-risk P2 escalation requires notifying the Support Team Lead at escalation. The thread records no such notification.
- Update cadence (policy 7.1, P2): at least once each business day; the 09:30 UTC update promised today satisfies it.

## Recommended next action
Tier 2 (Field Systems Engineering) should take the case now and, before the 09:30 UTC update, decide how vat 3 gets a working alarm (replace or repair GW-03, or another interim alarm path) and put that plan, with times, in the customer update. GW-03 is the one gateway with no working alarm, the customer is relying on hourly manual checks, and the resolution deadline is under 21 hours away.
Follow-ups: (1) notify the Support Team Lead today and record it on the ticket (policy 5.2); (2) find the real cause of the NTP timeouts with Peter Dunn (the customer says UDP 123 is open), since GW-01 and 02 may drift and fail again.

## Gaps and open questions
- No inputs missing.
- Whether GW-03 has a hardware fault is unconfirmed.
- The NTP cause is unconfirmed and the customer's statement conflicts with it. The VLAN of GW-04 to 09 is not stated, so the "VLAN 30" explanation is untested.
- Support Team Lead notification (5.2) is not recorded.
- The compensation request is with Joel Brandt (only he or the Head of Customer Support can offer credit, policy 6.3); no response is recorded. Support agents and Tier 2 must not promise compensation (6.2).
- Time of the Sunday-night event is given only as "about 01:00 our time"; exact date and time not stated.
- Public holidays are assumed to be none between 19 and 25 Nov.
