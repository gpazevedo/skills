# Escalation handoff: TRN-77391, Kestrel Dairy Co-operative (KDC-0418)

**Summary:** High-temperature SMS alarms do not fire for vat 3 (VAT-GW-03), whose clock is about 11 min fast and cannot be set; the ticket is at risk on its resolution target, due Wed 25 Nov 2026 11:20 AWST (03:20 UTC), and a customer update is due today 09:30 UTC.
**Reference time:** 2026-11-24 06:00 UTC, 14:00 AWST (latest thread entry; the export states it is the as-of time)

## Problem as currently understood
Alarm rules on VAT-GW-01 to 03 skip evaluation because the gateway clocks run ahead of sensor timestamps, after NTP stopped syncing on 12 Nov. A forced HTTPS time sync fixed GW-01 and GW-02 but GW-03 rejects the clock write twice, even after a reboot, so vat 3 still has no SMS alarm, and a possible RTC hardware fault is suspected. The cause of the NTP failure on VLAN 30 is unconfirmed, so GW-01 and GW-02 may drift again.
- [Verified] Rule engine logs "RULE_EVAL_SKIPPED reason=TS_FUTURE" at every evaluation since 12 Nov on GW-01 to 03 (Hannah Odum internal note, 2026-11-20 07:15)
- [Verified] Clocks ahead on 20 Nov: GW-01 +9 min 12 s, GW-02 +8 min 40 s, GW-03 +11 min 03 s; NTP log "sync failed: timeout (pool.terncloud.net:123)" since 12 Nov (same note)
- [Verified] GW-04 to 09 show last time sync OK in TernCloud; GW-01 to 03 are on VLAN 30 (same note)
- [Verified] Alarm rules for vats 1 to 9 use the same template and recipients (Hannah Odum, 2026-11-20 01:05)
- [Verified] After HTTPS force sync, GW-01 and GW-02 offset under 1 s; GW-03 "TIME_SET_REJECTED: RTC write error" on 23 Nov 02:35 and again 24 Nov 05:15; after reboot at 05:17 clock still +11 min (internal notes 2026-11-23 02:40, 2026-11-24 05:20)
- [Verified] NTP still failing on all three as of 24 Nov (internal note, 2026-11-24 05:20)
- [Reported] After sync, vats 1 and 2 sent SMS within a minute, vat 3 nothing (Aroha Ngata, 2026-11-23 03:05; test result, no support check recorded)
- [Reported] Customer IT says nothing changed on VLAN 30 and outbound UDP 123 is allowed (Aroha Ngata, 2026-11-23 01:40; not checked by support)
- [Reported] Vat 3 over 7°C for about 50 min on Sunday night, 18,000 litres of milk dumped; earlier event about 40 min on the Tuesday night before 19 Nov (Aroha Ngata, 2026-11-23 01:40 and 2026-11-19 07:50)
- [Reported] Night staff doing hourly dashboard checks as workaround; customer says this is not sustainable (Aroha Ngata, 2026-11-23 01:40)
Open questions:
- Is GW-03 an RTC hardware fault, or something else (firmware, config)? Only the error text suggests hardware; "may be a hardware fault" is Hannah's inference.
- Why does NTP fail on GW-01 to 03 only? UDP 123 on VLAN 30 is unconfirmed; the customer says it is open, which conflicts with the log timeouts. Peter Dunn (IT Coordinator, account record) has not been contacted directly.
- Will GW-01 and GW-02 drift again, and how fast?
- Do vats 1 and 2 alarms still work now (last test 23 Nov 03:05)?

