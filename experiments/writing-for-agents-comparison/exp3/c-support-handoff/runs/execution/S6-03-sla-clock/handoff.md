# Escalation handoff: TRN-77391 High-temperature SMS alarms not received from vat gateways GW-01 to 03; GW-03 (vat 3) still failing

Reference time ("now"): 2026-11-24 06:00 UTC (Tue 14:00 AWST) (last thread message)
Inputs missing: none (thread, account record and policy all supplied)

## Problem as currently understood
High-temperature SMS alarms stopped for vats 1 to 3 at the Brunswick plant. Support found that the rule engine on GW-01, 02 and 03 skips every evaluation with a "future timestamp" reason. The gateway clocks are 8 to 11 minutes fast, and NTP sync is failing on all three. Forcing the clock over HTTPS fixed GW-01 and GW-02, and the customer reports vats 1 and 2 now alarm. GW-03 rejects every clock set with an RTC write error, so vat 3 still has no SMS alarm, and a second excursion on vat 3 led to 18,000 litres of milk being dumped. NTP is still failing on all three gateways.

- Vat 3 exceeded 7°C for about 40 minutes on Tuesday night (17 Nov) and no SMS was received; the TernCloud dashboard shows the reading over the limit [reported] (Aroha Ngata, 2026-11-19 07:50 UTC)
- In a customer alarm test, vats 4 to 9 sent the SMS within a minute and vats 1, 2 and 3 sent nothing [reported] (Aroha Ngata, 2026-11-19 07:50 UTC)
- Each vat has its own gateway, VAT-GW-01 to VAT-GW-09, model G4-E (Ethernet), at the Brunswick processing plant [verified] (account record)
- Vats 1 to 9 all use the same alarm rule template ("Vat high temp, above 7°C for 5 min") with the same SMS recipients, so configuration does not explain the difference [verified] (Hannah Odum, 2026-11-20 01:05 UTC)
- The rule engine on GW-01, 02 and 03 logs "RULE_EVAL_SKIPPED reason=TS_FUTURE" at every evaluation since 12 Nov [verified] (Hannah Odum internal note, diagnostic bundles, 2026-11-20 07:15 UTC)
- Gateway clocks are ahead of sensor timestamps: GW-01 +9 min 12 s, GW-02 +8 min 40 s, GW-03 +11 min 03 s [verified] (Hannah Odum internal note, 2026-11-20 07:15 UTC)
- With the clock that far ahead the rule's 5-minute window never fills, so the rule is skipped [suspected] (Hannah Odum internal note, 2026-11-20 07:15 UTC); consistent with vats 1 and 2 alarming after their clocks were corrected [reported] (Aroha Ngata, 2026-11-23 03:05 UTC)
- NTP log on all three: "NTP sync failed: timeout (pool.terncloud.net:123)", repeated since 12 Nov [verified] (Hannah Odum internal note, 2026-11-20 07:15 UTC)
- GW-01 to 03 are on VLAN 30 [verified] (diagnostic bundles, Hannah Odum internal note, 2026-11-20 07:15 UTC)
- GW-04 to 09 show last time sync OK in TernCloud [verified] (Hannah Odum internal note, 2026-11-20 07:15 UTC)
- UDP 123 is blocked for VLAN 30 [suspected] (Hannah Odum internal note, 2026-11-20 07:15 UTC, "Not confirmed")
- Nothing has changed on VLAN 30 and outbound UDP 123 is allowed [reported] (Aroha Ngata relaying customer IT, 2026-11-23 01:40 UTC)
- Vat 3 went over 7°C again at about 01:00 AWST on Sunday (22 Nov), no SMS; over the limit about 50 minutes before the hourly check caught it; 18,000 litres dumped [reported] (Aroha Ngata, 2026-11-23 01:40 UTC)
- Hourly manual checks are not a practical workaround [reported] (Aroha Ngata, 2026-11-23 01:40 UTC); accepted by support in the P3 → P2 change citing clause 2.2 [verified] (event, Hannah Odum, 2026-11-23 02:15 UTC)
- GW-01 and GW-02 clocks are in sync (offset under 1 s) after "Force time sync (HTTPS)" [verified] (Hannah Odum internal note, 2026-11-23 02:40 UTC); still in sync [verified] (Hannah Odum internal note, 2026-11-24 05:20 UTC)
- GW-03 rejects the clock set with "TIME_SET_REJECTED: RTC write error" (twice) and is still +11 min after a reboot [verified] (Hannah Odum internal notes, 2026-11-23 02:40 UTC and 2026-11-24 05:20 UTC)
- GW-03's refusal to set its clock may be a hardware fault [suspected] (Hannah Odum, 2026-11-24 05:40 UTC)
- NTP is still failing on all three gateways [verified], so GW-01 and GW-02 may drift again [suspected] (Hannah Odum internal note, 2026-11-24 05:20 UTC)

