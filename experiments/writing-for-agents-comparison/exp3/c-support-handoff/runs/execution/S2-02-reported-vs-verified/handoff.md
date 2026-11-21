# Escalation handoff: TRN-77102 14 cellular (G4-C) gateways offline since firmware 4.7.2 rollout

**Customer:** Coldwater Freight Pty Ltd (CWF-2210), Business support plan (account record: Account ID, Support plan)
**Earliest deadline:** 2026-11-17 04:00 UTC (12:00 AWST Tue): customer update promised by Marcus Lee, now owned by Tier 2 (thread, Marcus Lee, 16 Nov 03:40 UTC; policy 5.3)

## Problem as currently understood
14 of Coldwater's 61 gateways, all G4-C cellular units at Darwin (11) and Katherine (3), stopped reporting at 18:20 to 18:24 UTC on Sat 14 Nov during the 4.7.2 firmware window; all 47 Ethernet G4-E units on the same firmware are online with complete data. The SIMs are Active on the carrier side but have made no session attempts since, and the units did not answer SMS wake. Open hypotheses are that the 4.7.2 cellular modem firmware (MX-31.4, G4-C only) is involved and that the modem is not registering on the mobile network.

### Verified
- Fleet is 61 gateways: 47 online and reporting, 14 offline (thread, Marcus Lee, 16 Nov 01:32 UTC, TernCloud as of 01:25 UTC)
- Offline units are Darwin (11) and Katherine (3) (thread, Marcus Lee, 16 Nov 01:32 UTC; matches account record: Gateway fleet)
- Each offline unit last reported 18:20 to 18:24 UTC on Sat 14 Nov, during the firmware window that started 18:00 UTC (thread, Marcus Lee, 16 Nov 01:32 UTC)
- All 61 gateways were updated to 4.7.2 in that window; all 47 online units run 4.7.2 (thread, Marcus Lee, 16 Nov 01:32 UTC)
- Readings from the 47 online units are complete in TernCloud with no gaps; TernCloud has no readings from the 14 offline units after their last report (thread, Marcus Lee, 16 Nov 01:32 UTC)
- All 14 offline units are G4-C (cellular); all 47 online units are G4-E (Ethernet) (thread, Marcus Lee internal note, 16 Nov 02:10 UTC; account record: Gateway fleet)
- All 14 SIMs are status Active; their last data sessions ended 18:21 to 18:24 UTC on 14 Nov, with no session attempts since (thread, Marcus Lee internal note, 16 Nov 02:10 UTC, Tern Connect console)
- The 4.7.2 release notes include "cellular modem firmware updated to MX-31.4 (G4-C only)" (thread, Marcus Lee internal note, 16 Nov 02:10 UTC)
- No record of a call or ticket with Coldwater last week; last ticket was TRN-75530, closed 2 Oct (thread, Marcus Lee, 16 Nov 01:32 UTC; account record: Recent tickets)

### Reported, not verified
- His team rebooted all Darwin gateways before the call, with no difference (thread, call note by Marcus Lee, 16 Nov 01:05 UTC)
- Every Darwin unit shows solid green power and flashing amber NET (thread, Grant Tobias, 16 Nov 03:05 UTC)
- All 11 Darwin units were power-cycled again on 16 Nov morning and the lights came back the same (thread, Grant Tobias, 16 Nov 03:05 UTC)
- Katherine units have not been touched (thread, Grant Tobias, 16 Nov 03:05 UTC)
- Impact of about $40,000 a day in stock that cannot be certified for delivery (thread, Grant Tobias, 16 Nov 01:12 UTC)
- Perth cannot dispatch the Darwin loads without the certificates, so "every site is affected" (thread, Grant Tobias, 16 Nov 03:05 UTC)
- Customer asked for P1 (thread, ticket event and call note, 16 Nov 01:05 UTC; Grant Tobias, 16 Nov 01:12 UTC)

### Contradicted
- "Every one of our gateways went dark" / all gateways stopped reporting (thread, call note 16 Nov 01:05 UTC; Grant Tobias, 16 Nov 01:12 UTC): 47 of 61 are online and reporting; 14 are offline (thread, Marcus Lee, 16 Nov 01:32 UTC)
- "We've lost all our temperature data for the last three days" (thread, Grant Tobias, 16 Nov 01:12 UTC): data from the 47 online units is complete; for the 14 offline units, G4 gateways store readings locally, so loss cannot yet be determined; outage began 14 Nov 18:20 UTC (thread, Marcus Lee, 16 Nov 01:32 UTC)

