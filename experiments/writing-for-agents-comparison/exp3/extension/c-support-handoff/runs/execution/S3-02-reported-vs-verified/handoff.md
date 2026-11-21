# Escalation handoff: TRN-77102 14 cellular gateways (Darwin, Katherine) offline since firmware 4.7.2 rollout

**Customer:** Coldwater Freight Pty Ltd, account CWF-2210, Business support plan (account record)  **Priority:** P2 (recorded 2026-11-16 01:05 UTC; customer's request for P1 recorded and not applied, event 03:50 UTC)  **Prepared:** 2026-11-21 18:35 UTC (Sunday 2026-11-22 02:35 AWST), from the environment clock

Ticket status at last entry: Escalated to Tier 2 (Field Systems Engineering), 2026-11-16 03:50 UTC. The export is described as the full ticket history and has no entries after that time. Per policy 5.3, Tier 2 now owns the ticket, "including customer updates and commitments already made".

## Service level
| Clock | Policy clause | Started | Deadline | Status |
|---|---|---|---|---|
| First response | 3.1 Business / P2: "4 business hours"; 1.4: "A ticket logged by an agent during a call with the customer counts as a first response when logged." | 2026-11-16 01:05 UTC (ticket created during Grant Tobias's call) | 2026-11-16 05:05 UTC | Met, at 2026-11-16 01:05 UTC |
| Resolution | 3.1 Business / P2: "27 business hours"; 3.3 business hours only; 4.1 clock starts at ticket creation; 4.2 paused only while "Pending customer" | 2026-11-16 01:05 UTC | 2026-11-19 01:05 UTC (09:05 AWST Thu) | Breached, 17 h 25 min business time since breach (2 days 17 h 30 min calendar). At risk (4.4, under 25% left) from 2026-11-18 03:20 UTC |
| Customer updates | 7.1: "P2: at least once each business day." | Last update to customer 2026-11-16 03:40 UTC | End of business day Tue 2026-11-17 (09:30 UTC) | Breached: no update recorded on Tue 17, Wed 18, Thu 19 or Fri 20 Nov. Next business day is Mon 2026-11-23, 00:30 to 09:30 UTC |

- Business day = 00:30 to 09:30 UTC (policy 1.1, 1.2), 9 h. Status was never "Pending customer", so no paused time.
- Resolution: Mon 16 Nov 01:05 to 09:30 = 8 h 25 min (18 h 35 min left); Tue 17 = 9 h (9 h 35 min left); Wed 18 = 9 h (35 min left); Thu 19 00:30 + 35 min = 01:05 UTC deadline.
- At-risk point: 25% of 27 h = 6 h 45 min; Thu 19 00:30 to 01:05 = 35 min, plus 6 h 10 min back from Wed 18 09:30 = 03:20 UTC Wed 18 Nov.
- Since breach: Thu 19 01:05 to 09:30 = 8 h 25 min; Fri 20 = 9 h; Sat 21 = 0 h; total 17 h 25 min.
- Gap: the policy excludes Western Australian public holidays (1.1) but no holiday list was supplied; none were assumed for 16 to 20 November.
- Alternative reading, customer-requested P1 (not applied; 2.5: "a priority applies only once recorded on the ticket"; 2.1 needs "more than half of the customer's gateways" offline, and 14 of 61 are): first response "2 hours, 24x7" met at 01:05 UTC; resolution "24 hours, 24x7" deadline 2026-11-17 01:05 UTC, breached by 4 days 17 h 30 min; updates "every 4 hours, 24x7" breached. The outcome (breached) is the same under either reading.
- Escalation (5.1, 5.2): at escalation (03:50 UTC 16 Nov) 2 h 45 min of 27 h had elapsed, so the ticket was not at risk and Team Lead notification was not required by 5.2. The ticket has since breached; whether the Support Team Lead has been told is not stated.

## Problem as currently understood
All 14 offline gateways are the cellular G4-C units at Darwin (11) and Katherine (3); all 47 Ethernet G4-E units updated to the same firmware 4.7.2 are online with complete data. The offline units dropped off at 18:20 to 18:24 UTC on Saturday 14 November during the rollout, their SIMs are Active but have made no session attempts since, and Darwin units reportedly show a flashing amber NET light (modem not registered, per the LED guide). The leading suspected cause is the G4-C-only cellular modem firmware update to MX-31.4 included in 4.7.2; this is not confirmed.

| Fact | Status | Evidence |
|---|---|---|
| Fleet is 61 gateways: 30 G4-E Kewdale (PER), 17 G4-E Wingfield (ADL), 11 G4-C Darwin (DRW), 3 G4-C Katherine (KTH) | Verified | Account record, gateway fleet table; matches Marcus Lee's TernCloud check (01:32 email) |
| 14 gateways offline: all 11 Darwin and all 3 Katherine units | Verified | Marcus Lee, TernCloud fleet view as of 01:25 UTC 16 Nov (01:32 email) |
| 47 gateways online and reporting normally; their readings in TernCloud are complete with no gaps | Verified | Marcus Lee, TernCloud check (01:32 email) |
| "Every one of our gateways went dark" (all 61) | Reported; contradicted for 47 units | Grant Tobias, call note 01:05 and email 01:12. TernCloud shows 47 online (see Contradictions) |
| All 61 gateways updated to firmware 4.7.2 in the customer's scheduled window (rollout started 18:00 UTC Sat 14 Nov) | Verified | Marcus Lee, TernCloud (01:32 email); window matches account record "Saturdays from 18:00 UTC" |
| Offline units last reported between 18:20 and 18:24 UTC on 14 Nov | Verified | Marcus Lee, TernCloud (01:32 email) |
| All 14 SIMs status Active; last data sessions ended 18:21 to 18:24 UTC on 14 Nov; no session attempts since | Verified | Marcus Lee, Tern Connect console (internal note 02:10) |
| All 14 offline units are G4-C (cellular); all 47 online units are G4-E (Ethernet) | Verified | Marcus Lee, model check (internal note 02:10); account record fleet table |
| 4.7.2 release notes include "cellular modem firmware updated to MX-31.4 (G4-C only)" | Verified | Marcus Lee, release notes quoted in internal note 02:10 |
| Darwin units show solid green power light and flashing amber NET light, unchanged after power-cycling all 11 again on the morning of 16 Nov | Reported | Grant Tobias email 03:05, relaying the Darwin site lead |
| Katherine units: LED state not checked; "Nobody at Katherine has touched theirs yet" | Reported | Grant Tobias email 03:05 |
| Flashing amber NET on a G4-C means the cellular modem is not registered on the mobile network | Verified (as documentation) | LED guide, cited by Marcus Lee email 03:40 |
| The offline units' modems are failing to register on the mobile network (gateway side, not SIM accounts) | Suspected | Marcus Lee email 03:40, from reported LEDs plus Active SIMs; "I can't confirm the cause yet" |
| The G4-C modem firmware update (MX-31.4) in 4.7.2 caused the outage | Suspected | Marcus Lee internal note 02:10: "Possible link; not confirmed" |
| TernCloud has no readings from the 14 offline units after their last report | Verified | Marcus Lee, TernCloud (01:32 email) |
| G4 gateways store readings locally when they cannot reach TernCloud and upload on reconnect, so loss is not yet established | Stated by support, not checked on these units | Marcus Lee email 01:32; customer told not to factory-reset (03:40) |
| "We've lost all our temperature data for the last three days" | Reported; contradicted for 47 units | Grant Tobias email 01:12 |
| Business impact: "around $40,000 a day in stock we can't certify for delivery" | Reported | Grant Tobias email 01:12 |
| "Perth can't dispatch the Darwin loads without the certificates" | Reported | Grant Tobias email 03:05 |
| A Tern engineer told the customer by phone "last week" that 4.7.2 "was fixed and safe to roll out" | Reported; no record found | Grant Tobias emails 01:12 and 03:05 (name not remembered); Marcus Lee found no call or ticket (01:32 email); account record lists only TRN-75530 (closed 2 Oct 2026) |

Contradictions:
- Scope: customer says all gateways went dark (call 01:05, email 01:12, ticket title "ALL gateways offline"); TernCloud shows 47 of 61 online and 14 offline (Marcus Lee 01:32). Customer's later point (03:05) is business impact at every site, not gateway status.
- Data loss: customer says all temperature data for three days is lost (01:12); TernCloud shows no gaps for the 47 online units, and the 14 offline units may hold readings locally (Marcus Lee 01:32).
- Prior advice: customer says a Tern engineer said 4.7.2 was fixed and safe last week (01:12, 03:05); support found no record of a call or ticket (01:32), and the account record's recent tickets list only TRN-75530.
- Who initiated the update: customer calls it "your firmware push" (01:12); account record says "customer-scheduled rollouts", and Marcus Lee describes "your scheduled firmware window" (01:32).
- Priority: customer requested P1 (01:05, 01:12); recorded P2 because 14 of 61 gateways are offline (01:32, event 03:50).

## What has been tried
| When | Who | Action | Result |
|---|---|---|---|
| Before 2026-11-16 01:05 UTC (date not stated) | Customer (Grant Tobias's team) | Rebooted all Darwin gateways | "made no difference" (reported, call note 01:05) |
| 2026-11-16 01:25 UTC | Marcus Lee (Tier 1) | Checked fleet status in TernCloud | 47 online on 4.7.2, 14 offline (Darwin, Katherine), last reports 18:20 to 18:24 UTC 14 Nov (01:32 email) |
| By 2026-11-16 01:32 UTC | Marcus Lee | Searched for a record of the "last week" engineer call | No call or ticket found; last ticket TRN-75530 (01:32 email) |
| By 2026-11-16 02:10 UTC | Marcus Lee | Checked the 14 SIMs in Tern Connect console | All Active; sessions ended 18:21 to 18:24 UTC 14 Nov; no attempts since (internal 02:10) |
| By 2026-11-16 02:10 UTC | Marcus Lee | Compared models of offline and online units; read 4.7.2 release notes | Offline all G4-C, online all G4-E; release notes list MX-31.4 modem firmware for G4-C only (internal 02:10) |
| 2026-11-16 02:05 UTC | Marcus Lee | Remote SMS wake to DRW-GW-01, DRW-GW-05, KTH-GW-02 | No response from any by 02:10 (internal 02:10) |
| Morning of 2026-11-16, before 03:05 UTC | Customer (Darwin site lead) | Read front-panel LEDs; power-cycled all 11 Darwin units again | Solid green power, flashing amber NET, same after power-cycle (reported, 03:05 email) |
| By 2026-11-16 03:40 UTC | Marcus Lee | Looked up flashing amber NET in LED guide | Means modem not registered on mobile network (03:40 email) |
| 2026-11-16 03:40 UTC | Marcus Lee | Advised customer not to factory-reset any unit | Result not recorded |
| 2026-11-16 03:50 UTC | Marcus Lee | Escalated to Tier 2 (Field Systems Engineering) | Status Escalated; priority P2 unchanged (event 03:50) |

## Commitments to the customer
| When | Made by | Commitment (quoted) | Due | State |
|---|---|---|---|---|
| 2026-11-16 01:05 UTC (phone) | Marcus Lee | "I told him I'd check the fleet and call him back within the hour." (internal call note's record of what was said on the call) | 2026-11-16 02:05 UTC | Met: call-back made, confirmed in 01:32 email ("as discussed on the phone just now") |
| 2026-11-16 01:32 UTC (email) | Marcus Lee | "If you can tell me who you spoke to, I'll follow it up." | Not stated | Open: customer replied 03:05 "one of your engineers. I don't remember his name"; no follow-up recorded |
| 2026-11-16 03:40 UTC (email) | Marcus Lee | "I'm escalating this to our Field Systems Engineering team now." | Not stated ("now") | Met: escalated 03:50 UTC |
| 2026-11-16 03:40 UTC (email) | Marcus Lee | "I'll send you an update by 12:00 AWST tomorrow, Tuesday 17 November (04:00 UTC), or sooner if engineering has news." | 2026-11-17 04:00 UTC | Overdue: no update recorded; 4 days 14 h 35 min past due. Owned by Tier 2 per 5.3 |

No fix date, credit or compensation has been promised (Marcus Lee 03:40: "I can't give you a fix date"). The customer has stated a cost of about $40,000 a day and attributes fault to Tern (01:12); per 6.2 and 6.3 only the Account Manager (Rhys Kaplan, account record) or the Head of Customer Support may offer a credit, refund or compensation, in writing. Account record: "Open credits: None".

## Recommended next action
Test the suspected modem-firmware cause on one offline G4-C unit: read the cellular modem's firmware version and its network registration state on one of the three untouched Katherine units (or a Darwin unit), and in parallel bring up a G4-C on 4.7.2 / MX-31.4 in the lab on the same carrier SIM type and see whether it registers. Remote access has failed (SMS wake, 02:05 UTC), so the unit-side read needs someone on site or a unit returned; the method is not stated in the case.
- Confirms: the unit reports MX-31.4 and a failed or rejected network registration, and a lab G4-C on MX-31.4 also fails to register while one on the previous modem firmware registers with the same SIM.
- Rules out: the modem registers normally, or runs a different modem firmware, or the lab unit on MX-31.4 registers; then look at the gateway-to-TernCloud path instead.
- Racing: the resolution target is already breached (since 2026-11-19 01:05 UTC), and the promised update (due 2026-11-17 04:00 UTC) and the P2 daily updates (7.1) are overdue. Send Grant Tobias an update at or before the start of business on Mon 2026-11-23 (00:30 UTC), stating current findings and the next update time, without a fix date (6.2). Keep the customer's instruction not to factory-reset in place so locally stored readings are preserved.

Open questions:
- Has anything happened on the ticket since 2026-11-16 03:50 UTC that is not in this export (Tier 2 work, customer contact)?
- Are other customers' G4-C units on 4.7.2 / MX-31.4 also offline? Not stated in the case.
- Is a rollback of the G4-C modem firmware, or of 4.7.2, possible remotely when the modem cannot register? Not stated.
- Do the 14 offline units still hold the readings since 14 Nov 18:20 UTC, and will they upload on reconnect? Stated as general G4 behaviour, not checked on these units.
- Who, if anyone, told the customer last week that 4.7.2 was "fixed and safe to roll out"? No record found; follow-up promised (01:32).
- Has the Support Team Lead been told the P2 ticket has breached? Not required by 5.2 at escalation, but the status has changed since.
- Should the Account Manager (Rhys Kaplan) be told of the customer's stated $40,000-a-day impact and attribution of fault to Tern? Not stated.