## Tried so far
- Checked alarm rule configuration for vats 1 to 9, by Hannah Odum, 2026-11-20 01:05: identical, no difference found
- Downloaded diagnostic bundles from GW-01 to 03, by Aroha Ngata, 2026-11-20 05:40: bundles attached; analysis in the 07:15 note
- Asked customer IT to check outbound UDP 123 from VLAN 30, by Hannah Odum, 2026-11-20 07:20: customer reports it is allowed (Reported); no support check recorded
- "Force time sync (HTTPS)" to GW-01 to 03, by Hannah Odum, 2026-11-23 02:35: GW-01 and 02 OK; GW-03 rejected with RTC write error
- Alarm test on vats 1 to 3, by Aroha Ngata, 2026-11-23 03:05: vats 1 and 2 pass, vat 3 fails (Reported)
- Second force sync to GW-03, by Hannah Odum, 2026-11-24 05:15: same RTC write error
- Remote reboot of GW-03 (customer agreed by phone 05:10), by Hannah Odum, 2026-11-24 05:17: back online 05:19, clock still +11 min
- Alarm test on vat 3 after the second sync and reboot: result not recorded

## Commitments to the customer
- "You'll get an update from us by 17:30 AWST today (09:30 UTC).", Hannah Odum, 2026-11-24 05:40: outstanding, 3.5 h left at reference time; Tier 2 now owns it (policy 5.3)
- "I've passed your request to Joel Brandt, your account manager.", Hannah Odum, 2026-11-23 02:20: unclear, no entry shows the request reached Joel or that he replied; no offer of compensation is recorded on the ticket or in the account record (policy 6.3), and none can be assumed
- "I'm going to send a command from TernCloud that sets the clock on GW-01 to 03 over HTTPS", Hannah Odum, 2026-11-23 02:20: met (sent 02:35)
- "No rush before Monday; the hourly checks cover you over the weekend.", Hannah Odum, 2026-11-20 07:20: not a commitment (reassurance); note the customer later reported that hourly checks were not sufficient
- Claimed by customer, not found in thread: none

## Service level
- Tier: Business (account record) | Priority: P2 (ticket, set by Hannah Odum 2026-11-23 02:15, policy 2.2 cited)
- Target: resolution 27 business hours (policy 3.1, Business P2); counted from ticket creation on the new priority, excluding paused time (4.3). Resolution needs every fault resolved (1.5), so GW-03 and the vat 3 alarm gap keep it open.
- Deadline: Wed 25 Nov 2026 11:20 AWST (03:20 UTC). Calculation (policy 1.1, 4.1 to 4.3): created Thu 19 Nov 15:50 AWST = 1 h 40 min to 17:30; Fri 20 Nov 9 h minus pause (Pending customer 20 Nov 01:10 to 05:40 UTC = 4 h 30 min, all inside business hours) = 4 h 30 min; Mon 23 Nov 9 h; Tue 24 Nov 9 h; total 24 h 10 min by end of Tue; remaining 2 h 50 min after 08:30 Wed gives 11:20 AWST. No WA public holiday assumed in this period.
- Status: at risk, not breached. At 14:00 AWST Tue, 20 h 40 min used, 6 h 20 min remaining, less than 25% of 27 h (6 h 45 min) (policy 4.4).
- Disagreement: Hannah's note (2026-11-24 01:30) gives Thu 26 Nov 10:15 AWST, counting from the priority change and ignoring the pause. Policy 4.3 governs; her due time is about 1 business day too late and "plenty of time" is wrong.
- Update obligation: P2 needs an update at least each business day (policy 7.1); today's is promised for 09:30 UTC.
- Escalation (5.2): an at-risk P2 escalation requires notifying the Support Team Lead; no notification is recorded in the thread. Not determinable whether it was done outside the ticket.

## Recommended next action
Confirm GW-03's RTC fault from a fresh diagnostic bundle and, if confirmed, arrange a replacement G4-E gateway for vat 3 (swap, then re-run the alarm test on vat 3), because two force syncs and a reboot all gave the same RTC write error. Serves: resolution deadline Wed 25 Nov 11:20 AWST and the 09:30 UTC update today. Notify the Support Team Lead now (policy 5.2) and ask Peter Dunn to confirm UDP 123 from VLAN 30 so GW-01 and GW-02 do not drift.
Tell the customer: by 09:30 UTC today, say that GW-03 still cannot set its clock, that vat 3 has no working SMS alarm until it is replaced or fixed, what the next step and next update time are, and that the compensation request is with Joel Brandt. Do not promise a fix date, credit, refund or compensation (policy 6.2, 6.3); tell Joel directly and record it on the ticket.
