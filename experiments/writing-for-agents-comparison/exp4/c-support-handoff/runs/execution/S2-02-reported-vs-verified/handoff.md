# Escalation handoff: TRN-77102 | Coldwater Freight Pty Ltd | 14 cellular gateways offline after firmware 4.7.2

**Service level:** 2026-11-19 01:05 UTC (09:05 AWST Thu), Business P2 resolution target of 27 business hours | Within target (as of 2026-11-16 03:50 UTC). Separate commitment due sooner: customer update by 2026-11-17 04:00 UTC (12:00 AWST Tue).

## Problem as currently understood
14 of 61 gateways are offline: all 11 Darwin and 3 Katherine units, which are all G4-C (cellular). Verified: each last reported between 18:20 and 18:24 UTC on 14 Nov, during the firmware window, and all 61 were updated to 4.7.2. The 47 online G4-E (Ethernet) units at Perth and Adelaide report normally with no gaps. Verified: all 14 SIMs are Active on the carrier side and show no session attempts since the last session ended. The leading Suspected cause is the 4.7.2 cellular modem firmware change (MX-31.4, G4-C only). Whether the offline units hold stored readings is unknown.

| Statement | Label | Source (author, timestamp) |
| --- | --- | --- |
| 14 gateways offline (Darwin 11, Katherine 3); 47 of 61 online and reporting normally | Verified | Marcus Lee, TernCloud check as of 01:25 UTC, email 2026-11-16 01:32 |
| Each offline gateway last reported 18:20 to 18:24 UTC on 14 Nov, in the 18:00 UTC rollout window | Verified | Marcus Lee, 2026-11-16 01:32 |
| All 61 gateways updated to 4.7.2 in that window | Verified (per TernCloud) | Marcus Lee, 2026-11-16 01:32 |
| Online units' readings are complete, with no gaps | Verified | Marcus Lee, 2026-11-16 01:32 |
| All 14 offline units are G4-C; all 47 online units are G4-E (matches the account record fleet table) | Verified | Marcus Lee, internal note 2026-11-16 02:10; account record |
| All 14 SIMs Active; last data sessions ended 18:21 to 18:24 UTC on 14 Nov; no attempts since | Verified | Marcus Lee, Tern Connect console, internal note 2026-11-16 02:10 |
| SMS wake sent to DRW-GW-01, DRW-GW-05, KTH-GW-02 at 02:05 UTC drew no response by 02:10 | Verified | Marcus Lee, 2026-11-16 02:10 |
| Darwin units show solid green power light and flashing amber NET light, unchanged after power-cycling | Reported | Grant Tobias relaying the Darwin site lead, 2026-11-16 03:05 |
| Flashing amber NET on a G4-C means the modem is not registered on the mobile network | Reported (from the LED guide, not tested on these units) | Marcus Lee, 2026-11-16 03:40 |
| Cause is on the gateway side, not the SIM accounts | Suspected | Marcus Lee, 2026-11-16 03:40 |
| 4.7.2 cellular modem firmware update (MX-31.4) causes the G4-C outage | Suspected | Marcus Lee, internal note 2026-11-16 02:10 ("Possible link; not confirmed") |
| "Every one of our gateways went dark" and "every site is affected" | Reported, contradicted by Verified data above | Grant Tobias, 2026-11-16 01:12 and 03:05 |
| "Lost all our temperature data for the last three days" | Reported. The offline units went silent about 31 hours before the 01:12 UTC email, and G4 units store readings locally | Grant Tobias, 2026-11-16 01:12; Marcus Lee, 01:32 |
| Loss of about $40,000 a day in stock that cannot be certified; Perth cannot dispatch Darwin loads without certificates | Reported | Grant Tobias, 2026-11-16 01:12 and 03:05 |
| Katherine units not yet inspected or power-cycled | Reported | Grant Tobias, 2026-11-16 03:05 |

## What has been tried
| Action | By | When | Result | Label |
| --- | --- | --- | --- | --- |
| Rebooted all Darwin gateways (first time, before the call) | Customer team | Before 2026-11-16 01:05 UTC | No difference | Reported |
| Checked fleet status in TernCloud | Marcus Lee | 2026-11-16 01:25 UTC | 14 offline, 47 online, all on 4.7.2 | Verified |
| Checked Tern Connect console for the 14 SIMs | Marcus Lee | 2026-11-16 02:10 UTC | All Active; no session attempts since 14 Nov | Verified |
| Compared model against online/offline status; read 4.7.2 release notes | Marcus Lee | 2026-11-16 02:10 UTC | Offline group is exactly the G4-C units; release notes list the MX-31.4 modem firmware update for G4-C | Verified (the correlation); cause Suspected |
| Remote SMS wake to DRW-GW-01, DRW-GW-05, KTH-GW-02 | Marcus Lee | 2026-11-16 02:05 UTC | No response by 02:10; later result not recorded | Verified |
| Power-cycled all 11 Darwin units again; read the lights | Customer team (Darwin site lead) | 2026-11-16, "this morning", reported 03:05 UTC | Lights unchanged: solid green power, flashing amber NET | Reported |
| Asked Darwin for front-panel lights on 2 or 3 units | Marcus Lee | 2026-11-16 01:32 UTC | Answered at 03:05 (Darwin only) | Reported |
| Asked customer not to factory-reset units, to protect stored readings | Marcus Lee | 2026-11-16 03:40 UTC | No reply yet | Not applicable (instruction, not a test) |

