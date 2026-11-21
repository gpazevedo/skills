Clarifying question: What is the current date and time? The environment clock reads 2026-11-21 18:35 UTC, which is before the ticket's last entries (up to 2026-11-24 06:00 UTC), so it cannot be the real "now". This handoff gives every status as at the escalation event, 2026-11-24 06:00 UTC (14:00 AWST); recompute the "Status" column against the real time using the deadlines given.

# Escalation handoff: TRN-77391 High-temperature SMS alarms not received from some vat gateways

**Customer:** Kestrel Dairy Co-operative, KDC-0418, Business support plan (account record)  **Priority:** P2 (raised from P3 at 2026-11-23 02:15 UTC)  **Prepared:** status as at 2026-11-24 06:00 UTC (14:00 AWST); see clarifying question above

## Service level
| Clock | Policy clause | Started | Deadline | Status |
|---|---|---|---|---|
| First response | 3.1 Business / P3 (priority at the time): "9 business hours"; 1.4 | 2026-11-19 07:50 UTC (Thu 15:50 AWST), ticket created | 2026-11-20 07:50 UTC (Fri 15:50 AWST) | Met at 2026-11-20 01:05 UTC (Hannah Odum's first reply), 2 h 15 min business time used |
| Resolution | 3.1 Business / P2: "27 business hours"; 4.3 "counted from ticket creation and excluding paused time"; 4.2 pause | 2026-11-19 07:50 UTC (ticket created) | 2026-11-25 03:20 UTC (Wed 11:20 AWST) | At risk (4.4): 6 h 20 min business time left, under the 25% line of 6 h 45 min; at risk since 2026-11-24 05:35 UTC |
| Customer update | 7.1: "P2: at least once each business day." | P2 from 2026-11-23 02:15 UTC | End of business Wed 25 Nov: 2026-11-25 09:30 UTC (17:30 AWST) | Met for Mon 23 Nov (02:20 UTC) and Tue 24 Nov (05:40 UTC); running for Wed 25 Nov. Separate open commitment for Tue 24 Nov 09:30 UTC, see Commitments |

- First response: Thu 19 Nov 07:50 to 09:30 UTC = 1 h 40 min; Fri 20 Nov 00:30 to 01:05 UTC = 35 min; total 2 h 15 min of 9 h. Under the P2 figure of "4 business hours" it would still be met (deadline 2026-11-20 02:50 UTC); 4.3 changes only the resolution target.
- Resolution: Thu 19 Nov 1 h 40 min + Fri 20 Nov (9 h minus 4 h 30 min "Pending customer", 01:10 to 05:40 UTC) 4 h 30 min + Mon 23 Nov 9 h + Tue 24 Nov 9 h = 24 h 10 min; remaining 2 h 50 min from Wed 25 Nov 00:30 UTC gives 03:20 UTC. Used at 06:00 UTC Tue 24 Nov: 15 h 10 min + 5 h 30 min = 20 h 40 min; left 6 h 20 min; 25% of 27 h = 6 h 45 min, crossed at 20 h 15 min used = Tue 24 Nov 05:35 UTC.
- Gap: the policy excludes "Western Australian public holidays" (1.1) but the case lists no holiday dates. The figures above assume none falls on 19 to 25 Nov; if one does, each deadline moves by that day's business hours.
- Escalation obligation: clause 5.2 says "When a P1 ticket, or an at-risk P2 ticket, is escalated, the Support Team Lead must be notified at escalation." The ticket was at risk when escalated at 06:00 UTC. The thread does not record a Team Lead notification.

## Problem as currently understood
Since 12 Nov, gateways VAT-GW-01, 02 and 03 (VLAN 30) have failed NTP sync to pool.terncloud.net:123, their clocks ran 8 to 11 minutes fast, and their rule engines skipped every alarm evaluation with "RULE_EVAL_SKIPPED reason=TS_FUTURE", so vats 1 to 3 sent no high-temperature SMS. A forced HTTPS time sync fixed the clocks on GW-01 and GW-02 (customer reports their alarms now work), but GW-03 rejects clock writes with "TIME_SET_REJECTED: RTC write error", also after a reboot, so vat 3 still has no working alarm; a GW-03 hardware fault is suspected. Why NTP fails is unknown: the suspected UDP 123 block on VLAN 30 is denied by the customer's IT, and GW-01 and GW-02 can drift again while NTP keeps failing.

| Fact | Status | Evidence |
|---|---|---|
| Each vat has its own gateway, VAT-GW-01 to 09, model G4-E (Ethernet), at Brunswick | Verified | Account record, "Sites and gateways"; customer message 2026-11-19 07:50 |
| Vats 1 to 9 use the same alarm rule template ("Vat high temp, above 7°C for 5 min") and the same SMS recipients | Verified | Hannah Odum checked alarm rules in TernCloud, 2026-11-20 01:05 |
| Rule engine on GW-01, 02 and 03 logs "RULE_EVAL_SKIPPED reason=TS_FUTURE" at every evaluation since 12 Nov | Verified | Diagnostic bundles, internal note 2026-11-20 07:15 |
| Gateway clocks ahead of sensor timestamps: GW-01 +9 min 12 s, GW-02 +8 min 40 s, GW-03 +11 min 03 s | Verified | Diagnostic bundles, internal note 2026-11-20 07:15 |
| Clock ahead means the 5-minute reading window never fills, so the rule is skipped | Suspected | Hannah Odum's reading of the bundles, internal note 2026-11-20 07:15; consistent with the TS_FUTURE reason code and with vats 1 and 2 alarming after their clocks were fixed (reported, below) |
| NTP log on GW-01, 02 and 03: "NTP sync failed: timeout (pool.terncloud.net:123)", repeated since 12 Nov | Verified | Diagnostic bundles, internal note 2026-11-20 07:15. Restated as "still failing on all three" in internal note 2026-11-24 05:20; the check used that day is not stated |
| GW-01 to 03 are on VLAN 30 | Verified | Diagnostic bundles, internal note 2026-11-20 07:15 |
| GW-04 to 09 show last time sync OK | Verified | TernCloud, internal note 2026-11-20 07:15 |
| UDP 123 is blocked for VLAN 30 | Suspected | Internal note 2026-11-20 07:15: "Possible cause ... Not confirmed." See Contradictions |
| Nothing has changed on VLAN 30 and outbound UDP 123 is allowed | Reported | Customer's IT, via Aroha Ngata 2026-11-23 01:40; how IT checked is not stated |
| GW-01 and GW-02 clocks now in sync, offset under 1 s | Verified | Force time sync result, internal note 2026-11-23 02:40; still in sync per internal note 2026-11-24 05:20 |
| GW-01 and GW-02 may drift again while NTP fails | Suspected | Internal note 2026-11-24 05:20 |
| GW-03 refuses clock set: "TIME_SET_REJECTED: RTC write error"; clock +11 min 05 s, still +11 min after reboot | Verified | Force time sync results 2026-11-23 02:35 and 2026-11-24 05:15; reboot 05:17 to 05:19; internal notes 2026-11-23 02:40 and 2026-11-24 05:20 |
| GW-03 has a hardware fault | Suspected | Hannah Odum to customer 2026-11-24 05:40: "may be a hardware fault" |
| After the clock fix, vats 1 and 2 sent the test SMS within a minute; vat 3 sent nothing | Reported | Aroha Ngata 2026-11-23 03:05 (customer test); no support-side check of SMS delivery recorded |
| Test on 19 Nov: vats 4 to 9 sent the SMS within a minute; vats 1, 2 and 3 sent nothing | Reported | Aroha Ngata 2026-11-19 07:50; the cause for 1 to 3 is supported by the verified log findings above |
| Tuesday night (17 Nov) vat 3 was above 7°C for about 40 minutes, no SMS; the dashboard showed the reading over the limit | Reported | Aroha Ngata 2026-11-19 07:50 |
| Sunday night, about 01:00 local time, vat 3 went over 7°C again, no SMS, over the limit about 50 minutes before the hourly check caught it; 18,000 litres dumped | Reported | Aroha Ngata 2026-11-23 01:40 |
| Night staff check the dashboard hourly as a workaround; customer says they "can't keep doing hourly checks" and the checks "aren't enough" | Reported | Aroha Ngata 2026-11-19 07:50 and 2026-11-23 01:40; priority raised under clause 2.2 for this reason, event 2026-11-23 02:15 |
| Customer asks for the cost of the dumped milk to be covered | Reported | Aroha Ngata 2026-11-23 01:40; passed to Joel Brandt (Account Manager) 2026-11-23 02:20; account record "Open credits: None" |

Contradictions:
- Cause of the NTP failure: internal note 2026-11-20 07:15 suspects "UDP 123 blocked for VLAN 30"; customer IT, 2026-11-23 01:40, says "nothing has changed on VLAN 30 and outbound UDP 123 is allowed". Both unconfirmed by a test.
- Resolution deadline: internal note 2026-11-24 01:30 counts "27 business hours" from the P2 change ("Mon 10:15 AWST"), giving "Thu 26 Nov 10:15 AWST. Plenty of time." Policy 4.3 counts the new target "from ticket creation and excluding paused time", giving Wed 25 Nov 11:20 AWST, and the ticket was at risk at escalation.
- Workaround adequacy: Hannah Odum told the customer 2026-11-20 07:20 "the hourly checks cover you over the weekend"; the customer reported 2026-11-23 01:40 that the hourly check found vat 3 about 50 minutes over the limit and the milk was dumped.

## What has been tried
| When | Who | Action | Result |
|---|---|---|---|
| 2026-11-19 (afternoon local, before 07:50 UTC) | Aroha Ngata (customer) | Alarm test on all nine vats | Vats 4 to 9 SMS within a minute; vats 1, 2, 3 nothing |
| From 2026-11-19 | Customer night staff | Hourly dashboard checks | Caught Sunday-night excursion after about 50 minutes; 18,000 litres dumped |
| 2026-11-20 01:05 UTC | Hannah Odum (Tier 1) | Checked alarm rules in TernCloud | Same template and recipients for vats 1 to 9 |
| 2026-11-20 01:10 to 05:40 UTC | Hannah Odum requested; Aroha Ngata supplied | Diagnostic bundles from GW-01, 02, 03 (Maintenance > Diagnostics > Download bundle) | TS_FUTURE rule skips, clock offsets, NTP timeouts since 12 Nov, VLAN 30 (internal note 07:15) |
| 2026-11-20 07:15 UTC | Hannah Odum | Checked time sync status of GW-04 to 09 in TernCloud | Last time sync OK |
| Between 2026-11-20 07:20 and 2026-11-23 01:40 UTC | Customer IT | Checked outbound UDP 123 from VLAN 30 | "nothing has changed on VLAN 30 and outbound UDP 123 is allowed"; method not stated |
| 2026-11-23 02:20 UTC | Hannah Odum | Passed compensation request to Joel Brandt | Result not recorded |
| 2026-11-23 02:35 UTC | Hannah Odum | "Force time sync (HTTPS)" to GW-01, 02, 03 | GW-01, GW-02: OK, offset under 1 s. GW-03: "TIME_SET_REJECTED: RTC write error", still +11 min 05 s |
| 2026-11-23 by 03:05 UTC | Aroha Ngata | Alarm test on vats 1 to 3 | Vats 1 and 2 SMS within a minute; vat 3 nothing |
| 2026-11-24 05:15 UTC | Hannah Odum | Second "Force time sync (HTTPS)" to GW-03 | Same "TIME_SET_REJECTED: RTC write error" |
| 2026-11-24 05:17 UTC | Hannah Odum (customer agreed by phone 05:10) | Remote reboot of GW-03 from TernCloud | Back online 05:19; clock still +11 min |
| 2026-11-24 06:00 UTC | Hannah Odum | Escalated to Tier 2 (Field Systems Engineering) | Status Escalated, priority P2 |

## Commitments to the customer
| When | Made by | Commitment (quoted) | Due | State |
|---|---|---|---|---|
| 2026-11-23 02:20 UTC | Hannah Odum | "I've passed your request to Joel Brandt, your account manager." | Not stated | Met as stated; no reply from Joel Brandt recorded |
| 2026-11-23 02:20 UTC | Hannah Odum | "Next, I'm going to send a command from TernCloud that sets the clock on GW-01 to 03 over HTTPS, which avoids the NTP port." | Not stated | Met, sent 02:35 UTC |
| 2026-11-24 05:40 UTC | Hannah Odum | "I'm escalating this to our Field Systems Engineering team now." | "now" | Met, 06:00 UTC |
| 2026-11-24 05:40 UTC | Hannah Odum | "You'll get an update from us by 17:30 AWST today (09:30 UTC)." | 2026-11-24 09:30 UTC | Open, 3 h 30 min left at 06:00 UTC; Tier 2 now owns it (clause 5.3) |

No compensation, credit or fix date has been offered. Clause 6.3: only Joel Brandt (Account Manager) or the Head of Customer Support may offer compensation, and only in writing on the ticket or account record.

## Recommended next action
Find out why GW-03 rejects clock writes: get a fresh diagnostic bundle from VAT-GW-03 (as on 20 Nov, Maintenance > Diagnostics > Download bundle, via Aroha Ngata; whether Tier 2 can pull it remotely is not stated) and read the entries around the 2026-11-24 05:15 UTC time set and the 05:17 UTC reboot for the cause of "RTC write error". This tests the leading suspected cause (GW-03 hardware fault), which is the one thing still keeping vat 3 without an alarm. A logged hardware fault in the RTC confirms it and points to replacing GW-03 as the fix; a cause other than the RTC hardware rules it out and becomes the next target. Vat 3 is the only reported failing alarm now, so this is the path to resolution, which is due 2026-11-25 03:20 UTC (Wed 11:20 AWST) with 6 h 20 min of business time left. Before that, the update promised for 2026-11-24 09:30 UTC (17:30 AWST) is due, and clause 5.2 requires the Support Team Lead to be notified of this at-risk P2 escalation.

Open questions:
- Was the Support Team Lead notified at escalation, as clause 5.2 requires? Not recorded.
- Is there a practical workaround for vat 3 until GW-03 is fixed or replaced? None is stated in the case.
- Why does NTP to pool.terncloud.net:123 time out from GW-01 to 03 when customer IT says UDP 123 is allowed? What changed on or around 12 Nov? Peter Dunn (IT Coordinator) is the network contact in the account record.
- Are GW-01 and GW-02 still in sync, and do vats 1 and 2 still alarm? Last clock check 2026-11-24 05:20 UTC; last alarm test (customer) 2026-11-23 03:05 UTC.
- Are the Harvey depot gateways DEP-GW-01 and DEP-GW-02 (G4-E, same account) affected? Not mentioned in the thread.
- Which date was the "Sunday night ... about 01:00 our time" excursion: early 22 Nov or early 23 Nov AWST? Not stated.
- Has Joel Brandt responded to the compensation request? Not recorded.
- Firmware versions of GW-01 to 09: not stated.
