Clarifying question: What is the current date, time and time zone? The sources do not give one, so every status below is measured as of the last thread entry (2026-11-16 03:50 UTC, the escalation event), with the times at which each status changes listed so it can be read against the actual current time.

# Escalation handoff: TRN-77102 14 cellular (G4-C) gateways at Darwin and Katherine offline since firmware 4.7.2 rollout

**Customer:** Coldwater Freight Pty Ltd, account CWF-2210, Business support plan (account record: "Support plan: Business")   **Severity/priority:** P2 (thread, Event 2026-11-16 01:05 UTC "Priority: P2"; unchanged at Event 2026-11-16 03:50 UTC). Customer requested P1; not applied because 14 of 61 gateways are offline and policy 2.1 sets P1 at "more than half of the customer's gateways are offline".
**Most urgent deadline:** Customer update promised for 2026-11-17 04:00 UTC (12:00 AWST, Tuesday 17 November) (thread, Marcus Lee 2026-11-16 03:40 UTC). Tier 2 now owns this commitment: policy 5.3 "From escalation, Tier 2 owns the ticket, including customer updates and commitments already made."

## Problem as currently understood
Since the customer's firmware 4.7.2 rollout on Saturday 14 November (window from 18:00 UTC), all 14 G4-C (cellular) gateways at Darwin (11) and Katherine (3) have stopped reporting to TernCloud, while all 47 G4-E (Ethernet) gateways on the same firmware report normally. The SIMs are active on the carrier side but the units have made no data session attempts since 18:24 UTC on 14 November, and the Darwin units reportedly show a flashing amber NET light, which the LED guide reads as the modem not registered on the mobile network. Support's untested hypothesis is that the G4-C-only cellular modem firmware (MX-31.4) bundled in 4.7.2 is the cause; whether readings from the offline units are lost or held on the units is unknown.

