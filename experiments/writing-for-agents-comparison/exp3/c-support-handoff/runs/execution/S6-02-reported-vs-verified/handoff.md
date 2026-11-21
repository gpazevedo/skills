# Escalation handoff: TRN-77102 14 of 61 Coldwater gateways (all cellular G4-C, Darwin and Katherine) offline since the 4.7.2 firmware window

Reference time ("now"): 2026-11-16 03:50 UTC (11:50 AWST, Monday) (last thread message)
Inputs missing: none (thread, account record and policy all supplied)

## Problem as currently understood
Since the customer's 4.7.2 firmware window on Saturday 14 Nov, the 14 cellular G4-C gateways at Darwin (11) and Katherine (3) have stopped reporting; the 47 Ethernet G4-E gateways at Perth and Adelaide, also on 4.7.2, are online with complete data. The SIMs are active on the carrier side but the units have made no data session attempts since, and Darwin units show the LED pattern for "modem not registered on the mobile network". The leading hypothesis is the G4-C-only cellular modem firmware (MX-31.4) shipped in 4.7.2, which is unconfirmed. Whether readings from the offline units are lost or held on the units is not yet known.

- 61 gateways in fleet: Kewdale (PER) 30 G4-E, Wingfield (ADL) 17 G4-E, Darwin (DRW) 11 G4-C, Katherine (KTH) 3 G4-C [verified] (account record)
- 47 online and reporting normally; 14 offline, all at Darwin (11) and Katherine (3), as of 01:25 UTC [verified] (Marcus Lee, 2026-11-16 01:32 UTC, TernCloud)
- Each offline unit last reported 18:20 to 18:24 UTC Sat 14 Nov, inside the firmware window that started 18:00 UTC [verified] (Marcus Lee, 01:32 UTC, TernCloud)
- All 61 gateways updated to 4.7.2 in that window; all 47 online units run 4.7.2 [verified] (Marcus Lee, 01:32 UTC)
- All 14 offline units are G4-C (cellular); all 47 online units are G4-E (Ethernet), so hardware model, not firmware version alone, separates the groups [verified] (Marcus Lee, internal note 02:10 UTC; account record)
- All 14 SIMs status Active in Tern Connect; last data sessions ended 18:21 to 18:24 UTC 14 Nov; no session attempts since [verified] (Marcus Lee, internal note 02:10 UTC, Tern Connect console)
- 4.7.2 release notes include "cellular modem firmware updated to MX-31.4 (G4-C only)" [verified] (Marcus Lee, internal note 02:10 UTC)
- The MX-31.4 modem firmware update is linked to the outage [suspected] (Marcus Lee, internal note 02:10 UTC: "Possible link; not confirmed.")
- Every Darwin unit shows solid green power light and flashing amber NET light, unchanged after another power-cycle of all 11 [reported] (Grant Tobias relaying Darwin site lead, 03:05 UTC)
- Katherine units: no one on site has touched them; LED state unknown [reported] (Grant Tobias, 03:05 UTC)
- Flashing amber NET on a G4-C means the cellular modem is not registered on the mobile network, so the Darwin modems are not registering [suspected] (Marcus Lee, 03:40 UTC, per LED guide applied to the reported lights)
- The fault is on the gateway side rather than the SIM accounts [suspected] (Marcus Lee, 03:40 UTC)
- Readings from the 47 online gateways are complete in TernCloud with no gaps; TernCloud has no readings from the 14 offline units after their last report [verified] (Marcus Lee, 01:32 UTC)
- G4 gateways store readings locally when they cannot reach TernCloud and upload on reconnect, so offline-unit readings may be recoverable [suspected] (Marcus Lee, 01:32 UTC: "I can't yet tell whether any data has actually been lost")
- Customer reports all temperature data lost for the last three days [reported] (Grant Tobias, 01:12 UTC)
- Business impact: about $40,000 a day in stock that cannot be certified for delivery [reported] (Grant Tobias, 01:12 UTC); Perth cannot dispatch Darwin loads without the certificates [reported] (Grant Tobias, 03:05 UTC)
- A Tern engineer told the customer by phone last week that 4.7.2 was fixed and safe to roll out [reported] (Grant Tobias, 01:12 and 03:05 UTC; name not remembered)
- No record of a call or ticket with Coldwater last week; last ticket TRN-75530 (P3, bracket replacement) closed 2 October [verified] (Marcus Lee, 01:32 UTC; account record)

