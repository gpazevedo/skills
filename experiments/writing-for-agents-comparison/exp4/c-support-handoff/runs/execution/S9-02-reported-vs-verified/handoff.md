# Escalation handoff: TRN-77102: 14 cellular (G4-C) gateways offline since 4.7.2 update

**Customer:** Coldwater Freight Pty Ltd (CWF-2210), Business · **Priority:** P2 · **Next deadline:** 2026-11-17 04:00 UTC (12:00 AWST), customer update promised, outstanding, 24h10m left (as of 2026-11-16 03:50 UTC). Resolution deadline: 2026-11-19 01:05 UTC, open.

## Problem as currently understood
14 of 61 gateways (all G4-C cellular: Darwin 11, Katherine 3) stopped reporting to TernCloud at about 18:20-18:24 UTC on Saturday 14 November, during the firmware rollout to 4.7.2. The 47 G4-E Ethernet gateways (Perth, Adelaide) are online and complete. The leading, unconfirmed explanation is the 4.7.2 cellular modem firmware change (MX-31.4, G4-C only). Whether stored readings on the 14 units are intact is unknown.

Evidence:
- [Verified] 61 gateways; 47 online and reporting normally, 14 offline (Marcus Lee, 01:32 UTC, read from TernCloud at 01:25 UTC)
- [Verified] The 14 offline units are Darwin (11) and Katherine (3); each last reported 18:20-18:24 UTC on 14 Nov, during the window that started 18:00 UTC (Marcus Lee, 01:32 UTC)
- [Verified] All 61 gateways were updated to 4.7.2; the 47 online units run 4.7.2 (Marcus Lee, 01:32 UTC)
- [Verified] Online units have no gaps in TernCloud readings (Marcus Lee, 01:32 UTC)
- [Verified] All 14 SIMs are Active in Tern Connect; last data sessions ended 18:21-18:24 UTC on 14 Nov; no attempts since (Marcus Lee internal note, 02:10 UTC)
- [Verified] All 14 offline units are G4-C and all 47 online are G4-E (Marcus Lee, 02:10 UTC; matches account record fleet table: Darwin and Katherine are G4-C, Cellular)
- [Verified] 4.7.2 release notes include "cellular modem firmware updated to MX-31.4 (G4-C only)" (Marcus Lee, 02:10 UTC)
- [Verified] Remote SMS wake sent to DRW-GW-01, DRW-GW-05, KTH-GW-02 at 02:05 UTC; no response by 02:10 UTC (Marcus Lee, 02:10 UTC)
- [Reported] Darwin units show solid green power and flashing amber NET light, unchanged after power-cycling (Grant Tobias, 03:05 UTC). Support's LED guide reading, flashing amber NET = modem not registered on the mobile network, is from Marcus Lee's 03:40 UTC email, not tested.
- [Reported] Darwin gateways were rebooted by the customer with no effect (Grant Tobias, call 01:05 UTC and 03:05 UTC); Katherine units untouched (Grant Tobias, 03:05 UTC)
- [Reported] "Every gateway" is affected and three days of temperature data are lost (Grant Tobias, 01:12 UTC). Contradicted by the Verified fleet status above; "three days" also exceeds the roughly 1.3 days between the last reports and the email.
- [Reported] Impact of about $40,000 a day in stock that cannot be certified, and Perth cannot dispatch Darwin loads without certificates (Grant Tobias, 01:12 and 03:05 UTC)
- [Inferred] The fault is specific to G4-C hardware, plausibly the modem firmware, not the SIM accounts (rests on: model split, Active SIMs, no session attempts since update, MX-31.4 release note)
- [Inferred] Stored readings may still be on the 14 units (rests on: Marcus Lee's statement that G4 units buffer locally; not verified for these units)

## Tried so far
| When (UTC) | Who | Action | Result |
| --- | --- | --- | --- |
| 14 Nov to 16 Nov | Customer (Reported) | Rebooted Darwin gateways; power-cycled all 11 again on 16 Nov | No change; solid green power, flashing amber NET |
| 2026-11-16 01:25 | Marcus Lee | Checked fleet status in TernCloud | 47 online, 14 offline, all Darwin/Katherine |
| 2026-11-16 02:05-02:10 | Marcus Lee | Checked SIM status in Tern Connect | All 14 Active; no sessions since 18:24 UTC on 14 Nov. SIM/account fault not supported |
| 2026-11-16 02:05 | Marcus Lee | Remote SMS wake to 3 units | No response by 02:10 |
| 2026-11-16 03:40 | Marcus Lee | Asked customer not to factory-reset units (would erase stored readings) | No result recorded |
| 2026-11-16 01:32 | Marcus Lee | Searched for a prior call/ticket last week | None found; last ticket TRN-75530 (closed 2 Oct) |

## Commitments to the customer
| Commitment (quoted) | Made by | When | Status |
| --- | --- | --- | --- |
| "I'd check the fleet and call him back within the hour" (call note) | Marcus Lee | 2026-11-16 01:05 UTC | Met: fleet checked at 01:25 and the 01:32 email follows a call-back "just now" (Inferred from the email wording; no call time logged) |
| "I'll send you an update by 12:00 AWST tomorrow, Tuesday 17 November (04:00 UTC), or sooner if engineering has news" | Marcus Lee | 2026-11-16 03:40 UTC | Outstanding, 24h10m left. Tier 2 now owns it (policy 5.3) |
| "If you can tell me who you spoke to, I'll follow it up" (conditional) | Marcus Lee | 2026-11-16 01:32 UTC | Conditional; customer has not named anyone |

No fix date, credit, refund or compensation has been promised; Marcus explicitly declined to give a fix date.

Claimed by the customer, not found in the thread: a Tern engineer told Grant Tobias "last week" that 4.7.2 "was fixed and safe to roll out" (01:12 and 03:05 UTC). Marcus found no record of a call or ticket; the engineer is unnamed. Grant states "this one is on Tern"; this is not a commitment and no credit has been offered.

## Service level
- Plan: Business (account record, Support plan). The customer states no different plan.
- Priority: P2, set by Marcus Lee at 01:05 UTC and kept at escalation (03:50 UTC). Customer asked for P1; that request is Reported and does not set the priority. Policy 2.1 (P1) requires "more than half of the customer's gateways" offline; 14 of 61 (23%) is under half (Verified). Policy 2.2 (P2) fits: "some of the customer's gateways are offline ... and there is no practical workaround" (no workaround recorded).
- Target (policy 3.1, Business P2): first response "4 business hours"; resolution "27 business hours".
- Clock start: policy 4.1 "when the ticket is created": 2026-11-16 01:05 UTC (09:05 AWST Monday), inside business hours (00:30-09:30 UTC). No "Pending customer" status in the thread, so no pause (policy 4.2).
- First response: met at 01:05 UTC, since policy 1.4 counts a ticket logged by an agent during the call.
- Resolution deadline: 27 business hours at 9 per day (00:30-09:30 UTC). Mon 01:05 to 09:30 = 8h25m; Tue 9h; Wed 9h (total 26h25m); the final 35m ends Thu 2026-11-19 01:05 UTC (09:05 AWST). Inferred; assumes no Western Australian public holiday on 16-19 Nov (none shown in the supplied material).
- Status as of 2026-11-16 03:50 UTC: within target. About 2h45m used, 24h15m of 27h remain; the "at risk" line (policy 4.4, under 25%, which is 6h45m remaining) is reached when 20h15m has been used: Wed 2026-11-18 03:20 UTC (11:20 AWST). Inferred.
- Update cadence (policy 7.1, P2): at least once each business day; the 04:00 UTC 17 Nov update covers that.
- Escalation: policy 5.1 met (cannot be resolved with documented procedures). The Support Team Lead notification (5.2) applies only to P1 or at-risk P2; this ticket is neither.

## Recommended next action
Tier 2 (Field Systems Engineering) should establish whether the MX-31.4 modem firmware in 4.7.2 is breaking network registration on G4-C units, for example by checking known issues for MX-31.4 and pulling modem or registration logs from one Darwin unit, and decide whether a remote recovery or on-site action is needed. Do this before the 04:00 UTC 17 Nov update so that update contains real findings, and well before the at-risk point (about 03:20 UTC 18 Nov). This tests the one explanation that is only Inferred and decides the fix path.

Follow-ups: (1) ask Katherine for LED status on one or two units, since only Darwin has reported; (2) keep the "do not factory-reset" instruction in force until stored readings are confirmed recoverable.

## Gaps and open questions
- Inputs: none missing (thread, account record, policy all supplied).
- Cause is unconfirmed; the MX-31.4 link is a hypothesis.
- Whether the 14 units hold buffered readings is unknown, so the customer's "three days of data lost" is unverified.
- Katherine LED status unknown; the SMS wake was tried on three units only and for five minutes.
- The "engineer said 4.7.2 was fixed" claim is unverified and the engineer unidentified; if 4.7.2 had a known G4-C issue, this matters. Internal check of prior advice/known issues for 4.7.2 is open.
- Customer states $40,000/day impact and blames Tern; any credit or compensation is for the Account Manager (Rhys Kaplan) or Head of Customer Support only (policy 6.3); agents must not promise it (6.2). No credit is open (account record).
- Customer says "every site" is affected; records show Perth and Adelaide online. The Perth dispatch problem is a downstream effect of Darwin data, Reported only.
- Deadline calculation assumes no WA public holiday 16-19 Nov.
