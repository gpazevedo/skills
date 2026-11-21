# Escalation handoff: TRN-77102 All 14 cellular (G4-C) gateways offline since the 4.7.2 firmware rollout

**Customer:** Coldwater Freight Pty Ltd (CWF-2210), Business plan | **Priority:** P2 (set by Marcus Lee, Tier 1 agent; customer requested P1, not applied)
**Service level:** within target, next deadline 2026-11-17 04:00 UTC (customer update commitment; 24h10m away from the as-of time 2026-11-16 03:50 UTC). Resolution deadline 2026-11-19 01:05 UTC.
**Open commitments:** 2, earliest due 2026-11-17 04:00 UTC (the second has no stated time)

## Problem as currently understood
Of 61 gateways, 14 (all 11 Darwin and 3 Katherine units, all G4-C cellular) stopped reporting between 18:20 and 18:24 UTC on 14 Nov, during the firmware 4.7.2 rollout; the 47 online units (all G4-E Ethernet) run 4.7.2 and report normally (Verified, Marcus Lee, 01:32 and 02:10 notes). The SIMs are Active on the carrier side and no data sessions have been attempted since 18:24 UTC (Verified, Marcus Lee, console, 02:10). Marcus Lee's hypothesis is that the 4.7.2 cellular modem firmware update (MX-31.4, G4-C only) is the cause, and that the flashing amber NET light means the modem is not registered on the mobile network; neither is confirmed. Whether readings stored on the 14 units are intact is unknown.

| Fact | Tag | Source |
|---|---|---|
| Fleet has 61 gateways: Kewdale 30 G4-E, Wingfield 17 G4-E, Darwin 11 G4-C, Katherine 3 G4-C | Verified (account record) | account.md fleet table |
| 14 gateways offline, 47 online, as of 01:25 UTC 16 Nov | Verified (Marcus Lee, TernCloud) | thread, 01:32 email |
| The 14 offline are Darwin (11) and Katherine (3); each last reported 18:20-18:24 UTC Sat 14 Nov, in the rollout window (started 18:00 UTC) | Verified (Marcus Lee, TernCloud) | thread, 01:32 email |
| All 61 gateways were updated to 4.7.2; the 47 online units run 4.7.2 | Verified (Marcus Lee, TernCloud) | thread, 01:32 email |
| 47 online units have complete readings, no gaps | Verified (Marcus Lee, TernCloud) | thread, 01:32 email |
| All 14 offline units are G4-C; all 47 online units are G4-E | Verified (Marcus Lee; consistent with account record) | thread, 02:10 note; account.md |
| All 14 SIMs are Active; last data sessions ended 18:21-18:24 UTC 14 Nov; no attempts since | Verified (Marcus Lee, Tern Connect console) | thread, 02:10 note |
| No response to SMS wake sent to DRW-GW-01, DRW-GW-05, KTH-GW-02 by 02:10 UTC | Verified (Marcus Lee) | thread, 02:10 note |
| Release notes for 4.7.2 include "cellular modem firmware updated to MX-31.4 (G4-C only)" | Reported (Marcus Lee quoting release notes; not seen by this handoff) | thread, 02:10 note |
| The MX-31.4 modem update may be the cause | Hypothesis (Marcus Lee: "Possible link; not confirmed") | thread, 02:10 note |
| Flashing amber NET on a G4-C means modem not registered on mobile network; points to a gateway-side problem rather than SIM accounts | Hypothesis (Marcus Lee, citing the LED guide; "I can't confirm the cause yet") | thread, 03:40 email |
| Darwin units show solid green power light and flashing amber NET light, unchanged after power-cycling | Reported (Darwin site lead via Grant Tobias) | thread, 03:05 email |
| Darwin team rebooted all Darwin gateways after the update, no difference; all 11 power-cycled again on 16 Nov | Reported (Grant Tobias) | thread, 01:05 call note and 03:05 email |
| Katherine units have not been touched or power-cycled | Reported (Grant Tobias) | thread, 03:05 email |
| Customer says "every one" of their gateways went dark, and "every site is affected" | Reported, contradicted by the 47 online G4-E units (Perth and Adelaide) | thread, 01:12 and 03:05 emails vs 01:32 email |
| Customer says all temperature data lost for the last three days | Reported; the 14 units went offline about 1.4 days before the as-of time, and stored-reading loss is unconfirmed | thread, 01:12 email; 01:32 email |
| Perth cannot dispatch Darwin loads without the certificates | Reported (Grant Tobias) | thread, 03:05 email |
| Business impact about $40,000 a day in stock that cannot be certified | Reported (Grant Tobias) | thread, 01:12 email |
| G4 gateways store readings locally when offline and upload on reconnect | Reported (Marcus Lee, as product behaviour; not observed on these units) | thread, 01:32 email |
| An engineer told the customer "last week" that 4.7.2 was fixed and safe; Tern has no record of a call or ticket (last ticket TRN-75530, closed 2 Oct) | Reported by customer; the absence of a record is Verified by Marcus Lee (account tickets) | thread, 01:12, 01:32, 03:05; account.md |

