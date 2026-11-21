# Escalation handoff: TRN-77391 High-temperature SMS alarms not received from vat gateways GW-01 to 03 (clock fault; GW-03 still failing)

**Customer:** Kestrel Dairy Co-operative (KDC-0418), Business plan, Site subscription, 11 G4-E gateways (account record: Support plan, TernCloud subscription, Sites and gateways)
**Earliest deadline:** 2026-11-24 09:30 UTC (17:30 AWST) today: customer update promised by Hannah Odum (thread, 2026-11-24 05:40 UTC). Resolution target follows at 2026-11-25 03:20 UTC (11:20 AWST) and the ticket is already "at risk" (see Service level).

## Problem as currently understood
GW-01, GW-02 and GW-03 have clocks running 8 to 11 minutes fast because NTP sync fails, so the 5-minute high-temperature rule is skipped and no SMS is sent. A forced HTTPS time sync fixed GW-01 and GW-02, but GW-03 rejects the clock write ("RTC write error") even after a second attempt and a reboot, so vat 3 still has no working alarm and a possible hardware fault is a hypothesis. The cause of the NTP failure is unknown, and NTP is still failing on all three, so GW-01 and GW-02 may drift again.

### Verified
- Alarm rules for vats 1 to 9 use the same template ("Vat high temp, above 7°C for 5 min") and the same SMS recipients (Hannah Odum, 2026-11-20 01:05 UTC).
- GW-01, 02, 03 log "RULE_EVAL_SKIPPED reason=TS_FUTURE" at every evaluation since 12 Nov (internal note, Hannah Odum, 2026-11-20 07:15 UTC, from the bundles).
- Gateway clocks were ahead by GW-01 +9 min 12 s, GW-02 +8 min 40 s, GW-03 +11 min 03 s (same note).
- NTP log on all three: "NTP sync failed: timeout (pool.terncloud.net:123)" since 12 Nov; the three gateways are on VLAN 30 (same note). NTP was still failing on all three on 24 Nov (internal note, 2026-11-24 05:20 UTC).
- TernCloud shows GW-04 to 09 with last time sync OK (same 07:15 note).
- "Force time sync (HTTPS)" sent 2026-11-23 02:35 UTC: GW-01 and GW-02 OK, offset under 1 s; GW-03 "TIME_SET_REJECTED: RTC write error", still +11 min 05 s (internal note, 2026-11-23 02:40 UTC).
- Second force sync to GW-03 at 05:15 UTC on 24 Nov gave the same rejection; reboot at 05:17, back online 05:19, clock still about +11 min; GW-01 and GW-02 still in sync (internal note, 2026-11-24 05:20 UTC).
- Priority was changed P3 to P2 and recorded on the ticket (system event, 2026-11-23 02:15 UTC).

### Reported, not verified
- Vat 3 went above 7°C for about 40 minutes on Tuesday night (17 Nov) with no SMS (Aroha Ngata, 2026-11-19 07:50 UTC). The dashboard reading is her statement; no support check is in the thread.
- Alarm test on all nine vats: vats 4 to 9 sent SMS within a minute, vats 1 to 3 sent nothing (Aroha Ngata, 2026-11-19 07:50 UTC).
- Night staff are checking the dashboard hourly as an interim measure (same message).
- Vat 3 went over 7°C again about 01:00 "our time" on Sunday night, no SMS, over the limit about 50 minutes, 18,000 litres dumped (Aroha Ngata, 2026-11-23 01:40 UTC). The time zone of "our time" is not stated.
- Customer IT says nothing changed on VLAN 30 and outbound UDP 123 is allowed (Aroha Ngata, 2026-11-23 01:40 UTC). No support check of the firewall.
- After the sync, vats 1 and 2 sent SMS within a minute and vat 3 sent nothing (Aroha Ngata, 2026-11-23 03:05 UTC).
- Customer asks for the cost of the milk to be covered (2026-11-23 01:40 UTC). This is a request, not an approved item.

### Contradicted
- None

