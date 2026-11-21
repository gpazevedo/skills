Clarifying question: What is the support level (Standard, Business or Enterprise) for account BV-3307? The "Support level" field in the account record is blank, and the plan name "Quillbill Clinic" is not one of the three levels in policy 1.3.

# Escalation handoff: QB-202861: Saved cards from before 1 Nov fail with "PCX-402 token not found" since the v8.2.3 card vault migration (suspected)

**Customer:** Brackenridge Veterinary Group Ltd (BV-3307), Quillbill Clinic plan, support level not recorded · **Priority:** P2 · **Next deadline:** cannot determine (support level missing); next known commitment is the customer update by 2026-11-05 16:00 UTC, outstanding, 5h 00m left (as of 2026-11-05 11:00 UTC)

## Problem as currently understood
Card payments made with saved cards fail with "PCX-402 token not found" for Brackenridge. The practice reports this at front desks. In the logs, every failure uses a card saved before 1 November and every success uses a card saved on or after 1 November. The leading explanation is that the v8.2.3 deployment on 1 November ("Card vault migrated to PayCollect v3") lost or did not carry over older tokens. This is not confirmed. The customer's PayCollect reconnect on 4 November did not fix it.

Evidence:
- [Verified] Since 2 Nov 14:00 UTC there were 38 card payment attempts: 31 failed with "PCX-402 token not found", 7 succeeded (James Whitfield, message 9, 2026-11-05 09:40; internal note, message 11, 10:20)
- [Verified] All 31 failures used cards saved before 1 Nov; all 7 successes used cards saved on or after 1 Nov (James Whitfield, message 9, 09:40)
- [Verified] Retry of INV-BV-20931 at 10:12 on 5 Nov failed with the same error. The card token was created 14 Oct 2026, and the PayCollect API said "token not found in vault" (James Whitfield, internal note, message 11, 10:20; message 12, 10:40). No charge was made.
- [Verified] The integration log shows PayCollect was re-authorised on 4 Nov at 14:41 UTC. 14 of the 31 failures are after that time (James Whitfield, internal note, message 11, 10:20)
- [Verified] Release notes for v8.2.3, deployed 1 Nov, say "Card vault migrated to PayCollect v3" (James Whitfield, internal note, message 11, 10:20)
- [Reported] "Every single card payment has failed since Monday" (Sunil Mehta, message 8, 2026-11-04 17:10). The logs contradict "every": 7 attempts succeeded.
- [Reported] Clients' saved cards are declined at the desk (Sunil Mehta, message 8, 2026-11-04 17:10)
- [Reported] The customer followed Priya's earlier reconnect instruction (Sunil Mehta, message 8, 2026-11-04 17:10). Messages 1 to 6 are not in the export, so the instruction itself is not seen.
- [Inferred] The vault migration most likely invalidated or dropped tokens saved before 1 Nov (rests on: the before/after 1 Nov split in all 38 attempts, token created 14 Oct not found in vault, v8.2.3 release note). Not confirmed by anyone.
- [Inferred] The customer's reconnect is not the cause or the fix (rests on: failures continuing after the 14:41 re-authorisation).
- [Inferred] Re-saving a card may work as a workaround, since cards saved on or after 1 Nov succeed. Nobody has tested this (rests on: the 7 successes).

## Tried so far
| When (UTC) | Who | Action | Result |
| --- | --- | --- | --- |
| 2026-11-03 to 2026-11-04 15:00 | Priya Nair | Messages 1 to 6, including a reconnect instruction to the customer (as the customer describes it) | Not in export; no result recorded |
| 2026-11-04 14:41 | Sunil Mehta (customer) | Re-authorised the PayCollect connection | Failures continued (14 after this time) |
| 2026-11-04 15:40 | Priya Nair | Said she would look at the payment logs | Not done by her; James did this on 5 Nov |
| 2026-11-05 09:40 | James Whitfield | Checked payment logs for the account | 38 attempts, 31 failed, 7 succeeded; the failures match the pre-1 Nov card pattern |
| 2026-11-05 10:12 | James Whitfield | Retried collection on INV-BV-20931, with customer consent (message 10) | Failed again, "token not found in vault"; no charge |
| 2026-11-05 09:40 | James Whitfield | Passed the credit request to Callum Reid (stated in message 9) | No result recorded; no record of Callum's reply |

