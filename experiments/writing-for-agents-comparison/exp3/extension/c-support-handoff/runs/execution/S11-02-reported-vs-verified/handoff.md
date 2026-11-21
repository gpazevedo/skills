# Escalation handoff: TRN-77102: 14 cellular (G4-C) gateways at Darwin and Katherine offline since firmware 4.7.2 rollout

**Customer:** Coldwater Freight Pty Ltd (CWF-2210), Business plan · **Priority:** P2 · **Next deadline:** Resolution target 2026-11-19 01:05 UTC (09:05 AWST), breached by 17 h 25 min of business hours (as of 2026-11-21 18:41 UTC / 2026-11-22 02:41 AWST)

## Problem as currently understood
Since the customer-scheduled firmware 4.7.2 rollout on Saturday 14 Nov 2026 (18:00 UTC), 14 of Coldwater's 61 gateways have been offline: all 11 at Darwin and all 3 at Katherine, every one a G4-C (cellular) unit. The 47 G4-E (Ethernet) units on the same firmware are online with complete data. The offline units show a flashing amber NET light, which per the LED guide means the cellular modem is not registered on the mobile network, while the carrier side shows all 14 SIMs active with no session attempts since the rollout. The leading explanation is the G4-C-only modem firmware update (MX-31.4) bundled in 4.7.2, but this is not confirmed. Whether any readings are lost is unknown; G4 units buffer readings locally while offline.

