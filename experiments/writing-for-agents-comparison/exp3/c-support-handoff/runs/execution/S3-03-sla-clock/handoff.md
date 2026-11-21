# Escalation handoff: TRN-77391, Kestrel Dairy Co-operative (KDC-0418)

**Service level:** at risk, deadline Wed 25 Nov 2026 11:20 AWST (03:20 UTC), Business P2 resolution 27 business hours (policy 3.1, counted from ticket creation per 4.3); 6 h 20 min remain, under the 25% (6 h 45 min) at-risk threshold of 4.4
**Next action:** Confirm whether GW-03's "TIME_SET_REJECTED: RTC write error" is a hardware fault and, if so, start a replacement of GW-03, telling Aroha the plan in the update promised for 17:30 AWST (09:30 UTC) today, 24 Nov.

## Problem as currently understood
Gateways VAT-GW-01 to 03 at Brunswick have failed NTP sync since 12 Nov, their clocks ran 8 to 11 minutes fast, and the rule engine skipped every high-temperature evaluation, so vats 1 to 3 sent no SMS. A forced HTTPS time sync fixed GW-01 and GW-02, but GW-03 refuses to set its clock (possible RTC hardware fault), so vat 3 still has no alarm; the NTP failure itself is unexplained, so GW-01 and GW-02 may drift again. This shifted from the opening report of an SMS delivery failure once the diagnostic bundles showed the alarms were never evaluated.

Evidence:
- [Reported] Vat 3 went above 7°C for about 40 minutes on Tuesday night and nobody received the SMS; the TernCloud dashboard shows the reading over the limit (Aroha Ngata, 2026-11-19 07:50 UTC)
- [Reported] In a test on all nine vats, vats 4 to 9 sent the SMS within a minute; vats 1, 2 and 3 sent nothing (Aroha Ngata, 2026-11-19 07:50 UTC)
- [Verified] Vats 1 to 9 use the same rule template ("Vat high temp, above 7°C for 5 min") with the same SMS recipients (Hannah Odum, TernCloud alarm rules, 2026-11-20 01:05 UTC)
- [Verified] The rule engine on GW-01, 02 and 03 logs "RULE_EVAL_SKIPPED reason=TS_FUTURE" at every evaluation since 12 Nov; gateway clocks ahead of sensor timestamps by GW-01 +9 min 12 s, GW-02 +8 min 40 s, GW-03 +11 min 03 s (Hannah Odum, diagnostic bundles, 2026-11-20 07:15 UTC)
- [Verified] NTP log on all three: "NTP sync failed: timeout (pool.terncloud.net:123)", repeated since 12 Nov; bundles put GW-01 to 03 on VLAN 30 (Hannah Odum, diagnostic bundles, 2026-11-20 07:15 UTC)
- [Verified] TernCloud shows GW-04 to 09 with last time sync OK (Hannah Odum, TernCloud, 2026-11-20 07:15 UTC)
- [Reported] Customer IT says nothing has changed on VLAN 30 and outbound UDP 123 is allowed (Aroha Ngata, relaying IT, 2026-11-23 01:40 UTC)
- [Reported] Vat 3 went over 7°C again at about 01:00 local time on Sunday night with no SMS; it was over the limit for about 50 minutes before the hourly check caught it, and 18,000 litres were dumped; the customer asks for the cost of the milk to be covered (Aroha Ngata, 2026-11-23 01:40 UTC)
- [Verified] "Force time sync (HTTPS)" sent at 02:35 UTC: GW-01 and GW-02 OK, offset under 1 s; GW-03 "TIME_SET_REJECTED: RTC write error", clock still +11 min 05 s (Hannah Odum, TernCloud command results, 2026-11-23 02:40 UTC)
- [Reported] After the sync, vats 1 and 2 sent the SMS within a minute; vat 3 still nothing (Aroha Ngata, 2026-11-23 03:05 UTC)
- [Verified] Second force sync to GW-03 at 05:15 UTC: same "TIME_SET_REJECTED: RTC write error"; GW-03 rebooted from TernCloud at 05:17, back online 05:19, clock still +11 min; GW-01 and GW-02 still under 1 s offset; NTP still failing on all three (Hannah Odum, TernCloud, 2026-11-24 05:20 UTC)
- Conflict: the bundles show NTP to pool.terncloud.net:123 timing out from all three VLAN 30 gateways since 12 Nov (verified), while customer IT reports outbound UDP 123 is allowed and VLAN 30 unchanged (reported). Hannah's "UDP 123 blocked for VLAN 30" hypothesis was never confirmed (internal note, 2026-11-20 07:15 UTC).
- Conflict: Hannah's internal SLA check put the resolution deadline at Thu 26 Nov 10:15 AWST, counted from the P2 change, with "Plenty of time" (2026-11-24 01:30 UTC). Policy 4.3 counts the new target from ticket creation, giving Wed 25 Nov 11:20 AWST, and the ticket is already at risk (see Service level).
- The two temperature excursions and the 18,000-litre loss are reported only; no one at Tern has checked them against TernCloud readings.

