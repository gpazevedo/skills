# Escalation handoff: TRN-77102, Coldwater Freight Pty Ltd (CWF-2210)

**Summary:** 14 of 61 gateways, all cellular G4-C units at Darwin and Katherine, have been offline since the firmware 4.7.2 rollout on 14 Nov; the 47 Ethernet G4-E units are fine. Next deadline is the promised customer update at 04:00 UTC Tue 17 Nov (12:00 AWST); P2 resolution target falls at 01:05 UTC Thu 19 Nov.
**Reference time:** 2026-11-16 03:50 UTC (latest thread entry)

## Problem as currently understood
Every G4-C (cellular) gateway stopped reporting during the 4.7.2 rollout and its modem appears not to register on the mobile network, while the SIMs are active on the carrier side. Every G4-E (Ethernet) gateway on 4.7.2 is reporting normally. The suspected link is the 4.7.2 modem firmware update to MX-31.4 (G4-C only), which is not confirmed.
- [Verified] 61 gateways; 47 online, 14 offline; the offline units are Darwin (11) and Katherine (3), last reports 18:20 to 18:24 UTC on 14 Nov, during the rollout that started 18:00 UTC (Marcus Lee, 2026-11-16 01:32 UTC, TernCloud check)
- [Verified] All 61 units are on 4.7.2 (Marcus Lee, 01:32, TernCloud check)
- [Verified] All 14 offline units are G4-C cellular; all 47 online are G4-E Ethernet (Marcus Lee, 02:10 internal note; account record fleet table)
- [Verified] 4.7.2 release notes: "cellular modem firmware updated to MX-31.4 (G4-C only)" (Marcus Lee, 02:10)
- [Verified] All 14 SIMs Active; last data sessions ended 18:21 to 18:24 UTC on 14 Nov; no session attempts since (Marcus Lee, 02:10, Tern Connect console)
- [Verified] Remote SMS wake sent to DRW-GW-01, DRW-GW-05, KTH-GW-02 at 02:05 UTC; no response by 02:10 (Marcus Lee, 02:10)
- [Verified] Readings from the 47 online units are complete with no gaps; no readings in TernCloud from the 14 offline units after their last report (Marcus Lee, 01:32, TernCloud check)
- [Reported] Darwin units show solid green power and flashing amber NET (Grant Tobias, customer, 03:05). Per the LED guide this means the cellular modem is not registered on the mobile network (Marcus Lee, 03:40)
- [Reported] G4 units buffer readings locally and upload on reconnect, so data loss is not yet known (Marcus Lee, 01:32; product behaviour stated, no check recorded)
- Conflicts: the customer says "every one of our gateways went dark" and "we've lost all our temperature data" (Grant Tobias, 01:12) and "every site is affected" because Perth cannot dispatch Darwin loads (03:05). The recorded TernCloud check governs: 14 of 61 offline, online units' data complete. The dispatch impact is Reported business impact, not a gateway fault at Perth.
- [Reported] Cost of about $40,000 a day in stock that cannot be certified (Grant Tobias, 01:12)

Open questions:
- Does the MX-31.4 modem update stop G4-C network registration (failed or incompatible modem flash)?
- How long can a G4-C buffer readings before local storage overwrites or fills?
- What do the 3 untouched Katherine units' LEDs show?
- Is there a recovery path (modem or firmware rollback) that does not need a factory reset?

## Tried so far
- Rebooted all Darwin gateways, by customer, before 01:05 UTC 16 Nov: no difference (Reported, Marcus Lee call note, 01:05)
- Fleet status check in TernCloud, by Marcus Lee, 01:25 UTC: 14 of 61 offline, all Darwin and Katherine (01:32)
- SIM status check in Tern Connect, by Marcus Lee, 02:10: all Active, no session attempts since 14 Nov
- Hardware model comparison, by Marcus Lee, 02:10: offline = G4-C, online = G4-E
- Remote SMS wake to 3 units, by Marcus Lee, 02:05: no response
- Front-panel LED check and second power-cycle of all 11 Darwin units, by customer's Darwin site lead, morning of 16 Nov: lights unchanged (Reported, Grant Tobias, 03:05). Katherine units not touched.

## Commitments to the customer
- "I'd check the fleet and call him back within the hour", Marcus Lee, 01:05 UTC: met (call-back and fleet status email at 01:32)
- "I'm escalating this to our Field Systems Engineering team now", Marcus Lee, 03:40: met (escalation event 03:50)
- "I'll send you an update by 12:00 AWST tomorrow, Tuesday 17 November (04:00 UTC), or sooner if engineering has news", Marcus Lee, 03:40: outstanding. Tier 2 now owns it (policy, section 5.3).
- Claimed by customer, not found in thread: an engineer told him on the phone last week that 4.7.2 "was fixed and safe to roll out" (Grant Tobias, 01:12 and 03:05). Marcus Lee found no call or ticket with Coldwater last week; last ticket TRN-75530 closed 2 Oct (01:32; account record agrees).
- No credit, refund or compensation has been offered; the account record shows open credits: none. Only Rhys Kaplan (Account Manager) or the Head of Customer Support may offer one (policy, section 6.3).

## Service level
- Tier: Business (account record) | Priority: P2 (ticket, set 01:05, confirmed at escalation 03:50). The customer's P1 request is recorded and not applied; 14 of 61 offline is not "more than half" (policy, sections 2.1, 2.2, 2.5).
- Target: first response 4 business hours; resolution 27 business hours (policy, section 3.1). Business hours 08:30 to 17:30 AWST Mon to Fri = 00:30 to 09:30 UTC (sections 1.1, 1.2). No pauses: status has never been "Pending customer" (section 4.2).
- First response: met at 01:05 UTC, ticket logged by an agent during the customer's call (section 1.4).
- Deadline: resolution by 2026-11-19 01:05 UTC (09:05 AWST Thu). Clock starts at creation 09:05 AWST Mon 16 Nov, inside business hours (section 4.1). Mon 09:05 to 17:30 = 8h25m; Tue 9h (17h25m); Wed 9h (26h25m); Thu 08:30 + 35m = 09:05 AWST. Assumes no WA public holiday 16 to 19 Nov; the policy does not list holiday dates.
- Status: open, within target (section 4.4); 2h45m used, 24h15m business hours remaining. Becomes "at risk" when under 6h45m remains: 11:20 AWST Wed 18 Nov (03:20 UTC).
- Customer updates: at least once each business day for P2 (section 7.1).

## Recommended next action
Reproduce on an in-house G4-C upgraded to 4.7.2 and confirm whether the MX-31.4 modem update stops network registration, and find a recovery path that avoids a factory reset. Because: the fault splits exactly by model (G4-C vs G4-E), the release note changes only the G4-C modem, SIMs are active with no session attempts, and the LED pattern points to an unregistered modem. Serves: the 04:00 UTC Tue 17 Nov update commitment and the 01:05 UTC Thu 19 Nov resolution deadline.
Tell the customer: by 04:00 UTC (12:00 AWST) Tue 17 Nov, Tier 2 sends the promised update: findings so far (model split, modem suspected), that a fix date cannot yet be given (policy, section 6.2), and a repeat of "do not factory-reset any unit". Ask the Katherine site for its LED state and, with Lina Petrakis (technical contact, account record), how long the units can buffer readings. Refer the $40,000-a-day cost and the "engineer last week" claim to Rhys Kaplan; do not discuss credits.
