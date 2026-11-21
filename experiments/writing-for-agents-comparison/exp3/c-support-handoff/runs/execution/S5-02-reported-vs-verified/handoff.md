## Escalation handoff: TRN-77102 14 cellular gateways (Darwin, Katherine) offline since firmware 4.7.2 rollout
As of: Saturday 21 November 2026, 15:28 UTC (23:28 AWST), from the environment clock
Customer: Coldwater Freight Pty Ltd (CWF-2210), Business support plan, TernCloud Fleet subscription; 61 G4 gateways: 47 G4-E Ethernet (Kewdale/Perth 30, Wingfield/Adelaide 17), 14 G4-C cellular (Darwin 11, Katherine 3); customer-scheduled firmware, window Saturdays 18:00 UTC. Contacts: Grant Tobias (Operations Manager, primary), Lina Petrakis (IT Manager, technical). Account Manager: Rhys Kaplan.

### Problem as currently understood
All 14 G4-C cellular gateways stopped reporting at 18:20 to 18:24 UTC on Sat 14 Nov, during the 4.7.2 rollout; all 47 G4-E Ethernet gateways on the same firmware are fine. The SIMs are active but the units have made no data session attempts since, which points to the gateway side. Leading explanation, unconfirmed and of moderate confidence: the G4-C-only cellular modem firmware update to MX-31.4 in 4.7.2 left the modems unable to register on the mobile network. Whether readings are lost or buffered on the units is unknown.
Evidence:
- [Verified] Fleet of 61: 47 online, 14 offline as of 01:25 UTC 16 Nov; the 14 are Darwin (11) and Katherine (3) (Marcus Lee, Tier 1, TernCloud, 16 Nov 01:32 email)
- [Verified] The 14 last reported 18:20 to 18:24 UTC Sat 14 Nov; rollout started 18:00 UTC; all 61 updated to 4.7.2 (Marcus Lee, TernCloud, 16 Nov 01:32)
- [Verified] Online units' readings complete; offline units have no TernCloud readings after last report (Marcus Lee, TernCloud, 16 Nov 01:32)
- [Verified] All 14 SIMs "Active"; last data sessions ended 18:21 to 18:24 UTC 14 Nov; no session attempts since (Marcus Lee, Tern Connect console, 16 Nov 02:10)
- [Verified] All 14 offline units are G4-C; all 47 online units are G4-E (Marcus Lee, model check 16 Nov 02:10; account record)
- [Verified] 4.7.2 release notes say "cellular modem firmware updated to MX-31.4 (G4-C only)"; link to this fault not confirmed (Marcus Lee, 16 Nov 02:10)
- [Verified] Remote SMS wake to DRW-GW-01, DRW-GW-05, KTH-GW-02 at 02:05 UTC: no response by 02:10 (Marcus Lee, 16 Nov 02:10)
- [Reported] Darwin units show solid green power and flashing amber NET (Grant Tobias via Darwin site lead, 16 Nov 03:05); per the LED guide this means the G4-C modem is not registered on the mobile network (Marcus Lee, 16 Nov 03:40). Katherine units not checked.
- [Reported] "Every one of our gateways went dark" and "lost all our temperature data" (Grant Tobias, 16 Nov 01:12). Contradicted in part: [Verified] 47 of 61 are online with complete data (Marcus Lee, TernCloud).
- [Reported] Perth cannot dispatch Darwin loads without the certificates; about $40,000 a day in stock that cannot be certified (Grant Tobias, 16 Nov 01:12 and 03:05)
- [Reported] A Tern engineer said on a call "last week" that 4.7.2 was "fixed and safe to roll out" (Grant Tobias, 16 Nov 01:12, 03:05). [Verified] No record of a call or ticket with Coldwater last week; last ticket TRN-75530 closed 2 Oct (Marcus Lee, 16 Nov 01:32; account record).

### Tried so far
- Before 16 Nov 01:05 Coldwater staff: rebooted all Darwin gateways → no change [Reported]
- 16 Nov 01:25 UTC Marcus Lee: checked fleet status in TernCloud → 14 of 61 offline, all Darwin/Katherine [Verified]
- 16 Nov ~02:10 UTC Marcus Lee: checked SIMs in Tern Connect → all Active, no session attempts since 14 Nov [Verified]
- 16 Nov 02:05 UTC Marcus Lee: remote SMS wake to 3 units → no response [Verified]
- 16 Nov morning Darwin site staff: power-cycled all 11 Darwin units again → LEDs unchanged [Reported]
- Not tried: anything on the Katherine units (untouched per Grant Tobias, 03:05); any on-unit modem diagnostics; any rollback of 4.7.2 or MX-31.4

