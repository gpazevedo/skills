# Handoff: TRN-77391 (Kestrel Dairy Co-operative, KDC-0418, Business plan)

State as of 2026-11-24 06:00 UTC (14:00 AWST). P2, Escalated to Tier 2. Tier 2 now owns customer updates and the commitments below (policy 5.3).

## Do first
1. **The SLA is at risk, and Tier 1's note is wrong.** The 01:30 UTC note says it is due Thu 26 Nov and that there is plenty of time. See section 4. The deadline is **Wed 25 Nov 11:20 AWST (03:20 UTC)**.
2. **Notify the Support Team Lead now.** Policy 5.2 requires this at escalation of an at-risk P2. The ticket has no record that it was done.
3. **Send the customer an update by 17:30 AWST today (09:30 UTC).** Hannah promised it (section 3).

## 1. Problem
Alarm rule "Vat high temp, above 7°C for 5 min" does not fire for vat 3 (VAT-GW-03). It also did not fire for vats 1 and 2 until the 23 Nov fix.

Verified by support:
- Diagnostic bundles for GW-01, 02 and 03 log `RULE_EVAL_SKIPPED reason=TS_FUTURE` at every evaluation since 12 Nov.
- The gateway clocks ran ahead of sensor timestamps: GW-01 +9m12s, GW-02 +8m40s, GW-03 +11m03s. The 5-minute window never fills, so the rule is skipped.
- NTP fails on all three: `NTP sync failed: timeout (pool.terncloud.net:123)` since 12 Nov. The bundles put all three on VLAN 30.
- TernCloud shows GW-04 to 09 with time sync OK.
- The rule template and SMS recipients are identical on vats 1 to 9.

Reported by customer, not verified:
- Vat 3 exceeded 7°C for about 40 min on Tue night 17 Nov, with no SMS.
- Vat 3 exceeded 7°C again about 01:00 on Mon 23 Nov (customer's local time, assumed AWST), with no SMS.
- The second event ran about 50 min before the night operator caught it on the hourly check, and 18,000 L of milk was dumped.
- Customer IT says nothing changed on VLAN 30 and outbound UDP 123 is allowed. This is relayed through Aroha, and Peter Dunn has not confirmed it directly.

Unconfirmed hypotheses:
- Hannah suspected UDP 123 blocked on VLAN 30. The customer's reply contradicts this.
- Hannah suspects a hardware (RTC) fault on GW-03.

## 2. Tried
| Action | Result |
|---|---|
| Compared alarm rules for vats 1 to 9 | Identical, so config is not the cause |
| Asked customer IT to check UDP 123 on VLAN 30 | Customer says it is allowed (unverified) |
| "Force time sync (HTTPS)" to GW-01 and 02, 23 Nov 02:35 UTC | OK, offset under 1 s. Customer's test at 03:05 UTC: vats 1 and 2 sent SMS |
| Same command to GW-03, 23 Nov 02:35 UTC | `TIME_SET_REJECTED: RTC write error`. Clock still +11m05s. Customer's test: vat 3 sent no SMS |
| Second HTTPS sync to GW-03, 24 Nov 05:15 UTC | Same RTC write error |
| Remote reboot of GW-03, 24 Nov 05:17 UTC (customer agreed by phone at 05:10) | Back online 05:19. Clock still about +11 min |

- NTP is still failing on all three gateways, so GW-01 and 02 may drift again. No drift rate is on file.
- **Vat 3 currently has no working high-temperature SMS alarm.**

## 3. Commitments to the customer
Made by Hannah Odum (Tier 1):
- Update by **17:30 AWST today (09:30 UTC)**. This is the only dated commitment.
- She passed the compensation request to Joel Brandt (account manager). She said she cannot offer compensation herself.

Not made:
- No credit, refund or compensation has been offered. Open credits: none.
- No fix date has been promised.
- Only Joel Brandt or the Head of Customer Support may make a compensation offer, and it must be written on the ticket or account record (6.3). The ticket has no record that Joel received the request, or of any reply. The customer expects the milk cost to be covered.

## 4. Service level
- Plan and priority: Business, P2. Resolution target is 27 business hours (3.1). Priority became P2 on 23 Nov 02:15 UTC, and under 4.3 the target counts from ticket creation.
- Clock start: created Thu 19 Nov 07:50 UTC (15:50 AWST), inside business hours.
- Paused: "Pending customer" from 20 Nov 01:10 to 05:40 UTC. That is 4.5 business hours, all inside business hours.
- Elapsed at 14:00 AWST on 24 Nov:

| Day (AWST) | Counted |
|---|---|
| Thu 19 Nov 15:50 to 17:30 | 1h40 |
| Fri 20 Nov 08:30 to 17:30, less 4.5h paused | 4h30 |
| Mon 23 Nov | 9h |
| Tue 24 Nov 08:30 to 14:00 | 5h30 |
| Total | 20h40 |

- Remaining: 6h20 of 27h, which is below 25% (6h45), so the status is **AT RISK, not breached**.
- **Due Wed 25 Nov 11:20 AWST (03:20 UTC).** This assumes no WA public holidays in the period.
- Why Tier 1 was wrong: the 01:30 note counted 27 hours from the P2 change, and it ignored the creation basis in 4.3.
- First response was met (Fri 20 Nov 01:05 UTC, about 2h15 business time against a 4-hour P2 target).
- Resolution means every fault on the ticket is fixed and the status is Resolved (1.5).

## 5. Recommended next action
1. Tell the Support Team Lead (5.2).
2. Treat GW-03 as a likely hardware fault. Arrange replacement or repair before 25 Nov 11:20 AWST if possible. The site has no spare on record, so check stock and logistics. Plan on-site work at Brunswick Junction, WA.
3. Until GW-03 is fixed, send the customer a vat 3 interim plan. Don't promise a fix date. Hourly checks already failed once, and 18,000 L was lost.
4. Update the customer by 09:30 UTC today with the above. Don't promise credits.
5. Ask Peter Dunn directly to check why only VLAN 30 fails NTP, for example DNS for `pool.terncloud.net` and the firewall logs for UDP 123. The cause is still open for all three gateways.

## Questions and requests for Tier 2
- Is the GW-03 RTC write error a known hardware fault? Is there a firmware workaround, or must it be replaced?
- Can Tier 2 reliably monitor GW-01 and 02 for drift while NTP is broken?
- Please get Joel Brandt (or the Head of Customer Support) to respond on the compensation request, in writing on the ticket.
- Was the Support Team Lead notified? If not, notify now.
- Check whether GW-04 to 09 are in sync only because they are on another VLAN. Also check DEP-GW-01 and 02 at Harvey.