### Hypotheses
- The 4.7.2 cellular modem firmware update (MX-31.4, G4-C only) is linked to the outage; "Possible link; not confirmed", proposed by Marcus Lee (thread, internal note, 16 Nov 02:10 UTC)
- The cellular modem is not registered on the mobile network (LED guide reading of the reported flashing amber NET), pointing to a gateway-side problem rather than the SIM accounts, proposed by Marcus Lee (thread, 16 Nov 03:40 UTC)
- The firmware push caused the outage and "this one is on Tern", proposed by Grant Tobias (thread, 16 Nov 01:12 UTC)

## Tried so far
| # | Action | By | Result | Source |
| --- | --- | --- | --- | --- |
| 1 | Rebooted all Darwin gateways | Customer (Grant Tobias's team) | No difference (reported) | Call note, Marcus Lee, 16 Nov 01:05 UTC |
| 2 | Checked fleet status in TernCloud as of 01:25 UTC | Marcus Lee | 47 online, 14 offline (Darwin 11, Katherine 3); all on 4.7.2; offline since 18:20 to 18:24 UTC 14 Nov | Marcus Lee, 16 Nov 01:32 UTC |
| 3 | Searched for last week's call or ticket | Marcus Lee | None found; last ticket TRN-75530 closed 2 Oct | Marcus Lee, 16 Nov 01:32 UTC |
| 4 | Checked the 14 SIMs in Tern Connect console | Marcus Lee | All Active; last sessions ended 18:21 to 18:24 UTC 14 Nov; no attempts since | Internal note, Marcus Lee, 16 Nov 02:10 UTC |
| 5 | Compared hardware models and 4.7.2 release notes | Marcus Lee | Offline all G4-C, online all G4-E; release includes modem firmware MX-31.4 for G4-C only | Internal note, Marcus Lee, 16 Nov 02:10 UTC |
| 6 | Sent remote SMS wake to DRW-GW-01, DRW-GW-05, KTH-GW-02 at 02:05 UTC | Marcus Lee | No response from any by 02:10 UTC | Internal note, Marcus Lee, 16 Nov 02:10 UTC |
| 7 | Checked front-panel LEDs on Darwin units, at support's request | Customer (Darwin site lead) | Solid green power, flashing amber NET on every unit (reported) | Request: Marcus Lee, 16 Nov 01:32 UTC; result: Grant Tobias, 16 Nov 03:05 UTC |
| 8 | Power-cycled all 11 Darwin units again | Customer (Darwin site) | Lights came back the same (reported) | Grant Tobias, 16 Nov 03:05 UTC |
| 9 | Read the LED state against the LED guide | Marcus Lee | Flashing amber NET on G4-C means modem not registered on the mobile network | Marcus Lee, 16 Nov 03:40 UTC |
| 10 | Told customer not to factory-reset any unit, as it would erase stored readings | Marcus Lee | Result not recorded | Marcus Lee, 16 Nov 03:40 UTC |
| 11 | Escalated to Tier 2 (Field Systems Engineering), priority P2 unchanged | Marcus Lee | Status Open to Escalated | Ticket event, 16 Nov 03:50 UTC |

## Commitments to the customer
| Commitment (quoted) | Made by | When | Due | Kept / Missed / Open | Source |
| --- | --- | --- | --- | --- | --- |
| "I told him I'd check the fleet and call him back within the hour" | Marcus Lee (by phone, recorded in his call note) | 16 Nov 01:05 UTC | "within the hour" = 16 Nov 02:05 UTC | Kept: call-back and fleet check reported "on the phone just now" (Marcus Lee, 16 Nov 01:32 UTC) | Call note, 16 Nov 01:05 UTC |
| "If you can tell me who you spoke to, I'll follow it up." | Marcus Lee | 16 Nov 01:32 UTC | No time stated | Open: customer could not give a name (Grant Tobias, 16 Nov 03:05 UTC) | Marcus Lee, 16 Nov 01:32 UTC |
| "I'm escalating this to our Field Systems Engineering team now." | Marcus Lee | 16 Nov 03:40 UTC | "now" | Kept (ticket event, 16 Nov 03:50 UTC) | Marcus Lee, 16 Nov 03:40 UTC |
| "I'll send you an update by 12:00 AWST tomorrow, Tuesday 17 November (04:00 UTC), or sooner if engineering has news." | Marcus Lee | 16 Nov 03:40 UTC | 2026-11-17 04:00 UTC | Open; Tier 2 now owns it (policy 5.3) | Marcus Lee, 16 Nov 03:40 UTC |

Customer-claimed, not found in thread:
- A Tern engineer said on the phone "last week that 4.7.2 was fixed and safe to roll out"; engineer's name not known; no record of the call or a ticket found (Grant Tobias, 16 Nov 01:12 and 03:05 UTC; Marcus Lee, 16 Nov 01:32 UTC; account record: Recent tickets)

## Service level
- Tier and priority: Business plan (account record: Support plan; policy 1.3); P2, assigned by Marcus Lee and unchanged at escalation (ticket events, 16 Nov 01:05 and 03:50 UTC). Customer's P1 request is not applied (policy 2.5); P1 needs more than half of gateways offline (policy 2.1), and 14 of 61 are offline (Marcus Lee, 16 Nov 01:32 UTC).
- Clock: starts at ticket creation, 16 Nov 01:05 UTC (09:05 AWST Mon), inside business hours 00:30 to 09:30 UTC (policy 1.1, 1.2, 4.1). No "Pending customer" status in the thread, so no pauses (policy 4.2; ticket events).
- Team Lead notification at escalation not required: ticket is P2 and was not at risk at 03:50 UTC (policy 5.2).
- Status as of: 2026-11-16 03:50 UTC, the last thread timestamp (current time not used)

| Target (quoted) | Policy section | Clock start / pauses | Deadline (arithmetic) | Status |
| --- | --- | --- | --- | --- |
| Business P2 first response: "4 business hours" | 3.1, 1.4 | Start 16 Nov 01:05 UTC; no pauses | 01:05 + 4 bh = 16 Nov 05:05 UTC; ticket logged during the call at 01:05 UTC counts as first response (1.4) | Met (16 Nov 01:05 UTC) |
| Business P2 resolution: "27 business hours" | 3.1, 3.3, 4.1, 4.4 | Start 16 Nov 01:05 UTC; no pauses | Mon 01:05 to 09:30 = 8h25m; + Tue 9h = 17h25m; + Wed 9h = 26h25m; + Thu 00:30 to 01:05 = 35m; total 27h, deadline Thu 19 Nov 01:05 UTC (09:05 AWST) | Not yet due: 2h45m used, 24h15m business hours remaining. At risk (under 25% = 6h45m left, 4.4) from Wed 18 Nov 03:20 UTC (Mon 8h25m + Tue 9h + Wed 00:30 to 03:20 = 2h50m; 20h15m used) |
| P2 updates: "at least once each business day" | 7.1 | Business days per 1.1 | Mon 16 Nov: updates sent 01:32 and 03:40 UTC; Tue 17 Nov: by end of business day, 09:30 UTC (17:30 AWST) | Mon: Met. Tue: Not yet due, 29h40m remaining (commitment above falls earlier, 04:00 UTC) |

## Recommended next action
Send Grant Tobias an update by 2026-11-17 04:00 UTC as Marcus promised, and do not promise a fix date or compensation (policy 6.2). Test whether 4.7.2 with modem firmware MX-31.4 stops a G4-C modem registering on the mobile network, for example by updating a lab G4-C on the same carrier, because every offline unit is G4-C with an active SIM but no session attempts since the update window. Ask the customer to read the LEDs on the untouched Katherine units to confirm they match Darwin, and to keep all units un-reset so stored readings survive.

## Gaps
- Katherine units' LED state and condition not reported; Darwin LED state is reported by the customer, not seen by support
- Whether readings stored locally on the 14 offline units survive is unknown (Marcus Lee, 16 Nov 01:32 UTC)
- Root cause unconfirmed; the MX-31.4 link is a hypothesis only
- The "engineer last week" claim is unresolved: no name, no record
- Customer's business impact ($40,000 a day, Perth dispatch blocked) is unverified
- Policy excludes WA public holidays from business hours (1.1) but lists none; assumed no public holiday between 16 and 19 Nov, which the resolution deadline depends on
- Technical contact Lina Petrakis (account record: Contacts) has not been involved in the thread
