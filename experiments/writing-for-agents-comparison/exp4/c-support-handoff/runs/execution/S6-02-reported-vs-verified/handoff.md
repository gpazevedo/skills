## Escalation handoff: TRN-77102 14 cellular (G4-C) gateways offline since 4.7.2 rollout
As of: 2026-11-16, 03:50 UTC (11:50 AWST)
Customer: Coldwater Freight Pty Ltd (CWF-2210), Business plan, contract 1 Jul 2025 to 30 Jun 2027, TernCloud Fleet. 61 gateways: Kewdale PER 30 G4-E, Wingfield ADL 17 G4-E (both Ethernet), Darwin DRW 11 G4-C, Katherine KTH 3 G4-C (both cellular). Customer-scheduled firmware rollouts. Contacts: Grant Tobias (Operations Manager, primary), Lina Petrakis (IT Manager, technical). Account Manager: Rhys Kaplan.

### Problem as currently understood
After the firmware 4.7.2 rollout on Sat 14 Nov, all 14 G4-C cellular gateways (Darwin 11, Katherine 3) stopped reporting and have not reconnected. The 47 G4-E Ethernet gateways are online and reporting. The leading explanation is the cellular modem firmware update to MX-31.4 bundled in 4.7.2 (G4-C only), but this is a hypothesis, not confirmed. Customer-side power cycles did not help.
Evidence:
- [Verified] 61 gateways, all updated to 4.7.2 in the window starting 18:00 UTC 14 Nov; 47 online and reporting with no gaps, 14 offline (Marcus Lee, TernCloud check at 01:25 UTC 16 Nov)
- [Verified] The 14 offline units are exactly the 11 Darwin and 3 Katherine units; they last reported 18:20 to 18:24 UTC 14 Nov (Marcus Lee, TernCloud, 01:25 UTC)
- [Verified] All 14 SIMs are status Active; last data sessions ended 18:21 to 18:24 UTC 14 Nov; no session attempts since (Marcus Lee, Tern Connect console, 02:10 UTC)
- [Verified] All 14 offline units are G4-C and all 47 online units are G4-E; the 4.7.2 release notes list "cellular modem firmware updated to MX-31.4 (G4-C only)" (Marcus Lee, 02:10 UTC; model also in account record)
- [Verified] Remote SMS wake sent to DRW-GW-01, DRW-GW-05, KTH-GW-02 at 02:05 UTC: no response by 02:10 (Marcus Lee)
- [Reported] Darwin units show solid green power light and flashing amber NET light, unchanged after power cycling all 11 on Mon morning (Grant Tobias, 03:05 UTC, relaying Darwin site lead). Marcus Lee reads amber NET as modem not registered on the mobile network, per the LED guide (not confirmed on a unit)
- [Reported] Darwin gateways were rebooted before the 01:05 call with no change (Grant Tobias, call)
- [Reported] Katherine units have not been touched or checked (Grant Tobias, 03:05 UTC)
- [Reported] "All gateways" are affected, "all temperature data lost for three days", Perth cannot dispatch Darwin loads without certificates, about $40,000 a day in uncertifiable stock (Grant Tobias). The first two are contradicted by the verified fleet check above (Perth and Adelaide online; the offline units dropped out Sat evening). Whether data is stored on the offline units is unknown: G4 units buffer readings locally (Marcus Lee, stated as general behaviour, not checked on these units)

### Tried so far
- 14 Nov to 16 Nov, customer: power-cycled all 11 Darwin units, twice (before the call and again Mon morning) → no change [Reported]
- 16 Nov 01:25 UTC Marcus Lee: fleet status check in TernCloud → 47 online, 14 offline, all G4-C [Verified]
- 16 Nov 02:05 UTC Marcus Lee: remote SMS wake to 3 units → no response by 02:10 [Verified]
- 16 Nov 02:10 UTC Marcus Lee: SIM status check in Tern Connect → all Active, no session attempts since 14 Nov [Verified]
- 16 Nov 03:40 UTC Marcus Lee: told customer not to factory-reset (would erase stored readings) [Verified, sent in email]
- Not done: no unit-level logs, modem firmware version, or Katherine LED check; SMS delivery receipt not recorded.

