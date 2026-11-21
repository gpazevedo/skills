# Escalation handoff: TRN-77102 14 of 61 Coldwater gateways (Darwin and Katherine G4-C) offline since 4.7.2 rollout

Reference time ("now"): 2026-11-16 03:50 UTC (11:50 AWST, Monday) (the export's stated as-of time, which is also the last thread message)
Inputs missing: none

## Problem as currently understood
Fourteen cellular G4-C gateways (Darwin 11, Katherine 3) stopped reporting between 18:20 and 18:24 UTC on 14 Nov, during the 4.7.2 firmware rollout. The 47 Ethernet G4-E units on the same firmware are online with complete readings. The carrier SIMs are active but the units show a flashing amber NET light, which the LED guide reads as "modem not registered on the mobile network". The leading hypothesis is that the cellular modem firmware update bundled in 4.7.2 (MX-31.4, G4-C only) left the modems unable to register. This is not confirmed. Customer-side power cycles at Darwin changed nothing, and whether any stored readings are lost is unknown.

- 61 gateways in the fleet: 30 G4-E Kewdale, 17 G4-E Wingfield, 11 G4-C Darwin, 3 G4-C Katherine [verified] (account record)
- 14 gateways offline as of 01:25 UTC, all at Darwin (11) and Katherine (3), last reporting 18:20 to 18:24 UTC on 14 Nov [verified] (Marcus Lee, 2026-11-16 01:32)
- All 61 were updated to 4.7.2 in the window; the 47 online units run 4.7.2 [verified] (Marcus Lee, 01:32)
- Readings from the 47 online units are complete, no gaps [verified] (Marcus Lee, 01:32)
- All 14 SIMs are Active, last data sessions ended 18:21 to 18:24 UTC on 14 Nov, no attempts since [verified] (Marcus Lee internal note, 02:10)
- All 14 offline units are G4-C and all 47 online units are G4-E [verified] (Marcus Lee internal note, 02:10; consistent with account record)
- The 4.7.2 release notes include "cellular modem firmware updated to MX-31.4 (G4-C only)" [verified] (Marcus Lee internal note, 02:10)
- The modem firmware update causes the outage [suspected] (Marcus Lee, 02:10: "Possible link; not confirmed")
- Darwin units show solid green power light and flashing amber NET light, unchanged after power cycling [reported] (Grant Tobias, 03:05, relaying the Darwin site lead; no Tern agent has seen the units)
- Flashing amber NET on a G4-C means the modem is not registered on the mobile network [reported] (Marcus Lee, 03:40, citing the LED guide; the guide itself is not in the case)
- The fault is on the gateway side rather than the SIM accounts [suspected] (Marcus Lee, 03:40: "I can't confirm the cause yet")
- Darwin gateways were rebooted with no effect [reported] (Grant Tobias, call note 01:05, and 03:05 for a second round)
- Katherine units have not been touched by the customer [reported] (Grant Tobias, 03:05)
- Readings may be held locally on the 14 units and upload on reconnect; any actual loss is unknown [suspected] (Marcus Lee, 01:32: "I can't yet tell whether any data has actually been lost")
- Impact of about $40,000 a day in stock that cannot be certified, and Perth cannot dispatch Darwin loads without certificates [reported] (Grant Tobias, 01:12 and 03:05)
- A Tern engineer told Grant "last week" that 4.7.2 was fixed and safe to roll out [reported] (Grant Tobias, 01:12 and 03:05; engineer unnamed)

Conflicts:
- Scope. Customer: "ALL gateways offline", "every site is affected" [reported] (Grant Tobias, 01:12, 03:05). Support: 14 of 61 offline, 47 online and reporting normally as of 01:25 UTC [verified] (Marcus Lee, 01:32). The fleet check is about 2h25m old at "now"; no later check is recorded.
- Data loss. Customer: "lost all our temperature data for the last three days" [reported] (01:12). Support: the 47 online units have complete readings, and loss on the 14 is undetermined [verified / suspected] (01:32). The outage began at 18:20 UTC on 14 Nov, about 1.3 days before the 01:12 email.
- Prior assurance. Customer says an engineer said 4.7.2 was fixed [reported] (01:12). Support: "I can't find a record of a call or a ticket with Coldwater last week" [verified: searched, nothing found] (Marcus Lee, 01:32). Absence of a record does not disprove the call.
- Priority. Customer asked for P1 (call note 01:05; email 01:12). Recorded priority is P2, with the P1 request recorded and not applied (event, 03:50).

## Tried so far
| When | Who | What | Result |
|------|-----|------|--------|
| before 2026-11-16 01:05 | Customer (Darwin team) | Rebooted all Darwin gateways | No difference (reported, call note 01:05) |
| 2026-11-16 01:25 | Marcus Lee | Checked fleet status in TernCloud | 47 online, 14 offline (Darwin and Katherine) |
| 2026-11-16 by 02:10 | Marcus Lee | Checked Tern Connect console for the 14 SIMs | All Active; last sessions 18:21 to 18:24 UTC 14 Nov; none since |
| 2026-11-16 by 02:10 | Marcus Lee | Compared hardware model and read the 4.7.2 release notes | Offline = G4-C, online = G4-E; MX-31.4 modem firmware note found; link unconfirmed |
| 2026-11-16 02:05 | Marcus Lee | Remote SMS wake to DRW-GW-01, DRW-GW-05, KTH-GW-02 | No response by 02:10; later result not recorded |
| 2026-11-16 03:05 (reported) "this morning" | Customer (Darwin, 11 units) | Power-cycled all 11 Darwin units again | Lights unchanged: solid green power, flashing amber NET |
| 2026-11-16 03:40 | Marcus Lee | Interpreted the LED guide against the SIM status | Points to the gateway side; cause unconfirmed |
| 2026-11-16 01:32 | Marcus Lee | Asked Darwin for front-panel lights on two or three units | Answered by Grant at 03:05 |

## Commitments to the customer
| When | Made by | Verbatim commitment | Status (met / pending / overdue) | Policy note |
|------|---------|---------------------|----------------------------------|-------------|
| 2026-11-16 01:05 | Marcus Lee | "I told him I'd check the fleet and call him back within the hour." (Marcus's call note; the words said to the customer are his own record) | met: Marcus's 01:32 email says "after call-back" and "as discussed on the phone just now"; the call time is not recorded, so completion within the hour (by 02:05) is inferred | 6.1: agents may commit to their own actions |
| 2026-11-16 03:40 | Marcus Lee | "I'll send you an update by 12:00 AWST tomorrow, Tuesday 17 November (04:00 UTC), or sooner if engineering has news." | pending; due 2026-11-17 04:00 UTC, 24h10m after "now"; owned by Tier 2 from escalation | 6.1 allows a next-update time; 5.3: Tier 2 owns commitments already made |

Not commitments: Grant's statement that an engineer said 4.7.2 was fixed is a claim [reported], not a Tern promise (no words in the thread by any Tern agent). Grant's "this one is on Tern" and the $40,000 a day figure imply a credit or compensation. None has been offered, the account record shows "Open credits: None", and no agent has promised one. Marcus wrote "I can't give you a fix date", which is consistent with 6.2 ("Support agents must not promise a fix date, a service credit, a refund or compensation."). Per 6.3, only the Account Manager (Rhys Kaplan) or the Head of Customer Support may offer a credit, valid only when recorded in writing on the ticket or account record.

## Service level
Plan from account record: Business. Priority recorded: P2 (set 2026-11-16 01:05, unchanged at 03:50). Under 2.1, P1 needs more than half of 61 gateways offline (at least 31); 14 are offline, so P2 under 2.2 fits the verified facts.

Clock 1: first response
- Clause: "3.1 ... Business | P2 | 4 business hours" and "1.4 ... A ticket logged by an agent during a call with the customer counts as a first response when logged."
- Clock: first response, business hours, started ticket creation 2026-11-16 01:05 UTC (09:05 AWST, inside business hours 00:30 to 09:30 UTC on a Monday)
- Deadline: 2026-11-16 05:05 UTC (01:05 + 4h, all inside the 00:30 to 09:30 UTC window)
- Status: met at 01:05 UTC (the ticket was logged by an agent during the call); also the 01:32 email. Missing terms: none

Clock 2: resolution
- Clause: "3.1 ... Business | P2 | ... 27 business hours"; "4.1 The clock starts when the ticket is created."; "4.2 The clock is paused only while the ticket status is 'Pending customer'."
- Clock: resolution, business hours, started ticket creation 2026-11-16 01:05 UTC. Status has gone Open then Escalated, never "Pending customer", so no paused time.
- Deadline: 2026-11-19 01:05 UTC (Thu 09:05 AWST). Arithmetic: Mon 01:05 to 09:30 = 8h25m; Tue 9h gives 17h25m; Wed 9h gives 26h25m; Thu from 00:30 needs 35m more, ending 01:05 UTC = 27h00m. This assumes no WA public holiday on 16 to 19 Nov (none is listed in the inputs).
- Elapsed at "now": 2h45m (01:05 to 03:50); remaining 24h15m. 25% of 27h = 6h45m; "at risk" applies below that.
- Status: open, within target, 24h15m business time remaining; not "at risk" under 4.4. Missing terms: none that changes the status (the public-holiday calendar is not supplied, but a holiday would only move the deadline later).
- If P1 were later applied (4.3): Business P1 resolution is "24 hours, 24x7", counted from creation, so the deadline would be 2026-11-17 01:05 UTC, with 21h15m left at "now" (calendar time).

Clock 3: customer update interval
- Clause: "7.1 ... P2: at least once each business day."
- Clock: business day; the last update to the customer was 03:40 UTC on 16 Nov (within today's business hours, ends 09:30 UTC). The next is committed for 2026-11-17 04:00 UTC, which is inside Tuesday's business hours.
- Status: met for 16 Nov; next due by 17 Nov 09:30 UTC at the latest by policy, 04:00 UTC by commitment. Missing terms: none

Escalation: 5.1 permits Tier 1 to Tier 2 when a ticket cannot be resolved with documented procedures. 5.2 (Support Team Lead notification) applies only to P1 or at-risk P2; the ticket is neither, so it is not required. The thread does not show whether the Lead was told.

## Open questions
- Whether any readings are lost on the 14 offline gateways (asked/raised by Marcus Lee, 2026-11-16 01:32; unanswered)
- Why the G4-C modems are not registering, and whether MX-31.4 is the cause (raised by Marcus Lee, 02:10 and 03:40; unanswered)
- Result of the SMS wake to DRW-GW-01, DRW-GW-05, KTH-GW-02 after 02:10 (sent by Marcus Lee, 02:05; no later result)
- The state of the Katherine units: lights not yet reported (asked of Darwin by Marcus Lee, 01:32; Grant said at 03:05 nobody at Katherine had touched them)
- Who the Tern engineer was who allegedly said 4.7.2 was safe (asked by Marcus Lee, 01:32; Grant at 03:05 did not know the name)
- Whether the fleet is still 14 of 61 offline (last check 01:25 UTC; Grant claims all gateways at all sites)
- Grant's request for P1 and implied liability or credit: priority decision recorded; no credit discussion has occurred (raised by Grant Tobias, 01:12)

## Recommended next action
Pull the 4.7.2 rollout and device logs for the 14 G4-C units from 18:00 to 18:25 UTC on 14 Nov, and check whether the MX-31.4 modem firmware update completed, failed or rolled back, compared against a G4-C unit (if any) that did not take the modem update. This tests the leading suspected cause directly and has not been run. Refresh the fleet count at the same time. Owner: Tier 2 Field Systems Engineering engineer on TRN-77102. By: 2026-11-16 09:30 UTC (end of today's business hours), so the result can feed the customer update due 2026-11-17 04:00 UTC. Rests on: ledger entries for the 02:10 internal note (all 14 offline are G4-C, MX-31.4 in the release notes, SIMs Active, link unconfirmed), the 02:05 SMS wake with no response, the customer's power cycles with no change, and the pending 04:00 UTC 17 Nov commitment now owned by Tier 2.
