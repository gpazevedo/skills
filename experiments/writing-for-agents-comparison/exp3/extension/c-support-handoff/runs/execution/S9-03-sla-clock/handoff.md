# Escalation handoff: TRN-77391, Kestrel Dairy Co-operative (KDC-0418)

**In one line:** Vat 3 at the Brunswick plant still has no high-temperature SMS alarm because gateway VAT-GW-03 rejects every attempt to set its clock (about 11 min fast), after a missed alarm already cost the customer 18,000 litres; an update is promised by 09:30 UTC today (24 Nov), and the P2 resolution deadline is Wed 25 Nov 03:20 UTC, which the ticket was already "at risk" against when it was escalated.

## Problem as currently understood
- [reported] Vat 3 went above 7°C for about 40 minutes on Tuesday night (17 Nov) and nobody received the high-temperature SMS; the customer says the TernCloud dashboard shows the reading over the limit. (source: Aroha Ngata, Plant Engineer, 19 Nov 07:50 UTC)
- [reported] In a customer test of all nine vats, vats 4 to 9 sent the SMS within a minute and vats 1, 2 and 3 sent nothing. Each vat has its own gateway (VAT-GW-01 to 09). (source: Aroha Ngata, 19 Nov 07:50 UTC)
- [verified] Vats 1 to 9 all use the same alarm rule template ("Vat high temp, above 7°C for 5 min") with the same SMS recipients, so configuration does not explain the difference. (evidence: Hannah Odum checked the alarm rules in TernCloud, 20 Nov 01:05 UTC)
- [verified] On GW-01, 02 and 03 the rule engine has logged "RULE_EVAL_SKIPPED reason=TS_FUTURE" at every evaluation since 12 Nov. Gateway clocks were ahead of sensor timestamps: GW-01 +9 min 12 s, GW-02 +8 min 40 s, GW-03 +11 min 03 s. Hannah's reading: the rule needs 5 minutes of readings, the window never fills, so the rule is skipped. (evidence: Hannah Odum read the customer's diagnostic bundles, internal note 20 Nov 07:15 UTC)
- [verified] NTP on all three gateways logs "NTP sync failed: timeout (pool.terncloud.net:123)" repeatedly since 12 Nov. The bundles place GW-01 to 03 on VLAN 30; TernCloud shows GW-04 to 09 with last time sync OK. (evidence: same bundle review and TernCloud check, Hannah Odum, 20 Nov 07:15 UTC)
- [reported] Customer IT says nothing has changed on VLAN 30 and outbound UDP 123 is allowed. (source: Aroha Ngata relaying IT, 23 Nov 01:40 UTC; no detail of how IT checked)
- [suspected] UDP 123 blocked for VLAN 30 as the cause of the NTP failures. (held by: Hannah Odum, 20 Nov 07:15 UTC, "Not confirmed"; basis: only the VLAN 30 gateways fail NTP. Now contradicted by the customer IT report above, and not checked by Tern)
- [reported] Vat 3 went over 7°C again at about 01:00 local time on "Sunday night" (most likely early Mon 23 Nov AWST, about 22 Nov 17:00 UTC; exact time not stated), no SMS; the night operator caught it on the hourly check after about 50 minutes over the limit, and 18,000 litres were dumped. Customer says hourly checks cannot continue and are not enough, and asks for the cost of the milk to be covered. (source: Aroha Ngata, 23 Nov 01:40 UTC)
- [verified] "Force time sync (HTTPS)" fixed GW-01 and GW-02 (offset under 1 s). GW-03 returned "TIME_SET_REJECTED: RTC write error"; clock still +11 min 05 s. (evidence: Hannah Odum, command sent 23 Nov 02:35 UTC, results in internal note 02:40 UTC)
- [reported] After the sync, vats 1 and 2 sent the SMS within a minute; vat 3 still sent nothing. (source: Aroha Ngata, 23 Nov 03:05 UTC)
- [verified] A second forced sync to GW-03 gave the same "TIME_SET_REJECTED: RTC write error"; a remote reboot (back online 05:19) left the clock still +11 min. GW-01 and GW-02 still in sync (under 1 s). NTP still failing on all three. (evidence: Hannah Odum, internal note 24 Nov 05:20 UTC)
- [suspected] GW-03 has a hardware fault in its real-time clock. (held by: Hannah Odum, 24 Nov 05:40 UTC, "may be a hardware fault"; basis: RTC write error persists across two time sets and a reboot, while the same command worked on GW-01 and 02)
- [suspected] GW-01 and GW-02 will drift again and vats 1 and 2 will lose their alarms again, because NTP is still failing. (held by: Hannah Odum, 24 Nov 05:20 UTC; basis: the forced sync is one-off and the NTP timeouts continue)
- Conflicts:
  - Customer IT says outbound UDP 123 from VLAN 30 is allowed; the gateway logs show NTP timeouts to pool.terncloud.net:123 on all three VLAN 30 gateways since 12 Nov. Neither side's claim has been tested further.
  - Hannah Odum's internal SLA note (24 Nov 01:30 UTC) gives a due time of Thu 26 Nov 10:15 AWST, counted from the P2 change. Policy 4.3 counts the new target from ticket creation, which gives Wed 25 Nov 11:20 AWST (see Service level). The earlier time governs.
  - Account facts: none. The customer did not state a plan; the account record says Business.

