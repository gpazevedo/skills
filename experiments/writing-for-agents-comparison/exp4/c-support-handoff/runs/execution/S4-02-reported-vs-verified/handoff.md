# Escalation handoff: TRN-77102, Coldwater Freight Pty Ltd (CWF-2210)

**Summary:** 14 of 61 gateways (all G4-C cellular, Darwin and Katherine) have been offline since the 4.7.2 firmware update on 14 Nov; cause unconfirmed. The most urgent deadline is the customer update promised by 04:00 UTC Tue 17 Nov; the P2 resolution deadline is 01:05 UTC Thu 19 Nov.
**Reference time:** 2026-11-16 03:50 UTC (latest thread entry; it equals the as-of time stated in the export)

## Problem as currently understood
All 14 offline gateways are G4-C units (Darwin 11, Katherine 3) that stopped reporting during the 4.7.2 rollout on 14 Nov; the 47 G4-E units are online. The G4-C units show a flashing amber NET light and do not respond to remote wake. A cellular modem firmware change in 4.7.2 (MX-31.4, G4-C only) is a possible but unconfirmed cause.
- [Verified] 61 gateways; 47 online and reporting with no gaps, 14 offline (Darwin 11, Katherine 3) (Marcus Lee, 2026-11-16 01:32; account record fleet table)
- [Verified] All 14 offline units last reported 18:20 to 18:24 UTC on 14 Nov, during the rollout that began 18:00 UTC (Marcus Lee, 01:32)
- [Verified] All 61 were updated to 4.7.2; the 47 online units run 4.7.2 (Marcus Lee, 01:32)
- [Verified] All 14 offline units are G4-C and all 47 online units are G4-E (Marcus Lee, 02:10; account record)
- [Verified] All 14 SIMs are Active in the Tern Connect console; last data sessions ended 18:21 to 18:24 UTC on 14 Nov; no session attempts since (Marcus Lee, 02:10)
- [Verified] Remote SMS wake sent 02:05 to DRW-GW-01, DRW-GW-05, KTH-GW-02; no response by 02:10 (Marcus Lee, 02:10)
- [Verified] 4.7.2 release notes include "cellular modem firmware updated to MX-31.4 (G4-C only)" (Marcus Lee, 02:10); link to the fault is not confirmed
- [Reported] Darwin units show solid green power and flashing amber NET light, unchanged after power cycling (Grant Tobias, 03:05, relaying the Darwin site lead). Marcus's reading that amber NET means no mobile registration is from the LED guide, which is not in the thread (Marcus Lee, 03:40); no unit check is recorded.
- [Reported] Customer says "every site is affected" and "every one of our gateways went dark" (Grant Tobias, 01:12, 03:05). This is contradicted by the Verified fleet status above (Perth and Adelaide are G4-E and online); the recorded check governs.
- [Reported] Customer says three days of temperature data are lost and the outage costs about $40,000 a day (Grant Tobias, 01:12). Offline units last reported about 33 hours before the reference time, not three days. Whether readings are stored locally on the G4-C units is unknown.
- [Reported] Customer says Perth cannot dispatch Darwin loads without certificates (Grant Tobias, 03:05); not checked.
Open questions:
- Does MX-31.4 stop the G4-C modems registering on the network, and is it a fault in the firmware or a settings/APN change?
- Do the G4-C units still hold unsent readings locally, and is any data actually lost?
- What do the Katherine units show (not yet checked by the customer)?
- Are other customers with G4-C units on 4.7.2 affected?

## Tried so far
- Reboot of all Darwin gateways, by customer (Grant Tobias), before 01:05 on 16 Nov (Reported): no change.
- Second power cycle of all 11 Darwin units, by customer, morning of 16 Nov, before 03:05 (Reported): lights unchanged.
- TernCloud fleet status check, by Marcus Lee, 01:25 UTC: 47 online, 14 offline, as above.
- Tern Connect SIM check, by Marcus Lee, about 02:10: all 14 SIMs Active, no session attempts since 14 Nov.
- Hardware model comparison, by Marcus Lee, about 02:10: offline units are all G4-C.
- Remote SMS wake to 3 units, by Marcus Lee, 02:05: no response by 02:10; result after 02:10 not recorded. Not sent to the other 11 units.
- Customer was told not to factory-reset (it would erase stored readings), by Marcus Lee, 03:40: no result expected.
- Katherine units: not touched by customer; nothing tried.