Conflicts:
- Scope: "Every one of our gateways went dark" and "every site is affected" [reported] (Grant Tobias, 01:12 and 03:05 UTC) vs 14 of 61 offline, Perth and Adelaide gateways online [verified] (Marcus Lee, 01:32 UTC). The customer's "every site" refers to business impact (Darwin certificates block Perth dispatch), not gateway status.
- Data loss: "lost all our temperature data for the last three days" [reported] (Grant Tobias, 01:12 UTC) vs online-unit data complete and offline-unit data status unknown [verified / suspected] (Marcus Lee, 01:32 UTC).
- Prior assurance: engineer said 4.7.2 was fixed [reported] (Grant Tobias, 01:12 UTC) vs no record of such a call or ticket [verified] (Marcus Lee, 01:32 UTC).
- Priority: customer requested P1 [reported] (Grant Tobias, call note and 01:12 UTC) vs P2 retained because fewer than half of gateways are offline (14 of 61) [verified] (Marcus Lee, 01:32 and 03:50 UTC; policy 2.1: P1 is "more than half of the customer's gateways are offline").

## Tried so far
| When | Who | What | Result |
|------|-----|------|--------|
| Before 2026-11-16 01:05 UTC | Customer's team | Rebooted all Darwin gateways | No difference [reported] (call note, Marcus Lee, 01:05 UTC) |
| 2026-11-16 01:25 UTC | Marcus Lee (Tier 1) | Checked fleet status in TernCloud | 47 online, 14 offline (DRW 11, KTH 3); all on 4.7.2; online data complete [verified] |
| By 2026-11-16 01:32 UTC | Marcus Lee | Searched for a record of last week's call or ticket | None found; last ticket TRN-75530, closed 2 Oct [verified] |
| By 2026-11-16 02:10 UTC | Marcus Lee | Checked the 14 SIMs in Tern Connect console | All Active; last sessions ended 18:21 to 18:24 UTC 14 Nov; no session attempts since [verified] |
| By 2026-11-16 02:10 UTC | Marcus Lee | Compared models of online vs offline units | Offline all G4-C, online all G4-E [verified] |
| 2026-11-16 02:05 UTC | Marcus Lee | Remote SMS wake to DRW-GW-01, DRW-GW-05, KTH-GW-02 | No response from any by 02:10 UTC [verified] |
| Morning of 2026-11-16 (reported 03:05 UTC) | Darwin site lead | Inspected front-panel LEDs and power-cycled all 11 Darwin units again | Solid green power, flashing amber NET, same after power-cycle [reported] |
| (none) | Katherine site | Nothing tried | Units not touched [reported] (Grant Tobias, 03:05 UTC) |

Customer has been told not to factory-reset any unit, because it would erase stored readings (Marcus Lee, 03:40 UTC).

