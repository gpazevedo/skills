# Escalation handoff: TRN-77102 14 of 61 gateways (all G4-C cellular, Darwin and Katherine) offline since firmware 4.7.2 rollout

**Customer:** Coldwater Freight Pty Ltd (CWF-2210), Business support plan, Fleet subscription up to 75 gateways, 61 units (account record: Support plan, TernCloud subscription, Gateway fleet)
**Earliest deadline:** Tue 17 Nov 2026 04:00 UTC (12:00 AWST), customer update promised by Marcus Lee (thread, Marcus Lee 03:40 UTC). Time remaining at 03:50 UTC Mon 16 Nov: 24h10m. Resolution target deadline is Thu 19 Nov 01:05 UTC (see Service level).

## Problem as currently understood
14 gateways, all G4-C cellular units at Darwin (11) and Katherine (3), stopped reporting at 18:20-18:24 UTC on Sat 14 Nov during the firmware 4.7.2 rollout. They show active SIMs, no session attempts since, and a flashing amber NET light as reported by the customer. All 47 G4-E Ethernet units are online and complete. The hardware model separates the two groups; a link to the 4.7.2 cellular modem firmware update (MX-31.4) is an open hypothesis only.

### Verified
- Fleet is 61 gateways; 14 offline, 47 online and reporting normally (thread, Marcus Lee 01:32 UTC, TernCloud as of 01:25 UTC; account record Gateway fleet total of 61).
- The 14 offline units are Darwin (11) and Katherine (3) (thread, Marcus Lee 01:32 UTC; account record shows Darwin 11 and Katherine 3).
- Each offline unit last reported between 18:20 and 18:24 UTC on Sat 14 Nov, during the rollout that started at 18:00 UTC (thread, Marcus Lee 01:32 UTC; account record: default window Saturdays from 18:00 UTC).
- All 61 gateways were updated to 4.7.2 in that window; the 47 online units run 4.7.2 (thread, Marcus Lee 01:32 UTC).
- Readings from the 47 online units are complete, with no gaps (thread, Marcus Lee 01:32 UTC).
- All 14 offline units are G4-C (cellular) and all 47 online units are G4-E (Ethernet) (thread, Marcus Lee internal note 02:10 UTC; account record Model and Backhaul columns agree).
- All 14 SIMs are status Active in the Tern Connect console; last data sessions ended 18:21-18:24 UTC on 14 Nov; no session attempts since (thread, Marcus Lee internal note 02:10 UTC).
- Remote SMS wake sent to DRW-GW-01, DRW-GW-05 and KTH-GW-02 at 02:05 UTC; no response from any by 02:10 UTC (thread, Marcus Lee internal note 02:10 UTC).
- The 4.7.2 release notes include "cellular modem firmware updated to MX-31.4 (G4-C only)" (thread, Marcus Lee internal note 02:10 UTC; Marcus quotes the release notes, the notes themselves are not in the supplied material).

### Reported, not verified
- Darwin units show a solid green power light and a flashing amber NET light (thread, Grant Tobias 03:05 UTC, relayed from the Darwin site lead; no agent has seen this).
- Darwin units were power-cycled by the customer, on 16 Nov before 01:05 UTC (thread, Marcus Lee call note 01:05 UTC, Grant Tobias call) and again the morning of 16 Nov, with no change (thread, Grant Tobias 03:05 UTC).
- Katherine units have not been touched or checked by the customer (thread, Grant Tobias 03:05 UTC); Katherine front-panel state is unknown.
- Customer reports about $40,000 a day in stock that cannot be certified for delivery (thread, Grant Tobias 01:12 UTC).
- Customer says Perth cannot dispatch Darwin loads without the certificates (thread, Grant Tobias 03:05 UTC).
- Customer says the 14 units hold stored readings; unknown whether any data is lost. Marcus notes G4 units store readings locally and upload on reconnect (thread, Marcus Lee 01:32 UTC), but this has not been checked on these units.

