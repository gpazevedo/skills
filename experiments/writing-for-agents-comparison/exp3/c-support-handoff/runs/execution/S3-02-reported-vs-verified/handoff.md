# Escalation handoff: TRN-77102, Coldwater Freight Pty Ltd

**Service level:** within target, deadline Thu 19 Nov 2026 01:05 UTC (09:05 AWST), Business P2 resolution "27 business hours" (policy 3.1); becomes at risk from Wed 18 Nov 03:20 UTC (11:20 AWST) (policy 4.4)
**Next action:** Reproduce on a lab G4-C: update it to firmware 4.7.2 and check whether its cellular modem (MX-31.4) registers on the mobile network.

## Problem as currently understood
The 14 cellular G4-C gateways at Darwin (11) and Katherine (3) have been offline since 18:20 to 18:24 UTC on Sat 14 Nov, during the customer's 4.7.2 rollout window; their SIMs are active but the units make no data session attempts, and the Darwin units' LEDs indicate the modem is not registered on the mobile network. The 47 Ethernet G4-E gateways on the same 4.7.2 firmware are online, so the fault follows the hardware model, and the G4-C-only modem firmware update (MX-31.4) in 4.7.2 is a possible but unconfirmed cause. This differs from the opening report ("ALL gateways offline", total data loss): the fleet check showed only the cellular sites are down and that data for the online units is complete.

Evidence:
- [Verified] Fleet has 61 gateways: 47 online and reporting normally, 14 offline (Marcus Lee, TernCloud fleet status as of 01:25 UTC, reported to customer 2026-11-16 01:32 UTC)
- [Verified] The 14 offline units are all at Darwin (11) and Katherine (3); each last reported between 18:20 and 18:24 UTC on Sat 14 Nov, during the scheduled firmware window that started at 18:00 UTC (Marcus Lee, TernCloud, 2026-11-16 01:32 UTC)
- [Verified] All 61 gateways were updated to firmware 4.7.2 in that window; the 47 online units all run 4.7.2 (Marcus Lee, TernCloud, 2026-11-16 01:32 UTC)
- [Verified] Readings from the 47 online units are complete in TernCloud with no gaps; TernCloud has no readings from the 14 offline units after their last report (Marcus Lee, TernCloud, 2026-11-16 01:32 UTC)
- [Verified] All 14 offline units are G4-C (cellular); all 47 online units are G4-E (Ethernet) (Marcus Lee, internal model check, 2026-11-16 02:10 UTC; matches the account record fleet table: DRW and KTH are G4-C cellular, PER and ADL are G4-E Ethernet)
- [Verified] All 14 SIMs are status Active; their last data sessions ended 18:21 to 18:24 UTC on 14 Nov, with no session attempts since (Marcus Lee, Tern Connect console, 2026-11-16 02:10 UTC)
- [Verified] The 4.7.2 release notes include "cellular modem firmware updated to MX-31.4 (G4-C only)"; the link to the outage is not confirmed (Marcus Lee, release notes, 2026-11-16 02:10 UTC)
- [Verified] Remote SMS wake sent to DRW-GW-01, DRW-GW-05 and KTH-GW-02 at 02:05 UTC; none responded by 02:10 UTC (Marcus Lee, internal note, 2026-11-16 02:10 UTC)
- [Verified] Per the LED guide, a flashing amber NET light on a G4-C means the cellular modem is not registered on the mobile network (Marcus Lee, LED guide, 2026-11-16 03:40 UTC)
- [Verified] No record of a call or ticket with Coldwater in the week before; the last ticket was TRN-75530, closed 2 October (Marcus Lee, ticket records, 2026-11-16 01:32 UTC; account record lists TRN-75530 as the only recent ticket)
- [Verified] Firmware rollouts on this account are customer-scheduled, default window Saturdays from 18:00 UTC (account record)
- [Reported] Every Darwin unit shows a solid green power light and a flashing amber NET light, unchanged after a second power-cycle of all 11 Darwin units this morning; nobody at Katherine has touched their units (Grant Tobias, relaying the Darwin site lead, 2026-11-16 03:05 UTC)
- [Reported] All Coldwater gateways stopped reporting after the weekend firmware update ("Every one of our gateways went dark") (Grant Tobias, call 2026-11-16 01:05 UTC and email 2026-11-16 01:12 UTC)
- [Reported] "We've lost all our temperature data for the last three days" (Grant Tobias, 2026-11-16 01:12 UTC)
- [Reported] A Tern engineer told him by phone last week that 4.7.2 "was fixed and safe to roll out"; he does not remember the engineer's name (Grant Tobias, 2026-11-16 01:12 UTC and 03:05 UTC)
- [Reported] Cost of around $40,000 a day in stock that cannot be certified for delivery (Grant Tobias, 2026-11-16 01:12 UTC)
- [Reported] "Every site is affected: Perth can't dispatch the Darwin loads without the certificates" (Grant Tobias, 2026-11-16 03:05 UTC)
- [Reported] G4 gateways store readings locally when they cannot reach TernCloud and upload them on reconnect, so stored data may survive (Marcus Lee, product statement in email, 2026-11-16 01:32 UTC; not checked on these units)
- Conflict: customer reports every gateway went dark; TernCloud shows 47 of 61 online and only the 14 cellular units offline. The ticket title "ALL gateways offline" reflects the reported claim, not the verified state.
- Conflict: customer reports all temperature data lost for three days; TernCloud shows complete readings for the 47 online units, and the 14 offline units may hold readings locally. The outage began 18:20 UTC Sat 14 Nov, about 31 hours before the email, not three days.
- Conflict: customer reports a Tern engineer cleared 4.7.2 by phone last week; Tier 1 found no record of any call or ticket that week.
- Conflict: customer calls it "your firmware push"; the account record shows rollouts are customer-scheduled, and Marcus described the window as "your scheduled firmware window".

