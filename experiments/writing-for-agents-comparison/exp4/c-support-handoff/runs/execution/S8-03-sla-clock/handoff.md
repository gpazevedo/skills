# Escalation handoff: TRN-77391 High-temperature SMS alarms not received from some vat gateways

**Customer:** Kestrel Dairy Co-operative, account KDC-0418, Business plan (account record)  **Priority:** P2 (changed from P3 on 2026-11-23 02:15 UTC, recorded on ticket)  **Prepared:** 2026-11-24 06:00 UTC (14:00 AWST), the as-of time in the ticket export

## Service level
| Clock | Policy clause | Started | Deadline | Status |
|---|---|---|---|---|
| First response (Business P2: "4 business hours") | 3.1, 1.4, 4.1 | Created Thu 2026-11-19 07:50 UTC (15:50 AWST) | Not reached; first agent contact came first | Met: Hannah Odum replied 2026-11-20 01:05 UTC after 2h15m of business time |
| Resolution (Business P2: "27 business hours") | 3.1, 4.1, 4.2, 4.3 | Counted from creation, 2026-11-19 07:50 UTC, excluding Pending customer time | Wed 2026-11-25 03:20 UTC (11:20 AWST) if no further pause | At risk: 20h40m used, 6h20m left (23.5% of 27h, under the 25% threshold in 4.4) |
| Customer update interval (P2: "at least once each business day") | 7.1 | Each business day | Next one due by end of Wed 2026-11-25 business hours; the committed update below is sooner | Met for today (update 2026-11-24 05:40 UTC) |

Arithmetic, resolution (business hours are 00:30 to 09:30 UTC, clause 1.2; no public holiday appears in the case): Thu 19 Nov 07:50 to 09:30 = 1h40m; Fri 20 Nov 00:30 to 09:30 = 9h00m, minus the Pending customer pause 01:10 to 05:40 (4h30m, clause 4.2) = 4h30m; Mon 23 Nov = 9h00m; Tue 24 Nov 00:30 to 06:00 = 5h30m. Total 1h40m + 4h30m + 9h00m + 5h30m = 20h40m. Remaining 27h - 20h40m = 6h20m. Tue has 3h30m more (to 09:30 UTC), leaving 2h50m on Wed from 00:30 UTC, so 03:20 UTC Wed.
First response arithmetic: Thu 07:50 to 09:30 = 1h40m, plus Fri 00:30 to 01:05 = 35m, total 2h15m, under 4h (and under the P3 target of 9h).
Correction to the internal note of 2026-11-24 01:30 UTC: it counted 27 hours from the priority change (Mon 10:15 AWST) and gave Thu 26 Nov 10:15 AWST. Clause 4.3 says the new target is counted from ticket creation, so that deadline is wrong by about a day and the ticket is at risk, not "plenty of time".
Clause 5.2: an at-risk P2 ticket escalated requires the Support Team Lead to be notified at escalation. The thread does not record that notification. It is not stated whether it happened.

## Problem as currently understood
Three gateways at Brunswick (VAT-GW-01 to 03, VLAN 30) have clocks running 8 to 11 minutes ahead because their NTP sync fails, so the 5-minute high-temperature rule is skipped and no SMS is sent. Forcing a time set over HTTPS fixed GW-01 and GW-02. GW-03 rejects the time set with an RTC write error, even after a reboot, so vat 3 still has no working alarm and has already caused one product loss. Why NTP fails on VLAN 30 is not established.

