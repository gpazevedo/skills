# Escalation handoff: TRN-77391 High-temperature SMS alarms not received from vat gateways VAT-GW-01 to 03 (GW-03 still failing)

**Customer:** Kestrel Dairy Co-operative, KDC-0418, Business plan (account record: "Support plan: Business")   **Severity/priority:** P2, recorded on ticket 2026-11-23 02:15 UTC by Hannah Odum (policy 2.5: "a priority applies only once recorded on the ticket")
**Most urgent deadline:** Customer update promised by 17:30 AWST today = 2026-11-24 09:30 UTC (thread, Hannah Odum 2026-11-24 05:40 UTC); 3h30m after the as-of time of 06:00 UTC. Tier 2 now owns it (policy 5.3). Next: P2 resolution target at about 2026-11-25 03:20 UTC (11:20 AWST Wed), see Service-level status.

## Problem as currently understood
Alarm rules on VAT-GW-01, 02 and 03 (Brunswick, VLAN 30) have been skipped since 12 Nov because the gateway clocks run 8 to 11 minutes ahead after NTP sync failures. A forced HTTPS time sync fixed GW-01 and GW-02, but GW-03 rejects the clock write twice ("RTC write error") and survived a reboot, so vat 3 still sends no high-temperature SMS. The customer reports two missed alarms on vat 3 (the second led to 18,000 litres being dumped) and has asked for the cost to be covered. The cause of the NTP failure is unexplained, so GW-01 and GW-02 may drift again.

| Fact | Status | How established / cite |
|---|---|---|
| Vats 1 to 3 sent no SMS in the customer's 19 Nov test; vats 4 to 9 did within a minute | Reported | Aroha Ngata, 2026-11-19 07:50 |
| Vat 3 exceeded 7°C for about 40 min on Tuesday night with no SMS; dashboard showed the reading | Reported | Aroha Ngata, 2026-11-19 07:50 |
| Vat 3 exceeded 7°C again about 01:00 customer time on Sunday night, about 50 min over limit, 18,000 L dumped, no SMS | Reported | Aroha Ngata, 2026-11-23 01:40 |
| Night staff doing hourly dashboard checks; customer says these are not sufficient | Reported | Aroha Ngata, 2026-11-19 07:50 and 2026-11-23 01:40 |
| Vats 1 to 9 use the same rule template and SMS recipients | Verified | Hannah Odum checked TernCloud alarm rules, 2026-11-20 01:05 |
| GW-01 to 03 log "RULE_EVAL_SKIPPED reason=TS_FUTURE" at every evaluation since 12 Nov | Verified | Diagnostic bundles read by Hannah Odum, internal note 2026-11-20 07:15 |
| Clock offsets before fix: GW-01 +9 min 12 s, GW-02 +8 min 40 s, GW-03 +11 min 03 s | Verified | Same bundles, note 2026-11-20 07:15 |
| NTP log on all three: "NTP sync failed: timeout (pool.terncloud.net:123)" since 12 Nov; GW-01 to 03 on VLAN 30 | Verified | Same bundles, note 2026-11-20 07:15 |
| TernCloud shows GW-04 to 09 last time sync OK | Verified | TernCloud view, note 2026-11-20 07:15 |
| Clock skew stops the rule window filling, which is why the rule is skipped | Hypothesis | Hannah Odum, note 2026-11-20 07:15. Supported by the customer-reported pass on vats 1 and 2 after sync, but no support test isolates it |
| UDP 123 is blocked for VLAN 30 | Hypothesis | Hannah Odum, note 2026-11-20 07:15 ("Not confirmed") |
| Customer IT says nothing changed on VLAN 30 and outbound UDP 123 is allowed | Reported | Aroha Ngata, 2026-11-23 01:40 |
| After "Force time sync (HTTPS)", GW-01 and GW-02 offset under 1 s; still under 1 s at 05:20 on 24 Nov | Verified | Command results, notes 2026-11-23 02:40 and 2026-11-24 05:20 |
| Vats 1 and 2 sent SMS within a minute after the sync | Reported | Aroha Ngata, 2026-11-23 03:05 (customer test) |
| GW-03 rejected time set twice ("TIME_SET_REJECTED: RTC write error"); clock still about +11 min after reboot at 05:17 (online 05:19) | Verified | Command results, notes 2026-11-23 02:40 and 2026-11-24 05:20 |
| Vat 3 still sent nothing in the 23 Nov test | Reported | Aroha Ngata, 2026-11-23 03:05 |
| GW-03 may have a hardware (RTC) fault | Hypothesis | Hannah Odum, 2026-11-24 05:40 ("may be a hardware fault") |
| NTP is still failing on all three, so GW-01 and GW-02 may drift again | Hypothesis | Hannah Odum, note 2026-11-24 05:20. The failing NTP is Verified; the drift is a prediction |
| Gateways are G4-E, one per vat, 9 at Brunswick | Verified | Account record, Sites and gateways |