## Tried so far
- Before 2026-11-16 01:05 UTC, customer (Darwin team): rebooted all Darwin gateways -> no difference (reported by Grant Tobias, call note 01:05 UTC)
- 2026-11-16 01:25 UTC, Marcus Lee: checked fleet status in TernCloud -> 47 online, 14 offline, all offline units at Darwin and Katherine
- 2026-11-16 ~01:30 UTC, Marcus Lee: called the customer back with the fleet status -> done (email 01:32 UTC says "as discussed on the phone just now")
- 2026-11-16 by 02:10 UTC, Marcus Lee: checked SIMs in Tern Connect console -> all 14 Active, no session attempts since 18:24 UTC 14 Nov
- 2026-11-16 by 02:10 UTC, Marcus Lee: compared models of offline and online units -> offline all G4-C, online all G4-E
- 2026-11-16 02:05 UTC, Marcus Lee: remote SMS wake to DRW-GW-01, DRW-GW-05, KTH-GW-02 -> no response by 02:10 UTC
- 2026-11-16 morning (before 03:05 UTC), Darwin site staff: power-cycled all 11 Darwin units again -> LEDs unchanged (reported by Grant Tobias, 03:05 UTC)
- 2026-11-16 03:05 UTC, Darwin site lead: read front-panel LEDs -> solid green power, flashing amber NET on every Darwin unit (reported)
- 2026-11-16 03:40 UTC, Marcus Lee: interpreted LEDs against the LED guide -> modem not registered on mobile network; told customer not to factory-reset units
- 2026-11-16 03:50 UTC, Marcus Lee: escalated to Tier 2 (Field Systems Engineering) -> status Escalated, priority P2 unchanged

## Commitments to the customer
- "I told him I'd check the fleet and call him back within the hour." (Marcus Lee, call note, 2026-11-16 01:05 UTC), due within the hour (by 02:05 UTC), met (call-back referenced in email at 01:32 UTC)
- "If you can tell me who you spoke to, I'll follow it up." (Marcus Lee, 2026-11-16 01:32 UTC), due when the customer names the person (no time given), open (customer replied at 03:05 UTC without a name)
- "I'm escalating this to our Field Systems Engineering team now." (Marcus Lee, 2026-11-16 03:40 UTC), due now, met (escalated 03:50 UTC)
- "I'll send you an update by 12:00 AWST tomorrow, Tuesday 17 November (04:00 UTC), or sooner if engineering has news." (Marcus Lee, 2026-11-16 03:40 UTC), due 12:00 AWST Tue 17 Nov (04:00 UTC), open. Tier 2 now owns this commitment (policy 5.3).
- Reported, unconfirmed: a Tern engineer said by phone last week that 4.7.2 "was fixed and safe to roll out" (Grant Tobias, 2026-11-16 01:12 UTC), no matching message or record in the thread, status unknown.
- No credit, refund or compensation has been offered. The customer's "this one is on Tern" and $40,000-a-day figure point toward a claim; only the Account Manager (Rhys Kaplan) or the Head of Customer Support may offer one, in writing (policy 6.2, 6.3).