## Tried so far
- 2026-11-19, before 07:50 UTC, Aroha Ngata: alarm test on all nine vats -> vats 4 to 9 sent SMS within a minute; vats 1 to 3 sent nothing
- 2026-11-20 01:05 UTC, Hannah Odum: compared alarm rules in TernCloud -> identical template and recipients on all nine vats; configuration does not explain the difference
- 2026-11-20 01:10 UTC, Hannah Odum: requested diagnostic bundles from GW-01 to 03 -> bundles attached by customer 05:40 UTC
- 2026-11-20 07:15 UTC, Hannah Odum: analysed bundles -> TS_FUTURE rule skips, clock offsets of 8 to 11 min, NTP timeouts since 12 Nov
- 2026-11-20 07:20 UTC, Hannah Odum: asked customer IT to check outbound UDP 123 from VLAN 30 -> IT reports nothing changed and UDP 123 allowed (2026-11-23 01:40 UTC)
- 2026-11-23 02:20 UTC, Hannah Odum: passed the compensation request to Joel Brandt (Account Manager) -> result not recorded
- 2026-11-23 02:35 UTC, Hannah Odum: "Force time sync (HTTPS)" to GW-01, 02, 03 -> GW-01 and 02 OK (under 1 s); GW-03 "TIME_SET_REJECTED: RTC write error"
- 2026-11-23 before 03:05 UTC, Aroha Ngata: alarm test on vats 1 to 3 -> vats 1 and 2 SMS within a minute; vat 3 nothing
- 2026-11-24 05:15 UTC, Hannah Odum: second force time sync to GW-03 -> same RTC write error
- 2026-11-24 05:17 UTC, Hannah Odum: remote reboot of GW-03 (customer agreed by phone 05:10) -> back online 05:19, clock still +11 min
- 2026-11-24 06:00 UTC, Hannah Odum: escalated to Tier 2 (Field Systems Engineering), status Escalated, priority P2

## Commitments to the customer
- "Next, I'm going to send a command from TernCloud that sets the clock on GW-01 to 03 over HTTPS, which avoids the NTP port." (Hannah Odum, 2026-11-23 02:20 UTC), due "Next", met (sent 02:35 UTC)
- "I've passed your request to Joel Brandt, your account manager." (Hannah Odum, 2026-11-23 02:20 UTC), no due time stated, open: no response from Joel Brandt and no offer recorded on the ticket (policy 6.3 requires any offer in writing on the ticket or account record; account record shows open credits: none)
- "I'm escalating this to our Field Systems Engineering team now." (Hannah Odum, 2026-11-24 05:40 UTC), due "now", met (escalated 06:00 UTC)
- "You'll get an update from us by 17:30 AWST today (09:30 UTC)." (Hannah Odum, 2026-11-24 05:40 UTC), due 17:30 AWST today (2026-11-24 09:30 UTC), open; Tier 2 now owns it (policy 5.3)
- Related statement, not a commitment: "No rush before Monday; the hourly checks cover you over the weekend." (Hannah Odum, 2026-11-20 07:20 UTC). The customer later reported the loss happened during that weekend's hourly checks; relevant to the compensation request.

