Clarifying question: What is the current date and time? The environment clock reads 2026-11-21 15:26 UTC, which is earlier than the last thread entry (2026-11-24 06:00 UTC), so it cannot be the as-of time. Deadlines below are computed; statuses are left not computed.

## Escalation handoff: TRN-77391 High-temp SMS alarm not raised for vat 3 (GW-03 clock 11 min fast, will not set)
As of: not known (environment clock 2026-11-21 15:26 UTC predates the thread; see Clarifying question). Thread ends 2026-11-24 06:00 UTC (14:00 AWST), at escalation.
Customer: Kestrel Dairy Co-operative (KDC-0418), Business support plan, TernCloud Site subscription. Brunswick processing plant, VAT-GW-01 to VAT-GW-09, model G4-E (Ethernet), one per milk vat; SMS alarms to plant on-call roster. Contacts: Aroha Ngata (Plant Engineer, primary technical), Peter Dunn (IT Coordinator, network). Account Manager: Joel Brandt. (account record)

### Problem as currently understood
High-temperature SMS alarms were not raised for vats 1 to 3 because the rule engine on GW-01 to 03 skips every evaluation when the gateway clock is ahead of the sensor timestamps, and the clocks drifted because NTP has failed since 12 Nov. A forced HTTPS time sync fixed GW-01 and GW-02, but GW-03 rejects any clock write ("RTC write error") and stays about 11 minutes fast, so vat 3 still has no alarm. Confidence is high on the mechanism (logs) and low on why GW-03 rejects the write (possible hardware fault, Tier 1 opinion) and why NTP fails (cause not found).
Evidence:
- [Verified] All nine vats use the same rule template ("Vat high temp, above 7°C for 5 min") and SMS recipients (Hannah Odum, TernCloud check, 20 Nov 01:05 UTC)
- [Verified] GW-01 to 03 log "RULE_EVAL_SKIPPED reason=TS_FUTURE" at every evaluation since 12 Nov; clocks ahead by 9:12, 8:40, 11:03; "NTP sync failed: timeout (pool.terncloud.net:123)" since 12 Nov; all three on VLAN 30 (Hannah Odum, diagnostic bundles, 20 Nov 07:15 UTC)
- [Verified] GW-04 to 09 show last time sync OK (Hannah Odum, TernCloud, 20 Nov 07:15 UTC)
- [Verified] GW-03 rejects time set ("TIME_SET_REJECTED: RTC write error") twice and after a reboot; still +11 min. GW-01/02 offset under 1 s, but NTP still failing on all three, so they may drift again (Hannah Odum, TernCloud, 23 Nov 02:40 and 24 Nov 05:20 UTC)
- [Reported] Vat 3 exceeded 7°C for about 40 min (Tue 17 Nov) and about 50 min (Sun 22 Nov) with no SMS; 18,000 L dumped after the second (Aroha Ngata)
- [Reported] Alarm test: vats 4 to 9 sent SMS, vats 1 to 3 did not (19 Nov); after the sync vats 1 and 2 sent SMS, vat 3 did not (23 Nov) (Aroha Ngata)
- [Reported] Outbound UDP 123 is allowed from VLAN 30 and nothing has changed (customer IT, via Aroha Ngata). Contradicts Tier 1's unconfirmed hypothesis that UDP 123 is blocked for VLAN 30; neither is confirmed.
- [Reported] Hourly manual dashboard checks are not enough and staff cannot sustain them (Aroha Ngata)

### Tried so far
- 20 Nov Hannah Odum: compared alarm rules for vats 1 to 9 → identical, config not the cause [Verified]
- 20 Nov Hannah Odum: diagnostic bundles from GW-01 to 03 → TS_FUTURE skips, clocks fast, NTP timeouts [Verified]
- 20 to 23 Nov customer IT: checked VLAN 30 firewall → UDP 123 allowed, no changes [Reported]
- 23 Nov 02:35 UTC Hannah Odum: "Force time sync (HTTPS)" to GW-01 to 03 → GW-01/02 OK; GW-03 RTC write error [Verified]; vats 1 and 2 alarm test then passed, vat 3 failed [Reported]
- 24 Nov 05:15 UTC Hannah Odum: second HTTPS time sync to GW-03 → same RTC write error [Verified]
- 24 Nov 05:17 UTC Hannah Odum: remote reboot of GW-03 (customer agreed by phone 05:10) → back online 05:19, clock still +11 min [Verified]