| Fact | Status | How established / cite |
|---|---|---|
| Fleet is 61 gateways: Kewdale (PER) 30 G4-E, Wingfield (ADL) 17 G4-E, Darwin (DRW) 11 G4-C, Katherine (KTH) 3 G4-C | Verified | Account record, "Gateway fleet (61 units)" table; matches TernCloud count in thread, Marcus Lee 2026-11-16 01:32 UTC |
| As of 01:25 UTC on 16 Nov, 47 gateways online and reporting normally, 14 offline | Verified | Marcus Lee read TernCloud; thread, Marcus Lee 2026-11-16 01:32 UTC |
| The 14 offline gateways are all at Darwin (11) and Katherine (3) | Verified | TernCloud; thread, Marcus Lee 2026-11-16 01:32 UTC |
| Each offline unit last reported between 18:20 and 18:24 UTC on Saturday 14 Nov, during the firmware window that started 18:00 UTC | Verified | TernCloud; thread, Marcus Lee 2026-11-16 01:32 UTC; window matches account record "default maintenance window Saturdays from 18:00 UTC" |
| All 61 gateways were updated to 4.7.2 in that window; all 47 online units run 4.7.2 | Verified | TernCloud; thread, Marcus Lee 2026-11-16 01:32 UTC |
| All 14 offline units are G4-C (cellular); all 47 online units are G4-E (Ethernet) | Verified | Model check by Marcus Lee; thread, internal note 2026-11-16 02:10 UTC; consistent with account record fleet table |
| 4.7.2 release notes include "cellular modem firmware updated to MX-31.4 (G4-C only)" | Verified | Marcus Lee read the release notes; thread, internal note 2026-11-16 02:10 UTC |
| All 14 SIMs are status Active; their last data sessions ended 18:21 to 18:24 UTC on 14 Nov; no session attempts since | Verified | Tern Connect console checked by Marcus Lee; thread, internal note 2026-11-16 02:10 UTC |
| Remote SMS wake sent at 02:05 UTC to DRW-GW-01, DRW-GW-05 and KTH-GW-02; none responded by 02:10 | Verified | Performed by Marcus Lee; thread, internal note 2026-11-16 02:10 UTC |
| All Darwin units show a solid green power light and a flashing amber NET light | Reported | Customer relaying Darwin site lead; thread, Grant Tobias 2026-11-16 03:05 UTC. Katherine LED state not reported |
| Per the LED guide, a flashing amber NET light on a G4-C means the cellular modem is not registered on the mobile network | Verified (guide content) | Marcus Lee cited the LED guide; thread, Marcus Lee 2026-11-16 03:40 UTC. Applies to these units only if the Reported LED state is confirmed |
| The fault is on the gateway side, not the SIM accounts | Hypothesis | Marcus Lee: "that points to a problem on the gateway side rather than with the SIM accounts, but I can't confirm the cause yet"; thread, 2026-11-16 03:40 UTC |
| The MX-31.4 modem firmware in 4.7.2 caused the outage | Hypothesis | Marcus Lee: "Possible link; not confirmed."; thread, internal note 2026-11-16 02:10 UTC. No test recorded |
| Customer's team rebooted all Darwin gateways after the update; no difference | Reported | Thread, call note Marcus Lee 2026-11-16 01:05 UTC |
| Darwin staff power-cycled all 11 Darwin units again on the morning of 16 Nov; lights came back the same | Reported | Thread, Grant Tobias 2026-11-16 03:05 UTC |
| Nobody at Katherine has touched its 3 units | Reported | Thread, Grant Tobias 2026-11-16 03:05 UTC |
| Customer says all gateways went dark / every gateway is affected | Reported | Thread, call note 2026-11-16 01:05 UTC; Grant Tobias 2026-11-16 01:12 UTC. Contradicted by TernCloud (see disagreements) |
| Customer says all temperature data for the last three days is lost | Reported | Thread, Grant Tobias 2026-11-16 01:12 UTC |
| Readings from the 47 online gateways are complete in TernCloud with no gaps; TernCloud has no readings from the 14 offline units after their last report | Verified | TernCloud; thread, Marcus Lee 2026-11-16 01:32 UTC |
| Readings from the 14 offline units are held on the units and will upload on reconnection | Hypothesis | Marcus Lee states G4 gateways store readings locally and upload on reconnect, "so I can't yet tell whether any data has actually been lost"; thread, 2026-11-16 01:32 UTC. Not checked on these units |
| Impact: about $40,000 a day in stock that cannot be certified for delivery | Reported | Thread, Grant Tobias 2026-11-16 01:12 UTC |
| Impact: Perth cannot dispatch the Darwin loads without the certificates ("every site is affected") | Reported | Thread, Grant Tobias 2026-11-16 03:05 UTC |
| A Tern engineer told the customer by phone the week before that 4.7.2 "was fixed and safe to roll out"; engineer's name not known | Reported | Thread, Grant Tobias 2026-11-16 01:12 UTC and 03:05 UTC |
| Support finds no record of a call or ticket with Coldwater the week before; last ticket was TRN-75530, closed 2 October | Verified | Marcus Lee checked records; thread, 2026-11-16 01:32 UTC; account record "Recent tickets: TRN-75530 ... Closed 2 October 2026" |
| Ticket priority P2; customer's P1 request recorded and not applied | Verified | Thread, Events 2026-11-16 01:05 UTC and 03:50 UTC |

**Open disagreements:**
- Scope: the customer says every gateway went dark (01:05 call note, 01:12 email); TernCloud shows 14 of 61 offline, all G4-C at Darwin and Katherine (01:32). The customer's later "every site is affected" (03:05) is a business-impact claim (Perth dispatch depends on Darwin certificates), not a gateway-status claim.
- Data loss: the customer says three days of temperature data are lost (01:12); support finds the 47 online units' data complete and cannot yet tell whether the 14 offline units' readings are lost or stored locally (01:32). The customer's "three days" also exceeds the time elapsed between the last reports (14 Nov 18:20 UTC) and the email (16 Nov 01:12 UTC), about 31 hours.
- Cause and liability: the customer attributes the outage to "your firmware push" and says it "is on Tern" because an engineer said 4.7.2 was safe (01:12); support finds firmware version alone does not separate the groups, since all 61 run 4.7.2 and only G4-C units are down (02:10), and finds no record of the claimed call (01:32).
- Priority: the customer asked for P1 (01:05, 01:12); support kept P2 under policy 2.1 (01:32, 03:50).

