# Handoff: TRN-77102, Coldwater Freight (CWF-2210), 14 G4-C gateways offline after firmware 4.7.2

## Problem
- 14 of 61 gateways are offline: Darwin (11) and Katherine (3). [Verified: TernCloud fleet view per Marcus Lee 01:32 UTC; account record fleet table confirms 61 units and these sites]
- The 14 offline units are all G4-C (cellular). The 47 online units are all G4-E (Ethernet). [Verified: Marcus Lee internal note 02:10; account record lists Kewdale and Wingfield as G4-E, Darwin and Katherine as G4-C]
- All 61 gateways were updated to firmware 4.7.2 in the customer's scheduled window starting 18:00 UTC Sat 14 Nov. [Verified: TernCloud per Marcus Lee 01:32; account record shows customer-scheduled rollouts, default window Saturdays from 18:00 UTC]
- The offline units last reported between 18:20 and 18:24 UTC on 14 Nov. [Verified: TernCloud per Marcus Lee 01:32]
- Their SIMs are all status Active and their last data sessions ended 18:21 to 18:24 UTC 14 Nov, with no session attempts since. [Verified: Tern Connect console, Marcus Lee 02:10]
- Release notes for 4.7.2 include "cellular modem firmware updated to MX-31.4 (G4-C only)". This is a possible link to the fault and is not confirmed. [Verified: release notes as quoted by Marcus Lee 02:10; the link itself is unconfirmed; release notes not in the inputs]
- Remote SMS wake sent to DRW-GW-01, DRW-GW-05 and KTH-GW-02 at 02:05 UTC got no response by 02:10. [Verified: Marcus Lee 02:10]
- Darwin units show solid green power light and flashing amber NET light, unchanged after power cycling. [Reported: Grant Tobias 03:05, relayed from Darwin site lead]
- Per Tern's LED guide, flashing amber NET on a G4-C means the modem is not registered on the mobile network. [Verified: Marcus Lee 03:40 citing the LED guide; the guide is not in the inputs]
- Darwin units were rebooted before the call and again on the morning of 16 Nov. [Reported: Grant Tobias via call note 01:05 and email 03:05]
- Katherine units have not been touched or checked. [Reported: Grant Tobias 03:05]
- G4 gateways store readings locally and upload on reconnect, so data may not be lost. [Verified: Marcus Lee 01:32, stated as product behaviour; whether these 14 units hold readings is unknown]
- Customer says all gateways in all sites are offline, "every site is affected", and all temperature data for three days is lost. [Reported: Grant Tobias 01:12, 03:05] CONFLICT: 47 of 61 gateways are online with complete readings [Verified: TernCloud per Marcus Lee 01:32]. The offline units went silent about 30 hours before the 01:12 email, not three days.
- Customer says a Tern engineer told him the previous week that 4.7.2 was fixed and safe, and that the fault is therefore Tern's responsibility. [Reported: Grant Tobias 01:12, 03:05] No record of such a call or ticket; the last ticket on the account is TRN-75530, closed 2 October. [Verified: Marcus Lee 01:32; account record recent tickets]. Customer cannot name the engineer.
- Customer says the outage costs about $40,000 a day in stock that cannot be certified, and that Perth cannot dispatch Darwin loads without certificates. [Reported: Grant Tobias 01:12, 03:05]
- Priority is P2, with the customer's P1 request recorded and not applied. Fewer than half of the gateways are offline (14 of 61), so P1 (2.1) does not apply. [Verified: thread event 03:50; policy 2.1, 2.2, 2.5; account record fleet count]

## Open questions
- Cause: is the MX-31.4 modem firmware in 4.7.2 behind the failed network registration? Check the 4.7.2 modem change against the G4-C units' state and any known issues; look for reports from other G4-C customers on 4.7.2.
- Do the 14 units hold stored readings? Settle by gaining remote or on-site access without a factory reset.
- Why did the SMS wake get no response? Only checked at 02:10; re-check delivery status and retry on the other 11 units.
- Katherine: ask for LED status on the 3 units (Marcus asked for "two or three of the units" at 01:32; only Darwin has replied).
- Did a Tern engineer really say 4.7.2 was safe? No record found. Ask the customer for date, time, or phone number, and check call logs and the engineering team.
- Customer-scheduled versus Tern-pushed: the customer says "your firmware push", while the account record says rollouts are customer-scheduled. Confirm who triggered the rollout and whether the customer had been told 4.7.2 was ready.
- Business-hours calculation assumes no Western Australian public holiday on 16 to 19 Nov 2026. Confirm.

