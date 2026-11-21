# Escalation handoff: TRN-77102 - 14 cellular (G4-C) gateways offline since firmware 4.7.2 rollout

Customer: Coldwater Freight Pty Ltd (CWF-2210) | Tier: Business (account record) | Priority: P2 (set on ticket; customer requested P1, not applied) | Prepared: 2026-11-21 15:22 UTC (system clock; the ticket export ends 2026-11-16 03:50 UTC)

## Service level
"Business | P2 | 4 business hours | 27 business hours" (policy 3.1) | Resolution deadline: 2026-11-19 01:05 UTC (09:05 AWST Thu) | Status: Breached: 17 h 25 min business hours over at 2026-11-21 15:22 UTC, if still unresolved (the export records no resolution)
Clock starts at ticket creation, Mon 2026-11-16 01:05 UTC (4.1); business hours are 00:30-09:30 UTC Mon-Fri (1.2). Mon 01:05-09:30 = 8 h 25 min; Tue 9 h; Wed 9 h (26 h 25 min); Thu 00:30 + 35 min = 01:05 UTC. Over: Thu 01:05-09:30 (8 h 25 min) + Fri 9 h = 17 h 25 min. No "Pending customer" status in the thread, so no pause (4.2). Assumes no WA public holiday 16-20 Nov; the policy excludes them (1.1) but the case does not list them.
- First response: Met. The ticket was logged by Marcus Lee during the customer's call at 01:05 UTC, which counts as first response (1.4).
- At the end of the export (16 Nov 03:50 UTC) the ticket was Within target: 24 h 15 min remaining. It became "at risk" (under 25%, 6 h 45 min, remaining; 4.4) at Wed 2026-11-18 03:20 UTC.
- P2 updates are due "at least once each business day" (7.1). The export shows no update after 16 Nov.

## Problem as currently understood
After the customer's firmware 4.7.2 rollout (Sat 14 Nov from 18:00 UTC), all 14 cellular G4-C gateways (Darwin 11, Katherine 3) stopped reporting, while all 47 Ethernet G4-E gateways on the same firmware are fine. The SIMs are active on the carrier side, the units show a flashing amber NET light, and the modems appear not to register on the mobile network. 4.7.2 updates the G4-C cellular modem firmware to MX-31.4, a possible but unconfirmed cause. The customer describes the outage as every gateway and all data; support's checks show 14 of 61 offline.
- [Verified] 61 gateways; 47 online, 14 offline; offline units are Darwin (11) and Katherine (3), each last reported 18:20-18:24 UTC on 14 Nov during the firmware window; all 61 are on 4.7.2 (Marcus Lee, TernCloud check at 01:25 UTC, email 2026-11-16 01:32 UTC)
- [Verified] Readings from the 47 online gateways are complete; no readings in TernCloud from the 14 offline units after their last report (Marcus Lee, 2026-11-16 01:32 UTC)
- [Reported] G4 gateways store readings locally when they cannot reach TernCloud, so data may not be lost (Marcus Lee, 2026-11-16 01:32 UTC; product behaviour stated, not checked on these units)
- [Verified] All 14 SIMs are "Active" in Tern Connect; last data sessions ended 18:21-18:24 UTC on 14 Nov; no session attempts since (Marcus Lee, internal note 2026-11-16 02:10 UTC)
- [Verified] All 14 offline units are G4-C (cellular); all 47 online are G4-E (Ethernet) (Marcus Lee, internal note 2026-11-16 02:10 UTC; matches account record fleet table)
- [Verified] 4.7.2 release notes include "cellular modem firmware updated to MX-31.4 (G4-C only)"; link to the outage not confirmed (Marcus Lee, internal note 2026-11-16 02:10 UTC)
- [Reported] Every Darwin unit shows solid green power and flashing amber NET, unchanged after a second power cycle; Katherine units not touched (Grant Tobias relaying Darwin site lead, 2026-11-16 03:05 UTC)
- [Reported] Per the LED guide, flashing amber NET on a G4-C means the modem is not registered on the mobile network (Marcus Lee, 2026-11-16 03:40 UTC)
- [Reported] "Every one of our gateways went dark" and "We've lost all our temperature data for the last three days" (Grant Tobias, 2026-11-16 01:12 UTC); contradicted by the verified fleet check above
- [Reported] Impact: about $40,000 a day in stock that cannot be certified (Grant Tobias, 2026-11-16 01:12 UTC); Perth cannot dispatch Darwin loads without the certificates (Grant Tobias, 2026-11-16 03:05 UTC)