## Service level
- Plan: Business (account record; policy 1.3 "The customer's support plan ... is the one in the account record")
- Priority: P2 (set by Marcus Lee at creation 2026-11-16 01:05 UTC, reconfirmed at escalation 03:50 UTC). Customer requested P1; not applied. Policy 2.1: "P1 (Critical): more than half of the customer's gateways are offline, or TernCloud is unavailable to all of the customer's users." Verified 14 of 61 offline (23%) does not meet this. Policy 2.2: "P2 (High): some of the customer's gateways are offline ... and there is no practical workaround" fits the verified impact. The reported impact ("every one of our gateways went dark") would earn P1 under 2.1, but it is contradicted by the verified fleet status, so no mismatch on the verified facts. Policy 2.5: "a priority applies only once recorded on the ticket."
- Target: "Business | P2 | 4 business hours | 27 business hours" (policy 3.1). First response met: ticket logged by an agent during the customer's call at 01:05 UTC (policy 1.4: "A ticket logged by an agent during a call with the customer counts as a first response when logged").
- Clock: started at ticket creation, 2026-11-16 01:05 UTC (Mon, 09:05 AWST) (policy 4.1 "The clock starts when the ticket is created"). Business hours only: "08:30 to 17:30 Australia/Perth time ... Monday to Friday, excluding Western Australian public holidays" = "00:30 to 09:30 UTC" (policy 1.1, 1.2, 3.3). Pauses: only while status is "Pending customer" (policy 4.2); the ticket has never been in that status (Open, then Escalated), so no paused time. The inputs do not list WA public holidays; the deadline assumes none fall on 16 to 19 Nov 2026.
- Deadline: Thu 19 Nov 2026 01:05 UTC (09:05 AWST). Count: Mon 16 Nov 01:05 to 09:30 UTC = 8h25m; Tue 17 = 9h; Wed 18 = 9h (26h25m); Thu 19 from 00:30 UTC + 35m = 27h. As of now = 2026-11-16 03:50 UTC (latest timestamp in the thread; the user gave no time): 2h45m used, 24h15m (about 90%) remaining, so "within target" (policy 4.4). At risk once less than 25% (6h45m) remains: from Wed 18 Nov 03:20 UTC (11:20 AWST). If the priority were raised to P1, policy 4.3 would apply the Business P1 target "24 hours, 24x7" from creation, giving a deadline of Tue 17 Nov 01:05 UTC.

## Recommended next action
Take a lab G4-C, update it to firmware 4.7.2 (including modem firmware MX-31.4), and check whether the modem registers on the mobile network and opens a data session. This is the most decisive open question: it would turn the leading hypothesis (the G4-C-only modem update stops the modem registering) into a verified cause, and it points directly at the workaround or fix, such as a modem firmware rollback, that resolution needs. It also tells you whether a fix can be delivered remotely at all, since the 14 units cannot currently reach the network, which shapes what Darwin and Katherine site staff must do on site before the 04:00 UTC Tuesday update.

Open questions:
- Is MX-31.4 the cause, and is there a rollback or recovery path that does not need network access (local or on-site procedure) and does not factory-reset the units?
- Do the 14 units still hold their readings locally since 18:20 UTC 14 Nov, and will they upload them on reconnect? This decides whether any data is actually lost.
- What do the 3 Katherine units' LEDs show? They have not been checked or touched.
- Is there a practical interim workaround (for example, temporary Ethernet backhaul at Darwin)? If one exists, the case may fit P3 under policy 2.3; if Coldwater's certification needs cannot be met without it, P2 stands.
- Who, if anyone, at Tern told Grant Tobias last week that 4.7.2 was fixed? No record found so far; the follow-up commitment is open.
- Does the $40,000-a-day impact claim need to go to the Account Manager, Rhys Kaplan, now?
- Support Team Lead notification is required only for a P1 or an at-risk P2 at escalation (policy 5.2); this ticket was within target at escalation, but notification becomes relevant if it reaches at risk at 03:20 UTC Wed 18 Nov.

Next customer update due: 12:00 AWST Tue 17 Nov 2026 (04:00 UTC), from Marcus Lee's commitment; this also meets policy 7.1 "P2: at least once each business day".