## Attempts
1. Darwin gateways rebooted by customer before the 01:05 call. Result: no difference (reported).
2. 01:05, Marcus Lee logged the ticket as P2 during the call. Result: ticket created, first response.
3. By 01:25, Marcus Lee checked fleet status in TernCloud. Result: 47 online, 14 offline, all G4-C at Darwin and Katherine.
4. 01:32, Marcus Lee emailed the customer after call-back with findings and asked for front-panel lights. Result: customer replied at 03:05.
5. By 02:10, Marcus Lee checked SIM status in Tern Connect. Result: all 14 Active, last sessions ended 18:21 to 18:24 UTC 14 Nov, no attempts since.
6. 02:05, Marcus Lee sent remote SMS wake to DRW-GW-01, DRW-GW-05, KTH-GW-02. Result: no response by 02:10.
7. Morning of 16 Nov (before 03:05), Darwin site lead power-cycled all 11 Darwin units again. Result: lights unchanged (solid green power, flashing amber NET).
8. 03:40, Marcus Lee advised the customer not to factory-reset. Result: no response yet.
9. 03:50, escalated to Tier 2. Result: Tier 2 owns the ticket.

## Commitments to the customer
| Commitment | Made by | When | Quote |
| --- | --- | --- | --- |
| Call back within the hour after checking the fleet | Marcus Lee, Support Agent Tier 1 | 01:05 UTC 16 Nov (phone call) | "I told him I'd check the fleet and call him back within the hour." (call note; the 01:32 email says "as discussed on the phone just now", so the call-back appears to have happened, within the hour) |
| Follow up the previous week's call or ticket if the customer names who he spoke to | Marcus Lee, Support Agent Tier 1 | 01:32 UTC 16 Nov | "If you can tell me who you spoke to, I'll follow it up." (conditional; the customer has not named anyone) |
| Customer update by 12:00 AWST Tue 17 Nov (04:00 UTC), or sooner if engineering has news | Marcus Lee, Support Agent Tier 1 | 03:40 UTC 16 Nov | "I'll send you an update by 12:00 AWST tomorrow, Tuesday 17 November (04:00 UTC), or sooner if engineering has news." (OPEN; Tier 2 now owns it per policy 5.3) |

No fix date, credit, refund or compensation has been promised. Marcus explicitly said "I can't give you a fix date." Only the Account Manager (Rhys Kaplan) or the Head of Customer Support may offer a credit, per policy 6.3; the customer has attributed fault to Tern and cited financial loss but has not asked for compensation in the thread.

## Service level
Term: Business plan, P2. First response "4 business hours"; resolution "27 business hours" (policy 3.1; plan from account record, Business). Targets count business hours only (3.3). Business hours are 00:30 to 09:30 UTC Mon to Fri (1.1, 1.2).
Clock start: ticket creation, 01:05 UTC Mon 16 Nov (09:05 AWST, inside business hours) (policy 4.1; thread event 01:05). No "Pending customer" status in the thread, so the clock has not been paused (4.2). Priority unchanged (4.3).
First response: met. The ticket was logged by an agent during the call at 01:05, which counts as first response (policy 1.4).
Deadline: resolution at 01:05 UTC Thu 19 Nov (09:05 AWST), assuming no public holiday. Working: 8h25m on Mon (01:05 to 09:30), 9h on Tue, 9h on Wed totals 26h25m; 35 minutes more reaches 01:05 Thu.
Status: Within target as of 03:50 UTC 16 Nov. 2h45m elapsed, 24h15m of 27h remaining. "At risk" threshold is under 6h45m remaining (25% of 27h) (policy 4.4).
Note: P1 would be a different target (24 hours, 24x7, clause 3.1) but P1 does not apply (2.1).

## Recommended next action
Action: Tier 2 to diagnose and restore cellular registration on the 14 G4-C gateways (Darwin 11, Katherine 3) on firmware 4.7.2, starting with whether the MX-31.4 modem firmware is the cause, and to find a recovery path that does not factory-reset units.
Reason: the only separator between offline and online units is model (G4-C versus G4-E). SIMs are active and the units are not registering on the network (flashing amber NET). The 4.7.2 release notes name a G4-C-only modem change that coincides with the loss time.
It must satisfy:
- The customer update due by 04:00 UTC Tue 17 Nov (12:00 AWST), sooner if there is news, covering diagnosis status and the Katherine check.
- Resolution within the 27 business hour target, by 01:05 UTC Thu 19 Nov. This is a deadline, not a promise: make no fix-date promise to the customer (policy 6.2).
- Preserve stored readings on the units: no factory resets; keep the customer's instruction in place.
- Follow up the customer's "Tern engineer said 4.7.2 was safe" claim if the customer identifies the person; otherwise check internally.
- Route any credit or compensation request to Rhys Kaplan or the Head of Customer Support (6.3). Do not discuss it at Tier 2 level.
- Correct the customer's picture: 47 of 61 gateways are online with complete data, so their statement that every site is affected is wrong. Do this tactfully in the update, as it affects their dispatch decisions.
Assumptions and checks:
- MX-31.4 causes the fault: unconfirmed; check by comparing modem logs or firmware version on a G4-C against a G4-E, or by roll-back test on a unit.
- Units hold readings: unconfirmed; verify before any recovery step.
- Katherine units show the same symptoms as Darwin: unverified; ask for LED status.
- No public holiday in 16 to 19 Nov: unverified; confirm to make the deadline firm.
- Priority stays at P2: if more gateways go offline (over 30 of 61), reassess for P1, which restarts the target as P1 from creation (4.3).