## Tried so far
| What was tried | Who, when | Result |
|---|---|---|
| Alarm test on all nine vats | Aroha Ngata (customer, on her own initiative), 19 Nov, reported 07:50 UTC | Vats 4 to 9 SMS within a minute; vats 1 to 3 nothing |
| Checked alarm rule configuration in TernCloud | Hannah Odum (Tier 1), 20 Nov 01:05 UTC | Same template and recipients on all nine vats |
| Diagnostic bundles downloaded from GW-01, 02, 03 and reviewed | Aroha Ngata at Hannah's request, attached 20 Nov 05:40 UTC; reviewed by Hannah Odum 07:15 UTC | TS_FUTURE rule skips and NTP timeouts since 12 Nov; clocks 8 to 11 min fast; all three on VLAN 30 |
| Customer IT check of outbound UDP 123 from VLAN 30 | Customer IT at Hannah's request (20 Nov 07:20 UTC), reported 23 Nov 01:40 UTC | "nothing has changed on VLAN 30 and outbound UDP 123 is allowed"; method not stated |
| Priority raised P3 to P2 | Hannah Odum, 23 Nov 02:15 UTC | Recorded; reason cites clause 2.2 |
| Compensation request passed to account manager Joel Brandt | Hannah Odum, 23 Nov 02:20 UTC | No result recorded |
| "Force time sync (HTTPS)" to GW-01, 02, 03 | Hannah Odum, 23 Nov 02:35 UTC | GW-01, 02 OK (under 1 s); GW-03 "TIME_SET_REJECTED: RTC write error", +11 min 05 s |
| Alarm test on vats 1 to 3 | Aroha Ngata at Hannah's request, reported 23 Nov 03:05 UTC | Vats 1 and 2 SMS within a minute; vat 3 nothing |
| Second "Force time sync (HTTPS)" to GW-03 | Hannah Odum, 24 Nov 05:15 UTC | Same "TIME_SET_REJECTED: RTC write error" |
| Remote reboot of GW-03 from TernCloud (customer agreed by phone 05:10) | Hannah Odum, 24 Nov 05:17 UTC | Back online 05:19; clock still +11 min |
| Escalated to Tier 2 (Field Systems Engineering) | Hannah Odum, 24 Nov 06:00 UTC | Status Escalated, P2 |