## Commitments to the customer
| Commitment (quoted) | Made by (name, role) | When | Due | Status |
| --- | --- | --- | --- | --- |
| "I'd check the fleet and call him back within the hour" (call note wording: "I told him I'd check the fleet and call him back within the hour") | Marcus Lee, Support Agent Tier 1 | 2026-11-16 01:05 UTC | 02:05 UTC | Kept (email "after call-back" sent 01:32 UTC) |
| "If you can tell me who you spoke to, I'll follow it up." | Marcus Lee, Support Agent Tier 1 | 2026-11-16 01:32 UTC | No date given | Outstanding (customer has not named the engineer) |
| "I'm escalating this to our Field Systems Engineering team now." | Marcus Lee, Support Agent Tier 1 | 2026-11-16 03:40 UTC | "now" (03:40 UTC) | Kept (escalated 03:50 UTC) |
| "I'll send you an update by 12:00 AWST tomorrow, Tuesday 17 November (04:00 UTC), or sooner if engineering has news." | Marcus Lee, Support Agent Tier 1 | 2026-11-16 03:40 UTC | 2026-11-17 04:00 UTC | Outstanding. Tier 2 owns it from escalation (policy 5.3). |

Claimed by the customer but not found in the thread: an unnamed Tern engineer told Grant Tobias "last week" that firmware 4.7.2 "was fixed and safe to roll out". Marcus Lee found no record of a call or ticket from that week (last ticket TRN-75530, closed 2 October 2026). No service credit, refund, compensation or fix date has been offered or promised by Tern in the thread.

## Service level
- Tier: Business support plan (account record, CWF-2210)
- Priority: P2, recorded at creation and unchanged at escalation. The customer's request for P1 was recorded and not applied.
- First response (4 business hours, policy 3.1; first contact by an agent counts, 1.4): clock started 2026-11-16 01:05 UTC (policy 4.1, inside business hours, 09:05 AWST Monday). Met at 01:05 UTC, when the agent logged the ticket during the call.
- Resolution (27 business hours, policy 3.1, 3.3; resolved only when every fault is resolved, 1.5): clock started 2026-11-16 01:05 UTC. Business hours are 00:30 to 09:30 UTC, Monday to Friday (1.1, 1.2). No pause: status has never been "Pending customer" (4.2). Elapsed 2h 45m, remaining 24h 15m. Deadline 2026-11-19 01:05 UTC (09:05 AWST Thursday), counting 8h 25m left on Mon, 9h Tue, 9h Wed, 35m Thu. Status: within target (4.4). "At risk" begins when under 6h 45m (25% of 27) remain.
- Customer update cadence for P2 (policy 7.1): at least once each business day. The next update is committed for 2026-11-17 04:00 UTC.
- P1 targets (2 hours / 24 hours, 24x7) do not apply: priority is P2 (policy 2.5, 3.1).
- Status as of: 2026-11-16 03:50 UTC (the as-of time stated in the ticket export)

## Recommended next action
A Tier 2 Field Systems engineer should test the leading Suspected cause: check whether 4.7.2's MX-31.4 modem firmware is known to prevent G4-C network registration (release notes, engineering defects, carrier or band issues). They should then pick a recovery path that preserves stored readings, based on Verified evidence that the offline set equals the G4-C set, SIMs are Active and units show a flashing amber NET light. If the change is a known issue, apply its remediation to the 14 units. If it is not, collect device-side logs from a Katherine unit (not yet power-cycled) before further resets. Send the customer update by 2026-11-17 04:00 UTC.

## Open questions
- Priority conflict: the customer asks for P1 and says all gateways are offline. Verified data shows 14 of 61 offline (23%), and policy 2.1 requires more than half (at least 31). P2 stays under 2.2 and 2.5. Re-check if any Ethernet units drop off, since that would change the priority.
- Claimed data loss ("three days"): unconfirmed. Stored readings on the 14 offline units cannot be checked until they reconnect or are read locally. The offline units went silent about 31 hours before the first email.
- Claim that an unnamed engineer said 4.7.2 was "fixed and safe": no record found. Ask Grant Tobias for the engineer's name, date, and channel, and search call and ticket records. This is the customer's claim only. It is not a Tern commitment.
- Financial and liability claims (around $40,000 a day; "this one is on Tern"): not confirmed. Under policy 6.2 and 6.3, Tier 2 must not promise a credit, refund or compensation. Only Rhys Kaplan (Account Manager) or the Head of Customer Support can offer one, recorded in writing. Refer the claim to Rhys Kaplan. No contract SLA was quoted and none is in the account record beyond the Business plan.
- Who initiated the 4.7.2 rollout: the account record says rollouts are customer-scheduled (default window Saturdays from 18:00 UTC), Marcus wrote "your scheduled firmware window", and Grant wrote "your firmware push". Confirm in TernCloud who started it. This matters for how the cause is described to the customer.
- Katherine units: lights not yet checked (customer has not touched them). Ask Grant Tobias or Lina Petrakis (IT Manager, technical contact) for the NET and power lights at Katherine.
- SMS wake result: only the 02:10 UTC check is recorded. Confirm whether any of the three units responded later.
- WA public holidays for 16 to 19 Nov are not stated in the supplied policy or thread. The deadline of 2026-11-19 01:05 UTC assumes none fall in that period.
- Escalation notification: policy 5.2 requires notifying the Support Team Lead only for P1 or at-risk P2. This is neither at the moment, so no notification is required. Confirm if priority or risk status changes.
- Missing inputs: none. Thread, account record and policy were all supplied.
