# Handoff: TRN-77102, Coldwater Freight (CWF-2210), as of 2026-11-16 03:50 UTC

## 1. Problem as currently understood
After the 4.7.2 firmware rollout (started Sat 14 Nov 18:00 UTC), 14 of 61 gateways (all G4-C cellular, Darwin 11 and Katherine 3) stopped reporting at 18:21-18:24 UTC and show a flashing amber NET light. The 47 G4-E Ethernet units are healthy. The cause is unconfirmed. Possible link is the cellular modem firmware update (MX-31.4) in 4.7.2.

**Reported by customer**
- All gateways are offline and all sites are affected (Tobias, 16 Nov 01:05 call, 01:12 and 03:05 emails).
- Temperature data is lost for three days; cost about $40,000 a day (16 Nov 01:12).
- Darwin units were rebooted twice with no change (16 Nov 01:05, 03:05). Darwin units show solid green power and flashing amber NET (16 Nov 03:05, per Darwin site lead). Katherine units untouched.
- An unnamed Tern engineer "last week" said 4.7.2 was fixed and safe (16 Nov 01:12, 03:05). Customer says it is therefore Tern's fault.
- Perth cannot dispatch Darwin loads without certificates (16 Nov 03:05).

**Verified by support**
- 61 gateways, all updated to 4.7.2; 47 online with complete readings; 14 offline (Lee, TernCloud, 16 Nov 01:32). The account record (Fleet table) matches the 11+3 G4-C units.
- All 14 offline units are G4-C; all 47 online are G4-E (Lee, 16 Nov 02:10, console check).
- All 14 SIMs Active; last sessions ended 18:21-18:24 UTC 14 Nov; no attempts since (Lee, Tern Connect console, 16 Nov 02:10).
- No record of a call or ticket last week; last ticket was TRN-75530, closed 2 Oct (Lee, 16 Nov 01:32; matches account record).

**Unverified hypotheses**
- MX-31.4 modem firmware change causes failure to register on the network (Lee, 02:10, "not confirmed").
- Gateway-side fault rather than SIM accounts (Lee, 03:40, from LED guide).
- Readings may be stored locally on the 14 units; data loss not yet determined.

## 2. Tried and result
- Customer rebooted all Darwin units, 16 Nov before 01:05: no change.
- Marcus Lee checked fleet status in TernCloud, 01:25: confirmed 14 offline (see above).
- Lee checked Tern Connect console, about 02:10: SIMs Active, no sessions since 18:24 UTC 14 Nov.
- Lee sent SMS wake to DRW-GW-01, DRW-GW-05, KTH-GW-02 at 02:05: no response by 02:10. No later check recorded.
- Customer power-cycled all 11 Darwin units again, morning of 16 Nov (before 03:05): lights unchanged.
- Lee asked customer not to factory-reset (03:40). Katherine units not yet touched.

## 3. Commitments to the customer
- Call back within the hour (Lee, 01:05 call): met, call-back and email at 01:32.
- Update by 12:00 AWST Tue 17 Nov (04:00 UTC) or sooner if engineering has news (Lee, 03:40): open. Tier 2 owns this under policy 5.3.
- "If you can tell me who you spoke to, I'll follow it up" (Lee, 01:32): conditional; customer has not named anyone (03:05). Open.
- No fix date, credit, refund or compensation promised. Lee stated no fix date can be given (03:40).

## 4. Service-level status and deadline
- Tier: Business (account record). Priority: P2, recorded on ticket at 01:05; customer's P1 request recorded but not applied (03:50). Under policy 2.1, P1 needs more than half of gateways offline; 14 of 61 is 23%. Policy 2.5: a priority applies only once recorded.
- Row used: Business, P2: first response 4 business hours; resolution 27 business hours (policy 3.1). Business hours are 08:30-17:30 AWST Mon-Fri, i.e. 00:30-09:30 UTC, 9 hours a day (1.1, 1.2).
- Clock start: ticket created 16 Nov 01:05 UTC (09:05 AWST), inside business hours (4.1). No "Pending customer" status in the thread, so no pause (4.2).
- First response: 01:05 UTC, ticket logged during the call counts (1.4). Met.
- Calculation: Mon 16 Nov 01:05-09:30 UTC = 8h25m, leaving 18h35m. Tue 17 = 9h, leaving 9h35m. Wed 18 = 9h, leaving 0h35m. Thu 19 from 00:30 UTC + 35m = **Thu 19 Nov 2026 01:05 UTC (09:05 AWST)**. Assumes no WA public holiday 17-19 Nov (none known to me).
- At 03:50 UTC on 16 Nov: elapsed 2h45m, remaining 24h15m. Status: within target (at risk only below 6.75 business hours, policy 4.4). The ticket becomes at risk on Wed 18 Nov at about 06:20 UTC (14:20 AWST). Re-measure if priority changes (4.3).

## 5. Recommended next action (support's judgement, not a commitment)
1. **Tier 2 (Field Systems Engineering) to test the MX-31.4 modem hypothesis** and confirm whether the cause is the modem firmware. First check whether the console or modem logs for one G4-C unit show failure to register, and compare with the 4.7.2 release notes. Reason: the hardware model is the only verified separator of the two groups. Next customer touchpoint: update to Tobias by 04:00 UTC 17 Nov, even if only a status.
2. Alternative: have Katherine staff report LEDs and hold off any reset; this tests whether the failure matches Darwin on a second site. Reason: Katherine is untouched.
3. Alternative: ask the customer to confirm which sites cannot dispatch and what data they need; the claim "every site affected" conflicts with verified status, and may point to a P1 or severity change if wrong. Reason: severity and data-loss impact are unquantified.
Owner: Tier 2 engineer. Keep customer updates at least once each business day for P2 (policy 7.1). Do not promise a fix date, credit or compensation (6.2); only the Account Manager (Rhys Kaplan) or Head of Customer Support may offer a credit (6.3).

## 6. Open questions
- Is the cause the MX-31.4 modem firmware? Is there a remote recovery path, or a site visit or SIM-level action needed?
- Are readings stored locally on the 14 units, and for how long? Do not factory reset.
- Conflicts: the customer says all gateways are offline, but support verified 47 of 61 online. The customer says three days of data are lost, but the outage began 14 Nov 18:21 UTC (about 2 days). The customer says an engineer last week called 4.7.2 safe, but support found no record. Name and date still unknown; the customer's liability claim is unverified.
- Is Perth's certificate and dispatch problem due to Darwin data only? The $40,000 a day figure is unverified.
- Was any further SMS wake attempted after 02:10?
- Support Team Lead notification (policy 5.2) applies only to P1 or at-risk P2; neither applies now.
