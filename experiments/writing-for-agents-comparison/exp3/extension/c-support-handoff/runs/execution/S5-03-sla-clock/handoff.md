# Escalation handoff: TRN-77391, Kestrel Dairy Co-operative (KDC-0418)

**Summary:** Gateway VAT-GW-03 rejects every attempt to set its clock ("RTC write error"), so the vat 3 high-temperature alarm rule never evaluates and vat 3 has no working SMS alarm. NTP is also still failing on GW-01 to 03. The customer was promised an update by 2026-11-24 09:30 UTC, and the P2 resolution deadline is 2026-11-25 03:20 UTC (11:20 AWST). The ticket is already at risk.
**Reference time:** 2026-11-24 06:00 UTC, Tue 14:00 AWST (latest thread entry)

## Problem as currently understood
The clocks on GW-01 to 03 (VLAN 30, Brunswick) run 8 to 11 minutes fast because NTP sync has failed since 12 Nov. As a result, the 5-minute alarm rule is skipped and no SMS is sent. A forced HTTPS time sync fixed GW-01 and GW-02 for now, but GW-03 refuses the clock write, which may be a hardware fault. The NTP failure itself is unexplained, so GW-01 and GW-02 may drift again.
- [Verified] All nine vats use the same alarm rule template and SMS recipients (Hannah Odum, 2026-11-20 01:05).
- [Verified] GW-01 to 03 have logged "RULE_EVAL_SKIPPED reason=TS_FUTURE" since 12 Nov. Their clock offsets were +9:12, +8:40 and +11:03 (Hannah Odum internal note, 2026-11-20 07:15, from diagnostic bundles).
- [Verified] GW-01 to 03 have logged "NTP sync failed: timeout (pool.terncloud.net:123)" since 12 Nov. All three are on VLAN 30. TernCloud shows GW-04 to 09 time sync OK (same note).
- [Verified] The forced HTTPS sync worked on GW-01 and GW-02 (offset now under 1 s). On GW-03 it failed with "TIME_SET_REJECTED: RTC write error", clock +11:05 (Hannah Odum internal note, 2026-11-23 02:40).
- [Verified] A second sync attempt and a remote reboot of GW-03 failed, and the clock is still +11 min. GW-01 and GW-02 are still in sync, and NTP is still failing on all three (Hannah Odum internal note, 2026-11-24 05:20).
- [Reported] After the sync, the alarm tests on vats 1 and 2 sent SMS within a minute, and vat 3 sent nothing (Aroha Ngata, 2026-11-23 03:05).
- [Reported] Per the customer's IT team, nothing has changed on VLAN 30 and outbound UDP 123 is allowed. This contradicts Tier 1's unconfirmed firewall theory (Aroha Ngata, 2026-11-23 01:40).
- [Reported] Vat 3 went over 7°C with no SMS twice: on Tuesday night (~40 min), and on Sunday at ~01:00 AWST (~50 min). The second incident cost 18,000 L of milk (Aroha Ngata, 2026-11-19 07:50 and 2026-11-23 01:40).

Open questions:
- Is the GW-03 RTC write error a hardware fault (replace the unit), or can it be cleared remotely?
- Why does NTP to pool.terncloud.net:123 time out from VLAN 30 when the customer says UDP 123 is allowed? Possible causes are DNS, an upstream filter, or something that changed on 12 Nov. The network contact is Peter Dunn, IT Coordinator (account record).
- Is there an interim way to alarm on vat 3 while GW-03's clock is wrong?

## Tried so far
- Alarm config check across vats 1 to 9, by Hannah Odum, 2026-11-20 01:05: identical rules, so config does not explain the fault.
- Alarm test on all nine vats, by the customer, 2026-11-19: vats 4 to 9 sent SMS, vats 1 to 3 sent nothing (Reported).
- Diagnostic bundles from GW-01 to 03, collected by the customer and analysed by Hannah Odum, 2026-11-20 05:40 to 07:15: found the clock offset and NTP timeouts.
- Firewall check for outbound UDP 123 on VLAN 30, by the customer's IT team, reported 2026-11-23 01:40: allowed, nothing changed (Reported).
- "Force time sync (HTTPS)" on GW-01 to 03, by Hannah Odum, 2026-11-23 02:35: OK on 01 and 02, RTC write error on 03.
- Alarm retest on vats 1 to 3, by the customer, 2026-11-23 03:05: vats 1 and 2 work, vat 3 does not (Reported).
- Second HTTPS time sync on GW-03, by Hannah Odum, 2026-11-24 05:15: same RTC write error.
- Remote reboot of GW-03 (customer agreed by phone at 05:10), by Hannah Odum, 2026-11-24 05:17: back online at 05:19, clock still +11 min.

