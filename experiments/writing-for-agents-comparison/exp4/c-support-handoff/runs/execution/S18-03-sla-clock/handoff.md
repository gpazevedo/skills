# Handoff: TRN-77391, Kestrel Dairy Co-operative (KDC-0418)

As of 2026-11-24 06:00 UTC (14:00 AWST Tue). Escalated to Tier 2 (Field Systems Engineering), P2. This ticket is at risk on its resolution target (section 4). Tier 2 owns customer updates and existing commitments from escalation (policy 5.3).

## 1. Problem as currently understood

High-temperature SMS alarms do not fire for vat 3 (VAT-GW-03 at Brunswick). Vats 1 and 2 were failing the same way but recovered after a forced HTTPS time sync. GW-03 refuses to set its clock, so its rule engine still skips the alarm rule. It may be a hardware fault, which is unconfirmed.

**Reported by customer**
- 2026-11-19 07:50, Aroha Ngata: vat 3 exceeded 7°C for about 40 min on Tue night with no SMS. A test on all nine vats had vats 4-9 sending SMS and vats 1-3 sending nothing.
- 2026-11-23 01:40, Aroha Ngata: vat 3 went over 7°C again about 01:00 AWST Mon, with no SMS. It was caught on the hourly check after about 50 min. 18,000 litres were dumped. The customer asks for the cost of the milk to be covered.
- 2026-11-23 01:40, Aroha Ngata: IT says nothing changed on VLAN 30 and outbound UDP 123 is allowed.
- 2026-11-23 03:05, Aroha Ngata: after the time sync, vats 1 and 2 sent SMS within a minute and vat 3 sent nothing.

**Verified by support**
- Alarm rules for vats 1-9 use the same template and recipients (Hannah Odum, 2026-11-20 01:05, checked in TernCloud).
- GW-01/02/03 log `RULE_EVAL_SKIPPED reason=TS_FUTURE` at every evaluation since 12 Nov. Gateway clocks were ahead by +9m12s, +8m40s and +11m03s (Hannah Odum, internal note 2026-11-20 07:15, from the diagnostic bundles).
- The NTP log on all three shows "NTP sync failed: timeout (pool.terncloud.net:123)" since 12 Nov (same note). TernCloud shows GW-04 to 09 with last time sync OK (same note).
- After "Force time sync (HTTPS)", GW-01 and GW-02 returned OK with offset under 1 s. GW-03 returned `TIME_SET_REJECTED: RTC write error` (Hannah Odum, notes 2026-11-23 02:40 and 2026-11-24 05:20). After a second attempt and a reboot at 05:17, GW-03 was still about +11 min.
- GW-01 and GW-02 were still in sync at 2026-11-24 05:20 (Hannah Odum, same note).

**Unverified hypotheses**
- GW-03 has a hardware fault (RTC), per Hannah Odum's 2026-11-24 05:40 message to the customer ("may be").
- UDP 123 is blocked for VLAN 30 (Hannah Odum, 2026-11-20 07:15, "not confirmed"). The customer's IT contradicts this (2026-11-23). The NTP timeout cause is unknown.
- GW-01 and GW-02 may drift again while NTP keeps failing (Hannah Odum, 2026-11-24 05:20).

## 2. Tried and result

1. 11-20 01:05, Hannah Odum: checked alarm rules and recipients for vats 1-9. They are identical, so config is ruled out.
2. 11-20 01:10, Hannah Odum: asked the customer for diagnostic bundles. The customer supplied them 11-20 05:40. Worked.
3. 11-20 07:20, Hannah Odum: asked the customer's IT to check outbound UDP 123 from VLAN 30. IT reported on 11-23 that it is allowed. Inconclusive, because the NTP timeout is unexplained.
4. 11-23 02:35, Hannah Odum: "Force time sync (HTTPS)" to GW-01/02/03. Worked on 01 and 02. Failed on 03 (RTC write error).
5. 11-23 03:05, Aroha Ngata: alarm test on vats 1-3. Vats 1 and 2 worked, vat 3 failed.
6. 11-24 05:15, Hannah Odum: second HTTPS time sync on GW-03. Failed with the same error.
7. 11-24 05:17, Hannah Odum: remote reboot of GW-03, agreed by Aroha by phone at 05:10. Back online 05:19, clock still +11 min. Failed.
8. Customer workaround: night staff check the dashboard hourly. It is not adequate (milk lost 11-23).

