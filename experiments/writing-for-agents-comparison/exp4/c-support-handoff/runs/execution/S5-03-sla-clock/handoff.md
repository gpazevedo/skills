# Handoff: TRN-77391, High-temperature SMS alarms not received from some vat gateways (Kestrel Dairy Co-operative, KDC-0418)

## Problem
- [Reported] High-temperature SMS alarms did not fire for vats 1, 2 and 3 at Brunswick plant in the customer's all-vat test on 19 Nov; vats 4 to 9 sent SMS within a minute. Each vat has its own gateway (VAT-GW-01 to 09).
- [Verified: account record] Brunswick has VAT-GW-01 to 09, model G4-E, one per vat; alarm delivery is TernCloud SMS to the plant on-call roster.
- [Verified: Hannah Odum's rule check, 20 Nov 01:05 UTC] Vats 1 to 9 use the same rule template ("Vat high temp, above 7°C for 5 min") and the same SMS recipients, so configuration does not explain the difference.
- [Verified: diagnostic bundles, internal note 20 Nov 07:15 UTC] GW-01, 02, 03 log "RULE_EVAL_SKIPPED reason=TS_FUTURE" at every evaluation since 12 Nov. Gateway clocks were ahead of sensor timestamps (GW-01 +9 min 12 s, GW-02 +8 min 40 s, GW-03 +11 min 03 s), so the 5-minute window never fills.
- [Verified: bundles] NTP log on all three: "NTP sync failed: timeout (pool.terncloud.net:123)" since 12 Nov. GW-01 to 03 are on VLAN 30.
- [Verified: TernCloud, per 20 Nov note] GW-04 to 09 show last time sync OK. Whether they are on a different VLAN is not stated.
- [Reported] Missed alarms: vat 3 over 7°C for about 40 minutes "on Tuesday night" (17 Nov); again about 01:00 customer time Sunday night (22/23 Nov), over limit about 50 minutes before the night operator caught it on the hourly check, 18,000 litres dumped. Customer asks for the milk cost to be covered. No support-side source confirms the loss or the durations.
- [Verified: TernCloud command results, 23 Nov 02:40 UTC] "Force time sync (HTTPS)" fixed GW-01 and GW-02 (offset under 1 s). GW-03 returned "TIME_SET_REJECTED: RTC write error", clock still +11 min 05 s.
- [Verified: internal note 24 Nov 05:20 UTC] A second HTTPS time sync on GW-03 gave the same RTC write error. After a remote reboot (05:17, back 05:19) the clock is still about +11 min. GW-01 and 02 are still in sync, but NTP still fails on all three.
- [Reported] After the first sync, vats 1 and 2 sent SMS within a minute on test; vat 3 sent nothing (customer, 23 Nov 03:05 UTC).
- [Reported] Customer's IT says nothing changed on VLAN 30 and outbound UDP 123 is allowed (23 Nov 01:40 UTC). CONFLICT: Tier 1's hypothesis was UDP 123 blocked for VLAN 30 ("Not confirmed"). The NTP timeouts are verified; the cause is not.
- [Reported] Night staff are doing hourly dashboard checks as the interim measure.

## Open questions
1. Why does NTP time out from VLAN 30 if UDP 123 is allowed? Verify: packet capture or firewall log for UDP 123 to pool.terncloud.net from VLAN 30; ask Peter Dunn (IT Coordinator) for the firewall rule evidence, not just the statement. Also check whether pool.terncloud.net resolves from VLAN 30 (DNS) and whether GW-04 to 09 are on VLAN 30.
2. Is GW-03 an RTC hardware fault? "RTC write error" persisting after reboot suggests it, but this is unconfirmed. Verify: Tier 2 review of the GW-03 bundle and RTC logs, and firmware version versus GW-01 and 02.
3. Will GW-01 and 02 drift again while NTP fails? Unverified. Verify: check their offsets daily, and fix NTP.
4. Was the 22/23 Nov vat 3 loss (18,000 L, ~50 min) real as described? Reported only. Compensation is outside Tier 1 and 2 authority (policy 6.3).
5. Has Joel Brandt received and acknowledged the compensation request? Hannah said she passed it on; there is no ticket event or reply showing this.
6. Was the Support Team Lead notified at escalation (policy 5.2, at-risk P2)? No notification is recorded in the thread.

## Attempts
1. Checked TernCloud alarm rules for vats 1 to 9, by Hannah Odum, 20 Nov 01:05 UTC. Result: identical rule and recipients, so config ruled out.
2. Asked the customer for diagnostic bundles from GW-01 to 03, by Hannah, 20 Nov 01:10 UTC (status Pending customer). Result: worked; customer supplied all three at 05:40 UTC.
3. Analysed the bundles, by Hannah, 20 Nov 07:15 UTC. Result: found the clock skew and NTP failures (see Problem).
4. Asked customer IT to check outbound UDP 123 from VLAN 30, by Hannah, 20 Nov 07:20 UTC. Result: customer IT says it is allowed and nothing changed (reported). Not independently confirmed.
5. Raised priority P3 to P2, by Hannah, 23 Nov 02:15 UTC. Result: done, recorded on the ticket.
6. Passed the compensation request to Joel Brandt, by Hannah, 23 Nov 02:20 UTC. Result: unknown, no response recorded.
7. "Force time sync (HTTPS)" to GW-01, 02, 03, by Hannah, 23 Nov 02:35 UTC. Result: worked for GW-01 and 02; failed for GW-03 (RTC write error). Customer test: vats 1 and 2 alarmed, vat 3 did not (reported).
8. Second "Force time sync (HTTPS)" to GW-03, 24 Nov 05:15 UTC, by Hannah. Result: failed, same error.
9. Remote reboot of GW-03 with Aroha's phone agreement at 05:10, by Hannah, 24 Nov 05:17 UTC. Result: rebooted, back at 05:19, clock still +11 min, so the fault is not fixed.
10. Escalated to Tier 2 (Field Systems Engineering), by Hannah, 24 Nov 06:00 UTC. Result: done, status Escalated, P2.

## Commitments to the customer
| Commitment | Made by | When | Quote |
| --- | --- | --- | --- |
| Update to customer by 17:30 AWST (09:30 UTC) on 24 Nov. Open; Tier 2 owns it under policy 5.3 | Hannah Odum, Support Agent (Tier 1) | 2026-11-24 05:40 UTC | "You'll get an update from us by 17:30 AWST today (09:30 UTC)." |
| Request for milk compensation passed to the Account Manager (action stated as done; outcome open, no credit or compensation offered) | Hannah Odum, Support Agent (Tier 1) | 2026-11-23 02:20 UTC | "I'm not able to offer compensation myself, so I've passed your request to Joel Brandt, your account manager." |

No fix date, credit, refund or compensation has been promised. The account record shows no open credits. Earlier commitments (set priority to P2; send the time-sync command) were fulfilled on 23 Nov.

## Service level
Term: Business plan, P2: first response "4 business hours"; resolution "27 business hours" (policy 3.1; plan from account record, priority P2 set 23 Nov 02:15 UTC and recorded on the ticket, clause 2.5). A multi-fault ticket resolves only when every fault is resolved (1.5).
Clock start: ticket creation, 2026-11-19 07:50 UTC = Thu 19 Nov 15:50 AWST (clause 4.1). Counted from creation under the P2 target even though the ticket was P3 until 23 Nov (clause 4.3).
Pause: "Pending customer" from 20 Nov 01:10 to 05:40 UTC (4.5 business hours, 09:10 to 13:40 AWST Fri), paused per 4.2. No other pauses are recorded.
Deadline: resolution due Wed 25 Nov 2026 11:20 AWST (03:20 UTC). Working: Thu 1h40 + Fri 9h - 4.5h pause + Mon 9h + Tue 9h = 24h10m by close Tue, so 2h50m more from 08:30 on Wed. No WA public holiday is assumed in this period; not checked in the inputs.
First response: met. 20 Nov 01:05 UTC (09:05 AWST) was about 2h15m of business time after creation, within 4 business hours (clause 1.4).
Status as of 2026-11-24 06:00 UTC (14:00 AWST Tue): about 20h40m of 27h used, about 6h20m remaining (about 23.5% of the target). That is below 25%, so the ticket is AT RISK (clause 4.4), not yet breached.
CONFLICT: Hannah's 24 Nov 01:30 UTC note gives the due time as Thu 26 Nov 10:15 AWST, counting 27 hours from the P2 change. That is wrong under clause 4.3; use Wed 25 Nov 11:20 AWST. Customer update cadence: P2 needs an update at least each business day (7.1).

## Recommended next action
Action: Tier 2 takes ownership now and gets vat 3 alarming. Treat GW-03 as a probable RTC fault: review its bundle and firmware, and if the RTC fault is confirmed, arrange replacement or on-site repair of the VAT-GW-03 gateway, with a stopgap for vat 3 if the swap cannot be done before the deadline.
Reason: the HTTPS time set and reboot both failed with the same RTC error on GW-03, while the identical command worked on GW-01 and 02, which points at the device. Vat 3 is the vat that caused the product loss.
Must satisfy:
- Send the customer update before 09:30 UTC (17:30 AWST) today (open commitment). It should also cover the next step and when the next update comes (6.1).
- Resolve before Wed 25 Nov 11:20 AWST (03:20 UTC). Resolution needs vat 3 fixed and the alarm test passed. The NTP failure on GW-01 to 03 should be fixed or clearly handled, since 01 and 02 may drift again.
- Notify the Support Team Lead now (5.2, at-risk P2), and record it on the ticket.
- Confirm in writing on the ticket that Joel Brandt has the compensation request. Do not say anything on credit or compensation to the customer (6.2, 6.3).
Assumptions and checks:
- GW-03 is a hardware (RTC) fault. Check: Tier 2 bundle review. If it is firmware or config, a firmware or config fix replaces the swap.
- Vats 1 and 2 remain working only while their clocks hold. Check: their offsets and a repeat alarm test, until NTP is fixed.
- The UDP 123 claim from customer IT is accurate. Check: firewall evidence from Peter Dunn.
- Any stopgap for vat 3 (for example reconnecting its sensor elsewhere) is feasible. Not established in the thread; check with the customer's engineer.
