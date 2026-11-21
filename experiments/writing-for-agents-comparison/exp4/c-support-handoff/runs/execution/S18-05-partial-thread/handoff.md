# Handoff: QB-202861, Brackenridge Veterinary Group (BV-3307), card payments failing "PCX-402"

Case as of 2026-11-05 11:00 UTC. Priority P2. Escalated to Tier 2 at 11:00 UTC. Only messages 7 to 12 were exported; messages 1 to 6 (2026-11-03 14:20 to 2026-11-04 15:00 UTC) were not seen.

## 1. Problem as currently understood
Saved cards created before 1 November 2026 are declined with "PCX-402 token not found" on the Quillbill/PayCollect integration, while newer saved cards work. A link to the v8.2.3 card vault migration is suspected but not confirmed.

Reported by customer
- Every card payment has failed since Monday 2 Nov; clients' saved cards are declined at the desk (Sunil Mehta, 2026-11-04 17:10, msg 8).
- Reconnected PayCollect as instructed, so the cause is not on their side (msg 8).

Verified by support
- 38 attempts since 2 Nov 14:00 UTC: 31 failed with "PCX-402 token not found", 7 succeeded. All failures used cards saved before 1 Nov; all successes used cards saved on or after 1 Nov (James Whitfield, payment logs, msg 9, 2026-11-05 09:40).
- Retry of INV-BV-20931 at 10:12 failed with the same error; token created 14 Oct 2026; API says "token not found in vault" (James, msg 11, 2026-11-05 10:20).
- Customer's PayCollect re-authorisation happened 4 Nov 14:41 UTC; 14 of the 31 failures are after it (James, integration log, msg 11).

Unverified hypotheses
- v8.2.3 (deployed 1 Nov, "Card vault migrated to PayCollect v3") broke older tokens (James, msg 11, "not confirmed").
- "A problem on our side" (James, msg 12) is his inference from the pattern, not a confirmed cause.

## 2. Tried and result
- Before 2026-11-04 15:00: customer reconnected PayCollect on Priya Nair's advice (the steps are not visible; msgs 1 to 6 not seen). Re-authorised 4 Nov 14:41 UTC. Failed (failures continued).
- 2026-11-05 09:40: James Whitfield checked payment logs. Worked as diagnosis (the pattern above).
- 2026-11-05 10:12: James retried INV-BV-20931 with customer consent (msg 10). Failed, no charge made.
- Anything done in messages 1 to 6: unknown.

## 3. Commitments to the customer
- James, msg 12 (2026-11-05 10:40): "I'll update you by 16:00 UTC today." Open, due 16:00 UTC 2026-11-05. Tier 2 now owns it (policy 5.2).
- James, msg 9 (09:40): he has passed the credit request to Callum Reid (CSM). Action done by James; no reply from Callum is on the ticket. The customer asked (msg 10) for written confirmation. Open.
- Priya, msg 7 (2026-11-04 15:40): will look at payment logs and "come back tomorrow morning". Met by James's logs and message at 09:40 on 5 Nov.
- Credit: the customer says Priya said the October fee would be credited (msg 8). No such statement appears in messages 7 to 12, and msgs 1 to 6 were not seen. Not counted as a commitment. Per policy 6.2 and 6.3 only the CSM or Head of Support can offer a credit, in writing on the ticket or account record. Account record shows "Open credits: None recorded". Status: no valid credit offer exists.

## 4. Service-level status and deadline
Not determinable. The account record's "Support level" field is blank, and policy 1.3 and 3.1 set targets by that level (Standard, Business or Enterprise). Do not assume a tier.

Known inputs
- Priority P2 (event log; policy 2.2). Clock start 2026-11-03 14:20 UTC, ticket creation (policy 4.1). Business hours are 08:00 to 18:00 London time, Mon to Fri; London is GMT=UTC on these dates (policy 1.1).
- Pause: "Pending customer" 2026-11-04 09:30 to 15:00 UTC, 5h30 excluded (policy 4.2, 4.3).
- Business hours elapsed by 11:00 on 5 Nov: 3h40 (3 Nov) + 1h30 (4 Nov before pause) + 3h00 (4 Nov after pause) + 3h00 (5 Nov) = 11h10. Calendar time elapsed excluding pause: 44h40 minus 5h30 = 39h10.
- First response was 15:02 on 3 Nov, 42 minutes after creation; whether that met target also depends on tier.

What each tier would mean (policy 3.1, for reference only, not a finding)
- Enterprise P2: resolution 24h calendar. Would be breached (39h10 elapsed).
- Business P2: 20 business hours. 8h50 left; "at risk" threshold (under 25%, 5h) not reached.
- Standard P2: 40 business hours. 28h50 left; within target.
Note: if the tier is not Enterprise, the 5.1 trigger for escalating an at-risk P2 does not apply on these numbers. If breached, policy 5.3 requires the Support Duty Manager to be told.

## 5. Recommended next action (support's judgement, not a commitment)
Primary: Tier 2 (Product Engineering) checks whether the v8.2.3 vault migration to PayCollect v3 left pre-1 Nov tokens missing, starting with INV-BV-20931's token created 14 Oct, and decides on a fix or workaround. Reason: failures split cleanly on 1 Nov save date and the API says "not found in vault". Owner: Tier 2 engineer. Customer touchpoint due: update by 16:00 UTC 2026-11-05 (James's promise), even if the update is "still investigating". Do not promise a fix date (policy 6.2).
Alternatives
- Confirm the support level with Callum Reid or the account owner today, then apply the section 4 table and notify the Duty Manager if breached. Reason: the deadline cannot be computed without it.
- Ask Callum Reid to give the customer a written reply on the October credit, or to say it is being considered. Reason: the customer asked for it in writing and only he or the Head of Support can offer it. Support should not discuss credit terms.
- Possible workaround to look into: customers re-saving cards (successes use cards saved on or after 1 Nov). Untested; not offered to the customer.

## 6. Open questions
- What is the customer's support level? The account field is blank.
- What did messages 1 to 6 say, in particular the reconnect steps and whether any credit was mentioned?
- Has Callum Reid responded on the credit? Nothing is recorded on the ticket or account.
- Conflict: customer says a credit was promised; nothing visible supports it.
- Is v8.2.3 the cause? How many accounts are affected beyond this one?
- Why do failures continue after the 4 Nov 14:41 re-authorisation (14 of 31)?
- Is there customer-facing impact still ongoing at the desk practices (4 practices on the front-desk add-on)? Should priority be reviewed? P2 stands per the event log.