### Commitments to the customer
- Call back within the hour after checking the fleet | made by Marcus Lee, Tier 1, on 16 Nov 01:05 UTC (call note) | due ~02:05 UTC 16 Nov | met (call-back before 01:32 UTC email)
- Escalate to Field Systems Engineering "now" | made by Marcus Lee, Tier 1, on 16 Nov 03:40 UTC | no time given | met (escalated 03:50 UTC)
- "I'll send you an update by 12:00 AWST tomorrow, Tuesday 17 November (04:00 UTC), or sooner if engineering has news" | made by Marcus Lee, Tier 1, on 16 Nov 03:40 UTC | due 17 Nov 04:00 UTC | missed (no update in the thread); Tier 2 owns it from escalation (policy 5.3)
- Follow up the claimed call last week "if you can tell me who you spoke to" | made by Marcus Lee, Tier 1, on 16 Nov 01:32 UTC | no time given | open, condition not met (customer could not name the engineer, 03:05)

### Service level
- Priority P2 under 2.2 ("some of the customer's gateways are offline ... and there is no practical workaround"); plan Business. Customer's P1 request not supported: 2.1 needs "more than half of the customer's gateways are offline"; [Verified] 14 of 61 (23%).
- First response (4 business hours, 3.1): met at 16 Nov 01:05 UTC (ticket logged by agent during the customer's call; 1.4 "counts as a first response when logged")
- Resolution (27 business hours, 3.1; clock starts at creation, 4.1; business hours 08:30 to 17:30 AWST Mon to Fri, 1.1): deadline Thu 19 Nov 01:05 UTC / 09:05 AWST (Mon 09:05 to 17:30 = 8h25m, Tue 9h, Wed 9h, Thu 08:30 + 35m = 27h; no "Pending customer" pause, 4.2) | breached by 17h25m business hours (Thu 8h25m + Fri 9h)
- Customer updates ("P2: at least once each business day", 7.1): last update 16 Nov 03:40 UTC; none recorded on Tue 17, Wed 18, Thu 19 or Fri 20 Nov | breached (first missed by Tue 17 Nov 17:30 AWST / 09:30 UTC); next due by Mon 23 Nov 17:30 AWST (09:30 UTC)

### Recommended next action
The Tier 2 (Field Systems Engineering) owner should email Grant Tobias now, copying Lina Petrakis, acknowledging the missed 17 Nov update and giving current status, and in any case before Mon 23 Nov 08:30 AWST (00:30 UTC), because the promised update, the daily-update obligation and the resolution target have all lapsed with no recorded contact since 16 Nov 03:40 UTC.
Then: verify the MX-31.4 hypothesis, which rests only on the model split, SIM data and customer-reported LEDs: get modem registration diagnostics from a G4-C unit (Katherine units are untouched; Lina Petrakis is the technical contact) and check whether other G4-C units on 4.7.2 show the same failure.
Then: confirm whether the offline units are buffering readings, and keep the "do not factory-reset" instruction in place until that is known.

### Gaps
- The thread export ends 16 Nov 03:50 UTC, five days before the as-of time. The service-level and commitment statuses assume, as the export states, that it is the full history; if there was later activity, recompute.
- [Reported] commitment, not found in thread: a Tern engineer said last week that 4.7.2 was fixed and safe to roll out (Grant Tobias). Support found no record of the call.
- Customer request, not agreed: P1 priority (requested 16 Nov 01:05; recorded and not applied at escalation).
- Customer's "$40,000 a day" and "this one is on Tern" imply a compensation expectation. No credit or compensation has been offered; only the Account Manager (Rhys Kaplan) or the Head of Customer Support may offer one (6.3).
- Unverified and needed next: root cause (MX-31.4 link is a hypothesis); LED state seen only by customer staff, and not at Katherine; whether readings are stored on the offline units.
- Policy silences: 1.1 excludes WA public holidays but lists none; I assumed none fell on 16 to 20 Nov 2026. 7.1 does not say by what time in the business day the update is due; I used the end of business hours (17:30 AWST).
- Policy 5.2 (Team Lead notification) did not apply at escalation: 2h45m of 27 business hours had elapsed, so the ticket was not at risk. The policy does not say whether the Team Lead must be told of a later breach.
