Clarifying question: The account record's "Support level" field is blank. Which support level (Standard, Business or Enterprise) does Brackenridge Veterinary Group (BV-3307) have? Can you also supply thread messages 1 to 6, which this export leaves out? Without an answer, this handoff gives the service-level deadline under each support level, and lists what those messages would settle.

# Escalation handoff: QB-202861, Brackenridge Veterinary Group Ltd (BV-3307)

**Summary:** PayCollect card payments fail with "PCX-402 token not found" for every saved card created before 1 Nov 2026. Cards saved on or after 1 Nov still work, and v8.2.3 (deployed 1 Nov) migrated the card vault to PayCollect v3. The most urgent deadline is the customer update promised by 16:00 UTC on 5 Nov. The P2 resolution target is already breached if the account is Enterprise, but the support level is not recorded.
**Reference time:** 2026-11-05 11:00 UTC (latest thread entry; no current time was supplied)

## Problem as currently understood
Saved-card payments fail with "PCX-402 token not found" when the card token was created before 1 Nov 2026. PayCollect reports these tokens as "not found in vault", and the failures continued after the customer reconnected PayCollect. A possible cause is the 1 Nov card vault migration to PayCollect v3, but nobody has confirmed it.
- [Verified] Since 2 Nov 14:00 UTC there were 38 card payment attempts: 31 failed with "PCX-402 token not found" and 7 succeeded (James Whitfield, msg 9, 2026-11-05 09:40, from the payment logs)
- [Verified] All 31 failures used cards saved before 1 Nov, and all 7 successes used cards saved on or after 1 Nov (James Whitfield, msg 9, 2026-11-05 09:40)
- [Verified] A retry on INV-BV-20931 at 10:12 failed with the same error. Its card token was created 14 Oct 2026, and the PayCollect API response was "token not found in vault" (James Whitfield, internal note msg 11, 2026-11-05 10:20)
- [Verified] PayCollect was re-authorised on 4 Nov at 14:41 UTC, and 14 of the 31 failures came after that (James Whitfield, msg 11, 2026-11-05 10:20, from the integration log)
- [Verified] The v8.2.3 release notes (deployed 1 Nov) say "Card vault migrated to PayCollect v3". That this caused the failures is not confirmed (James Whitfield, msg 11, 2026-11-05 10:20)
- [Reported] "Every single card payment has failed since Monday" (Sunil Mehta, msg 8, 2026-11-04 17:10). The log check governs here: 7 payments succeeded.
- [Reported] Clients' saved cards are declined at the front desk when they collect their pets (Sunil Mehta, msg 8, 2026-11-04 17:10)

Open questions:
- Were tokens created before 1 Nov left out of the PayCollect v3 vault migration, or failing to map to it? Does this affect other customers?
- Why does the log window start at 2 Nov 14:00 when the deployment was on 1 Nov? Were there any failures before then?
- Is re-saving an affected card a working workaround? (Cards saved on or after 1 Nov succeed, but no re-save test is recorded.)
- What did messages 1 to 6 contain, including the reconnect steps Priya sent and the credit the customer says was promised? (These messages are not in the export.)

## Tried so far
- Reconnect steps sent to the customer, by Priya Nair, in messages 2 to 6 (2026-11-03 to 2026-11-04): result not recorded (the messages are not in the export)
- Reconnecting PayCollect, by the customer, on 4 Nov: [Reported] "the reconnect didn't help" (msg 7/msg 8). [Verified] The re-authorisation happened at 14:41 UTC and failures continued after it (msg 11).
- Payment log review, by James Whitfield, 2026-11-05 09:40: found the before/after 1 Nov pattern described above (msg 9)
- Retry of INV-BV-20931 (with customer approval, msg 10), by James Whitfield, 2026-11-05 10:12: failed with PCX-402 "token not found in vault"; no charge was made (msgs 11, 12)
- Release notes review, by James Whitfield, 2026-11-05 10:20: found the v8.2.3 vault migration as a possible link, not confirmed (msg 11)
- Escalated to Tier 2, by James Whitfield, 2026-11-05 11:00 (ticket event)

