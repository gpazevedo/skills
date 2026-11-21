# Escalation handoff: TRN-77102 14 cellular (G4-C) gateways offline since 4.7.2 firmware rollout

**Customer:** Coldwater Freight Pty Ltd, account CWF-2210, Business plan (account record: "Support plan: Business")   **Severity/priority:** P2, recorded on the ticket at creation (thread, 2026-11-16 01:05 UTC event; policy 2.5: "a priority applies only once recorded on the ticket"). Customer's P1 request recorded, not applied (thread, 03:50 UTC).
**Most urgent deadline:** Customer update promised by 2026-11-17 04:00 UTC (12:00 AWST), Marcus Lee, 03:40 UTC message. Nearest service-level clock: P2 resolution target 2026-11-19 01:05 UTC.

As-of time used for all judgements: 2026-11-16 03:50 UTC (thread header).

## Problem as currently understood
Of 61 gateways, 14 (all G4-C cellular, at Darwin and Katherine) have sent nothing since their last session on 14 Nov 18:21-18:24 UTC, during the 4.7.2 firmware rollout. The 47 G4-E Ethernet gateways are online and reporting. The 4.7.2 notes mention a cellular modem firmware update (MX-31.4, G4-C only), a possible but unconfirmed link. Whether stored readings on the 14 units are intact is unknown.

| Fact | Status | How established / cite |
|---|---|---|
| Fleet is 61 gateways: Darwin 11 G4-C, Katherine 3 G4-C, Kewdale 30 G4-E, Wingfield 17 G4-E | Verified | Account record, gateway fleet table |
| 14 gateways offline (Darwin 11, Katherine 3); 47 online and reporting | Verified | Marcus Lee, 01:32 UTC, read in TernCloud as of 01:25 UTC. Not re-checked after 01:25 in the thread |
| The 14 offline units last reported 18:20-18:24 UTC on Sat 14 Nov, during the window (rollout started 18:00 UTC) | Verified | Marcus Lee, 01:32 UTC (TernCloud); 02:10 UTC note (Tern Connect sessions ended 18:21-18:24) |
| All 61 gateways were updated to 4.7.2; the 47 online run 4.7.2 | Verified (TernCloud); firmware on the 14 offline units not separately stated | Marcus Lee, 01:32 UTC |
| 47 online gateways have complete readings, no gaps | Verified | Marcus Lee, 01:32 UTC (TernCloud) |
| All 14 offline units are G4-C; all 47 online are G4-E | Verified | Marcus Lee 02:10 UTC note; matches account record fleet table |
| All 14 SIMs are Active; no session attempts since 18:24 UTC on 14 Nov | Verified | Marcus Lee, 02:10 UTC note (Tern Connect console) |
| Remote SMS wake sent to DRW-GW-01, DRW-GW-05, KTH-GW-02 at 02:05 UTC; no response by 02:10 | Verified (attempt and result at 02:10) | Marcus Lee, 02:10 UTC note. Not re-checked after 02:10 |
| 4.7.2 release notes include "cellular modem firmware updated to MX-31.4 (G4-C only)" | Verified (that the notes say it) | Marcus Lee, 02:10 UTC note |
| The modem firmware update caused the outage | Hypothesis | Marcus Lee, 02:10 UTC note: "Possible link; not confirmed." |
| Flashing amber NET light means a G4-C modem is not registered on the mobile network | Verified (from the LED guide, as quoted) | Marcus Lee, 03:40 UTC, citing the LED guide |
| Fault is on the gateway side, not the SIM accounts | Hypothesis | Marcus Lee, 03:40 UTC: "points to", "I can't confirm the cause yet" |
| Darwin units show solid green power and flashing amber NET | Reported | Grant Tobias, 03:05 UTC (relaying Darwin site lead); no support check |
| Darwin units rebooted at the weekend, and power-cycled again this morning, no change | Reported | Grant Tobias, 01:05 call note (Marcus Lee records it) and 03:05 UTC email |
| Katherine units not touched; their lights unknown | Reported | Grant Tobias, 03:05 UTC |
| Customer has lost all temperature data for the last three days | Reported (contested) | Grant Tobias, 01:12 UTC. Contradicted in part, see disagreements |
| Impact of about $40,000 a day in stock that cannot be certified; Perth cannot dispatch Darwin loads without certificates | Reported | Grant Tobias, 01:12 and 03:05 UTC |
| Customer was told last week by a Tern engineer that 4.7.2 was "fixed and safe to roll out" | Reported | Grant Tobias, 01:12 and 03:05 UTC (engineer unnamed). Marcus found no record, 01:32 UTC |
| Gateways store readings locally when they cannot reach TernCloud and upload on reconnect | Verified (as stated by agent); not tested on these units | Marcus Lee, 01:32 UTC |
| Rollout was in the customer's scheduled window (Saturdays from 18:00 UTC) | Verified | Account record, firmware management; thread 01:32 UTC |

