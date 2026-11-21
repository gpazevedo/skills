# Escalation handoff: TRN-77102 | Coldwater Freight Pty Ltd (CWF-2210) | 14 cellular G4-C gateways offline since firmware 4.7.2 rollout

**Service level:** Resolution due 2026-11-19 01:05 UTC (Thu 19 Nov, 09:05 AWST), Business P2 resolution target of 27 business hours (policy 3.1) | Pending, 24 h 15 min business hours remaining as of 2026-11-16 03:50 UTC (latest thread timestamp); "within target" under policy 4.4

## Problem as currently understood
14 of the customer's 61 gateways, all the G4-C (cellular) units at Darwin (11) and Katherine (3), stopped reporting between 18:20 and 18:24 UTC on Sat 14 Nov during the customer's firmware 4.7.2 rollout; the 47 G4-E (Ethernet) units on 4.7.2 are online with complete data (Verified, Marcus Lee). The carrier side shows all 14 SIMs Active with no session attempts since 14 Nov, and remote SMS wake to three units got no response (Verified). The customer reports a flashing amber NET light on Darwin units, which the LED guide maps to the cellular modem not being registered on the network. The leading Suspected cause is the cellular modem firmware update (MX-31.4, G4-C only) bundled in 4.7.2; untested. Whether any readings are lost is not determined: G4 units buffer readings locally, and the customer reports all data lost.

| Statement | Label | Source (author, timestamp) |
| --- | --- | --- |
| Fleet is 61 gateways: 47 online and reporting normally, 14 offline | Verified (Marcus Lee, TernCloud as of 01:25 UTC) | Marcus Lee, Tier 1, 2026-11-16 01:32 UTC |
| The 14 offline units are Darwin (11) and Katherine (3); each last reported 18:20 to 18:24 UTC Sat 14 Nov, during the firmware window that started 18:00 UTC | Verified (Marcus Lee, TernCloud as of 01:25 UTC) | Marcus Lee, 2026-11-16 01:32 UTC |
| All 61 gateways were updated to 4.7.2 in that window; the 47 online units run 4.7.2 | Verified (Marcus Lee, TernCloud as of 01:25 UTC) | Marcus Lee, 2026-11-16 01:32 UTC |
| Readings from the 47 online units are complete with no gaps; TernCloud has no readings from the 14 offline units after their last report | Verified (Marcus Lee, TernCloud as of 01:25 UTC) | Marcus Lee, 2026-11-16 01:32 UTC |
| All 14 offline units are G4-C (cellular); all 47 online units are G4-E (Ethernet) | Verified (Marcus Lee, model check, 02:10 UTC; consistent with account record fleet table) | Marcus Lee, internal note, 2026-11-16 02:10 UTC |
| All 14 SIMs are Active; last data sessions ended 18:21 to 18:24 UTC 14 Nov; no session attempts since | Verified (Marcus Lee, Tern Connect console, 02:10 UTC) | Marcus Lee, internal note, 2026-11-16 02:10 UTC |
| 4.7.2 release notes include "cellular modem firmware updated to MX-31.4 (G4-C only)" | Verified (Marcus Lee, release notes, 02:10 UTC) | Marcus Lee, internal note, 2026-11-16 02:10 UTC |
| The MX-31.4 modem firmware update in 4.7.2 caused the G4-C outage ("Possible link; not confirmed") | Suspected | Marcus Lee, internal note, 2026-11-16 02:10 UTC |
| Darwin units show solid green power light and flashing amber NET light | Reported | Grant Tobias (customer, relaying Darwin site lead), 2026-11-16 03:05 UTC |
| Per the LED guide, flashing amber NET on a G4-C means the modem is not registered on the mobile network; with SIMs active, the fault is on the gateway side, not the SIM accounts | Suspected (interpretation of a Reported light pattern) | Marcus Lee, 2026-11-16 03:40 UTC |
| "Every one of our gateways went dark" | Reported; contradicted by Verified fleet status (47 of 61 online) | Grant Tobias, 2026-11-16 01:12 UTC |
| "We've lost all our temperature data for the last three days" | Reported; contradicted for the 47 online units; not determined for the 14 offline units, which store readings locally until reconnect | Grant Tobias, 2026-11-16 01:12 UTC; Marcus Lee, 01:32 UTC |
| Impact of around $40,000 a day in stock that cannot be certified for delivery | Reported | Grant Tobias, 2026-11-16 01:12 UTC |
| Every site is affected because Perth cannot dispatch Darwin loads without the certificates | Reported | Grant Tobias, 2026-11-16 03:05 UTC |
| Katherine units have not been touched by site staff | Reported | Grant Tobias, 2026-11-16 03:05 UTC |

## What has been tried
| Action | By | When | Result | Label |
| --- | --- | --- | --- | --- |
| Rebooted all Darwin gateways | Customer's team | Before 2026-11-16 01:05 UTC (time not given) | "made no difference" | Reported (Grant Tobias, call note 01:05 UTC) |
| Checked fleet status, models and firmware in TernCloud | Marcus Lee (Tier 1) | 2026-11-16 01:25 UTC | 14 G4-C units offline since 14 Nov firmware window; 47 online | Verified (Marcus Lee) |
| Checked SIM status in Tern Connect console | Marcus Lee | By 2026-11-16 02:10 UTC | All 14 SIMs Active; no session attempts since 18:24 UTC 14 Nov | Verified (Marcus Lee) |
| Remote SMS wake sent to DRW-GW-01, DRW-GW-05, KTH-GW-02 | Marcus Lee | 2026-11-16 02:05 UTC | No response from any by 02:10 UTC | Verified (Marcus Lee) |
| Power-cycled all 11 Darwin units again | Customer's Darwin site staff | Morning of 2026-11-16 (time not given) | Lights came back the same (green power, flashing amber NET) | Reported (Grant Tobias, 03:05 UTC) |
| Checked for a record of the call the customer says took place last week | Marcus Lee | By 2026-11-16 01:32 UTC | No record of a call or ticket last week; last ticket TRN-75530 closed 2 Oct | Verified (Marcus Lee; account record agrees) |

