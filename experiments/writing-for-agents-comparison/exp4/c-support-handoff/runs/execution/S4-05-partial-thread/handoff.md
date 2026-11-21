# Escalation handoff: QB-202861, Brackenridge Veterinary Group Ltd (BV-3307)

**Summary:** Saved cards stored before 1 Nov 2026 fail with "PCX-402 token not found" on PayCollect; the customer cannot take desk card payments. The next customer update is due by 16:00 UTC today (5 Nov), and the service-level deadline cannot be computed because the account record has no support level.
**Reference time:** 2026-11-05 11:00 UTC (the export's stated as-of time; it is also the latest thread entry, the escalation event)

Note: the export holds messages 7 to 12 only. Messages 1 to 6 (3 Nov 14:20 to 4 Nov 15:00 UTC) are not in it.

## Problem as currently understood
Card payments made with cards saved before 1 Nov 2026 fail with "PCX-402 token not found"; cards saved on or after 1 Nov succeed. The failures began after v8.2.3 (deployed 1 Nov), which migrated the card vault to PayCollect v3, and the customer's PayCollect reconnect did not fix them. The cause is not confirmed.
- [Verified] 38 card payment attempts since 2 Nov 14:00 UTC: 31 failed with "PCX-402 token not found", 7 succeeded (James Whitfield, msg 9, 5 Nov 09:40; log check)
- [Verified] All 31 failures used cards saved before 1 Nov; all 7 successes used cards saved on or after 1 Nov (James Whitfield, msg 9, 5 Nov 09:40; log check)
- [Verified] Retry of INV-BV-20931 at 10:12 on 5 Nov failed with the same error; the API says "token not found in vault"; the token was created 14 Oct 2026; no charge was made (James Whitfield, msg 11 and 12)
- [Verified] PayCollect was re-authorised on 4 Nov 14:41 UTC; 14 of the 31 failures came after that (James Whitfield, msg 11, integration log)
- [Verified] v8.2.3 deployed 1 Nov, release note "Card vault migrated to PayCollect v3" (James Whitfield, msg 11, release notes). The link to the failures is [Reported] by an agent, not confirmed.
- [Reported] Every card payment has failed since Monday (2 Nov) (Sunil Mehta, msg 8). This conflicts with the logs (7 successes); the logs govern.
- [Reported] Clients' saved cards are declined at the desk (Sunil Mehta, msg 8)
Open questions:
- Did the v3 vault migration drop or fail to migrate tokens saved before 1 Nov?
- Can the old tokens be restored or migrated, or must customers re-save cards? Is a workaround available (for example taking the card again at the desk)?
- Are other accounts affected? (Not asked in the thread.)
- Is the vault problem the only cause, given the 31/7 split could also have another explanation?

## Tried so far
- Reconnect of PayCollect (steps sent by Priya Nair in messages 1 to 6, not visible), by the customer, before 4 Nov 14:41: re-authorisation happened [Verified, integration log]; failures continued
- Payment log review, by James Whitfield, 5 Nov 09:40: pattern above
- Retry of collection on INV-BV-20931, by James Whitfield, 5 Nov 10:12, with customer consent (msg 10): failed, "PCX-402 token not found"
- Messages 1 to 6: other actions not visible (James could not see them); result not recorded here

## Commitments to the customer
- "I'll come back to you tomorrow morning" (look at payment logs), Priya Nair, 4 Nov 15:40: met. James replied with the log findings at 09:40 on 5 Nov.
- "I'll update you by 16:00 UTC today", James Whitfield, 5 Nov 10:40: outstanding, due in 5 hours. Tier 2 now owns it (policy 5.2).
- "I've passed your request to Callum Reid" (October credit), James Whitfield, 5 Nov 09:40: unclear. The thread shows no record that the request reached Callum Reid, and no response from him. He is the Customer Success Manager in the account record, so he may offer credits (policy 6.3).
- Claimed by customer, not found in thread: that Priya said "yesterday" (4 Nov) the October subscription fee would be credited (Sunil Mehta, msg 8). Message 7 does not say it; messages 1 to 6 are not in the export, so it cannot be checked. Any such promise would breach policy 6.3, and only a written offer from Callum Reid or the Head of Support is valid.
- Customer demand: October credit confirmed in writing (Sunil Mehta, msg 10). This is not a commitment by Quillbill; no credit has been offered.

## Service level
- Tier: Not determinable. The "Support level" field in the account record is blank (policy 1.3 takes the level from the account record). The plan is "Quillbill Clinic", which the policy does not map to a level.
- Priority: P2 (recorded on the ticket by support at creation, 3 Nov 14:20, and again at escalation, 5 Nov 11:00)
- Target: Not determinable. Policy 3.1 sets different P2 targets by level (Enterprise 24 hours calendar; Business 20 business hours; Standard 40 business hours), and the policy has no single target for all customers.
- Deadline: Not determinable, for the same reason. Clock facts known: it started 3 Nov 14:20 (policy 4.1) and was paused 4 Nov 09:30 to 15:00 (5.5 hours, policy 4.2).
- Status: Not determinable. Policy 5.1 requires escalation of a P2 that is at risk, and 5.3 requires telling the Support Duty Manager of a P2 that is breached; neither can be checked.

## Recommended next action
Tier 2 should investigate the PayCollect v3 vault migration for tokens created before 1 Nov (for example INV-BV-20931, token created 14 Oct) to confirm whether they are missing and whether they can be restored, because 31 of 31 failures involve pre-1 Nov cards and 7 of 7 successes involve later ones. Also ask the account owner or support management to fill the support level in the account record, so the deadline can be computed, and make sure Callum Reid has the credit request. Serves: the 16:00 UTC update today; the resolution target once the level is known.
Tell the customer: by 16:00 UTC today, report that the problem is with older saved cards and is under investigation by Product Engineering Support, and give a time for the next update. Do not promise a fix date or a credit (policy 6.2); say the credit request is with the Customer Success Manager, who alone can offer one in writing (6.3), once that is confirmed.

## Blocked
- Account record: support level is blank, which blocks the Service level section (tier, target, deadline, status).
- Ticket messages 1 to 6 are missing from the export, so the original report, the reconnect steps sent, and any credit remark by Priya cannot be checked.
