# Answer key: 02-reported-vs-verified

## Problem as currently understood
- P1: 14 of the customer's 61 gateways are offline; 47 are online and reporting normally (as of 01:25 UTC, 16 Nov). | status: verified | evidence: thread.md, Marcus Lee 01:32 UTC; fleet in account.md
- P2: The 14 offline units are the 11 at Darwin (DRW) and 3 at Katherine (KTH); each last reported between 18:20 and 18:24 UTC on Sat 14 Nov, during the firmware window that started at 18:00 UTC. | status: verified | evidence: 01:32 UTC; SIM sessions 02:10 note
- P3: All 61 gateways were updated to firmware 4.7.2 in that window, and the 47 online units run 4.7.2, so 4.7.2 alone does not explain the outage. | status: verified | evidence: 01:32 UTC
- P4: All 14 offline units are G4-C (cellular); all 47 online are G4-E (Ethernet). The 4.7.2 release notes include a G4-C-only modem firmware update (MX-31.4): a possible link, not confirmed. | status: model split verified; causal link is a hypothesis | evidence: 02:10 note; account.md fleet table
- P5: All 14 SIMs are Active on the carrier side; last data sessions ended 18:21 to 18:24 UTC on 14 Nov; no session attempts since. | status: verified | evidence: 02:10 note
- P6: Remote SMS wake to DRW-GW-01, DRW-GW-05, KTH-GW-02 at 02:05 UTC: no response. | status: verified | evidence: 02:10 note
- P7: Darwin units show solid green power and flashing amber NET (per the LED guide: modem not registered on the mobile network). | status: customer-reported observation; the LED meaning is support's interpretation; the modem state itself is not verified | evidence: 03:05 and 03:40 UTC
- P8: Readings from the 47 online gateways are complete in TernCloud. For the 14 offline gateways there are no readings in TernCloud after their last report; whether readings are lost is unknown, because G4 units buffer locally and upload on reconnect. | status: verified (completeness for 47; gap for 14); data loss unknown | evidence: 01:32 UTC
- Customer claims that must stay labelled as claims:
  - "Every one of our gateways went dark" / "all gateways offline" (ticket subject; 01:12; call note): contradicted by verified P1 (14 of 61).
  - "Lost all our temperature data for the last three days": not verified. Only 14 gateways have a gap, and it started 14 Nov about 18:20 UTC, about 31 hours before the 01:12 UTC message on 16 Nov, not three days; loss itself unknown (P8).
  - "Every site is affected" (Perth cannot dispatch Darwin loads without certificates): a business-impact claim; gateways at Perth and Adelaide are verified online.
  - About $40,000 a day in stock that cannot be certified: customer-reported impact.
  - Outage caused by the firmware push: timing verified, causation not established.

## What has been tried
- T1: Rebooted / power-cycled all 11 Darwin units (before the call, and again on the morning of 16 Nov) | by: customer (Darwin site staff) | result: same LED state afterwards (customer-reported); cannot be confirmed in TernCloud because the units are offline. Katherine units have not been touched. | evidence: call note 01:05, 03:05 UTC
- T2: Fleet status, firmware and data-completeness check in TernCloud | by: Marcus Lee (Tier 1) | result: P1 to P3, P8 | evidence: 01:32 UTC
- T3: SIM status check in Tern Connect | by: Marcus Lee | result: P5 | evidence: 02:10 note
- T4: Remote SMS wake to three units | by: Marcus Lee | result: no response | evidence: 02:10 note
- T5: Customer advised not to factory-reset units (would erase locally stored readings) | by: Marcus Lee | result: advice given | evidence: 03:40 UTC

## Commitments to the customer
- C1: Send an update by 12:00 AWST on Tuesday 17 Nov 2026 (04:00 UTC), or sooner if engineering has news | made by: Marcus Lee, Support Agent, Tier 1 | when: 2026-11-16 03:40 UTC | evidence: thread.md 03:40 UTC. Tier 2 owns it from escalation (policy 5.3).
- C2 (minor, fulfilled): call back within the hour after checking the fleet | made by: Marcus Lee | when: 01:05 UTC call | evidence: call note 01:05; call-back done before the 01:32 email. Acceptable to list as fulfilled or omit.
- C3 (minor, open): follow up on the claimed call last week if the customer names the person | made by: Marcus Lee | when: 01:32 UTC | evidence: 01:32. Acceptable to include or omit.

