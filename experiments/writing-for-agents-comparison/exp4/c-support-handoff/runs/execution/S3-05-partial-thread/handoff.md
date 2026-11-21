# Escalation handoff: QB-202861, Brackenridge Veterinary Group Ltd (BV-3307)

**Service level:** Undetermined. The account record's "Support level:" field is blank (policy 1.3 takes the level from that field), so the target and deadline cannot be set. Priority is P2, ticket created 2026-11-03 14:20 UTC, so under policy 3.1 the resolution deadline ranges from breached (if Enterprise) to 2026-11-06 09:50 UTC (if Business); see Service level section.
**Next action:** Check whether the v8.2.3 card-vault migration to PayCollect v3 dropped tokens saved before 1 Nov, starting with the token on INV-BV-20931 (created 14 Oct 2026), and update the customer by 16:00 UTC today.

## Problem as currently understood
Saved cards created before 1 Nov 2026 are being declined with "PCX-402 token not found" (PayCollect API: "token not found in vault"), while cards saved on or after 1 Nov succeed; a link to the v8.2.3 vault migration is suspected but not confirmed. This differs from the customer's framing ("every single card payment has failed"; "not on our side"): the failures are narrower than reported, and the customer's reconnect did not fix them.

Evidence:
- [Verified] 38 card payment attempts since 2 Nov 14:00 UTC: 31 failed with "PCX-402 token not found", 7 succeeded (James Whitfield, payment logs, message 9, 2026-11-05 09:40)
- [Verified] All 31 failures used cards saved before 1 Nov; all 7 successes used cards saved on or after 1 Nov (James Whitfield, payment logs, message 9, 2026-11-05 09:40)
- [Verified] Retry of INV-BV-20931 at 10:12 failed again with "PCX-402 token not found"; PayCollect API said "token not found in vault"; the token was created 14 Oct 2026; no charge made (James Whitfield, retry and API response, message 11 at 2026-11-05 10:20 and message 12 at 10:40)
- [Verified] PayCollect connection was re-authorised on 4 Nov at 14:41 UTC, and 14 of the 31 failures are after that time (James Whitfield, integration log, message 11, 2026-11-05 10:20)
- [Verified] Release notes for v8.2.3 (deployed 1 Nov) say "Card vault migrated to PayCollect v3." (James Whitfield, release notes, message 11). A causal link to the failures is not confirmed (James's own words).
- [Reported] Every card payment has failed since Monday; clients' saved cards are declined at the desk (Sunil Mehta, message 8, 2026-11-04 17:10)
- [Reported] The customer did what the earlier message said and reconnected PayCollect, so the problem is not on their side (Sunil Mehta, message 8, 2026-11-04 17:10). The reconnect itself is verified (above); which steps were sent to the customer is not visible to Tier 1.
- Conflict: Sunil reports that "every single card payment" has failed (message 8); the logs show 7 of 38 attempts succeeded, all on cards saved on or after 1 Nov. The failures are specific to older saved cards.
- Not in this export: messages 1 to 6 (2026-11-03 14:20 to 2026-11-04 15:00 UTC), including the original report and Priya Nair's earlier reconnect instructions. The ticket event log is complete.

## Tried so far
- 2026-11-03 15:02, Priya Nair: first agent response (message 2) -> content not in export; result not recorded
- 2026-11-03 to 2026-11-04, Priya Nair: sent reconnect-PayCollect steps (as described by Priya in message 7 and Sunil in message 8; messages 1 to 6 not in export) -> reconnect done 2026-11-04 14:41 UTC (integration log); failures continued, 14 after reconnect
- 2026-11-04 15:40, Priya Nair: said she would look at the payment logs -> done by James Whitfield, below
- 2026-11-05 09:40, James Whitfield: checked payment logs -> 38 attempts, 31 failed, 7 succeeded; failures all on cards saved before 1 Nov
- 2026-11-05 09:40, James Whitfield: passed the October credit request to Callum Reid (message 9) -> result not recorded (no record Callum has acknowledged or replied)
- 2026-11-05 10:12, James Whitfield: retried collection on INV-BV-20931 with customer's consent (message 10 at 09:55) -> failed, "PCX-402 token not found"
- 2026-11-05 10:20, James Whitfield: reviewed integration log and v8.2.3 release notes -> reconnect confirmed; possible link to the 1 Nov vault migration, not confirmed
- 2026-11-05 11:00, James Whitfield: escalated to Tier 2, status Open -> Escalated, priority P2

## Commitments to the customer
- "I'll come back to you tomorrow morning." (Priya Nair, message 7, 2026-11-04 15:40), due the morning of 2026-11-05, met: James Whitfield replied at 09:40 UTC on 2026-11-05 (message 9)
- "I'll update you by 16:00 UTC today." (James Whitfield, message 12, 2026-11-05 10:40), due 2026-11-05 16:00 UTC, open (as of 11:00 UTC)
- "I've passed your request to Callum Reid." (James Whitfield, message 9, 2026-11-05 09:40), no due time given, open: no recorded response from Callum. This is an action taken, not a credit offer.
- [Reported, unconfirmed] Sunil says Priya said in a message "yesterday" (2026-11-03) that October's subscription fee would be credited: "as you said in your message yesterday, we'll be expecting October's subscription fee to be credited" (Sunil Mehta, message 8, 2026-11-04 17:10). No matching message in the available thread (messages 1 to 6 not in export). Policy 6.2 and 6.3 bar agents from promising credits; only Callum Reid (CSM named in the account record) or the Head of Support can offer one, in writing on the ticket or account record, and none is recorded (account: "Open credits: None recorded"). Check messages 1 to 6 for what Priya actually wrote.
- Sunil has asked for the credit "confirmed in writing, not passed around" (message 10, 2026-11-05 09:55); unanswered. Under policy 5.2 Tier 2 now owns commitments made to the customer, including the 16:00 update.

## Service level
- Plan: Quillbill Clinic (account record). Support level: blank in the account record ("Support level:"). Policy 1.3: "A customer's support level (Standard, Business or Enterprise) is the level recorded in the customer's account record." "Quillbill Clinic" is a plan name, not one of those levels, so it cannot be mapped. **Undetermined**: support level missing from the account record.
- Priority: P2 (ticket created as P2 by Sunil Mehta, event log 2026-11-03 14:20; still P2 at escalation, 2026-11-05 11:00; no priority change recorded). Policy 2.2: "P2 (High): a major function, such as invoice sending, payment collection or bank feeds, does not work and there is no practical workaround." Mismatch to note: payment collection is affected, but the 7 successful attempts on cards saved on or after 1 Nov suggest a partial workaround (re-saving the card) may exist; whether it is practical for desk payments is unknown. If so, P3 (policy 2.3) could apply. Under 2.5 only a support agent can change priority. P1 is not met (not all users unavailable; no data loss recorded). Recommend keeping P2 unless Tier 2 decides otherwise.
- Target: Undetermined without the support level. Policy 3.1 rows for P2: Enterprise 2 hours first response, 24 hours resolution, 24x7; Business 4 business hours first response, 20 business hours resolution; Standard 8 business hours first response, 40 business hours resolution. Policy 3.3: 24x7 targets run on calendar time, others count business hours only.
- Clock: started 2026-11-03 14:20 UTC, ticket created (policy 4.1). Paused only while status is "Pending customer" (4.2): 2026-11-04 09:30 to 15:00 UTC, 5.5 hours, all inside business hours (event log). Business hours are 08:00 to 18:00 Europe/London, Monday to Friday, excluding English bank holidays (1.1); Europe/London is GMT = UTC in this period (1.1). 3, 4 and 5 November 2026 are Tuesday to Thursday with no bank holiday.
- First response: agent response at 2026-11-03 15:02 UTC (event log), 42 minutes after creation, so the first-response target is met at any level.
- Deadline: **Undetermined** as of now = 2026-11-05 11:00 UTC (stated by the user in the thread export). Elapsed since creation excluding the pause: 11 h 10 min of business hours (3 h 40 min on 3 Nov, 4 h 30 min on 4 Nov, 3 h on 5 Nov); 39 h 10 min of calendar time. Illustrations only, each assumes a support level the account record does not state, and the policy does not say which applies:
  - If Business: 20 business hours, 8 h 50 min remaining (about 44%, above the 25% at-risk threshold in 4.5), within target, deadline 2026-11-06 09:50 UTC.
  - If Standard: 40 business hours, about 28 h 50 min remaining, within target, deadline 2026-11-10 (Tuesday) 09:50 UTC (remaining 28 h 50 min counted from 2026-11-05 11:00: 7 h on 5 Nov, 10 h on 6 Nov, none on the weekend, 10 h on 9 Nov, 1 h 50 min on 10 Nov).
  - If Enterprise: 24 hours calendar, 39 h 10 min elapsed excluding the pause, so breached; deadline would have been 2026-11-04 19:50 UTC (24 h plus the 5.5 h pause). Policy 5.3 would then require the Support Duty Manager to be told, and none is recorded as told.
  - Policy 5.1 also allows escalation when a P2 is at risk; the escalation recorded here is for a ticket Tier 1 could not resolve.

## Recommended next action
Tier 2 should determine whether the v8.2.3 migration (deployed 1 Nov, "Card vault migrated to PayCollect v3") left tokens created before 1 Nov missing from the vault, starting with the token for INV-BV-20931 (created 14 Oct 2026). It comes first because the logs already show a clean split (all 31 failures on pre-1-Nov cards, all 7 successes on later cards) and the only unconfirmed step is the cause. Confirming it turns the "possible link" into a verified cause and decides the workaround and the fix path. In parallel, get the support level corrected in the account record, because it decides whether this ticket is breached.

Open questions:
- What is the customer's support level? The account record field is blank. If Enterprise the ticket is breached and the Support Duty Manager must be told (5.3).
- Did the v8.2.3 vault migration drop pre-1-Nov tokens, and can they be restored or migrated?
- Is there a practical workaround (customers re-entering and re-saving cards) that is usable at the front desk? This decides P2 versus P3.
- What did Priya Nair write in messages 1 to 6: the reconnect steps, and any statement about a credit? Does it support Sunil's account that a credit for October was mentioned?
- Has Callum Reid received the credit request and answered it in writing (6.3)? Agents must not promise a credit, fix date or release date (6.1, 6.2), and the customer wants written confirmation.
- Are other customers with cards saved before 1 Nov affected? (Not stated in the inputs.)

Next customer update due: 2026-11-05 16:00 UTC (James Whitfield's commitment, message 12). Policy 7.1 also requires at least one update each business day for P2.
