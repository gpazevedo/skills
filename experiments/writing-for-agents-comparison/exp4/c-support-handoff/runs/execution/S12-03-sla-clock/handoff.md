# Escalation handoff: TRN-77391 - High-temperature SMS alarms not received from vat gateways (GW-03 still failing)

Customer: Kestrel Dairy Co-operative (KDC-0418) | Tier: Business | Priority: P2 (set 2026-11-23 02:15 UTC by Hannah Odum) | Prepared: 2026-11-24 06:00 UTC (export as-of time)

## Service level
Policy 3.1, Business P2: resolution "27 business hours" (first response 4 business hours). Clock starts at ticket creation and pauses only in "Pending customer" (4.1, 4.2); after a priority change the P2 target is counted from creation (4.3). | Deadline: Wed 2026-11-25 11:20 AWST (03:20 UTC) | Status: At risk, not breached (about 6h20m of 27h remain; under 25% = 6h45m) (4.4)
Arithmetic (business hours 08:30-17:30 AWST, 1.1): created Thu 19 Nov 15:50 AWST (07:50 UTC). Thu 15:50-17:30 = 1h40. Fri 20 Nov full day 9h minus pause Pending customer 01:10-05:40 UTC (Fri 09:10-13:40 AWST, 4h30, all inside business hours) = 4h30. Weekend 0. Mon 23 Nov 9h. Tue 24 Nov 08:30-14:00 AWST (06:00 UTC) = 5h30. Used = 20h40m; remaining 27h - 20h40m = 6h20m, which runs out Tue 17:30 (3h30m) then Wed 08:30 + 2h50m = 11:20 AWST. Assumes no WA public holiday between 19 and 25 Nov; the case does not list any.
Correction: Hannah Odum's internal note (2026-11-24 01:30 UTC) gives "Thu 26 Nov 10:15 AWST, plenty of time". That counts from the priority change, but 4.3 counts from creation. Her due time is wrong by about a day and a half of business time. The ticket is at risk, not comfortable. Policy 5.2 requires the Support Team Lead to be notified when an at-risk P2 is escalated; the thread records no such notification.