**Open questions:** What is the actual cause (modem firmware MX-31.4, or something else)? What are the modem state, registration status and firmware version on the offline units? Are readings stored on the 14 units intact? Do the three Katherine units show the same lights as Darwin (not yet reported)? Did any Tern engineer tell the customer 4.7.2 was fixed, and who (customer cannot name him)? Is the data loss the customer describes real, given the 47 online units are complete?

## What has been tried
| Action | By | When | Result |
|---|---|---|---|
| Checked fleet status in TernCloud | Marcus Lee | 01:25 UTC 16 Nov | 14 offline, 47 online (see facts) |
| Rebooted all Darwin gateways | Customer (Darwin team) | after the update, before 01:05 UTC 16 Nov (date and time not recorded) | No difference (Reported) |
| Power-cycled all 11 Darwin units again | Customer (Darwin site lead) | morning of 16 Nov (time not recorded; before 03:05 UTC) | Lights unchanged: solid green power, flashing amber NET (Reported) |
| Checked Tern Connect console for the 14 SIMs | Marcus Lee | by 02:10 UTC 16 Nov | All Active, no sessions since 18:24 UTC 14 Nov |
| Model check of offline vs online units | Marcus Lee | by 02:10 UTC 16 Nov | All offline are G4-C, all online G4-E |
| Remote SMS wake to DRW-GW-01, DRW-GW-05, KTH-GW-02 | Marcus Lee | 02:05 UTC 16 Nov | No response by 02:10 UTC; later result not recorded |
| Asked Darwin for front-panel lights on 2-3 units | Marcus Lee | 01:32 UTC 16 Nov | Answered 03:05 UTC (see facts) |
| Asked customer not to factory-reset units (would erase stored readings) | Marcus Lee | 03:40 UTC 16 Nov | Instruction only; compliance not recorded |
| Searched for the claimed call/ticket from last week | Marcus Lee | by 01:32 UTC 16 Nov | No record found |

