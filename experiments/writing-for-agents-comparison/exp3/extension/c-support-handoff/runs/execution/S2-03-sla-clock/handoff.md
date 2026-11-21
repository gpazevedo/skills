Clarifying question: What is the current date, time and time zone? The thread does not say, and the service-level statuses below depend on it. Without an answer, every status below is measured at the last event in the thread, 2026-11-24 06:00 UTC (14:00 AWST, Tuesday), when the ticket was escalated.

# Escalation handoff: TRN-77391 Vat 3 high-temperature SMS alarm still not firing because GW-03's clock cannot be set; NTP still failing on GW-01 to 03

**Customer:** Kestrel Dairy Co-operative, account KDC-0418, Support plan: Business (account record, "Support plan")   **Severity/priority:** P2 (event 2026-11-23 02:15 UTC, Priority P3 → P2 by Hannah Odum, reason "Missed alarm caused product loss; hourly manual checks not a practical workaround (clause 2.2)")
**Most urgent deadline:** Customer update promised "by 17:30 AWST today (09:30 UTC)", i.e. 2026-11-24 09:30 UTC (Hannah Odum, 2026-11-24 05:40 UTC). Tier 2 now owns it (policy 5.3). After that: P2 resolution target due 2026-11-25 03:20 UTC (11:20 AWST Wed), and the ticket is already "at risk" (see Service-level status).

## Problem as currently understood
Gateways VAT-GW-01 to 03 at the Brunswick plant cannot reach the NTP server, their clocks ran 8 to 11 minutes fast, and their rule engines skipped every alarm evaluation ("TS_FUTURE"), so vats 1 to 3 sent no high-temperature SMS. A forced HTTPS time sync fixed GW-01 and GW-02, but GW-03 rejects any clock write ("RTC write error"), so vat 3 still has no working alarm; it has already caused a reported loss of 18,000 litres. The NTP failure on all three is unexplained (customer IT says UDP 123 is allowed), so GW-01 and GW-02 may drift and fail again.

