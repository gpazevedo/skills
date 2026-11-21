# Escalation handoff: TRN-77391, Kestrel Dairy Co-operative (KDC-0418)

**In one line:** High-temperature SMS alarms do not fire for vat gateways VAT-GW-01 to 03 because their clocks run fast; GW-01 and GW-02 are fixed for now, GW-03 refuses a clock set (possible hardware fault) and has already cost the customer 18,000 L of milk. The P2 resolution target is "at risk" (about 6 h 20 min of business time left, deadline Wed 25 Nov 11:20 AWST) and a customer update is promised by 09:30 UTC today.

## Problem as currently understood
- [verified] On VAT-GW-01, 02 and 03 the rule engine logs "RULE_EVAL_SKIPPED reason=TS_FUTURE" at every evaluation since 12 Nov (evidence: Hannah Odum read the diagnostic bundles, internal note 2026-11-20 07:15 UTC).
- [verified] Clock offsets at that time: GW-01 +9 min 12 s, GW-02 +8 min 40 s, GW-03 +11 min 03 s (evidence: same bundle read, 2026-11-20 07:15 UTC).
- [verified] NTP log on all three: "NTP sync failed: timeout (pool.terncloud.net:123)", repeated since 12 Nov; bundles put GW-01 to 03 on VLAN 30 (evidence: same bundle read). TernCloud shows GW-04 to 09 with last time sync OK (Hannah, same note).
- [verified] Alarm rules are the same on vats 1 to 9: template "Vat high temp, above 7°C for 5 min", same SMS recipients (evidence: Hannah checked the rules in TernCloud, 2026-11-20 01:05 UTC).
- [verified] After "Force time sync (HTTPS)" sent 2026-11-23 02:35 UTC, GW-01 and GW-02 returned OK with offset under 1 s; GW-03 returned "TIME_SET_REJECTED: RTC write error", clock +11 min 05 s (evidence: Hannah, internal note 2026-11-23 02:40 UTC).
- [verified] Second forced sync on GW-03 at 05:15 UTC on 2026-11-24 gave the same RTC write error; after a remote reboot (05:17, back 05:19) the clock is still about +11 min. GW-01 and GW-02 still in sync (evidence: Hannah, internal note 2026-11-24 05:20 UTC).
- [verified] Account facts: Business plan, contract 1 Mar 2026 to 28 Feb 2028, Site subscription, Brunswick VAT-GW-01 to 09 (G4-E, one per vat), alarms by TernCloud SMS to the plant on-call roster (evidence: account record).
- [reported] Vat 3 went above 7°C for about 40 minutes on Tuesday night (17 Nov) with no SMS; the dashboard showed the reading over the limit (source: Aroha Ngata, 2026-11-19 07:50 UTC).
- [reported] Alarm test on all nine vats on 19 Nov: vats 4 to 9 sent SMS within a minute; vats 1, 2, 3 sent nothing (source: Aroha, 2026-11-19 07:50 UTC).
- [reported] After the 23 Nov clock fix, test: vats 1 and 2 sent SMS within a minute, vat 3 sent nothing (source: Aroha, 2026-11-23 03:05 UTC; support did not state it checked this itself).
- [reported] Vat 3 went over 7°C again about 01:00 local on Sunday night (22/23 Nov), no SMS, over the limit about 50 minutes before the hourly manual check caught it; 18,000 litres dumped (source: Aroha, 2026-11-23 01:40 UTC).
- [reported] Customer IT says nothing changed on VLAN 30 and outbound UDP 123 is allowed (source: Aroha relaying IT, 2026-11-23 01:40 UTC). Not checked by support.
- [reported] Night staff check the dashboard hourly as an interim measure (source: Aroha, 2026-11-19 07:50 UTC and 2026-11-23 01:40 UTC).
- [suspected] The fast clocks cause the missed alarms (held by: Hannah; basis: TS_FUTURE skips plus the 5-minute window, and the customer-reported pass on vats 1 and 2 after the clock fix; the causal link itself has no recorded direct check).
- [suspected] UDP 123 is blocked for VLAN 30 (held by: Hannah, "Not confirmed", 2026-11-20 07:15 UTC; basis: only the three failing gateways are on VLAN 30). Contradicted by the customer's IT report above.
- [suspected] GW-03 has a hardware fault in its real-time clock (held by: Hannah, "may be a hardware fault", 2026-11-24 05:40 UTC; basis: repeated RTC write error, unchanged after reboot).
- [suspected] GW-01 and GW-02 may drift again because NTP still fails (held by: Hannah, 2026-11-24 05:20 UTC).
- Conflicts: (1) Hannah's SLA note (2026-11-24 01:30 UTC) gives a due time of Thu 26 Nov 10:15 AWST; that is wrong under the policy, see Service level. (2) Whether UDP 123 is open from VLAN 30: customer IT says yes; support suspects no; unresolved. (3) No tier or contact conflicts between thread and account record.