### Commitments to the customer
- Call back within the hour of the 01:05 call | made by Marcus Lee, Support Agent T1, on 16 Nov 01:05 UTC | due 02:05 UTC | met (call-back and email by 01:32 UTC)
- "I'll send you an update by 12:00 AWST tomorrow, Tuesday 17 November (04:00 UTC), or sooner if engineering has news" | made by Marcus Lee on 16 Nov 03:40 UTC | due Tue 17 Nov 04:00 UTC | open, 24h10m remaining
- Policy 5.3: Tier 2 now owns this ticket, including the 04:00 UTC Tue update.
- Not commitments: Marcus said he cannot give a fix date; no credit or compensation has been offered by anyone.

### Service level
- Priority P2 under policy 2.2 (some gateways offline, no practical workaround); plan Business. Customer requested P1; not applied. Policy 2.1 needs more than half offline, and 14/61 (23%) is not. The priority is supported by the Verified fleet check.
- First response: deadline 05:05 UTC 16 Nov (4 business hours, 3.1; clock starts at creation 01:05 UTC, inside business hours 00:30 to 09:30 UTC) | met at 01:05 UTC (1.4: ticket logged during the call counts as first response)
- Resolution: deadline Thu 19 Nov 01:05 UTC, 09:05 AWST (27 business hours, 3.1; 9h a day: Mon 01:05 to 09:30 = 8h25m, Tue 9h, Wed 9h, leaves 0h35m, so Thu 00:30 + 0h35m; no Pending customer pause, no public holidays assumed) | open, 24h15m business hours remaining of 27h (elapsed 2h45m); within target (4.4: at-risk threshold is under 6h45m remaining)
- Customer update (7.1, P2: at least once each business day): next due by end of Tue 17 Nov business day (09:30 UTC); Marcus's own commitment of 04:00 UTC is earlier and governs | open
- Priority would change to P1 only if more than half (31 or more) of gateways go offline; the resolution target would then be 24 hours calendar from creation (4.3), i.e. 01:05 UTC Tue 17 Nov.

### Recommended next action
Tier 2 engineer: confirm or rule out the MX-31.4 modem firmware hypothesis on one Darwin unit and one Katherine unit (pull the modem firmware version and network registration state from the console or logs, and compare with a G4-E unit and the 4.7.2 release notes), and send the customer an update by 04:00 UTC Tue 17 Nov (12:00 AWST), sooner if the result is known. Only the modem hypothesis is supported by the Verified evidence, and nothing yet shows the cause.
Then: ask the customer (Lina Petrakis) for the Katherine unit LED states, and the name of the engineer from "last week" if recalled; ask what the 14 offline units are used for so the data-retrieval plan (readings stored on the units) can be set up before any reset or reflash.

### Gaps
- No unit-level evidence of the cause; modem firmware link is unconfirmed.
- Whether the offline units hold stored readings, and how much data is at risk, is unknown. Customer's "three days" of lost data is Reported and does not match the Saturday evening failure time.
- Customer claims an engineer last week said 4.7.2 was "fixed and safe to roll out", so "this one is on Tern": [Reported] commitment/assurance, not found in thread; Marcus found no record of a call or ticket (last ticket TRN-75530, closed 2 Oct). No fix date, credit or compensation is committed. Policy 6.2 bars agents from promising these; credits can only be offered by Rhys Kaplan or the Head of Customer Support (6.3), and the account has no open credits. The customer's $40,000 a day loss is Reported.
- Customer's claim that Perth is affected is contradicted by the check; Perth and Adelaide are online.
- Team Lead notification (5.2) is not required: the ticket is P2 and not at risk.
- Policy silent on public holidays beyond "WA public holidays"; none assumed between 16 and 19 Nov.
