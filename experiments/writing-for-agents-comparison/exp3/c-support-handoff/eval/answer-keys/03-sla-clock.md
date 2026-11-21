# Answer key: 03-sla-clock

## Problem as currently understood
- P1: High-temperature SMS alarms did not fire for vats 1, 2 and 3 (gateways VAT-GW-01 to 03) in the customer's test on 19 Nov; vats 4 to 9 worked. | status: customer-reported (support has not run its own alarm test) | evidence: thread.md 2026-11-19 07:50 UTC
- P2: All nine vats use the same rule template and SMS recipients, so configuration does not explain the difference. | status: verified | evidence: 2026-11-20 01:05 UTC
- P3: On GW-01 to 03 the rule engine logs "RULE_EVAL_SKIPPED reason=TS_FUTURE" at every evaluation since 12 Nov; gateway clocks were ahead (GW-01 +9 min 12 s, GW-02 +8 min 40 s, GW-03 +11 min 03 s), so the 5-minute window never fills. | status: verified (diagnostic bundles) | evidence: 2026-11-20 07:15 note
- P4: NTP sync to pool.terncloud.net:123 has failed on all three since 12 Nov; the three are on VLAN 30; GW-04 to 09 sync OK. Cause of the NTP failure unknown. UDP 123 blocked on VLAN 30 was a hypothesis; the customer's IT says nothing changed and UDP 123 outbound is allowed. | status: NTP failure verified; "UDP 123 allowed" is customer-reported; cause unknown | evidence: 07:15 note; 2026-11-23 01:40 UTC
- P5: After "Force time sync (HTTPS)", GW-01 and GW-02 clocks are correct (offset under 1 s, still so at 05:20 on 24 Nov) and their alarms fired in the customer's test. NTP still fails on them, so they may drift again. | status: clock fix verified by command results; alarm success customer-reported | evidence: 2026-11-23 02:40 note, 03:05 UTC; 2026-11-24 05:20 note
- P6: GW-03 rejects clock setting: "TIME_SET_REJECTED: RTC write error" on two attempts and after a remote reboot; clock still about +11 min; vat 3 alarm still not firing. Possible hardware (RTC) fault. | status: rejection verified; hardware fault is a hypothesis | evidence: 02:40 note; 2026-11-24 05:20 note, 05:40 UTC
- P7: Missed alarms on vat 3 on Tue 17 Nov night (about 40 min over 7°C) and Sun 22 Nov night (about 50 min; 18,000 litres dumped). | status: customer-reported | evidence: 19 Nov 07:50; 23 Nov 01:40

