# Handoff: TRN-77391, Kestrel Dairy Co-operative (KDC-0418)

As-of time: 2026-11-24 06:00 UTC (Tue 24 Nov 14:00 AWST). Escalated to Tier 2 (Field Systems Engineering), P2.

## 1. Problem and evidence

**Problem:** High-temperature SMS alarms do not fire for vats 1 to 3 at Brunswick. On VAT-GW-01 to 03 the gateway clocks run 8 to 11 minutes ahead because NTP sync fails, so the 5-minute rule window never fills and the rule is skipped. GW-01 and GW-02 now have correct clocks after a forced HTTPS time sync. GW-03 rejects the clock write ("RTC write error"), so vat 3 still has no working alarm. Vat 3 has had two missed alarms and an 18,000 litre milk dump (reported).

Evidence:

1. Vat 3 went over 7 C for about 40 minutes on Tuesday night (17 Nov) with no SMS. **Reported** (Aroha Ngata, 2026-11-19 07:50). The dashboard showing the reading is the customer's account; support did not record viewing it.
2. Alarm test on all nine vats: vats 4 to 9 sent SMS, vats 1 to 3 did not. **Reported** (Aroha, 2026-11-19 07:50).
3. Vats 1 to 9 use the same rule template ("Vat high temp, above 7°C for 5 min") with the same recipients. **Verified**, TernCloud alarm rules (Hannah Odum, 2026-11-20 01:05).
4. On GW-01, 02 and 03 the rule engine logs "RULE_EVAL_SKIPPED reason=TS_FUTURE" at every evaluation since 12 Nov. Clock offsets were +9 min 12 s, +8 min 40 s and +11 min 03 s. **Verified**, diagnostic bundles (internal note, 2026-11-20 07:15).
5. NTP log on all three: "NTP sync failed: timeout (pool.terncloud.net:123)", since 12 Nov. **Verified**, diagnostic bundles (2026-11-20 07:15).
6. GW-01 to 03 are on VLAN 30. **Verified**, bundles (2026-11-20 07:15). GW-04 to 09 show last time sync OK. **Verified**, TernCloud (same note).
7. GW-01 and GW-02: "Force time sync (HTTPS)" result OK, offset under 1 s. **Verified**, TernCloud command result (2026-11-23 02:40). Still in sync at 2026-11-24 05:20. **Verified**, same source.
8. GW-03: "TIME_SET_REJECTED: RTC write error" on 23 Nov 02:35 and again 24 Nov 05:15. Clock still +11 min 05 s, then still +11 min after reboot at 05:17 (back online 05:19). **Verified**, TernCloud command results (notes 2026-11-23 02:40 and 2026-11-24 05:20).
9. After the forced sync, vats 1 and 2 sent SMS in the test and vat 3 did not. **Reported** (Aroha, 2026-11-23 03:05). No support-side confirmation.
10. Vat 3 went over limit again about 01:00 AWST Mon 23 Nov (Sunday night) for about 50 minutes, with no SMS. 18,000 litres were dumped. **Reported** (Aroha, 2026-11-23 01:40).
11. Hardware fault on GW-03 is suspected. **Reported** as a suspicion by Tier 1 ("may be a hardware fault", 2026-11-24 05:40). Not confirmed.
12. Cause of the NTP failure is unknown. The hypothesis that UDP 123 is blocked on VLAN 30 is "Not confirmed" (internal note, 2026-11-20 07:15).

**Conflicts:**

- IT (via Aroha, 2026-11-23 01:40) says nothing changed on VLAN 30 and outbound UDP 123 is allowed. This is **Reported**. It conflicts with the verified NTP timeouts from VLAN 30 gateways (item 5). One of these is wrong, or the block is elsewhere (DNS resolution of pool.terncloud.net, upstream firewall, or the pool itself).
- The NTP failure has been logged since 12 Nov. The first reported miss was 17 Nov. Whether alarms on vats 1 to 3 failed from 12 Nov is not established.

## 2. Tried and results