## Commitments to the customer
Under policy 5.3, Tier 2 now owns all of these.
- "You'll get an update from us by 17:30 AWST today (09:30 UTC)", Hannah Odum, 2026-11-24 05:40: **outstanding**, due 2026-11-24 09:30 UTC (3 h 30 min after reference time).
- "I'm escalating this to our Field Systems Engineering team now", Hannah Odum, 2026-11-24 05:40: met (escalation event 06:00).
- "I'm going to send a command from TernCloud that sets the clock on GW-01 to 03 over HTTPS", Hannah Odum, 2026-11-23 02:20: met (sent 02:35).
- "I've passed your request to Joel Brandt, your account manager", Hannah Odum, 2026-11-23 02:20: unclear. The thread records no handoff and no reply from Joel Brandt.
  - Background: the customer asked "We'd like the cost of that milk covered" (Aroha Ngata, 2026-11-23 01:40).
  - No compensation has been offered. Only the Account Manager or the Head of Customer Support may offer it (policy 6.3).
  - The account record shows no open credits.

## Service level
- Tier: Business (account record) | Priority: P2 (ticket, set by Hannah Odum 2026-11-23 02:15 under clause 2.2; was P3)
- Target: resolution in 27 business hours. On a priority change, the target is counted from ticket creation, excluding paused time (policy 3.1, 4.1 to 4.3). First response target: met, after 2 h 15 min of business time (2026-11-20 01:05).
- Deadline: **2026-11-25 03:20 UTC (Wed 11:20 AWST)**. Business hours are 00:30 to 09:30 UTC (policy 1.2). Business time counted:
  - Thu 19 Nov 07:50 to 09:30 = 1 h 40 min
  - Fri 20 Nov 00:30 to 01:10 = 0 h 40 min, then paused while Pending customer from 01:10 to 05:40, then 05:40 to 09:30 = 3 h 50 min
  - Mon 23 Nov = 9 h
  - Tue 24 Nov = 9 h
  - Running total at close of Tue 24 Nov: 24 h 10 min
  - The remaining 2 h 50 min runs from 00:30 Wed 25 Nov, ending 03:20 UTC.
  - This assumes no WA public holiday falls between 19 and 25 Nov. The policy does not list holidays.
- Conflict: Hannah Odum's internal note (2026-11-24 01:30) gives Thu 26 Nov 10:15 AWST, counted from the priority change. Policy 4.3 counts from creation, and the policy governs.
- Status: open, 6 h 20 min business time remaining at reference time (20 h 40 min of 27 h used).
  - The ticket is **at risk** under policy 4.4: less than 25% (6 h 45 min) of the target remains. It became at risk at about 05:35 UTC on 24 Nov, before the 06:00 escalation.
  - Under policy 5.2, the Support Team Lead must be notified at escalation. The thread does not record that notification.
- Customer updates: P2 requires at least one update each business day (policy 7.1).

## Recommended next action
Diagnose the GW-03 "TIME_SET_REJECTED: RTC write error" with Tier 2 tooling. If it cannot be cleared remotely, start replacing GW-03. The evidence: the HTTPS sync, a retry and a reboot all failed on GW-03 while the same command fixed GW-01 and GW-02. That points to the GW-03 unit, not the network, and vat 3 currently has no working alarm. Serves: the 2026-11-25 03:20 UTC resolution deadline. Investigate the NTP failure on VLAN 30 (with Peter Dunn) next, because GW-01 and GW-02 can drift again.
Tell the customer by **2026-11-24 09:30 UTC (17:30 AWST)**:
- Tier 2 now has the case.
- Vat 3's alarm is still not working, so vat 3 needs manual checks until GW-03 is fixed or replaced.
- Give the GW-03 plan and next update time. Do not promise a fix date or compensation (policy 6.2).
- The compensation request sits with Joel Brandt.