**Open disagreements:**
- UDP 123: support's hypothesis (blocked on VLAN 30) vs the customer's IT (allowed, nothing changed). Unresolved; the NTP timeout cause is unknown.
- Resolution due time: Hannah Odum's note (2026-11-24 01:30) gives Thu 26 Nov 10:15 AWST. This does not follow policy 4.3 (see Service-level status, which gives about Wed 25 Nov 11:20 AWST). Treat her figure as wrong.

## What has been tried
| When | Who | Action | Result | Cite |
|---|---|---|---|---|
| 2026-11-20 01:05 | Hannah Odum | Checked TernCloud alarm rules for vats 1 to 9 | Same template and recipients; config does not explain difference | Thread 01:05 |
| 2026-11-20 01:10 | Hannah Odum | Asked customer for diagnostic bundles from GW-01 to 03 | Customer attached all three at 05:40 | Thread 01:10, 05:40 |
| 2026-11-20 07:15 | Hannah Odum | Analysed bundles | TS_FUTURE skips, clocks ahead, NTP timeouts | Internal note 07:15 |
| 2026-11-20 07:20 | Hannah Odum | Asked customer IT to check outbound UDP 123 from VLAN 30 | Customer IT: allowed, nothing changed (reported 23 Nov) | Thread 07:20; 2026-11-23 01:40 |
| 2026-11-23 02:15 | Hannah Odum | Raised priority P3 to P2 | Recorded | Event 02:15 |
| 2026-11-23 02:20 | Hannah Odum | Passed the compensation request to Joel Brandt | No response or credit recorded | Thread 02:20 |
| 2026-11-23 02:35 | Hannah Odum | "Force time sync (HTTPS)" to GW-01, 02, 03 | 01, 02 OK; 03 TIME_SET_REJECTED: RTC write error | Note 02:40 |
| 2026-11-23 03:05 | Aroha Ngata | Alarm test on vats 1 to 3 | Vats 1, 2 SMS in a minute; vat 3 nothing | Thread 03:05 |
| 2026-11-24 05:15 | Hannah Odum | Second forced time sync on GW-03 | Same RTC write error | Note 05:20 |
| 2026-11-24 05:17 | Hannah Odum (customer agreed by phone 05:10) | Remote reboot of GW-03 | Online 05:19; clock still about +11 min | Note 05:20 |
| 2026-11-24 06:00 | Hannah Odum | Escalated to Tier 2 | Status Escalated, P2 | Event 06:00 |
| Before 2026-11-23 | Customer IT | Checked VLAN 30 firewall | See above (reported only) | Thread 2026-11-23 01:40 |
| 2026-11-24 | Hannah Odum | Notify Support Team Lead (policy 5.2) | Not recorded | No thread entry |

## Commitments to the customer
| Commitment (verbatim) | Made by (role) | When / cite | Deadline | Kept / Open / Missed |
|---|---|---|---|---|
| "I've passed your request to Joel Brandt, your account manager." | Hannah Odum (Tier 1 agent) | 2026-11-23 02:20 | None stated | Kept as an action, but no reply from Joel or written offer is recorded. Policy 6.3: only the Account Manager or Head of Customer Support may offer a credit; the agent made no offer (6.2 respected). Customer's request is unanswered |
| "I'm going to send a command from TernCloud that sets the clock on GW-01 to 03 over HTTPS" | Hannah Odum | 2026-11-23 02:20 | None stated | Kept (sent 02:35) |
| "I'm escalating this to our Field Systems Engineering team now." | Hannah Odum | 2026-11-24 05:40 | Now | Kept (escalated 06:00) |
| "You'll get an update from us by 17:30 AWST today (09:30 UTC)." | Hannah Odum | 2026-11-24 05:40 | 2026-11-24 09:30 UTC | Open (3h30m left at 06:00). Within 6.1 (time of next update). Tier 2 owns it (5.3) |