## What has been tried
| When | Who | Action | Result | Cite |
|---|---|---|---|---|
| Between the update on 14 Nov and 16 Nov 01:05 UTC (exact time not recorded) | Customer's Darwin team | Rebooted all Darwin gateways | "made no difference" (Reported) | Call note, Marcus Lee 2026-11-16 01:05 UTC |
| 16 Nov, read as of 01:25 UTC | Marcus Lee (Tier 1) | Checked fleet status in TernCloud | 47 online, 14 offline (DRW 11, KTH 3); last reports 18:20 to 18:24 UTC 14 Nov; all 61 on 4.7.2; online units' data complete | Marcus Lee 2026-11-16 01:32 UTC |
| 16 Nov, by 01:32 UTC | Marcus Lee (Tier 1) | Searched for a record of the claimed call or ticket the week before | None found; last ticket TRN-75530 closed 2 October | Marcus Lee 2026-11-16 01:32 UTC |
| 16 Nov, by 02:10 UTC | Marcus Lee (Tier 1) | Checked SIM status in Tern Connect console | All 14 SIMs Active; last sessions ended 18:21 to 18:24 UTC 14 Nov; no session attempts since | Internal note, Marcus Lee 2026-11-16 02:10 UTC |
| 16 Nov, by 02:10 UTC | Marcus Lee (Tier 1) | Compared models of online and offline units; read 4.7.2 release notes | Offline all G4-C, online all G4-E; release notes list modem firmware MX-31.4 (G4-C only) | Internal note, Marcus Lee 2026-11-16 02:10 UTC |
| 16 Nov 02:05 UTC | Marcus Lee (Tier 1) | Remote SMS wake to DRW-GW-01, DRW-GW-05, KTH-GW-02 | No response from any by 02:10 UTC | Internal note, Marcus Lee 2026-11-16 02:10 UTC |
| 16 Nov 01:32 UTC (request); reply 03:05 UTC | Marcus Lee asked; Darwin site lead checked | Front-panel LED readout on Darwin units | All Darwin units: solid green power, flashing amber NET (Reported). Katherine not checked | Marcus Lee 2026-11-16 01:32 UTC; Grant Tobias 2026-11-16 03:05 UTC |
| Morning of 16 Nov, before 03:05 UTC (exact time not recorded) | Darwin site staff | Power-cycled all 11 Darwin units again | "the lights came back the same" (Reported) | Grant Tobias 2026-11-16 03:05 UTC |
| 16 Nov 03:40 UTC | Marcus Lee (Tier 1) | Looked up the LED pattern in the LED guide | Flashing amber NET on G4-C = modem not registered on mobile network | Marcus Lee 2026-11-16 03:40 UTC |
| 16 Nov 03:40 UTC | Marcus Lee (Tier 1) | Told the customer not to factory-reset any unit, to protect stored readings | Not recorded (no customer acknowledgement in the thread) | Marcus Lee 2026-11-16 03:40 UTC |
| 16 Nov 03:50 UTC | Marcus Lee (Tier 1) | Escalated to Tier 2 (Field Systems Engineering) | Status Open → Escalated; priority P2 unchanged | Event 2026-11-16 03:50 UTC |

