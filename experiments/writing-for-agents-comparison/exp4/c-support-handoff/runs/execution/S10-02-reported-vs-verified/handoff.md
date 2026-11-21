# Escalation handoff: TRN-77102, Coldwater Freight Pty Ltd (CWF-2210)

**In one line:** 14 of 61 gateways (all G4-C cellular, Darwin and Katherine) went offline during the 14 Nov firmware 4.7.2 rollout and are still offline. Cause is unknown. Marcus Lee promised the customer an update by 04:00 UTC Tue 17 Nov (12:00 AWST), and the P2 resolution deadline is Thu 19 Nov 01:05 UTC.

## Problem as currently understood
- [verified] 61 gateways on the account: Kewdale 30 and Wingfield 17 (G4-E, Ethernet), Darwin 11 and Katherine 3 (G4-C, cellular). (evidence: account record, Gateway fleet table)
- [verified] 47 gateways are online and reporting normally, and 14 are offline. (evidence: Marcus Lee read TernCloud as of 01:25 UTC, email 01:32 UTC)
- [verified] The 14 offline gateways are the 11 Darwin and 3 Katherine units. Each last reported between 18:20 and 18:24 UTC on Sat 14 Nov, during the firmware window (rollout began 18:00 UTC). (evidence: Marcus Lee, TernCloud, email 01:32 UTC)
- [verified] All 61 gateways were updated to 4.7.2 in that window, and the 47 online units run 4.7.2. Readings from the 47 online units are complete with no gaps. (evidence: Marcus Lee, TernCloud, 01:32 UTC)
- [verified] All 14 offline units are G4-C and all 47 online units are G4-E, so the hardware model separates the two groups. (evidence: Marcus Lee, internal note 02:10 UTC; matches the account record fleet table)
- [verified] In the Tern Connect console all 14 SIMs are Active. Their last data sessions ended between 18:21 and 18:24 UTC on 14 Nov, with no session attempts since. (evidence: Marcus Lee, internal note 02:10 UTC)
- [verified] A remote SMS wake sent at 02:05 UTC to DRW-GW-01, DRW-GW-05 and KTH-GW-02 got no response from any of them by 02:10 UTC. (evidence: Marcus Lee, internal note 02:10 UTC). Only a 5-minute window is recorded.
- [verified] The 4.7.2 release notes include "cellular modem firmware updated to MX-31.4 (G4-C only)". (evidence: Marcus Lee, internal note 02:10 UTC; the release notes themselves are not in the supplied material)
- [reported] Darwin units show a solid green power light and a flashing amber NET light. Power-cycling all 11 Darwin units again on the morning of 16 Nov changed nothing. (source: Grant Tobias, relaying the Darwin site lead, email 03:05 UTC). Nobody at Katherine has touched their units.
- [reported] Darwin gateways were rebooted before the 01:05 UTC call and it made no difference. (source: Grant Tobias, call note 01:05 UTC)
- [reported] Customer has lost "all our temperature data for the last three days". (source: Grant Tobias, email 01:12 UTC). Support says data loss is not yet known, because G4 units store readings locally and upload on reconnect (Marcus Lee, 01:32 UTC, stated without a recorded check).
- [reported] The outage costs about $40,000 a day in stock that cannot be certified. Perth cannot dispatch Darwin loads without the certificates. (source: Grant Tobias, 01:12 and 03:05 UTC)
- [reported] A Tern engineer told Grant by phone the week before that 4.7.2 was fixed and safe to roll out, so the customer says "this one is on Tern". (source: Grant Tobias, 01:12 and 03:05 UTC). He cannot name the engineer. Marcus found no record of a call or ticket that week.
- [suspected] The 4.7.2 cellular modem firmware update (MX-31.4) stops the G4-C modems registering on the mobile network. (held by: Marcus Lee; basis: the model split, the release note, and the flashing amber NET light, which Marcus says the LED guide reads as "modem isn't registered on the mobile network". "Possible link; not confirmed.") No check has been run on the modem firmware.
- [suspected] The fault is on the gateway side rather than in the SIM accounts. (held by: Marcus Lee, 03:40 UTC; basis: SIMs Active and the LED guide reading)
- Conflicts:
  - Customer says "ALL gateways" are down, and the ticket title says "ALL gateways offline". The thread's TernCloud check and the account record show 14 of 61 offline, and the customer's own mention that Perth cannot dispatch Darwin loads fits a Darwin/Katherine-only outage. The account record fleet table wins for fleet facts.
  - Customer says data is lost for "three days". The offline units stopped reporting at about 18:20 UTC Sat 14 Nov, which is about 1 day 9.5 hours before 03:50 UTC Mon 16 Nov. This is a time-count mismatch, not yet checked with the customer.
  - Customer says a Tern engineer vouched for 4.7.2. Marcus found no record of this (the last ticket on the account is TRN-75530, closed 2 Oct 2026, a P3 bracket replacement). Not resolved.
  - Customer requested P1. The ticket is at P2 (see Service level).