Conflicts:
- NTP failure cause: support suspects UDP 123 is blocked for VLAN 30 [suspected] (Hannah Odum, 2026-11-20 07:15 UTC); customer IT says nothing changed on VLAN 30 and outbound UDP 123 is allowed [reported] (Aroha Ngata, 2026-11-23 01:40 UTC). Neither side's check is shown in the case.
- Adequacy of hourly checks: support told the customer "the hourly checks cover you over the weekend" (Hannah Odum, 2026-11-20 07:20 UTC); the customer reports they were not enough, with 50 minutes over limit and 18,000 litres dumped [reported] (Aroha Ngata, 2026-11-23 01:40 UTC).

## Tried so far
| When | Who | What | Result |
|------|-----|------|--------|
| 2026-11-19 afternoon (before 07:50 UTC) | Customer (Aroha Ngata) | Alarm test on all nine vats | Vats 4 to 9 sent SMS within a minute; vats 1 to 3 sent nothing [reported] |
| From 2026-11-19 | Customer night staff | Hourly dashboard checks as workaround | Caught the 22 Nov vat 3 excursion only after about 50 minutes; 18,000 litres dumped [reported] |
| 2026-11-20 01:05 UTC | Hannah Odum (Tier 1) | Checked TernCloud alarm rules for vats 1 to 9 | Same template and recipients on all nine; not the cause [verified] |
| 2026-11-20 01:10 to 07:15 UTC | Hannah Odum, with customer | Diagnostic bundles from GW-01, 02, 03 requested, supplied (05:40) and reviewed | TS_FUTURE rule skips, clocks 8 to 11 min fast, NTP timeouts since 12 Nov, all on VLAN 30 [verified] |
| 2026-11-20 07:20 to 2026-11-23 01:40 UTC | Customer IT | Checked outbound UDP 123 from VLAN 30 | "Nothing has changed on VLAN 30 and outbound UDP 123 is allowed" [reported]; method not recorded |
| 2026-11-23 02:35 UTC | Hannah Odum | "Force time sync (HTTPS)" to GW-01, 02, 03 | GW-01, GW-02 OK, offset under 1 s; GW-03 "TIME_SET_REJECTED: RTC write error", still +11 min 05 s [verified] |
| 2026-11-23 (reported 03:05 UTC) | Customer (Aroha Ngata) | Alarm test on vats 1 to 3 | Vats 1 and 2 sent SMS within a minute; vat 3 nothing [reported] |
| 2026-11-24 05:15 UTC | Hannah Odum | Second "Force time sync (HTTPS)" to GW-03 | Same "TIME_SET_REJECTED: RTC write error" [verified] |
| 2026-11-24 05:17 UTC | Hannah Odum (customer agreed by phone 05:10) | Remote reboot of GW-03 from TernCloud | Back online 05:19; clock still +11 min [verified] |

## Commitments to the customer
| When | Made by | Verbatim commitment | Status (met / pending / overdue) | Policy note |
|------|---------|---------------------|----------------------------------|-------------|
| 2026-11-20 01:05 UTC | Hannah Odum | "I'd like to look at the gateways themselves." | Met (bundles reviewed, internal note 2026-11-20 07:15 UTC) | 6.1: "Support agents may commit to the time of the next update and to actions they will take themselves." |
| 2026-11-23 02:20 UTC | Hannah Odum | "I'm not able to offer compensation myself, so I've passed your request to Joel Brandt, your account manager." | Met as stated; no reply from Joel Brandt and no offer recorded on the ticket | 6.2: "Support agents must not promise a fix date, a service credit, a refund or compensation." 6.3: "Only the Account Manager named in the account record, or the Head of Customer Support, may offer a service credit, refund or compensation. An offer is valid only when recorded in writing on the ticket or in the account record." Account record: Account Manager Joel Brandt; open credits none. |
| 2026-11-23 02:20 UTC | Hannah Odum | "Next, I'm going to send a command from TernCloud that sets the clock on GW-01 to 03 over HTTPS, which avoids the NTP port." | Met (sent 02:35 UTC; GW-03 rejected) | 6.1 (as above) |
| 2026-11-24 05:40 UTC | Hannah Odum | "I'm escalating this to our Field Systems Engineering team now." | Met (escalated 06:00 UTC) | 6.1 (as above) |
| 2026-11-24 05:40 UTC | Hannah Odum | "You'll get an update from us by 17:30 AWST today (09:30 UTC)." | Pending; due 2026-11-24 09:30 UTC, 3 h 30 min from now | 6.1 (as above). 5.3: "From escalation, Tier 2 owns the ticket, including customer updates and commitments already made." |

