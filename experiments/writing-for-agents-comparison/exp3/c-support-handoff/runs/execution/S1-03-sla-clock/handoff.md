# Escalation handoff: TRN-77391 - VAT-GW-03 clock will not set, so vat 3 high-temp SMS alarm never fires

Customer: Kestrel Dairy Co-operative (KDC-0418) | Tier: Business (account record) | Priority: P2 (set on ticket by Hannah Odum, 2026-11-23 02:15 UTC) | Prepared: as at 2026-11-24 06:00 UTC (escalation event, last entry in the thread); the actual current time is not determinable from the supplied material

## Service level
Policy 3.1, Business P2: "4 business hours" first response, "27 business hours" resolution | Resolution deadline: Wed 25 Nov 2026 03:20 UTC (11:20 AWST) | Status at 2026-11-24 06:00 UTC: Within target: 6 h 20 min business time remaining, which policy 4.4 classes as "at risk" (under 25% of 27 h = 6 h 45 min). Status now: fill in at the current time.
Arithmetic: business hours are 00:30-09:30 UTC Mon-Fri (policy 1.1, 1.2). Per 4.3 the P2 target counts from ticket creation (Thu 19 Nov 07:50 UTC), excluding the Pending customer pause (Fri 20 Nov 01:10-05:40 UTC, policy 4.2). Thu 1 h 40 + Fri 4 h 30 + Mon 9 h + Tue 9 h = 24 h 10; remaining 2 h 50 from Wed 00:30 UTC = 03:20 UTC. Elapsed at 06:00 UTC Tue = 20 h 40; the ticket became at risk at 05:35 UTC Tue. Assumes no WA public holiday 19-25 Nov (the supplied material lists none; confirm).
- First response: Met. Hannah Odum's reply at 2026-11-20 01:05 UTC came 2 h 15 min business time after creation (inside both the P3 9 h and P2 4 h targets).
- Hannah's internal note (2026-11-24 01:30 UTC) gives a due time of "Thu 26 Nov 10:15 AWST", counted from the P2 change. That conflicts with policy 4.3 (count from creation); use Wed 25 Nov 03:20 UTC.
- Policy 5.2: an at-risk P2 escalation requires the Support Team Lead to be notified at escalation. The thread does not record that notification.
- Policy 7.1: P2 needs a customer update at least once each business day; from escalation Tier 2 owns updates and existing commitments (5.3).

## Problem as currently understood
VAT-GW-03 (vat 3, Brunswick plant) has a clock about 11 minutes fast, so its rule engine skips the 5-minute high-temperature rule and vat 3 sends no SMS alarm. Forcing the time over HTTPS fails on GW-03 with an RTC write error, and a remote reboot did not help; Tier 1 suspects a hardware fault (not confirmed). Separately, NTP still fails on GW-01, 02 and 03 (all on VLAN 30), so GW-01 and GW-02, corrected by a forced sync, may drift again; the cause of the NTP failure is not known, and the customer's IT says UDP 123 is allowed. Vat 3 currently has no working alarm and the customer reports a product loss while relying on hourly manual checks.
- [Verified] Vats 1-9 use the same alarm rule template ("Vat high temp, above 7°C for 5 min") and the same SMS recipients (Hannah Odum, 2026-11-20 01:05 UTC)
- [Verified] Diagnostic bundles: GW-01 to 03 log "RULE_EVAL_SKIPPED reason=TS_FUTURE" at every evaluation since 12 Nov; clocks ahead by GW-01 +9 min 12 s, GW-02 +8 min 40 s, GW-03 +11 min 03 s (Hannah Odum internal note, 2026-11-20 07:15 UTC)
- [Verified] NTP log on all three: "NTP sync failed: timeout (pool.terncloud.net:123)" since 12 Nov; bundles put GW-01 to 03 on VLAN 30; TernCloud shows GW-04 to 09 last time sync OK (Hannah Odum internal note, 2026-11-20 07:15 UTC). Her cause "UDP 123 blocked for VLAN 30" is marked "Not confirmed".
- [Reported] Customer IT says nothing changed on VLAN 30 and outbound UDP 123 is allowed (Aroha Ngata relaying IT, 2026-11-23 01:40 UTC)
- [Verified] Forced HTTPS sync at 02:35: GW-01 and GW-02 OK, offset under 1 s; GW-03 "TIME_SET_REJECTED: RTC write error", clock still +11 min 05 s (Hannah Odum internal note, 2026-11-23 02:40 UTC)
- [Reported] Alarm test after sync: vats 1 and 2 sent SMS within a minute, vat 3 nothing (Aroha Ngata, 2026-11-23 03:05 UTC)
- [Verified] Second forced sync to GW-03 rejected with the same error; reboot at 05:17, back online 05:19, clock still +11 min; GW-01 and 02 still in sync; NTP still failing on all three (Hannah Odum internal note, 2026-11-24 05:20 UTC)
- [Reported] Possible hardware fault on GW-03 (Hannah Odum, 2026-11-24 05:40 UTC; hypothesis, not checked)
- [Reported] Tuesday night (17 Nov) vat 3 was above 7°C for about 40 min with no SMS; dashboard showed the reading over the limit (Aroha Ngata, 2026-11-19 07:50 UTC)
- [Reported] Initial test: vats 4-9 sent SMS within a minute, vats 1-3 nothing (Aroha Ngata, 2026-11-19 07:50 UTC)
- [Reported] Sunday night vat 3 went over 7°C at about 01:00 local time, no SMS, caught on the hourly check after about 50 min; 18,000 litres dumped; hourly checks are not sustainable or sufficient (Aroha Ngata, 2026-11-23 01:40 UTC)

