Clarifying question: The account record's "Support level" field is blank. Which support level (Standard, Business or Enterprise) is Brackenridge Veterinary Group on? The resolution deadline cannot be computed without it.

## Escalation handoff: QB-202861 Saved-card payments failing with "PCX-402 token not found"
As of: 2026-11-05, 11:00 UTC (11:00 GMT, Europe/London)
Customer: Brackenridge Veterinary Group Ltd (BV-3307); plan Quillbill Clinic, support level not recorded; UK data region; Quillbill Invoicing (cloud), PayCollect card payments integration, Clinic front-desk add-on (4 practices) (account record). Primary contact Sunil Mehta; Customer Success Manager Callum Reid.

### Problem as currently understood
Card payments on saved cards are failing with "PCX-402 token not found". Every failure involves a card saved before 1 November, and every success involves a card saved on or after 1 November. The leading explanation is that the v8.2.3 card vault migration (deployed 1 Nov) left older tokens missing from the vault. This is a hypothesis and has not been confirmed. Support has not looked at any vault records.
Evidence:
- [Verified] 38 card payment attempts since 2 Nov 14:00 UTC: 31 failed with PCX-402, 7 succeeded (James Whitfield, payment logs, msg 9, 5 Nov 09:40)
- [Verified] All 31 failures used cards saved before 1 Nov; all 7 successes used cards saved on or after 1 Nov (James Whitfield, payment logs, msg 9)
- [Verified] Retry of INV-BV-20931 at 10:12 on 5 Nov failed with PCX-402. The PayCollect API response says "token not found in vault". The token was created 14 Oct 2026 (James Whitfield, internal note, msg 11)
- [Verified] PayCollect was re-authorised on 4 Nov at 14:41 UTC, and 14 of the 31 failures happened after that (James Whitfield, integration log, msg 11)
- [Verified] The release notes for v8.2.3 (deployed 1 Nov) say "Card vault migrated to PayCollect v3" (James Whitfield, msg 11)
- [Reported] Every card payment has failed since Monday, and clients' saved cards are declined at the desk (Sunil Mehta, msg 8). The logs partly contradict this: 7 attempts succeeded, all on newly saved cards.
- [Reported] The customer followed Priya's reconnect instructions, so the fault is not on their side (Sunil Mehta, msg 8). The re-authorisation itself is verified by the integration log.

### Tried so far
- 3 Nov to 4 Nov, Priya Nair: reconnect PayCollect, and other steps from messages 1 to 6 → did not help (customer says the reconnect did not help, msg 7; the other steps are not in the export) [Reported]
- 4 Nov 14:41 UTC, customer: PayCollect re-authorised → failures continued [Verified: integration log, James Whitfield, 5 Nov]
- 5 Nov 09:40, James Whitfield: checked payment logs → pattern above [Verified: James Whitfield]
- 5 Nov 10:12, James Whitfield: retried collection on INV-BV-20931 with customer consent (msg 10) → failed with PCX-402, no charge made [Verified: James Whitfield]

### Commitments to the customer
- Come back to the customer "tomorrow morning" (5 Nov) | made by Priya Nair, Support Agent Tier 1, on 4 Nov 15:40 UTC | due morning of 5 Nov, no exact time | met: James Whitfield replied at 09:40 UTC on 5 Nov with the log findings
- "I'll update you by 16:00 UTC today" | made by James Whitfield, Support Agent Tier 1, on 5 Nov 10:40 UTC | due 5 Nov 16:00 UTC | open, 5 hours remaining. Tier 2 owns this from escalation (policy 5.2).
- Credit: none. James said he cannot agree credits and has "passed your request to Callum Reid". That is a referral, not a promise. Sunil wants any credit confirmed in writing.

### Service level
- Priority P2, set at ticket creation and recorded as P2 at escalation. The definition in policy 2.2 fits (payment collection failing for older saved cards). Whether a practical workaround exists is not verified (see Gaps). Plan Quillbill Clinic; support level not recorded (policy 1.3: the level is the one in the account record).
- First response: met. Ticket created 3 Nov 14:20, first agent reply 15:02 (42 minutes). Policy 1.4 counts agent replies, and 42 minutes is inside the P2 first-response target at every level (policy 3.1: Enterprise 2 hours 24x7, Business 4 business hours, Standard 8 business hours).
- Resolution: not computable, because the support level is blank. Elapsed time under policy 4.1 to 4.3 is the same for every level. The clock starts at creation (3 Nov 14:20) and pauses only in "Pending customer" (4 Nov 09:30 to 15:00, 5.5 hours). Calendar time is 44h40 minus 5h30 paused = 39h10. Business hours (08:00 to 18:00 GMT, Mon to Fri) are 3h40 on 3 Nov, 1h30 and 3h00 on 4 Nov, and 3h00 on 5 Nov, which is 11h10 in total. If the level turns out to be one of these, the status is:
  - Enterprise (24 hours, 24x7): breached by 15h10. Policy 5.3 then requires telling the Support Duty Manager.
  - Business (20 business hours): open, 8h50 remaining, about 44%, within target.
  - Standard (40 business hours): open, 28h50 remaining, within target.
- Customer updates (policy 7.1, P2, once each business day): today's update was sent at 09:40.

### Recommended next action
Tier 2 (the engineer picking this up) should check whether pre-1 Nov card tokens, such as the one on INV-BV-20931 created 14 Oct, exist in the PayCollect v3 vault after the v8.2.3 migration, and send Sunil an update before 16:00 UTC today. The update should say what is confirmed, which is that older saved cards fail and newly saved ones work. It must not promise a fix date (policy 6.2). The explanation is only a hypothesis (msg 11) and the next step depends on confirming it.
Then: Confirm the support level with the account owner or Callum Reid, and apply policy 5.3 if it is Enterprise. Ask Callum Reid to answer the credit request in writing, since only he or the Head of Support can offer a credit (policy 6.3).

### Gaps
- Support level is blank in the account record, so the resolution status is not computable and the Duty Manager duty is undetermined.
- Messages 1 to 6 are not in the export, so the first-contact details, the reconnect steps Priya sent and the other attempts cannot be verified.
- [Reported] commitment, not found in thread: Sunil says "as you said in your message yesterday" October's subscription fee would be credited. Nothing in messages 7 to 12 shows a credit being promised, and Priya's message 7 contains none. Check messages 1 to 6. Policy 6.2 and 6.3 bar agents from promising credits, and the account record shows "Open credits: None recorded".
- Whether a practical workaround exists (for example re-saving the card on file, which fits the pattern that newly saved cards work) has not been tested, so the P2 versus P3 distinction is unconfirmed.
- Policy 4.2 pauses the clock only in "Pending customer", and the ticket is now "Escalated". Policy 1.1 excludes English bank holidays and none fall in the window, so none were applied.
