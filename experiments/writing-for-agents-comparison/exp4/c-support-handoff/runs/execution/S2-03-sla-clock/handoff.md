# Escalation handoff: TRN-77391 | Kestrel Dairy Co-operative | Vat 1-3 gateway high-temperature SMS alarms not firing

**Service level:** Resolution target for Business P2, 27 business hours, due Wed 25 Nov 2026 11:20 AWST (03:20 UTC) | Pending, 6 h 20 min of business time remaining as of 2026-11-24 06:00 UTC, which is under 25% of the target (6.75 h), so "at risk" under policy 4.4

## Problem as currently understood
Alarm rules on VAT-GW-01, 02 and 03 (Brunswick plant) have been skipped since 12 Nov because those gateways' clocks run 8 to 11 minutes fast and their NTP syncs fail. Verified: the skip log, the clock offsets, the NTP timeouts, and that a forced HTTPS time sync fixed GW-01 and GW-02 (offset under 1 s) but GW-03 rejects it with an RTC write error, also after a reboot. Not verified: why NTP fails (customer IT says UDP 123 from VLAN 30 is allowed) and whether GW-03 has a hardware fault. Vat 3 has twice exceeded 7 degC with no SMS, and the customer reports 18,000 L of milk dumped after the second event.

| Statement | Label | Source (author, timestamp) |
| --- | --- | --- |
| Vat 3 exceeded 7 degC for about 40 min on Tue 17 Nov night with no SMS; the dashboard showed the reading | Reported | Aroha Ngata, 2026-11-19 07:50 |
| Alarm test: vats 4 to 9 sent SMS, vats 1 to 3 did not | Reported | Aroha Ngata, 2026-11-19 07:50 |
| Alarm rules for vats 1 to 9 use the same template and recipients in TernCloud | Verified | Hannah Odum, 2026-11-20 01:05 |
| GW-01, 02, 03 log RULE_EVAL_SKIPPED reason=TS_FUTURE at every evaluation since 12 Nov | Verified | Hannah Odum (diagnostic bundles), 2026-11-20 07:15 |
| Gateway clocks ahead: GW-01 +9 min 12 s, GW-02 +8 min 40 s, GW-03 +11 min 03 s | Verified | Hannah Odum, 2026-11-20 07:15 |
| NTP sync fails (timeout to pool.terncloud.net:123) on GW-01 to 03 since 12 Nov; still failing on all three | Verified | Hannah Odum, 2026-11-20 07:15 and 2026-11-24 05:20 |
| GW-01 to 03 are on VLAN 30; TernCloud shows GW-04 to 09 last time sync OK | Verified | Hannah Odum, 2026-11-20 07:15 |
| UDP 123 is blocked for VLAN 30 | Suspected (Hannah, 07:15, "Not confirmed"); customer IT says nothing changed and outbound UDP 123 is allowed (Reported, Aroha Ngata, 2026-11-23 01:40) | Hannah Odum, 2026-11-20 07:15; Aroha Ngata, 2026-11-23 01:40 |
| Vat 3 exceeded 7 degC again Sun night about 01:00 AWST for about 50 min with no SMS; found by hourly manual check | Reported | Aroha Ngata, 2026-11-23 01:40 |
| 18,000 L of milk was dumped after that event | Reported | Aroha Ngata, 2026-11-23 01:40 |
| After HTTPS force time sync, GW-01 and GW-02 offset under 1 s; GW-03 rejected the write and stayed +11 min 05 s | Verified | Hannah Odum, 2026-11-23 02:40 |
| Vats 1 and 2 sent SMS in the post-fix test; vat 3 did not | Reported | Aroha Ngata, 2026-11-23 03:05 |
| GW-03 second time-set rejected (RTC write error); after reboot back online 05:19, clock still about +11 min; GW-01 and 02 still in sync | Verified | Hannah Odum, 2026-11-24 05:20 |
| GW-03 may have a hardware fault (RTC) | Suspected | Hannah Odum, 2026-11-24 05:40 |
| GW-01 and 02 may drift again because NTP is still failing | Suspected | Hannah Odum, 2026-11-24 05:20 |
| Hourly dashboard checks by night staff are not sustainable | Reported | Aroha Ngata, 2026-11-23 01:40 |

