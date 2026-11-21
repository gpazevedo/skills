## Escalation handoff: TRN-77391 Vat 3 (VAT-GW-03) still sends no high-temperature SMS alarm; clock cannot be set
As of: Tue 24 Nov 2026, 06:00 UTC (14:00 AWST)
Customer: Kestrel Dairy Co-operative (KDC-0418), Business plan, TernCloud Site subscription. Brunswick plant VAT-GW-01 to 09 (G4-E, one per milk vat); Harvey depot DEP-GW-01 and 02. Alarms go by SMS to the plant on-call roster. Contact: Aroha Ngata, Plant Engineer. Account Manager: Joel Brandt. Open credits: none (account record).

### Problem as currently understood
The high-temperature rule is skipped on VAT-GW-03 because its clock runs about 11 minutes ahead of the sensor timestamps, so the 5-minute window never fills. The clock cannot be corrected: the HTTPS force-sync fails twice with "TIME_SET_REJECTED: RTC write error", and a reboot did not help, so a hardware fault in the real-time clock is suspected but unconfirmed. GW-01 and GW-02 are corrected for now, but NTP still fails on all three, so they may drift again. Cause of the NTP failure is unknown.
Evidence:
- [Verified] VAT-GW-01 to 09 use the same rule template and SMS recipients (Hannah Odum, Tier 1, 20 Nov 01:05 UTC).
- [Verified] On GW-01, 02 and 03 the rule engine logs RULE_EVAL_SKIPPED reason=TS_FUTURE at every evaluation since 12 Nov. Clocks were ahead by 9m12s, 8m40s and 11m03s. NTP times out to pool.terncloud.net:123 since 12 Nov. All three are on VLAN 30 (Hannah Odum, diagnostic bundles, 20 Nov 07:15 UTC).
- [Verified] TernCloud shows GW-04 to 09 with last time sync OK (Hannah Odum, 20 Nov 07:15 UTC).
- [Verified] After the 23 Nov 02:35 force sync, GW-01 and 02 are within 1 s; GW-03 rejected it and was still +11m05s. On 24 Nov at 05:15 a second sync was rejected and the 05:17 reboot left GW-03 at about +11 min (Hannah Odum, 23 Nov 02:40 and 24 Nov 05:20 UTC).
- [Reported] Vat 3 went over 7°C for about 40 minutes on Tue 17 Nov with no SMS; the dashboard showed the reading (Aroha Ngata).
- [Reported] On 19 Nov, vats 4 to 9 sent the test SMS and vats 1 to 3 did not (Aroha Ngata).
- [Reported] Vat 3 went over 7°C again about 01:00 AWST on Mon 23 Nov for about 50 minutes, with no SMS. 18,000 litres were dumped (Aroha Ngata, 23 Nov).
- [Reported] After the sync, vats 1 and 2 sent the test SMS within a minute and vat 3 sent nothing (Aroha Ngata, 23 Nov 03:05 UTC).
- [Reported] Customer IT says nothing changed on VLAN 30 and outbound UDP 123 is allowed (Aroha Ngata, relaying Peter Dunn's team, 23 Nov). This contradicts Tier 1's suspicion (UDP 123 blocked, "Not confirmed") and nobody has checked it.

### Tried so far
- 20 Nov Hannah Odum: checked the alarm rules and recipients in TernCloud → identical across vats 1 to 9, so configuration ruled out as the difference [Verified]
- 20 Nov Hannah Odum: asked for diagnostic bundles from GW-01 to 03 and set the ticket to Pending customer → bundles received 05:40 UTC, root symptom found (clock skew, NTP timeout) [Verified]
- 20 Nov Hannah Odum: asked Aroha to have IT check UDP 123 from VLAN 30 → IT says it is allowed; not independently checked [Reported]
- 23 Nov 02:35 UTC Hannah Odum: "Force time sync (HTTPS)" to GW-01, 02, 03 → GW-01 and 02 OK; GW-03 rejected with an RTC write error [Verified]
- 24 Nov 05:15 UTC Hannah Odum: second force sync on GW-03 → same rejection [Verified]
- 24 Nov 05:17 UTC Hannah Odum: remote reboot of GW-03 (customer agreed by phone at 05:10) → back online 05:19, clock still about +11 min [Verified]
- Not done: no workaround for vat 3 other than the customer's hourly manual dashboard checks; nothing recorded on checking NTP reachability from our side.

### Commitments to the customer
- Update to Aroha "by 17:30 AWST today (09:30 UTC)" | made by Hannah Odum, Tier 1 Support Agent, on 24 Nov 05:40 UTC | due 24 Nov 09:30 UTC | open, 3h30 remaining. Tier 2 owns this from escalation (policy 5.3).
- "I've passed your request to Joel Brandt, your account manager" (the customer's request to cover the milk cost) | made by Hannah Odum on 23 Nov 02:20 UTC | no due time given | passing it on is stated as done; no reply or response from Joel Brandt is on the ticket.
- "I'm going to send a command ... that sets the clock on GW-01 to 03" and then asks for a retest | Hannah Odum, 23 Nov 02:20 UTC | no due time | met (sent 02:35 UTC).
- No credit, refund, compensation or fix date has been promised. The milk-cost request is a customer ask only.

### Service level
- Priority P2 under policy 2.2 (alarms fail for some gateways, no practical workaround; Tier 1 recorded this on 23 Nov 02:15 UTC). Raised from P3 on that date. Plan Business (account record).
- First response: deadline Fri 20 Nov 05:15 UTC "4 business hours" (policy 3.1, clock from creation 4.1). Created Thu 19 Nov 07:50 UTC (15:50 AWST), 1h40 left of Thursday plus 35 min Friday to the 01:05 UTC reply = 2h15 used | met.
- Resolution: 27 business hours (policy 3.1 Business P2), counted from ticket creation excluding paused time (4.3, 4.2). Business hours 00:30 to 09:30 UTC, Mon to Fri (1.1, 1.2). Used: Thu 1h40 + Fri 9h00 minus 4h30 paused (Pending customer, 20 Nov 01:10 to 05:40 UTC) + Mon 9h00 + Tue 5h30 (to 06:00 UTC) = 20h40. Remaining 6h20. Deadline Wed 25 Nov 03:20 UTC (11:20 AWST) | open, 6h20 remaining, AT RISK (policy 4.4: under 25% of 27h = 6h45 remains).
- Tier 1's internal note of 24 Nov 01:30 UTC (due Thu 26 Nov 10:15 AWST, "plenty of time") counts from the priority change, which policy 4.3 does not allow, and is wrong.
- Update interval (policy 7.1, P2: at least once each business day): the 24 Nov update is promised for 09:30 UTC | open.

### Recommended next action
Tier 2 (Field Systems Engineering, the engineer taking this ticket) should send Aroha a customer update before 09:30 UTC today (17:30 AWST) that states Tier 2 now owns the case, the GW-03 clock hardware suspicion, and the next step and time of the next update, and should notify the Support Team Lead now. The update is the nearest deadline, and policy 5.2 requires the Team Lead to be told of an at-risk P2 at escalation and the thread records no notification.
Then: (1) work out how to get vat 3 alarming before the resolution deadline, for example a replacement GW-03, since a hardware fault is only suspected and unconfirmed; (2) find why NTP times out from VLAN 30 only, because customer IT's "UDP 123 allowed" is unverified and GW-01 and 02 may drift again.
Do not promise credit or a fix date (policy 6.2); a credit can only come from Joel Brandt or the Head of Customer Support, in writing on the ticket (6.3).

### Gaps
- Support Team Lead notification (policy 5.2) is not recorded on the ticket.
- Reply from Joel Brandt on the milk-cost request: none on the ticket. No credit offered or valid under 6.3.
- Cause of the NTP failure on VLAN 30 is unknown; the UDP 123 block hypothesis conflicts with IT's report and is unchecked. The RTC hardware fault on GW-03 is not confirmed.
- Policy silent on WA public holidays in the window; none assumed between 19 and 25 Nov.
- Customer impact figures (40 and 50 minutes, 18,000 litres) are customer-reported only.
- Customer's night staff are still doing hourly manual dashboard checks; Aroha has said these are not sustainable.