### Commitments to the customer
- Update to the customer, "You'll get an update from us by 17:30 AWST today (09:30 UTC)" | made by Hannah Odum, Support Agent Tier 1, on 24 Nov 05:40 UTC | due 24 Nov 09:30 UTC (17:30 AWST) | open at escalation; met/missed not computable (current time unknown). Tier 2 now owns it (policy 5.3).
- Send a command setting the clock on GW-01 to 03 over HTTPS | made by Hannah Odum, Tier 1, on 23 Nov 02:20 UTC | no time given | met (sent 23 Nov 02:35 UTC)

### Service level
- Priority P2 under clause 2.2 ("alarms ... fail for some gateways ... and there is no practical workaround"), set 23 Nov 02:15 UTC by Hannah Odum; plan Business (account record). The policy supports P2: the alarm failure is verified; the lack of a practical workaround rests on the customer's report.
- First response, 4 business hours (3.1, Business P2; met under P3's 9 hours too): deadline Fri 20 Nov 02:50 UTC (Thu 07:50 to 09:30 UTC = 1h40m, plus Fri 00:30 to 02:50 = 2h20m) | met: first reply Fri 20 Nov 01:05 UTC, 2h15m business
- Resolution, 27 business hours (3.1; 4.3 "counted from ticket creation and excluding paused time"; 4.2 pause only while "Pending customer"): deadline Wed 25 Nov 03:20 UTC = 11:20 AWST (Thu 19 Nov 1h40m + Fri 20 Nov 9h less 4h30m paused 01:10 to 05:40 UTC + Mon 9h + Tue 9h = 24h10m; remaining 2h50m from Wed 00:30 UTC) | not computed: current time unknown. At escalation (24 Nov 06:00 UTC) 6h20m remained, under the 25% line of 6h45m (4.4), so the ticket has been "at risk" since 24 Nov 05:35 UTC.
- Customer update, P2 "at least once each business day" (7.1): last update 24 Nov 05:40 UTC; next due by end of business Wed 25 Nov, 09:30 UTC (reading used, see Gaps) | not computed: current time unknown
- Tier 1's internal note of 24 Nov 01:30 UTC gives the resolution due time as Thu 26 Nov 10:15 AWST, counting from the priority change. That contradicts clause 4.3; the deadline above (Wed 25 Nov 03:20 UTC) is the one the policy supports.

### Recommended next action
Tier 2 (Field Systems Engineering, owner under 5.3) sends Aroha Ngata the update promised for 24 Nov 09:30 UTC (17:30 AWST), stating that vat 3 still has no working alarm and what Tier 2 will do next for GW-03, because the GW-03 clock write fails after two syncs and a reboot [Verified] and the resolution deadline is Wed 25 Nov 03:20 UTC.
Then:
- Diagnose the GW-03 "RTC write error" (hardware versus firmware) and restore a working vat 3 alarm, for example by replacing the gateway, before Wed 25 Nov 03:20 UTC.
- Find why NTP fails on GW-01 to 03 (customer IT reports UDP 123 open; check with Peter Dunn), since GW-01 and GW-02 will drift again without it.

### Gaps
- Current time unknown: all statuses depend on it (see Clarifying question).
- Policy 5.2 requires the Support Team Lead to be notified when an at-risk P2 ticket is escalated; the ticket was at risk from 24 Nov 05:35 UTC and escalated at 06:00 UTC, and no notification is recorded in the thread.
- Customer request to have the cost of the dumped milk covered: asked by Aroha Ngata, not agreed by anyone. Hannah Odum passed it to Joel Brandt (Account Manager); no offer is recorded on the ticket, and the account record shows no open credits. Only the Account Manager or Head of Customer Support may offer compensation (6.3).
- The product loss (18,000 L) and the vat 3 excursions are reported only; the 22 Nov readings have not been checked in TernCloud.
- Cause of the NTP failure on VLAN 30 is unconfirmed; the customer's report (UDP 123 allowed) and Tier 1's hypothesis conflict.
- Policy silences: 7.1 does not say by what time of day the daily P2 update is due (read as end of business hours, 09:30 UTC); 1.1 excludes WA public holidays but none are listed (assumed none between 19 and 25 Nov); 4.3 does not say whether the first-response target also changes with priority (met under both).
- Tier 1 told the customer on 20 Nov that "the hourly checks cover you over the weekend"; the customer now says they did not (not a commitment, but relevant to the compensation request).