### Hypotheses
- UDP 123 blocked for VLAN 30 is the possible cause of the NTP failure, proposed by Hannah Odum, "Not confirmed" (internal note, 2026-11-20 07:15 UTC). The customer's IT disputes it (Aroha Ngata, 2026-11-23 01:40 UTC), so it is neither confirmed nor ruled out.
- GW-03 may have a hardware fault (RTC), proposed by Hannah Odum (message, 2026-11-24 05:40 UTC).
- GW-01 and GW-02 may drift again while NTP keeps failing, proposed by Hannah Odum (internal note, 2026-11-24 05:20 UTC).

## Tried so far
| # | Action | By | Result | Source |
|---|---|---|---|---|
| 1 | Checked TernCloud alarm rules for vats 1 to 9 | Hannah Odum | Same template and recipients; config does not explain difference | Thread 2026-11-20 01:05 UTC |
| 2 | Asked for diagnostic bundles from GW-01, 02, 03 (status Pending customer 01:10 to 05:40 UTC) | Customer (Aroha Ngata) at Hannah's request | Bundles supplied; showed TS_FUTURE skips, clock offsets, NTP timeouts | Thread 2026-11-20 05:40 and 07:15 UTC |
| 3 | Asked customer IT to check outbound UDP 123 from VLAN 30 | Customer IT at Hannah's request | Customer says it is allowed and nothing changed (not checked by support) | Thread 2026-11-20 07:20, 2026-11-23 01:40 UTC |
| 4 | Force time sync (HTTPS) to GW-01, 02, 03 at 02:35 UTC on 23 Nov | Hannah Odum | GW-01 and 02 OK; GW-03 RTC write error | Note 2026-11-23 02:40 UTC |
| 5 | Alarm test on vats 1 to 3 after sync | Customer (Aroha Ngata) | Vats 1 and 2 sent SMS; vat 3 nothing | Thread 2026-11-23 03:05 UTC |
| 6 | Second force sync to GW-03 at 05:15 UTC on 24 Nov | Hannah Odum | Same RTC write error | Note 2026-11-24 05:20 UTC |
| 7 | Remote reboot of GW-03 at 05:17 UTC (customer agreed by phone 05:10) | Hannah Odum | Back online 05:19; clock still about +11 min | Note 2026-11-24 05:20 UTC |
| 8 | Did not re-test vat 3 alarm after the second sync and reboot | n/a | Result not recorded | Thread (no entry) |

## Commitments to the customer
| Commitment (quoted) | Made by | When | Due | Kept / Missed / Open | Source |
|---|---|---|---|---|---|
| "I'm going to send a command from TernCloud that sets the clock on GW-01 to 03 over HTTPS" | Hannah Odum | 2026-11-23 02:20 UTC | No time stated | Kept (sent 02:35 UTC) | Messages 02:20 and note 02:40 UTC |
| "I'm escalating this to our Field Systems Engineering team now." | Hannah Odum | 2026-11-24 05:40 UTC | "now" (24 Nov 05:40 UTC) | Kept (escalation event 06:00 UTC) | Messages 05:40 and 06:00 UTC |
| "You'll get an update from us by 17:30 AWST today (09:30 UTC)." | Hannah Odum | 2026-11-24 05:40 UTC | 2026-11-24 09:30 UTC | Open (3 h 30 min left at 06:00 UTC); now owned by Tier 2 (policy 5.3) | Message 05:40 UTC |

Customer-claimed, not found in thread:
- None. The customer asks for the milk cost to be covered but does not claim anyone promised it.

Other items:
- Hannah Odum wrote "I've passed your request to Joel Brandt, your account manager" (2026-11-23 02:20 UTC). The thread shows no reply or offer from Joel Brandt, and no credit or compensation is recorded on the ticket or in the account record (Open credits: None). Policy 6.2 bars agents from promising compensation and 6.3 allows only the Account Manager or Head of Customer Support to offer it, in writing. Nothing has been promised.
- Hannah Odum wrote "No rush before Monday; the hourly checks cover you over the weekend" (2026-11-20 07:20 UTC). This is non-committal about timing, but the customer's later message shows the hourly checks were not enough.

## Service level
- Tier and priority: Business plan (account record); P2 recorded on the ticket 2026-11-23 02:15 UTC (system event; policy 2.5). Ticket was created as P3.
- Status as of: 2026-11-24 06:00 UTC (14:00 AWST Tue), the as-of time stated in the thread export, treated as current.

