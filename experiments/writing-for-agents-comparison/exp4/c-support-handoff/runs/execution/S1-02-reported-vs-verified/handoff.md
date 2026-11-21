# Handoff: TRN-77102, Coldwater Freight (CWF-2210)

As-of: 2026-11-16 03:50 UTC (11:50 AWST, Monday). All three inputs (thread, account record, policy v2026.2) were provided.

## 1. Summary
14 of 61 gateways (all G4-C cellular units at Darwin and Katherine) went offline during the 4.7.2 firmware rollout on Saturday 14 November, and nothing so far has restored them. The ticket is P2, within its service-level target (resolution due 2026-11-19 01:05 UTC), but the customer reports about $40,000 a day of impact and a customer update is owed by 04:00 UTC tomorrow.

## 2. Problem as understood

Verified
- Fleet is 61 gateways: Perth 30 and Adelaide 17 (G4-E, Ethernet), Darwin 11 and Katherine 3 (G4-C, cellular). Source: account record.
- At 01:25 UTC, 47 gateways were online and reporting, and 14 were offline (the 11 Darwin and 3 Katherine units). Source: TernCloud view, Marcus Lee email 01:32. This was not re-checked after 01:25.
- Each offline unit last reported between 18:20 and 18:24 UTC on 14 Nov. The rollout began at 18:00 UTC. All 61 units were updated to 4.7.2. Source: Marcus Lee email 01:32.
- Readings from the 47 online units are complete, with no gaps. Source: Marcus Lee email 01:32.
- All 14 SIMs show Active in the Tern Connect console, and their last data sessions ended 18:21 to 18:24 UTC on 14 Nov, with no attempts since. Source: internal note 02:10.
- All 14 offline units are G4-C and all 47 online units are G4-E. The 4.7.2 release notes include "cellular modem firmware updated to MX-31.4 (G4-C only)". Source: internal note 02:10 (release notes as quoted by the agent).
- SMS wake sent at 02:05 to DRW-GW-01, DRW-GW-05 and KTH-GW-02 got no response by 02:10. Source: internal note 02:10.
- Priority P2 is consistent with policy 2.1 and 2.2: 14 of 61 is fewer than half, and the thread gives no practical workaround. Source: policy and account record.

Reported (no check shown)
- "Every" or "all" gateways are offline, and "every site is affected" (Grant, 01:12 and 03:05). This conflicts with the Verified fleet view above. Perth and Adelaide are online.
- Temperature data has been lost "for the last three days" (Grant, 01:12). The outage began Saturday 18:20 UTC, about 1.3 days before the ticket. Whether any data is actually lost is unknown, because G4 units store readings locally and upload on reconnect (Marcus, 01:32).
- A Tern engineer told Grant "last week" that 4.7.2 was fixed and safe. Marcus found no record of a call or ticket (the last was TRN-75530, closed 2 Oct). Grant cannot name the engineer. Unverified.
- Cost is "around $40,000 a day" in stock that can't be certified. This is the customer's figure only.
- Perth can't dispatch the Darwin loads without the certificates (Grant, 03:05). Not checked.
- Darwin site lead reports a solid green power light and a flashing amber NET light on every Darwin unit, unchanged after power-cycling (Grant, 03:05, relayed second-hand). Marcus cites the LED guide that flashing amber NET on a G4-C means the modem is not registered on the mobile network. The LED guide is not in the provided material.
- Darwin units were rebooted before the call and again this morning (Grant). Katherine units have not been touched or checked.
- Cause: the MX-31.4 modem firmware is a possible link, "not confirmed" (internal note 02:10). A gateway-side fault is inferred, not established.

## 3. Tried so far

| Action | By | Result |
| --- | --- | --- |
| Reboot or power-cycle all 11 Darwin units (before 01:05 call, and again the morning of 16 Nov) | Customer (Darwin site) | Failed. No change; lights are the same. Evidence: Grant, 01:05 call note and 03:05 email (Reported) |
| Check fleet status in TernCloud (01:25) | Marcus Lee | Worked as a diagnostic. 14 offline, all G4-C. Evidence: email 01:32 |
| Check SIM status and sessions in Tern Connect | Marcus Lee | Worked as a diagnostic. SIMs Active, no sessions since 18:24 UTC. Evidence: internal note 02:10 |
| Compare model against firmware and release notes | Marcus Lee | Inconclusive. Model separates the groups, link to MX-31.4 unconfirmed. Evidence: internal note 02:10 |
| Remote SMS wake to DRW-GW-01, DRW-GW-05, KTH-GW-02 at 02:05 | Marcus Lee | Failed. No response by 02:10. Evidence: internal note 02:10 |
| Ask for front-panel lights on 2 or 3 Darwin units | Marcus Lee, answered by customer | Worked. Lights reported at 03:05. Evidence: Grant's email |
| Advise not to factory-reset | Marcus Lee | Precaution, no result. Preserves locally stored readings. Evidence: email 03:40 |
| Escalate to Tier 2 | Marcus Lee | Done 03:50 |

## 4. Commitments to the customer