| Fact | Status | How established / cite |
|---|---|---|
| On Tuesday night (17 Nov) vat 3 went above 7°C for about 40 minutes and nobody received the high-temperature SMS | Reported | Aroha Ngata, 2026-11-19 07:50 UTC |
| The TernCloud dashboard showed the reading over the limit | Reported | Aroha Ngata, 2026-11-19 07:50 UTC (support did not record checking the dashboard) |
| Customer test on 19 Nov: vats 4 to 9 sent the SMS within a minute; vats 1, 2 and 3 sent nothing | Reported | Aroha Ngata, 2026-11-19 07:50 UTC |
| Each vat has its own gateway, VAT-GW-01 to VAT-GW-09, model G4-E (Ethernet), at the Brunswick plant | Verified | Account record, "Sites and gateways"; also Aroha Ngata, 2026-11-19 07:50 UTC |
| Vats 1 to 9 use the same alarm rule template ("Vat high temp, above 7°C for 5 min") and the same SMS recipients | Verified | Hannah Odum checked the alarm rules in TernCloud, 2026-11-20 01:05 UTC |
| Rule engine on GW-01, 02 and 03 logs "RULE_EVAL_SKIPPED reason=TS_FUTURE" at every evaluation since 12 Nov | Verified | Diagnostic bundles read by Hannah Odum, internal note 2026-11-20 07:15 UTC |
| Gateway clocks ahead of sensor timestamps: GW-01 +9 min 12 s, GW-02 +8 min 40 s, GW-03 +11 min 03 s | Verified | Diagnostic bundles, internal note 2026-11-20 07:15 UTC |
| NTP log on all three: "NTP sync failed: timeout (pool.terncloud.net:123)", repeated since 12 Nov | Verified | Diagnostic bundles, internal note 2026-11-20 07:15 UTC |
| GW-01 to 03 are on VLAN 30 | Verified | Diagnostic bundles, internal note 2026-11-20 07:15 UTC |
| GW-04 to 09 show their last time sync OK | Verified | TernCloud, internal note 2026-11-20 07:15 UTC |
| The fast clocks stop the 5-minute rule window from filling, so the rule is skipped and no alarm is sent | Hypothesis (strongly supported) | Hannah Odum, internal note 2026-11-20 07:15 UTC. Supporting test: after the clocks on GW-01 and 02 were set, the customer reports vats 1 and 2 alarmed (Aroha Ngata, 2026-11-23 03:05 UTC); that test result is customer-reported |
| Outbound UDP 123 is blocked for VLAN 30 | Hypothesis (untested by support; contradicted by customer) | Hannah Odum, internal note 2026-11-20 07:15 UTC: "Possible cause ... Not confirmed." |
| Customer IT says nothing has changed on VLAN 30 and outbound UDP 123 is allowed | Reported | Aroha Ngata, 2026-11-23 01:40 UTC (how IT checked is not recorded) |
| On Sunday night vat 3 went over 7°C again at about 01:00 local time, for about 50 minutes, with no SMS; the night operator caught it on the hourly check | Reported | Aroha Ngata, 2026-11-23 01:40 UTC |
| The customer dumped 18,000 litres of milk and wants the cost covered | Reported | Aroha Ngata, 2026-11-23 01:40 UTC |
| Hourly manual dashboard checks are the customer's workaround; night staff cannot keep doing them and they are not enough | Reported | Aroha Ngata, 2026-11-19 07:50 UTC and 2026-11-23 01:40 UTC |
| Force time sync (HTTPS) at 02:35 on 23 Nov: GW-01 and GW-02 OK, offset under 1 s; GW-03 "TIME_SET_REJECTED: RTC write error", clock still +11 min 05 s | Verified | TernCloud command results, Hannah Odum internal note 2026-11-23 02:40 UTC |
| After the sync, vats 1 and 2 sent the SMS within a minute; vat 3 still nothing | Reported | Aroha Ngata, 2026-11-23 03:05 UTC |
| Second force sync to GW-03 on 24 Nov 05:15 gave the same "TIME_SET_REJECTED: RTC write error"; after a reboot (05:17, online 05:19) the clock is still +11 min | Verified | TernCloud, Hannah Odum internal note 2026-11-24 05:20 UTC |
| As of 24 Nov 05:20 UTC, GW-01 and GW-02 still in sync (offset under 1 s); NTP still failing on all three | Verified | Hannah Odum internal note 2026-11-24 05:20 UTC |
| GW-01 and GW-02 may drift again because NTP still fails | Hypothesis | Hannah Odum internal note 2026-11-24 05:20 UTC |
| GW-03 has a hardware fault (the gateway refuses to set its clock) | Hypothesis | Hannah Odum, 2026-11-24 05:40 UTC: "may be a hardware fault" |
| Customer also has Harvey depot gateways DEP-GW-01 and DEP-GW-02 (G4-E); the thread does not mention them | Verified (existence only) | Account record, "Sites and gateways" |

**Open disagreements:**
- Support's hypothesis that UDP 123 is blocked on VLAN 30 (internal note 2026-11-20 07:15 UTC) against the customer's IT, who say UDP 123 is allowed and nothing changed (Aroha Ngata, 2026-11-23 01:40 UTC). The bundles still show NTP timeouts on all three gateways (internal note 2026-11-24 05:20 UTC), so the cause of the NTP failure is unresolved.
- Support told the customer "the hourly checks cover you over the weekend" (Hannah Odum, 2026-11-20 07:20 UTC); the customer reports the hourly check let vat 3 run about 50 minutes over the limit and lost 18,000 litres (Aroha Ngata, 2026-11-23 01:40 UTC).