Ruled out: the customer's PayCollect connection and settings. The reconnect happened and the failures continued.

## Commitments to the customer
| Commitment (quoted) | Made by | When | Status |
| --- | --- | --- | --- |
| "I'll come back to you tomorrow morning." (resolves to the morning of 2026-11-05, Inferred) | Priya Nair | 2026-11-04 15:40 UTC | Met: James replied at 09:40 on 2026-11-05 with the log findings |
| "I'll update you by 16:00 UTC today." (2026-11-05 16:00 UTC) | James Whitfield | 2026-11-05 10:40 UTC | Outstanding, 5h 00m left. Tier 2 now owns it (policy 5.2) |
| "I've passed your request to Callum Reid." | James Whitfield | 2026-11-05 09:40 UTC | An action taken by support, not a promise of an outcome; no reply from Callum is recorded. The customer expects written confirmation. |

Claimed by the customer, not found in the thread: that Priya said in a message on 4 Nov ("your message yesterday") that October's subscription fee would be credited. Messages 1 to 6 are not in the export, so this can be neither confirmed nor ruled out. Policy 6.2 and 6.3 do not let a support agent promise a credit, and no valid credit offer is recorded. Account record: open credits "None recorded".

## Service level
- Plan: Quillbill Clinic (account record). Support level: blank in the account record, so no target can be chosen. Cannot determine: support level missing.
- Priority: P2. The ticket was created as P2 via the portal, and the escalation event on 2026-11-05 11:00 still shows P2. No support agent is recorded as setting or changing it. Policy 2.2 (payment collection does not work) fits (Inferred). A "practical workaround" under 2.3 has not been shown.
- Target: cannot determine: support level missing. Policy 3.1 gives different P2 targets for Standard, Business and Enterprise, and the plan name does not map to any of them.
- Clock: starts at ticket creation, 2026-11-03 14:20 UTC (policy 4.1). The only pause is while the status is "Pending customer" (4.2): 2026-11-04 09:30 to 15:00 UTC (event log, Verified). Business hours are 08:00 to 18:00 Europe/London, which equals UTC from 25 October (policy 1.1). No bank holiday falls in the period.
- Elapsed time, as of 2026-11-05 11:00 UTC, excluding the pause: 11h 10m business time (3h 40m on 3 Nov, 4h 30m on 4 Nov, 3h 00m on 5 Nov) and 39h 10m calendar time.
- First response: 2026-11-03 15:02 UTC, 42 minutes after creation (Verified, event log). The target is not determinable, but 42 minutes is inside every P2 first-response target in 3.1.
- Resolution deadline and status: cannot determine: support level missing. Once the level is known, apply the P2 resolution target from 3.1 to the elapsed time above. Policy 3.3 says only 24x7 targets run on calendar time. Whether the ticket is breached or at risk (policy 4.5) depends on the level.

## Recommended next action
Tier 2 (Product Engineering Support) should check, before sending the 16:00 UTC customer update, whether the pre-1 Nov tokens exist in the PayCollect v3 vault after the v8.2.3 migration. The same check should test whether re-saving one affected card works. This is the main unconfirmed claim, and the answer shows whether the customer has a workaround. Follow-ups: (1) ask the account owner or Callum Reid to confirm the support level today, so the deadline and the Duty Manager duty under policy 5.3 can be settled; (2) get Callum Reid's written reply on the credit request to the customer. Tier 2 should not promise a fix date or a credit (policy 6.2).

## Gaps and open questions
- Support level is blank in the account record, so the target, deadline and breach status cannot be determined.
- Messages 1 to 6 are missing from the export. This covers the original problem description, the reconnect instruction and the claimed credit statement. Priya's actions cannot be verified.
- Cause is unconfirmed: the vault migration link is only a release note and a pattern. Nobody has checked whether the tokens exist in the PayCollect v3 vault.
- The customer says every payment failed, but the logs show 7 successes. All 7 used cards saved on or after 1 Nov, so the customer's claim may be right for their older saved cards only.
- The logs begin at 2 Nov 14:00 UTC, while the deployment was on 1 Nov. Failures between 1 Nov and 2 Nov 14:00 are not covered by the log summary.
- Whether Callum Reid has received or answered the credit request is not recorded.
- Please confirm the support level for account BV-3307.