## Commitments to the customer
| Commitment (quoted) | Made by | When | Due | Status |
|---|---|---|---|---|
| "I'm going to send a command from TernCloud that sets the clock on GW-01 to 03 over HTTPS" | Hannah Odum (Tier 1) | 23 Nov 02:20 UTC | No date given | Met (sent 23 Nov 02:35 UTC) |
| "I'm escalating this to our Field Systems Engineering team now." | Hannah Odum (Tier 1) | 24 Nov 05:40 UTC | Immediately ("now") | Met (escalated 24 Nov 06:00 UTC) |
| "You'll get an update from us by 17:30 AWST today (09:30 UTC)." | Hannah Odum (Tier 1) | 24 Nov 05:40 UTC | 24 Nov 09:30 UTC (17:30 AWST) | Pending, 3 h 30 min left as of 24 Nov 06:00 UTC. Tier 2 now owns it (policy 5.3: "From escalation, Tier 2 owns the ticket, including customer updates and commitments already made.") |

Not a commitment: the customer asked for the cost of the dumped milk to be covered (23 Nov 01:40 UTC). Hannah said "I'm not able to offer compensation myself" and passed the request to Joel Brandt. No offer is recorded on the ticket, and the account record shows "Open credits: None". Under policy 6.2 and 6.3, Tier 2 must not promise compensation; only Joel Brandt (named Account Manager) or the Head of Customer Support may offer it, in writing on the ticket or account record.

## Service level
- Tier: Business support plan (account record, "Support plan: Business"; policy 1.3 makes the account record authoritative)
- Priority/severity: P2 since 23 Nov 02:15 UTC; P3 at creation (ticket events 19 Nov 07:50 UTC and 23 Nov 02:15 UTC)
- Target: policy 3.1, Business / P2: "4 business hours" first response, "27 business hours" resolution. (Business / P3, which applied at creation: "9 business hours" first response, "72 business hours" resolution.)
- Clock rule:
  - Policy 4.1: "The clock starts when the ticket is created. Business-hours targets count only time inside business hours".
  - Policy 1.1 / 1.2: business hours "08:30 to 17:30 Australia/Perth time ... Monday to Friday, excluding Western Australian public holidays", which is "00:30 to 09:30 UTC on the same date".
  - Policy 4.2: "The clock is paused only while the ticket status is "Pending customer"."
  - Policy 4.3: "If the priority changes, the resolution target becomes the target for the new priority, counted from ticket creation and excluding paused time."
  - Resolution (policy 1.5) needs "a fix or a workaround that restores the affected function" and status Resolved; "A ticket that reports more than one fault is resolved only when every fault on it is resolved."
- First response: met. Ticket created Thu 19 Nov 07:50 UTC (inside business hours); first agent contact Fri 20 Nov 01:05 UTC. Elapsed: Thu 07:50 to 09:30 = 1 h 40 min, Fri 00:30 to 01:05 = 35 min, total 2 h 15 min, within both the P3 9 h and the P2 4 h targets.
- Deadline (resolution): **Wed 25 Nov 2026 03:20 UTC (11:20 AWST)**
  - Arithmetic, business hours counted from creation:
    - Thu 19 Nov: 07:50 to 09:30 UTC = 1 h 40 min (running 1 h 40 min)
    - Fri 20 Nov: 00:30 to 09:30 = 9 h, minus Pending customer 01:10 to 05:40 = 4 h 30 min, so 4 h 30 min (running 6 h 10 min)
    - Sat 21, Sun 22 Nov: 0
    - Mon 23 Nov: 9 h (running 15 h 10 min)
    - Tue 24 Nov: 9 h (running 24 h 10 min)
    - Wed 25 Nov: remaining 27 h minus 24 h 10 min = 2 h 50 min, so 00:30 + 2 h 50 min = 03:20 UTC
  - The status history in the export shows one pause only (20 Nov 01:10 to 05:40). For checking: without the pause the deadline would be Tue 24 Nov 07:50 UTC.
  - Assumes no WA public holiday falls between 19 and 25 Nov; the holiday calendar is not stated in the supplied sources.