### Contradicted
- "Every one of our gateways went dark" / "ALL gateways offline" / "every site is affected": 47 of 61 are online and reporting; Perth (Kewdale) and Adelaide (Wingfield) G4-E units are online (thread, Grant Tobias 01:12 UTC and 03:05 UTC vs Marcus Lee 01:32 UTC; account record Gateway fleet).
- "Lost all our temperature data for the last three days": the online units have complete data, and the offline units stopped reporting about 31 hours before the email, not three days (thread, Grant Tobias 01:12 UTC vs Marcus Lee 01:32 UTC). Loss on the 14 offline units is unconfirmed.

### Hypotheses
- Cellular modem firmware MX-31.4 in 4.7.2 is linked to the failure: "Possible link; not confirmed", proposed by Marcus Lee (thread, 02:10 UTC internal note).
- The fault is on the gateway side rather than the SIM accounts, because a flashing amber NET light on a G4-C means the modem is not registered on the network, per the LED guide; proposed by Marcus Lee, "I can't confirm the cause yet" (thread, 03:40 UTC). The light state itself is only reported.

## Tried so far
| # | Action | By | Result | Source |
| --- | --- | --- | --- | --- |
| 1 | Rebooted all Darwin gateways (before the call) | Customer (Darwin team) | "Made no difference" (customer's statement) | Thread, Marcus Lee call note 01:05 UTC |
| 2 | Checked fleet status in TernCloud (as of 01:25 UTC) | Marcus Lee | 47 online, 14 offline, all offline are Darwin and Katherine | Thread, Marcus Lee 01:32 UTC |
| 3 | Checked Tern Connect console for the 14 SIMs | Marcus Lee | All Active; last sessions 18:21-18:24 UTC 14 Nov; no attempts since | Thread, Marcus Lee 02:10 UTC |
| 4 | Compared model and firmware across groups | Marcus Lee | Offline = G4-C, online = G4-E; 4.7.2 notes mention MX-31.4 (G4-C only) | Thread, Marcus Lee 02:10 UTC |
| 5 | Remote SMS wake to DRW-GW-01, DRW-GW-05, KTH-GW-02 at 02:05 UTC | Marcus Lee | No response by 02:10 UTC | Thread, Marcus Lee 02:10 UTC |
| 6 | Asked Darwin to report front-panel lights on 2-3 units | Marcus Lee (request) | Lights reported as solid green power, flashing amber NET | Thread, Marcus Lee 01:32 UTC; Grant Tobias 03:05 UTC |
| 7 | Power-cycled all 11 Darwin units again (16 Nov morning) | Customer (Darwin team) | Lights unchanged | Thread, Grant Tobias 03:05 UTC |
| 8 | Searched for the prior call/ticket the customer cites | Marcus Lee | No record found; last ticket was TRN-75530 closed 2 Oct | Thread, Marcus Lee 01:32 UTC |
| 9 | Told customer not to factory-reset units (would erase stored readings) | Marcus Lee | Instruction given; customer's response not recorded | Thread, Marcus Lee 03:40 UTC |

## Commitments to the customer
| Commitment (quoted) | Made by | When | Due | Kept / Missed / Open | Source |
| --- | --- | --- | --- | --- | --- |
| "I told him I'd check the fleet and call him back within the hour." (Marcus's own note of what he told the customer) | Marcus Lee | 2026-11-16 01:05 UTC | Within the hour, i.e. by 02:05 UTC (resolved from the message timestamp) | Kept: call-back and email at 01:32 UTC ("as discussed on the phone just now") | Thread, call note 01:05 UTC; Marcus Lee 01:32 UTC |
| "I'll send you an update by 12:00 AWST tomorrow, Tuesday 17 November (04:00 UTC), or sooner if engineering has news." | Marcus Lee | 2026-11-16 03:40 UTC | Tue 17 Nov 2026 04:00 UTC (12:00 AWST), as stated | Open (owned by Tier 2 from escalation, policy 5.3) | Thread, Marcus Lee 03:40 UTC; policy 5.3 |

Customer-claimed, not found in thread:
- An unnamed Tern engineer told the customer "last week" that 4.7.2 "was fixed and safe to roll out" (thread, Grant Tobias 01:12 UTC and 03:05 UTC). Marcus found no record of the call or any ticket (thread, Marcus Lee 01:32 UTC). The customer also states that "this one is on Tern" (liability); no one at Tern has accepted this.

Possible expectation (non-committal statement): none treated as a promise by the customer.
No credit, refund or compensation has been offered or recorded; the account record shows Open credits: None. Under policy 6.2 and 6.3 support agents must not promise any, and only the Account Manager (Rhys Kaplan, account record) or the Head of Customer Support may offer one.

## Service level
- Tier and priority: Business plan (account record: Support plan); priority P2 recorded on the ticket at creation and unchanged at escalation (thread, ticket created 01:05 UTC; escalation event 03:50 UTC). The customer's P1 request is recorded but not applied (policy 2.5). Facts support P2: 14 of 61 (about 23%) offline is not more than half, so P1 criteria (policy 2.1) are not met; some gateways offline with no practical workaround matches policy 2.2.
- Status as of: 2026-11-16 03:50 UTC, the as-of time in the thread export (treated as current time).
- Clock: starts at ticket creation, Mon 16 Nov 01:05 UTC = 09:05 AWST, inside business hours (policy 4.1, 1.1, 1.2). No "Pending customer" status in the thread, so no pauses (policy 4.2); "Escalated" does not pause the clock.

| Target (quoted) | Policy section | Clock start / pauses | Deadline (arithmetic) | Status |
| --- | --- | --- | --- | --- |
| First response: "4 business hours" (Business, P2) | 3.1, 1.4 | Start 01:05 UTC 16 Nov; no pauses | Ticket logged by an agent during the customer's call counts as first response when logged (1.4): 01:05 UTC. Anyway 01:05 + 4h = 05:05 UTC, inside business hours | Met (at 01:05 UTC; email at 01:32 UTC also) |
| Resolution: "27 business hours" (Business, P2) | 3.1, 3.3, 4.1 | Start 01:05 UTC 16 Nov; no pauses | Mon 16: 01:05 to 09:30 = 8h25m. Tue 17: 00:30 to 09:30 = 9h, total 17h25m. Wed 18: 9h, total 26h25m. Remaining 35m on Thu 19: 00:30 + 35m = 01:05 UTC Thu 19 Nov (09:05 AWST) | Not yet due: elapsed 2h45m business time (01:05 to 03:50), 24h15m remaining |
| Customer update: "at least once each business day" (P2) | 7.1 | Business days | Update due on each business day; Mon 16 satisfied (01:32 and 03:40 UTC); Tue 17 covered by the 04:00 UTC commitment | Met for Mon 16; Tue 17 not yet due |

- Resolution health (policy 4.4): at risk means less than 25% of 27h (6h45m) remaining; 24h15m remaining is 89.8%, so within target.
- Policy 5.2 notification of the Support Team Lead applies only to P1 or at-risk P2 escalations; this P2 is not at risk, so it is not required by policy. The thread records no notification.
- Per policy 1.5, resolution requires a fix or workaround and status set to Resolved; one fault on the ticket (the 14 offline gateways).

## Recommended next action
Establish whether the 14 G4-C units' cellular modem is stuck after the MX-31.4 modem firmware update (the leading hypothesis, currently unconfirmed) by pulling device and modem logs or a test unit, and get Katherine front-panel state checked, since the amber NET light is only customer-reported. Send the customer an update by 04:00 UTC Tue 17 Nov (12:00 AWST) even if there is no news, and do not promise a fix date, credit or refund (policy 6.2; credits only via Rhys Kaplan). Keep the customer from factory-resetting units, which would erase stored readings.

## Gaps
- Western Australian public holidays for 16-19 Nov 2026 were not stated in the supplied material; the deadline assumes none, and a holiday would push the resolution deadline later.
- Results not recorded: the customer's reaction to the no-factory-reset instruction; whether the customer reported back on Katherine.
- Data loss on the 14 offline units is unknown; stored readings on units not confirmed.
- The prior engineer conversation is unverified; no record found. Liability claim ("on Tern") is unresolved and out of scope for support.
- The 4.7.2 release notes and LED guide are cited by Marcus Lee only; the documents themselves were not supplied.
- Whether the Support Team Lead was notified is not recorded (not required by policy 5.2 at current P2 / not at risk).
