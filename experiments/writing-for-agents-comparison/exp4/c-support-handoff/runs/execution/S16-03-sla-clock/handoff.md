# Handoff: TRN-77391, Kestrel Dairy Co-operative (KDC-0418), P2, escalated to Tier 2 at 2026-11-24 06:00 UTC

## 1. Problem as understood
High-temperature SMS alarms do not fire for vat gateways VAT-GW-01 to 03 (Brunswick plant). GW-01 and GW-02 are now working after a forced time sync, but GW-03 still fails because it refuses to set its clock, and a milk loss has already occurred.

Evidence:
- Reported (Aroha Ngata, 2026-11-19 07:50): vat 3 exceeded 7°C for about 40 min on Tuesday night with no SMS. Test of all nine vats: vats 4-9 sent SMS, vats 1-3 sent none.
- Verified (Hannah Odum, 2026-11-20 01:05, TernCloud rule check): vats 1-9 use the same rule template and recipients, so rule configuration does not explain it.
- Verified (Odum, 2026-11-20 07:15, diagnostic bundles for GW-01 to 03): "RULE_EVAL_SKIPPED reason=TS_FUTURE" at every evaluation since 12 Nov. Gateway clocks were ahead by +9m12s (01), +8m40s (02), +11m03s (03). NTP log "sync failed: timeout (pool.terncloud.net:123)" since 12 Nov. The three are on VLAN 30. TernCloud shows GW-04 to 09 with last time sync OK.
- Verified (Odum, 2026-11-23 02:40): after "Force time sync (HTTPS)", GW-01 and 02 returned OK with offset under 1 s. GW-03 returned "TIME_SET_REJECTED: RTC write error", clock +11m05s.
- Reported (Ngata, 2026-11-23 03:05): after the sync, vats 1 and 2 sent SMS within a minute; vat 3 sent nothing.
- Verified (Odum, 2026-11-24 05:20): second forced sync on GW-03 gave the same RTC write error. Reboot at 05:17, back at 05:19, clock still about +11 min. GW-01 and 02 still within 1 s, but NTP still failing on all three.
- Reported (Ngata, 2026-11-23 01:40): vat 3 went over 7°C again at about 01:00 AWST Monday with no SMS; over the limit about 50 min; 18,000 litres dumped. Not verified by support (no log or record cited).
- Reported (Ngata via IT, 2026-11-23 01:40): nothing changed on VLAN 30 and outbound UDP 123 is allowed. Not verified by support.