## What has been tried
| When | Who | Action | Result | Cite |
|---|---|---|---|---|
| 2026-11-19, afternoon local, before 07:50 UTC | Customer (Aroha Ngata) | Alarm test on all nine vats | Vats 4 to 9 SMS within a minute; vats 1 to 3 nothing | Aroha Ngata, 2026-11-19 07:50 UTC |
| From 2026-11-19 | Customer night staff | Hourly dashboard checks as a workaround | Missed about 50 minutes of over-limit temperature on vat 3 on Sunday night; 18,000 litres dumped | Aroha Ngata, 2026-11-19 07:50 UTC and 2026-11-23 01:40 UTC |
| 2026-11-20 01:05 UTC | Hannah Odum (Tier 1) | Checked alarm rules for vats 1 to 9 in TernCloud | Same template and recipients on all nine; configuration does not explain the difference | Hannah Odum, 2026-11-20 01:05 UTC |
| 2026-11-20 01:10 to 05:40 UTC | Hannah Odum requested; customer supplied | Diagnostic bundles from GW-01, 02 and 03 | Bundles attached for all three | Hannah Odum, 2026-11-20 01:10 UTC; Aroha Ngata, 2026-11-20 05:40 UTC |
| 2026-11-20 07:15 UTC | Hannah Odum | Analysed bundles; compared with TernCloud sync status of GW-04 to 09 | TS_FUTURE rule skips, clocks 8 to 11 min fast, NTP timeouts since 12 Nov, GW-01 to 03 on VLAN 30; GW-04 to 09 sync OK | Internal note 2026-11-20 07:15 UTC |
| 2026-11-20 07:20 UTC to 2026-11-23 01:40 UTC | Hannah Odum asked; customer IT checked | Check whether outbound UDP 123 is allowed from VLAN 30 | IT says nothing changed and UDP 123 is allowed (method not recorded) | Hannah Odum, 2026-11-20 07:20 UTC; Aroha Ngata, 2026-11-23 01:40 UTC |
| 2026-11-23 02:15 UTC | Hannah Odum | Raised priority P3 → P2 | Recorded on ticket | Event 2026-11-23 02:15 UTC |
| 2026-11-23 02:20 UTC | Hannah Odum | Passed compensation request to Joel Brandt (account manager) | Not recorded (no response from Joel Brandt in the thread) | Hannah Odum, 2026-11-23 02:20 UTC |
| 2026-11-23 02:35 UTC | Hannah Odum | "Force time sync (HTTPS)" to GW-01, 02, 03 | GW-01, GW-02 OK, offset under 1 s; GW-03 "TIME_SET_REJECTED: RTC write error", still +11 min 05 s | Internal note 2026-11-23 02:40 UTC |
| 2026-11-23, before 03:05 UTC | Customer (Aroha Ngata) | Alarm test on vats 1 to 3 | Vats 1 and 2 SMS within a minute; vat 3 nothing | Aroha Ngata, 2026-11-23 03:05 UTC |
| 2026-11-24 05:15 UTC | Hannah Odum | Second "Force time sync (HTTPS)" to GW-03 (customer agreed by phone at 05:10) | Same "TIME_SET_REJECTED: RTC write error" | Internal note 2026-11-24 05:20 UTC |
| 2026-11-24 05:17 UTC | Hannah Odum | Remote reboot of GW-03 from TernCloud | Back online 05:19; clock still +11 min | Internal note 2026-11-24 05:20 UTC |
| 2026-11-24 06:00 UTC | Hannah Odum | Escalated to Tier 2 (Field Systems Engineering) | Status Open → Escalated, P2 | Event 2026-11-24 06:00 UTC |