| Fact | Status | Evidence |
|---|---|---|
| Alarm rules for vats 1 to 9 use the same template ("Vat high temp, above 7°C for 5 min") and same SMS recipients | Verified | Hannah Odum checked rules in TernCloud, 2026-11-20 01:05 |
| Gateways VAT-GW-01, 02, 03 log "RULE_EVAL_SKIPPED reason=TS_FUTURE" at every evaluation since 12 Nov | Verified | Diagnostic bundles read by Hannah Odum, internal note 2026-11-20 07:15 |
| Clocks ahead of sensor timestamps: GW-01 +9m12s, GW-02 +8m40s, GW-03 +11m03s | Verified | Same bundles, same note |
| NTP fails on GW-01 to 03: "NTP sync failed: timeout (pool.terncloud.net:123)" since 12 Nov | Verified | Same bundles, same note |
| GW-01 to 03 are on VLAN 30 | Verified | Bundles, same note |
| GW-04 to 09 show last time sync OK | Verified | TernCloud view, same note |
| The 5-minute window never fills because the clock is ahead, so the rule is skipped | Suspected | Hannah's reasoning in the internal note; the log reason supports it but no test isolates it |
| Outbound UDP 123 from VLAN 30 is blocked | Suspected | Internal note 2026-11-20 07:15 ("Not confirmed"); customer IT reports it is allowed (below) |
| IT says nothing changed on VLAN 30 and outbound UDP 123 is allowed | Reported | Aroha Ngata, 2026-11-23 01:40; no network check by support recorded |
| Vats 4 to 9 sent the SMS within a minute on test; vats 1 to 3 sent nothing | Reported | Aroha Ngata, 2026-11-19 07:50 |
| Vat 3 went above 7°C for about 40 minutes on Tuesday night (17 Nov) with no SMS | Reported | Aroha Ngata, 2026-11-19 07:50; dashboard reading cited by customer, not checked by support |
| Vat 3 went over 7°C again about 01:00 AWST Monday 23 Nov, over limit about 50 minutes, 18,000 litres dumped | Reported | Aroha Ngata, 2026-11-23 01:40 |
| Force time sync (HTTPS) set GW-01 and GW-02 to offset under 1 s | Verified | Result OK in internal note 2026-11-23 02:40; still under 1 s at 2026-11-24 05:20 |
| Vats 1 and 2 now send the SMS on test | Reported | Aroha Ngata, 2026-11-23 03:05 (no support-side check recorded) |
| GW-03 refuses to set its clock: "TIME_SET_REJECTED: RTC write error", twice (02:35 and 05:15 UTC), clock still about +11 min after reboot | Verified | Internal notes 2026-11-23 02:40 and 2026-11-24 05:20 |
| GW-03 has a hardware fault (RTC) | Suspected | Hannah Odum's message 2026-11-24 05:40 ("may be a hardware fault") |
| Vat 3 still sends no SMS on test | Reported | Aroha Ngata, 2026-11-23 03:05; not retested after the 05:17 reboot |
| GW-01 and GW-02 may drift again because NTP still fails | Suspected | Internal note 2026-11-24 05:20 |
| Night staff check the dashboard hourly as the interim measure | Reported | Aroha Ngata, 2026-11-19 07:50 and 2026-11-23 01:40 |

Contradictions:
- Hannah's message to the customer (2026-11-20 07:20) says the clocks are fast "because they can't reach our time server"; her internal note of 07:15 says the UDP 123 block is "Not confirmed". Customer IT later reports UDP 123 is allowed (2026-11-23 01:40). Both versions stand; the cause of the NTP timeout is open.
- Internal SLA note (2026-11-24 01:30) gives a deadline of Thu 26 Nov 10:15 AWST; policy clause 4.3 gives Wed 25 Nov 11:20 AWST (see Service level).
- Hannah's message of 2026-11-20 07:20 says "the hourly checks cover you over the weekend"; the customer's 2026-11-23 01:40 message says hourly checks were not enough, and the priority change records they are not a practical workaround.