## Service-level status
As-of 2026-11-24 06:00 UTC (Tue 14:00 AWST). Plan Business, priority P2.

| Clock | Policy clause (quoted) | Started | Deadline (with arithmetic) | Status |
|---|---|---|---|---|
| First response | 3.1 Business P2: "4 business hours"; 1.4 first contact by an agent | Created 2026-11-19 07:50 UTC (Thu 15:50 AWST, inside 00:30 to 09:30 UTC hours) | Agent reply 2026-11-20 01:05 UTC. Elapsed: Thu 07:50 to 09:30 = 1h40, plus Fri 00:30 to 01:05 = 35m, total 2h15 | Met (also under P3's 9 hours; met either way) |
| Resolution | 3.1 Business P2: "27 business hours"; 4.3 "counted from ticket creation and excluding paused time"; 4.2 paused only while "Pending customer" | Created 2026-11-19 07:50 UTC | Pause 2026-11-20 01:10 to 05:40 UTC = 4h30 (all inside business hours). Used by 06:00 24 Nov: Thu 1h40 + Fri (9h00 minus 4h30 = 4h30) + Mon 9h00 + Tue 00:30 to 06:00 = 5h30, total 20h40. Remaining 27h - 20h40 = 6h20. Tue has 3h30 left (to 09:30 UTC), leaving 2h50 on Wed from 00:30 UTC: due 2026-11-25 03:20 UTC = Wed 11:20 AWST | At risk: 4.4 "less than 25%" = under 6h45; 6h20 remains (23.5%) |
| Customer updates | 7.1 "P2: at least once each business day" | Business-day basis | Updates sent Mon 23 Nov 02:20 UTC and Tue 24 Nov 05:40 UTC; next needed by Wed 25 Nov 09:30 UTC | On track |
| Escalation | 5.1 "when a P1 or P2 ticket is at risk"; 5.2 "the Support Team Lead must be notified at escalation" | Escalated 2026-11-24 06:00 UTC | Notification due at escalation | Escalation done; notification not recorded (see Gaps) |

## Recommended next action
Confirm whether GW-03 has a hardware (RTC) fault, and if so arrange its replacement, within today's business hours. Evidence: GW-03 alone rejects the clock write with "RTC write error" twice (2026-11-23 02:40, 2026-11-24 05:20), remained about +11 min after a reboot, while GW-01 and GW-02 accepted the same command. Take a fresh GW-03 diagnostic bundle and check the RTC error detail; this settles whether swapping the unit (or a workaround that keeps vat 3 alerting) is needed, versus a firmware or configuration cause. The hardware fault is only a Hypothesis, so the confirmation is part of the action. Also check why NTP times out for VLAN 30 (customer IT says UDP 123 is open) because GW-01 and GW-02 may drift again. Deadline it must beat: the update promised by 09:30 UTC today (Tier 2 must send it, with the findings so far), then resolution about 03:20 UTC Wed 25 Nov. The Support Team Lead needs notifying. Do not promise a credit or fix date to the customer (6.2); route the milk-cost request to Joel Brandt.

## Gaps
- Support Team Lead notification (policy 5.2): not recorded. Close by notifying and recording it.
- Joel Brandt's response to the compensation request: nothing recorded. Close with a written decision from the Account Manager or Head of Customer Support (6.3); the customer's request is unanswered.
- Cause of NTP timeouts on VLAN 30: unknown (UDP 123 block is a Hypothesis, denied by customer IT). Close with a packet capture or check of what the other gateways use (VLAN of GW-04 to 09 not recorded).
- Whether clock skew is the actual cause of the skipped rule: Hypothesis; the customer test on vats 1 and 2 is Reported only.
- Whether any gateway besides GW-01 to 03 is affected: GW-04 to 09 last sync OK; Harvey depot gateways were not checked.
- Customer's two missed-alarm events and the 18,000 L loss are Reported only; no TernCloud dashboard or alarm log was read by support.
- Business-hours count assumes no Western Australian public holiday between 19 and 25 Nov (none stated in sources).
- Current priority/SLA assumes P2 per ticket; Hannah Odum's own SLA due time (Thu 26 Nov 10:15 AWST) is inconsistent with policy 4.3 and should be corrected on the ticket.