## What has been tried
1. Alarm test on all nine vats - Aroha Ngata (customer), 2026-11-19 (Reported) - Unknown as a fix (diagnostic): vats 4-9 alarmed, 1-3 did not
2. Checked TernCloud alarm rule configuration for vats 1-9 - Hannah Odum, 2026-11-20 01:05 UTC - No change: configuration identical, ruled out as the cause
3. Collected and analysed diagnostic bundles from GW-01 to 03 - Hannah Odum (bundles from Aroha 05:40), 2026-11-20 07:15 UTC - No change: found clock skew, TS_FUTURE skips and NTP timeouts
4. Customer IT checked outbound UDP 123 from VLAN 30 - Aroha Ngata relaying IT, 2026-11-23 01:40 UTC (Reported) - No change: reported allowed and unchanged; NTP still failing (Hannah, 2026-11-24 05:20 UTC)
5. "Force time sync (HTTPS)" to GW-01, 02, 03 - Hannah Odum, 2026-11-23 02:35 UTC - Partial: GW-01 and 02 clocks corrected and vats 1 and 2 alarm on test; GW-03 rejected (RTC write error)
6. Second "Force time sync (HTTPS)" to GW-03 - Hannah Odum, 2026-11-24 05:15 UTC - No change: same RTC write error
7. Remote reboot of GW-03 from TernCloud (customer agreed by phone at 05:10) - Hannah Odum, 2026-11-24 05:17 UTC - No change: clock still +11 min
8. Compensation request passed to Joel Brandt (Account Manager) - Hannah Odum, 2026-11-23 02:20 UTC - Unknown: no result recorded

## Commitments to the customer
- "I'm going to send a command from TernCloud that sets the clock on GW-01 to 03 over HTTPS" - Hannah Odum, 2026-11-23 02:20 UTC - due none stated - met (sent 02:35 UTC)
- "I've passed your request to Joel Brandt, your account manager." - Hannah Odum, 2026-11-23 02:20 UTC - due none stated - met as stated; no reply from Joel Brandt recorded. No compensation was offered ("I'm not able to offer compensation myself"); per policy 6.3 only the Account Manager or Head of Customer Support can offer it, in writing.
- "I'm escalating this to our Field Systems Engineering team now." - Hannah Odum, 2026-11-24 05:40 UTC - due now - met (escalated 06:00 UTC)
- "You'll get an update from us by 17:30 AWST today (09:30 UTC)." - Hannah Odum, 2026-11-24 05:40 UTC - due 2026-11-24 09:30 UTC - open at 06:00 UTC; now owned by Tier 2 (policy 5.3)
- Not a commitment, but relevant: "No rush before Monday; the hourly checks cover you over the weekend." (Hannah Odum, 2026-11-20 07:20 UTC); the customer reports the hourly checks failed to prevent the Sunday loss.
Claimed by customer, not found in thread: none. (The customer requests that the cost of the milk be covered, Aroha Ngata, 2026-11-23 01:40 UTC; that is a request, not a claimed promise.)

## Open questions
- What exactly fails on GW-03's RTC: firmware version, RTC hardware status, any further error detail beyond "RTC write error"? The thread has no GW-03 firmware or hardware data.
- What changed around 12 Nov, when the NTP failures and TS_FUTURE skips began on GW-01 to 03?
- Why does NTP to pool.terncloud.net:123 time out from VLAN 30 if IT says UDP 123 is allowed (for example DNS resolution or return traffic from VLAN 30)? Peter Dunn (IT Coordinator, network contact) has not been involved in the thread.
- Is there any interim alarm cover for vat 3 other than the hourly manual checks?
- Are the Harvey depot gateways (DEP-GW-01, DEP-GW-02) affected? The thread does not mention them.
- Was the Support Team Lead notified at escalation (policy 5.2)?
- Has Joel Brandt responded to the compensation request?

## Recommended next action
Investigate the RTC write failure on VAT-GW-03 (pull a fresh diagnostic bundle or RTC/system logs from it and check its firmware and hardware state) and decide between a firmware fix and replacing the gateway, because vat 3 is the only vat still without an alarm, every software-side attempt (two forced syncs and a reboot) failed at the RTC write, and the customer has already lost product. Send Aroha Ngata the promised update with your plan by 2026-11-24 09:30 UTC; the resolution deadline is 2026-11-25 03:20 UTC, and the ticket is already at risk.
Follow-ups: (1) Resolution under policy 1.5 also needs the VLAN 30 NTP failure fixed, since GW-01 and 02 may drift again; work it with Peter Dunn. (2) Notify the Support Team Lead if not already done (policy 5.2).
