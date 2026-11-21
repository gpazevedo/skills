# Escalation handoff: TRN-77391, Kestrel Dairy Co-operative (KDC-0418)

**Service level:** At risk, deadline Wed 25 Nov 2026 11:20 AWST (03:20 UTC), Business plan P2 resolution target of 27 business hours (policy 3.1, 4.3); about 6.3 business hours remain, under the 6.75 h at-risk threshold (4.4)
**Next action:** Have a field engineer get GW-03 to accept a clock set (or replace or swap its RTC or unit) and re-run the vat 3 alarm test, since GW-03 is the one fault still unresolved and the deadline is Wed 11:20 AWST.

## Problem as currently understood
High-temperature SMS alarms do not fire on vat gateways whose clocks run ahead of the sensor timestamps, because the rule engine skips evaluation (TS_FUTURE). It started as "some vats not alarming, cause unknown". It is now narrowed to clock drift caused by failed NTP sync on GW-01 to 03. GW-01 and GW-02 are fixed for now. GW-03 refuses to set its clock (RTC write error) and still does not alarm, so a hardware fault is suspected.

Evidence:
- [Reported] Vat 3 exceeded 7°C for about 40 minutes on a Tuesday night with no SMS; the dashboard showed the reading (Aroha Ngata, 2026-11-19 07:50 UTC).
- [Reported] Alarm test on all nine vats: vats 4 to 9 sent SMS within a minute; vats 1, 2, 3 sent nothing (Aroha Ngata, 2026-11-19 07:50 UTC).
- [Verified] Vats 1 to 9 all use the same rule template and the same SMS recipients, so configuration does not explain the difference (Hannah Odum, checked rules in TernCloud, 2026-11-20 01:05 UTC).
- [Verified] GW-01 to 03 log "RULE_EVAL_SKIPPED reason=TS_FUTURE" at every evaluation since 12 Nov. Clock offsets were GW-01 +9 min 12 s, GW-02 +8 min 40 s, GW-03 +11 min 03 s (Hannah Odum, from diagnostic bundles, internal note 2026-11-20 07:15 UTC).
- [Verified] NTP log on GW-01 to 03: "NTP sync failed: timeout (pool.terncloud.net:123)" repeated since 12 Nov; GW-01 to 03 are on VLAN 30; TernCloud shows GW-04 to 09 with last time sync OK (Hannah Odum, bundles and TernCloud, 2026-11-20 07:15 UTC).
- [Reported] IT says nothing changed on VLAN 30 and outbound UDP 123 is allowed (Aroha Ngata, relaying IT, 2026-11-23 01:40 UTC).
- Conflict: IT's report that UDP 123 is allowed (reported) sits against the verified NTP timeouts on GW-01 to 03 only. The firewall cause is unconfirmed (Hannah's note says "Not confirmed"). The block may be elsewhere, or IT's check may not cover VLAN 30 as seen by those gateways.
- [Reported] Vat 3 went over 7°C again on Sunday night, about 01:00 customer time, with no SMS; it was over the limit about 50 minutes before the night operator caught it on the hourly check; 18,000 litres dumped; customer wants the milk cost covered (Aroha Ngata, 2026-11-23 01:40 UTC).
- [Verified] "Force time sync (HTTPS)" at 02:35 UTC on 23 Nov: GW-01 and GW-02 OK with offset under 1 s; GW-03 "TIME_SET_REJECTED: RTC write error", still +11 min 05 s (Hannah Odum, TernCloud command results, internal note 2026-11-23 02:40 UTC).
- [Reported] After that, vats 1 and 2 sent SMS within a minute; vat 3 sent nothing (Aroha Ngata, 2026-11-23 03:05 UTC).
- [Verified] Second HTTPS time sync on GW-03 at 05:15 UTC on 24 Nov gave the same RTC write error. Remote reboot at 05:17 UTC (back online 05:19) left the clock still about +11 min. GW-01 and GW-02 still show offset under 1 s, but NTP still fails on all three, so they may drift again (Hannah Odum, internal note 2026-11-24 05:20 UTC).

