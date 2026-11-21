# Handoff: TRN-77102, Coldwater Freight Pty Ltd (CWF-2210)

Position as of 2026-11-16 03:50 UTC (11:50 AWST, Monday).

## 1. Summary
Coldwater Freight Pty Ltd (account CWF-2210, Business plan) has 14 of its 61 TernGate G4 gateways offline in TernCloud. These are all G4-C cellular units at Darwin (11) and Katherine (3). They went offline during the 2026-11-14 firmware 4.7.2 rollout. The ticket is P2 and within its resolution target, with the next customer update due at 2026-11-17 04:00 UTC (12:00 AWST). The customer says it is losing about $40,000 a day and is pressing for P1.

## 2. Problem and evidence
- _verified_ (account record, fleet table): the fleet is 61 gateways. Kewdale 30 and Wingfield 17 are G4-E Ethernet. Darwin 11 and Katherine 3 are G4-C cellular.
- _verified_ (Lee 01:32 email, TernCloud as of 01:25 UTC): 47 gateways are online and reporting with complete readings, and 14 are offline. The 14 are all Darwin (11) and Katherine (3).
- _verified_ (Lee 01:32, TernCloud): all 61 gateways were updated to 4.7.2 in the window that started 2026-11-14 18:00 UTC. The 47 online units run 4.7.2.
- _verified_ (Lee 02:10 internal note, Tern Connect): all 14 SIMs are Active. Their last data sessions ended between 18:21 and 18:24 UTC on 14 Nov, with no session attempts since.
- _verified_ (Lee 02:10 note, plus account record): all 14 offline units are G4-C and all 47 online units are G4-E.
- _reported_ (Tobias 03:05, relaying the Darwin site lead): every Darwin unit shows solid green POWER and flashing amber NET, unchanged after power-cycling. Not observed by support. Katherine has not been checked.
- _hypothesis_ (Lee 02:10): the 4.7.2 cellular modem firmware update to MX-31.4 (G4-C only) is the link. Stated in the release notes as part of 4.7.2. The link to the outage is untested and Lee called it "not confirmed".
- _hypothesis_ (Lee 03:40): a flashing amber NET light on a G4-C means the modem is not registered on the mobile network, so the fault is on the gateway side and not the SIM accounts. The LED meaning comes from the LED guide, which is not in the case file. The inference is untested, and Lee said he "can't confirm the cause yet".
- _reported_ (Tobias 01:12): "all temperature data for the last three days" is lost. This is unverified, and the timeline contradicts it. Offline units last reported on 2026-11-14 at about 18:21 UTC, about 33.5 hours before the as-of time. Lee also noted that G4 gateways store readings locally and upload them on reconnect, so data loss is not established.
- _reported_ (Tobias 01:12, 03:05): "every one of our gateways" and "every site" is affected, and Perth cannot dispatch Darwin loads without the certificates. The all-gateways claim is contradicted by the verified 47 online units (Perth and Adelaide are online). The Perth dispatch dependency on Darwin certificates is plausible but unverified.
- _reported_ (Tobias 01:12): the cost is about $40,000 a day in uncertifiable stock. Unverified.
- _reported_ (Tobias 01:12, 03:05): an unnamed Tern engineer said "last week" that 4.7.2 was fixed and safe. Lee found no record of a call or ticket that week, and the last ticket was TRN-75530 (closed 2 Oct). Tobias has not named the engineer. Treat as unverified.

## 3. Tried so far
| Action | Result | Who |
| --- | --- | --- |
| Rebooted all Darwin gateways (reported on the 01:05 call, before ticket creation) | No difference (reported) | Customer, Darwin team |
| Fleet check in TernCloud (as of 01:25 UTC) | 47 online, 14 offline, with the pattern above | Marcus Lee |
| Checked Tern Connect console for the 14 SIMs | All Active, last sessions 18:21-18:24 UTC 14 Nov, none since | Marcus Lee |
| Compared model against status | Offline = G4-C, online = G4-E; 4.7.2 release notes mention modem firmware MX-31.4 | Marcus Lee |
| Remote SMS wake to DRW-GW-01, DRW-GW-05, KTH-GW-02 at 02:05 UTC | No response by 02:10; later result not recorded | Marcus Lee |
| Asked Darwin for front-panel lights on 2-3 units | Answered 03:05 (see section 2) | Lee asked, customer answered |
| Power-cycled all 11 Darwin units again (the morning of 16 Nov, before 03:05 UTC) | Lights unchanged (reported) | Customer, Darwin site lead |
| Katherine units | Not touched, not checked; no result | Customer |
| Interpreted NET light via the LED guide | Modem not registered on the network (inference, see section 2) | Marcus Lee |
| Instructed customer not to factory-reset (preserves locally stored readings) | Instruction only; compliance not recorded | Marcus Lee |

## 4. Commitments to the customer
| Quote | Author | When | Status |
| --- | --- | --- | --- |
| "I'd check the fleet and call him back within the hour" (call note paraphrase) | Marcus Lee | 2026-11-16 01:05 UTC | Kept. Fleet checked and call-back plus email sent at 01:32 UTC (27 minutes). |
| "If you can tell me who you spoke to, I'll follow it up." | Marcus Lee | 01:32 UTC | Conditional and open. The customer has not named the engineer (03:05). |
| "I'm escalating this to our Field Systems Engineering team now." | Marcus Lee | 03:40 UTC | Kept. Escalated to Tier 2 at 03:50 UTC. |
| "I'll send you an update by 12:00 AWST tomorrow, Tuesday 17 November (04:00 UTC), or sooner if engineering has news." | Marcus Lee | 03:40 UTC | OPEN. Due 2026-11-17 04:00 UTC. Tier 2 now owns it (policy 5.3). |