## Tried so far
| What was tried | Who, when | Result |
|---|---|---|
| Checked alarm rules in TernCloud for vats 1 to 9 | Hannah, 2026-11-20 01:05 UTC | Same template and recipients; config does not explain the difference |
| Asked customer for diagnostic bundles from GW-01 to 03 | Hannah, 2026-11-20 01:10 UTC (customer supplied 05:40 UTC) | Bundles received; showed TS_FUTURE skips, fast clocks, NTP timeouts |
| Asked customer IT to check outbound UDP 123 from VLAN 30 | Hannah, 2026-11-20 07:20 UTC; customer IT | IT reports no change and UDP 123 allowed (reported, not checked by support) |
| "Force time sync (HTTPS)" to GW-01, 02, 03 | Hannah, 2026-11-23 02:35 UTC | GW-01, 02 OK (under 1 s); GW-03 TIME_SET_REJECTED: RTC write error |
| Customer alarm test on vats 1 to 3 after sync | Aroha at Hannah's request, 2026-11-23 03:05 UTC | Vats 1, 2 sent SMS; vat 3 nothing (reported) |
| Raised priority P3 to P2 | Hannah, 2026-11-23 02:15 UTC | Recorded with reason citing clause 2.2 |
| Passed the compensation request to account manager Joel Brandt | Hannah, 2026-11-23 02:20 UTC (stated in customer message) | No response from Joel recorded |
| Second forced time sync on GW-03 | Hannah, 2026-11-24 05:15 UTC | Same RTC write error |
| Remote reboot of GW-03 (customer agreed by phone 05:10) | Hannah, 2026-11-24 05:17 UTC | Back online 05:19; clock still about +11 min |
| Customer's interim measure: hourly dashboard checks | Plant night staff | Missed or late catch on 23 Nov; milk lost |

## Commitments to the customer
| Commitment (quoted) | Made by | When | Due | Status |
|---|---|---|---|---|
| "You'll get an update from us by 17:30 AWST today (09:30 UTC)." | Hannah Odum (named agent, Tier 1) | 2026-11-24 05:40 UTC | 2026-11-24 09:30 UTC | Pending (3 h 30 min left as of 06:00 UTC). Tier 2 owns it (policy 5.3) |

Not commitments: the customer's request that the cost of the milk be covered is a claim (customer asked); nobody agreed to it. Hannah said "I've passed your request to Joel Brandt" (an action she took; not a promise of an outcome) and "I'm not able to offer compensation myself". No credit, refund, compensation or fix date has been promised; the account record shows "Open credits: None". Hannah's "No rush before Monday" is not a commitment.

