# Escalation handoff: TRN-77102 14 of 61 gateways (all cellular G4-C, Darwin and Katherine) offline since 4.7.2 firmware rollout

**Customer:** Coldwater Freight Pty Ltd (CWF-2210), Business support plan | **Priority:** P2 (set by Marcus Lee, Tier 1; customer's request for P1 recorded and not applied)
**Service level:** within target, next deadline 2026-11-17 09:30 UTC (daily P2 update; 29 h 40 min calendar time remaining at reference time). Resolution due 2026-11-19 01:05 UTC.
**Open commitments:** 2, earliest due 2026-11-17 04:00 UTC (12:00 AWST), the update promised by Marcus Lee. Tier 2 now owns it (policy 5.3).

## Problem as currently understood
Since 18:20 to 18:24 UTC on Saturday 14 November, during the customer's scheduled 4.7.2 firmware rollout, 14 of Coldwater's 61 gateways have not reported to TernCloud: all 11 at Darwin and all 3 at Katherine. These 14 are exactly the cellular G4-C units; the 47 Ethernet G4-E units are on 4.7.2 and reporting normally with no data gaps (Verified, Marcus Lee). The 14 SIMs are Active on the carrier side but have made no data session attempts since 14 Nov, and SMS wake to three units got no response (Verified, Marcus Lee). The customer reports the Darwin units show a flashing amber NET light after repeated power cycles, which per the LED guide means the modem is not registered on the mobile network; Marcus Lee's hypothesis is that the cellular modem firmware MX-31.4 bundled in 4.7.2 for G4-C only is the cause (not confirmed).

| Fact | Tag | Source |
|---|---|---|
| "all Coldwater gateways stopped reporting after the firmware update on the weekend"; "Every one of our gateways went dark" | Reported (Grant Tobias). Contradicted by the Verified 47/14 split below | Call note 2026-11-16 01:05; email 01:12 |
| Fleet is 61 gateways | Verified (Marcus Lee, TernCloud; matches account record) | Email 01:32; account.md "Gateway fleet (61 units)" |
| As of 01:25 UTC 16 Nov, 47 gateways online and reporting normally, 14 offline | Verified (Marcus Lee, TernCloud) | Email 01:32 |
| The 14 offline are Darwin (11) and Katherine (3) | Verified (Marcus Lee, TernCloud) | Email 01:32 |
| Each offline unit last reported between 18:20 and 18:24 UTC Sat 14 Nov; rollout started 18:00 UTC | Verified (Marcus Lee, TernCloud) | Email 01:32 |
| All 61 gateways were updated to 4.7.2 in that window; the 47 online units run 4.7.2 | Verified (Marcus Lee, TernCloud). Running version of the 14 offline units not separately shown, see open questions | Email 01:32 |
| Readings from the 47 online gateways complete in TernCloud, no gaps | Verified (Marcus Lee, TernCloud) | Email 01:32 |
| TernCloud has no readings from the 14 offline gateways after their last report | Verified (Marcus Lee, TernCloud) | Email 01:32 |
| "We've lost all our temperature data for the last three days" | Reported (Grant Tobias). Contradicted for the 47 online units | Email 01:12 |
| G4 gateways buffer readings locally and upload on reconnect, so data from the 14 may not be lost | Hypothesis (Marcus Lee; product behaviour stated, not checked on these units) | Email 01:32 |
| All 14 SIMs status Active; last data sessions ended 18:21 to 18:24 UTC 14 Nov; no session attempts since | Verified (Marcus Lee, Tern Connect console) | Internal note 02:10 |
| All 14 offline units are G4-C (cellular); all 47 online units are G4-E (Ethernet) | Verified (Marcus Lee; matches account record fleet table) | Internal note 02:10; account.md fleet table |
| 4.7.2 release notes include "cellular modem firmware updated to MX-31.4 (G4-C only)" | Verified (Marcus Lee, release notes) | Internal note 02:10 |
| MX-31.4 modem firmware is linked to the outage | Hypothesis (Marcus Lee: "Possible link; not confirmed") | Internal note 02:10 |
| SMS wake sent to DRW-GW-01, DRW-GW-05, KTH-GW-02 at 02:05 UTC; no response by 02:10 | Verified (Marcus Lee) | Internal note 02:10 |
| Customer's team rebooted all Darwin gateways before 16 Nov; no difference | Reported (Grant Tobias) | Call note 01:05 |
| Every Darwin unit shows solid green power light and flashing amber NET light | Reported (Grant Tobias relaying Darwin site lead) | Email 03:05 |
| All 11 Darwin units power-cycled again on the morning of 16 Nov; lights came back the same | Reported (Grant Tobias) | Email 03:05 |
| Katherine units not touched by anyone on site | Reported (Grant Tobias) | Email 03:05 |
| Flashing amber NET on a G4-C means the cellular modem is not registered on the mobile network | Verified as LED guide content (Marcus Lee); applies to Darwin only via the Reported LED state | Email 03:40 |
| Fault is on the gateway side rather than the SIM accounts | Hypothesis (Marcus Lee: "I can't confirm the cause yet") | Email 03:40 |
| A Tern engineer told the customer by phone last week that 4.7.2 was "fixed and safe to roll out"; engineer's name not remembered | Reported (Grant Tobias) | Email 01:12; email 03:05 |
| No record of a call or ticket with Coldwater last week; last ticket TRN-75530, closed 2 Oct | Verified (Marcus Lee; matches account record recent tickets) | Email 01:32; account.md "Recent tickets" |
| Cost to customer around $40,000 a day in stock that cannot be certified for delivery | Reported (Grant Tobias) | Email 01:12 |
| "every site is affected: Perth can't dispatch the Darwin loads without the certificates" | Reported (Grant Tobias). Business impact; Perth (Kewdale) gateways themselves are among the 47 online | Email 03:05 |

**Open questions:**
- Did the 14 G4-C units complete the 4.7.2 update, including the MX-31.4 modem firmware, or stop part-way? What firmware and modem firmware are they actually running?
- Is MX-31.4 the cause (Marcus Lee's hypothesis), and does 4.7.2 fail the same way on any G4-C unit, or only in Coldwater's setup?
- What do the 3 untouched Katherine units' LEDs show? (Only Darwin has been reported.)
- Are readings buffered on the 14 units, how much buffer capacity is left after roughly 2 days offline, and will they upload on reconnect?
- Is there a recovery path (modem firmware rollback, local reflash) that does not require a factory reset, which Marcus asked the customer to avoid?
- Who, if anyone, spoke to the customer last week about 4.7.2? No record found so far.

## What has been tried
| Action | By | When | Result |
|---|---|---|---|
| Rebooted all Darwin gateways | Customer's team (Reported) | Before 2026-11-16 01:05 UTC; exact time not recorded | "made no difference" (Reported) |
| Checked fleet status in TernCloud | Marcus Lee | 2026-11-16 01:25 UTC | 47 online, 14 offline (DRW 11, KTH 3), last reports 18:20 to 18:24 UTC 14 Nov, no gaps for online units |
| Searched for a record of last week's call or ticket | Marcus Lee | By 2026-11-16 01:32 UTC | None found; last ticket TRN-75530 closed 2 Oct |
| Asked customer for front-panel lights on two or three units | Marcus Lee | 2026-11-16 01:32 UTC | Answered 03:05: Darwin all solid green power, flashing amber NET |
| Checked SIM status in Tern Connect console | Marcus Lee | By 2026-11-16 02:10 UTC | All 14 Active; no session attempts since 18:21 to 18:24 UTC 14 Nov |
| Compared models of online and offline units; read 4.7.2 release notes | Marcus Lee | By 2026-11-16 02:10 UTC | Offline = all G4-C, online = all G4-E; release notes list MX-31.4 modem firmware for G4-C only |
| Sent remote SMS wake to DRW-GW-01, DRW-GW-05, KTH-GW-02 | Marcus Lee | 2026-11-16 02:05 UTC | No response from any by 02:10 |
| Power-cycled all 11 Darwin units again | Darwin site (Reported) | Morning of 2026-11-16; exact time not recorded | Lights came back the same (Reported) |
| Interpreted LED state against LED guide | Marcus Lee | 2026-11-16 03:40 UTC | Flashing amber NET = modem not registered on mobile network |
| Advised customer not to factory-reset any unit | Marcus Lee | 2026-11-16 03:40 UTC | Result not recorded (no customer acknowledgement in thread) |
| Escalated to Tier 2 (Field Systems Engineering) | Marcus Lee | 2026-11-16 03:50 UTC | Status Open to Escalated; priority P2 unchanged |

## Commitments to the customer
| Commitment (quoted) | Made by | When | Status |
|---|---|---|---|
| "I told him I'd check the fleet and call him back within the hour" (said to customer on the call; recorded in Marcus's call note) | Marcus Lee | 2026-11-16 01:05 UTC (due 02:05) | Met: call-back and email by 01:32 ("as discussed on the phone just now") |
| "If you can tell me who you spoke to, I'll follow it up." | Marcus Lee | 2026-11-16 01:32 UTC | Open: customer replied at 03:05 with no name ("one of your engineers"); no follow-up recorded; no due time given |
| "I'm escalating this to our Field Systems Engineering team now." | Marcus Lee | 2026-11-16 03:40 UTC | Met: escalated 03:50 |
| "I'll send you an update by 12:00 AWST tomorrow, Tuesday 17 November (04:00 UTC), or sooner if engineering has news." | Marcus Lee | 2026-11-16 03:40 UTC | Open, due 2026-11-17 04:00 UTC; owned by Tier 2 from escalation (policy 5.3) |

Not commitments: Marcus said "I can't confirm the cause yet and I can't give you a fix date" (03:40). No fix date, credit or compensation has been offered (policy 6.2, 6.3; account record "Open credits: None").

**Requested, not committed:**
- P1 priority: requested by Grant Tobias on the call (01:05) and by email ("This needs to be P1.", 01:12). Declined by Marcus Lee at 01:32 and recorded as not applied at 03:50, since 14 of 61 gateways are offline (policy 2.1 needs "more than half").
- No explicit request for a credit or compensation, but the customer states "this one is on Tern" and cites about $40,000 a day in losses (01:12). Only Account Manager Rhys Kaplan or the Head of Customer Support may offer anything (policy 6.3).

## Service level
Measured at 2026-11-16 03:50 UTC (Mon 11:50 AWST), the escalation event and last entry in the thread. Recompute if reading later.

Readings used for ambiguous terms:
- Business hours: policy 1.2 "08:30 to 17:30 AWST is 00:30 to 09:30 UTC on the same date", so one business day = 9 business hours. 16 Nov is a Monday (thread: "tomorrow, Tuesday 17 November").
- "excluding Western Australian public holidays" (1.1): the policy lists no dates; I assumed no WA public holiday falls on 16 to 19 Nov 2026.
- "P2: at least once each business day" (7.1): read as at least one customer update in each business day the ticket is open, due by 17:30 AWST (09:30 UTC) that day. The policy does not state when this cadence clock starts or whether "Pending customer" pauses it.
- First response: policy 1.4 "A ticket logged by an agent during a call with the customer counts as a first response when logged."

| Target (policy quote) | Clock start | Deadline (arithmetic) | Status |
|---|---|---|---|
| First response, Business P2: "4 business hours" (3.1) | Ticket created 2026-11-16 01:05 UTC, inside business hours (4.1: "The clock starts when the ticket is created") | 01:05 + 4 h = 2026-11-16 05:05 UTC. Response at 01:05 (ticket logged during call, 1.4), 0 h elapsed | Met |
| Resolution, Business P2: "27 business hours" (3.1); 4.1 "Business-hours targets count only time inside business hours" | 2026-11-16 01:05 UTC | Mon 01:05 to 09:30 = 8 h 25 min (18 h 35 min left); Tue 17 Nov 9 h (9 h 35 min left); Wed 18 Nov 9 h (35 min left); Thu 19 Nov 00:30 + 35 min = **2026-11-19 01:05 UTC** (09:05 AWST). Elapsed at reference time: 01:05 to 03:50 = 2 h 45 min; remaining 24 h 15 min (89.8%) | Within target |
| At-risk threshold: "'at risk' if less than 25% of its resolution target remains" (4.4) | Same as resolution | 25% of 27 h = 6 h 45 min; at risk after 20 h 15 min elapsed: Mon 8 h 25 min + Tue 9 h = 17 h 25 min, plus 2 h 50 min on Wed from 00:30 = **2026-11-18 03:20 UTC** (11:20 AWST) | Not yet at risk |
| Update cadence: "P2: at least once each business day" (7.1) | Policy does not state the event that starts this clock | Mon 16 Nov: updates sent 01:32 and 03:40, met. Tue 17 Nov: due by 09:30 UTC (17:30 AWST); the open commitment (04:00 UTC) is earlier | Met for 16 Nov; 17 Nov within target |

Pauses: 4.2 "The clock is paused only while the ticket status is 'Pending customer'." Status went Open to Escalated; it has never been "Pending customer", so no paused time.

Priority note: if the priority were changed to P1 (for example if more gateways go offline, 2.1), 4.3 says "the resolution target becomes the target for the new priority, counted from ticket creation": Business P1 "24 hours, 24x7" gives 2026-11-16 01:05 + 24 h = 2026-11-17 01:05 UTC, and P1 updates become "at least every 4 hours, 24x7" (7.1). Escalating a P2 once it is at risk requires notifying the Support Team Lead (5.2); this escalation happened before the at-risk point.

## Recommended next action
Tier 2 (Field Systems Engineering) to test Marcus Lee's MX-31.4 hypothesis by updating a G4-C test unit to 4.7.2 and checking whether its modem fails to register (flashing amber NET, no data sessions), and in parallel pull the firmware and modem-firmware version the 14 units last reported to TernCloud before 18:24 UTC 14 Nov. Owner: Tier 2 Field Systems Engineering. By 2026-11-17 04:00 UTC. Because: the evidence already isolates the fault to the G4-C model on 4.7.2 (all 14 offline are G4-C, all 47 G4-E are fine, SIMs Active with no session attempts), so confirming or ruling out MX-31.4 decides between a fleet-wide modem rollback path and a site-specific cause; the result can go into the update promised to the customer for 04:00 UTC 17 Nov, which Tier 2 now owns, and leaves about 8 business hours (Tue 04:00 to 09:30 UTC, then Wed 00:30 to 03:20 UTC) before the resolution target turns at risk at 03:20 UTC 18 Nov (due 01:05 UTC 19 Nov). This is my recommendation, not a step recorded in the thread.
