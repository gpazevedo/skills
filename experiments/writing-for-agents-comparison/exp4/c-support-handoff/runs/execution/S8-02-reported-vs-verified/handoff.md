# Escalation handoff: TRN-77102 14 cellular gateways offline after firmware 4.7.2 update

**Customer:** Coldwater Freight Pty Ltd, account CWF-2210, Business plan (account record)  **Priority:** P2 (thread, 01:05 and 03:50 events; customer asked for P1, not applied)  **Prepared:** 2026-11-16 03:50 UTC (11:50 AWST), the thread's stated as-of time

## Service level
| Clock | Policy clause | Started | Deadline | Status |
|---|---|---|---|---|
| First response, Business P2: "4 business hours" | 3.1, 1.4, 4.1 | 2026-11-16 01:05 UTC (ticket created, in business hours) | 05:05 UTC 2026-11-16 | Met at 01:05 UTC: ticket was logged by an agent during the customer's call, which counts as first response when logged (1.4) |
| Resolution, Business P2: "27 business hours" | 3.1, 3.3, 4.1, 4.2 | 2026-11-16 01:05 UTC | 01:05 UTC Thu 2026-11-19 (09:05 AWST) | Running: 24h 15m of business time remaining. Within target (4.4) |
| Update interval, P2: "at least once each business day" | 7.1 | Last update 2026-11-16 03:40 UTC | Tue 2026-11-17 business day (00:30 to 09:30 UTC); agent has committed to 04:00 UTC | Running |

Arithmetic, resolution: business hours are 00:30 to 09:30 UTC, Mon to Fri (1.1, 1.2). Mon 16 Nov 01:05 to 09:30 = 8h25m; Tue 9h (total 17h25m); Wed 9h (total 26h25m); 27h minus 26h25m = 35m, so Thu 19 Nov 00:30 + 35m = 01:05 UTC. Elapsed at 03:50 UTC is 2h45m; remaining 24h15m. No "Pending customer" time so far (4.2). Assumes no WA public holiday on 16 to 19 Nov; none is stated in the case. "At risk" (4.4) means under 25% of 27h = 6h45m remaining, which would begin about 03:20 UTC Wed 18 Nov.
Priority gap: if the customer's requested P1 were recorded, Business P1 is "2 hours, 24x7" first response and "24 hours, 24x7" resolution (3.1), giving a resolution deadline of 01:05 UTC Tue 17 Nov (21h15m left at as-of). Under 2.5 a priority applies only once recorded, and 2.1 needs more than half of gateways offline (14 of 61 is 23%), so P2 stands. If the 4.3 priority change were ever made, the target is counted from ticket creation.
Escalation: 5.2 requires notifying the Support Team Lead only for P1 or at-risk P2; neither applies now, and no notification is recorded. Under 5.3 Tier 2 now owns the ticket, including the commitments below.

## Problem as currently understood
The 14 G4-C cellular gateways (Darwin 11, Katherine 3) stopped reporting 18:21 to 18:24 UTC on 14 Nov, during the 4.7.2 rollout, and have not tried to connect since. The 47 G4-E Ethernet gateways updated to 4.7.2 and are fine, so model/backhaul separates the groups. The leading suspect is the 4.7.2 cellular modem firmware change (MX-31.4, G4-C only), which is not confirmed.

| Fact | Status | Evidence |
|---|---|---|
| Fleet is 61 gateways: Perth 30 G4-E, Adelaide 17 G4-E, Darwin 11 G4-C, Katherine 3 G4-C | Verified | Account record fleet table; thread 01:32 (Marcus, TernCloud) |
| 47 gateways online and reporting, 14 offline, as of 01:25 UTC | Verified | TernCloud check, thread 01:32 |
| The 14 offline are all Darwin (11) and Katherine (3); each last reported 18:20 to 18:24 UTC Sat 14 Nov | Verified | TernCloud check, thread 01:32 |
| All 14 offline units are G4-C, all 47 online units are G4-E | Verified | Internal note 02:10; matches account record models |
| All 61 gateways updated to 4.7.2 in the customer's scheduled window (rollout from 18:00 UTC) | Verified for the 47 online units (TernCloud, 01:32); Reported/stated by agent for the 14 offline (their running version is not shown as checked) | Thread 01:32; account record (customer-scheduled rollouts, Saturday 18:00 UTC window) |
| The 47 online units have complete readings, no gaps | Verified | TernCloud check, thread 01:32 |
| All 14 SIMs are Active; last data sessions ended 18:21 to 18:24 UTC 14 Nov; no session attempts since | Verified | Tern Connect console, internal note 02:10 |
| SMS wake sent to DRW-GW-01, DRW-GW-05, KTH-GW-02 at 02:05 UTC: no response by 02:10 | Verified (for those 3 units, as of 02:10) | Internal note 02:10 |
| Darwin units show solid green power light and flashing amber NET light, unchanged after power-cycling | Reported (by the Darwin site lead via Grant); not checked by support | Thread 03:05 |
| Flashing amber NET on a G4-C means the modem is not registered on the mobile network | Reported by support from the LED guide (document not in the case) | Thread 03:40 |
| Fault is on the gateway side, not the SIM accounts | Suspected | Thread 03:40 ("can't confirm the cause yet") |
| 4.7.2 modem firmware update (MX-31.4, G4-C only) is the cause | Suspected | Internal note 02:10 ("Possible link; not confirmed") |
| Readings stored locally on the 14 units; whether any data is lost is unknown | Suspected (local storage is stated from G4 behaviour, not checked on these units) | Thread 01:32 |
| Katherine units not touched or checked; their lights are unknown | Verified gap | Thread 03:05 |
| About $40,000 a day cost in stock that cannot be certified for delivery | Reported | Thread 01:12 |
| Perth cannot dispatch Darwin loads without the certificates | Reported | Thread 03:05 |
| An engineer told Grant "last week" that 4.7.2 was "fixed and safe to roll out" | Reported; no record found | Thread 01:12, 03:05; Marcus found no call or ticket (01:32) and the last ticket is TRN-75530, closed 2 Oct (account record) |