## What has been tried
| When (UTC) | Who | Action | Result |
|---|---|---|---|
| 2026-11-20 01:05 | Hannah Odum | Checked alarm rules for vats 1 to 9 | Same template and recipients; config does not explain it |
| 2026-11-20 01:10 | Hannah Odum | Asked customer for diagnostic bundles from GW-01 to 03 | Customer attached all three, 05:40 |
| 2026-11-20 07:15 | Hannah Odum | Read the bundles | Clock offsets, RULE_EVAL_SKIPPED and NTP timeouts found |
| 2026-11-20 07:20 | Hannah Odum | Asked customer IT to check outbound UDP 123 from VLAN 30 | Customer IT says it is allowed (2026-11-23 01:40); no network-side check by support recorded |
| 2026-11-19 (before ticket) | Aroha Ngata | Alarm test on all nine vats | Vats 4 to 9 worked, 1 to 3 did not (reported) |
| 2026-11-23 02:35 | Hannah Odum | "Force time sync (HTTPS)" to GW-01, 02, 03 | GW-01 and 02 OK, offset under 1 s; GW-03 rejected, RTC write error |
| 2026-11-23 03:05 | Aroha Ngata | Alarm test on vats 1 to 3 after the sync | Vats 1 and 2 sent SMS; vat 3 nothing (reported) |
| 2026-11-24 05:10 | Hannah Odum | Phone agreement with Aroha for a remote reboot of GW-03 | Agreed |
| 2026-11-24 05:15 | Hannah Odum | Second "Force time sync (HTTPS)" to GW-03 | Same RTC write error |
| 2026-11-24 05:17 | Hannah Odum | Remote reboot of GW-03 from TernCloud | Back online 05:19; clock still about +11 min |
| 2026-11-23 02:20 | Hannah Odum | Passed the compensation request to Joel Brandt | No response from Joel recorded |
| 2026-11-24 06:00 | Hannah Odum | Escalated to Tier 2 (Field Systems Engineering), status Escalated | Tier 2 owns the ticket (clause 5.3) |

## Commitments to the customer
| When (UTC) | Made by | Commitment (quoted) | Due | State |
|---|---|---|---|---|
| 2026-11-24 05:40 | Hannah Odum | "You'll get an update from us by 17:30 AWST today (09:30 UTC)." | 2026-11-24 09:30 UTC | Open, 3h30m left; Tier 2 now owns it (clause 5.3) |
| 2026-11-23 02:20 | Hannah Odum | "I'm not able to offer compensation myself, so I've passed your request to Joel Brandt, your account manager." | Not stated | Open: no reply from Joel Brandt is recorded, and no credit or compensation has been offered (clause 6.3 allows only the Account Manager or Head of Customer Support, in writing) |
| 2026-11-23 02:20 | Hannah Odum | "Next, I'm going to send a command from TernCloud that sets the clock on GW-01 to 03 over HTTPS" and "could you run the alarm test on vats 1 to 3?" | Not stated | Met: command sent 02:35, test run 03:05 |

No fix date, credit, refund or compensation has been promised. The account record holds no commitments (open credits: none; flags: none).

## Recommended next action
Have Field Systems Engineering look at GW-03 first: pull a fresh diagnostic bundle after the 05:17 reboot, read the RTC error and the firmware version, and compare against GW-01 and GW-02 (which accepted the HTTPS time set). If a firmware reapply or local-page clock set clears the error, GW-03 is fixed in place; if the RTC write error persists, the hardware-fault suspicion is confirmed and a replacement G4-E for vat 3 should be arranged, then ask Aroha to rerun the vat 3 alarm test. Racing the 09:30 UTC (17:30 AWST) update commitment today and the at-risk resolution deadline of 03:20 UTC Wed 25 Nov (11:20 AWST). Vat 3 is the gateway with two reported excursions and the product loss.

Open questions:
- Was the Support Team Lead notified at escalation (clause 5.2)? Not recorded.
- Has Joel Brandt replied on the 18,000-litre compensation request? Nothing recorded; the customer has had no answer on it.
- Why does NTP time out from VLAN 30 when customer IT says UDP 123 is open? Only GW-01 to 03 are known to be on VLAN 30; which VLAN GW-04 to 09 use is not stated in the case.
- GW-01 and GW-02 are in sync only by the one-off HTTPS set; with NTP still failing they may drift again. Recheck their offsets.
- Vat 3 has no alarm coverage now; the hourly dashboard check is the only interim control and the customer says it is not sustainable.
