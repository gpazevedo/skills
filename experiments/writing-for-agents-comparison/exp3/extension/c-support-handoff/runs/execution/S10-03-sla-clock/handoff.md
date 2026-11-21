# Escalation handoff: TRN-77391 | Kestrel Dairy Co-operative (KDC-0418) | Vat 3 high-temperature SMS alarm still failing; GW-03 clock rejected

**Service level:** Resolution (Business, P2, 27 business hours) due Wed 25 Nov 2026 11:20 AWST (03:20 UTC) | At risk: 6 h 20 min of business time remaining as of 2026-11-24 06:00 UTC (policy 4.4 threshold is 6 h 45 min). A customer update is separately promised by 2026-11-24 09:30 UTC (see Commitments).

## Problem as currently understood
High-temperature SMS alarms from the milk vats on VAT-GW-01, 02 and 03 stopped firing because the gateway rule engine skipped every evaluation, and support verified from diagnostic bundles that those three gateway clocks were 8 to 11 minutes fast with NTP sync failing since 12 Nov. A forced HTTPS time sync verifiably brought GW-01 and GW-02 back into sync, and the customer reports vats 1 and 2 now alarm; GW-03 verifiably rejects every clock write ("TIME_SET_REJECTED: RTC write error") and stays about 11 minutes fast after two attempts and a reboot, so vat 3 has no SMS alarm. NTP is still verifiably failing on all three gateways, so GW-01 and GW-02 may drift again; the cause of the NTP failure is not known. The customer reports a missed vat 3 alarm on Sunday 22 Nov that led to 18,000 litres of milk being dumped, and has asked for the cost to be covered.

| Statement | Label | Source (author, timestamp) |
| --- | --- | --- |
| Vat 3 at Brunswick went above 7°C for about 40 minutes on "Tuesday night" (no date given; 17 Nov by inference) and nobody received the SMS; the dashboard shows the reading over the limit | Reported | Aroha Ngata, 2026-11-19 07:50 UTC |
| In the customer's test on 19 Nov afternoon, vats 4 to 9 sent the SMS within a minute and vats 1, 2 and 3 sent nothing | Reported | Aroha Ngata, 2026-11-19 07:50 UTC |
| Vats 1 to 9 all use the same alarm rule template ("Vat high temp, above 7°C for 5 min") with the same SMS recipients | Verified (Hannah Odum checked TernCloud, 2026-11-20 01:05 UTC) | Hannah Odum, 2026-11-20 01:05 UTC |
| Rule engine on GW-01, 02 and 03 logs "RULE_EVAL_SKIPPED reason=TS_FUTURE" at every evaluation since 12 Nov | Verified (Hannah Odum, from customer-supplied bundles, 2026-11-20 07:15 UTC) | Hannah Odum internal note, 2026-11-20 07:15 UTC |
| Gateway clocks ahead of sensor timestamps: GW-01 +9 min 12 s, GW-02 +8 min 40 s, GW-03 +11 min 03 s | Verified (Hannah Odum, bundles, 2026-11-20 07:15 UTC) | Hannah Odum internal note, 2026-11-20 07:15 UTC |
| NTP log on all three: "NTP sync failed: timeout (pool.terncloud.net:123)", repeated since 12 Nov | Verified (Hannah Odum, bundles, 2026-11-20 07:15 UTC) | Hannah Odum internal note, 2026-11-20 07:15 UTC |
| GW-01 to 03 are on VLAN 30; GW-04 to 09 show last time sync OK in TernCloud | Verified (Hannah Odum, bundles and TernCloud, 2026-11-20 07:15 UTC) | Hannah Odum internal note, 2026-11-20 07:15 UTC |
| With the clock that far ahead the 5-minute reading window never fills, so the rule is skipped | Suspected (consistent with vats 1 and 2 alarming after their clocks were fixed, but that test result is customer-reported) | Hannah Odum internal note, 2026-11-20 07:15 UTC |
| UDP 123 is blocked for VLAN 30 | Suspected (Hannah Odum: "Not confirmed") | Hannah Odum internal note, 2026-11-20 07:15 UTC |
| Customer IT says nothing has changed on VLAN 30 and outbound UDP 123 is allowed | Reported | Aroha Ngata (relaying IT), 2026-11-23 01:40 UTC |
| Vat 3 went over 7°C again at about 01:00 AWST Sunday 22 Nov (21 Nov 17:00 UTC), no SMS; over the limit about 50 minutes before the hourly check caught it; 18,000 litres dumped | Reported | Aroha Ngata, 2026-11-23 01:40 UTC |
| After forced HTTPS sync, GW-01 and GW-02 clock offset under 1 s; GW-03 "TIME_SET_REJECTED: RTC write error", still +11 min 05 s | Verified (Hannah Odum, TernCloud command results, 2026-11-23 02:35 UTC) | Hannah Odum internal note, 2026-11-23 02:40 UTC |
| After the sync, vats 1 and 2 sent the SMS within a minute; vat 3 still nothing | Reported | Aroha Ngata, 2026-11-23 03:05 UTC |
| GW-03 rejected a second clock write and is still about +11 min after a reboot; GW-01 and GW-02 still under 1 s offset; NTP still failing on all three | Verified (Hannah Odum, TernCloud, 2026-11-24 05:15 to 05:20 UTC) | Hannah Odum internal note, 2026-11-24 05:20 UTC |
| GW-03 has a hardware (real-time clock) fault | Suspected | Hannah Odum, 2026-11-24 05:40 UTC |
| GW-01 and GW-02 may drift again because NTP is still failing | Suspected | Hannah Odum internal note, 2026-11-24 05:20 UTC |

