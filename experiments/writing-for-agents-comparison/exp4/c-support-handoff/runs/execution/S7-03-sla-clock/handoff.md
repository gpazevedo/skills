# Handoff: TRN-77391, high-temperature SMS alarms not received from some vat gateways (Kestrel Dairy Co-operative, KDC-0418)

## Problem as understood
Vat high-temperature SMS alarms do not fire for vats 1 to 3 at the Brunswick plant. On GW-01 to 03 the rule engine skips evaluation because the gateway clocks run ahead of sensor timestamps and NTP is failing. A forced HTTPS time sync fixed GW-01 and GW-02, but GW-03 (vat 3) rejects the clock write, so vat 3 still has no working alarm. Ticket is P2, escalated to Tier 2 at 2026-11-24 06:00 UTC.
- Verified: Rule engine logged "RULE_EVAL_SKIPPED reason=TS_FUTURE" at every evaluation since 12 Nov on GW-01, 02, 03 (evidence: diagnostic bundles, Hannah Odum note 2026-11-20 07:15).
- Verified: Gateway clocks were ahead by +9m12s (GW-01), +8m40s (GW-02), +11m03s (GW-03) (evidence: bundles).
- Verified: "NTP sync failed: timeout (pool.terncloud.net:123)" on all three since 12 Nov; GW-01 to 03 are on VLAN 30; TernCloud shows GW-04 to 09 last time sync OK (evidence: bundles, TernCloud).
- Verified: After "Force time sync (HTTPS)" GW-01 and GW-02 offset is under 1 s; GW-03 returned "TIME_SET_REJECTED: RTC write error" twice (02:35 on 23 Nov, 05:15 on 24 Nov) and is still about +11 min after a reboot (evidence: TernCloud command results, internal notes).
- Reported: Vats 4 to 9 sent SMS within a minute in the all-vat test; vats 1 to 3 sent nothing (customer, 2026-11-19).
- Reported: After the sync, vats 1 and 2 sent SMS, vat 3 did not (customer, 2026-11-23 03:05).
- Reported: Vat 3 exceeded 7°C with no SMS on the Tuesday night (customer, 2026-11-19) and again on the Sunday night, about 50 minutes over limit (customer, 2026-11-23). Not independently confirmed in the thread.
- Reported: 18,000 litres of milk were dumped (customer, 2026-11-23).
- Reported: IT says nothing changed on VLAN 30 and outbound UDP 123 is allowed (customer, 2026-11-23). This conflicts with the logged NTP timeouts; not verified.
- Not established: why NTP times out, and whether GW-03 has a hardware fault ("may be a hardware fault" is Hannah's suspicion, 2026-11-24 05:40).

## Tried so far
- Checked alarm rules, vats 1 to 9, by Hannah Odum, 2026-11-20: same template and recipients, so configuration does not explain it.
- Requested diagnostic bundles from GW-01 to 03, by Hannah, 2026-11-20: customer supplied them; they gave the findings above.
- Asked customer IT to check outbound UDP 123 from VLAN 30, by Hannah, 2026-11-20: IT replied it is allowed; no further check shown.
- Force time sync (HTTPS) to GW-01 to 03, by Hannah, 2026-11-23: worked on 01 and 02, failed on 03.
- Customer alarm test of vats 1 to 3, 2026-11-23: vats 1 and 2 passed, vat 3 failed.
- Second forced sync on GW-03, by Hannah, 2026-11-24 05:15: failed (same error).
- Remote reboot of GW-03 (customer agreed by phone 05:10), by Hannah, 2026-11-24 05:17: back online 05:19, clock still about +11 min.
- Passed the compensation request to Joel Brandt, by Hannah, 2026-11-23: no reply from him in the thread.

## Commitments to the customer
- Pass compensation request to account manager, by Hannah Odum, 2026-11-23 02:20 UTC: "I've passed your request to Joel Brandt, your account manager."
- Next update, by Hannah Odum, 2026-11-24 05:40 UTC: "You'll get an update from us by 17:30 AWST today (09:30 UTC)."
- No fix date, credit, refund or compensation was promised; Hannah stated "I'm not able to offer compensation myself." Tier 2 now owns these commitments (policy 5.3).

## Service level
Tier: Business (source: account record). Target: P2 resolution, 27 business hours (policy 3.1; business hours 08:30 to 17:30 AWST Mon to Fri, 1.1). Clock started: 2026-11-19 07:50 UTC (Thu 15:50 AWST, ticket creation, 4.1). Priority changed P3 to P2 on 23 Nov, so the P2 target counts from creation excluding paused time (4.3). Pause: Pending customer 2026-11-20 01:10 to 05:40 UTC (4.5 business hours, excluded).
Elapsed business hours at 2026-11-24 06:00 UTC (14:00 AWST): Thu 1.67 + Fri 4.50 + Mon 9.00 + Tue 5.50 = 20.67 h. Remaining 6.33 h. At-risk threshold is 25% of 27 = 6.75 h, so remaining is below it.
Deadline: Wed 2026-11-25 11:20 AWST (03:20 UTC), if no further pause and no public holiday. Status: at risk.
The thread's internal note (Thu 26 Nov 10:15 AWST) counts from the priority change and ignores 4.3, so it is wrong.

## Recommended next action
Tier 2 to treat GW-03 as a likely clock or RTC hardware fault and arrange a gateway swap or hardware diagnosis for vat 3, and give the customer an interim measure for vat 3 before the 17:30 AWST update. Reason: GW-03 rejected the clock write twice and a reboot did not help, and vat 3 has twice gone over limit unalarmed. Open question: is GW-03 faulty hardware, or is another cause behind the RTC write error?
- Alternative: Have Peter Dunn (IT) run a packet capture for UDP 123 on VLAN 30, since logs and IT's statement conflict; fixing NTP also protects GW-01 and GW-02 from drifting again.
- Alternative: Check whether a firmware or config reset on GW-03 clears the RTC error before replacement.

## Gaps
- Policy 5.2: the Support Team Lead must be notified when an at-risk P2 is escalated; the thread shows no notification. Do it now.
- Joel Brandt has not recorded any response on compensation (policy 6.3: only he or the Head of Customer Support may offer it, in writing).
- The incidents and 18,000 L loss are customer statements only. No alarm or SMS delivery logs were examined.
- Public holidays were not checked against the clock calculation.
- Customer-facing updates are due at least once each business day (7.1); the next is due 09:30 UTC today.