## Tried so far
- 2026-11-20 01:05 UTC, Hannah Odum: compared alarm rule configuration for vats 1 to 9 -> identical template and recipients.
- 2026-11-20 01:10 UTC, Hannah Odum: asked customer for diagnostic bundles from GW-01 to 03 (status set to Pending customer) -> customer supplied them 05:40 UTC; they showed the clock drift and NTP failures.
- 2026-11-20 07:20 UTC, Hannah Odum: asked customer's IT to check outbound UDP 123 from VLAN 30 -> IT reports it is allowed (2026-11-23 01:40 UTC, reported); not independently verified.
- 2026-11-23 02:35 UTC, Hannah Odum: "Force time sync (HTTPS)" to GW-01, 02, 03 -> 01 and 02 OK, 03 rejected (RTC write error).
- 2026-11-23 03:05 UTC, Aroha Ngata (at Hannah's request): alarm test on vats 1 to 3 -> vats 1, 2 sent SMS; vat 3 did not.
- 2026-11-23 02:15 UTC, Hannah Odum: raised priority P3 to P2 -> recorded.
- 2026-11-23 02:20 UTC, Hannah Odum: passed compensation request to Joel Brandt -> result not recorded.
- 2026-11-24 05:15 UTC, Hannah Odum: second HTTPS time sync on GW-03 -> same RTC write error.
- 2026-11-24 05:17 UTC, Hannah Odum: remote reboot of GW-03, agreed with Aroha by phone at 05:10 UTC -> back online 05:19 UTC, clock still about +11 min.
- 2026-11-24 05:40 UTC, Hannah Odum: no alarm retest on vat 3 after the reboot -> result not recorded (clock still offset).

## Commitments to the customer
- "Next, I'm going to send a command from TernCloud that sets the clock on GW-01 to 03 over HTTPS" (Hannah Odum, 2026-11-23 02:20 UTC), due: no time stated, met (sent 02:35 UTC).
- "I've passed your request to Joel Brandt, your account manager." (Hannah Odum, 2026-11-23 02:20 UTC), due: no time stated, open. The thread has no record that Joel Brandt received it or replied. This is not a credit offer; policy 6.2 and 6.3 bar agents from promising compensation and only Joel Brandt or the Head of Customer Support can offer it, in writing on the ticket or account record. No offer is recorded.
- "You'll get an update from us by 17:30 AWST today (09:30 UTC)." (Hannah Odum, 2026-11-24 05:40 UTC), due 17:30 AWST Tue 24 Nov (09:30 UTC), open. Under 5.3 Tier 2 owns this commitment.
- Earlier "No rush before Monday; the hourly checks cover you over the weekend" (Hannah Odum, 2026-11-20 07:20 UTC) is not a commitment on a deliverable. Customer later reported the hourly checks were not enough.

## Service level
- Plan: Business (account record: "Support plan: Business")
- Priority: P2 (set by Hannah Odum 2026-11-23 02:15 UTC with reason citing clause 2.2). It was P3 from creation. Under 2.2 and 2.3 the original report (alarms failing for some gateways, hourly dashboard checks as the only workaround) was arguably borderline; 2.5 says priority applies only once recorded, so P3 applied until 02:15 UTC on 23 Nov. P2 now fits 2.2 and is not P1, as fewer than half the 11 gateways are affected (2.1).
- Target: Business, P2: "4 business hours" first response, "27 business hours" resolution (3.1). 4.3: "the resolution target becomes the target for the new priority, counted from ticket creation and excluding paused time." Resolution requires every fault on the ticket resolved (1.5); GW-03 remains.
- Clock: started at ticket creation, Thu 2026-11-19 07:50 UTC (15:50 AWST) (4.1). Business hours 00:30 to 09:30 UTC Mon to Fri (1.1, 1.2); no WA public holiday identified in the policy or thread. Paused only in "Pending customer" (4.2): 2026-11-20 01:10 to 05:40 UTC (4.5 h, all inside business hours).
- Counted business hours: Thu 19 (07:50 to 09:30 UTC) 1.67 h; Fri 20 (9 h less 4.5 h paused) 4.5 h; Mon 23 9 h; Tue 24 (00:30 to 06:00 UTC) 5.5 h; total about 20.67 h of 27 used, about 6.33 h left. Weekend not counted.
- Deadline: Wed 25 Nov 2026 03:20 UTC (11:20 AWST) as of now = 2026-11-24 06:00 UTC (the as-of time given in the ticket export). Status: at risk (4.4: less than 25% of 27 h, i.e. 6.75 h, remains). Not breached.
- Correction: Hannah's internal note (2026-11-24 01:30 UTC) put the due time at Thu 26 Nov 10:15 AWST by counting 27 business hours from the priority change. Policy 4.3 counts from creation, so that date is about 1 business day too late. Do not rely on it.
- First response: met. First agent contact 2026-11-20 01:05 UTC, about 2.25 business hours after creation, inside the 4 h P2 target (and the 9 h P3 target).
- Escalation: 5.1 requires escalation when a P2 ticket is at risk, and 5.2 requires the Support Team Lead be notified at escalation. The thread does not record that notification.
- Update cadence: P2 needs an update at least once each business day (7.1). Last customer update 2026-11-24 05:40 UTC.

## Recommended next action
Engage the field team on GW-03 now: the HTTPS time set and reboot both failed, so this is the only unresolved fault and the one that determines whether the ticket meets the Wed 11:20 AWST deadline. Options are a hardware diagnosis of the RTC, a replacement or swap of the unit, or any documented workaround that gets vat 3 alarming. After any change, repeat the vat 3 alarm test with the customer. Also notify the Support Team Lead (5.2) and confirm with Joel Brandt that he received the compensation request.

Open questions:
- Why does NTP time out only on GW-01 to 03 (VLAN 30) when IT says UDP 123 is open? Check IT's rule and any DNS issue with pool.terncloud.net from that VLAN. GW-01 and GW-02 may drift again until it is fixed. Is a permanent fix, such as a different time source, needed?
- Is the GW-03 RTC write error a hardware fault, and is a replacement unit available on site at Brunswick or must it be sent?
- Has the Support Team Lead been notified? Has Joel Brandt acknowledged the compensation request?
- Is there an interim workaround for vat 3 (for example a local alarm or a second monitoring path) while GW-03 is faulty, since hourly manual checks have already led to a 18,000 litre loss?
- Was the earlier "Tuesday night" event and the Sunday event caused by the same clock drift on GW-03? Evidence is the 12 Nov onset; not confirmed for those dates.

Next customer update due: 17:30 AWST Tue 24 Nov 2026 (09:30 UTC), from Hannah's commitment at 05:40 UTC; thereafter at least once each business day (7.1).
