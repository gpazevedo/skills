# Handoff: TRN-77391, Kestrel Dairy Co-operative (KDC-0418)

## 1. Summary
Kestrel Dairy Co-operative (account KDC-0418, Business plan), Brunswick plant: TernCloud high-temperature SMS alarms do not fire for milk vat 3 (gateway VAT-GW-03, TernGate G4-E, TernCloud alarm rules), and product has already been lost once (18,000 litres). The ticket is P2 and **at risk** on its resolution target (about 6h20m of 27 business hours left, due Wed 25 Nov 2026 11:20 AWST / 03:20 UTC by my count), and Tier 2 now owns an update promised to the customer by 17:30 AWST today (09:30 UTC).

## 2. Problem and evidence
- _reported_ (thread, Aroha Ngata, 2026-11-19 07:50 UTC): vat 3 went above 7°C for about 40 minutes on Tuesday night (17 Nov) with no SMS. Dashboard showed the reading over the limit.
- _reported_ (same message): in a test on all nine vats, vats 4 to 9 sent SMS within a minute; vats 1, 2, 3 sent nothing. One gateway per vat (VAT-GW-01 to 09).
- _verified_ (thread, Hannah Odum note 2026-11-20 07:15 UTC, from diagnostic bundles): TernCloud rule template is identical for vats 1 to 9 with the same SMS recipients (Hannah's 2026-11-20 01:05 message).
- _verified_ (bundles, 2026-11-20 07:15 note): GW-01, 02, 03 log "RULE_EVAL_SKIPPED reason=TS_FUTURE" at every evaluation since 12 Nov. Clocks ahead of sensor timestamps: GW-01 +9 min 12 s, GW-02 +8 min 40 s, GW-03 +11 min 03 s.
- _verified_ (bundles): NTP log on all three: "NTP sync failed: timeout (pool.terncloud.net:123)" since 12 Nov. All three on VLAN 30. TernCloud shows GW-04 to 09 last time sync OK.
- _hypothesis_ (Hannah, same note): UDP 123 blocked for VLAN 30. Not confirmed. _reported_ (Aroha, 2026-11-23 01:40 UTC, relaying IT): nothing changed on VLAN 30 and outbound UDP 123 is allowed. This is unverified and cuts against the hypothesis. The root cause of the NTP failure is therefore unknown.
- _hypothesis_ (rule skipped because the 5-minute window never fills, same note): consistent with the logs, but the mechanism was not tested separately. It is supported by the fact that after the clock fix, vats 1 and 2 alert.
- _verified_ (internal note 2026-11-23 02:40 UTC): after "Force time sync (HTTPS)" at 02:35, GW-01 and 02 show offset under 1 s. GW-03 returned "TIME_SET_REJECTED: RTC write error", clock +11 min 05 s.
- _reported_ (Aroha, 2026-11-23 03:05 UTC): vats 1 and 2 now send SMS in test; vat 3 does not.
- _verified_ (internal note 2026-11-24 05:20 UTC): second HTTPS time sync on GW-03 gave the same RTC write error. After remote reboot (05:17, online 05:19) clock still about +11 min. GW-01/02 still in sync, but NTP still fails on all three, so 01 and 02 may drift again.
- _reported_ (Aroha, 2026-11-23 01:40 UTC): vat 3 went over 7°C again on Sunday night at about 01:00 "our time" with no SMS; over limit about 50 minutes; 18,000 litres dumped. Not independently verified from logs.
- _hypothesis_ (Hannah, 2026-11-24 05:40 UTC, told to customer): GW-03 RTC "may be a hardware fault". Untested.

## 3. Tried so far
| Action | Result | Who |
|---|---|---|
| Compared alarm rules across vats 1 to 9 | Identical; config does not explain it | Hannah Odum, 2026-11-20 |
| Diagnostic bundles from GW-01/02/03 requested and analysed | Found TS_FUTURE skips, clock drift, NTP timeouts | Hannah (request); Aroha (supplied) |
| Asked customer IT to check UDP 123 from VLAN 30 | Customer reports allowed and no changes; not verified by support | Hannah / customer IT via Aroha |
| Force time sync (HTTPS) to GW-01/02/03, 2026-11-23 02:35 UTC | GW-01, 02 OK; GW-03 RTC write error | Hannah |
| Customer alarm test vats 1 to 3 | Vats 1, 2 OK; vat 3 no SMS (reported) | Aroha |
| Second Force time sync (HTTPS) to GW-03, 2026-11-24 05:15 UTC | Same RTC write error | Hannah |
| Remote reboot GW-03, 05:17 UTC (customer agreed by phone 05:10) | Back 05:19; clock still about +11 min | Hannah |
| Re-test of vat 3 after the reboot | result not recorded | none |
| Fix for NTP on the gateways / confirm what blocks UDP 123 | not attempted | none |

## 4. Commitments to the customer
| Quote | Author | Date | Status |
|---|---|---|---|
| "No rush before Monday; the hourly checks cover you over the weekend." | Hannah Odum | 2026-11-20 07:20 UTC | Not a service commitment, but customer relied on it. The ticket later recorded (2026-11-23 02:15 UTC, clause 2.2) that hourly checks are not a practical workaround. Contradiction. |
| "I've passed your request to Joel Brandt, your account manager." (milk cost) | Hannah Odum | 2026-11-23 02:20 UTC | No record on ticket or account of the hand-off to Joel Brandt or of any response. No compensation offered. Policy 6.2 and 6.3 bar agents from promising it; only Joel Brandt or the Head of Customer Support may offer it, in writing. Open. |
| "I'm going to send a command from TernCloud that sets the clock on GW-01 to 03 over HTTPS" | Hannah Odum | 2026-11-23 02:20 UTC | Kept (sent 02:35). Worked for 01 and 02 only. |
| "could you run the alarm test on vats 1 to 3?" (request, not a promise) | Hannah | 2026-11-23 02:20 UTC | Done by customer 03:05. |
| "You'll get an update from us by 17:30 AWST today (09:30 UTC)." | Hannah Odum | 2026-11-24 05:40 UTC | Open; due 2026-11-24 09:30 UTC, 3h30m after the as-of time. Now owned by Tier 2 (clause 5.3). |
| "I've raised the ticket to P2." | Hannah | 2026-11-23 02:20 UTC | Kept (recorded 02:15 UTC). |
No fix date, credit or refund has been promised.

## 5. Service level
- Tier: Business (account record). Priority P2 recorded 2026-11-23 02:15 UTC (clause 2.2, 2.5).
- Resolution target: 27 business hours (clause 3.1, Business P2). Priority change means counting from creation at the new target, excluding paused time (4.3).
- Clock start: ticket created Thu 2026-11-19 07:50 UTC (15:50 AWST), inside business hours (4.1).
- Pause: "Pending customer" 2026-11-20 01:10 to 05:40 UTC, 4h30m, all within business hours (4.2). Deducted.
- Business-hours elapsed to as-of 2026-11-24 06:00 UTC:
  - Thu 19 Nov 07:50 to 09:30 UTC = 1h40m
  - Fri 20 Nov 00:30 to 09:30 UTC = 9h00m, minus 4h30m paused = 4h30m
  - Sat/Sun excluded (1.1)
  - Mon 23 Nov 00:30 to 09:30 UTC = 9h00m
  - Tue 24 Nov 00:30 to 06:00 UTC = 5h30m
  - Total 20h40m (20.67 h)
- Remaining: 27h minus 20h40m = 6h20m.
- Deadline: Tue has 3h30m left (to 09:30 UTC); the remaining 2h50m falls on Wed 25 Nov from 00:30 UTC, giving **Wed 2026-11-25 03:20 UTC = 11:20 AWST**.
- Status (4.4): at risk threshold is 25% of 27 h = 6h45m. Remaining 6h20m is less, so **at risk**, not breached. (No WA public holiday is stated in the supplied material; I assumed none.)
- First response (P2 first response is 4 business hours, 3.1): created 07:50 UTC Thu, first agent contact Fri 01:05 UTC = 1h40m + 35m = 2h15m elapsed. Met (and under P3 as well).
- Customer-update cadence for P2 (7.1): at least once each business day. Updates exist on 20, 23, 24 Nov. Today's update is the 09:30 UTC promise above.
- Tier 1's note of 2026-11-24 01:30 UTC ("due Thu 26 Nov 10:15 AWST, plenty of time") is wrong: it counted 27 hours from the P2 change and ignored clock start at creation (4.3) and the pause. Do not use that date.

## 6. Recommended next action
Primary (owner: Field Systems Engineering, Tier 2): treat GW-03 as the open fault and decide whether its RTC is faulty, for example by pulling the GW-03 RTC and firmware state and log from the existing bundle and a fresh one, then arrange a hardware swap or on-site visit, as appropriate. This confirms or rules out the "hardware fault" hypothesis, which nothing has tested. Serves: the open 17:30 AWST (09:30 UTC) update commitment, and the resolution deadline of 2026-11-25 11:20 AWST. Resolution under 1.5 needs a fix or workaround that restores vat 3 alerting.

Alternatives and parallel items:
1. Support Team Lead notification now (owner: Tier 1/Tier 2 hand-off): clause 5.2 requires it at escalation of an at-risk P2. None recorded. Also confirm the hand-off to Joel Brandt about the compensation request is recorded in writing.
2. Interim cover for vat 3 while GW-03 is unresolved (owner: Tier 2, with Aroha): agree and record a practical alternative, and confirm it before the update. The hourly check is already judged impractical. Do not promise a fix date or compensation (6.2).
3. NTP root cause (owner: Tier 2, with Peter Dunn, IT Coordinator): confirm outbound UDP 123 from VLAN 30 with a packet capture or firewall log, because GW-01/02 may drift again. This would confirm or refute the blocked-port hypothesis.
4. Have Aroha re-test vat 3 after the reboot (result not recorded).

## 7. Gaps and conflicts
- No record that the Support Team Lead was notified (5.2).
- No record the account manager (Joel Brandt) has the compensation request; no response from him.
- Customer says UDP 123 is open and nothing changed, versus support's blocked-port hypothesis. GW-04 to 09 sync fine; why only VLAN 30 gateways fail is unexplained.
- SLA date conflict: Tier 1 note (Thu 26 Nov 10:15 AWST) versus clause-based calculation here (Wed 25 Nov 11:20 AWST).
- Hourly-check statement of 2026-11-20 contradicts the priority reason recorded 2026-11-23.
- Timing of the second vat 3 miss: "Sunday night at about 01:00 our time" is ambiguous (night of 22 Nov, so 01:00 AWST on Mon 23 Nov or Sun 22 Nov) and not corroborated by logs. First incident described as "Tuesday night" (17 Nov) with no time given. Both are _reported_.
- No logs or sensor timestamps for either missed alarm were supplied, only the gateway bundles for 01 to 03; no bundle from after the reboot.
- Hannah's 2026-11-24 05:40 message was sent to the customer before the escalation event at 06:00 UTC.
- Policy does not define what counts as a fix for a faulty gateway (hardware replacement lead time), and gives no workaround definition beyond 2.2/2.3; no SLA term stated for compensation.