| Target (quoted) | Policy section | Clock start / pauses | Deadline (arithmetic) | Status |
|---|---|---|---|---|
| Resolution, Business P2: "27 business hours" | 3.1, 4.3 (counted from creation, new priority) | Start: created 2026-11-19 07:50 UTC (Thu 15:50 AWST). Pause: Pending customer 2026-11-20 01:10 to 05:40 UTC (4 h 30 min, all inside business hours) (4.2) | Business hours used to 06:00 UTC 24 Nov: Thu 15:50 to 17:30 = 1 h 40; Fri 08:30 to 17:30 = 9 h; Mon = 9 h; Tue 08:30 to 14:00 = 5 h 30; total 25 h 10; minus 4 h 30 pause = 20 h 40. Remaining 27 h - 20 h 40 = 6 h 20. Today 14:00 to 17:30 = 3 h 30, leaving 2 h 50 from 08:30 Wed 25 Nov = 11:20 AWST Wed 25 Nov = 03:20 UTC Wed 25 Nov. | At risk (6 h 20 left is 23.5% of 27 h, below 25% = 6 h 45; policy 4.4). Not breached. |
| First response, Business P2: "4 business hours" (ticket was P3 at creation: "9 business hours") | 3.1, 4.1, 1.4 | Start: created Thu 15:50 AWST; first agent contact Hannah Odum Fri 2026-11-20 01:05 UTC (09:05 AWST) | Thu 15:50 to 17:30 = 1 h 40, plus Fri 08:30 to 09:05 = 35 min; total 2 h 15 | Met under either target |
| Customer updates, P2: "at least once each business day" | 7.1 | Business days since creation | Agent messages to the customer on Fri 20 Nov, Mon 23 Nov and Tue 24 Nov (2026-11-20 07:20 UTC, 2026-11-23 02:20 UTC, 2026-11-24 05:40 UTC). Wed 25 Nov update is next due, and the 09:30 UTC promise today is separate. | Met so far; next due Wed 25 Nov |

- Conflict with the thread: Hannah Odum's internal note (2026-11-24 01:30 UTC) gives "Thu 26 Nov 10:15 AWST. Plenty of time", counting 27 business hours from the priority change at Mon 10:15 AWST. Policy 4.3 counts from ticket creation and excludes only paused time, so that deadline is wrong by about 1.5 business days. The policy-based deadline is Wed 25 Nov 11:20 AWST. This assumes no WA public holiday on 19 to 25 Nov, which is not stated in the supplied material.
- Escalation: policy 5.1 allows escalation when a P2 is at risk, and 5.2 requires the Support Team Lead to be notified at escalation. No notification is recorded in the thread.

## Recommended next action
Tier 2 should send the customer the promised update by 09:30 UTC today and ask a Tier 2 or field engineer to deal with the GW-03 clock fault (RTC or hardware, replacement or other workaround so vat 3 alarms), with the NTP failure on VLAN 30 investigated next so GW-01 and GW-02 stay in sync. The evidence points to GW-03 because it alone rejects the clock write after two attempts and a reboot, and the resolution target is at risk, due 03:20 UTC on Wed 25 Nov (11:20 AWST). Notify the Support Team Lead now (policy 5.2) and chase Joel Brandt about the compensation request; no one at Tern has offered anything yet.

## Gaps
- Support Team Lead notification (policy 5.2): not recorded in the thread; unknown whether it happened.
- No reply from Joel Brandt on the compensation request, and no recorded written offer (policy 6.3).
- Root cause of the NTP failure is unconfirmed: the UDP 123 hypothesis is disputed by customer IT and no support-side network check was made.
- GW-03 alarm test after the second sync and reboot: result not recorded.
- Whether Sunday's event ("01:00 our time") falls before or after the 2026-11-23 02:35 UTC sync: time zone not stated; the customer message arrived 01:40 UTC on 23 Nov.
- Public holidays: none assumed for 19 to 25 Nov 2026; the supplied material does not list them, and any holiday would move the resolution deadline later.
- Customer-reported facts (vat 3 breaches, 18,000 L loss, test results) have no support verification.
