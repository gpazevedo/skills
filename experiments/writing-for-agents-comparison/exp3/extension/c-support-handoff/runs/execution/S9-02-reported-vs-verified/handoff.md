# Escalation handoff: TRN-77102, Coldwater Freight Pty Ltd (CWF-2210)

**In one line:** 14 of 61 gateways are offline: all 14 cellular G4-C units at Darwin (11) and Katherine (3). They dropped during the firmware 4.7.2 rollout on Sat 14 Nov. A customer update is promised by 2026-11-17 04:00 UTC (12:00 AWST), and the P2 resolution deadline is 2026-11-19 01:05 UTC (09:05 AWST).

## Problem as currently understood
- [verified] Fleet is 61 gateways. 47 are online and reporting normally. 14 are offline: 11 at Darwin and 3 at Katherine. (evidence: TernCloud fleet status checked by Marcus Lee, Tier 1, as of 2026-11-16 01:25 UTC, email 01:32 UTC. Fleet size and sites match the account record.)
- [verified] Each offline gateway last reported between 18:20 and 18:24 UTC on Sat 14 Nov, inside the customer's firmware window, which started at 18:00 UTC. (evidence: TernCloud, Marcus Lee, email 01:32 UTC 16 Nov. The account record gives the default window as "Saturdays from 18:00 UTC".)
- [verified] All 61 gateways were updated to firmware 4.7.2 in that window. The 47 online units all run 4.7.2. (evidence: TernCloud, Marcus Lee, email 01:32 UTC 16 Nov)
- [verified] All 14 offline units are G4-C (cellular). All 47 online units are G4-E (Ethernet). (evidence: model check by Marcus Lee, internal note 02:10 UTC 16 Nov. This matches the account record: DRW 11 G4-C, KTH 3 G4-C, PER 30 G4-E, ADL 17 G4-E.)
- [verified] The 4.7.2 release notes include "cellular modem firmware updated to MX-31.4 (G4-C only)". (evidence: Marcus Lee, internal note 02:10 UTC 16 Nov)
- [verified] All 14 SIMs show status Active. Their last data sessions ended between 18:21 and 18:24 UTC on 14 Nov, with no session attempts since. (evidence: Tern Connect console, Marcus Lee, internal note 02:10 UTC 16 Nov)
- [verified] Remote SMS wakes sent to DRW-GW-01, DRW-GW-05 and KTH-GW-02 at 02:05 UTC got no response from any unit by 02:10 UTC. (evidence: Marcus Lee, internal note 02:10 UTC 16 Nov)
- [verified] TernCloud readings from the 47 online units are complete with no gaps. TernCloud has no readings from the 14 offline units after their last report. (evidence: TernCloud, Marcus Lee, email 01:32 UTC 16 Nov)
- [verified] Support found no record of a call or ticket with Coldwater in the week before. The last ticket on the account is TRN-75530 (P3, bracket replacement), closed 2 Oct 2026. (evidence: search by Marcus Lee, email 01:32 UTC 16 Nov. The account record agrees.)
- [reported] Every Darwin unit shows a solid green power light and a flashing amber NET light. Darwin power-cycled all 11 units again on the morning of 16 Nov and the lights came back the same. Nobody at Katherine has touched their units. (source: Grant Tobias, quoting the Darwin site lead, email 03:05 UTC 16 Nov)
- [reported] Before the ticket was opened, the customer's team rebooted all the Darwin gateways, and it made no difference. (source: Grant Tobias on the call, as recorded in Marcus Lee's call note, 01:05 UTC 16 Nov)
- [reported] A Tern engineer told him by phone the week before that 4.7.2 "was fixed and safe to roll out". He cannot name the engineer. (source: Grant Tobias, emails 01:12 and 03:05 UTC 16 Nov)
- [reported] Temperature data for "the last three days" is lost. (source: Grant Tobias, email 01:12 UTC 16 Nov)
- [reported] The outage costs "around $40,000 a day in stock we can't certify for delivery". Perth cannot dispatch the Darwin loads without the certificates. (source: Grant Tobias, emails 01:12 and 03:05 UTC 16 Nov)
- [suspected] The MX-31.4 modem firmware in 4.7.2 left the G4-C modems unable to register on the mobile network. (held by: Marcus Lee, internal note 02:10 UTC, "Possible link; not confirmed". Basis: only G4-C units are down. They dropped minutes into the 4.7.2 rollout. The release note changes the G4-C modem firmware. The SIMs are active but have made no session attempts. Per Marcus's 03:40 UTC email, the LED guide reads a flashing amber NET light on a G4-C as "the cellular modem isn't registered on the mobile network".)
- [suspected] The fault is on the gateway side, not with the SIM accounts. (held by: Marcus Lee, email 03:40 UTC 16 Nov. Basis: the amber NET light, with the SIMs active on the carrier side.)
- [suspected] Readings from the offline period may still be held on the gateways. (held by: Marcus Lee, email 01:32 UTC 16 Nov. Basis: G4 gateways store readings locally when they can't reach TernCloud and upload them on reconnect. Nobody has checked this on these units.)
- Conflicts:
  - Scope: the customer says "Every one of our gateways went dark" and "every site is affected". TernCloud shows 14 of 61 offline, all at Darwin and Katherine. Perth and Adelaide gateways are online. The customer's "every site" refers to the business impact on Perth dispatch, not to Perth gateways being offline.
  - Priority: the customer asked for P1. The ticket is P2. Policy 2.1 sets P1 at "more than half of the customer's gateways are offline", and 14 of 61 (23%) is below that. Per 2.5, "a priority applies only once recorded on the ticket".
  - Data loss: the customer says the data is lost. TernCloud has complete data for the 47 online units. For the 14 offline units, whether data is lost is unknown (see the suspected item above).
  - Prior advice: the customer says a Tern engineer cleared 4.7.2 by phone. Support found no record of that call.
  - Duration: the customer says "the last three days". At his 01:12 UTC email on 16 Nov, about 31 hours had passed since the 18:20 UTC drop-off on 14 Nov.

## Tried so far
| What was tried | Who, when | Result |
|---|---|---|
| Rebooted all Darwin gateways (customer's own action, before the ticket; reported) | Customer's team, before 16 Nov 01:05 UTC | "made no difference" (reported) |
| Checked fleet status in TernCloud | Marcus Lee (Tier 1), as of 16 Nov 01:25 UTC | 47 online, 14 offline (DRW 11, KTH 3). Offline units last reported 18:20 to 18:24 UTC on 14 Nov. All 61 on 4.7.2. |
| Searched for a record of the customer's claimed call with a Tern engineer the week before | Marcus Lee, by 16 Nov 01:32 UTC | No call or ticket found. Last ticket TRN-75530 closed 2 Oct. Asked the customer for a name; he cannot remember it. |
| Checked SIM status in the Tern Connect console | Marcus Lee, by 16 Nov 02:10 UTC | All 14 SIMs Active. Last data sessions ended 18:21 to 18:24 UTC on 14 Nov. No session attempts since. |
| Compared hardware models of online and offline units | Marcus Lee, by 16 Nov 02:10 UTC | Offline units all G4-C, online units all G4-E |
| Reviewed the 4.7.2 release notes | Marcus Lee, by 16 Nov 02:10 UTC | Found "cellular modem firmware updated to MX-31.4 (G4-C only)" |
| Remote SMS wake to DRW-GW-01, DRW-GW-05 and KTH-GW-02 | Marcus Lee, 16 Nov 02:05 UTC | No response by 02:10 UTC |
| Asked the customer to read the front-panel lights on two or three units | Marcus Lee asked at 01:32 UTC. Darwin site lead answered via Grant Tobias at 03:05 UTC on 16 Nov | Every Darwin unit: solid green power light, flashing amber NET light (reported). Marcus read this against the LED guide as the modem not registered on the mobile network. |
| Power-cycled all 11 Darwin units again (customer's own action; reported) | Darwin site, morning of 16 Nov (reported 03:05 UTC) | Lights came back the same (reported) |

## Commitments to the customer
| Commitment (quoted) | Made by | When | Due | Status |
|---|---|---|---|---|
| "I told him I'd check the fleet and call him back within the hour." (Marcus's call note records what he said on the call) | Marcus Lee (Tier 1), by phone | 16 Nov 01:05 UTC | 16 Nov 02:05 UTC | Met. Marcus's 01:32 UTC email opens "as discussed on the phone just now". |
| "If you can tell me who you spoke to, I'll follow it up." | Marcus Lee (Tier 1), email | 16 Nov 01:32 UTC | No date given | Condition not met. The customer could not name the engineer (03:05 UTC). No follow-up recorded. |
| "I'm escalating this to our Field Systems Engineering team now." | Marcus Lee (Tier 1), email | 16 Nov 03:40 UTC | No date given ("now") | Met. Escalated to Tier 2 at 03:50 UTC. |
| "I'll send you an update by 12:00 AWST tomorrow, Tuesday 17 November (04:00 UTC), or sooner if engineering has news." | Marcus Lee (Tier 1), email | 16 Nov 03:40 UTC | 17 Nov 04:00 UTC (12:00 AWST) | Pending. Tier 2 now owns it (policy 5.3). |

No fix date has been promised: Marcus wrote "I can't give you a fix date" (03:40 UTC). No credit, refund or compensation has been offered. The account record shows "Open credits: None".

## Service level
- Tier (support plan): Business (account record, "Support plan: Business"; policy 1.3). The thread uses "Tier 1" and "Tier 2" for support levels; these are not the support plan.
- Priority/severity: P2 (ticket field at creation, 16 Nov 01:05 UTC; unchanged at escalation, 03:50 UTC). The customer's request for P1 is recorded and was not applied.
- Target: per policy 3.1, Business P2 is "4 business hours" for first response and "27 business hours" for resolution.
- Clock rule:
  - Start: "The clock starts when the ticket is created" (4.1): 2026-11-16 01:05 UTC.
  - Business hours: "08:30 to 17:30 Australia/Perth time (AWST, UTC+8, no daylight saving), Monday to Friday, excluding Western Australian public holidays" (1.1), which is "00:30 to 09:30 UTC on the same date" (1.2). Business-hours targets "count business hours only" (3.3).
  - Pauses: "paused only while the ticket status is 'Pending customer'" (4.2). The exported status history shows only Open and then Escalated, so no paused time is applied.
  - The policy does not list holiday dates. The arithmetic below assumes no WA public holiday falls between 16 and 19 Nov 2026.
- First response: met. The ticket was logged by Marcus Lee during the customer's call at 01:05 UTC, and policy 1.4 says this "counts as a first response when logged".
- Deadline (resolution): **Thursday 2026-11-19 01:05 UTC (09:05 AWST)**. Arithmetic (one business day is 9 hours, 00:30 to 09:30 UTC):
  - Mon 16 Nov, 01:05 to 09:30 UTC: 8h25m counted. 18h35m left.
  - Tue 17 Nov: 9h counted. 9h35m left.
  - Wed 18 Nov: 9h counted. 35m left.
  - Thu 19 Nov, from 00:30 UTC: 00:30 + 35m = 01:05 UTC.
  - If a "Pending customer" period exists that this export does not show, the deadline moves later by the paused business time.
- At-risk point: policy 4.4 says "at risk" means "less than 25% of its resolution target remains". 25% of 27h is 6h45m, so the ticket becomes at risk at **Wed 2026-11-18 03:20 UTC (11:20 AWST)**. Arithmetic: counting back 6h45m of business time from Thu 01:05 UTC gives 35m on Thu, then 6h10m back from Wed 09:30 UTC, which is Wed 03:20 UTC.
- Status: **open** (within target in policy terms), with 24h15m business hours remaining (2h45m used, from 01:05 to 03:50 UTC). This is as of 2026-11-16 03:50 UTC, the last thread timestamp (the escalation event), labelled as such.
  - If this handoff is read on this session's date, 2026-11-21 (Saturday), both the 17 Nov update commitment and the 19 Nov resolution deadline have passed. The export shows neither met, which would make the update overdue and the ticket breached. Check for activity after this export.
- Customer updates: for P2, policy 7.1 requires "at least once each business day". That means an update is needed on Tue 17 Nov (covered if the 04:00 UTC promise is kept) and on Wed 18 Nov.
- Escalation notes: from escalation, Tier 2 "owns the ticket, including customer updates and commitments already made" (5.3). Team Lead notification at escalation (5.2) applies only to P1 or at-risk P2. Neither applied at 03:50 UTC.

## Recommended next action
Turn the leading suspect (the MX-31.4 modem firmware in 4.7.2 stops G4-C modems registering) into verified or ruled out, using Tern's own systems before involving the customer's sites. In TernCloud, look for any other G4-C gateway that has taken 4.7.2 (other customers' fleets or internal test units), and check whether it stayed online through and after its update.

- If other G4-C units on 4.7.2 also went offline when they updated, the firmware cause is effectively confirmed, and the issue is not specific to Coldwater. Next, find a recovery path for units that can't be reached remotely (rollback of the modem firmware or the gateway image). Plan for on-site work at Darwin and Katherine, since SMS wake failed. Flag the 4.7.2 rollout to G4-C units internally.
- If other G4-C units on 4.7.2 are online and reporting, the modem firmware alone does not explain it. Look at what is specific to these 14 units, starting with their mobile network registration. Ask the carrier side whether the 14 SIMs show network attach attempts or rejections (Marcus checked data sessions, not registration).
- If no other G4-C unit has 4.7.2, the check can't decide. Instead, have Coldwater's technical contact, Lina Petrakis (IT Manager, account record), or the Katherine site read modem status from one unit. Katherine's units are untouched, so they are the cleanest sample.

Customer update due first: the update Marcus promised is due by **Tue 17 Nov 04:00 UTC (12:00 AWST)**. Send it to Grant Tobias even if the check is not finished. Within policy 6.1 and 6.2, it may give the next-update time and the actions Tier 2 is taking, but no fix date. Repeat Marcus's instruction not to factory-reset any unit, because that would erase stored readings, and ask Katherine to leave their 3 units as they are. If the customer pursues the $40,000-a-day loss or compensation, only the Account Manager, Rhys Kaplan, or the Head of Customer Support may make an offer (6.3), and none has been made. Send another update on Wed 18 Nov (7.1). Keep the at-risk point (Wed 03:20 UTC) and the deadline (Thu 01:05 UTC) in view.

## Gaps
- Root cause not verified. The MX-31.4 link rests on correlation and the LED reading.
- Whether the 14 units hold readings from 14 Nov 18:20 UTC onward has not been checked. Nor has whether those readings survive the power-cycles Darwin has already done twice.
- Whether 4.7.2 or MX-31.4 can be rolled back on a G4-C, remotely or on site, is not stated in the sources.
- Carrier-side network registration or attach records for the 14 SIMs have not been checked. Only data sessions were checked.
- Katherine's LED state is unknown. The customer reported Darwin only.
- The claimed call from a Tern engineer saying 4.7.2 "was fixed and safe" is unconfirmed, and no record was found. "Fixed" suggests a known earlier 4.7.2 issue; nobody has checked internally for one.
- WA public holiday dates are not stated in the policy. The deadline assumes none between 16 and 19 Nov.
- Status history comes from the thread export only. The deadline assumes no "Pending customer" period.
- No activity after 16 Nov 03:50 UTC appears in the export. It is not known whether the 17 Nov update went out.
- The technical contact, Lina Petrakis, has not been involved in the thread so far.