## Service level
Plan: Business (account record). Priority: P3 at creation, P2 since 2026-11-23 02:15 UTC (event). Business hours per 1.1 and 1.2: 00:30 to 09:30 UTC, Monday to Friday. Ticket created Thu 2026-11-19 07:50 UTC, inside business hours. Paused per 4.2 while "Pending customer": 2026-11-20 01:10 to 05:40 UTC (4 h 30 min, all inside business hours).

First response
- Clause: "Business | P3 | 9 business hours | 72 business hours" (3.1); "First response means the first contact with the customer by a support agent, by phone, email or portal." (1.4)
- Clock: first response, business hours, started at ticket creation 2026-11-19 07:50 UTC (4.1)
- Deadline: 2026-11-20 07:50 UTC (Thu 07:50 to 09:30 = 1 h 40 min; Fri 00:30 + 7 h 20 min = 07:50)
- Status: met; first contact 2026-11-20 01:05 UTC after 2 h 15 min of business time (1 h 40 min Thu + 35 min Fri). Also within the P2 target of 4 business hours. Missing terms: none

Resolution
- Clause: "Business | P2 | 4 business hours | 27 business hours" (3.1); "If the priority changes, the resolution target becomes the target for the new priority, counted from ticket creation and excluding paused time." (4.3); "A ticket is "breached" if its resolution target has passed unresolved, and "at risk" if less than 25% of its resolution target remains, measured on the same basis (calendar or business hours) as the target." (4.4); "A ticket that reports more than one fault is resolved only when every fault on it is resolved." (1.5)
- Clock: resolution, business hours, started at ticket creation 2026-11-19 07:50 UTC, excluding the 4 h 30 min pause
- Deadline: 2026-11-25 03:20 UTC (Wed 11:20 AWST). Arithmetic: Thu 19 Nov 07:50 to 09:30 = 1 h 40 min; Fri 20 Nov 9 h minus 4 h 30 min paused = 4 h 30 min (running 6 h 10 min); Mon 23 Nov 9 h (15 h 10 min); Tue 24 Nov 9 h (24 h 10 min); Wed 25 Nov 00:30 + 2 h 50 min = 03:20 UTC (27 h)
- Status: "at risk". Elapsed at now = 15 h 10 min + Tue 00:30 to 06:00 (5 h 30 min) = 20 h 40 min; remaining 6 h 20 min, which is less than 25% of 27 h (6 h 45 min). It became at risk at 2026-11-24 05:35 UTC, before the 06:00 UTC escalation. Missing terms: WA public holidays (1.1 excludes them; the policy does not list them). The computation assumes none on 19, 20, 23, 24 or 25 Nov, as the thread itself treats Mon 23 and Thu 26 Nov as working days.
- Note: Hannah Odum's internal SLA check (2026-11-24 01:30 UTC) counted 27 business hours from the P2 change ("Mon 10:15 AWST") to a due time of Thu 26 Nov 10:15 AWST. Clause 4.3 counts from ticket creation, which gives Wed 25 Nov 11:20 AWST.
- Note: 5.2 says "When a P1 ticket, or an at-risk P2 ticket, is escalated, the Support Team Lead must be notified at escalation." The ticket was an at-risk P2 when escalated at 06:00 UTC; no Team Lead notification is recorded in the thread.

Customer updates
- Clause: "P2: at least once each business day." (7.1)
- Clock: update interval, business days, started at the P2 change 2026-11-23 02:15 UTC (while P3 on 19 and 20 Nov the clause was "when there is news")
- Deadline: next update by end of business day Wed 2026-11-25 09:30 UTC; the separate commitment above falls due earlier, at 2026-11-24 09:30 UTC
- Status: met for Mon 23 Nov (message 02:20 UTC) and Tue 24 Nov (message 05:40 UTC); open for Wed 25 Nov. Missing terms: none

## Open questions
- Request that the cost of the dumped milk (18,000 litres) be covered (asked by Aroha Ngata, 2026-11-23 01:40 UTC); passed to Joel Brandt (Hannah Odum, 2026-11-23 02:20 UTC), no answer recorded
- No other unanswered questions in the thread.

## Recommended next action
Tier 2 (Field Systems Engineering) to confirm or rule out the suspected hardware fault behind GW-03's "TIME_SET_REJECTED: RTC write error" and settle how vat 3's alarm will be restored, then report the outcome to Aroha Ngata in the committed update; owner Tier 2 (Field Systems Engineering), by 2026-11-24 09:30 UTC (17:30 AWST), ahead of the at-risk resolution deadline of 2026-11-25 03:20 UTC. Rests on: GW-03 clock set rejected twice and reboot failed (2026-11-23 02:40, 2026-11-24 05:20 UTC); suspected hardware fault (2026-11-24 05:40 UTC); vat 3 still not alarming and product already lost (2026-11-23 01:40 and 03:05 UTC); update commitment due 09:30 UTC and Tier 2 ownership (5.3); resolution status "at risk".
