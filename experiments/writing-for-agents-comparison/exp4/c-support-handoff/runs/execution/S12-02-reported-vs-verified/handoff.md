# Escalation handoff: TRN-77102 - 14 G4-C cellular gateways (Darwin, Katherine) offline since the 4.7.2 firmware rollout

Customer: Coldwater Freight Pty Ltd (CWF-2210) | Tier: Business | Priority: P2 (set on ticket by Marcus Lee, 2026-11-16 01:05 UTC; customer requested P1, not applied) | Prepared: 2026-11-16 03:50 UTC (the export's as-of time)

## Service level
Policy 3.1, Business P2: "First response 4 business hours; Resolution 27 business hours" | Resolution deadline: Thu 2026-11-19 01:05 UTC (09:05 AWST) | Status: Within target, 24h15m of 27 business hours remaining (not at risk; policy 4.4 at-risk line is under 6h45m remaining)
Arithmetic: clock starts at ticket creation, Mon 16 Nov 01:05 UTC (09:05 AWST, inside business hours 00:30-09:30 UTC, policy 1.1-1.2, 4.1). Used so far 01:05 to 03:50 = 2h45m; status never "Pending customer", so no paused time (4.2). Deadline: Mon 01:05-09:30 = 8h25m, Tue 9h, Wed 9h = 26h25m, so the last 0h35m falls on Thu from 00:30 = 01:05 UTC Thu 19 Nov. Remaining now: 27h - 2h45m = 24h15m. No public holiday assumed: the policy says WA public holidays are excluded but the case lists none for 16-19 Nov; engineer should confirm. First response: Met at creation, 01:05 UTC (policy 1.4, ticket logged during the call).
Priority basis: policy 2.1 needs more than half of gateways offline for P1. Verified 14 of 61 offline (23%), so P2 under 2.2. If priority changes, 4.3 recalculates from creation.

## Problem as currently understood
After the customer-scheduled firmware rollout to 4.7.2 (started Sat 14 Nov 18:00 UTC), all 14 G4-C cellular gateways (Darwin 11, Katherine 3) stopped reporting around 18:20-18:24 UTC and have not reconnected. The 47 G4-E Ethernet gateways (Perth, Adelaide) on 4.7.2 are online. Leading hypothesis, unconfirmed: the 4.7.2 cellular modem firmware update (MX-31.4, G4-C only) left the modems unable to register on the network. The customer says all gateways are affected and that data is lost; support's check shows only the 14 are offline, and data loss is not yet established.
- [Verified] 61 gateways in fleet; 47 online and reporting, 14 offline, all at Darwin (11) and Katherine (3); all 61 updated to 4.7.2 (Marcus Lee, 2026-11-16 01:32, TernCloud check as of 01:25 UTC). Matches the account record fleet table (reading it, not a Tern check of the thread).
- [Verified] The 14 offline last reported 18:20-18:24 UTC on 14 Nov; 47 online readings are complete with no gaps (Marcus Lee, 01:32).
- [Verified] All 14 SIMs Active in Tern Connect, last data sessions ended 18:21-18:24 UTC 14 Nov, no attempts since (Marcus Lee, internal note 02:10).
- [Verified] All 14 offline units are G4-C, all 47 online are G4-E (Marcus Lee, 02:10). Per the account record, DRW and KTH are G4-C Cellular.
- [Verified] 4.7.2 release notes include "cellular modem firmware updated to MX-31.4 (G4-C only)"; link to the fault "not confirmed" (Marcus Lee, 02:10).
- [Reported] Darwin units show solid green power light and flashing amber NET light, unchanged after power-cycling (Grant Tobias, 03:05). Per Marcus's LED guide reading, amber NET flashing means the modem is not registered on the mobile network (Marcus Lee, 03:40; guide not checked by us, cause "can't confirm").
- [Reported] Darwin units were rebooted with no change, before 01:05 (Grant Tobias via Marcus Lee call note, 01:05) and power-cycled again the morning of 16 Nov (Grant Tobias, 03:05).
- [Reported] "Every one of our gateways went dark" and "every site is affected" (Grant Tobias, 01:12 and 03:05). Contradicted by the Verified fleet check above.
- [Reported] Lost "all our temperature data for the last three days" (Grant Tobias, 01:12). Not supported: the rollout was about 31 hours before the call; G4 units store readings locally and upload on reconnect, so loss is unknown (Marcus Lee, 01:32).
- [Reported] Cost "around $40,000 a day" in stock that cannot be certified; Perth cannot dispatch Darwin loads without certificates (Grant Tobias, 01:12 and 03:05).

## What has been tried
1. Customer rebooted all Darwin gateways - Coldwater (Grant Tobias), before 01:05, per call note - No change [Reported]
2. Marcus Lee checked fleet status in TernCloud (as of 01:25) - Marcus Lee, 01:32 - Partial: established 14 offline, 47 online; cause not found
3. Checked Tern Connect console for the SIMs; compared hardware model - Marcus Lee, 02:10 - Partial: SIMs ruled out as inactive; model split found, cause unconfirmed
4. Remote SMS wake sent to DRW-GW-01, DRW-GW-05, KTH-GW-02 - Marcus Lee, 02:05 - No change (no response by 02:10); no later result recorded
5. Customer power-cycled all 11 Darwin units again - Coldwater (Grant Tobias), morning of 16 Nov, reported 03:05 - No change [Reported]
6. Asked the customer to check front-panel lights at Darwin - Marcus Lee, 01:32 - Partial: Darwin answered 03:05; Katherine not yet checked
7. Told customer not to factory-reset units (would erase stored readings) - Marcus Lee, 03:40 - Unknown: no result recorded

## Commitments to the customer
- "I told him I'd check the fleet and call him back within the hour" (call note) - Marcus Lee, 01:05 - due 02:05 UTC - met: call-back and email recorded at 01:32 (the call itself is recorded only as "after call-back" in the email, not separately logged)
- "I'll send you an update by 12:00 AWST tomorrow, Tuesday 17 November (04:00 UTC), or sooner if engineering has news." - Marcus Lee, 03:40 - due Tue 2026-11-17 04:00 UTC - open; Tier 2 owns it from escalation (policy 5.3)
- "If you can tell me who you spoke to, I'll follow it up." - Marcus Lee, 01:32 - conditional on customer naming the engineer; no due time; Grant could not name him (03:05)
- Marcus stated he "can't give you a fix date" (03:40); no fix date, credit, refund or compensation was promised anywhere in the thread.
Claimed by customer, not found in thread: that a Tern engineer said "last week" that 4.7.2 "was fixed and safe to roll out" (Grant Tobias, 01:12 and 03:05; Marcus found no call or ticket, last ticket TRN-75530 closed 2 Oct, 01:32). Customer also states "this one is on Tern" (liability); the thread contains no Tern acceptance of this. Policy 6.2-6.3: only the Account Manager (Rhys Kaplan) or Head of Customer Support may offer credit or compensation, in writing.

## Open questions
- Which MX modem firmware version is actually on the 14 units, and does it equal MX-31.4? Not checked.
- Do the Katherine units show the same lights? Nobody there has touched them (Grant Tobias, 03:05).
- Did the SMS wake reach anything after 02:10? No result recorded.
- Are readings stored on the 14 units intact? Unknown; recovery depends on units not being reset.
- Did any customer-side change besides the rollout occur (APN, carrier, antennas, SIM changes)? Not in the thread.
- Which engineer did the customer speak to "last week"? Not found.
- Are any WA public holidays in 16-19 Nov that would shift the deadline? None shown.
- Is the customer's loss claim of "three days" a data period actually missing from TernCloud for the 47 online units? Marcus verified those are complete.

## Recommended next action
In Tern Connect / TernCloud, pull the modem firmware version, registration and attach logs for DRW-GW-01, DRW-GW-05 and KTH-GW-02 (the three SMS-wake targets), and compare them with a G4-C that has not taken 4.7.2, to confirm or rule out the MX-31.4 modem firmware as the cause. Reason: the only difference found between the 14 offline and 47 online units is the G4-C model, with active SIMs, no session attempts and an amber NET light, which fit a modem that cannot register. Do this before the customer update due Tue 17 Nov 04:00 UTC (12:00 AWST), so the update can state a cause or the next step; the resolution deadline is Thu 19 Nov 01:05 UTC.
Follow-ups: (1) ask Coldwater to report the Katherine LEDs and keep every unit powered and unreset so local readings survive; (2) once cause is known, decide a remote recovery or on-site path for Darwin and Katherine, and notify the customer.