## Commitments to the customer
Under policy section 5.2, Tier 2 now owns these commitments.
- "the next step is for me to look at the payment logs on our side. I'll come back to you tomorrow morning.", Priya Nair, 2026-11-04 15:40: met. James did the log review and replied on 2026-11-05 at 09:40 (msg 9).
- "I'm escalating this to our Product Engineering Support team now.", James Whitfield, 2026-11-05 10:40: met. The ticket was escalated at 11:00 (ticket event).
- "I'll update you by 16:00 UTC today.", James Whitfield, 2026-11-05 10:40: outstanding, due 2026-11-05 16:00 UTC, with 5 h remaining.
- Claimed by customer, not found in thread: that a support agent said in a message on 3 Nov that October's subscription fee would be credited (Sunil Mehta, msg 8, 2026-11-04 17:10). Messages 1 to 6 are missing from the export, so the claim cannot be checked against them. Under policy 6.2 and 6.3, agents may not promise credits, and only the Customer Success Manager (Callum Reid, per the account record) or the Head of Support may offer one in writing. The account record shows "Open credits: None recorded". James passed the request to Callum Reid (msg 9), and the customer has asked for written confirmation, not to be passed around (msg 10, 2026-11-05 09:55).

## Service level
- Tier: **Not determinable**. The account record's "Support level" field is blank, and the policy has no single target for P2 across support levels (policy 1.3, 3.1). | Priority: P2 (ticket, set at creation and again at escalation)
- Clock: starts at creation, 2026-11-03 14:20 UTC (policy 4.1). It was paused while the ticket was Pending customer, from 2026-11-04 09:30 to 15:00, which is 5 h 30 min (policy 4.2, 4.3). Business hours are 08:00 to 18:00 UTC, Monday to Friday (policy 1.1), and there are no English bank holidays in this period.
- First response: 15:02 on 2026-11-03, 42 min after creation, met under every level (policy 1.4, 3.1).
- Resolution target and deadline under each level (policy 3.1, 3.3):
  - Enterprise, 24 h calendar time: 14:20 on 2026-11-04 plus the 5 h 30 min pause gives **2026-11-04 19:50 UTC**. Status: **breached** (15 h 10 min overdue at the reference time). The Support Duty Manager must be told (policy 5.3).
  - Business, 20 business hours: 3 h 40 min on 3 Nov (14:20 to 18:00) plus 4 h 30 min on 4 Nov (08:00 to 09:30 and 15:00 to 18:00) plus 10 h on 5 Nov makes 18 h 10 min, so 1 h 50 min falls on 6 Nov: **2026-11-06 09:50 UTC**. Status: open, 8 h 50 min of business time remaining. This is not yet at risk: under policy 4.5, "at risk" begins below 5 h.
  - Standard, 40 business hours: 18 h 10 min by the end of 5 Nov, 28 h 10 min by the end of 6 Nov and 38 h 10 min by the end of 9 Nov, so 1 h 50 min falls on 10 Nov: **2026-11-10 09:50 UTC**. Status: open, 28 h 50 min of business time remaining. This is not at risk (the threshold is 10 h).
- Update cadence: P2 tickets need an update at least once each business day (policy 7.1).

## Recommended next action
Check in the PayCollect v3 vault whether the INV-BV-20931 token (created 14 Oct) and BV-3307's other tokens saved before 1 Nov were migrated by v8.2.3. The evidence for this is that every failure involves a pre-1 Nov token, PayCollect returns "token not found in vault", and failures continued after the reconnect. In the same step, test whether re-saving one affected card restores payment, as a possible workaround. Serves: the 16:00 UTC update commitment, and the P2 resolution deadline (already breached if Enterprise, 2026-11-06 09:50 if Business).
Tell the customer: by **2026-11-05 16:00 UTC**, say that the failures are traced to saved cards stored before 1 Nov and are on Quillbill's side, not in their settings. Say that engineering is investigating, and give the workaround if the re-save test works. Do not give a fix date (policy 6.2). Say that the October credit request is with Callum Reid, who is the only person able to confirm credits in writing (policy 6.3). Separately, confirm the account's support level now. If it is Enterprise, the ticket has breached its target and the Support Duty Manager must be told.

## Blocked
- Account record support level (blank): blocks the service-level tier, target, deadline and status. Each reading is given above.
- Thread messages 1 to 6 (not in export): block checking the customer's claim about the October credit, and the details and results of Priya's earlier troubleshooting steps.