Contradictions:
- Scope: Grant says "ALL gateways" went dark (subject, 01:12) and "every site is affected" (03:05). TernCloud shows 47 of 61 online and Perth and Adelaide reporting (01:32). Verified version: 14 of 61, Darwin and Katherine only.
- Duration: Grant says "lost all our temperature data for the last three days" (01:12). Offline units stopped reporting on 14 Nov 18:20 to 18:24 UTC, about 31 hours before the 01:05 UTC call on 16 Nov (01:32 note); online units have no gaps.
- Who pushed the update: Grant calls it "your firmware push" (01:12). The account record says rollouts are customer-scheduled, and Marcus calls it "your scheduled firmware window" (01:32). Who started the 14 Nov rollout is not shown in the case.
- Prior assurance: Grant says an engineer promised 4.7.2 was fixed. Support found no record of that contact (01:32). Both versions kept.

## What has been tried
| When | Who | Action | Result |
|---|---|---|---|
| Before 01:05 UTC 16 Nov | Customer (Darwin team) | Rebooted all Darwin gateways | "made no difference" (call note 01:05) |
| 01:05 to 01:32 | Marcus Lee | Checked fleet status in TernCloud | 47 online, 14 offline, as above (01:32) |
| 01:32 | Marcus Lee | Asked Darwin to report front-panel lights on 2 or 3 units | Answered 03:05: solid green power, flashing amber NET |
| By 02:10 | Marcus Lee | Checked all 14 SIMs in Tern Connect console | All Active; no session attempts since 18:24 UTC |
| 02:05 | Marcus Lee | Sent SMS wake to DRW-GW-01, DRW-GW-05, KTH-GW-02 | No response by 02:10; later result not recorded |
| 02:10 | Marcus Lee | Compared model against online/offline status; read 4.7.2 release notes | G4-C vs G4-E split; MX-31.4 note found; link unconfirmed |
| Morning of 16 Nov (before 03:05) | Customer (Darwin team) | Power-cycled all 11 Darwin units again | Lights unchanged (03:05) |
| 03:40 | Marcus Lee | Asked customer not to factory-reset units | Result not recorded; Katherine units not yet touched |
| 03:50 | Marcus Lee | Escalated to Tier 2 | Status Escalated; priority kept at P2 |

## Commitments to the customer
| When | Made by | Commitment (quoted) | Due | State |
|---|---|---|---|---|
| 2026-11-16 01:05 UTC (phone) | Marcus Lee | "I'd check the fleet and call him back within the hour" (call note wording) | 02:05 UTC | Met: call-back happened before the 01:32 email, which opens "as discussed on the phone just now" (exact call time not recorded) |
| 2026-11-16 01:32 UTC | Marcus Lee | "If you can tell me who you spoke to, I'll follow it up." | Not stated; conditional | Open: Grant could not name the engineer (03:05) |
| 2026-11-16 03:40 UTC | Marcus Lee | "I'm escalating this to our Field Systems Engineering team now." | now | Met at 03:50 UTC |
| 2026-11-16 03:40 UTC | Marcus Lee | "I'll send you an update by 12:00 AWST tomorrow, Tuesday 17 November (04:00 UTC), or sooner if engineering has news." | 04:00 UTC Tue 17 Nov | Open, about 24h10m away; now owned by Tier 2 (policy 5.3) |

Account record: no commitments, credits or flags. No fix date, service credit or refund has been promised (thread; 03:40 "I can't give you a fix date"). Grant states "this one is on Tern" (01:12), a liability claim; policy 6.2 and 6.3 reserve any credit or compensation to the Account Manager (Rhys Kaplan) or the Head of Customer Support, in writing. Tier 2 must not offer one.

## Recommended next action
Test the leading suspected cause on the affected units: in Tern Connect and TernCloud, pull the device and modem logs for DRW-GW-01, DRW-GW-05 and KTH-GW-02 (the SMS-wake units) around 18:15 to 18:30 UTC on 14 Nov, and read the modem firmware version and update state on each of the 14 G4-C units. Also check the 4.7.2 release notes and known issues for MX-31.4 compatibility with the Darwin and Katherine carrier or network settings. Confirms the cause: logs show the MX-31.4 update running or failing at 18:20 to 18:24 and the modem never registering afterwards, on all 14 units. Rules it out: modems are on the expected firmware and registered on the network up to the drop, or the logs show a different failure (for example gateway application or SIM-profile loss). With the cause known, choose a recovery path (modem rollback or a re-flash) that preserves locally stored readings, since the customer was told not to factory-reset. Race: the Tuesday 17 Nov 04:00 UTC customer update (about 24h away; send sooner if there is news), with the resolution deadline of 01:05 UTC Thu 19 Nov behind it.

Open questions:
- Did any G4-C gateway ever come back, and did the SMS wake produce any later response?
- What are the Katherine units' lights? (Customer has not yet checked.)
- Which firmware version is actually running on each of the 14 offline units, and who started the 14 Nov rollout (customer schedule or Tern push)?
- Is any data stored on the 14 units, and how long can they hold it before overwriting?
- Who was the "engineer" Grant spoke to last week? Can the phone or call records be searched?
- Is there a WA public holiday between 16 and 19 Nov that would move the resolution deadline? None is stated in the case.
- The LED guide quoted at 03:40 is not in the case; confirm its wording.