## Commitments to the customer
- "I told him I'd check the fleet and call him back within the hour", Marcus Lee, 01:05 (internal call note): met. The fleet email "after call-back" at 01:32 says "as discussed on the phone just now". The call itself is not separately logged.
- "I'll send you an update by 12:00 AWST tomorrow, Tuesday 17 November (04:00 UTC), or sooner if engineering has news", Marcus Lee, 03:40: outstanding, 24h10m remaining. Tier 2 owns it under policy 5.3.
- "If you can tell me who you spoke to, I'll follow it up", Marcus Lee, 01:32: unclear. It is conditional on a name; the customer replied at 03:05 that he does not remember the engineer's name, so no follow-up is currently possible.
- "I'm escalating this to our Field Systems Engineering team now", Marcus Lee, 03:40: met at 03:50 (escalation event).
- Claimed by customer, not found in thread: an engineer told him "on the phone last week that 4.7.2 was fixed and safe to roll out" (Grant Tobias, 01:12; repeated 03:05 without a name). Marcus found no record of a call or ticket last week; the last ticket was TRN-75530, closed 2 Oct (Marcus Lee, 01:32; account record). Treat as unverified. Do not accept liability ("this one is on Tern") in writing.
- No service credit, refund or compensation has been offered or promised. Only the Account Manager (Rhys Kaplan) or the Head of Customer Support may offer one, in writing on the ticket (policy 6.2, 6.3).

## Service level
- Tier: Business (account record) | Priority: P2 (ticket, recorded by Marcus Lee 01:05, unchanged 03:50). The customer's P1 request is recorded but not applied. Policy 2.1 needs more than half of the gateways offline; 14 of 61 (23%) is below that, so P2 is correct.
- Target: first response 4 business hours; resolution 27 business hours (policy 3.1, Business P2). Business hours are 00:30 to 09:30 UTC, Mon to Fri (policy 1.1, 1.2). The clock runs from creation with no pauses (policy 4.1, 4.2). The ticket has not been "Pending customer".
- First response: met at 01:05 UTC, when the agent logged the ticket during the call (policy 1.4).
- Deadline (resolution): Thu 2026-11-19 01:05 UTC (09:05 AWST), calculated as: created Mon 01:05 UTC, inside business hours. Mon 01:05 to 09:30 = 8h25m; Tue 9h gives 17h25m; Wed 9h gives 26h25m; the remaining 35m runs from 00:30 Thu to 01:05 Thu. No public holiday is assumed on 16 to 19 Nov (policy does not list dates; confirm none applies).
- Status: open, within target. Elapsed 2h45m of 27h; 24h15m of business time remains. At risk (under 25%, which is 6.75 business hours remaining) would begin at about 03:20 UTC Wed 18 Nov (policy 4.4).
- If priority were raised to P1 (not assessed as met): resolution 24h calendar from creation would be 01:05 UTC Tue 17 Nov (policy 3.1, 4.3).
- Customer update cadence: P2 needs one update each business day (policy 7.1); the 04:00 UTC Tue commitment meets it for Tuesday.

## Recommended next action
Have Field Systems Engineering test whether the 4.7.2 G4-C modem update (MX-31.4) is stopping network registration: pull modem and gateway diagnostics for one offline unit, such as DRW-GW-01 (remotely, or through Lina Petrakis if on-site access is needed), and compare with an equivalent G4-C unit on another customer's 4.7.2. Also ask the customer to report the Katherine lights, and tell him not to reset any unit. This is justified by the all-G4-C pattern, the active SIMs, the flashing NET light, and the MX-31.4 release note, which is a lead only. Serves: the 04:00 UTC Tue 17 Nov update and the 01:05 UTC Thu 19 Nov resolution deadline.
Tell the customer: by 04:00 UTC Tue 17 Nov (12:00 AWST), send the promised update stating what engineering has found, even if there is no result. Do not give a fix date, a credit or an admission of fault (policy 6.2). Refer any compensation request to Account Manager Rhys Kaplan. Make clear that Perth and Adelaide are not affected. Ask about the "last week" call again only if the customer can name the engineer or date.