| When (UTC) | Who | What | Result |
| --- | --- | --- | --- |
| 2026-11-20 01:05 | Hannah Odum | Checked TernCloud alarm rules for vats 1 to 9 | Identical templates and recipients; config does not explain the difference |
| 2026-11-20 01:10 | Hannah Odum | Asked customer for diagnostic bundles from GW-01 to 03 (status set to Pending customer) | Worked: bundles attached 05:40 |
| 2026-11-20 07:15 | Hannah Odum | Analysed bundles | Found clock skew and NTP failures (evidence 4 to 6) |
| 2026-11-20 07:20 | Hannah Odum | Asked customer's IT to check outbound UDP 123 from VLAN 30 | Answered 23 Nov: IT says allowed. Did not resolve the cause |
| 2026-11-23 02:15 | Hannah Odum | Priority P3 to P2 | Recorded on ticket |
| 2026-11-23 02:20 | Hannah Odum | Passed compensation request to Joel Brandt | No result recorded; no response from Joel in thread |
| 2026-11-23 02:35 | Hannah Odum | "Force time sync (HTTPS)" to GW-01, 02, 03 | GW-01, 02 worked; GW-03 failed (RTC write error) |
| 2026-11-23 03:05 | Aroha Ngata | Alarm test on vats 1 to 3 | Vats 1, 2 sent SMS; vat 3 failed (reported) |
| 2026-11-24 05:15 | Hannah Odum | Second "Force time sync (HTTPS)" on GW-03 | Failed, same RTC write error |
| 2026-11-24 05:17 | Hannah Odum | Remote reboot of GW-03 (customer agreed by phone 05:10) | Reboot succeeded (online 05:19); clock still +11 min, so the fix failed |
| 2026-11-24 05:40 | Hannah Odum | Told customer, escalated to Tier 2 | Escalation event at 06:00 |

Not an attempt: the 24 Nov 01:30 note (SLA check, contains an error; see section 4). The NTP root cause has not been fixed on any gateway, so GW-01 and GW-02 may drift again.

## 3. Commitments to the customer

Under policy 5.3, Tier 2 now owns these, including commitments already made.

1. **Update by 17:30 AWST today.** Hannah Odum, 2026-11-24 05:40: "You'll get an update from us by 17:30 AWST today (09:30 UTC)." This is a promise of the time of the next update, allowed by 6.1. It is due in 3.5 hours from the as-of time.
2. **Send a time-set command and ask for a retest.** Hannah Odum, 2026-11-23 02:20: "Next, I'm going to send a command from TernCloud that sets the clock on GW-01 to 03 over HTTPS". This is a statement of her own future action and it was carried out (02:35). Closed. Marked ambiguous as to whether it counts as a promise.
3. **Compensation request passed on.** Hannah Odum, 2026-11-23 02:20: "I'm not able to offer compensation myself, so I've passed your request to Joel Brandt, your account manager." This is a report of an action, not a promise of an outcome. It is listed because the customer is waiting on a milk-cost decision (ambiguous). Under 6.3 only the Account Manager or the Head of Customer Support may offer credit or compensation, and nothing is recorded in writing. No credit, refund or compensation has been promised. Open credits: None (account record).
4. The 2026-11-20 07:20 remarks "No rush before Monday; the hourly checks cover you over the weekend" and the 2026-11-24 05:40 "Vats 1 and 2 are still working" are not promises.

Policy 7.1 also requires at least one update per business day on a P2.

## 4. Service level and deadline

- **Plan:** Business (account record, "Support plan: Business").
- **Priority:** P2. Recorded on the ticket 2026-11-23 02:15 (clause 2.5). Customer reason: product loss and hourly checks are not a practical workaround (clause 2.2).
- **Targets (clause 3.1, Business P2):** first response 4 business hours; resolution 27 business hours.
- **Clock start (clause 4.1):** "The clock starts when the ticket is created." Created 2026-11-19 07:50 UTC (Thu 15:50 AWST), inside business hours. Business hours (1.1, 1.2): 00:30 to 09:30 UTC, Mon to Fri.
- **Priority change (clause 4.3):** "the resolution target becomes the target for the new priority, counted from ticket creation and excluding paused time." The clock is not restarted at the P2 change.
- **Pause (clause 4.2):** only while status is "Pending customer". The ticket was Pending customer 2026-11-20 01:10 to 05:40 UTC = 4h30m, all inside business hours, so it is subtracted.

**Business hours used (UTC):**

| Day | Counted | Hours |
| --- | --- | --- |
| Thu 19 Nov | 07:50 to 09:30 | 1h40 |
| Fri 20 Nov | 00:30 to 09:30 (9h) minus pause 4h30 | 4h30 |
| Sat 21, Sun 22 | weekend | 0 |
| Mon 23 Nov | 00:30 to 09:30 | 9h |
| Tue 24 Nov | 00:30 to 06:00 | 5h30 |
| **Total** | | **20h40 (20.67h)** |