## Tried so far
| What was tried | Who, when | Result |
|---|---|---|
| Checked fleet status in TernCloud | Marcus Lee, 01:25 UTC | 47 online, 14 offline (Darwin, Katherine) |
| Called the customer back (promised within the hour) | Marcus Lee, about 01:30 UTC (email 01:32 says "as discussed on the phone just now") | Call-back made; no content recorded other than what the email repeats |
| Checked the Tern Connect console for SIM status | Marcus Lee, by 02:10 UTC | All 14 SIMs Active; last sessions 18:21 to 18:24 UTC 14 Nov; no attempts since |
| Compared hardware model across the online and offline units | Marcus Lee, by 02:10 UTC | Offline = G4-C, online = G4-E; release note mentions MX-31.4 for G4-C |
| Remote SMS wake to DRW-GW-01, DRW-GW-05, KTH-GW-02 | Marcus Lee, 02:05 UTC | No response by 02:10 UTC; no later check recorded |
| Rebooted all Darwin gateways (before the call) | Customer (Darwin team), before 01:05 UTC 16 Nov | No difference (reported) |
| Power-cycled all 11 Darwin units again | Customer (Darwin site lead), morning of 16 Nov, before 03:05 UTC | Lights unchanged: solid green power, flashing amber NET (reported) |
| Asked Darwin for front-panel light states (Marcus 01:32); customer asked not to factory-reset (03:40) | Marcus Lee | Lights reported at 03:05 UTC; no factory reset is known to have been done |
| Asked the customer who the engineer from last week was | Marcus Lee, 01:32 UTC | Customer cannot name him; unresolved |

## Commitments to the customer
| Commitment (quoted) | Made by | When | Due | Status |
|---|---|---|---|---|
| "I'd check the fleet and call him back within the hour" (call note, 01:05 UTC) | Marcus Lee (Tier 1) | 01:05 UTC Mon 16 Nov, by phone | 02:05 UTC Mon 16 Nov | met (call-back before 01:32 UTC) |
| "I'll send you an update by 12:00 AWST tomorrow, Tuesday 17 November (04:00 UTC), or sooner if engineering has news." (email 03:40 UTC) | Marcus Lee (Tier 1) | 03:40 UTC Mon 16 Nov | 04:00 UTC Tue 17 Nov | pending (24 h 10 min left at 03:50 UTC); owned by Tier 2 from escalation (policy 5.3) |
| "If you can tell me who you spoke to, I'll follow it up." (email 01:32 UTC, about the earlier engineer call) | Marcus Lee (Tier 1) | 01:32 UTC Mon 16 Nov | none; conditional on the customer naming the engineer | no date given |

Not commitments: Marcus's "I can't give you a fix date", and the request not to factory-reset. No fix date, credit, refund or compensation has been promised. Policy 6.2 bars agents from promising one, and 6.3 reserves credits and refunds to the Account Manager (Rhys Kaplan per the account record) or the Head of Customer Support. No such offer is on the ticket or in the account record.

