# Escalation handoff: TRN-77391 Vat 3 high-temperature SMS alarm still not firing; GW-03 rejects clock set

**Customer:** Kestrel Dairy Co-operative (KDC-0418), Business support plan | **Priority:** P2 (set by Hannah Odum, Tier 1, 2026-11-23 02:15 UTC; was P3 at creation)
**Service level:** at risk, next deadline 2026-11-25 03:20 UTC / 11:20 AWST (resolution; 6 h 20 min business time remaining at reference time)
**Open commitments:** 1, earliest due 2026-11-24 09:30 UTC / 17:30 AWST (3 h 30 min after reference time)

## Problem as currently understood
Since 12 Nov the alarm rule engine on VAT-GW-01, 02 and 03 has skipped every evaluation ("RULE_EVAL_SKIPPED reason=TS_FUTURE"), while those gateways' clocks ran 8 to 11 minutes fast and their NTP sync to pool.terncloud.net:123 timed out (Verified, Hannah Odum, diagnostic bundles). A forced time sync over HTTPS brought GW-01 and GW-02 to under 1 s offset, and the customer reports vats 1 and 2 now send the SMS; GW-03 rejects every clock set with "TIME_SET_REJECTED: RTC write error", including after a remote reboot, and is still about 11 minutes fast (Verified, Hannah Odum), so vat 3 has no working SMS alarm (Reported, customer test). NTP is still failing on all three gateways (Verified), so GW-01 and GW-02 may drift again (Hypothesis, Hannah Odum); Hannah's hypothesis that UDP 123 is blocked on VLAN 30 is contradicted by the customer's IT, who report UDP 123 is allowed (Reported). Hannah's working hypothesis for GW-03 is a hardware fault (Hypothesis), and the customer reports a second missed vat 3 alarm that led to 18,000 litres of milk being dumped (Reported).