- **Remaining:** 27h - 20h40 = **6h20** of business hours.
- **Deadline:** 3h30 remain on Tue 24 (06:00 to 09:30), leaving 2h50 on Wed 25. The resolution deadline is **Wed 25 Nov 2026 03:20 UTC (11:20 AWST)**.
- **Status (clause 4.4):** "at risk" if less than 25% of the target remains. 25% of 27h = 6h45. 6h20 is below that, so the ticket is **at risk** (not breached). It crossed the threshold at about 05:35 UTC on 24 Nov.
- **Error in the ticket:** Hannah's note (2026-11-24 01:30) gives Thu 26 Nov 10:15 AWST by counting 27 business hours from the P2 change. That conflicts with clause 4.3. The correct deadline is about 1 business day earlier. Do not rely on "Plenty of time".
- **First response:** first contact was 2026-11-20 01:05 UTC. Elapsed business time was 1h40 + 35 min = 2h15, inside the 4h target. Met. It was also inside the 9h P3 target that applied at the time.
- **Escalation rules:** clause 5.1: Tier 1 escalates a P2 ticket when it is at risk. Clause 5.2: "the Support Team Lead must be notified at escalation". No Team Lead notification is recorded in the thread.
- **Update cadence (clause 7.1):** P2 needs at least one update per business day. Tue 24 was met (05:40). Wed 25 is due, and the 17:30 AWST update today is the stated commitment.
- **Calendar assumption:** public holidays were not supplied (clause 1.1 excludes WA public holidays). The calculation assumes none on 19 to 25 Nov.

## 5. Recommended next action

**Action:** Tier 2 (Field Systems Engineering) should treat GW-03 as a probable RTC hardware fault and arrange its replacement (or field swap) at Brunswick, so vat 3 has a working alarm before the deadline of Wed 25 Nov 11:20 AWST. Send the customer the update promised by 17:30 AWST today (09:30 UTC).

**Why:** The clock write on GW-03 failed twice with an RTC write error and a reboot did not clear it (evidence 8). The other two gateways accepted the same command. The rule skip on GW-03 follows from the clock offset, and vat 3 has had two reported missed alarms (evidence 1, 10), the second with product loss. Nothing short of a correct clock on GW-03 restores vat 3 alarms. The ticket is at risk, with 6h20 of business hours left.

**Owner tier:** Tier 2 (Field Systems Engineering), as the ticket owner under 5.3.

**First check:** Pull a fresh diagnostic bundle from GW-03 and compare its firmware version and RTC or hardware error log with GW-01 and GW-02, to separate a hardware RTC fault from a firmware fault (which would change the fix to a firmware update).

**Open questions for the customer:**
- Can Peter Dunn confirm, with a packet capture or firewall log from VLAN 30, whether UDP 123 traffic to pool.terncloud.net leaves the site? Can DNS resolve that name from VLAN 30? (This addresses the conflict in section 1.)
- Is the night shift still checking the dashboard every hour, and can they keep a manual check of vat 3 until GW-03 is fixed?

**Open questions for engineering:**
- Why does NTP time out on VLAN 30 gateways while GW-04 to 09 sync, and what will stop GW-01 and GW-02 drifting again? Is there a persistent HTTPS time-sync option?
- Can the vat 3 rule be made tolerant of clock offset in the interim?

## 6. Gaps (missing inputs, conflicts, unverified assumptions)

- **Team Lead notification missing:** clause 5.2 requires the Support Team Lead to be notified on escalating an at-risk P2. The thread records none. Tier 2 should confirm it was done, or do it now.
- **Wrong SLA date in the ticket:** deadline is Wed 25 Nov 11:20 AWST, not Thu 26 Nov 10:15 AWST (section 4).
- **Compensation:** the customer asked for the cost of 18,000 litres of milk to be covered. Nothing from Joel Brandt is recorded. Agents must not promise credit (6.2). Joel Brandt must be chased so the request is answered in writing on the ticket (6.3). No offer exists.
- **Missing inputs:** the diagnostic bundles themselves and the TernCloud alarm rule were not supplied; items 3 to 6 rest on Hannah Odum's notes. No WA public holiday calendar was supplied.
- **Unverified:** the vat 3 over-temperature events and the milk loss (reported only); the vat 1 and 2 retest results (customer reported); that the dashboard showed the reading; that GW-03's rule skip continues (inferred, not freshly observed after the reboot).
- **Conflict:** IT says UDP 123 is allowed; gateway logs show NTP timeouts from VLAN 30 (section 1).
- **Unfixed root cause:** NTP is still failing on GW-01 to 03, so GW-01 and GW-02 are working only until their clocks drift again.
