# Handoff: TRN-77102, Coldwater Freight (CWF-2210), as of 2026-11-16 03:50 UTC (11:50 AWST)

## 1. Problem as understood
After the 14 Nov firmware 4.7.2 rollout, 14 of 61 gateways (all 11 Darwin and 3 Katherine G4-C cellular units) stopped reporting and show a flashing amber NET light. The 47 G4-E Ethernet units are online and reporting. The customer says all gateways are affected and that data has been lost. Support has not verified either claim. The cause is unconfirmed; the leading hypothesis is the 4.7.2 cellular modem update (MX-31.4, G4-C only).

Evidence:
- 14 offline units are all G4-C; 47 online units are all G4-E and run 4.7.2. Verified (M. Lee, TernCloud and account record fleet table, 16 Nov 01:25 and 02:10 UTC).
- The 14 offline units last reported 18:20 to 18:24 UTC on 14 Nov, in the rollout window (started 18:00 UTC). Verified (M. Lee, TernCloud, 16 Nov 01:32; Tern Connect sessions ended 18:21 to 18:24, 02:10).
- All 14 SIMs are status Active and there have been no session attempts since. Verified (M. Lee, Tern Connect console, 02:10).
- Online units have complete readings with no gaps. Verified (M. Lee, TernCloud, 01:32).
- Darwin units show solid green power and flashing amber NET after power cycles. Reported (G. Tobias, 03:05, relayed by Darwin site lead). Support's reading that amber NET means "modem not registered" comes from the LED guide, not from a check of the units.
- Link to modem firmware MX-31.4: hypothesis only. Support noted it as "possible link; not confirmed" (M. Lee, 02:10; release notes).
- "Every gateway went dark" and "every site is affected": Reported (Tobias, 01:12, 03:05). Contradicted by the verified 47 online units.
- "Lost all temperature data for the last three days": Reported (Tobias, 01:12). Unverified. Offline units were last seen about 1.3 days before the call. G4 units store readings locally and upload on reconnect, so loss is unknown (M. Lee, 01:32).
- A Tern engineer told Tobias the previous week that 4.7.2 was fixed and safe: Reported, unconfirmed. Support found no record of a call or ticket (M. Lee, 01:32); the only recent ticket is TRN-75530 (account record). The engineer is unnamed.
- Business impact of about $40,000 per day and Perth unable to dispatch Darwin loads without certificates: Reported (Tobias, 01:12, 03:05).
- Open contradiction: the customer asked for P1; the verified count is 14/61 offline (23%).

## 2. Tried and result
- Customer (Darwin): power-cycled all 11 units, then again the morning of 16 Nov. Failed, no change in lights (Tobias, 01:05, 03:05).
- Marcus Lee: checked fleet status in TernCloud. Fault isolated to the 14 G4-C units.
- Marcus Lee: checked SIM status in Tern Connect. All Active. SIM accounts are ruled out as a cause on the carrier side.
- Marcus Lee: remote SMS wake to DRW-GW-01, DRW-GW-05, KTH-GW-02 at 02:05 UTC. No response by 02:10. Later outcome unknown.
- Katherine: no one has touched the units yet. Untried.
- Ruled out: a fleet-wide 4.7.2 failure (Ethernet units fine) and SIM deactivation (see above). Not ruled out: modem firmware MX-31.4.
- Customer was told not to factory-reset units, to preserve stored readings.

## 3. Commitments to the customer
- M. Lee, 16 Nov 01:05 (call): check the fleet and call back within the hour. Met (email after call-back at 01:32).
- M. Lee, 16 Nov 03:40: "I'll send you an update by 12:00 AWST tomorrow, Tuesday 17 November (04:00 UTC), or sooner if engineering has news." Open. Tier 2 owns this (policy 5.3).
- M. Lee, 03:40: asked the customer not to factory-reset. This is an instruction, not a promise.
- No fix date, credit, refund or compensation has been promised; M. Lee said he "can't give you a fix date". The customer implies Tern is liable ("this one is on Tern"). Unconfirmed customer assertion about last week's engineer: see section 1.

## 4. Service-level status and deadline
- Plan: Business (account record). Priority: P2, recorded on the ticket (policy 2.5). The customer's P1 request was recorded and not applied. P2 fits policy 2.1/2.2: 14/61 is under half offline, so P1 does not apply (2.1 needs more than half).
- Targets, policy 3.1 (Business, P2): first response 4 business hours; resolution 27 business hours. Business hours are 00:30 to 09:30 UTC, Mon to Fri (1.1, 1.2); targets count business hours only (3.3).
- Clock start (4.1): ticket created Mon 16 Nov 01:05 UTC (09:05 AWST), inside business hours.
- First response: the ticket was logged during the customer's call, which counts when logged (1.4). Met at 01:05, so 0 of 4 hours were used.
- Pause (4.2): only while status is "Pending customer". The thread shows statuses Open then Escalated, never Pending customer, so no paused time. Assumption: no WA public holiday on 16 to 19 Nov (no holiday list was supplied).
- Resolution arithmetic: Mon 01:05 to 09:30 = 8h25. Tue 9h and Wed 9h make 26h25. Remaining 0h35 falls on Thu 19 Nov from 00:30 UTC, so the deadline is Thu 19 Nov 2026 01:05 UTC (09:05 AWST).
- Elapsed at 03:50 UTC: 2h45; remaining 24h15 of 27h. Status: within target (4.4).
- At risk (under 25% = 6h45 remaining) begins Wed 18 Nov 03:20 UTC (11:20 AWST). Breached if unresolved after Thu 19 Nov 01:05 UTC.
- Resolution (1.5) needs a fix or workaround and status Resolved. The ticket also carries the data-loss concern, but only one fault (offline units) is logged.
- Escalation: policy 5.1 allows it when documented procedures cannot resolve it. 5.2 (notify Support Team Lead) applies only to P1 or at-risk P2; this ticket is neither, so it is not required. The thread records no notice.
- Next customer-contact deadline: Tue 17 Nov 04:00 UTC (committed). Policy 7.1 also requires a P2 update at least once each business day.
- Policy does not state: any service credit or liability terms for outages; only 6.2/6.3 limits on who may offer one.

## 5. Recommended next action
Primary action: Tier 2 (Field Systems Engineering engineer) tests the modem hypothesis before the Tue 04:00 UTC update, aiming to meet the Thu 19 Nov 01:05 UTC resolution target. Check the 4.7.2 and MX-31.4 known issues with firmware engineering, and ask for one Darwin unit's NET and modem status (and one Katherine unit, since none has been power-cycled). If the modem registration failure is confirmed, plan a recovery or workaround path that preserves stored readings (no factory reset). If not confirmed, request device logs and escalate for unit-level diagnosis.
Rationale: only G4-C units failed and their SIMs are Active (section 1), so the cheapest discriminating check is the modem firmware, not more SIM or reboot attempts.

Customer contact: send an update by Tue 17 Nov 04:00 UTC (12:00 AWST) even if only to report progress. Do not promise a fix date, credit or refund (6.2). Any credit question goes to Account Manager Rhys Kaplan or the Head of Customer Support (6.3). Ask Grant for the name of the engineer he spoke to and for Darwin and Katherine confirmation of any change in LEDs.