## What has been tried
1. Rebooted all Darwin gateways - customer's team, before 2026-11-16 01:05 UTC (Reported by Grant Tobias via call note) - No change
2. SMS remote wake sent to DRW-GW-01, DRW-GW-05, KTH-GW-02 - Marcus Lee, 2026-11-16 02:05 UTC - No change (no response by 02:10 UTC)
3. Power-cycled all 11 Darwin units again - Darwin site staff, morning of 16 Nov before 03:05 UTC (Reported by Grant Tobias) - No change (same lights)
4. Diagnostic checks (TernCloud fleet status, Tern Connect SIM status, model comparison, release notes) - Marcus Lee, 01:25-02:10 UTC on 16 Nov - Unknown: no result recorded beyond the findings above; not a fix attempt

## Commitments to the customer
Tier 2 now owns these (policy 5.3).
- "I told him I'd check the fleet and call him back within the hour" - Marcus Lee, 2026-11-16 01:05 UTC (call note) - due 02:05 UTC - met (call-back referenced in email 01:32 UTC)
- "If you can tell me who you spoke to, I'll follow it up." - Marcus Lee, 2026-11-16 01:32 UTC - due none stated - open (customer could not give a name, 03:05 UTC)
- "I'm escalating this to our Field Systems Engineering team now." - Marcus Lee, 2026-11-16 03:40 UTC - due now - met (escalation event 03:50 UTC)
- "I'll send you an update by 12:00 AWST tomorrow, Tuesday 17 November (04:00 UTC), or sooner if engineering has news." - Marcus Lee, 2026-11-16 03:40 UTC - due 2026-11-17 04:00 UTC - overdue (no update in the export)
Claimed by customer, not found in thread: "Your engineer told me on the phone last week that 4.7.2 was fixed and safe to roll out" (Grant Tobias, 2026-11-16 01:12 UTC). Marcus Lee found no call or ticket record from last week; last ticket TRN-75530 closed 2 Oct (01:32 UTC). Customer cannot name the engineer (03:05 UTC).
Customer's request for P1 is Reported (Grant Tobias, 01:05 and 01:12 UTC); 14 of 61 offline does not meet P1's "more than half" (policy 2.1).

## Open questions
- Is the ticket still unresolved, and was the 17 Nov 04:00 UTC update sent outside this export?
- Are other customers' G4-C gateways on 4.7.2 / MX-31.4 offline in the same way?
- What do carrier-side registration (attach) records show for the 14 SIMs since 14 Nov 18:20 UTC? Only data sessions were checked.
- What modem firmware version is actually on the offline units, and can 4.7.2 or the modem firmware be rolled back without a factory reset?
- How long can a G4-C store readings locally before they are overwritten? This sets the data-loss deadline.
- What do the Katherine units' lights show?
- Has the technical contact, Lina Petrakis (IT Manager), been involved? Only Grant Tobias appears in the thread.

## Recommended next action
Query TernCloud and Tern Connect for other G4-C gateways (any customer) updated to 4.7.2 / modem MX-31.4, and check whether they lost connectivity during the update. Why: the only verified difference between the 14 offline units and the 47 online ones is the G4-C cellular model, and 4.7.2 changes only the G4-C modem firmware; the SIMs are active, and the reported amber NET light points to the modem failing to register. Deadline: already past. The resolution target (19 Nov 01:05 UTC) and the promised update (17 Nov 04:00 UTC) have both passed, if the export is complete.
- Follow-up 1: Send Grant Tobias the overdue update now (policy 5.3, 7.1). Repeat the "do not factory-reset" warning, and give no fix date (6.2).
- Follow-up 2: If the modem firmware is implicated, work with Lina Petrakis on a recovery for the Darwin and Katherine units that keeps their locally stored readings.