| Fact | Tag | Source |
|---|---|---|
| On Tuesday night vat 3 at Brunswick was above 7°C for about 40 minutes and nobody received the high-temperature SMS | Reported | Aroha Ngata, 2026-11-19 07:50 UTC |
| The TernCloud dashboard shows the vat 3 reading went over the limit | Reported | Aroha Ngata, 2026-11-19 07:50 UTC |
| Customer test on all nine vats: vats 4 to 9 sent the SMS within a minute; vats 1, 2 and 3 sent nothing | Reported | Aroha Ngata, 2026-11-19 07:50 UTC |
| Brunswick has VAT-GW-01 to VAT-GW-09, model G4-E (Ethernet), one per milk vat | Verified (account record) | account.md, "Sites and gateways" |
| Night staff are checking the dashboard every hour until fixed | Reported | Aroha Ngata, 2026-11-19 07:50 UTC |
| Vats 1 to 9 all use the same rule template ("Vat high temp, above 7°C for 5 min") with the same SMS recipients | Verified (Hannah Odum, TernCloud alarm rules) | Hannah Odum, 2026-11-20 01:05 UTC |
| Rule engine on GW-01, 02 and 03 logs "RULE_EVAL_SKIPPED reason=TS_FUTURE" at every evaluation since 12 Nov | Verified (Hannah Odum, diagnostic bundles) | Internal note, 2026-11-20 07:15 UTC |
| Gateway clocks ahead of sensor timestamps: GW-01 +9 min 12 s, GW-02 +8 min 40 s, GW-03 +11 min 03 s | Verified (Hannah Odum, diagnostic bundles) | Internal note, 2026-11-20 07:15 UTC |
| With the clock that far ahead the 5-minute window never fills, so the rule is skipped | Hypothesis (Hannah Odum); consistent with vats 1 and 2 alarming after their clocks were fixed | Internal note, 2026-11-20 07:15 UTC; Aroha Ngata, 2026-11-23 03:05 UTC |
| NTP log on GW-01, 02 and 03: "NTP sync failed: timeout (pool.terncloud.net:123)", repeated since 12 Nov | Verified (Hannah Odum, diagnostic bundles) | Internal note, 2026-11-20 07:15 UTC |
| GW-01 to 03 are on VLAN 30 | Verified (Hannah Odum, diagnostic bundles) | Internal note, 2026-11-20 07:15 UTC |
| TernCloud shows GW-04 to 09 with last time sync OK | Verified (Hannah Odum, TernCloud) | Internal note, 2026-11-20 07:15 UTC |
| UDP 123 is blocked for VLAN 30 ("Not confirmed") | Hypothesis (Hannah Odum) | Internal note, 2026-11-20 07:15 UTC |
| Customer IT says nothing has changed on VLAN 30 and outbound UDP 123 is allowed | Reported (customer's IT, via Aroha Ngata) | Aroha Ngata, 2026-11-23 01:40 UTC |
| Sunday night at about 01:00 local time vat 3 went over 7°C again, no SMS; caught on the hourly check after about 50 minutes over the limit; 18,000 litres dumped | Reported | Aroha Ngata, 2026-11-23 01:40 UTC |
| Night staff can't keep doing hourly checks, and they aren't enough | Reported | Aroha Ngata, 2026-11-23 01:40 UTC |
| Priority raised P3 to P2: "Missed alarm caused product loss; hourly manual checks not a practical workaround (clause 2.2)" | Verified (ticket event) | Event, 2026-11-23 02:15 UTC |
| Force time sync (HTTPS) at 02:35: GW-01 and GW-02 OK, offset under 1 s; GW-03 "TIME_SET_REJECTED: RTC write error", clock still +11 min 05 s | Verified (Hannah Odum, TernCloud command results) | Internal note, 2026-11-23 02:40 UTC |
| After the sync, vats 1 and 2 sent the SMS within a minute; vat 3 still nothing | Reported | Aroha Ngata, 2026-11-23 03:05 UTC |
| Second force time sync to GW-03 at 05:15: same "TIME_SET_REJECTED: RTC write error" | Verified (Hannah Odum) | Internal note, 2026-11-24 05:20 UTC |
| GW-03 rebooted from TernCloud at 05:17, back online 05:19, clock still +11 min | Verified (Hannah Odum) | Internal note, 2026-11-24 05:20 UTC |
| GW-01 and GW-02 still in sync (offset under 1 s); NTP still failing on all three | Verified (Hannah Odum) | Internal note, 2026-11-24 05:20 UTC |
| GW-01 and GW-02 may drift again | Hypothesis (Hannah Odum) | Internal note, 2026-11-24 05:20 UTC |
| GW-03 refusing to set its clock may be a hardware fault | Hypothesis (Hannah Odum) | Hannah Odum, 2026-11-24 05:40 UTC |

**Open questions:**
- Is GW-03's "RTC write error" a hardware fault (replace the unit) or something that can be cleared remotely? Not tested beyond two sync attempts and one reboot.
- Why does NTP time out from GW-01 to 03 if customer IT reports outbound UDP 123 is allowed from VLAN 30? The port-block hypothesis is contradicted but nothing else has been checked.
- What changed on or about 12 Nov, when both the NTP failures and the skipped rule evaluations began?
- How fast do GW-01 and GW-02 drift without NTP, and at what clock offset does the rule start skipping again? Not determined.
- The two missed vat 3 alarms (Tuesday night and Sunday night) are Reported only; support has not confirmed them in TernCloud data.
- Are the Harvey depot gateways (DEP-GW-01, DEP-GW-02) affected? The thread does not cover them.
- The thread records no Support Team Lead notification at escalation (see Service level, clause 5.2).
- The thread records no response from Joel Brandt on the customer's request to cover the cost of the milk.

## What has been tried
| Action | By | When | Result |
|---|---|---|---|
| Alarm test on all nine vats | Aroha Ngata (customer) | 2026-11-19 afternoon, local time (exact time not recorded) | Vats 4 to 9 SMS within a minute; vats 1 to 3 nothing (Reported) |
| Checked TernCloud alarm rules for vats 1 to 9 | Hannah Odum | 2026-11-20 01:05 UTC | Same template and same SMS recipients on all nine; configuration doesn't explain the difference |
| Requested diagnostic bundles from GW-01, 02, 03 | Hannah Odum | 2026-11-20 01:10 UTC | Customer attached all three at 05:40 UTC |
| Analysed diagnostic bundles | Hannah Odum | 2026-11-20 07:15 UTC | RULE_EVAL_SKIPPED reason=TS_FUTURE since 12 Nov; clocks 8 to 11 min fast; NTP timeouts to pool.terncloud.net:123 since 12 Nov; all three on VLAN 30 |
| Asked customer IT to check outbound UDP 123 from VLAN 30 | Hannah Odum (request); customer IT (check) | Requested 2026-11-20 07:20 UTC; answered 2026-11-23 01:40 UTC | Nothing changed on VLAN 30; outbound UDP 123 allowed (Reported) |
| "Force time sync (HTTPS)" to GW-01, 02, 03 | Hannah Odum | 2026-11-23 02:35 UTC | GW-01, 02 OK, offset under 1 s; GW-03 "TIME_SET_REJECTED: RTC write error", still +11 min 05 s |
| Alarm test on vats 1 to 3 | Aroha Ngata (customer) | Reported 2026-11-23 03:05 UTC | Vats 1 and 2 SMS within a minute; vat 3 nothing (Reported) |
| Second "Force time sync (HTTPS)" to GW-03 | Hannah Odum | 2026-11-24 05:15 UTC | Same "TIME_SET_REJECTED: RTC write error" |
| Remote reboot of GW-03 from TernCloud (customer agreed by phone at 05:10) | Hannah Odum | 2026-11-24 05:17 UTC | Back online 05:19; clock still +11 min |
| Alarm test on vat 3 after the reboot | Not done | n/a | Not recorded in the thread |

## Commitments to the customer
| Commitment (quoted) | Made by | When | Status |
|---|---|---|---|
| "I'd like to look at the gateways themselves." | Hannah Odum | 2026-11-20 01:05 UTC | Met: bundles requested 01:10 and analysed 07:15 UTC |
| "I've raised the ticket to P2." | Hannah Odum | 2026-11-23 02:20 UTC | Met: priority event 02:15 UTC |
| "I'm not able to offer compensation myself, so I've passed your request to Joel Brandt, your account manager." (commitment is to pass the request on, not to compensate) | Hannah Odum | 2026-11-23 02:20 UTC | Met as stated by Hannah; no record on the ticket of the handover or of any reply from Joel Brandt |
| "I'm going to send a command from TernCloud that sets the clock on GW-01 to 03 over HTTPS, which avoids the NTP port." | Hannah Odum | 2026-11-23 02:20 UTC | Met: sent 02:35 UTC (internal note 02:40) |
| Remote reboot of GW-03 (agreed by phone; wording not recorded, paraphrased in internal note: "Aroha agreed by phone at 05:10 to a remote reboot of GW-03") | Hannah Odum | 2026-11-24 05:10 UTC | Met: rebooted 05:17 UTC |
| "I'm escalating this to our Field Systems Engineering team now." | Hannah Odum | 2026-11-24 05:40 UTC | Met: escalated to Tier 2 at 06:00 UTC |
| "You'll get an update from us by 17:30 AWST today (09:30 UTC)." | Hannah Odum | 2026-11-24 05:40 UTC | Open, due 2026-11-24 09:30 UTC. Under policy 5.3 Tier 2 now owns it |

Note: Hannah's message of 2026-11-20 07:20 UTC said "No rush before Monday; the hourly checks cover you over the weekend." This was an assurance, not a commitment, but the customer reports a missed alarm and product loss that weekend.

**Requested, not committed:**
- "We'd like the cost of that milk covered." (Aroha Ngata, 2026-11-23 01:40 UTC). Support committed only to pass the request to Joel Brandt. Policy 6.2: "Support agents must not promise a fix date, a service credit, a refund or compensation." Policy 6.3: "Only the Account Manager named in the account record, or the Head of Customer Support, may offer a service credit, refund or compensation." No offer is recorded; account record shows "Open credits: None".

## Service level
Measured at 2026-11-24 06:00 UTC (14:00 AWST, Tuesday), the escalation event and last entry in the thread. Readings used for ambiguous terms:
- WA public holidays: policy 1.1 excludes "Western Australian public holidays" but does not list them; the calculation assumes none fall between 19 and 25 Nov 2026. Re-check if one does.
- First response target: policy 4.3 changes only "the resolution target" on a priority change, so first response is measured against the priority at creation (P3). It is met under the P2 target too.
- Update cadence "at least once each business day" (7.1): read as at least one customer-facing update inside each business day's hours (00:30 to 09:30 UTC), from the business day the ticket became P2.
- Dates: 2026-11-19 is a Thursday; 21 and 22 Nov are a weekend.

Business hours per policy 1.2: "08:30 to 17:30 AWST is 00:30 to 09:30 UTC on the same date" (9 business hours per weekday).
Paused time per policy 4.2: status "Pending customer" from 2026-11-20 01:10 UTC to 05:40 UTC = 4 h 30 min, all inside business hours.

| Target (policy quote) | Clock start | Deadline (arithmetic) | Status |
|---|---|---|---|
| First response, Business P3: "9 business hours" (3.1); "First response means the first contact with the customer by a support agent" (1.4) | 2026-11-19 07:50 UTC, ticket created inside business hours (4.1: "The clock starts when the ticket is created") | Thu 07:50 to 09:30 = 1 h 40 min; remaining 7 h 20 min from Fri 00:30 = Fri 2026-11-20 07:50 UTC. Actual first response 2026-11-20 01:05 UTC = 1 h 40 min + 35 min = 2 h 15 min elapsed (also under the P2 "4 business hours") | Met |
| Resolution, Business P2: "27 business hours" (3.1); "If the priority changes, the resolution target becomes the target for the new priority, counted from ticket creation and excluding paused time" (4.3) | 2026-11-19 07:50 UTC | Thu 19 Nov 07:50 to 09:30 = 1:40. Fri 20 Nov 9:00 minus 4:30 paused = 4:30 (total 6:10). Mon 23 Nov 9:00 (total 15:10). Tue 24 Nov 9:00 (total 24:10). Wed 25 Nov: 27:00 minus 24:10 = 2:50, so 00:30 + 2:50 = **2026-11-25 03:20 UTC (11:20 AWST)**. At reference time: elapsed 15:10 + Tue 00:30 to 06:00 (5:30) = 20:40; remaining 6:20 | **At risk**: 4.4 "'at risk' if less than 25% of its resolution target remains"; 25% of 27 h = 6 h 45 min; 6 h 20 min remains. Crossed into at risk at 2026-11-24 05:35 UTC (elapsed 20:15) |
| Updates, P2: "at least once each business day" (7.1); P3: "when there is news" | Policy does not state when the update clock starts; reading: business day of the P2 change, Mon 2026-11-23 | Mon 23 Nov: update at 02:20 UTC (met). Tue 24 Nov: update at 05:40 UTC (met). Next: Wed 25 Nov by 09:30 UTC (end of business day) | Within target |

Pauses: "The clock is paused only while the ticket status is 'Pending customer'. It resumes when the status leaves 'Pending customer'. Paused time does not count toward any target." (4.2)

Correction to Tier 1's calculation: Hannah Odum's internal note of 2026-11-24 01:30 UTC computed the resolution due time as "Thu 26 Nov 10:15 AWST", counting 27 business hours from the P2 change. Policy 4.3 counts the new target "from ticket creation and excluding paused time", which gives Wed 25 Nov 11:20 AWST (03:20 UTC), about one business day earlier.

Escalation rule: policy 5.2 says "When a P1 ticket, or an at-risk P2 ticket, is escalated, the Support Team Lead must be notified at escalation." The ticket was at risk at escalation (06:00 UTC; at risk since 05:35 UTC). The thread records no Support Team Lead notification.

Resolution definition: "Tern has provided a fix or a workaround that restores the affected function and the ticket status has been set to Resolved." (1.5). Restoring vat 3's alarm is required; per 1.5 "A ticket that reports more than one fault is resolved only when every fault on it is resolved."

## Recommended next action
Tier 2 (Field Systems Engineering) should determine whether GW-03's "TIME_SET_REJECTED: RTC write error" is a hardware fault, using a fresh GW-03 diagnostic bundle taken after the 05:17 UTC reboot (Maintenance > Diagnostics > Download bundle, as Aroha did before), and from that decide between a remote fix and replacing the G4-E unit. Owner: the assigned Field Systems Engineering engineer (name not recorded on the ticket). By 2026-11-24 09:30 UTC (17:30 AWST), so the result goes into the update promised to Aroha for that time. Because vat 3 is the only vat with no working SMS alarm (Reported, 2026-11-23 03:05 UTC), two retries and a reboot have not cleared the error (Verified, 2026-11-24 05:20 UTC), and the resolution deadline is 2026-11-25 03:20 UTC with 6 h 20 min of business time left, the ticket is already at risk. Also confirm the Support Team Lead was notified (policy 5.2). The VLAN 30 NTP failure can come second: GW-01 and GW-02 are in sync for now (Verified). Peter Dunn, IT Coordinator, is the customer's network contact in the account record.