## Commitments to the customer
| Commitment (verbatim) | Made by (role) | When / cite | Deadline | Kept / Open / Missed |
|---|---|---|---|---|
| "I'd like to look at the gateways themselves." | Hannah Odum (Support Agent, Tier 1) | 2026-11-20 01:05 UTC | None set | Kept (bundles requested 01:10 and analysed 07:15 on 20 Nov) |
| "No rush before Monday; the hourly checks cover you over the weekend." | Hannah Odum (Tier 1) | 2026-11-20 07:20 UTC | Weekend of 21 to 22 Nov | Missed (assurance of an outcome; customer reports the hourly check missed about 50 minutes and 18,000 litres were dumped, Aroha Ngata 2026-11-23 01:40 UTC) |
| "Next, I'm going to send a command from TernCloud that sets the clock on GW-01 to 03 over HTTPS, which avoids the NTP port." | Hannah Odum (Tier 1) | 2026-11-23 02:20 UTC | None set | Kept (sent 02:35, internal note 2026-11-23 02:40 UTC; GW-03 rejected it) |
| "I'm escalating this to our Field Systems Engineering team now." | Hannah Odum (Tier 1) | 2026-11-24 05:40 UTC | "now" | Kept (escalation event 2026-11-24 06:00 UTC) |
| "You'll get an update from us by 17:30 AWST today (09:30 UTC)." | Hannah Odum (Tier 1) | 2026-11-24 05:40 UTC | 2026-11-24 09:30 UTC | Open (Tier 2 owns it: policy 5.3 "From escalation, Tier 2 owns the ticket, including customer updates and commitments already made."; within what 6.1 allows: "Support agents may commit to the time of the next update") |

Related, not a commitment: Hannah Odum told the customer "I'm not able to offer compensation myself, so I've passed your request to Joel Brandt, your account manager." (2026-11-23 02:20 UTC). This is within policy 6.2 and 6.3 ("Only the Account Manager named in the account record, or the Head of Customer Support, may offer a service credit, refund or compensation."). No offer is recorded on the ticket, and the account record shows "Open credits: None".

## Service-level status
Plan: Business (account record). Priority: P3 from creation, P2 since 2026-11-23 02:15 UTC. Business hours: "08:30 to 17:30 Australia/Perth time (AWST, UTC+8, no daylight saving), Monday to Friday, excluding Western Australian public holidays" (1.1), i.e. "00:30 to 09:30 UTC on the same date" (1.2). Pause: "The clock is paused only while the ticket status is "Pending customer"" (4.2); the only pause was 2026-11-20 01:10 to 05:40 UTC (4 h 30 min, all inside business hours). Ticket created Thu 2026-11-19 07:50 UTC (15:50 AWST), inside business hours. The policy lists no public holiday dates; the arithmetic assumes none fall on 19 to 25 Nov.

| Clock | Policy clause (quoted) | Started | Deadline (with arithmetic) | Status |
|---|---|---|---|---|
| First response | 3.1 "Business \| P3 \| 9 business hours" (priority at the time); 1.4 "First response means the first contact with the customer by a support agent" | 2026-11-19 07:50 UTC (ticket created, 4.1) | Due 2026-11-20 07:50 UTC with no pause (Thu 07:50 to 09:30 = 1 h 40 min; remaining 7 h 20 min from Fri 00:30 = 07:50 UTC Fri). Actual first response 2026-11-20 01:05 UTC (Hannah Odum) = 1 h 40 min + 35 min = 2 h 15 min. Also within the P2 value of 4 business hours. | Met |
| Resolution | 3.1 "Business \| P2 \| ... \| 27 business hours"; 4.3 "If the priority changes, the resolution target becomes the target for the new priority, counted from ticket creation and excluding paused time." | 2026-11-19 07:50 UTC (ticket creation, per 4.3) | 2026-11-25 03:20 UTC (11:20 AWST Wed). Thu 19: 07:50 to 09:30 = 1 h 40 min. Fri 20: 9 h minus 4 h 30 min paused = 4 h 30 min (total 6 h 10 min). Sat/Sun: 0. Mon 23: 9 h (15 h 10 min). Tue 24: 9 h (24 h 10 min). Wed 25: remaining 2 h 50 min from 00:30 = 03:20 UTC. | At risk. 4.4: "at risk" if "less than 25% of its resolution target remains". 25% of 27 h = 6 h 45 min, reached at 20 h 15 min elapsed = 2026-11-24 05:35 UTC. At 06:00 UTC, elapsed 20 h 40 min, remaining 6 h 20 min. Breached if unresolved at 2026-11-25 03:20 UTC. |
| Customer update interval | 7.1 "P2: at least once each business day." | 2026-11-23 02:15 UTC (P2 recorded; 2.5 "a priority applies only once recorded on the ticket") | Mon 23 Nov: update sent 02:20 UTC. Tue 24 Nov: update sent 05:40 UTC. Next due by end of business Wed 25 Nov = 2026-11-25 09:30 UTC (the open commitment above is earlier: 2026-11-24 09:30 UTC). | On track (met for 23 and 24 Nov) |