## Problem as currently understood
Vat high-temperature SMS alarms do not fire on gateways whose clocks run ahead of sensor timestamps, because their NTP sync fails. The rule engine skips evaluation and the alarm never triggers. GW-01 and GW-02 were fixed by an HTTPS forced time set. GW-03 (vat 3) refuses to set its clock (RTC write error), even after a reboot, so vat 3 still has no working alarm; possible hardware fault. The root cause of the NTP failure on VLAN 30 is not established, so GW-01 and GW-02 may drift again. The customer lost 18,000 L of milk on one missed alarm and is asking for compensation.
- [Reported] Vat 3 over 7C for about 40 min on Tuesday night with no SMS; dashboard shows the reading (Aroha Ngata, 2026-11-19 07:50)
- [Reported] Alarm test: vats 4-9 sent SMS in under a minute, vats 1-3 sent nothing (Aroha Ngata, 2026-11-19 07:50)
- [Verified] Alarm rules for vats 1-9 use the same template and recipients (Hannah Odum, 2026-11-20 01:05)
- [Verified] Bundles from GW-01/02/03: "RULE_EVAL_SKIPPED reason=TS_FUTURE" at every evaluation since 12 Nov; clocks ahead by +9m12s, +8m40s, +11m03s; NTP "sync failed: timeout (pool.terncloud.net:123)" since 12 Nov; all three on VLAN 30 (Hannah Odum, internal note 2026-11-20 07:15)
- [Verified] TernCloud shows GW-04 to 09 last time sync OK (Hannah Odum, 2026-11-20 07:15)
- [Reported] Customer IT says nothing changed on VLAN 30 and outbound UDP 123 is allowed (Aroha Ngata, relaying IT, 2026-11-23 01:40). This conflicts with the NTP timeouts and was not checked by Tern.
- [Reported] Vat 3 over limit again Sunday night at about 01:00 (customer time), about 50 min, 18,000 L dumped (Aroha Ngata, 2026-11-23 01:40)
- [Verified] GW-01 and GW-02 force time sync OK, offset under 1 s; GW-03 "TIME_SET_REJECTED: RTC write error", +11m05s (Hannah Odum, internal note 2026-11-23 02:40)
- [Reported] Alarm test after fix: vats 1 and 2 sent SMS, vat 3 nothing (Aroha Ngata, 2026-11-23 03:05)
- [Verified] Second force sync on GW-03 rejected with the same error; reboot 05:17, online 05:19, clock still +11 min; GW-01/02 still in sync but NTP still failing (Hannah Odum, internal note 2026-11-24 05:20)
- [Reported] Cause of GW-03 fault may be hardware (Hannah Odum's suggestion, 2026-11-24 05:40; not tested)
Support and customer agree on the problem. The customer attributes it to alarms not firing; support attributes it to clock skew from failed NTP.

## What has been tried
1. Checked TernCloud alarm rules for vats 1-9 (identical) - Hannah Odum, 2026-11-20 01:05 - Unknown: ruled out as cause, no change made
2. Customer ran alarm test on all nine vats - Aroha Ngata (Reported), 2026-11-19 - No change (diagnostic only)
3. Requested and analysed diagnostic bundles from GW-01/02/03 - Hannah Odum, 2026-11-20 01:10-07:15 - Partial: found clock skew and NTP failure
4. Asked customer IT to check UDP 123 outbound from VLAN 30 - Hannah Odum, 2026-11-20 07:20; answer 2026-11-23 01:40 (Reported: allowed, nothing changed) - Unknown: firewall not verified by Tern; NTP failure unexplained
5. "Force time sync (HTTPS)" to GW-01/02/03 - Hannah Odum, 2026-11-23 02:35 - Partial: GW-01 and 02 fixed (customer test passed, Reported 03:05); GW-03 rejected
6. Customer alarm test on vats 1-3 - Aroha Ngata (Reported), 2026-11-23 03:05 - Partial: vats 1-2 pass, vat 3 fails
7. Second HTTPS time sync on GW-03 - Hannah Odum, 2026-11-24 05:15 - No change
8. Remote reboot of GW-03 (customer agreed by phone 05:10) - Hannah Odum, 2026-11-24 05:17 - No change
9. Customer's manual hourly dashboard checks as workaround - Aroha Ngata (Reported) - Partial: missed the Sunday event by about 50 min

## Commitments to the customer
- "You'll get an update from us by 17:30 AWST today (09:30 UTC)." - Hannah Odum, 2026-11-24 05:40 UTC - due 2026-11-24 09:30 UTC - open (3h30m left). Policy 5.3 passes this commitment to Tier 2.
- "I've passed your request to Joel Brandt, your account manager." - Hannah Odum, 2026-11-23 02:20 - action already stated as done; the thread has no record of a message to Joel Brandt or any reply - unverified
- "Once that's done, could you run the alarm test..." and "I'm going to send a command from TernCloud..." - Hannah Odum, 2026-11-23 02:20 - done at 02:35 - met
- "I've raised the ticket to P2." - Hannah Odum, 2026-11-23 02:20 - recorded 02:15 - met
- No promise of a fix date, credit, refund or compensation appears in the thread (policy 6.2 forbids it; only Joel Brandt or the Head of Customer Support may offer, in writing, 6.3).
Claimed by customer, not found in thread: none. The customer has requested that the cost of the milk be covered (Aroha Ngata, 2026-11-23 01:40); this is a request, and no response from Joel Brandt or the Head of Customer Support is recorded.

## Open questions
- Why is NTP timing out on VLAN 30 when customer IT says UDP 123 is open? (not checked by Tern; GW-04 to 09 sync fine; the customer's network is unverified)
- Is GW-03 hardware faulty (RTC)? Firmware version and any gateway firmware versions are not in the case.
- Was the Support Team Lead notified at escalation (policy 5.2)? Not recorded.
- Did Joel Brandt receive the compensation request, and what has been said to the customer? Not recorded.
- Exact time of the Sunday vat 3 incident in UTC ("about 01:00 our time" is ambiguous), and whether GW-03 reported the over-limit reading.
- Is there an on-site spare G4-E gateway, and can a replacement reach Brunswick before the deadline? Not in the case.
- Current interim cover for vat 3: only hourly manual checks (Reported); the customer says this is insufficient.
- Any WA public holiday affecting the deadline calculation: none identified in the case.

## Recommended next action
Establish a working alarm path for vat 3 and decide on replacing GW-03: on the TernCloud console for GW-03, check firmware version and RTC state, and arrange a replacement G4-E (or a workaround, such as moving the vat 3 sensor to a spare gateway) for the Brunswick plant, since two forced time sets and a reboot were rejected with RTC write error. Reason: GW-01 and 02 respond to the HTTPS time set and GW-03 does not, which points to hardware. Deadline: send the customer an update by 2026-11-24 09:30 UTC (17:30 AWST) per the open commitment, and have vat 3 resolved by 2026-11-25 03:20 UTC (11:20 AWST) at the latest, the P2 deadline. Follow-ups: (1) notify the Support Team Lead now (policy 5.2) and confirm the compensation request reached Joel Brandt, without promising any credit; (2) find out why NTP fails from VLAN 30 (ask Peter Dunn, IT Coordinator, for a packet capture or firewall log), because GW-01 and 02 may drift again.