## Service level
- Tier: Business (account record, "Support plan: Business").
- Priority/severity: P2 since 2026-11-23 02:15 UTC (thread event; originally P3 at creation).
- Target: Business P2, first response 4 business hours, resolution 27 business hours (policy 3.1 table). Policy 4.3: "the resolution target becomes the target for the new priority, counted from ticket creation and excluding paused time."
- Clock rule: starts at ticket creation (4.1); business hours 08:30 to 17:30 AWST Mon to Fri excluding WA public holidays (1.1), i.e. 00:30 to 09:30 UTC (1.2); paused only while status is "Pending customer" (4.2).
- Deadline (arithmetic, AWST = UTC+8):
  - Created Thu 19 Nov 15:50 AWST (07:50 UTC), inside business hours.
  - Business time elapsed to 24 Nov 06:00 UTC (Tue 14:00 AWST): Thu 15:50 to 17:30 = 1 h 40 min; Fri 9 h; Mon 9 h; Tue 08:30 to 14:00 = 5 h 30 min; weekend 0. Total 25 h 10 min.
  - Paused: Pending customer Fri 20 Nov 01:10 to 05:40 UTC (09:10 to 13:40 AWST), all in business hours = 4 h 30 min.
  - Counted: 25 h 10 min - 4 h 30 min = 20 h 40 min. Remaining: 27 h - 20 h 40 min = 6 h 20 min.
  - Deadline with pause applied: Tue 24 Nov 14:00 AWST + 3 h 30 min (to 17:30) + 2 h 50 min from Wed 08:30 = Wed 25 Nov 11:20 AWST (03:20 UTC).
  - Deadline if the pause were ignored: 1 h 50 min left, Tue 24 Nov 15:50 AWST (07:50 UTC). The pause is recorded in the thread, so the first figure is the one to use. No WA public holiday falls in the window as far as the supplied material shows; the policy lists none.
  - Hannah's figure (Thu 26 Nov 10:15 AWST) counts from the priority change and ignores 4.3, so it overstates the time left by about 1.5 business days.
- First response: met. Hannah's first contact was 2026-11-20 01:05 UTC (Fri 09:05 AWST), 2 h 15 min of business time after creation, inside both the P3 (9 h) and P2 (4 h) targets.
- Status: at risk (policy 4.4: under 25% of 27 h = 6 h 45 min remaining; 6 h 20 min remains), not breached, as of 2026-11-24 06:00 UTC (the as-of time given in the ticket export).
- Update cadence: P2 needs an update at least once each business day (7.1). Escalation of an at-risk P2 requires notifying the Support Team Lead (5.2).
- Credits/compensation: only the Account Manager (Joel Brandt) or Head of Customer Support may offer, in writing on the ticket or account record (6.3). Agents must not promise a fix date, credit, refund or compensation (6.2). Any service-level credit terms beyond this: not stated in policy.

## Recommended next action
1. Notify the Support Team Lead now: policy 5.2 requires it for an at-risk P2 escalation and the thread records no notification.
2. Take a fresh diagnostic bundle from GW-03 (via the customer's local page, or TernCloud if it supports it) and read the RTC and time-subsystem logs, then compare with GW-01. This is the cheapest check on the leading suspected cause.
   - RTC write error or hardware fault shown: GW-03 hardware is confirmed as the cause; the path is a replacement or workaround for vat 3, and the customer update must say that without promising a date (6.2).
   - No hardware fault shown (for example a firmware or config issue): try a documented firmware or config remedy on GW-03 and re-test vat 3.
3. In parallel, because NTP is failing on all three gateways, GW-01 and GW-02 may drift again: check from TernCloud whether UDP 123 to pool.terncloud.net really works from VLAN 30 (customer IT says yes, Hannah suspects no). If blocked, ask Peter Dunn (IT Coordinator, network contact) to open it; this protects vats 1 and 2.
4. Customer update must go out by 2026-11-24 09:30 UTC (17:30 AWST), owned by Tier 2: say what is confirmed (vats 1 and 2 fixed, vat 3 still unprotected), what is being checked, and the next update time. Remind the customer to keep the hourly checks on vat 3 until it is fixed (and on vats 1 and 2 until NTP is sound). Do not state a fix date, credit or compensation.
5. Resolution needs a fix or workaround for vat 3 and status Resolved (1.5) by Wed 25 Nov 11:20 AWST.
6. Ask Joel Brandt to respond to the compensation request in writing on the ticket; Tier 2 must not comment on it.

## Gaps
- No record that the Support Team Lead was notified at escalation (policy 5.2).
- No response from Joel Brandt on the compensation request recorded; nothing states that he received it beyond Hannah's message.
- Whether outbound UDP 123 from VLAN 30 is open: not checked by support; sources conflict.
- No direct check that the fast clocks cause the missed SMS; the evidence is the log reason plus the customer-reported test results.
- Vats 1 and 2 passes are customer-reported; support has not re-tested or confirmed the sync stays stable.
- Public holidays in the window: policy lists none; none seen in the material.
- Hardware diagnostics of GW-03 not examined since the reboot; no bundle after 20 Nov.
- Policy and account record do not state any contractual service credit terms for missed alarms: not stated in policy or account record.