Evidence:
- [Verified] Fleet is 61 gateways: 47 online and reporting, 14 offline (Marcus Lee, 2026-11-16 01:32 UTC, TernCloud as of 01:25 UTC)
- [Verified] The 14 offline units are 11 at Darwin and 3 at Katherine; each last reported 18:20 to 18:24 UTC on 14 Nov, inside the firmware window that started 18:00 UTC (Marcus Lee, 2026-11-16 01:32 UTC)
- [Verified] All 61 units were updated to 4.7.2 in that window; all 47 online units run 4.7.2 (Marcus Lee, 2026-11-16 01:32 UTC)
- [Verified] Readings from the 47 online units are complete; TernCloud has no readings from the 14 offline units after their last report (Marcus Lee, 2026-11-16 01:32 UTC)
- [Verified] All 14 offline units are G4-C (cellular); all 47 online units are G4-E (Ethernet) (Marcus Lee internal note, 2026-11-16 02:10 UTC; account record fleet table)
- [Verified] All 14 SIMs are Active in Tern Connect; last data sessions ended 18:21 to 18:24 UTC on 14 Nov; no session attempts since (Marcus Lee internal note, 2026-11-16 02:10 UTC)
- [Verified] 4.7.2 release notes include "cellular modem firmware updated to MX-31.4 (G4-C only)" (Marcus Lee internal note, 2026-11-16 02:10 UTC)
- [Verified] Remote SMS wake sent to DRW-GW-01, DRW-GW-05 and KTH-GW-02 at 02:05 UTC; no response by 02:10 UTC (Marcus Lee internal note, 2026-11-16 02:10 UTC)
- [Verified] No record of a Coldwater call or ticket in the week before; last ticket TRN-75530, closed 2 Oct 2026 (Marcus Lee, 2026-11-16 01:32 UTC; account record, Recent tickets)
- [Reported] Darwin units show solid green power and flashing amber NET; all 11 were power-cycled again with the same result; Katherine units not touched (Grant Tobias, 2026-11-16 03:05 UTC)
- [Reported] Darwin gateways were rebooted earlier with no change (Grant Tobias by phone, recorded in call note 2026-11-16 01:05 UTC)
- [Reported] "Every one of our gateways went dark" and "lost all our temperature data for the last three days" (Grant Tobias, 2026-11-16 01:12 UTC); contradicted by the verified 47 online units with complete data
- [Reported] Business impact of about $40,000 a day in stock that cannot be certified; Perth cannot dispatch Darwin loads without certificates (Grant Tobias, 2026-11-16 01:12 and 03:05 UTC)
- [Reported] A Tern engineer, unnamed, said by phone the previous week that 4.7.2 "was fixed and safe to roll out" (Grant Tobias, 2026-11-16 01:12 and 03:05 UTC); no record found
- [Inferred] The fault is on the G4-C gateway side, likely the modem after the MX-31.4 update, not the SIM accounts or 4.7.2 generally (rests on: model split exactly matches online/offline split, SIMs active with no session attempts, NET LED meaning, G4-C-only modem change in 4.7.2)
- [Inferred] Readings from the offline units may still be stored on the gateways and recoverable on reconnection, provided no unit is factory-reset (rests on: Marcus Lee's statement that G4 units buffer locally, 01:32 UTC; his no-reset instruction, 03:40 UTC)

## Tried so far
| When | Who | Action | Result |
| --- | --- | --- | --- |
| Before 2026-11-16 01:05 UTC | Customer (Darwin team) | Rebooted all Darwin gateways | No change (Reported) |
| 2026-11-16 01:25 UTC | Marcus Lee (Tier 1) | Checked fleet status in TernCloud | 47 online on 4.7.2, 14 offline (Darwin and Katherine), offline since 18:20 to 18:24 UTC 14 Nov; firmware version alone ruled out as the separator |
| 2026-11-16 01:32 UTC | Marcus Lee | Searched for record of the claimed engineer call last week | No call or ticket found |
| 2026-11-16 by 02:10 UTC | Marcus Lee | Checked SIM status in Tern Connect | All 14 SIMs Active; no session attempts since 14 Nov; SIM account problem made unlikely |
| 2026-11-16 by 02:10 UTC | Marcus Lee | Compared models of online and offline units | Offline = all G4-C, online = all G4-E; linked to MX-31.4 modem update in release notes (not confirmed) |
| 2026-11-16 02:05 UTC | Marcus Lee | Remote SMS wake to DRW-GW-01, DRW-GW-05, KTH-GW-02 | No response by 02:10 UTC |
| 2026-11-16 before 03:05 UTC | Customer (Darwin site lead) | Read front-panel LEDs; power-cycled all 11 Darwin units again | Solid green power, flashing amber NET, unchanged after power cycle (Reported) |
| 2026-11-16 03:40 UTC | Marcus Lee | Interpreted LEDs against LED guide; told customer not to factory-reset | Modem not registered on mobile network; gateway-side fault indicated, cause not confirmed |
| 2026-11-16 03:50 UTC | Marcus Lee | Escalated to Tier 2 (Field Systems Engineering), priority kept at P2 | No result recorded; no ticket activity after this point in the supplied export |

## Commitments to the customer
| Commitment (quoted) | Made by | When | Status |
| --- | --- | --- | --- |
| "I'd check the fleet and call him back within the hour" (as recorded in call note) | Marcus Lee (Tier 1) | 2026-11-16 01:05 UTC | Met: call-back made before the 01:32 UTC email ("as discussed on the phone just now") |
| "If you can tell me who you spoke to, I'll follow it up." | Marcus Lee | 2026-11-16 01:32 UTC | Outstanding but not triggered: customer could not name the engineer (03:05 UTC) |
| "I'm escalating this to our Field Systems Engineering team now." | Marcus Lee | 2026-11-16 03:40 UTC | Met: escalated 03:50 UTC |
| "I'll send you an update by 12:00 AWST tomorrow, Tuesday 17 November (04:00 UTC), or sooner if engineering has news." | Marcus Lee | 2026-11-16 03:40 UTC | Overdue by 4 days 14 h 41 min (due 2026-11-17 04:00 UTC); no update in the supplied thread. Tier 2 now owns it (policy 5.3) |

Claimed by the customer, not found in the thread: a Tern engineer told Grant Tobias by phone the week before 16 Nov that 4.7.2 "was fixed and safe to roll out" (Grant Tobias, 2026-11-16 01:12 and 03:05 UTC). Not a promise of a fix or credit, but the customer uses it to say "this one is on Tern".

## Service level
- **Plan:** Business [Verified] (account record, Support plan). Policy 1.3 uses the plan in the account record.
- **Priority:** P2 [Verified] (ticket event 2026-11-16 01:05 UTC, reaffirmed at escalation 03:50 UTC). Consistent with policy 2.1/2.2: 14 of 61 offline is not more than half. Customer's request for P1 [Reported] (Grant Tobias, 01:12 UTC) was recorded and not applied, so it does not set the clock.
- **Target:** [Verified] policy 3.1, "Business | P2 | 4 business hours | 27 business hours"; policy 3.3, targets not marked 24x7 "count business hours only". Business hours are "08:30 to 17:30 Australia/Perth time (AWST, UTC+8 ...), Monday to Friday" (policy 1.1), i.e. 00:30 to 09:30 UTC.
- **Clock start:** [Verified] 2026-11-16 01:05 UTC (09:05 AWST, Monday), ticket creation (policy 4.1), inside business hours.
- **Pauses:** none [Verified]: status went Open to Escalated; never "Pending customer" (policy 4.2) in the supplied thread.
- **First response:** met [Verified] at 2026-11-16 01:05 UTC; ticket logged by an agent during a call with the customer counts as first response (policy 1.4).
- **Resolution deadline:** 2026-11-19 01:05 UTC (09:05 AWST, Thursday) [Inferred] (rests on: start 09:05 AWST Mon; 8 h 25 min Mon + 9 h Tue + 9 h Wed + 35 min Thu = 27 business hours; no WA public holidays assumed in 16 to 19 Nov).
- **Status as of 2026-11-21 18:41 UTC (2026-11-22 02:41 AWST, Sunday):** breached by 17 h 25 min of business hours (8 h 25 min Thu + 9 h Fri) [Inferred] (rests on: deadline above; no Resolved status in the supplied thread). Policy 4.4.
- **Update cadence:** [Verified] policy 7.1, "P2: at least once each business day." No customer update appears in the thread for Tue 17 to Fri 20 Nov [Inferred] (rests on: supplied export ends 2026-11-16 03:50 UTC).

## Recommended next action
The Tier 2 (Field Systems Engineering) owner should send Grant Tobias the overdue update now, and no later than the start of business hours on Monday 23 Nov (08:30 AWST, 2026-11-23 00:30 UTC), stating the current cause analysis and asking Lina Petrakis (technical contact) to give Tier 2 local access to one Darwin G4-C unit to read its modem state and firmware. The resolution target is already breached and the 17 Nov update commitment is overdue; the diagnosis rests on the unconfirmed link between the MX-31.4 modem update and the G4-C units' failure to register, which only on-unit evidence can confirm.

Follow-ups:
1. Tier 2 to confirm with the firmware team whether MX-31.4 has a known registration fault on G4-C and whether a rollback or modem re-flash path exists that preserves locally stored readings.
2. Tier 2 to inform the Support Team Lead and Account Manager Rhys Kaplan of the breach and of the customer's $40,000-a-day impact claim and "this one is on Tern" position; only they may handle any credit or compensation (policy 6.3).

## Gaps and open questions
- The supplied export ends at escalation (2026-11-16 03:50 UTC). Whether Tier 2 has since updated the customer, changed status or resolved the ticket is unknown; if any of that happened, the commitment and breach statuses above change.
- Root cause unconfirmed: MX-31.4 modem firmware on G4-C is a possible link only (Marcus Lee, 02:10 UTC).
- Unknown whether readings were lost or are buffered on the 14 units; depends on local storage capacity and on no unit having been factory-reset.
- Katherine units have not been physically checked (customer, 03:05 UTC); their LED state is assumed to match Darwin.
- Conflict: customer says "every one of our gateways" is down and all data lost; TernCloud shows 47 of 61 online with complete data. Customer's "every site is affected" refers to downstream dispatch impact, not gateway status.
- Customer's claim that a Tern engineer approved 4.7.2 last week is unverified; no call or ticket record found and the engineer is unnamed.
- Customer's $40,000-a-day loss figure is unverified.
- The resolution deadline assumes no Western Australian public holiday between 16 and 19 Nov 2026; the policy excludes them but the material supplied does not list them.
