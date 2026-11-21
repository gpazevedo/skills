# Handoff: TRN-77102, Coldwater Freight (CWF-2210)

As-of 2026-11-16 03:50 UTC (11:50 AWST, Monday). Escalated to Tier 2 (Field Systems Engineering) at 03:50 UTC. Priority P2, Business plan.

## 1. Problem and evidence

**Problem:** 14 of 61 gateways (all G4-C cellular units at Darwin, 11, and Katherine, 3) stopped reporting at 18:20-18:24 UTC on Sat 14 Nov, during the 4.7.2 firmware rollout. They show a flashing amber NET light and do not respond to power cycles or an SMS wake. The 47 G4-E Ethernet units (Perth, Adelaide) are online. Suspected link, not confirmed: the 4.7.2 cellular modem firmware change (MX-31.4, G4-C only).

Evidence (grade, source):

- Fleet is 61 gateways: Perth 30 G4-E, Adelaide 17 G4-E, Darwin 11 G4-C, Katherine 3 G4-C. **Verified**, account record (fleet table).
- 47 online and reporting normally, 14 offline, as of 01:25 UTC. **Verified**, TernCloud view quoted by Marcus Lee, 01:32 message.
- The 14 offline units last reported 18:20-18:24 UTC on 14 Nov, rollout started 18:00 UTC. **Verified**, TernCloud (01:32 message).
- All 61 units updated to 4.7.2; the 47 online units run 4.7.2. **Verified**, TernCloud (01:32 message).
- Online units' readings are complete, with no gaps. **Verified**, TernCloud (01:32 message).
- All 14 SIMs are Active, with last data sessions ending 18:21-18:24 UTC and no attempts since. **Verified**, Tern Connect console (internal note, 02:10).
- All 14 offline units are G4-C and all 47 online are G4-E. **Verified**, Tern Connect console and account record (02:10 note).
- The 4.7.2 release notes say "cellular modem firmware updated to MX-31.4 (G4-C only)". **Verified** as release-note text (02:10 note). That it is the cause is a hypothesis, not confirmed.
- SMS wake sent at 02:05 UTC to DRW-GW-01, DRW-GW-05 and KTH-GW-02. No response by 02:10. **Verified**, internal note 02:10. Only five minutes had elapsed.
- Darwin units show solid green POWER and flashing amber NET. **Reported**, Grant Tobias 03:05, relaying the site lead. Not observed by Tern.
- Darwin units were power-cycled, first before 01:05 and again on the morning of 16 Nov, with no change. **Reported**, call note 01:05 and 03:05 email.
- Katherine units are untouched and their lights are unknown. **Reported**, 03:05.
- Meaning of a flashing amber NET light on a G4-C is "modem not registered on the mobile network". **Verified** as LED-guide content (cited by Marcus, 03:40). It is not an observation of these units.
- Temperature data lost "for the last three days". **Reported**, 01:12. Conflict: the units went offline at about 18:24 UTC on 14 Nov, roughly 33 hours before the as-of time, not three days. G4 units buffer readings locally, so loss is unconfirmed (01:32).
- "Every gateway" / "every site is affected" and "Perth can't dispatch the Darwin loads without the certificates". **Reported**, 01:12 and 03:05. Conflict with TernCloud: Perth and Adelaide are online and complete. Marcus did not challenge the "every site" claim in his 03:40 reply. The Perth dispatch dependency on Darwin data is unexplained.
- Cost of about $40,000 per day in uncertifiable stock. **Reported**, 01:12.
- An engineer told Grant "last week" that 4.7.2 was fixed and safe. **Reported**. Conflict: no call or ticket found by Marcus (01:32). The engineer is unnamed (03:05). The latest ticket on the account is TRN-75530, closed 2 Oct.
- "Your firmware push": Grant describes Tern pushing the firmware. The account record says rollouts are customer-scheduled, default window Saturdays from 18:00 UTC, and Marcus calls it "your scheduled firmware window". Who triggered the 14 Nov rollout is not recorded in the thread.

## 2. Tried and results