## What has been tried
| Action | By | When | Result | Label |
| --- | --- | --- | --- | --- |
| Alarm test on all nine vats | Aroha Ngata (customer) | 19 Nov afternoon AWST (reported 2026-11-19 07:50 UTC) | Vats 4 to 9 sent SMS within a minute; vats 1 to 3 sent nothing | Reported |
| Hourly manual dashboard checks by night staff (customer's interim workaround) | Customer night staff | From 19 Nov | Caught the Sunday 22 Nov vat 3 excursion only after about 50 minutes; customer says staff cannot keep doing them | Reported |
| Review of alarm rule configuration in TernCloud | Hannah Odum (Tier 1) | 2026-11-20 01:05 UTC | Same template and recipients on vats 1 to 9; configuration does not explain the difference | Verified (Hannah Odum, 2026-11-20 01:05 UTC) |
| Diagnostic bundles from GW-01, 02, 03 requested, supplied and analysed | Hannah Odum; bundles downloaded by Aroha Ngata | Requested 2026-11-20 01:10 UTC; supplied 05:40 UTC; analysed 07:15 UTC | TS_FUTURE rule skips, clocks 8 to 11 min fast, NTP timeouts since 12 Nov, all three on VLAN 30 | Verified (Hannah Odum, 2026-11-20 07:15 UTC) |
| Check of outbound UDP 123 from VLAN 30 | Customer IT (relayed by Aroha Ngata) | Reported 2026-11-23 01:40 UTC | Nothing changed on VLAN 30; UDP 123 allowed | Reported |
| "Force time sync (HTTPS)" to GW-01, 02, 03 | Hannah Odum | 2026-11-23 02:35 UTC | GW-01 and GW-02 OK, offset under 1 s; GW-03 "TIME_SET_REJECTED: RTC write error", still +11 min 05 s | Verified (Hannah Odum, 2026-11-23 02:40 UTC) |
| Alarm test on vats 1 to 3 after the sync | Aroha Ngata (customer) | Reported 2026-11-23 03:05 UTC | Vats 1 and 2 sent SMS within a minute; vat 3 nothing | Reported |
| Second "Force time sync (HTTPS)" to GW-03 | Hannah Odum | 2026-11-24 05:15 UTC | Same "TIME_SET_REJECTED: RTC write error" | Verified (Hannah Odum, 2026-11-24 05:20 UTC) |
| Remote reboot of GW-03 from TernCloud (customer agreed by phone at 05:10 UTC) | Hannah Odum | 2026-11-24 05:17 UTC; back online 05:19 UTC | Clock still about +11 min | Verified (Hannah Odum, 2026-11-24 05:20 UTC) |

## Commitments to the customer
| Commitment (quoted) | Made by (name, role) | When | Due | Status |
| --- | --- | --- | --- | --- |
| "I'd like to look at the gateways themselves." | Hannah Odum, Support Agent Tier 1 | 2026-11-20 01:05 UTC | No date given | Kept (bundles requested and analysed 2026-11-20) |
| "I've passed your request to Joel Brandt, your account manager." | Hannah Odum, Support Agent Tier 1 | 2026-11-23 02:20 UTC | No date given | Kept as stated; no response from Joel Brandt is recorded in the thread |
| "Next, I'm going to send a command from TernCloud that sets the clock on GW-01 to 03 over HTTPS, which avoids the NTP port." | Hannah Odum, Support Agent Tier 1 | 2026-11-23 02:20 UTC | No date given | Kept (sent 2026-11-23 02:35 UTC) |
| "I'm escalating this to our Field Systems Engineering team now." | Hannah Odum, Support Agent Tier 1 | 2026-11-24 05:40 UTC | "now" | Kept (escalated 2026-11-24 06:00 UTC) |
| "You'll get an update from us by 17:30 AWST today (09:30 UTC)." | Hannah Odum, Support Agent Tier 1 | 2026-11-24 05:40 UTC | 2026-11-24 09:30 UTC (17:30 AWST, "today") | Outstanding; owned by Tier 2 from escalation (policy 5.3) |

Claimed by the customer but not found in the thread: None. (The customer's request to have the cost of the milk covered is a request, not a claimed promise; no offer has been made.)

## Service level
- Tier: Business (account record, support plan)
- Priority: P2, recorded 2026-11-23 02:15 UTC by Hannah Odum (was P3 at creation); reason recorded: "Missed alarm caused product loss; hourly manual checks not a practical workaround (clause 2.2)."
- Timestamps: thread is in UTC throughout; business hours are 08:30 to 17:30 AWST, 00:30 to 09:30 UTC (policy 1.1, 1.2).
- Clock: started at ticket creation 2026-11-19 07:50 UTC (Thu 15:50 AWST, inside business hours) (policy 4.1). Paused while Pending customer, 2026-11-20 01:10 to 05:40 UTC, 4 h 30 min of business time excluded (policy 4.2). Business time counted: Thu 19 Nov 1 h 40 min; Fri 20 Nov 4 h 30 min; Mon 23 Nov 9 h; Tue 24 Nov 08:30 to 14:00 AWST 5 h 30 min; total 20 h 40 min as of 2026-11-24 06:00 UTC.
- First response (policy 3.1): 9 business hours at P3 at the time, 4 business hours at P2; first contact 2026-11-20 01:05 UTC after 2 h 15 min of business time. Met under either target (policy 1.4, 3.1).
- Resolution (policy 3.1, 4.3): 27 business hours for Business P2, counted from creation excluding paused time. Due Wed 25 Nov 2026 11:20 AWST (03:20 UTC). Status: at risk, 6 h 20 min remaining, below 25% of the target (6 h 45 min) since 2026-11-24 05:35 UTC (policy 4.4).
- Customer updates (policy 7.1): P2 requires at least one update each business day. Updates sent Mon 23 Nov (02:20 UTC) and Tue 24 Nov (05:40 UTC): met to date. Next required during business day Wed 25 Nov.
- Escalation (policy 5.2): the ticket was an at-risk P2 when escalated at 2026-11-24 06:00 UTC, so the Support Team Lead must be notified at escalation.
- Status as of: 2026-11-24 06:00 UTC, the latest timestamp in the thread.

## Recommended next action
Field Systems Engineering should restore alarming on vat 3 before 2026-11-25 03:20 UTC by dealing with GW-03 as a likely real-time clock hardware fault, for example by arranging a replacement G4-E gateway for vat 3, and say so in the update promised by 2026-11-24 09:30 UTC. The evidence is that the same HTTPS time sync fixed GW-01 and GW-02 but GW-03 rejected the clock write twice and after a reboot. If a Tier 2 diagnostic shows GW-03 can accept a clock write by another method, the hardware theory is wrong and the plan changes to correcting its clock in place.

## Open questions
- Deadline conflict: Hannah Odum's internal note (2026-11-24 01:30 UTC) put the P2 resolution due at Thu 26 Nov 10:15 AWST by counting from the priority change and called it "Plenty of time". Policy 4.3 counts the new target from ticket creation excluding paused time, which gives Wed 25 Nov 11:20 AWST (03:20 UTC), and the ticket is already at risk. Tier 2 should work to the policy figure.
- Support Team Lead notification: policy 5.2 requires it for an at-risk P2 at escalation. The thread does not record it. Confirm it was done, or do it now.
- Compensation: the customer asked for the cost of 18,000 litres of milk to be covered (Aroha Ngata, 2026-11-23 01:40 UTC). Only Joel Brandt (Account Manager) or the Head of Customer Support may offer it, in writing on the ticket or account record (policy 6.3); no response from Joel Brandt is recorded. Tier 2 must not promise it (policy 6.2). Relevant context for him: on 2026-11-20 07:20 UTC Tier 1 told the customer "No rush before Monday; the hourly checks cover you over the weekend.", and the loss happened on Sunday.
- NTP root cause unknown: customer IT says UDP 123 is allowed from VLAN 30 and nothing changed, but NTP to pool.terncloud.net:123 has failed on GW-01 to 03 since 12 Nov. What changed on 12 Nov is not established. Peter Dunn (IT Coordinator, network contact in the account record) is the contact for a network-side check.
- Ticket resolution scope: policy 1.5 requires every fault on the ticket to be resolved. Not determined whether the ongoing NTP failure on GW-01 and GW-02 (offsets correct now, but they may drift) counts as an unresolved fault, or whether the HTTPS sync is an accepted workaround for them.
- Harvey depot gateways DEP-GW-01 and DEP-GW-02 are not mentioned in the thread; whether they share the NTP failure is not checked.
- The first missed alarm's date ("Tuesday night") was not given by the customer; 17 Nov is inferred from the ticket date.
- Public holidays: the policy excludes WA public holidays from business hours but does not list them. The deadline above assumes none fall on 19 to 25 Nov 2026.
- First-response target after a priority change: policy 4.3 covers only the resolution target. Not material here, since first response was met under both P3 and P2.