## Commitments to the customer
| When | Made by | Verbatim commitment | Status (met / pending / overdue) | Policy note |
|------|---------|---------------------|----------------------------------|-------------|
| 2026-11-16 01:05 UTC | Marcus Lee | "I told him I'd check the fleet and call him back within the hour." (Marcus's own internal call note; the words said on the call are not in the thread) | Met: fleet checked 01:25 UTC and 01:32 UTC email refers to the phone call "just now" | 6.1: "Support agents may commit to the time of the next update and to actions they will take themselves." |
| 2026-11-16 01:32 UTC | Marcus Lee | "If you can tell me who you spoke to, I'll follow it up." | Pending: customer replied 03:05 UTC with "one of your engineers" but no name; no follow-up recorded | 6.1 as above |
| 2026-11-16 03:40 UTC | Marcus Lee | "I'm escalating this to our Field Systems Engineering team now." | Met: escalated to Tier 2 at 03:50 UTC | 6.1 as above |
| 2026-11-16 03:40 UTC | Marcus Lee | "I'll send you an update by 12:00 AWST tomorrow, Tuesday 17 November (04:00 UTC), or sooner if engineering has news." | Pending, due 2026-11-17 04:00 UTC | 6.1 as above; 5.3: "From escalation, Tier 2 owns the ticket, including customer updates and commitments already made." |

No fix date, credit or compensation has been promised. Marcus stated "I can't give you a fix date" (03:40 UTC), consistent with 6.2: "Support agents must not promise a fix date, a service credit, a refund or compensation." The customer's "this one is on Tern" and $40,000-a-day loss (01:12 UTC) are [reported] claims, not commitments; 6.3: "Only the Account Manager named in the account record, or the Head of Customer Support, may offer a service credit, refund or compensation." Account Manager is Rhys Kaplan; open credits: none (account record).

## Service level
Applicable row: Business plan (account record), priority P2 (ticket, 01:05 and 03:50 UTC). Ticket created 2026-11-16 01:05 UTC = 09:05 AWST Monday, inside business hours (policy 1.1, 1.2). No "Pending customer" status appears in the thread (statuses Open, then Escalated), so no paused time (policy 4.2).

First response
- Clause: "Business | P2 | 4 business hours | 27 business hours" (3.1); "A ticket logged by an agent during a call with the customer counts as a first response when logged." (1.4)
- Clock: first response, business hours, started at ticket creation 2026-11-16 01:05 UTC (09:05 AWST)
- Deadline: 2026-11-16 05:05 UTC (09:05 AWST + 4 business hours = 13:05 AWST, same business day)
- Status: met (ticket logged during the call at 01:05 UTC, 0 business hours elapsed); missing terms: none

Resolution
- Clause: "Business | P2 | 4 business hours | 27 business hours" (3.1); "Business-hours targets count only time inside business hours" (4.1)
- Clock: resolution, business hours (08:30 to 17:30 AWST = 00:30 to 09:30 UTC, Mon to Fri, 9 hours a day), started at ticket creation 2026-11-16 01:05 UTC (09:05 AWST Mon)
- Deadline: 2026-11-19 01:05 UTC (09:05 AWST Thu) (Mon 09:05 to 17:30 = 8h25m, 18h35m left; Tue 9h, 9h35m left; Wed 9h, 0h35m left; Thu 08:30 + 0h35m = 09:05 AWST)
- Status: "within target" (4.4). Elapsed at now: 09:05 to 11:50 AWST = 2h45m; remaining 24h15m of 27h. "At risk" is "less than 25% of its resolution target remains" (4.4): 25% of 27h = 6h45m, reached after 20h15m elapsed, at 2026-11-18 03:20 UTC (11:20 AWST Wed) (Mon 8h25m + Tue 9h = 17h25m; Wed 08:30 + 2h50m = 11:20). Missing terms: WA public holidays for 16 to 19 Nov are not listed in the inputs; the deadline assumes none. A holiday would only push the deadline later, so the status at now is "within target" either way.
- Note: if the ticket were re-prioritised to P1, "the resolution target becomes the target for the new priority, counted from ticket creation" (4.3); Business P1 resolution is "24 hours, 24x7" (3.1), which would give 2026-11-17 01:05 UTC (01:05 UTC + 24 calendar hours). P1 is not recorded on the ticket, and "a priority applies only once recorded on the ticket" (2.5).

Customer updates
- Clause: "P2: at least once each business day." (7.1)
- Clock: update interval, business days, Monday 16 Nov update sent (01:32 and 03:40 UTC)
- Deadline: Tuesday 17 Nov update by 2026-11-17 09:30 UTC (end of business day, 17:30 AWST); the earlier commitment of 04:00 UTC (12:00 AWST) governs in practice
- Status: Monday met; Tuesday open, 24h10m to the 04:00 UTC commitment and 29h40m to the policy end of day at now; missing terms: none

Escalation notice: 5.2 requires notifying the Support Team Lead only for "a P1 ticket, or an at-risk P2 ticket"; this P2 was within target at escalation (03:50 UTC), so no notice was required.

## Open questions
- Who was the Tern engineer who said 4.7.2 was fixed? (asked by Marcus Lee, 2026-11-16 01:32 UTC; customer replied 03:05 UTC that he does not remember the name; still unanswered)
- What do the front-panel lights show? (asked by Marcus Lee, 2026-11-16 01:32 UTC; answered for Darwin at 03:05 UTC; Katherine units not yet inspected)
- Has any data actually been lost, or are readings held on the offline units? (raised by Marcus Lee, 2026-11-16 01:32 UTC: "I can't yet tell whether any data has actually been lost")
- What is the cause, and when will there be a fix? (Marcus Lee to customer, 2026-11-16 03:40 UTC: "I can't confirm the cause yet and I can't give you a fix date")

## Recommended next action
Reproduce in the lab: take a G4-C on a working cellular SIM, update it to 4.7.2 (modem firmware MX-31.4), and check whether the modem registers on the network and opens a data session; if it fails, test whether reverting only the modem firmware restores registration. This tests the leading [suspected] cause directly without touching the customer's units or the readings they may hold. Owner: Tier 2 Field Systems Engineering (owns the ticket per 5.3), by 2026-11-17 04:00 UTC so the result can go into the committed Tuesday update. Rests on: offline set is exactly the G4-C units, online set exactly the G4-E units, all on 4.7.2 [verified, 02:10 UTC]; release notes MX-31.4 G4-C only [verified, 02:10 UTC]; SIMs Active with no session attempts since 18:21 to 18:24 UTC 14 Nov [verified, 02:10 UTC]; flashing amber NET (modem not registered) [reported 03:05 UTC, suspected 03:40 UTC]; reboots, power-cycles and SMS wake did not recover units [reported / verified]; update commitment due 2026-11-17 04:00 UTC [Marcus Lee, 03:40 UTC].