| Who | When (UTC) | What | Result |
| --- | --- | --- | --- |
| Customer (Darwin) | before 01:05 on 16 Nov | Rebooted all Darwin gateways (reported) | No difference (reported) |
| Customer (Darwin) | morning of 16 Nov, reported 03:05 | Power-cycled all 11 Darwin units again (reported) | Lights unchanged (reported) |
| Marcus Lee | 01:05-01:25 | Checked fleet in TernCloud | Found 14 offline, all Darwin and Katherine |
| Marcus Lee | 02:05 | SMS wake to DRW-GW-01, DRW-GW-05, KTH-GW-02 | No response by 02:10. No later result recorded |
| Marcus Lee | by 02:10 | Checked SIM status and sessions in Tern Connect | SIMs Active, no sessions since 18:24 on 14 Nov |
| Marcus Lee | by 02:10 | Compared model against online status and read the release notes | G4-C vs G4-E split; MX-31.4 modem firmware noted. Cause unconfirmed |
| Marcus Lee | 01:32 | Asked Darwin for front-panel light status | Answered at 03:05 (Darwin only) |
| Marcus Lee | 03:40 | Told customer not to factory reset | Customer response not recorded |
| Marcus Lee | 03:50 | Escalated to Tier 2, left at P2 | Done |

Nothing was tried on Katherine units. No remote diagnostics, modem log pull or modem firmware check is recorded. The 01:05 call-back, 03:40 priority statement and the escalation are actions, not fixes.

## 3. Commitments to the customer

Tier 2 owns these from escalation (policy 5.3).

1. **Call-back within the hour.** Marcus Lee, 01:05 (call note): "I'd check the fleet and call him back within the hour." Kept: the call-back took place before the 01:32 email.
2. **Update by 04:00 UTC Tue 17 Nov.** Marcus Lee, 03:40: "I'll send you an update by 12:00 AWST tomorrow, Tuesday 17 November (04:00 UTC), or sooner if engineering has news." Open. Within policy 6.1 (time of next update).
3. **Follow up the "last week" engineer call.** Marcus Lee, 01:32: "If you can tell me who you spoke to, I'll follow it up." **Ambiguous**: conditional on the customer naming the engineer, who has not been named (03:05). Treat it as open.

Not promises: "I can't give you a fix date", "That doesn't change how seriously we're taking it". No fix date, credit, refund or compensation was promised (policy 6.2). Grant's "this one is on Tern" and the $40,000 per day figure are unanswered. Any credit is for Account Manager Rhys Kaplan or the Head of Customer Support only (policy 6.3).

## 4. Service level and deadline

- Plan: Business (account record). Priority recorded on ticket: P2 (01:05 event; confirmed 03:50). Policy 2.5: "A customer may request a different priority; a priority applies only once recorded on the ticket." P1 was requested and not recorded.
- Priority check: 14 of 61 offline is 23%, not "more than half" (policy 2.1). No workaround is evident, which fits P2 (2.2). P2 stands on current evidence. It would become P1 only if more than 30 of 61 are offline.
- Targets (policy 3.1, Business P2): first response "4 business hours", resolution "27 business hours". Per 3.3 these count business hours only.
- Clock start (policy 4.1): "The clock starts when the ticket is created." Created 01:05 UTC Mon 16 Nov (09:05 AWST), inside business hours (00:30-09:30 UTC, policy 1.1/1.2). No pause: the status has never been "Pending customer" (4.2).
- First response: policy 1.4 says a ticket logged during a call counts when logged. Met at 01:05 UTC, 0 hours after creation.
- Resolution deadline, with inputs: 27 business hours counted from 01:05 UTC on Mon 16.
  - Mon 16: 01:05 to 09:30 = 8h25m (cumulative 8h25m)
  - Tue 17: 00:30 to 09:30 = 9h (cumulative 17h25m)
  - Wed 18: 9h (cumulative 26h25m)
  - Thu 19: 35m needed, so 00:30 + 0:35 = **01:05 UTC Thu 19 Nov (09:05 AWST)**
