# Escalation handoff: TRN-77391 High-temperature SMS alarms not firing from vat gateways VAT-GW-01 to 03 (GW-03 still failing)

**Customer:** Kestrel Dairy Co-operative (KDC-0418), Business support plan, TernCloud Site subscription (account record: Support plan, TernCloud subscription)
**Earliest deadline:** 2026-11-24 09:30 UTC (17:30 AWST): customer update promised by Hannah Odum, now owned by Tier 2 (thread 2026-11-24 05:40 UTC; policy 5.3). Resolution target falls due 2026-11-25 03:20 UTC (11:20 AWST) and the ticket is already "at risk" (policy 4.4).

## Problem as currently understood
The alarm rule on VAT-GW-01, 02 and 03 is skipped at every evaluation because each gateway's clock runs 8 to 11 minutes fast after NTP sync to pool.terncloud.net:123 began timing out on 12 Nov. A forced HTTPS time sync fixed the clocks on GW-01 and GW-02, but GW-03 rejects any clock write with an RTC write error, even after a reboot, so vat 3 still has no working high-temperature alarm. Open hypotheses: a hardware fault in GW-03, and UDP 123 being blocked for VLAN 30 (the customer's IT says it is not). Because NTP still fails on all three gateways, GW-01 and 02 may drift again.

### Verified
- Alarm rules for vats 1 to 9 use the same template ("Vat high temp, above 7°C for 5 min") and the same SMS recipients, so configuration does not explain the difference (Hannah Odum, 2026-11-20 01:05 UTC)
- Rule engine on GW-01, 02 and 03 logs "RULE_EVAL_SKIPPED reason=TS_FUTURE" at every evaluation since 12 Nov (internal note, Hannah Odum, 2026-11-20 07:15 UTC)
- Gateway clocks ahead of sensor timestamps: GW-01 +9 min 12 s, GW-02 +8 min 40 s, GW-03 +11 min 03 s (internal note, 2026-11-20 07:15 UTC)
- NTP log on all three: "NTP sync failed: timeout (pool.terncloud.net:123)", repeated since 12 Nov (internal note, 2026-11-20 07:15 UTC)
- Bundles place GW-01 to 03 on VLAN 30; TernCloud shows GW-04 to 09 with last time sync OK (internal note, 2026-11-20 07:15 UTC)
- Force time sync (HTTPS) at 02:35: GW-01 and GW-02 OK, offset under 1 s; GW-03 "TIME_SET_REJECTED: RTC write error", clock still +11 min 05 s (internal note, 2026-11-23 02:40 UTC)
- Second HTTPS sync to GW-03 at 05:15 gave the same RTC write error; GW-03 rebooted at 05:17, back online 05:19, clock still +11 min (internal note, 2026-11-24 05:20 UTC)
- GW-01 and GW-02 still in sync (offset under 1 s) but NTP still failing on all three (internal note, 2026-11-24 05:20 UTC)
- Priority P2 recorded on the ticket (event, 2026-11-23 02:15 UTC)

### Reported, not verified
- Vat 3 went above 7°C for about 40 minutes on Tuesday night with no SMS received, and the TernCloud dashboard showed the reading over the limit (Aroha Ngata, 2026-11-19 07:50 UTC)
- Customer alarm test on all nine vats: vats 4 to 9 sent the SMS within a minute, vats 1, 2 and 3 sent nothing (Aroha Ngata, 2026-11-19 07:50 UTC)
- Customer IT: nothing changed on VLAN 30 and outbound UDP 123 is allowed (Aroha Ngata, 2026-11-23 01:40 UTC). This sits against the NTP timeout logs (internal note, 2026-11-20 07:15 UTC) and is unresolved.
- On "Sunday night" vat 3 went over 7°C again "at about 01:00 our time", no SMS, over the limit for about 50 minutes, and 18,000 litres were dumped (Aroha Ngata, 2026-11-23 01:40 UTC)
- Hourly manual dashboard checks by night staff are the current workaround and are not sustainable or sufficient (Aroha Ngata, 2026-11-19 07:50 UTC and 2026-11-23 01:40 UTC)
- After the HTTPS sync, vats 1 and 2 sent the SMS within a minute and vat 3 sent nothing (Aroha Ngata, 2026-11-23 03:05 UTC)

