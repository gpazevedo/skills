# Handoff: TRN-77391, Kestrel Dairy Co-operative (KDC-0418)

As-of: 2026-11-24 06:00 UTC (14:00 AWST, Tuesday). All three inputs (thread, account record, policy v2026.2) were provided.

## 1. Summary
High-temperature SMS alarms do not fire for vat 3 (GW-03) at Brunswick because its clock runs about 11 minutes fast and will not accept a time set; a second milk loss (18,000 L) has already occurred. The P2 resolution target is at risk, with the deadline at Wed 25 Nov 2026 11:20 AWST (03:20 UTC), and an update is owed to the customer by 09:30 UTC today.

## 2. Problem as understood

Reported (customer or agent assertion, no check shown):
- Vat 3 exceeded 7°C for about 40 minutes on Tuesday night (17 Nov) with no SMS (Aroha Ngata, 19 Nov 07:50 UTC).
- Vat 3 exceeded 7°C again about 01:00 Sunday night (22 Nov) for about 50 minutes, no SMS; 18,000 L of milk dumped (Aroha, 23 Nov 01:40 UTC).
- Initial test: vats 4 to 9 sent SMS, vats 1 to 3 did not (Aroha, 19 Nov).
- After the HTTPS time sync, vats 1 and 2 sent SMS and vat 3 did not (Aroha, 23 Nov 03:05 UTC).
- Customer IT says nothing changed on VLAN 30 and outbound UDP 123 is allowed (Aroha, relaying IT, 23 Nov 01:40 UTC). Not checked by support.
- Hypothesis, unconfirmed: UDP 123 blocked for VLAN 30 (Hannah's note, 20 Nov 07:15 UTC, "Not confirmed"). The customer's IT statement contradicts it, and the NTP timeout is unexplained.
- Customer is asking for the cost of the milk to be covered, and says hourly manual checks by night staff are not sustainable.

Verified (support observed, with source):
- Rules for vats 1 to 9 use the same template ("Vat high temp, above 7°C for 5 min") and the same recipients (TernCloud rule check, Hannah, 20 Nov 01:05 UTC).
- GW-01, 02, 03 log "RULE_EVAL_SKIPPED reason=TS_FUTURE" at every evaluation since 12 Nov (diagnostic bundles, internal note 20 Nov 07:15 UTC).
- Clock offsets at that time: GW-01 +9 min 12 s, GW-02 +8 min 40 s, GW-03 +11 min 03 s (bundles).
- NTP log on all three: "NTP sync failed: timeout (pool.terncloud.net:123)" since 12 Nov (bundles).
- GW-01 to 03 are on VLAN 30 (bundles). TernCloud shows GW-04 to 09 with last time sync OK.
- After "Force time sync (HTTPS)" at 23 Nov 02:35 UTC, GW-01 and 02 returned OK with offset under 1 s. GW-03 returned "TIME_SET_REJECTED: RTC write error", offset +11 min 05 s (internal note 23 Nov 02:40 UTC).
- Second HTTPS sync to GW-03 on 24 Nov at 05:15 UTC gave the same rejection. After a remote reboot (05:17, back 05:19 UTC) the clock was still about +11 min (internal note 24 Nov 05:20 UTC). GW-01 and 02 were still in sync at that time.
- Account record: Business plan, GW-01 to 09 at Brunswick (model G4-E), alarm delivery by TernCloud SMS to the plant on-call roster.
- Priority P3 to P2 at 23 Nov 02:15 UTC, recorded on the ticket with reason (ticket event).

Not established: the cause of the NTP timeouts, and whether the RTC write error is a hardware fault (Hannah says "may be"). Whether the clock offset is the sole cause of the vat 3 alarm failure is an inference from the TS_FUTURE log on the three bundles. No bundle from GW-03 after the reboot is in the thread.

## 3. Tried so far

| Action | By | Result |
| --- | --- | --- |
| Compared alarm rule templates and recipients, vats 1 to 9 | Hannah Odum, 20 Nov | Worked as diagnosis: config identical, ruled out as cause |
| Requested and analysed diagnostic bundles for GW-01, 02, 03 | Hannah / Aroha, 20 Nov | Worked as diagnosis: found TS_FUTURE skips, clock drift, NTP failure |
| Asked customer IT to check outbound UDP 123 from VLAN 30 | Hannah, 20 Nov | Inconclusive: IT reports allowed, NTP still fails, unverified by support |
| "Force time sync (HTTPS)" to GW-01, 02, 03 | Hannah, 23 Nov 02:35 UTC | Worked for GW-01 and 02 (offset under 1 s, vats 1 and 2 alarm per customer test); failed for GW-03 (RTC write error) |
| Second "Force time sync (HTTPS)" to GW-03 | Hannah, 24 Nov 05:15 UTC | Failed: same RTC write error |
| Remote reboot of GW-03 (customer agreed by phone 05:10 UTC) | Hannah, 24 Nov 05:17 UTC | Failed: clock still about +11 min |
| Raised priority to P2 | Hannah, 23 Nov | Done |
| Passed compensation request to Account Manager Joel Brandt | Hannah, 23 Nov | Unknown: no response or outcome recorded |
| Customer interim measure: hourly dashboard checks by night staff | Customer | Inconclusive as a workaround; failed on 22 Nov (50 minutes over limit, milk dumped) |

## 4. Commitments to the customer

| Quote | Who | When |
| --- | --- | --- |
| "You'll get an update from us by 17:30 AWST today (09:30 UTC)." | Hannah Odum | 24 Nov 05:40 UTC |
| "I've passed your request to Joel Brandt, your account manager." (action on herself, done; see below) | Hannah Odum | 23 Nov 02:20 UTC |

- Ownership: policy 5.3 says Tier 2 now owns the update commitment above, because Tier 2 owns customer updates and existing commitments from escalation.
- No fix date, credit, refund or compensation was promised. Hannah wrote "I'm not able to offer compensation myself". The customer's request for the milk cost is open. Per policy 6.3 only Joel Brandt or the Head of Customer Support may offer it, in writing on the ticket or account record. None is recorded, and Tier 2 should not offer or imply it.
- "No rush before Monday; the hourly checks cover you over the weekend" (20 Nov 07:20 UTC) is a judgement, not a promise, and was later contradicted by the 22 Nov loss.
- "Once that's done, could you run the alarm test": request to the customer, not a commitment.

## 5. Service level

Status: **at risk** (policy 4.4). The target is not yet breached, and the deadline is Wed 25 Nov 2026 11:20 AWST (03:20 UTC).

Terms (sources):
- Plan: Business (account record). Priority: P2 (recorded on ticket 23 Nov 02:15 UTC; policy 2.5).
- Target: Business P2 resolution "27 business hours" (policy 3.1). Business hours "08:30 to 17:30 AWST ... 00:30 to 09:30 UTC" (1.1, 1.2), a 9 h day.
- Clock: "starts when the ticket is created" (4.1). Created Thu 19 Nov 07:50 UTC (15:50 AWST), inside business hours.
- Pause: "paused only while the ticket status is 'Pending customer'" (4.2). Pending customer ran 20 Nov 01:10 to 05:40 UTC, 4 h 30 min, all inside business hours. The "Escalated" status does not pause.
- Priority change: "target becomes the target for the new priority, counted from ticket creation and excluding paused time" (4.3). The clock is not restarted at 23 Nov 02:15 UTC.

Arithmetic (business time only, UTC):
- Thu 19 Nov 07:50 to 09:30 = 1 h 40.
- Fri 20 Nov 00:30 to 09:30 = 9 h, minus 4 h 30 paused = 4 h 30. Running total 6 h 10.
- Sat 21 and Sun 22: 0.
- Mon 23 Nov: 9 h. Total 15 h 10.
- Tue 24 Nov 00:30 to 06:00 = 5 h 30. Total 20 h 40 elapsed at as-of time.
- Remaining 27 h - 20 h 40 = 6 h 20 (23.5% of 27 h). The at-risk threshold is under 25%, i.e. under 6 h 45, so at risk.
- Deadline: Tue 24 Nov rest of day 3 h 30 (06:00 to 09:30) gives 24 h 10. Still needed: 2 h 50. Wed 25 Nov 00:30 + 2 h 50 = 03:20 UTC = 11:20 AWST.

Correction to Hannah's internal note (24 Nov 01:30 UTC): she gave "Thu 26 Nov 10:15 AWST, plenty of time", counting 27 business hours from the priority change. Policy 4.3 counts from ticket creation, so the deadline is about 1 business day earlier, and it is not "plenty of time".

First response was met: created Thu 07:50 UTC, first agent contact Fri 20 Nov 01:05 UTC = 1 h 40 + 0 h 35 = 2 h 15 business time, against 4 business hours at P3 and also within P2 (policy 1.4, 3.1).

Escalation: policy 5.1 allows escalation of an at-risk P2, and 5.2 requires the Support Team Lead to be notified at escalation. The thread shows no notification (see Gaps). P2 customer update cadence (7.1, at least once per business day) is being met.

Assumption: no WA public holiday falls on 19 to 25 Nov (none is stated in the material). A holiday would move the deadline later.

## 6. Recommended next action
Treat GW-03 as a probable hardware (RTC) fault and get vat 3 alarmed again before 03:20 UTC Wed 25 Nov (11:20 AWST): arrange a replacement G4-E gateway for vat 3 (the account has 20 gateway licences and 9 at Brunswick), or another working alarm path for vat 3, and verify with the customer's alarm test on vat 3.

Reason: two HTTPS time-set attempts and a reboot all failed with the same RTC write error, while GW-01 and 02 accepted the same command. Per 1.5, the ticket is resolved only when a fix or workaround restores the function and status is set to Resolved.

Before the deadline:
1. Send the customer update by 09:30 UTC today (Tier 2 now owns it). Say what is being done on GW-03 and the next update time. Do not state a fix date.
2. Notify the Support Team Lead now (5.2), and record that on the ticket.
3. Chase Joel Brandt on the compensation request and tell the customer it is with him, without promising an outcome (6.2).
4. Ask Aroha for a fresh bundle from GW-03 (post-reboot) to confirm the RTC error and record it.
5. Plan for the NTP fault on GW-01 and 02: they are corrected for now but may drift again and lose alarms, so the root cause needs follow-up. Ask peter.dunn for a packet capture or firewall log for UDP 123 on VLAN 30 (Brunswick), as his team's "no change" statement is not a test. Also ask why GW-04 to 09 sync.

Open questions for the customer that block this: site access and approval for swapping GW-03, and whether the night roster needs interim cover on vat 3 until it is fixed.

## 7. Gaps
- No post-reboot diagnostic bundle for GW-03. The RTC fault is Hannah's suspicion ("may be a hardware fault"), not confirmed.
- NTP root cause unknown. The UDP 123 theory is unconfirmed and contradicted by customer IT. The thread does not show whether GW-04 to 09 are on a different VLAN.
- The link between the clock offset and the missed alarms on 17 and 22 Nov is inferred from the TS_FUTURE log on three bundles. The thread does not verify the 22 Nov event or its 50 minutes, nor the 18,000 L loss.
- The vat 1 and 2 alarm success rests on the customer's test report and the sync result OK. No later alarm test of vats 1 and 2 after the 24 Nov reboot is recorded.
- No evidence the Support Team Lead was notified of the escalation of an at-risk P2 (policy 5.2).
- No recorded reply from Joel Brandt on the compensation request, and no written offer exists.
- Holiday calendar: public holidays in the 19 to 25 Nov window are assumed none.
- Hannah's internal SLA note used the wrong clock start (see section 5).