**Open disagreements:**
1. Scope: Grant says "ALL" and "every one of our gateways" are dark (01:12) and "every site is affected" (03:05). TernCloud shows 14 of 61 offline, 47 online with complete data (Marcus Lee, 01:32).
2. Data loss: Grant says all temperature data lost for three days (01:12). Support sees complete data for 47 units and only 14 units silent since 14 Nov ~18:20 UTC, about a day and a half at the time of the call; whether stored data survives on the 14 is unknown (01:32).
3. Prior assurance: Grant says an engineer said last week 4.7.2 was fixed and safe; support found no call or ticket (last ticket TRN-75530, closed 2 Oct). Unresolved, engineer not identified.
4. Priority: customer wants P1; recorded P2 (see Service-level status).

## What has been tried
| When | Who | Action | Result | Cite |
|---|---|---|---|---|
| 14 Nov weekend (time not given) | Customer (Darwin team) | Rebooted all Darwin gateways | No difference (customer's report) | Call note 01:05 UTC |
| 2026-11-16 ~01:25 | Marcus Lee | Checked fleet status in TernCloud | 14 offline, 47 online; offline units last reported 18:20-18:24 UTC 14 Nov | Email 01:32 UTC |
| 2026-11-16 by 02:10 | Marcus Lee | Checked Tern Connect console for the 14 SIMs | All Active; no sessions since 18:21-18:24 UTC 14 Nov | Internal note 02:10 UTC |
| 2026-11-16 by 02:10 | Marcus Lee | Compared models and release notes | All offline units G4-C; notes list MX-31.4 modem update; link unconfirmed | Internal note 02:10 UTC |
| 2026-11-16 02:05 | Marcus Lee | Remote SMS wake to DRW-GW-01, DRW-GW-05, KTH-GW-02 | No response by 02:10; later result not recorded | Internal note 02:10 UTC |
| 2026-11-16 01:32 | Marcus Lee | Asked Darwin to report front-panel lights | Answered at 03:05 (customer report) | Email 01:32; Grant 03:05 UTC |
| 2026-11-16 before 03:05 | Customer (Darwin) | Power-cycled all 11 Darwin units again | No change; lights same | Grant Tobias 03:05 UTC |
| 2026-11-16 03:40 | Marcus Lee | Checked LED guide for amber NET meaning; told customer not to factory-reset | Modem not registered on network; no reset confirmed or refused by customer: not recorded | Email 03:40 UTC |
| 2026-11-16 03:50 | Marcus Lee | Escalated to Tier 2 | Status Escalated | Event 03:50 UTC |

## Commitments to the customer
| Commitment (verbatim) | Made by (role) | When / cite | Deadline | Kept / Open / Missed |
|---|---|---|---|---|
| "I'd check the fleet and call him back within the hour" (call note wording of what Marcus told Grant: "I told him I'd check the fleet and call him back within the hour") | Marcus Lee (Tier 1 agent) | 2026-11-16 01:05 UTC call note (said during call; internal note paraphrase, not the customer-facing words) | 02:05 UTC | Kept: call-back and email at 01:32 UTC ("as discussed on the phone just now") |
| "If you can tell me who you spoke to, I'll follow it up." | Marcus Lee (Tier 1 agent) | 01:32 UTC email | None set | Open, conditional on customer naming the engineer; customer has not (03:05 UTC) |
| "I'm escalating this to our Field Systems Engineering team now." | Marcus Lee (Tier 1 agent) | 03:40 UTC email | Now | Kept: escalated at 03:50 UTC |
| "I'll send you an update by 12:00 AWST tomorrow, Tuesday 17 November (04:00 UTC), or sooner if engineering has news." | Marcus Lee (Tier 1 agent) | 03:40 UTC email | 2026-11-17 04:00 UTC | Open. Within what policy 6.1 allows ("Support agents may commit to the time of the next update"). Tier 2 now owns it (policy 5.3: "Tier 2 owns the ticket, including customer updates and commitments already made") |

No commitment exceeds policy. Marcus declined a fix date ("I can't give you a fix date", 03:40 UTC), consistent with 6.2. No credit, refund or compensation has been offered. The customer's "this one is on Tern" and $40,000/day statements are claims, not commitments; any credit may only come from the Account Manager (Rhys Kaplan, account record) or the Head of Customer Support (policy 6.3).

## Service-level status
Plan Business (account record); priority P2 (2.2: some gateways offline, no practical workaround; 14 of 61 is not "more than half", so not 2.1). Business P2 targets (policy 3.1): first response "4 business hours", resolution "27 business hours". Business hours "08:30 to 17:30 Australia/Perth time ... Monday to Friday" (1.1) = 00:30 to 09:30 UTC (1.2), 9 hours a day. No "Pending customer" status in the thread, so no pause (4.2). Monday 16 Nov 2026 is a weekday; no public holiday is recorded in the sources (not checked beyond the sources).

| Clock | Policy clause (quoted) | Started | Deadline (with arithmetic) | Status |
|---|---|---|---|---|
| First response | 1.4 "A ticket logged by an agent during a call with the customer counts as a first response when logged"; 3.1 Business P2 "4 business hours" | 01:05 UTC Mon 16 Nov (created, inside business hours, 4.1) | 01:05 + 4h = 05:05 UTC Mon 16 Nov | Met at 01:05 UTC (logged during call); email 01:32 UTC also |
| Resolution (P2) | 3.1 "27 business hours" | 01:05 UTC Mon 16 Nov | Mon 01:05-09:30 = 8h25m; Tue 9h (17h25m); Wed 9h (26h25m); remaining 0h35m from Thu 00:30 UTC = Thu 19 Nov 01:05 UTC (09:05 AWST) | Within target. Elapsed 2h45m (01:05-03:50); remaining 24h15m of 27h; 4.4 at risk threshold is under 25% = under 6h45m remaining, not reached |
| Customer update interval | 7.1 "P2: at least once each business day" | n/a | Each business day; update sent Mon 01:32 UTC; next promised 17 Nov 04:00 UTC | On track |
| Conditional: if upgraded to P1 | 3.1 Business P1 resolution "24 hours, 24x7"; 4.3 counted from ticket creation; 7.1 "P1: an update at least every 4 hours, 24x7" | 01:05 UTC Mon 16 Nov | 01:05 + 24h = 01:05 UTC Tue 17 Nov (09:05 AWST); first response 2 hours = 03:05 UTC Mon 16 Nov | Not applicable now (P2 recorded). If P1 applied: 21h15m of resolution time left at 03:50 UTC; updates due at least every 4 hours, last customer contact 03:40 UTC, so next by 07:40 UTC |

P1 trigger (2.1) needs more than half of 61 gateways offline (31 or more); 14 is not. Escalation basis: 5.1 "cannot be resolved with documented procedures"; ticket is not at risk, so the Support Team Lead notification in 5.2 ("an at-risk P2 ticket") is not triggered by policy. Priority should be re-assessed if more gateways go offline or Katherine/other units change.

## Recommended next action
Tier 2: pull device-side diagnostics for the G4-C units (start with DRW-GW-01, DRW-GW-05 and KTH-GW-02, the units already sent an SMS wake) and compare the modem firmware version and registration logs against 4.7.2 with MX-31.4. Evidence: 14 of 14 G4-C offline, 47 of 47 G4-E online, SIMs Active, last session in the update window, amber NET light (modem not registered), and the release note naming a G4-C-only modem update. The result would settle whether the modem firmware update is the cause (Hypothesis today) and whether a rollback or modem fix is available. As part of this, confirm the Reported items it depends on: get Katherine's LED state and have Katherine and Darwin confirm no factory reset, and check whether stored readings remain on the units. Re-check TernCloud fleet counts, since the only count is from 01:25 UTC. Deadline to beat: send the customer an update by 2026-11-17 04:00 UTC (12:00 AWST); resolution target 2026-11-19 01:05 UTC.

## Gaps
- Fleet counts and wake-SMS result are from 01:25 and 02:10 UTC; no later check recorded. Close by re-checking TernCloud and Tern Connect.
- Result of the 02:05 SMS wake after 02:10 UTC: not recorded.
- Whether firmware on the 14 offline units is 4.7.2 with MX-31.4: not stated per unit.
- Time of the weekend Darwin reboot: not recorded.
- Katherine front-panel lights: not reported.
- Whether data survives on the 14 units: unknown.
- Engineer the customer says gave assurance last week: unidentified, no record found.
- Customer's response to the "don't factory-reset" request: not recorded.
- WA public holidays 16-19 Nov 2026: not given in the sources; the deadline assumes none.
- Whether the customer expects a credit: no credit offered; route any such request to Rhys Kaplan (policy 6.3).