### Contradicted
- None

### Hypotheses
- UDP 123 blocked for VLAN 30, marked "Not confirmed", proposed by Hannah Odum (internal note, 2026-11-20 07:15 UTC); customer IT reports it allowed (Aroha Ngata, 2026-11-23 01:40 UTC)
- GW-03 refusing to set its clock "may be a hardware fault", proposed by Hannah Odum (2026-11-24 05:40 UTC)
- GW-01 and GW-02 "may drift again" because NTP is still failing, proposed by Hannah Odum (internal note, 2026-11-24 05:20 UTC)

## Tried so far
| # | Action | By | Result | Source |
| --- | --- | --- | --- | --- |
| 1 | Alarm test on all nine vats | Customer (Aroha Ngata) | Vats 4 to 9 SMS within a minute; vats 1 to 3 nothing | Aroha Ngata, 2026-11-19 07:50 UTC |
| 2 | Checked alarm rules and SMS recipients in TernCloud | Hannah Odum | Identical template and recipients on all nine; config ruled out | Hannah Odum, 2026-11-20 01:05 UTC |
| 3 | Downloaded and attached diagnostic bundles from GW-01, 02, 03 (on support's instruction) | Customer (Aroha Ngata) | Bundles attached | Hannah Odum, 2026-11-20 01:10 UTC; Aroha Ngata, 2026-11-20 05:40 UTC |
| 4 | Analysed bundles | Hannah Odum | TS_FUTURE rule skips, clocks 8 to 11 min fast, NTP timeouts since 12 Nov, gateways on VLAN 30 | Internal note, 2026-11-20 07:15 UTC |
| 5 | Checked VLAN 30 for outbound UDP 123 (on support's instruction) | Customer IT | Nothing changed; UDP 123 allowed | Hannah Odum, 2026-11-20 07:20 UTC; Aroha Ngata, 2026-11-23 01:40 UTC |
| 6 | "Force time sync (HTTPS)" to GW-01, 02, 03 at 02:35 UTC | Hannah Odum | GW-01, 02 OK (under 1 s); GW-03 RTC write error, +11 min 05 s | Internal note, 2026-11-23 02:40 UTC |
| 7 | Alarm test on vats 1 to 3 (on support's instruction) | Customer (Aroha Ngata) | Vats 1 and 2 SMS within a minute; vat 3 nothing | Aroha Ngata, 2026-11-23 03:05 UTC |
| 8 | Second "Force time sync (HTTPS)" to GW-03 at 05:15 UTC | Hannah Odum | Same RTC write error | Internal note, 2026-11-24 05:20 UTC |
| 9 | Remote reboot of GW-03 from TernCloud at 05:17 UTC (customer agreed by phone at 05:10) | Hannah Odum | Back online 05:19; clock still +11 min | Internal note, 2026-11-24 05:20 UTC |

## Commitments to the customer
| Commitment (quoted) | Made by | When | Due | Kept / Missed / Open | Source |
| --- | --- | --- | --- | --- | --- |
| "I'm going to send a command from TernCloud that sets the clock on GW-01 to 03 over HTTPS" | Hannah Odum (Tier 1) | 2026-11-23 02:20 UTC | No time stated | Kept (sent 02:35 UTC, internal note 2026-11-23 02:40 UTC) | Hannah Odum, 2026-11-23 02:20 UTC |
| "I'm escalating this to our Field Systems Engineering team now." | Hannah Odum (Tier 1) | 2026-11-24 05:40 UTC | "now" | Kept (escalation event 2026-11-24 06:00 UTC) | Hannah Odum, 2026-11-24 05:40 UTC |
| "You'll get an update from us by 17:30 AWST today (09:30 UTC)." | Hannah Odum (Tier 1) | 2026-11-24 05:40 UTC | "17:30 AWST today (09:30 UTC)" = 2026-11-24 09:30 UTC | Open (Tier 2 owns it, policy 5.3) | Hannah Odum, 2026-11-24 05:40 UTC |

Customer-claimed, not found in thread:
- None

## Service level
- Tier and priority: Business plan (account record: Support plan); P2, set by Hannah Odum at 2026-11-23 02:15 UTC, previously P3 from creation (events, 2026-11-19 07:50 UTC and 2026-11-23 02:15 UTC)
- Business hours: 00:30 to 09:30 UTC, Monday to Friday, 9 hours a day (policy 1.1, 1.2). Clock starts at creation (policy 4.1); paused only while "Pending customer": 2026-11-20 01:10 to 05:40 UTC, 4 h 30 min (events; policy 4.2). "Escalated" status does not pause it.
- Status as of: 2026-11-24 06:00 UTC, the last thread timestamp (not the current time)

| Target (quoted) | Policy section | Clock start / pauses | Deadline (arithmetic) | Status |
| --- | --- | --- | --- | --- |
| First response, Business P3 (priority at the time): "9 business hours" (Business P2 equivalent: "4 business hours") | 3.1, 1.4 | Start Thu 2026-11-19 07:50 UTC; first agent contact 2026-11-20 01:05 UTC (Hannah Odum) | Used: Thu 07:50 to 09:30 (1 h 40 min) + Fri 00:30 to 01:05 (35 min) = 2 h 15 min | Met (within both 9 h and 4 h) |
| Resolution, Business P2: "27 business hours", counted from ticket creation after priority change, excluding paused time | 3.1, 4.3 | Start 2026-11-19 07:50 UTC; pause 2026-11-20 01:10 to 05:40 UTC | Thu 1 h 40 min + Fri (9 h − 4 h 30 min) 4 h 30 min + Mon 9 h + Tue 9 h = 24 h 10 min; remaining 2 h 50 min from Wed 00:30 = 2026-11-25 03:20 UTC (11:20 AWST) | Not yet due: 6 h 20 min business time left (Tue 06:00 to 09:30 = 3 h 30 min + Wed 00:30 to 03:20 = 2 h 50 min). "At risk" under 4.4: 6 h 20 min is below 25% of 27 h (6 h 45 min); at risk since 2026-11-24 05:35 UTC |
| Customer updates, P2: "at least once each business day" | 7.1 | From P2 on Mon 2026-11-23 | Mon update 2026-11-23 02:20 UTC; Tue update 2026-11-24 05:40 UTC; Wed 2026-11-25 update needed by end of business day 09:30 UTC (my reading of "each business day") | Met to date; Wed update not yet due |

- Conflicting deadline in thread: Hannah Odum's SLA check gives "Thu 26 Nov 10:15 AWST", counting 27 business hours from the priority change at Mon 10:15 AWST (internal note, 2026-11-24 01:30 UTC). Policy 4.3 counts from ticket creation, which gives 2026-11-25 03:20 UTC (11:20 AWST Wed), about one business day earlier.
- Escalation of an at-risk P2 ticket requires the Support Team Lead to be notified at escalation (policy 5.2); no notification is recorded in the thread.

## Recommended next action
Confirm the Support Team Lead has been notified (policy 5.2) and send the customer the promised update before 2026-11-24 09:30 UTC. Then restore the vat 3 alarm before the resolution deadline of 2026-11-25 03:20 UTC: GW-03 rejected two HTTPS clock writes and a reboot with an RTC write error, so treat it as a likely hardware fault and arrange a swap or another working alarm path for vat 3. In parallel, find why NTP to pool.terncloud.net:123 times out from VLAN 30 despite customer IT reporting UDP 123 allowed, since GW-01 and 02 may drift and fail again.

## Gaps
- No WA public-holiday calendar supplied; deadlines assume none falls on 19 to 25 Nov 2026 (policy 1.1).
- Status is computed as of the last thread timestamp (2026-11-24 06:00 UTC); actual current status may differ.
- Support Team Lead notification at escalation (policy 5.2) not recorded in the thread.
- Compensation for 18,000 litres of dumped milk requested (Aroha Ngata, 2026-11-23 01:40 UTC); Hannah Odum says she passed it to Joel Brandt (2026-11-23 02:20 UTC). No response from Joel Brandt recorded; only the Account Manager or Head of Customer Support may offer it, in writing (policy 6.3); account record shows "Open credits: None".
- Time of the Sunday-night incident is ambiguous ("Sunday night ... about 01:00 our time") and not checked against GW-03 or TernCloud logs.
- Conflict unresolved between customer IT's "outbound UDP 123 is allowed" and the gateways' NTP timeout logs.
- Harvey depot gateways (DEP-GW-01, 02) not checked for NTP or clock drift in the thread.