## What has been tried
| Action | By | When | Result | Label |
| --- | --- | --- | --- | --- |
| Compared alarm rules for vats 1 to 9 | Hannah Odum | 2026-11-20 01:05 | Same template and recipients; configuration does not explain the difference | Verified |
| Requested and analysed diagnostic bundles from GW-01 to 03 | Hannah Odum | 2026-11-20 01:10 to 07:15 | Clock ahead, rule skipped, NTP failing (see above) | Verified |
| Asked customer IT to check outbound UDP 123 from VLAN 30 | Hannah Odum (customer IT reply via Aroha Ngata) | Asked 2026-11-20 07:20; answered 2026-11-23 01:40 | IT says nothing changed and UDP 123 is allowed; not independently checked | Reported |
| "Force time sync (HTTPS)" to GW-01, 02, 03 | Hannah Odum | 2026-11-23 02:35 | GW-01 and 02 OK (under 1 s); GW-03 TIME_SET_REJECTED: RTC write error | Verified |
| Alarm test on vats 1 to 3 after sync | Aroha Ngata | 2026-11-23 03:05 | Vats 1 and 2 SMS received; vat 3 none | Reported |
| Second HTTPS time sync on GW-03 | Hannah Odum | 2026-11-24 05:15 | Same RTC write error | Verified |
| Remote reboot of GW-03 (customer agreed by phone 05:10) | Hannah Odum | 2026-11-24 05:17 | Online 05:19; clock still +11 min | Verified |
| Priority raised P3 to P2 | Hannah Odum | 2026-11-23 02:15 | Recorded with reason | Verified |
| Request for compensation passed to account manager Joel Brandt | Hannah Odum | 2026-11-23 02:20 | No response recorded in the thread | Reported (Hannah's statement; no record of passing it on) |

## Commitments to the customer
| Commitment (quoted) | Made by (name, role) | When | Due | Status |
| --- | --- | --- | --- | --- |
| "I've passed your request to Joel Brandt, your account manager." | Hannah Odum, Support Agent Tier 1 | 2026-11-23 02:20 | No date given | Outstanding (no reply from Joel on the ticket) |
| "Next, I'm going to send a command from TernCloud that sets the clock on GW-01 to 03 over HTTPS" | Hannah Odum, Support Agent Tier 1 | 2026-11-23 02:20 | No date given ("Next") | Kept (sent 02:35) |
| "I'm escalating this to our Field Systems Engineering team now." | Hannah Odum, Support Agent Tier 1 | 2026-11-24 05:40 | "now" (2026-11-24 05:40) | Kept (escalated 06:00) |
| "You'll get an update from us by 17:30 AWST today (09:30 UTC)." | Hannah Odum, Support Agent Tier 1 | 2026-11-24 05:40 | 2026-11-24 09:30 UTC (17:30 AWST) | Outstanding; owned by Tier 2 from escalation (policy 5.3) |

Claimed by the customer but not found in the thread: None. The customer asked for the cost of the milk to be covered (2026-11-23 01:40); no support-side promise of compensation exists in the thread and none has been recorded in writing by the Account Manager or Head of Customer Support (policy 6.3).

## Service level
- Tier: Business (account record; contract term 1 Mar 2026 to 28 Feb 2028)
- Priority: P2 (recorded 2026-11-23 02:15 UTC; ticket was created as P3)
- Resolution, 27 business hours (policy 3.1, 4.3): clock from ticket creation 2026-11-19 07:50 UTC (Thu 15:50 AWST), counting business hours 08:30 to 17:30 AWST Mon to Fri. Paused while "Pending customer" 2026-11-20 01:10 to 05:40 UTC (4.5 business hours, policy 4.2). Used: Thu 1.67 h + Fri 4.5 h + Mon 9 h + Tue 5.5 h = 20.67 h. Remaining 6.33 h. Deadline Wed 25 Nov 2026 11:20 AWST (03:20 UTC). Status: at risk (less than 6.75 h remaining, policy 4.4). Not resolved (1.5: needs a fix or workaround and status Resolved).
- First response, 4 business hours for Business P2 (policy 3.1): ticket created 15:50 AWST Thu; Hannah replied 2026-11-20 01:05 UTC (09:05 AWST Fri), 2 h 15 min of business time. Met (also within the 9 hour P3 target in force at the time).
- Customer updates, P2: at least once each business day (policy 7.1). Updates on 23 Nov and 24 Nov so far; next due by end of business day 24 Nov and committed to 09:30 UTC.
- Escalation (policy 5.1, 5.2): ticket was at risk at escalation, so the Support Team Lead had to be notified at escalation; no notification is recorded in the thread.
- Status as of: 2026-11-24 06:00 UTC (the as-of time given in the export; 14:00 AWST Tue)

## Recommended next action
Tier 2 (Field Systems Engineering) should send the customer the committed update before 09:30 UTC today and, in it, ask Peter Dunn (customer IT) to test outbound UDP 123 from a VLAN 30 host (or capture traffic at the VLAN 30 gateway) to test the unconfirmed blocked-NTP cause, since NTP is still failing on all three gateways and GW-01 and 02 may drift again. If UDP 123 is confirmed open, the NTP failure is a gateway or DNS issue and GW-03's RTC write error should be treated as a probable hardware fault for replacement.

## Open questions
- Hannah's note (2026-11-24 01:30) gives the due time as Thu 26 Nov 10:15 AWST, counted from the priority change and ignoring the pause. Policy 4.3 counts from creation excluding paused time, giving Wed 25 Nov 11:20 AWST. This handoff uses the policy figure. Please confirm.
- The policy does not list public holidays; no WA public holiday is assumed on 24 or 25 Nov. Confirm none applies.
- Support Team Lead notification at escalation (policy 5.2) is not recorded. Notify and record.
- Compensation request (milk, 18,000 L): only Joel Brandt (Account Manager) or the Head of Customer Support may offer anything, in writing on the ticket or account record (6.3). No reply is on record. Chase Joel; do not promise anything (6.2).
- Conflict on the cause: Hannah's suspected block of UDP 123 on VLAN 30 versus customer IT saying it is allowed (reported, untested by support). Why GW-04 to 09 sync and GW-01 to 03 do not is unexplained.
- Why the gateways stopped syncing on 12 Nov is unknown; check for any change that day.
- Whether GW-03 has a hardware fault is unconfirmed; whether a workaround is acceptable for resolution (policy 1.5) is not defined for vat 3, and the customer's interim workaround (hourly manual checks) is rejected by the customer.
- No Tern-side alert exists for the vats between now and fix. Customer is relying on hourly manual checks, which the customer says are not sustainable.