## Commitments to the customer
| Commitment (quoted) | Made by | When | Status |
|---|---|---|---|
| "I'd check the fleet and call him back within the hour" (call note; told to customer on the call) | Marcus Lee | 01:05 UTC 16 Nov (call) | Met: call-back email sent 01:32 UTC, inside the hour (deadline 02:05 UTC) |
| "If you can tell me who you spoke to, I'll follow it up." (about last week's alleged engineer call) | Marcus Lee | 01:32 UTC 16 Nov | Open. Customer replied at 03:05 UTC that he does not remember the name; no follow-up is recorded and no time was stated |
| "I'm escalating this to our Field Systems Engineering team now." | Marcus Lee | 03:40 UTC 16 Nov | Met: escalated 03:50 UTC |
| "I'll send you an update by 12:00 AWST tomorrow, Tuesday 17 November (04:00 UTC), or sooner if engineering has news." | Marcus Lee | 03:40 UTC 16 Nov | Open, due 2026-11-17 04:00 UTC. Tier 2 now owns it (policy 5.3) |

**Requested, not committed:** P1 priority (declined, recorded 03:50 UTC); implied acceptance of liability ("this one is on Tern") and any compensation for the roughly $40,000 a day, with no credit requested explicitly and none offered; a fix date (Marcus Lee: "I can't give you a fix date"); an explanation of the earlier "fixed" claim. Account record shows Open credits: None.

## Service level
Measured at 2026-11-16 03:50 UTC (the as-of time in the thread export, Monday). Readings used for ambiguous terms: (1) no WA public holiday is assumed between 16 and 19 Nov, since the policy refers to holidays but supplies no list; (2) a "business hour" is an hour inside 00:30-09:30 UTC Mon-Fri, so a business day is 9 hours; (3) the ticket status has not been "Pending customer", so no pause time is deducted; (4) the "not currently P1" status is taken as correct, since 14 of 61 is under half.

Plan Business (account.md), priority P2 (set by Marcus Lee, thread 01:05 and 03:50). Policy 2.1: P1 is "more than half of the customer's gateways are offline"; 14/61 is about 23%, so P2 stands (policy 2.5: "a priority applies only once recorded on the ticket").

| Target (policy quote) | Clock start | Deadline (arithmetic) | Status |
|---|---|---|---|
| First response, Business P2: "4 business hours" (3.1); "A ticket logged by an agent during a call with the customer counts as a first response when logged" (1.4) | Ticket created 01:05 UTC 16 Nov (4.1); inside business hours | Logged at 01:05 UTC, 0h elapsed against the 4h target (would have been 05:05 UTC) | Met |
| Resolution, Business P2: "27 business hours" (3.1) | 01:05 UTC Mon 16 Nov | Mon: 01:05 to 09:30 = 8h25m, leaving 18h35m. Tue 17: 9h, leaving 9h35m. Wed 18: 9h, leaving 0h35m. Thu 19: starts 00:30, plus 0h35m = 01:05 UTC. Deadline 2026-11-19 01:05 UTC (09:05 AWST Thu) | Within target. Elapsed 2h45m (01:05 to 03:50), 24h15m of 27h remain |
| At-risk threshold (4.4): "less than 25% of its resolution target remains", 25% of 27h = 6h45m | Same | At risk when elapsed exceeds 20h15m: Mon 8h25m + Tue 9h = 17h25m, plus 2h50m Wed from 00:30 = 2026-11-18 03:20 UTC | Not yet at risk; at risk from 03:20 UTC Wed 18 Nov |
| Update cadence, P2: "at least once each business day" (7.1) | Business day | Tue 17 Nov by 09:30 UTC at the latest. Today's business day already has Marcus's 03:40 UTC update. The customer commitment of 04:00 UTC is earlier and governs | Within target |

Pauses: policy 4.2: "The clock is paused only while the ticket status is 'Pending customer'." No such status appears in the thread.

Escalation notes (policy 5.2): the Support Team Lead must be notified at escalation only for a P1 or an at-risk P2; the ticket is neither, and the thread records no such notification. If priority is later raised to P1 (more than 31 of 61 offline would be needed, so unlikely), 4.3 restarts the target at 24 hours calendar from creation, which would be 01:05 UTC 17 Nov.

## Recommended next action
Own recommendation: Field Systems Engineering (Tier 2 on duty) should check the modem state on the G4-C units: confirm the firmware and modem version on a sample of the 14 units in TernCloud and Tern Connect, compare with the 4.7.2 release notes for MX-31.4, and check whether the carrier shows any registration attempts. In parallel, ask Lina Petrakis (technical contact) to have Katherine, which is untouched, report the NET and power lights on one unit without power-cycling or resetting. Owner: Tier 2 Field Systems Engineering, with a first finding by 2026-11-16 09:30 UTC (end of business hours today), because the 04:00 UTC Tue 17 customer update is open and Tier 2 owns it, the P2 resolution deadline is 2026-11-19 01:05 UTC, and the stored readings on the 14 units are at risk if a reset is attempted. Also reply to the customer on the unresolved "last week's engineer" follow-up when the update is sent.
