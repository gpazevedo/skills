# Escalation handoff: TRN-77391 High-temperature SMS alarms not received from vat gateways (GW-03 still failing)

Reference time ("now"): 2026-11-24 06:00 UTC = Tue 24 Nov 14:00 AWST (given in the thread export header as the as-of time; matches the escalation event)
Inputs missing: none (thread, account record and policy all supplied). Not supplied: a list of WA public holidays; none are assumed in the 19-26 Nov window.

## Problem as currently understood
The high-temperature SMS alarm rule does not fire on gateways whose clocks run ahead of the sensor timestamps, because the rule engine skips evaluation. Vats 1 and 2 are working again after an HTTPS time set. Vat 3 (VAT-GW-03) is still not alarming: it rejects the time set with an RTC write error, twice, and a reboot did not help, so a hardware fault is suspected. The cause of the NTP failure is unknown. NTP is still failing on all three gateways, so GW-01 and GW-02 may drift again. Product loss has already occurred (18,000 L dumped).

- Vat 3 went over 7°C on Tuesday night (17 Nov) for about 40 min with no SMS [reported] (Aroha Ngata, 2026-11-19 07:50)
- TernCloud dashboard shows the reading went over the limit [reported] (Aroha Ngata, 2026-11-19 07:50)
- Alarm test on 19 Nov: vats 4-9 sent SMS within a minute; vats 1-3 sent nothing [reported] (Aroha Ngata, 2026-11-19 07:50)
- Each vat has its own gateway VAT-GW-01 to 09, model G4-E [verified] (account record)
- Vats 1-9 use the same rule template and same SMS recipients [verified] (Hannah Odum, 2026-11-20 01:05, checked rules in TernCloud)
- Rule engine on GW-01/02/03 logs RULE_EVAL_SKIPPED reason=TS_FUTURE at every evaluation since 12 Nov [verified] (Hannah Odum internal note, 2026-11-20 07:15, from bundles)
- Gateway clocks ahead: GW-01 +9m12s, GW-02 +8m40s, GW-03 +11m03s [verified] (same note)
- NTP log "sync failed: timeout (pool.terncloud.net:123)" on all three since 12 Nov [verified] (same note)
- GW-01 to 03 are on VLAN 30; GW-04 to 09 show last time sync OK in TernCloud [verified] (same note)
- The 5-minute window never fills while the clock is ahead, so the rule is skipped [suspected] (mechanism proposed in Hannah Odum's note, 2026-11-20 07:15; the skip log supports it, but no test isolates it)
- UDP 123 blocked for VLAN 30 [suspected] (Hannah Odum, 2026-11-20 07:15, "Not confirmed")
- Customer IT says nothing changed on VLAN 30 and outbound UDP 123 is allowed [reported] (Aroha Ngata, 2026-11-23 01:40; relayed from IT, no check shown)
- Vat 3 went over 7°C again about 01:00 "our time" on Sunday night with no SMS; found about 50 min later on the hourly check; 18,000 L dumped [reported] (Aroha Ngata, 2026-11-23 01:40)
- After HTTPS force time sync: GW-01 and GW-02 offset under 1 s [verified] (Hannah Odum internal note, 2026-11-23 02:40); vats 1 and 2 SMS sent within a minute in the retest [reported] (Aroha Ngata, 2026-11-23 03:05); GW-01 and GW-02 still in sync on 24 Nov [verified] (Hannah Odum internal note, 2026-11-24 05:20)
- GW-03 rejects time set: TIME_SET_REJECTED: RTC write error, twice; clock still about +11 min after reboot [verified] (Hannah Odum internal notes, 2026-11-23 02:40 and 2026-11-24 05:20)
- Vat 3 SMS still not received on retest [reported] (Aroha Ngata, 2026-11-23 03:05)
- GW-03 may have a hardware fault [suspected] (Hannah Odum, 2026-11-24 05:40)
- Hourly dashboard checks by night staff are not a practical workaround [reported] (Aroha Ngata, 2026-11-23 01:40); the ticket was raised to P2 on that basis, citing clause 2.2 [verified] (priority event, 2026-11-23 02:15)

Conflicts:
- UDP 123 on VLAN 30: support [suspected] blocked (Odum, 2026-11-20 07:15) vs customer IT [reported] allowed (Ngata, 2026-11-23 01:40). Unresolved; no network check by support is recorded.
- Workaround: on 2026-11-20 07:20 Odum wrote "the hourly checks cover you over the weekend"; the customer reported on 2026-11-23 that hourly checks failed and led to product loss. Support accepted this by moving to P2 (2026-11-23 02:15).

## Tried so far
| When (UTC) | Who | What | Result |
|------|-----|------|--------|
| 2026-11-19 (afternoon, before ticket) | Aroha Ngata | Alarm test on all nine vats | Vats 4-9 SMS OK; vats 1-3 no SMS |
| 2026-11-20 01:05 | Hannah Odum | Compared TernCloud alarm rules, vats 1-9 | Same template and recipients; config does not explain it |
| 2026-11-20 01:10 to 05:40 | Aroha Ngata | Downloaded diagnostic bundles from GW-01, 02, 03 | Attached; showed TS_FUTURE skips, clock offsets, NTP timeouts |
| 2026-11-20 07:20 | Hannah Odum (asked of customer IT) | Check whether outbound UDP 123 is allowed from VLAN 30 | Customer IT reports allowed (2026-11-23 01:40); not independently checked |
| 2026-11-23 02:35 | Hannah Odum | "Force time sync (HTTPS)" to GW-01, 02, 03 | GW-01, 02 OK (offset under 1 s); GW-03 TIME_SET_REJECTED: RTC write error |
| 2026-11-23 ~03:05 | Aroha Ngata | Alarm test vats 1-3 after sync | Vats 1, 2 SMS OK; vat 3 nothing |
| 2026-11-24 05:15 | Hannah Odum | Second force time sync to GW-03 | Same RTC write error |
| 2026-11-24 05:17 | Hannah Odum (customer agreed by phone 05:10) | Remote reboot of GW-03 | Back online 05:19; clock still +11 min |
| 2026-11-24 after 05:19 | Hannah Odum | Alarm test on vat 3 after reboot | Result not recorded |

## Commitments to the customer
| When (UTC) | Made by | Verbatim commitment | Status | Policy note |
|------|---------|---------------------|--------|-------------|
| 2026-11-23 02:20 | Hannah Odum | "I've passed your request to Joel Brandt, your account manager." (request = cost of milk covered) | Pending: no reply from Joel Brandt recorded in the thread or account record (open credits: none) | 6.2: agents "must not promise ... a service credit, a refund or compensation"; 6.3: "Only the Account Manager named in the account record, or the Head of Customer Support, may offer a service credit, refund or compensation. An offer is valid only when recorded in writing on the ticket or in the account record." No compensation has been promised. |
| 2026-11-23 02:20 | Hannah Odum | "Once that's done, could you run the alarm test on vats 1 to 3?" (customer request; she committed to send the sync command, which she did at 02:35) | Met | 6.1 allows actions agents take themselves |
| 2026-11-24 05:40 | Hannah Odum | "I'm escalating this to our Field Systems Engineering team now. You'll get an update from us by 17:30 AWST today (09:30 UTC)." | Pending; due in 3h30m at now; 09:30 UTC is 17:30 AWST | 6.1 allows committing to the time of the next update; 5.3: from escalation Tier 2 owns customer updates and commitments already made |

The customer's request that the milk cost be covered is a request, not a commitment.

## Service level
Plan Business (account record). Ticket created 2026-11-19 07:50 UTC (Thu 15:50 AWST). Priority P3 at creation, P2 from 2026-11-23 02:15 UTC.

Resolution clock
- Clause: 3.1 "Business | P2 | 4 business hours | 27 business hours"; 4.3 "If the priority changes, the resolution target becomes the target for the new priority, counted from ticket creation and excluding paused time."; 4.2 "The clock is paused only while the ticket status is 'Pending customer'."
- Clock: resolution, business hours (08:30-17:30 AWST, Mon-Fri), started 2026-11-19 07:50 UTC (15:50 AWST, inside business hours)
- Business hours elapsed to now: Thu 19 Nov 15:50-17:30 = 1h40; Fri 20 Nov 08:30-17:30 = 9h, less pause 01:10-05:40 UTC (09:10-13:40 AWST, Pending customer) 4h30 = 4h30; Mon 23 Nov = 9h; Tue 24 Nov 08:30-14:00 = 5h30. Weekend excluded. Total = 1h40 + 4h30 + 9h + 5h30 = 20h40.
- Remaining: 27h - 20h40 = 6h20. At-risk threshold: 25% of 27h = 6h45.
- Deadline: Tue 24 Nov has 3h30 left after 14:00 (to 17:30); remaining 2h50 into Wed 25 Nov from 08:30 gives Wed 25 Nov 11:20 AWST = 2026-11-25 03:20 UTC.
- Status: at risk (6h20 remaining is under 6h45; policy 4.4: "at risk if less than 25% of its resolution target remains"); missing terms: none (no WA public holiday is assumed in the period; any holiday would move the deadline later but not change at risk).
- Note: Hannah Odum's internal note of 2026-11-24 01:30 gives a due time of Thu 26 Nov 10:15 AWST, counting 27 hours from the priority change at 10:15 AWST Mon. That contradicts 4.3 (count from creation). Do not use it. Her "Plenty of time" is wrong.

First response clock
- Clause: 3.1 "Business | P2 | 4 business hours" and "Business | P3 | 9 business hours"; 1.4 first response is the first contact with the customer by a support agent.
- Clock: business hours, started 2026-11-19 07:50 UTC (15:50 AWST); first agent contact 2026-11-20 01:05 UTC (09:05 AWST Fri)
- Elapsed: Thu 1h40 + Fri 08:30-09:05 0h35 = 2h15.
- Status: met under P3 (9h) and under P2 (4h); missing terms: none.

Customer update clock
- Clause: 7.1 "P2: at least once each business day."
- Updates were sent Mon 23 Nov 02:20 UTC and Tue 24 Nov 05:40 UTC (05:40 UTC is 13:40 AWST). Status: met for 24 Nov; next due by end of business Wed 25 Nov, and the 09:30 UTC commitment above comes first.

Escalation requirement
- Clause: 5.2 "When a P1 ticket, or an at-risk P2 ticket, is escalated, the Support Team Lead must be notified at escalation."
- The ticket is an at-risk P2 at escalation (2026-11-24 06:00 UTC). No notification of the Support Team Lead is recorded in the thread. Status: not recorded; needs doing.

## Open questions
- Is outbound UDP 123 actually reachable from VLAN 30 at Brunswick? Support suspected blocked, customer IT says allowed. (Hannah Odum, 2026-11-20 07:20; answered by customer IT, unverified 2026-11-23 01:40)
- Why does NTP time out on GW-01 to 03 since 12 Nov, and why is GW-04 to 09 unaffected? Not answered.
- Is GW-03 RTC hardware faulty? (Odum, 2026-11-24 05:40, "may be")
- Does vat 3 alarm after the 05:17 reboot? No test result recorded.
- Will GW-01 and GW-02 drift again while NTP is failing?
- What did Joel Brandt answer on the milk compensation request? (Aroha Ngata asked 2026-11-23 01:40; passed on 2026-11-23 02:20; no reply recorded)
- Was the Support Team Lead notified of the at-risk P2 escalation? (policy 5.2)
- What interim measure covers vat 3 alarming while GW-03 is faulty? Not discussed.

## Recommended next action
Tier 2 (Field Systems Engineering) engineer to diagnose GW-03 now (pull a fresh diagnostic bundle after the reboot, check the RTC write error, decide on replacement or an interim alarm path for vat 3) and send the customer an update on the result by 2026-11-24 09:30 UTC (17:30 AWST), the commitment already made, copying the outcome to the ticket. In the same hour, notify the Support Team Lead (clause 5.2) and chase Joel Brandt for a written answer on the compensation request. Rests on: GW-03 RTC write errors x2 and reboot failure (Odum 2026-11-23 02:40, 2026-11-24 05:20), the update commitment (Odum 2026-11-24 05:40), the at-risk resolution status (deadline Wed 25 Nov 11:20 AWST) and the unrecorded Team Lead notification.