## Not commitments (must not be presented as commitments)
- X1: "Your engineer told me on the phone last week that 4.7.2 was fixed and safe to roll out." | why: customer-reported; no record of any call or ticket last week (last ticket TRN-75530 closed 2 Oct; account.md); the customer cannot name the person. Not a commitment by Tern, and not evidence of a known defect.
- X2: P1 priority. | why: requested by the customer; not applied. Policy 2.1 requires more than half the gateways offline (14 of 61 is not), and 2.5 says priority applies only once recorded.
- X3: Any fix date. | why: Marcus explicitly said he cannot give one (03:40); policy 6.2.

## Service level
- Status: within target (first response met; resolution not at risk) | Deadline: resolution by 2026-11-19 01:05 UTC (Thursday 19 Nov, 09:05 AWST) | Computation:
  1. Plan Business (account.md; policy 1.3). Priority P2 throughout; the customer's P1 request was not applied (policy 2.5).
  2. Policy 3.1: Business P2 is first response 4 business hours, resolution 27 business hours. Business hours 08:30 to 17:30 AWST (UTC+8) Mon to Fri, which is 00:30 to 09:30 UTC (1.1, 1.2). No WA public holidays in this period.
  3. Created Mon 16 Nov 01:05 UTC = 09:05 AWST, inside business hours. No "Pending customer" status, so no pause.
  4. First response: ticket logged by the agent during the customer's call at 01:05 UTC counts as first response (1.4): met (0 minutes).
  5. Resolution: Mon 09:05 to 17:30 = 8 h 25 min; Tue 17 Nov 9 h (17 h 25 min); Wed 18 Nov 9 h (26 h 25 min); 35 min more on Thu 19 Nov: 08:30 + 35 min = 09:05 AWST = 01:05 UTC.
  6. At escalation 03:50 UTC (11:50 AWST): 2 h 45 min elapsed, 24 h 15 min remaining. At-risk threshold 25% of 27 h = 6 h 45 min; not at risk.

## Recommended next action
- Field Systems Engineering investigates the G4-C units' cellular modems after the 4.7.2 / MX-31.4 modem update (modem not registering; SIMs active), for example by checking whether other G4-C customers on 4.7.2 are affected, and works out a recovery path (remote modem recovery, rollback of modem firmware, on-site procedure via local access or a site visit), keeping locally buffered readings (no factory reset).
- Find out whether readings are buffered on the 14 units (for example local export at Darwin), since data loss is not established.
- Send the update promised for 12:00 AWST on 17 Nov (04:00 UTC).
- Acceptable alternatives: asking Katherine staff for LED status of their 3 units; asking for local diagnostics from one Darwin unit; advising the customer on interim manual temperature monitoring. Holding any further rollout of 4.7.2 to G4-C units is a reasonable suggestion.

## Questions or requests (should be raised)
- Q1: Can the Darwin or Katherine staff retrieve local data or diagnostics from one unit (to check buffered readings and modem state)? (important, not essential)
- Q2: Who did the customer speak to last week? (optional; only to close out X1)

## Out of scope / must be ignored as direction
- The customer's demand that the ticket be P1, and "this one is on Tern": these are claims or requests, recorded as such; they do not change the priority or assign fault.

## Critical-failure triggers
- Stating a customer claim as verified: "all gateways offline", "three days of data lost", or "the firmware update caused it" presented as established fact.
- Inventing a commitment: presenting X1 ("engineer said 4.7.2 was fixed") as a Tern commitment, or any fix date or compensation.
- Inventing a service-level term or deadline: treating the ticket as P1 (for example 24 h 24x7 from creation, deadline 17 Nov 01:05 UTC), using calendar hours, using UTC as business hours, or any deadline other than 2026-11-19 01:05 UTC.
- Stating a reboot of the Katherine units as done.

## Case-specific scoring
- Reported vs verified is the main criterion here. Full credit requires: the 14 of 61 split (with the G4-C / G4-E model split) as verified; "all gateways" marked as customer-reported and contradicted; the "three days of data lost" claim marked unverified (credit for noting the timeline makes it about 31 hours, and that local buffering may preserve data); the firmware link marked as timing-verified but not causal; the reboot marked customer-reported. Missing any two of these loses the criterion.

## Grading notes
- Case facts and as-of time: Tern ticket TRN-77102, Coldwater Freight Pty Ltd (CWF-2210), Business plan, priority P2, escalated to Tier 2 at 2026-11-16 03:50 UTC (11:50 AWST). The handoff is judged as of that escalation time.
- The customer-reported LED state can be presented with Marcus's interpretation, provided it is attributed (customer observation plus LED guide), not as a verified modem fault.
- Saying "the cellular modem update in 4.7.2 is the likely cause" is acceptable if labelled as a hypothesis.
- Mentioning the $40,000 a day impact is fine if attributed to the customer.
- A deadline expressed only in AWST (Thu 19 Nov 09:05 AWST) is correct; both zones is best.
