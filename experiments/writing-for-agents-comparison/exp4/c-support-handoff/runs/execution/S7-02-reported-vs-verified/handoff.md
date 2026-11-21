# Handoff: TRN-77102, Coldwater Freight (CWF-2210), gateways offline after firmware 4.7.2

## Problem as understood
14 of 61 Coldwater gateways (all G4-C cellular, at Darwin and Katherine) stopped reporting to TernCloud during the 14 Nov firmware window and have not returned. The 47 G4-E Ethernet units are online and complete. The customer says all gateways are affected; the thread shows otherwise. As of 2026-11-16 03:50 UTC the ticket is P2, escalated to Tier 2.
- Verified: 61 gateways in fleet; 47 online and reporting normally, 14 offline (evidence: TernCloud fleet view at 01:25 UTC, Marcus Lee email 01:32; account record fleet table)
- Verified: all 14 offline units last reported 18:20-18:24 UTC on 14 Nov, during the window that started 18:00 UTC (evidence: TernCloud, Lee 01:32)
- Verified: all 61 were updated to 4.7.2; the 47 online units run 4.7.2 (evidence: TernCloud, Lee 01:32)
- Verified: the 14 offline units are all G4-C; the 47 online are all G4-E (evidence: Lee internal note 02:10, matches account record)
- Verified: all 14 SIMs are Active, last data sessions ended 18:21-18:24 UTC 14 Nov, no attempts since (evidence: Tern Connect console, Lee 02:10)
- Verified: SMS wake to DRW-GW-01, DRW-GW-05, KTH-GW-02 at 02:05 UTC got no response by 02:10 (evidence: Lee 02:10)
- Unconfirmed hypothesis (Tern, not customer): 4.7.2 release notes list "cellular modem firmware updated to MX-31.4 (G4-C only)"; a link is possible, not confirmed (Lee 02:10)
- Reported: Darwin units show solid green power and flashing amber NET light, unchanged after power-cycling (customer, 2026-11-16 03:05; Lee's 03:40 LED-guide reading, amber NET = modem not registered, is not independently confirmed)
- Reported: Darwin units were rebooted before the call (customer, call note 01:05)
- Reported: Katherine units not yet checked or touched (customer, 03:05)
- Reported: "every gateway" is affected, Perth cannot dispatch Darwin loads without certificates (customer, 01:12, 03:05). Contradicted by TernCloud for Perth and Adelaide.
- Reported: temperature data lost "for the last three days" (customer, 01:12). Unconfirmed: G4s store readings locally, and the offline units last reported about 1.3 days before the call.
- Reported: cost of about $40,000 a day (customer, 01:12)
- Reported: an unnamed Tern engineer said "last week" that 4.7.2 was fixed and safe (customer, 01:12, 03:05). No matching call or ticket found by support (Lee 01:32).

## Tried so far
- Customer rebooted all 11 Darwin units, Grant Tobias's team, before 01:05 on 16 Nov: no change (customer-reported)
- Fleet status check in TernCloud, Marcus Lee, 01:25: found 14 offline, 47 online
- Call-back and email to customer, Marcus Lee, 01:32: findings shared; requested LED status from Darwin
- SIM check in Tern Connect, Marcus Lee, 02:10: all Active, no sessions since 14 Nov
- Remote SMS wake to 3 units, Marcus Lee, 02:05: no response
- Customer power-cycled all 11 Darwin units again, 16 Nov morning: lights unchanged (customer-reported, 03:05)
- Customer asked not to factory-reset units (would erase stored readings), Marcus Lee, 03:40: no reply recorded
- Not tried: Katherine LED check, any action on the other 11 Darwin units by SMS, any fix or rollback

## Commitments to the customer
- Update by 12:00 AWST Tue 17 Nov (04:00 UTC), or sooner, by Marcus Lee, 2026-11-16 03:40: "I'll send you an update by 12:00 AWST tomorrow, Tuesday 17 November (04:00 UTC), or sooner if engineering has news." Tier 2 now owns this (policy 5.3).
- Call-back within the hour, by Marcus Lee, 01:05 (call note): "I told him I'd check the fleet and call him back within the hour." Met at 01:32 (call-back email).
- Follow-up on last week's alleged call, by Marcus Lee, 01:32: "If you can tell me who you spoke to, I'll follow it up." Conditional on the customer naming the engineer. Not named at 03:05.
- No fix date, credit, refund or compensation promised. 03:40: "I can't give you a fix date." The customer's statement "this one is on Tern" is a claim; no one at Tern accepted it.

## Service level
Tier: Business (source: account record). Priority: P2 (recorded on ticket 01:05; customer's P1 request not applied, policy 2.5; 14/61 = 23% offline, below the half needed for P1 in 2.1). Target: resolution 27 business hours; first response 4 business hours (policy 3.1). Clock started: 2026-11-16 01:05 UTC (09:05 AWST Monday, inside business hours, 4.1); never "Pending customer", so no paused time (4.2). First response: met at 01:05 (logged during the call, 1.4). Deadline: Thu 2026-11-19 01:05 UTC (09:05 AWST). Working: 01:05-09:30 UTC Mon = 8h25m; Tue 9h and Wed 9h (00:30-09:30 UTC each) = 26h25m; 35m more from 00:30 UTC Thu gives 01:05 UTC Thu. Elapsed at 03:50 UTC: 2h45m; remaining 24h15m of 27h. At-risk line is under 6h45m (25%, 4.4). Status: on track (within target). Assumes no WA public holiday on 17-19 Nov; none is stated in the inputs. Update cadence: P2 needs at least one update each business day (7.1); the 17 Nov 04:00 UTC commitment satisfies this for Tuesday.

## Recommended next action
Tier 2 to diagnose the G4-C cellular modem failure on 4.7.2 (check MX-31.4 modem firmware and registration behaviour on a Darwin unit), and have the customer check Katherine LEDs now. Reason: the offline set matches the G4-C model exactly and the SIMs are active, so the fault is probably on the gateway side. Open question: does the Katherine LED pattern match Darwin, and can any G4-C unit be reached or recovered remotely (the answer decides between a remote fix and a site visit)?
- Alternative: if the modem firmware is confirmed as cause, plan a rollback or corrective firmware for the 14 G4-C units, with the customer's rollout schedule (customer-scheduled rollouts).
- Alternative: if remote recovery fails, plan an on-site visit (Darwin and Katherine) to recover units and retrieve stored readings, keeping the no-factory-reset instruction.

## Gaps
- Conflict: customer says all gateways affected; TernCloud and the account record show 14 of 61 (Darwin and Katherine only). Not reconciled; the customer's Perth dispatch statement is unexplained.
- Conflict: customer says three days of data lost; offline since 18:20 UTC Sat 14 Nov, and local storage may hold the readings. Data loss is not confirmed either way.
- Unverified: the alleged engineer statement that 4.7.2 was safe. No record found. Do not accept or deny liability.
- Customer's P1 request is recorded on the thread only; any priority change would reset the resolution target per policy 4.3 (counted from creation).
- Support Team Lead notification (policy 5.2) applies to P1 or at-risk P2; not required now (ticket is not at risk). No credit or compensation may be offered by Tier 2; only the Account Manager (Rhys Kaplan) or the Head of Customer Support may, in writing (6.3). The customer cites a loss of $40,000 a day, so loop in the Account Manager.
- Not in the inputs: reply to the no-factory-reset request, Katherine status, SMS wake results for the other 11 units.