- Elapsed at 03:50 UTC Mon 16: 2h45m. Remaining: 24h15m of 27h (90%).
- Status (policy 4.4): at risk when "less than 25% of its resolution target remains" (6h45m). Currently **within target**. It becomes at risk when elapsed passes 20h15m: Mon 8h25m + Tue 9h + Wed 2h50m, so at 03:20 UTC Wed 18 Nov (11:20 AWST).
- Customer updates (policy 7.1): P2 "at least once each business day". The 04:00 UTC Tue update promise satisfies Tuesday.
- Escalation (policy 5.1): met on "cannot be resolved with documented procedures". Notifying the Support Team Lead (5.2) is required only for a P1 or an at-risk P2. Neither applies now.
- Assumption: no Western Australian public holiday falls on 16-19 Nov 2026. The policy supplies no holiday list. Check this; a holiday would move the deadline later.

## 5. Recommended next action

**Tier 2 (Field Systems Engineering) should determine whether 4.7.2's cellular modem firmware update (MX-31.4) is stopping the G4-C units from registering on the mobile network.**

Reason: the only verified separator between the 47 healthy and 14 failed units is model (G4-C vs G4-E). SIMs are Active, so the carrier side looks fine. The failures began within minutes of the modem update, the release notes name a G4-C-only modem firmware change, and no remote or local recovery has worked.

First check: for the 14 units, compare the last telemetry before dropout (modem firmware version, registration or error codes, last boot or update stage) against the expected MX-31.4 state. Then check whether other 4.7.2 G4-C customers show the same pattern or a known issue.

Constraints for Tier 2:

- Do not factory reset. Local readings may be stored on the units and would be erased.
- Send the customer update by 04:00 UTC Tue 17 Nov, or sooner.
- Keep the P2 priority under review, and tell the Support Team Lead if the ticket goes at risk.
- Do not promise a fix date, credit or refund (6.2). Route the customer's liability and cost claim to Rhys Kaplan.

Open questions for the customer (via Grant Tobias, or Lina Petrakis, IT Manager, technical contact):
- What do the lights show at Katherine (3 units)?
- Who was the engineer who spoke to you last week, when, and how (phone number or email)?
- Who started the 14 Nov rollout, and was it the default Saturday 18:00 UTC window?
- Which exact gateways does the "every site is affected" statement cover? Why can Perth not dispatch Darwin loads, and what data do the certificates need?
- What data period do you consider missing, by gateway?

Open questions for engineering:
- Is the rollout still queued for any other G4-C units on this account? (14 of 14 G4-C units are affected, so check whether a rollback or hold applies elsewhere.)
- How many hours of readings can a G4-C buffer, and will it upload when it reconnects?
- Can a remote recovery of the modem work when the unit has not registered on the network?
- Is there a known issue or hotfix for MX-31.4?
- Has the SMS wake worked on any G4-C unit? Only three units were tried, and only five minutes were given.

## 6. Gaps (missing inputs, conflicts, unverified assumptions)

- Conflicts: "all gateways offline" vs 47 of 61 online (verified); "three days of data lost" vs about 33 hours offline and local buffering; "your push" vs customer-scheduled rollouts per the account record.
- Unverified: the "last week" engineer call (no record found); the Darwin LED states and reboots (customer-reported); the modem-firmware cause (hypothesis only); any data loss (unknown until units reconnect).
- Unknown: Katherine LEDs and whether any Katherine unit has been power-cycled; the buffer capacity of the G4-C; the SMS wake outcome after 02:10.
- No public holiday list supplied with the policy; the deadline assumes none on 16-19 Nov.
- The thread export does not show the call-back time, only the 01:32 email, so commitment 1 is judged kept from the email's wording.
- The ticket status "Escalated" is not "Pending customer", so no pause applies. If Tier 2 sets "Pending customer" while awaiting the customer, the clock pauses (4.2) and the deadline moves later by the paused business time.
- The customer's $40,000 per day claim and liability assertion have no recorded response and no account-manager contact on the ticket. No credits are open and the account has no flags.