Open questions for Tier 2:
- Why does NTP time out on GW-01 to 03 when the customer says UDP 123 is open? Odum's firewall hypothesis (2026-11-20 07:15) is unconfirmed and the customer's statement contradicts it. Why do GW-04 to 09 sync?
- Is the GW-03 RTC write error a hardware fault (Odum's suggestion on 2026-11-24 05:40, unconfirmed)? Does GW-03 need replacement?
- Will GW-01 and 02 drift again while NTP fails? Is the rule skip also evidenced for GW-03 on the 23 Nov incident (bundle logs after 12 Nov were not reviewed past the first set)?

## 2. Tried so far
- Customer tested alarms on all nine vats (2026-11-19, Ngata): vats 1-3 failed. Identified the scope.
- Odum compared alarm rule templates (2026-11-20 01:05): no difference. Ruled out configuration.
- Customer supplied diagnostic bundles for GW-01 to 03 (2026-11-20 05:40, Ngata): worked, revealed clock skew and NTP failure.
- Customer IT checked VLAN 30 and UDP 123 (reported 2026-11-23 01:40, Ngata/IT): customer says allowed. Inconclusive, not independently checked.
- Odum sent "Force time sync (HTTPS)" to GW-01, 02, 03 (2026-11-23 02:35): worked on 01 and 02, failed on 03.
- Customer retested vats 1-3 (2026-11-23 03:05): 1 and 2 worked, 3 failed.
- Odum second forced sync and remote reboot of GW-03, customer agreed by phone at 05:10 (2026-11-24 05:15 and 05:17): failed, clock still +11 min.
- Customer workaround: night staff check the dashboard hourly (Ngata). It failed to prevent the loss on 23 Nov (about 50 min over limit).

## 3. Commitments to the customer
- Update by 17:30 AWST today, 2026-11-24 (09:30 UTC): promised by Hannah Odum, 2026-11-24 05:40. Tier 2 owns this under policy 5.3.
- Odum, 2026-11-23 02:20: "I've passed your request to Joel Brandt" (compensation request). An action by Odum. The thread does not show that Brandt received or answered it.
- Soft assurance: none found (Odum's apology on 2026-11-23 02:20 and "No rush before Monday" on 2026-11-20 07:20 set no expectation).
- No credit, refund, compensation or fix date has been offered. Odum stated she cannot offer compensation (2026-11-23 02:20), consistent with policy 6.2 and 6.3. The customer's request for the milk cost to be covered (Reported, 2026-11-23 01:40) is open with the Account Manager.

## 4. Service-level status
- Plan: Business (account record). Priority: P2, recorded 2026-11-23 02:15 UTC (policy 2.5). Resolution target: 27 business hours (policy 3.1).
- Clock start: ticket created 2026-11-19 07:50 UTC = Thu 15:50 AWST. Per 4.3 the P2 target counts from creation, excluding paused time.
- Pause: "Pending customer" 2026-11-20 01:10 to 05:40 UTC = Fri 09:10 to 13:40 AWST, 4.5 business hours excluded.
- Business hours used to the as-of time (2026-11-24 06:00 UTC = Tue 14:00 AWST): Thu 15:50-17:30 = 1h40; Fri 9h minus 4.5h pause = 4h30; Mon 23 Nov 9h; Tue 08:30-14:00 = 5h30. Total 20h40 used. Weekend excluded. No Western Australian public holiday is identified in the inputs for these dates; confirm none applies.
- Remaining: 6h20 of 27h. At-risk threshold (policy 4.4) is 25% = 6h45 remaining, so the ticket is AT RISK (not breached).
- Deadline: Wed 2026-11-25 11:20 AWST (03:20 UTC), computed from 14:00 Tue + 3h30 to 17:30, then 2h50 from 08:30 Wed.
- Correction: Odum's internal note (2026-11-24 01:30) gives Thu 26 Nov 10:15 AWST. That is wrong: it counts from the priority change instead of creation, ignores the pause and the business-hours window. Use the Wed 11:20 AWST deadline.
- First response: not an issue (ticket 07:50 UTC, agent reply 2026-11-20 01:05 UTC).
- Escalation: policy 5.1 and 5.2 require the Support Team Lead be notified at escalation of an at-risk P2. The thread shows no such notification. Status: unconfirmed, do it now.
- Breach trigger: the policy states no consequence or credit for a breach (only a status label). Unknown whether any applies; Account Manager Joel Brandt is the only route to a credit (6.3).
- Customer update cadence: P2 needs at least one update per business day (7.1).

## 5. Recommended next action
Primary: Tier 2 (Field Systems Engineering) takes GW-03 first. Treat the RTC write error as a probable hardware fault and arrange replacement or on-site/field repair of VAT-GW-03, targeting before the deadline Wed 11:20 AWST. If replacement cannot happen in time, tell the customer plainly that vat 3 has no working alarm and agree a stronger interim cover (this is a customer-safety issue, since milk was already lost on vat 3).
Why: GW-03 is the only gateway still failing after the forced sync, the reboot, and a second sync (evidence 2026-11-23 02:40 and 2026-11-24 05:20). The deadline is Wed 11:20 AWST.
In parallel: (1) notify the Support Team Lead now (policy 5.2); (2) investigate the NTP failure on VLAN 30 so GW-01 and 02 do not drift again, since the sync is a one-off fix; (3) confirm to Joel Brandt that the compensation request exists and ask him to respond to the customer, as only he or the Head of Customer Support can (6.3).
Unverified and depended upon: that GW-03's fault is hardware, that the NTP failure is a network block (customer says not), and that the vat 3 loss on 23 Nov was caused by the same clock skew.
Customer update due: by 17:30 AWST today (09:30 UTC), promised by Odum. State that the ticket is escalated, GW-01 and 02 work, GW-03 is being treated as a possible hardware fault, and give the time of the next update. Do not promise a fix date, credit or compensation (6.2).