- Status: **open, and "at risk" under policy 4.4**, with 6 h 20 min of business time remaining (Tue 06:00 to 09:30 UTC = 3 h 30 min, plus Wed 00:30 to 03:20 UTC = 2 h 50 min), as of 24 Nov 06:00 UTC. "Now" is the last timestamp in the thread (the escalation event); no current time was supplied with the case.
  - At-risk threshold: 25% of 27 h = 6 h 45 min remaining, crossed at 20 h 15 min elapsed, which is Tue 24 Nov 05:35 UTC. So the ticket was at risk when escalated at 06:00 UTC.
  - Policy 5.2: "When a P1 ticket, or an at-risk P2 ticket, is escalated, the Support Team Lead must be notified at escalation." The thread records no such notification.
- Customer update cadence: policy 7.1, "P2: at least once each business day". Next one due on Wed 25 Nov at the latest, in addition to the 09:30 UTC commitment today.

## Recommended next action
1. **Now:** notify the Support Team Lead that this at-risk P2 was escalated (policy 5.2), since the thread does not record it.
2. **Main action:** confirm or rule out the GW-03 real-time clock hardware fault from GW-03's own logs. Ask Aroha Ngata (primary technical contact) for a fresh diagnostic bundle from VAT-GW-03 (local web page, Maintenance > Diagnostics > Download bundle), taken after the 24 Nov 05:15 time-set rejection and the 05:17 reboot. Read it for entries around "TIME_SET_REJECTED: RTC write error", and for any record of what fails when the gateway tries to write its clock.
   - If the logs show an RTC write failure at the hardware level: treat GW-03 as faulty hardware and arrange a replacement gateway for vat 3. The replacement process and timing are not stated in the supplied sources. A swap is unlikely to finish before the Wed 03:20 UTC deadline, so tell the customer plainly that the deadline is at risk.
   - If the logs show the write being refused for another reason (for example, a software or configuration state): the hardware theory is ruled out, and the fix is to clear that state and repeat "Force time sync (HTTPS)", then have the customer rerun the vat 3 alarm test.
3. **Parallel, second fault:** the NTP failure on VLAN 30 is still unexplained and will let GW-01 and 02 drift out again. The customer's "UDP 123 is allowed" report is untested. Ask Peter Dunn (IT Coordinator, network contact in the account record) for evidence of how that was checked, and track it as a separate fault on this ticket. Policy 1.5 requires every fault resolved before the ticket counts as resolved.
4. **Customer update due first: by 24 Nov 09:30 UTC (17:30 AWST) today**, owned by Tier 2. Send it from the Tier 2 engineer. It should:
   - say Field Systems Engineering has the case;
   - state that vat 3 still has no SMS alarm, so manual monitoring of vat 3 must continue for now;
   - make the GW-03 bundle request;
   - give the time of the next update (no later than Wed 25 Nov business hours, per 7.1).
   Do not promise a fix date or compensation (policy 6.2); the compensation request sits with Joel Brandt.

## Gaps
- No working protection for vat 3 has been identified. The customer says hourly checks are neither sustainable nor sufficient, and no interim alternative (for example, any way to alarm on vat 3 without GW-03's clock) is discussed in the thread.
- Root cause of the NTP timeouts on VLAN 30 since 12 Nov is unknown. Tern has not tested reachability of pool.terncloud.net:123 from VLAN 30, and customer IT's check method is not recorded. What changed on 12 Nov is not established.
- GW-03 hardware fault is suspected only. No hardware diagnostic has been run, and no replacement or RMA process is stated in the supplied sources.
- No response from Joel Brandt to the compensation request is recorded. On 20 Nov 07:20 UTC Tier 1 told the customer "No rush before Monday; the hourly checks cover you over the weekend", before the 18,000-litre loss. The account manager should be aware of this when answering the request.
- Exact time of the second incident is ambiguous ("Sunday night ... about 01:00 our time").
- Support Team Lead notification at escalation (policy 5.2) is not recorded.
- WA public holiday calendar for the counting window is not stated in the supplied sources (deadline assumes none).
- The customer's first-incident dashboard observation and both of the customer's alarm-test results have not been independently checked by Tern (for example, against TernCloud alarm/SMS delivery logs).
