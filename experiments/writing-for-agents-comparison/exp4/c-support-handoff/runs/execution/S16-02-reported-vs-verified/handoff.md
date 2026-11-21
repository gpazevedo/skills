# Handoff: TRN-77102, Coldwater Freight (CWF-2210), to Tier 2 Field Systems Engineering

As-of: 2026-11-16 03:50 UTC (11:50 AWST, Monday). Plan: Business. Priority: P2 (recorded).

## 1. Problem as understood
14 of 61 TernGate gateways (all G4-C cellular, Darwin 11 and Katherine 3) stopped reporting to TernCloud at about 18:20 UTC on 14 Nov, during the firmware 4.7.2 rollout, and have not returned. The 47 G4-E Ethernet gateways (Perth, Adelaide) are online; the cause is not yet known.

Evidence:
- Verified (TernCloud fleet view, Marcus Lee, 01:32): 47 online and reporting with no gaps, 14 offline, all in Darwin and Katherine. Each last reported 18:20 to 18:24 UTC on 14 Nov. All 61 were updated to 4.7.2 in that window (rollout start 18:00 UTC).
- Verified (Tern Connect console, Marcus Lee internal note 02:10): all 14 SIMs are Active; last data sessions ended 18:21 to 18:24 UTC on 14 Nov; no session attempts since.
- Verified (same note): all 14 offline units are G4-C and all 47 online units are G4-E. The model separates the groups.
- Verified (release notes, per 02:10 note): 4.7.2 includes "cellular modem firmware updated to MX-31.4 (G4-C only)". Link to the outage is a hypothesis, not confirmed.
- Reported (Grant Tobias, 03:05): all Darwin units show solid green power and flashing amber NET. Marcus (03:40) cites the LED guide: flashing amber NET on a G4-C means the modem is not registered on the mobile network. The lights themselves are not Verified by Tern; Katherine lights are unknown.
- Reported, contradicted: "ALL gateways offline" (01:12) and "every site is affected" (03:05). TernCloud shows 47 of 61 online. Perth cannot dispatch Darwin loads without certificates is Reported and unverified.
- Reported, unverified: "lost all temperature data for the last three days"; about $40,000 per day impact; "an engineer told me last week 4.7.2 was fixed and safe". Marcus found no record of that call or ticket (01:32); the customer cannot name the engineer (03:05).

Open questions:
- Is the modem on the 14 units failing under MX-31.4, or stuck for another reason?
- Do the offline units hold buffered readings, and will they upload on reconnect? Data loss is unknown.
- What do the Katherine units show?
- Did anyone at Tern make the claimed "4.7.2 is safe" statement?

## 2. Tried so far
- Darwin staff power-cycled all 11 units (customer, before 01:05): failed, no change. Repeated this morning (reported 03:05): failed, same lights.
- Marcus Lee checked the TernCloud fleet and Tern Connect SIM status (01:25 to 02:10): done; SIMs are Active, so a SIM account fault looks unlikely.
- Marcus Lee sent a remote SMS wake to DRW-GW-01, DRW-GW-05 and KTH-GW-02 at 02:05 UTC: no response by 02:10. Inconclusive; no later check is recorded.
- Katherine units: nothing tried.
- Customer told not to factory-reset (03:40), to protect stored readings.

## 3. Commitments to the customer
- Marcus Lee, 01:05 call: call back within the hour. Done (call-back and email by 01:32).
- Marcus Lee, 03:40: an update by 12:00 AWST Tuesday 17 Nov (04:00 UTC), or sooner if engineering has news. Open. Tier 2 owns it under policy 5.3.
- Soft assurance: Marcus, 01:32, "doesn't change how seriously we're taking it". No expectation set.
- No fix date, credit, refund or compensation has been promised. Marcus explicitly declined a fix date (03:40).
- The customer's claim of a prior engineer's assurance is not a commitment: no maker or date is shown in the thread.

## 4. Service-level status
- Plan: Business (account record, contract 1 Jul 2025 to 30 Jun 2027). Priority P2, recorded at creation. The customer's P1 request is recorded but not applied (policy 2.5). P1 needs more than half offline (2.1); 14 of 61 is 23%.
- Clause: policy 3.1 Business P2: first response 4 business hours; resolution 27 business hours.
- Clock start: ticket created 2026-11-16 01:05 UTC (09:05 AWST), inside business hours (00:30 to 09:30 UTC). No "Pending customer" time, so no pause.
- First response: met. The ticket was logged during the call (policy 1.4) at 01:05.
- Elapsed: 01:05 to 03:50 = 2h45m. Remaining: 24h15m of 27h (90%). Status: within target.
- Deadline: 27h from creation. Mon 16 Nov has 8h25m (01:05 to 09:30 UTC); Tue 17 has 9h (running 17h25m); Wed 18 has 9h (26h25m); Thu 19 needs 35m, so the deadline is Thu 2026-11-19 01:05 UTC (09:05 AWST).
- At risk (under 25%, so under 6h45m left) from about Wed 18 Nov 03:20 UTC (11:20 AWST) if unresolved.
- Breach trigger: the policy only defines "breached" and the at-risk escalation duty (5.1, 5.2). It states no credit or penalty.
- Assumption: no WA public holiday on 16 to 19 Nov; the policy supplies no holiday list, so this is unchecked.
- Resolution (policy 1.5) needs every fault on the ticket resolved. A separate data-loss fault would have to be resolved too.
- Customer updates: P2 needs one update per business day (7.1).
- Support Team Lead notification (5.2) applies to at-risk P2s. The ticket is not at risk, and the thread records no notification.

## 5. Recommended next action
Primary: a Tier 2 Field Systems Engineer should test the hypothesis that the MX-31.4 modem firmware in 4.7.2 stops G4-C modems registering on the network. Start with the three SMS-wake units (DRW-GW-01, DRW-GW-05, KTH-GW-02): check modem logs and carrier registration, and look for known issues, a recovery path or a rollback for G4-C. Reason: the only Verified discriminator is the G4-C model, SIMs are Active, and power cycles and SMS wake have failed. Begin now, because it decides whether this can be fixed remotely or needs site visits.

Unverified and still needed: the cause, recoverability without a factory reset, and whether buffered data survives.

Customer-facing update due: by 04:00 UTC Tue 17 Nov (12:00 AWST), Tier 2 to send, even if only a status update. Do not promise a fix date, credit or refund (6.2). Direct any credit or compensation request to Account Manager Rhys Kaplan (6.3). Do not accept the "engineer said it was safe" claim as fact. Ask Grant for the date, time and number used, and keep the factory-reset warning. Ask Katherine to report their LED states.
Re-check the priority if more gateways go offline.