## Commitments to the customer
| Commitment (quoted) | Made by (name, role) | When | Due | Status |
| --- | --- | --- | --- | --- |
| "I told him I'd check the fleet and call him back within the hour." (call note recording a phone commitment) | Marcus Lee, Support Agent, Tier 1 | 2026-11-16 01:05 UTC | 2026-11-16 02:05 UTC ("within the hour") | Kept (call-back and fleet status by 01:32 UTC) |
| "If you can tell me who you spoke to, I'll follow it up." | Marcus Lee, Tier 1 | 2026-11-16 01:32 UTC | No date given | Outstanding (conditional; customer did not supply a name, 03:05 UTC) |
| "I'm escalating this to our Field Systems Engineering team now." | Marcus Lee, Tier 1 | 2026-11-16 03:40 UTC | "now" | Kept (escalated 03:50 UTC) |
| "I'll send you an update by 12:00 AWST tomorrow, Tuesday 17 November (04:00 UTC), or sooner if engineering has news." | Marcus Lee, Tier 1 | 2026-11-16 03:40 UTC | 2026-11-17 04:00 UTC (12:00 AWST) | Outstanding; owned by Tier 2 from escalation (policy 5.3) |

Claimed by the customer but not found in the thread: a Tern engineer said on the phone "last week that 4.7.2 was fixed and safe to roll out" (Grant Tobias, 01:12 UTC; engineer's name not remembered, 03:05 UTC). Tier 1 found no record of such a call or ticket.

## Service level
- Tier: Business (account record CWF-2210)
- Priority: P2 (recorded at creation 01:05 UTC and unchanged at escalation 03:50 UTC; customer's P1 request recorded and not applied)
- First response: 4 business hours from ticket creation; ticket logged by agent during the customer call at 2026-11-16 01:05 UTC counts as first response (policy 1.4, 3.1, 4.1). Met.
- Resolution: 27 business hours from ticket creation at 2026-11-16 01:05 UTC (Mon, inside business hours 00:30 to 09:30 UTC); deadline 2026-11-19 01:05 UTC (Thu, 09:05 AWST), assuming no WA public holiday 16 to 19 Nov and no "Pending customer" time (none recorded). Pending, 24 h 15 min business hours remaining; becomes "at risk" under policy 4.4 (less than 6 h 45 min remaining) at 2026-11-18 03:20 UTC (Wed, 11:20 AWST) (policy 3.1, 3.3, 4.1, 4.2, 4.4).
- Customer updates: P2 requires at least one update each business day (policy 7.1); next committed update 2026-11-17 04:00 UTC.
- Clock: never paused; status has not been "Pending customer" (policy 4.2). All thread timestamps are UTC.
- Status as of: 2026-11-16 03:50 UTC, the latest timestamp in the thread.

## Recommended next action
Field Systems Engineering (Tier 2, now owner under policy 5.3) should test the Suspected MX-31.4 modem firmware cause on one untouched Katherine G4-C unit (local modem diagnostics via the technical contact Lina Petrakis or site staff), and check whether other customers' G4-C units on 4.7.2 show the same failure; the evidence is the Verified model split (all G4-C offline, all G4-E online) with SIMs active and the Reported amber NET light. Confirmation would point to a modem firmware rollback or patch path that keeps locally stored readings; a modem that registers normally under 4.7.2 would redirect the investigation to the carrier or site network. Send the committed update by 2026-11-17 04:00 UTC either way.

## Open questions
- Priority conflict: customer requests P1 (Grant Tobias, 01:05 and 01:12 UTC) and states "every site is affected" (03:05 UTC). Policy 2.1 sets P1 at more than half of gateways offline; Verified status is 14 of 61 offline, so P2 under policy 2.2 stands as recorded. The customer's business-impact argument is not a policy criterion.
- Customer claims a Tern engineer said last week that 4.7.2 was fixed and safe to roll out; Tier 1 found no call or ticket record. The engineer is unidentified; Grant Tobias attributes responsibility to Tern ("this one is on Tern").
- Customer reports $40,000 a day losses; no credit, refund or compensation has been offered, and only Account Manager Rhys Kaplan or the Head of Customer Support may offer one (policy 6.3). Consider whether the Account Manager should be informed.
- Data loss on the 14 offline units is not determined; depends on whether locally stored readings survive and upload on reconnect. Customer was told not to factory-reset; any remediation (including firmware rollback) must be checked for its effect on stored readings.
- Katherine units' LED state is unreported; only Darwin was described.
- Policy 1.1 excludes WA public holidays but the policy does not list them; the resolution deadline assumes none fall 16 to 19 Nov 2026. Please confirm against the WA public holiday calendar.
- SLA status is computed as of the latest thread timestamp (2026-11-16 03:50 UTC); if this handoff is read later, recompute. If the ticket is still unresolved after 2026-11-19 01:05 UTC, it is breached.
- Policy 5.2 Team Lead notification is not required at escalation (P2 was within target, not at risk), but it would apply if the ticket becomes at risk (2026-11-18 03:20 UTC) or is raised to P1.
