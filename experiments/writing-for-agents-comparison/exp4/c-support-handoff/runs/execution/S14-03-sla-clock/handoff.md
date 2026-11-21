# Handoff: TRN-77391 (Kestrel Dairy Co-operative, KDC-0418), as of 2026-11-24 06:00 UTC

## 1. Problem as understood
High-temperature SMS alarms do not fire for vat gateways VAT-GW-03 (and, until 23 Nov, 01 and 02) at Brunswick. Support found the rule engine skipping evaluation because the gateway clocks run ahead of sensor timestamps, and NTP fails on all three. A forced HTTPS time sync fixed GW-01 and GW-02 but GW-03 rejects it with an RTC write error, which survived a reboot. GW-03 is still not alarming and a second product-loss event has occurred. The cause of the NTP failure is unexplained.

Evidence:
- Rule template for vats 1-9 identical, same SMS recipients: Verified, Hannah Odum (Tier 1), 20 Nov 01:05 (checked in TernCloud).
- Rule engine logs RULE_EVAL_SKIPPED reason=TS_FUTURE since 12 Nov on GW-01/02/03; clocks +9m12s, +8m40s, +11m03s: Verified, Hannah Odum, diagnostic bundles, note 20 Nov 07:15.
- NTP "sync failed: timeout (pool.terncloud.net:123)" since 12 Nov on GW-01/02/03; all on VLAN 30; GW-04 to 09 last sync OK: Verified, Hannah Odum, bundles and TernCloud, 20 Nov 07:15.
- GW-01 and GW-02 offset under 1 s after forced HTTPS sync: Verified, Hannah Odum, command result, 23 Nov 02:40. Customer states vats 1 and 2 alarm in test: Reported, Aroha Ngata, 23 Nov 03:05.
- GW-03 "TIME_SET_REJECTED: RTC write error" twice (23 Nov 02:35, 24 Nov 05:15), still +11 min after reboot at 05:17: Verified, Hannah Odum, notes 23 Nov 02:40 and 24 Nov 05:20. "May be a hardware fault" is Hannah's suggestion, not confirmed.
- Vats 4-9 send SMS in test; vats 1-3 did not on 19 Nov: Reported, Aroha Ngata, 19 Nov 07:50.
- Vat 3 over 7C for about 40 min (Tue 17 Nov night) and about 50 min (Sun 22 Nov night, about 01:00 local), 18,000 L dumped: Reported, Aroha Ngata, 19 Nov and 23 Nov. No support check of the dashboard readings or the volume.
- Contradiction: Hannah suspected UDP 123 blocked on VLAN 30 (not confirmed). Customer IT says nothing changed and UDP 123 is allowed (Reported, Aroha Ngata relaying IT, 23 Nov 01:40). No firewall check by Tern. Cause of NTP failure is open.
- Recorded priority is P2 (event 23 Nov 02:15, reason recorded). Account: Business plan (account record).

## 2. Tried and result
- Hannah Odum compared alarm rules vats 1-9, 20 Nov: identical, config ruled out.
- Hannah asked customer for bundles from GW-01/02/03, 20 Nov 01:10: worked (received 05:40), found clock skew and NTP failure.
- Hannah asked customer IT to check UDP 123 from VLAN 30, 20 Nov 07:20: customer reports it is allowed; unverified, unresolved.
- Hannah sent Force time sync (HTTPS) to GW-01/02/03, 23 Nov 02:35: worked on 01 and 02; failed on 03.
- Hannah repeated sync on GW-03 and rebooted it remotely (customer agreed by phone 05:10), 24 Nov 05:15-05:19: failed, clock still about +11 min.
- NTP still failing on all three, so GW-01/02 may drift again (Hannah, 24 Nov 05:20).
- Not done: alarm test on GW-03 after reboot; check of the customer's firewall/DNS path for pool.terncloud.net; no hardware replacement arranged.

## 3. Commitments to the customer
- Hannah Odum, 24 Nov 05:40: "You'll get an update from us by 17:30 AWST today (09:30 UTC)." Tier 2 now owns this (policy 5.3).
- Hannah Odum, 23 Nov 02:20: she "passed your request" for milk cost compensation to Joel Brandt. This is a referral, not an offer. No credit, refund or compensation offer is recorded in the thread or account record (open credits: None). Customer request "cost of that milk covered" is Reported and unanswered. Do not promise anything (policy 6.2, 6.3).
- Hannah, 23 Nov 02:20: will send a time command and asked customer to retest (done).
- No fix date has been promised.

## 4. Service-level status and deadline
- Tier: Business plan (account record), P2 recorded. Policy 3.1: first response 4 business hours; resolution 27 business hours. Business hours 00:30-09:30 UTC, Mon-Fri (1.1, 1.2). No WA public holiday found in the window (assumption; not checked).
- Clock start: ticket creation 19 Nov (Thu) 07:50 UTC (4.1). The P2 change counts from creation, not from 23 Nov 02:15 (4.3).
- Pause: only "Pending customer" (4.2): 20 Nov 01:10-05:40 UTC, 4h30 inside business hours. The 20 Nov 07:20 request to customer IT left status Open, so no pause.
- Counted: Thu 19 Nov 07:50-09:30 = 1h40; Fri 20 Nov 00:30-09:30 = 9h less 4h30 = 4h30; Mon 23 Nov 9h; Tue 24 Nov 00:30-06:00 = 5h30. Total 20h40. Remaining 6h20.
- Resolution deadline: Wed 25 Nov 03:20 UTC (11:20 AWST) (3.5h left Tue to 09:30, then 2h50 from 00:30 Wed).
- Status: AT RISK (4.4: under 25% of 27h = 6h45 remains; 6h20 does). Not breached. Hannah's note of Thu 26 Nov 10:15 AWST is wrong: it counted from the P2 change, not creation (4.3).
- First response: 20 Nov 01:05 UTC, 2h15 counted after creation (1h40 + 35 min), within 4 hours (1.4, 3.1). Met.
- Resolution needs every fault resolved with status Resolved (1.5); GW-03 is unresolved.
- Policy 5.1/5.2: an at-risk P2 escalation requires notifying the Support Team Lead at escalation. The thread shows no such notification.
- Customer update: P2 at least once each business day (7.1); the 09:30 UTC update serves this.

## 5. Recommended next action
Owner: Tier 2 Field Systems Engineering. First, notify the Support Team Lead now (policy 5.2, ticket is at risk). Primary action: ask Aroha for a fresh diagnostic bundle from GW-03 post-reboot and confirm whether the RTC fault is hardware. If confirmed, arrange a GW-03 replacement or workaround to restore vat 3 alarming. Target is before 03:20 UTC Wed 25 Nov (11:20 AWST). If not a hardware fault, escalate the cause of the NTP failure (firewall check on VLAN 30 with Peter Dunn) and tell the team lead the deadline is at risk. Rationale: GW-03 rejects clock writes even after reboot (evidence items 4-5), and vat 3 has now lost product twice (item 7).

Tell the customer by 09:30 UTC today: the action under way and the next update time. Do not give a fix date, credit or refund. Ask Joel Brandt (Account Manager) to respond in writing on the ticket about the milk request, and tell Aroha it has been referred. Remind Aroha that GW-01/02 may drift again while NTP fails, and that manual checks should continue for vat 3.