## Service level
- Tier: Business support plan (account record, "Support plan: Business")
- Priority/severity: P2 (thread: ticket created at P2, and the 03:50 UTC event records it "unchanged"). The customer's P1 request is recorded but not applied. Policy 2.1 defines P1 as "more than half of the customer's gateways are offline"; 14 of 61 is 23%. Policy 2.5: "a priority applies only once recorded on the ticket".
- Target: Resolution is "27 business hours" for Business P2 (policy 3.1). First response is "4 business hours".
- Clock rule: "The clock starts when the ticket is created" (4.1). Business hours are 08:30 to 17:30 AWST Mon to Fri, excluding WA public holidays (1.1), which is 00:30 to 09:30 UTC (1.2). Paused only while status is "Pending customer" (4.2). Escalation does not stop the clock.
- Deadline: Thu 19 Nov 2026 01:05 UTC (09:05 AWST).
  - Arithmetic: created Mon 16 Nov 01:05 UTC, which is inside business hours.
  - Mon 01:05 to 09:30 = 8 h 25 min. Tue = 9 h and Wed = 9 h, so 26 h 25 min used by end of Wed 18 Nov.
  - 27 h - 26 h 25 min = 35 min remaining, counted from Thu 00:30 UTC, so the deadline is Thu 01:05 UTC.
  - Pause rule: the supplied status history shows only Open then Escalated, with no "Pending customer" period, so none was applied. Any pause would move the deadline later. If a WA public holiday falls on Tue 17 to Wed 18 Nov, the deadline would also move later; the policy does not list holidays and none was checked.
  - Without pause rule, with a 27 h target and no pauses, the deadline is the same: Thu 19 Nov 01:05 UTC. The status history before 01:05 UTC is not in the export.
  - If priority were ever changed to P1 (policy 4.3): the target would be 24 hours on a 24x7 basis from creation, so Tue 17 Nov 01:05 UTC. Not applicable at the moment.
- First response: target "4 business hours" (3.1). The ticket was logged by an agent during the customer's call at 01:05 UTC, which counts as first response when logged (1.4). Status: met at 0 minutes elapsed.
- Status: open, within target. As of 03:50 UTC Mon 16 Nov (the thread's stated as-of time), 2 h 45 min of 27 business hours are used and 24 h 15 min remain. "At risk" is under 25% remaining (6 h 45 min), so the ticket is not at risk (policy 4.4). The ticket is not at risk, so policy 5.2 (Team Lead notification) does not apply on that ground, and the thread records none. Business hours remaining: Mon 03:50 to 09:30 UTC = 5 h 40 min, then Tue 9 h, Wed 9 h, Thu 35 min = 24 h 15 min.
- Customer update cadence: P2 requires "at least once each business day" (7.1); Marcus's promised update at 04:00 UTC Tue falls on Tuesday's business day.

## Recommended next action
Test the leading suspected cause, that the 4.7.2 modem firmware MX-31.4 is stopping G4-C modems from registering. The cheapest check is on the Tern side, with no customer visit needed. Pull the 4.7.2 / MX-31.4 notes and known issues for G4-C, and look at the other G4-C gateways on 4.7.2 across TernCloud for the same offline pattern after their rollouts, with the last-session time after update.
- If other G4-C fleets on 4.7.2 went offline the same way, the modem firmware is the likely cause. Escalate to the firmware team for a fix or rollback path, and ask whether stored readings survive it (the customer has been told not to factory-reset).
- If other G4-C units on 4.7.2 are fine, the modem firmware alone is less likely. Move on to what is specific to Darwin and Katherine, such as carrier network or APN settings, or the rollout itself.

In parallel, ask Lina Petrakis (technical contact) to read the Katherine units' lights without power-cycling them, to see whether they match Darwin. Also check whether the SMS wake was retried after 02:10 UTC.

Customer update: send before 04:00 UTC Tue 17 Nov (12:00 AWST), the time Marcus promised. Tier 2 owns it now (policy 5.3). Do not promise a fix date, credit or refund (6.2); the Account Manager Rhys Kaplan or the Head of Customer Support would handle any credit question (6.3). The update can cover the model split, what is being checked, and the instruction not to factory-reset.

## Gaps
- Not stated in the thread: whether the Support Team Lead was told. Policy 5.2 requires it only for P1 or at-risk P2, and this is neither.
- Not stated in the policy: WA public holidays on 17 to 19 Nov (none checked). Not stated in the thread: any "Pending customer" status history before escalation.
- The 4.7.2 release notes were not supplied. Only Marcus's one-line quote of them is available.
- No one has examined the unit LEDs directly. The LED guide was cited but not supplied.
- The SMS wake result covers only 5 minutes and 3 of the 14 units.
- Katherine units have not been checked at all. Data loss on the 14 units is unknown.
- The engineer who allegedly said 4.7.2 was fixed is unidentified. No record exists in the supplied material.
- Customer business impact ($40,000 a day) is the customer's figure, with no supporting evidence in the account record.