Note on the internal SLA check: Hannah Odum's internal note (2026-11-24 01:30 UTC) gives a due time of "Thu 26 Nov 10:15 AWST", counted 27 business hours from the priority change on Mon 10:15 AWST, and says "Plenty of time." That conflicts with 4.3, which counts from ticket creation; the correct due time is 2026-11-25 03:20 UTC (11:20 AWST Wed). Because the ticket was at risk at escalation (from 05:35 UTC; escalated 06:00 UTC), 5.2 applies: "When a P1 ticket, or an at-risk P2 ticket, is escalated, the Support Team Lead must be notified at escalation." The thread records no such notification.

## Recommended next action
Confirm whether GW-03 has a hardware RTC fault by running Tier 2 diagnostics on its real-time clock, and if it is confirmed, arrange a replacement G4-E for vat 3 that is time-synced over HTTPS before it goes into service.

Evidence: GW-03 rejected two HTTPS time syncs with "TIME_SET_REJECTED: RTC write error" and kept its +11 min offset through a reboot (internal notes 2026-11-23 02:40 and 2026-11-24 05:20 UTC), while the same command fixed GW-01 and GW-02. The hardware fault is still a Hypothesis (Hannah Odum, 2026-11-24 05:40 UTC), so confirming it is the first part of the action. Vat 3 is the only vat still without an alarm and has already had two reported misses, one with product loss.

What the result settles: whether vat 3's alarm needs hardware replacement or a software/firmware fix on GW-03. It does not settle the NTP failure: any gateway on VLAN 30, including a replacement GW-03, will still fail NTP and drift (NTP still failing on all three, 2026-11-24 05:20 UTC). Resolution under 1.5 needs both faults fixed, so the NTP cause (support's VLAN 30 hypothesis against the customer IT report) must be worked in parallel with Peter Dunn, the customer's network contact (account record).

Deadlines it must beat: the customer update promised for 2026-11-24 09:30 UTC (17:30 AWST), then the P2 resolution target at 2026-11-25 03:20 UTC (11:20 AWST).

## Gaps
- Current date and time not supplied; all statuses are measured at 2026-11-24 06:00 UTC. Closed by the user giving the current time.
- Support Team Lead notification required by 5.2 (at-risk P2 escalated) is not recorded. Closed by notifying the Team Lead and recording it on the ticket.
- Compensation request for 18,000 litres: no response from Joel Brandt recorded. Closed by Joel Brandt (or the Head of Customer Support, 6.3) answering in writing on the ticket.
- Cause of NTP failure on VLAN 30 unknown; how customer IT checked UDP 123 not recorded. Closed by a packet capture or NTP test from VLAN 30 with Peter Dunn.
- Harvey depot gateways DEP-GW-01 and DEP-GW-02 (account record) have not been checked for NTP failure or TS_FUTURE skips. Closed by checking their time-sync status in TernCloud.
- The exact time of the Sunday night event ("about 01:00 our time") is ambiguous (Sunday 01:00 or early Monday 01:00 AWST). Closed by the customer or GW-03/TernCloud readings for vat 3.
- Neither missed vat 3 event (Tuesday 17 Nov, Sunday night) has been confirmed by support from TernCloud readings; both are Reported. Closed by pulling vat 3's readings for those nights.
- Policy does not list Western Australian public holiday dates; the resolution arithmetic assumes none on 19 to 25 Nov. Closed by checking the holiday calendar.