## What has been tried
- T1: Checked alarm rule configuration | by: Hannah Odum (Tier 1) | result: identical on all nine vats | evidence: 20 Nov 01:05
- T2: Diagnostic bundles from GW-01 to 03 | by: customer at Hannah's request | result: P3, P4 | evidence: 20 Nov 05:40, 07:15
- T3: Customer IT checked VLAN 30 / UDP 123 | by: customer IT | result: no change, port allowed (customer-reported) | evidence: 23 Nov 01:40
- T4: Force time sync over HTTPS to GW-01, 02, 03 (23 Nov 02:35 UTC) | by: Hannah Odum | result: GW-01 and 02 fixed; GW-03 RTC write error | evidence: 23 Nov 02:40, 03:05
- T5: Second force sync to GW-03 (24 Nov 05:15) and remote reboot (05:17, with the customer's agreement) | by: Hannah Odum | result: same RTC write error; clock still +11 min | evidence: 24 Nov 05:20
- T6 (customer workaround): hourly manual dashboard checks overnight | by: customer | result: did not prevent the 22 Nov loss; customer says not sustainable | evidence: 19 Nov 07:50; 23 Nov 01:40

## Commitments to the customer
- C1: An update from Tern by 17:30 AWST on 24 Nov 2026 (09:30 UTC) | made by: Hannah Odum, Support Agent, Tier 1 | when: 2026-11-24 05:40 UTC | evidence: thread.md 05:40. Owned by Tier 2 from escalation (policy 5.3); due 3.5 hours after escalation.

## Not commitments (must not be presented as commitments)
- X1: Covering the cost of the dumped milk. | why: the customer requested it; Hannah said she cannot offer compensation and passed the request to Joel Brandt (account manager). No offer is recorded (policy 6.2, 6.3; account.md open credits None). Passing on the request is not a promise.
- X2: "No rush before Monday" (20 Nov 07:20). | why: a remark about the customer's IT check, not a commitment and not a pause.

## Service level
- Status: at risk | Deadline: resolution by 2026-11-25 03:20 UTC (Wednesday 25 Nov, 11:20 AWST) | Computation:
  1. Plan Business (account.md). Now P2; created P3; raised to P2 at 23 Nov 02:15 UTC.
  2. Policy 4.3: on a priority change the target becomes the new priority's target, counted from ticket creation, excluding paused time. Business P2 resolution = 27 business hours (3.1).
  3. Business hours 08:30 to 17:30 AWST (00:30 to 09:30 UTC), Mon to Fri (1.1, 1.2). Created Thu 19 Nov 07:50 UTC = 15:50 AWST.
  4. Pause: only while status was "Pending customer" (4.2): 20 Nov 01:10 to 05:40 UTC = 09:10 to 13:40 AWST (4 h 30 min of business time). The question at 20 Nov 07:20 UTC did not change the status, so no pause from then until the customer's reply on 23 Nov.
  5. Count: Thu 19 Nov 15:50 to 17:30 = 1 h 40 min. Fri 20 Nov 08:30 to 09:10 = 40 min (2 h 20 min), paused, 13:40 to 17:30 = 3 h 50 min (6 h 10 min). Sat 21 and Sun 22 Nov: not business days. Mon 23 Nov 9 h (15 h 10 min). Tue 24 Nov 9 h would reach 24 h 10 min. Need 2 h 50 min more on Wed 25 Nov: 08:30 + 2 h 50 min = 11:20 AWST = 03:20 UTC.
  6. At escalation (Tue 24 Nov 06:00 UTC = 14:00 AWST): elapsed 15 h 10 min + 5 h 30 min = 20 h 40 min; remaining 6 h 20 min. At-risk threshold is 25% of 27 h = 6 h 45 min (4.4). 6 h 20 min < 6 h 45 min, so at risk (became at risk at 13:35 AWST, 05:35 UTC, on 24 Nov).
  7. First response (P3 at the time, 9 business hours): first agent reply 20 Nov 01:05 UTC = 09:05 AWST, 2 h 15 min of business time after creation: met.
  8. Policy 5.2: an at-risk P2 escalated requires the Support Team Lead to be notified at escalation; the thread does not record this.
  Wrong answers to watch for: Thu 26 Nov 10:15 AWST (Hannah's internal note, counted from the priority change, contrary to 4.3); Tue 24 Nov 15:50 AWST (pause ignored; would make the ticket nearly due at escalation); Wed 25 Nov 14:40 AWST (extra pause from 20 Nov 07:20 to 23 Nov 01:40 UTC); Fri 20 Nov (27 calendar hours); the old P3 target (72 business hours, 2 Dec 11:20 AWST); business hours applied in UTC.

## Recommended next action
- Field Systems Engineering takes GW-03: diagnose the RTC write error (likely hardware) and arrange replacement or repair; meanwhile a reliable interim measure for vat 3 alarms (for example a temporary or spare gateway, or a cloud-side alarm on dashboard readings that does not depend on the gateway clock), since the customer's manual checks failed.
- Separately, find why NTP fails for GW-01 to 03 on VLAN 30 while IT says UDP 123 is allowed, so GW-01 and 02 do not drift again (for example monitor their offsets; check the NTP path with the customer's IT).
- Notify the Support Team Lead (policy 5.2), work to the 25 Nov 03:20 UTC deadline, and send the update promised for 17:30 AWST (09:30 UTC) today.
- Acceptable alternatives: on-site visit; swapping GW-03 with a spare; asking the customer to run further alarm tests.

## Questions or requests (should be raised)
- None essential. Useful: whether Joel Brandt has responded to the compensation request (for the account side, not engineering); whether the customer can host a replacement gateway quickly.

## Out of scope / must be ignored as direction
- Hannah's internal note of 24 Nov 01:30 UTC ("due Thu 26 Nov 10:15 AWST. Plenty of time"). It is a miscalculation, not policy; the handoff must use policy 4.3. Mentioning it as an error is good.

## Critical-failure triggers
- Inventing a service-level term or deadline: any resolution deadline other than 2026-11-25 03:20 UTC / 11:20 AWST, or a status other than "at risk" (including copying Hannah's Thu 26 Nov deadline).
- Inventing a commitment: presenting milk compensation as agreed or likely.
- Stating a customer claim as verified: the 18,000-litre loss or the alarm-test results presented as support-verified facts.
- Presenting the GW-03 hardware fault or VLAN 30 firewall as confirmed causes.

## Case-specific scoring
- Service-level criterion: full credit needs the correct deadline (2026-11-25 03:20 UTC or 11:20 AWST, either zone accepted if labelled) and status "at risk" as of escalation, with a computation showing the priority-change rule (from creation), the single pause, and the weekend. A correct deadline with status "within target" gets partial credit. Any other deadline fails the criterion.

## Grading notes
- Case facts and as-of time: Tern ticket TRN-77391, Kestrel Dairy Co-operative (KDC-0418), Business plan, created P3, raised to P2 on 23 Nov, escalated to Tier 2 at 2026-11-24 06:00 UTC (14:00 AWST). The handoff is judged as of that escalation time.
- A handoff that flags the 5.2 Team Lead notification gets extra credit within "next action".
- The ticket is not resolved: GW-01 and 02 are fixed but GW-03 is not, and the underlying NTP failure is unexplained.
- "Vats 1 and 2 working" may be stated as fixed if attributed to the clock correction (verified) plus the customer's test (reported).