Also stated, not promises: "I can't give you a fix date" (03:40), and "That doesn't change how seriously we're taking it" (01:32). No fix date, credit, refund or compensation has been promised. Policy 6.2 prohibits agents from promising these, and under 6.3 only Rhys Kaplan (Account Manager) or the Head of Customer Support may offer a credit.

## 5. Service level
- Tier: Business plan (account record). Current priority P2 (recorded on the ticket; the customer's P1 request was not applied, policy 2.5).
- Priority check: P1 needs more than half of the gateways offline (policy 2.1). 14 of 61 is 23%, so P2 under 2.2 stands. Offline gateways lack a practical workaround, so P3 does not apply.
- Clock start (policy 4.1): ticket created Mon 2026-11-16 01:05 UTC (09:05 AWST), inside business hours (00:30-09:30 UTC, policy 1.2). No "Pending customer" time, so no pause (4.2).
- First response (policy 3.1, Business P2: 4 business hours): logged by an agent during the call, so it counts at 01:05 UTC (1.4). Met. The email follow-up came at 01:32.
- Resolution target (policy 3.1, Business P2: 27 business hours), arithmetic:
  - Mon 16 Nov: 01:05 to 09:30 UTC = 8h25m, so 18h35m remain.
  - Tue 17 Nov: 9h, so 9h35m remain.
  - Wed 18 Nov: 9h, so 0h35m remain.
  - Thu 19 Nov: 00:30 + 0h35m = 01:05 UTC.
  - Deadline: Thu 2026-11-19 01:05 UTC (09:05 AWST). This assumes no WA public holiday on 17-19 Nov, which the supplied case does not check.
- Elapsed at 03:50 UTC: 2h45m of business time. Remaining: 24h15m of 27h (about 90%). At-risk threshold (policy 4.4) is under 25%, that is under 6h45m. Status: **within target**.
- If it were P1 (not applicable): Business P1 resolution is 24 hours on calendar time, giving 2026-11-17 01:05 UTC. Reprioritising would also change the deadline (4.3).
- Customer updates (policy 7.1, P2): at least once each business day. The promised 04:00 UTC Tuesday update meets this.
- Escalation (policy 5.2): the Support Team Lead must be notified at escalation only for P1 or an at-risk P2. This ticket is neither, so no notification is required. None is recorded.

## 6. Recommended next action
**Primary (owner: Tier 2 Field Systems Engineer, Field Systems Engineering).** Test the 4.7.2 / MX-31.4 modem firmware hypothesis on G4-C units. Pull device or modem logs for one or more of the 14 units and check whether the modem update completed and why the unit does not register. Run 4.7.2 on a lab G4-C if one is available. This confirms or rules out the cause, which the case has no verified evidence for. It serves the 2026-11-17 04:00 UTC customer update and the 2026-11-19 01:05 UTC resolution target.

Alternatives and parallel steps:
1. Support (Tier 2 owner of the ticket): before 04:00 UTC Tuesday, send the committed update even if the cause is not found, saying what was checked and what is next. Do not give a fix date or mention credits (6.2).
2. Ask Lina Petrakis (technical contact) to read the Katherine LEDs (not yet checked), so the fault is confirmed on all 14 units and not only Darwin. This confirms the group is uniform.
3. Check whether other customers' G4-C units that took 4.7.2 are also offline. This confirms whether the issue is general and not specific to this account.
4. Repeat the SMS wake to a few units and record the outcome. The first attempt has no recorded result after 02:10.
5. Refer the customer's cost and "Tern is responsible" claims to Rhys Kaplan (Account Manager). Support must not respond on compensation.
6. Keep the "do not factory reset" instruction in place until stored readings are confirmed safe.

## 7. Gaps and conflicts
- **Conflict: scope.** The customer says all gateways and every site are down. TernCloud shows 47 of 61 online (Perth and Adelaide) and 14 offline (Darwin and Katherine). Only the verified figures should drive priority.
- **Conflict: duration of data loss.** The customer says three days. The offline units last reported on 14 Nov about 18:21 UTC, about 33.5 hours before the as-of time. Whether any readings are truly lost is not known, because of local storage on the G4.
- **Conflict: "fixed and safe" claim.** The customer says an engineer assured them that 4.7.2 was safe. Support found no record. Engineer unidentified. Do not accept or deny it.
- **Conflict (minor): last-report time.** Lee's 01:32 email says last reports were 18:20-18:24 UTC. The 02:10 console note says data sessions ended 18:21-18:24 UTC. They are different measures. The difference is minor.
- **Missing:** the LED guide, the 4.7.2 release notes and the device logs are not in the case file. The NET-light and MX-31.4 statements rest on Lee's summary.
- **Missing:** no result is recorded for the SMS wake after 02:10. Katherine LEDs and units are unchecked.
- **Not stated in the supplied policy:** any term on data-loss liability, a fix date, a hardware or firmware defect process, or how long Tier 2 has to respond after escalation. No deadline is given for these. Public-holiday status of 17-19 Nov in WA is not in the case.
- **Not verified:** the $40,000-a-day cost and the Perth dispatch dependency.