## Commitments to the customer
| Commitment (verbatim) | Made by (role) | When / cite | Deadline | Kept / Open / Missed |
|---|---|---|---|---|
| "I told him I'd check the fleet and call him back within the hour." (made by phone; the words are Marcus's internal record of the call, not the customer-facing wording) | Marcus Lee (Support Agent, Tier 1) | Call note, 2026-11-16 01:05 UTC | 2026-11-16 02:05 UTC (01:05 + 1 hour) | Kept: call-back and fleet check done, confirmed in email "as discussed on the phone just now", 2026-11-16 01:32 UTC |
| "If you can tell me who you spoke to, I'll follow it up." | Marcus Lee (Tier 1) | Email, 2026-11-16 01:32 UTC | None set; conditional on the customer naming the engineer | Open: customer replied he does not remember the name (Grant Tobias 2026-11-16 03:05 UTC); no follow-up recorded |
| "I'm escalating this to our Field Systems Engineering team now." | Marcus Lee (Tier 1) | Email, 2026-11-16 03:40 UTC | "now" | Kept: escalated at Event 2026-11-16 03:50 UTC |
| "I'll send you an update by 12:00 AWST tomorrow, Tuesday 17 November (04:00 UTC), or sooner if engineering has news." | Marcus Lee (Tier 1); owned by Tier 2 from escalation (policy 5.3) | Email, 2026-11-16 03:40 UTC | 2026-11-17 04:00 UTC | Open as of the last thread entry. Becomes Missed if no update is sent by 2026-11-17 04:00 UTC; the thread export ("full ticket history") records no update after 2026-11-16 03:50 UTC |

All four are within policy 6.1 ("Support agents may commit to the time of the next update and to actions they will take themselves."). Marcus explicitly declined a fix date ("I can't give you a fix date", 03:40), in line with policy 6.2. No credit, refund or compensation has been offered (account record "Open credits: None"). The customer's $40,000-a-day figure and "this one is on Tern" (01:12) invite one: policy 6.3 says "Only the Account Manager named in the account record, or the Head of Customer Support, may offer a service credit, refund or compensation." The named Account Manager is Rhys Kaplan (account record).

## Service-level status
Basis: Business plan (account record), P2 (Event 2026-11-16 01:05 UTC). Business hours per policy 1.2: "08:30 to 17:30 AWST is 00:30 to 09:30 UTC on the same date", Monday to Friday (policy 1.1), so 9 business hours per business day. 16 November 2026 is a Monday (thread: "Tuesday 17 November"). Ticket created 2026-11-16 01:05 UTC (09:05 AWST), inside business hours. No pause applies: policy 4.2 "The clock is paused only while the ticket status is 'Pending customer'", and the thread shows only Open and Escalated. Statuses are as of the last thread entry, 2026-11-16 03:50 UTC, when 2 h 45 min of business time had elapsed (01:05 to 03:50).

| Clock | Policy clause (quoted) | Started | Deadline (with arithmetic) | Status |
|---|---|---|---|---|
| First response | 3.1 "Business \| P2 \| 4 business hours"; 1.4 "A ticket logged by an agent during a call with the customer counts as a first response when logged." | Ticket created 2026-11-16 01:05 UTC | 01:05 + 4 business hours = 2026-11-16 05:05 UTC (all within Monday's 00:30 to 09:30 UTC window) | Met: first response at 2026-11-16 01:05 UTC (ticket logged by Marcus Lee during the customer's call) |
| Resolution | 3.1 "Business \| P2 \| ... \| 27 business hours"; 4.1 "The clock starts when the ticket is created." | Ticket created 2026-11-16 01:05 UTC | Mon 16 Nov 01:05 to 09:30 = 8 h 25 min (18 h 35 min left); Tue 17 Nov 00:30 to 09:30 = 9 h (9 h 35 min left); Wed 18 Nov 00:30 to 09:30 = 9 h (35 min left); Thu 19 Nov 00:30 + 35 min = **2026-11-19 01:05 UTC (09:05 AWST)** | Within target as of 2026-11-16 03:50 UTC (24 h 15 min of 27 h remaining). Policy 4.4: "at risk" if "less than 25% of its resolution target remains": 25% of 27 h = 6 h 45 min, reached after 20 h 15 min elapsed: 8 h 25 min (Mon) + 9 h (Tue) + 2 h 50 min (Wed from 00:30) = **at risk from 2026-11-18 03:20 UTC (11:20 AWST)**; **breached after 2026-11-19 01:05 UTC** if not Resolved |
| Customer update interval | 7.1 "P2: at least once each business day." | Business day of ticket creation, Mon 16 Nov | Each business day by its close, 09:30 UTC: Mon 16 Nov met; next due by 2026-11-17 09:30 UTC (17:30 AWST), then 18, 19, 20 Nov 09:30 UTC. The open commitment (04:00 UTC 17 Nov) is earlier than the policy's Tuesday deadline | Mon 16 Nov: met (updates at 01:32 and 03:40 UTC). Tue 17 Nov onward: on track as of the last thread entry; no later update recorded in the thread |

Escalation notice: policy 5.2 requires the Support Team Lead to be notified when "an at-risk P2 ticket, is escalated". At escalation (03:50 UTC 16 Nov) the ticket was within target, so the notice was not required then. If the priority is changed to P1, policy 4.3 applies the new resolution target "counted from ticket creation", which for Business P1 is "24 hours, 24x7": 2026-11-16 01:05 UTC + 24 h = 2026-11-17 01:05 UTC.

## Recommended next action
Test the MX-31.4 hypothesis directly: update a lab G4-C to firmware 4.7.2 (which carries modem firmware MX-31.4) and check whether its modem registers on the mobile network; in the same step, ask the customer's technical contact, Lina Petrakis (IT Manager, account record), to have Katherine read the NET light on its 3 untouched units, to confirm the Reported LED state on units nobody has power-cycled.

Evidence: firmware version alone does not separate the groups (all 61 on 4.7.2), but model does (all 14 offline are G4-C, all 47 online G4-E; 02:10 internal note); the 4.7.2 release notes change modem firmware only on G4-C; failures began 18:20 to 18:24 UTC, inside the update window; SIMs are Active yet no session attempts have occurred since; SMS wake got no response; and Darwin units reportedly show the LED pattern the guide reads as "modem not registered" (03:05, 03:40). Repeated power cycles at Darwin changed nothing (Reported).

What the result settles: if the lab G4-C fails to register after the update, the cause is the G4-C modem firmware in 4.7.2, and the fix path is a modem firmware recovery that does not rely on the cellular link (the units cannot be reached remotely). If the lab unit registers normally, the modem-firmware hypothesis is weakened and the investigation moves to site or carrier factors at Darwin and Katherine. Either way, any recovery step must avoid a factory reset until it is confirmed whether readings are stored on the units (03:40), since that decides the customer's data-loss claim.

Deadline to beat: the update promised for **2026-11-17 04:00 UTC (12:00 AWST)**, now Tier 2's to keep (policy 5.3). The resolution clock goes at risk at 2026-11-18 03:20 UTC and is breached after 2026-11-19 01:05 UTC.

## Gaps
- Current date, time and time zone not supplied: all statuses are as of 2026-11-16 03:50 UTC. Closed by the user giving the current time; then re-read each status against the thresholds above.
- WA public holidays: policy 1.1 excludes them from business hours, but no holiday calendar is in the sources. The resolution arithmetic assumes none falls on 16 to 19 November 2026. Closed by checking the WA public holiday list.
- Katherine units' LED state not reported (Grant Tobias 03:05: "Nobody at Katherine has touched theirs yet"). Closed by a site readout.
- Whether readings are stored on the 14 offline units: not checked (Marcus Lee 01:32). Closed by local diagnostics on an offline unit or by reconnection.
- Cause not tested: the MX-31.4 link is a Hypothesis (02:10). Closed by the recommended lab test.
- Time of the customer's first Darwin reboot not recorded (01:05 call note).
- Customer acknowledgement of the "don't factory-reset" instruction not recorded (03:40).
- Identity of the engineer who allegedly said 4.7.2 was safe: customer cannot name him (03:05); no record found (01:32). Commitment to follow up is Open with nothing to follow. Closed by checking internal call logs for calls with Coldwater in the week of 9 November, or by asking the customer for the date and number called.
- The modem firmware version actually running on the offline units (MX-31.4 or otherwise) is not recorded; only the release notes were read (02:10). Closed by local diagnostics on an offline unit.