## Service level
- Plan: Business (account record; policy 1.3 "The customer's support plan ... is the one in the account record")
- Priority: P2 (thread event 2026-11-23 02:15 UTC, Hannah Odum: "Missed alarm caused product loss; hourly manual checks not a practical workaround (clause 2.2)"). Matches policy 2.2: "alarms ... fail for some gateways ... and there is no practical workaround". No mismatch: P1 (2.1) needs more than half of gateways offline, and the gateways are online. The original P3 fit 2.3 while hourly checks were the workaround.
- Target: policy 3.1, "Business | P2 | 4 business hours | 27 business hours"; 4.3 "If the priority changes, the resolution target becomes the target for the new priority, counted from ticket creation and excluding paused time." First response (Hannah Odum, 2026-11-20 01:05 UTC) came 2 h 15 min business time after creation, within both the P3 (9 h) and P2 (4 h) targets.
- Clock: started at ticket creation, Thu 19 Nov 07:50 UTC (15:50 AWST) (4.1 "The clock starts when the ticket is created"); business hours only, 08:30 to 17:30 AWST Mon to Fri, which is 00:30 to 09:30 UTC (1.1, 1.2, 3.3); paused only in "Pending customer" (4.2): Fri 20 Nov 01:10 to 05:40 UTC (4 h 30 min). No WA public holiday falls in the period. Counted: Thu 19 Nov 1 h 40 min; Fri 20 Nov 4 h 30 min; Mon 23 Nov 9 h; Tue 24 Nov to 06:00 UTC 5 h 30 min; total 20 h 40 min of 27 h.
- Deadline: Wed 25 Nov 2026 11:20 AWST (03:20 UTC), as of now = 2026-11-24 06:00 UTC (latest timestamp in the thread, the escalation event; no "now" was given). 6 h 20 min remain, below 25% of 27 h (6 h 45 min), so "at risk" under 4.4; it crossed into at risk at about 05:35 UTC today, before the escalation.
- Policy 5.2: "When a P1 ticket, or an at-risk P2 ticket, is escalated, the Support Team Lead must be notified at escalation." The thread records no such notification.
- Update cadence: policy 7.1, "P2: at least once each business day."

## Recommended next action
Establish whether GW-03's "RTC write error" is a hardware fault (it survived two forced syncs and a reboot) and, if it is, start a replacement of GW-03, giving Aroha the plan and its timing in the update due 09:30 UTC today. Vat 3 is the only vat still without an alarm, it is the vat that has already cost the customer 18,000 litres (reported), the customer says hourly checks are not enough, and the resolution deadline is under 6 h 20 min of business time away.

Open questions:
- Why does NTP to pool.terncloud.net:123 time out from VLAN 30 when customer IT says UDP 123 is allowed? What changed on 12 Nov? Are GW-04 to 09 on a different VLAN or network path? The network contact in the account record is Peter Dunn, IT Coordinator.
- Until NTP is fixed, will GW-01 and GW-02 drift past the rule window again, and who is watching their offset?
- What interim protection can vat 3 have until GW-03 is fixed or replaced?
- Are the Harvey depot gateways (DEP-GW-01, DEP-GW-02) syncing time correctly? The thread does not say.
- Was the Support Team Lead notified at escalation, as policy 5.2 requires for an at-risk P2?
- Has Joel Brandt picked up the compensation request? Tier 2 must not promise compensation (policy 6.2); only the Account Manager or Head of Customer Support may offer it (6.3).
- Do TernCloud readings confirm the two reported vat 3 excursions (Tuesday night, about 40 min; Sunday night about 01:00 AWST, about 50 min)?

Next customer update due: 17:30 AWST (09:30 UTC) Tue 24 Nov 2026, from Hannah Odum's commitment; after that at least once each business day under policy 7.1.
