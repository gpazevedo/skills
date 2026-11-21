# Escalation handoff: TRN-77102, Coldwater Freight Pty Ltd (CWF-2210)

**Service level:** Within target, resolution deadline Thu 19 Nov 2026 01:05 UTC (09:05 AWST), Business plan P2 "27 business hours" (policy 3.1); as of 2026-11-16 03:50 UTC about 24h15m of the 27 business hours remain (about 90%, above the 25% at-risk line in 4.4).
**Next action:** Get a G4-C modem diagnostic (cellular modem firmware version and registration logs on a Darwin/Katherine unit) to test the unconfirmed MX-31.4 link, and send the customer an update by 04:00 UTC Tue 17 Nov.

## Problem as currently understood
14 of 61 gateways (all G4-C cellular units at Darwin and Katherine) stopped reporting during the 14 Nov firmware 4.7.2 rollout and have not reconnected; the 47 G4-E Ethernet units are fine. The opening report was "ALL gateways offline"; this narrowed after Tier 1 checked TernCloud at 01:25 UTC. Likely cause is gateway-side modem registration failure, possibly tied to the 4.7.2 cellular modem update, but not confirmed.

Evidence:
- [Verified] 61 gateways on the account: 30 G4-E Perth, 17 G4-E Adelaide, 11 G4-C Darwin, 3 G4-C Katherine (Account record, CWF-2210).
- [Verified] 47 gateways online and reporting normally, 14 offline, in TernCloud as of 01:25 UTC (Marcus Lee, TernCloud, 2026-11-16 01:32 UTC).
- [Verified] The 14 offline are the Darwin (11) and Katherine (3) units; each last reported 18:20 to 18:24 UTC Sat 14 Nov, in the rollout window that started 18:00 UTC (Marcus Lee, TernCloud, 01:32 UTC).
- [Verified] All 61 gateways were updated to 4.7.2; the 47 online units run 4.7.2; their readings are complete with no gaps (Marcus Lee, TernCloud, 01:32 UTC).
- [Verified] All 14 offline units are G4-C and all 47 online units are G4-E (Marcus Lee, internal note 02:10 UTC; matches account record).
- [Verified] All 14 SIMs are Active in the Tern Connect console; last data sessions ended 18:21 to 18:24 UTC 14 Nov; no session attempts since (Marcus Lee, console, 02:10 UTC).
- [Verified] 4.7.2 release notes include "cellular modem firmware updated to MX-31.4 (G4-C only)" (Marcus Lee, internal note 02:10 UTC). The link to the outage is a hypothesis, not confirmed.
- [Verified] SMS wake sent to DRW-GW-01, DRW-GW-05, KTH-GW-02 at 02:05 UTC; no response by 02:10 UTC (Marcus Lee, internal note).
- [Reported] Darwin units show solid green power light and flashing amber NET light, unchanged after power-cycling all 11 this morning (Grant Tobias, 03:05 UTC). Not observed by Tern. Marcus Lee's reading, from the LED guide, is that flashing amber NET on a G4-C means the modem is not registered on the mobile network (03:40 UTC); that is an interpretation of reported lights.
- [Reported] Darwin team rebooted all Darwin gateways before the call, with no change (Grant Tobias via Marcus Lee's call note, 01:05 UTC; Grant Tobias, 03:05 UTC).
- [Reported] Katherine units have not been touched (Grant Tobias, 03:05 UTC).
- [Reported] Temperature data lost "for the last three days" and "around $40,000 a day" in stock that cannot be certified (Grant Tobias, 01:12 UTC); Perth cannot dispatch Darwin loads without certificates (Grant Tobias, 03:05 UTC).
- [Reported] The gateway firmware push was Tern's ("your firmware push", Grant Tobias, 01:12 UTC). The account record says firmware rollouts are customer-scheduled with a default Saturday 18:00 UTC window; Marcus Lee called it "your scheduled firmware window". Who triggered this rollout is not recorded.
- Conflict: Grant reports "every one of our gateways went dark" and "every site is affected" (01:12 and 03:05 UTC); verified, 47 of 61 are online with complete readings and 14 are offline (Marcus Lee, 01:32 UTC). Perth and Adelaide being unaffected by the outage itself is verified; any indirect impact on Perth dispatch is reported only.
- Conflict: "lost all our temperature data for the last three days" (reported) vs the outage starting 18:21 UTC Sat 14 Nov, about 31 hours before 01:25 UTC Mon (verified, last sessions). Whether the 14 units hold unsent readings locally is unknown; Marcus Lee notes G4 units store locally and upload on reconnect, so loss is not yet established.

## Tried so far
- 2026-11-16 01:05 UTC, Marcus Lee: ticket logged during the call at P2; fleet status check -> 14 of 61 offline, all G4-C (see evidence).
- 2026-11-16 01:32 UTC, Marcus Lee: emailed fleet findings; asked Darwin for front-panel lights -> customer replied 03:05 UTC (lights above).
- Before 01:05 UTC (customer, reported), Darwin team: rebooted all Darwin gateways -> no change.
- Morning of 16 Nov (customer, reported, by 03:05 UTC), Darwin site: power-cycled all 11 units again -> no change in lights.
- 2026-11-16 02:05 UTC, Marcus Lee: SMS wake to DRW-GW-01, DRW-GW-05, KTH-GW-02 -> no response by 02:10 UTC; later result not recorded.
- 2026-11-16 02:10 UTC, Marcus Lee: checked Tern Connect SIM status and release notes -> SIMs Active, MX-31.4 noted.
- 2026-11-16 03:40 UTC, Marcus Lee: asked customer not to factory-reset units -> customer response not recorded.
- 2026-11-16 03:50 UTC, Marcus Lee: escalated to Tier 2; priority kept at P2 -> pending.
- No firmware rollback, remote reconfiguration or carrier-side check has been tried; none is recorded.

## Commitments to the customer
- "I'll send you an update by 12:00 AWST tomorrow, Tuesday 17 November (04:00 UTC), or sooner if engineering has news." (Marcus Lee, 2026-11-16 03:40 UTC), due 04:00 UTC Tue 17 Nov, open. Tier 2 now owns it (policy 5.3).
- Call back "within the hour" (Marcus Lee's call note, 01:05 UTC; paraphrase from an internal note, not a verbatim customer-facing quote), due by 02:05 UTC; call-back occurred before the 01:32 UTC email ("after call-back"), met.
- Reported, unconfirmed: Grant says an unnamed Tern engineer told him "last week" that 4.7.2 "was fixed and safe to roll out" (Grant Tobias, 01:12 and 03:05 UTC). No matching message, call or ticket found (Marcus Lee, 01:32 UTC; the last ticket is TRN-75530, closed 2 Oct). Treat as a customer assertion; Grant says "this one is on Tern", so expect a credit or liability request. No credit, refund or fix date has been promised; Marcus said he cannot give a fix date (03:40 UTC).

## Service level
- Plan: Business (account record).
- Priority: P2, recorded at ticket creation (Marcus Lee, 01:05 UTC) and kept at 03:50 UTC. Policy 2.1: P1 is "more than half of the customer's gateways are offline"; verified 14 of 61 (about 23%) are offline, so the customer's P1 request does not meet the criteria. Policy 2.5: "a priority applies only once recorded on the ticket". The reported "all gateways" impact would qualify for P1, but is contradicted by verified data, so there is no mismatch on the verified facts. Reassess if more units go offline (over 30 offline would reach P1).
- Target: Business P2 (policy 3.1): first response "4 business hours", resolution "27 business hours".
- Clock: started at ticket creation, 2026-11-16 01:05 UTC (09:05 AWST Monday), inside business hours (policy 4.1; 1.1/1.2: 00:30 to 09:30 UTC, Mon to Fri). Pauses: only while "Pending customer" (4.2); none recorded, status went Open then Escalated. Assumes no WA public holiday in 17 to 19 Nov (none stated in the inputs).
- Deadline: 27 business hours of 9h/day: Mon 8h25m (01:05 to 09:30 UTC), Tue 9h, Wed 9h, leaving 35m on Thu from 00:30 UTC, so Thu 19 Nov 2026 01:05 UTC (09:05 AWST), as of now = 2026-11-16 03:50 UTC (as-of time in the thread export). Elapsed 2h45m; remaining 24h15m. Status: within target (4.4). At risk begins when under 6h45m remain (25% of 27h), which is Wed 18 Nov 2026 03:20 UTC (11:20 AWST).
- First response: met at 01:05 UTC, when the agent logged the ticket during the call (policy 1.4).
- Escalation: Tier 1 to Tier 2 under 5.1 (cannot be resolved with documented procedures). Policy 5.2 Support Team Lead notification applies to P1 or at-risk P2; neither applies now and no notification is recorded. Updates (7.1, P2): at least once each business day.
- Resolution (1.5) requires a fix or workaround restoring function and status Resolved.

## Recommended next action
Obtain direct evidence from a G4-C unit of what state the modem is in (modem firmware version, network registration and error logs), starting with the Katherine units, which the customer has not power-cycled. Ask Katherine to report their LEDs without power-cycling or resetting, and compare with Darwin. This turns the key reported claim (NET light flashing, not registered) and the unconfirmed MX-31.4 hypothesis into verified facts, and decides whether a rollback or modem fix is possible. It comes first because it has the most bearing on the fix and on the stored data, and the only open commitment is a status update.

Open questions:
- Is MX-31.4 the cause? Do the 14 units show a modem firmware version change, or a registration failure at carrier level (SIM active, no sessions)?
- Is the customer's data intact on the offline units, and what is the local storage window?
- Who triggered the rollout, Tern or the customer's schedule?
- Is there any record of a Tern engineer saying 4.7.2 was safe? Ask Grant for date or name; check with Rhys Kaplan (Account Manager).
- Did the customer follow the "do not factory-reset" request?
- Did the SMS wake produce any response after 02:10 UTC?
- Credit or liability: only Rhys Kaplan or the Head of Customer Support may offer one (policy 6.3); Tier 2 must not promise a fix date or credit (6.2).

Next customer update due: 04:00 UTC Tue 17 Nov 2026 (12:00 AWST), from Marcus Lee's commitment of 03:40 UTC.