## 3. Commitments to the customer

- 11-24 05:40, Hannah Odum: customer "will get an update from us by 17:30 AWST today (09:30 UTC)". **Open**, due 2026-11-24 09:30 UTC (about 3.5 h after as-of). Now Tier 2's to meet (policy 5.3).
- 11-23 02:20, Hannah Odum: "passed your request to Joel Brandt" (milk compensation). Whether Joel has been told is not recorded on the ticket. Status **open**. No credit or compensation has been offered. The account record shows open credits: None. Only the Account Manager or Head of Customer Support may offer one, in writing (policy 6.3).
- 11-23 02:20, Hannah Odum: would send the time-sync command, then asked the customer to test. **Met.**

## 4. Service-level status and deadline

- Tier: Business (account record). Severity: P2 since 2026-11-23 02:15 UTC (recorded on the ticket). Policy 3.1, Business P2: "27 business hours" resolution.
- Policy 4.3: the target is counted from ticket creation (2026-11-19 07:50 UTC = Thu 15:50 AWST), excluding paused time. Hannah's 11-24 note counted from the P2 change (Mon 10:15 AWST) and gave Thu 26 Nov 10:15. That is wrong.
- Business hours are 08:30-17:30 AWST, Mon-Fri (policy 1.1). I found no WA public holiday in the thread's dates, but this was not checked against a holiday list.
- Pause (policy 4.2): "Pending customer" 11-20 01:10 to 05:40 UTC = 4.5 h, all inside business hours.
- Count, all in AWST:

| Period | Business hours counted |
| --- | --- |
| Thu 19, 15:50-17:30 | 1h40 |
| Fri 20, 9h less 4.5h pause | 4h30 |
| Mon 23 | 9h00 |
| Tue 24, 08:30-14:00 | 5h30 |
| **Total used** | **20h40** |

- Remaining: 27h - 20h40 = **6h20**.
- **Deadline: Wed 2026-11-25 about 11:20 AWST (03:20 UTC)**, assuming no further pause. This is 3h30 left on Tue (to 17:30), then 2h50 from Wed 08:30.
- Status: 25% of 27h is 6h45, and 6h20 remaining is less than that, so the ticket is **at risk** (policy 4.4). It is not breached.
- The customer's update commitment (17:30 AWST today) falls inside the window. P2 also requires an update at least once per business day (policy 7.1).

## 5. Recommended next action (support's judgement, not a commitment)

**Primary.** Tier 2 (Field Systems Engineering) should decide today whether GW-03 is a hardware fault and arrange the fix route (repair or replacement of GW-03, or an on-site visit). The fix must land by about 11:20 AWST Wed. Resolution needs a working vat 3 alarm, because a ticket with one unresolved fault is not resolved (policy 1.5). Send the customer an update before 17:30 AWST today (09:30 UTC), as committed. Make no promise of a fix date or a credit (policy 6.2). The reason is that two time-set attempts and a reboot all failed with an RTC write error.

Alternatives:
1. Find out why NTP times out for VLAN 30, for example a capture with Peter Dunn, so GW-01 and GW-02 do not drift again. The reason is that the HTTPS sync is a one-off fix and NTP is still failing.
2. Look for an interim way to cover vat 3 until GW-03 is fixed. Nothing is established in the thread. The reason is that hourly manual checks already failed once (18,000 L).

Also:
- The Support Team Lead must be notified at escalation of an at-risk P2 (policy 5.2). The thread does not show this was done, so do it now.
- Ask Joel Brandt, Account Manager, to answer the milk compensation request. Tier 2 must not discuss compensation with the customer.

## 6. Open questions

- Is GW-03's RTC faulty? Does a firmware or factory reset help? Is the unit on the current firmware? None of this is in the thread.
- Why does NTP time out on VLAN 30 if UDP 123 is allowed? Is it a DNS issue, or a different path or firewall rule? How did GW-04 to 09 (VLAN not stated) keep syncing?
- What began on 12 Nov, when the NTP failures started?
- Was the Support Team Lead notified? Has Joel Brandt received the compensation request?
- Conflict: Hannah's SLA note (due Thu 26 Nov 10:15 AWST) disagrees with policy 4.3 (due about Wed 25 Nov 11:20 AWST). Use the policy figure.
- Was the 11-19 test of vat 4-9 alarms the only check of those vats? No other evidence of their state exists in the thread.