| Quote | Who | When | Status |
| --- | --- | --- | --- |
| "I'd check the fleet and call him back within the hour" (call note, paraphrase of what he told Grant) | Marcus Lee | 01:05 UTC 16 Nov | Met. Call-back and email at 01:32 UTC |
| "If you can tell me who you spoke to, I'll follow it up." | Marcus Lee | 01:32 UTC 16 Nov | Conditional on Grant naming the engineer, who has not. Open. Ownership after escalation is unclear |
| "I'll send you an update by 12:00 AWST tomorrow, Tuesday 17 November (04:00 UTC), or sooner if engineering has news." | Marcus Lee | 03:40 UTC 16 Nov | Open. Due 2026-11-17 04:00 UTC. Under policy 5.3 Tier 2 owns this commitment from escalation, so the receiving engineer owns it |
| "I can't give you a fix date." | Marcus Lee | 03:40 UTC 16 Nov | Not a promise. It is a refusal, consistent with policy 6.2 |

No fix date, credit, refund or compensation has been promised. Grant has asserted "this one is on Tern" and cites cost. Under 6.3 only the Account Manager (Rhys Kaplan) or the Head of Customer Support may offer credits, and none is recorded on the account ("Open credits: None").

## 5. Service level
Status: **on track (within target)**.

- Plan: Business (account record). Priority: P2 as recorded on the ticket. The customer's P1 request is recorded but not applied; policy 2.5: "a priority applies only once recorded on the ticket".
- First response: target 4 business hours (policy 3.1). Policy 1.4: "A ticket logged by an agent during a call with the customer counts as a first response when logged." Met at 01:05 UTC.
- Resolution target: 27 business hours (policy 3.1).
- Clock start: ticket creation, 2026-11-16 01:05 UTC (policy 4.1). That is 09:05 AWST on Monday, inside business hours (00:30 to 09:30 UTC, policy 1.1 and 1.2), so counting starts at creation.
- Pauses: none. Status has never been "Pending customer" (policy 4.2).
- Arithmetic, 9 business hours per day (00:30 to 09:30 UTC):
  - Mon 16 Nov: 01:05 to 09:30 = 8h25m. Remaining 27h00 - 8h25 = 18h35.
  - Tue 17 Nov: 9h00. Remaining 9h35.
  - Wed 18 Nov: 9h00. Remaining 0h35.
  - Thu 19 Nov: 00:30 + 0h35 = **01:05 UTC (09:05 AWST) Thursday 19 November 2026**.
- Elapsed at 03:50 UTC: 01:05 to 03:50 = 2h45m. Remaining 24h15m of 27h (90%). At-risk threshold is under 25%, i.e. under 6h45m remaining (policy 4.4), so the ticket is not at risk.
- Not stated in provided material: any WA public holiday on 17 to 19 Nov. I assumed none. A holiday would push the deadline later.
- Resolution requires every fault on the ticket to be resolved (policy 1.5).
- Update cadence: P2 means at least once each business day (policy 7.1). Marcus's 04:00 UTC Tuesday update covers Tuesday.
- Escalation: policy 5.1 allows it because documented procedures have not resolved it. The Support Team Lead notification (5.2) applies only to P1 or at-risk P2 escalations, so it is not required now.
- Priority would become P1 if more than half of the gateways (31 or more of 61) were offline (policy 2.1). Policy 4.3 would then recount the 24-hour target from creation. Katherine units are untouched and not confirmed as still offline beyond the 01:25 view.

## 6. Recommended next action
Tier 2 should investigate the G4-C modem as the cause. Specifically, compare the modem firmware on the offline G4-C units against the online state and the 4.7.2 MX-31.4 modem update, and get diagnostics from one unit (for example DRW-GW-01 or KTH-GW-02) on why the modem is not registering on the network (flashing amber NET, SIMs Active, no sessions since 18:24 UTC).

Why: the evidence separates the groups cleanly by model (14 of 14 G4-C offline, 47 of 47 G4-E online), the only G4-C-specific change in the release notes is MX-31.4, SIMs are active carrier-side, and reboots and the SMS wake did not help.

Before the deadlines:
- Send the customer update by 2026-11-17 04:00 UTC even if there is no news (Tier 2 owns it now).
- Keep the instruction not to factory-reset, to preserve stored readings.
- Re-check TernCloud fleet status so the 14-offline figure is current. Confirm Katherine's state.
- Hold any further G4-C 4.7.2 rollouts, if any are scheduled.
- Resolution due 2026-11-19 01:05 UTC.

Questions for the customer (they do not block the diagnostic work):
- What do the lights show at Katherine?
- Who was the engineer on the call "last week" and which date?
- When did Darwin last see devices reporting?

## 7. Gaps
- Marcus's fleet view is as of 01:25 UTC. There is no later check, and the 03:50 state is unknown.
- No LED guide, release notes or Tern Connect output is in the provided material. They are quoted second-hand.
- Data loss on the 14 offline units is unknown, because stored readings are on the devices.
- The customer's claim that "all" gateways are down contradicts the Verified 14 of 61, and "three days" does not fit the timeline.
- The "4.7.2 was fixed" prior call is unverified, with no record. If a prior defect or known-issue note on 4.7.x exists, that would matter, and Tier 2 should check.
- Which Tern person owns follow-up of the prior-call enquiry after escalation is unclear.
- Public holidays 17 to 19 Nov are not stated in the provided material.
- $40,000 per day and the certificate and dispatch impact are the customer's figures and unverified. They are relevant to Account Manager Rhys Kaplan if goodwill is discussed, but support cannot promise a credit (policy 6.2 and 6.3).
- Lights at Katherine are unknown.
