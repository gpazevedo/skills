# Handoff: QB-202861, Brackenridge Veterinary Group Ltd (BV-3307)

As-of: 2026-11-05 11:00 UTC (export time). Thread export is partial: messages 7 to 12 only.

## 1. Summary

Brackenridge Veterinary Group Ltd (account BV-3307) cannot collect saved-card payments in Quillbill Invoicing through the PayCollect card payments integration: 31 of 38 attempts since 2026-11-02 14:00 UTC failed with "PCX-402 token not found". The ticket is P2 and was escalated to Tier 2 at 2026-11-05 11:00 UTC. The customer is upset (clients declined at the front desk), Tier 2 now owns a customer update promised by 2026-11-05 16:00 UTC, and the customer demands a written credit decision. The service-level deadline cannot be computed because the account record has no support level.

## 2. Problem and evidence

- Card payments with saved cards are failing at the front desk; "every single card payment has failed since Monday" (2026-11-02). _Reported_ (message 8, Sunil Mehta, 2026-11-04 17:10). Part-contradicted by logs: 7 payments succeeded (next line).
- Since 2026-11-02 14:00 UTC there were 38 card payment attempts: 31 failed with "PCX-402 token not found", 7 succeeded. _Verified_ (payment logs, message 9, James Whitfield, 2026-11-05 09:40).
- All 31 failures used cards saved before 1 Nov; all 7 successes used cards saved on or after 1 Nov. _Verified_ (payment logs, message 9). Timezone for the "1 Nov" boundary is not stated.
- Retry of INV-BV-20931 at 2026-11-05 10:12 UTC failed with "PCX-402 token not found"; the PayCollect API response says "token not found in vault". The token on that invoice was created 2026-10-14. _Verified_ (message 11, internal note).
- PayCollect connection was re-authorised on 2026-11-04 at 14:41 UTC; 14 of the 31 failures are after that time. _Verified_ (integration log, message 11). So the reconnect happened and did not fix it. The customer's statement that they reconnected is therefore confirmed.
- Release v8.2.3 deployed 2026-11-01 says "Card vault migrated to PayCollect v3." _Verified_ as release-note text (message 11). _Hypothesis_: old saved-card tokens were not carried over by the vault migration. Nobody has tested this; message 11 says "not confirmed". Message 12 told the customer the failures point to "a problem on our side"; that is the same untested hypothesis.
- Ticket priority is P2 (ticket events, 2026-11-03 14:20 UTC). _Verified_ (ticket log). Policy 2.2 defines P2 as a major function such as payment collection not working with "no practical workaround". Cards saved on or after 1 Nov work, but no message says whether re-saving cards was offered or is practical. Do not change priority without recording it (policy 2.5).
- Customer impact: "clients come in to collect their pets and their saved card is declined at the desk". _Reported_ (message 8).

## 3. Tried so far

| Action | Result | Who |
| --- | --- | --- |
| Reconnect PayCollect, steps sent by support in messages 1 to 6 (content not visible) | Re-authorisation logged 2026-11-04 14:41 UTC; failures continued (message 7 "the reconnect didn't help"; 14 failures after it) | Customer carried it out; the author of the instructions is not visible (the customer says "your earlier message") |
| Other troubleshooting in messages 1 to 6 | result not recorded (messages 1 to 6 not in the export; James notes he cannot see them) | Priya Nair (Tier 1) and others, unknown |
| Payment log review, 2026-11-05 by 09:40 UTC | Found 31 failed and 7 succeeded; failures all on cards saved before 1 Nov | James Whitfield |
| Retry of collection on INV-BV-20931 at 2026-11-05 10:12 UTC (customer agreed in message 10) | Failed, "PCX-402 token not found"; no charge made | James Whitfield |
| Integration log check | Reconnect on 4 Nov 14:41 UTC confirmed | James Whitfield |
| Release notes check (v8.2.3) | Possible link to pre-1 Nov tokens; not confirmed | James Whitfield |
| Credit request passed to Callum Reid (CSM) | result not recorded (no reply from Callum and no ticket entry shown) | James Whitfield |

## 4. Commitments to the customer

| Quote | Author | Date (UTC) | Status |
| --- | --- | --- | --- |
| "I'll come back to you tomorrow morning." (after looking at the payment logs) | Priya Nair | 2026-11-04 15:40 | Kept in effect: the log findings were sent 2026-11-05 09:40 by James Whitfield after reassignment. Priya did not send it herself. |
| "I've passed your request to Callum Reid." (the October credit request) | James Whitfield | 2026-11-05 09:40 | Action stated as done; no confirmation on the ticket that Callum received or answered it. Not a credit promise. James also said he cannot agree credits. |
| "I'll update you by 16:00 UTC today." | James Whitfield | 2026-11-05 10:40 | Open. Due 2026-11-05 16:00 UTC, 5 hours after the as-of time. Tier 2 owns it from escalation (policy 5.2). Permitted under policy 6.1. |
| "I'm escalating this to our Product Engineering Support team now." | James Whitfield | 2026-11-05 10:40 | Kept: escalation event at 11:00 UTC. |

Disputed or unverifiable:
- The customer says "as you said in your message yesterday, we'll be expecting October's subscription fee to be credited" (message 8, 2026-11-04 17:10). "Yesterday" is 2026-11-03, within messages 1 to 6, which are not in the export. Whether any agent promised a credit is not verified; _reported_ only. In the visible messages no agent promises a credit. The account record shows "Open credits: None recorded". Policy 6.2 forbids agents promising credits and 6.3 allows only the named CSM (Callum Reid) or the Head of Support to offer one, in writing on the ticket or account record. Check messages 1 to 6 for this.
- Customer demand: "I want the credit confirmed in writing, not passed around" (message 10, 2026-11-05 09:55). Unanswered and open.

## 5. Service level

- Tier: not determinable. The account record field "Support level:" is blank. Policy 1.3 says the level is the one in the account record, and policy 3.1 targets depend on it (Standard, Business or Enterprise).
- Priority: P2 (ticket log; policy 2.2).
- First response, resolution target and deadline: not stated in the supplied policy for this account, since no level is recorded. No deadline is given. Do not assume a level.
- Clock start: 2026-11-03 14:20 UTC, ticket creation (policy 4.1).
- Paused: "Pending customer" 2026-11-04 09:30 to 15:00 UTC = 5 h 30 min (policy 4.2, 4.3).
- Elapsed, calendar, as-of 2026-11-05 11:00 UTC: 3 Nov 14:20 to 5 Nov 11:00 = 44 h 40 min, minus 5 h 30 min paused = 39 h 10 min. Business-hour elapsed time is not computed because no target applies.
- Status (breached, at risk, within target): cannot be determined (policy 4.5 needs a resolution target). Consequences: whether the Duty Manager must be told (policy 5.3, breached P2) is unknown.
- First response occurred 2026-11-03 15:02 UTC, 42 min after creation (ticket log), but cannot be compared to any target.
- Update cadence: P2 needs an update at least once per business day (policy 7.1). Visible updates: 4 Nov 15:40, 5 Nov 09:40, 5 Nov 10:40.

## 6. Recommended next action

Primary (owner: Tier 2 engineer, Product Engineering Support): check the PayCollect v3 card-vault migration released in v8.2.3 (1 Nov) for tokens created before 1 Nov. Compare the token for INV-BV-20931 (created 2026-10-14) and the 31 failed attempts against the 7 successful ones, and check whether the migration skipped or lost pre-1 Nov tokens. This confirms or rules out the hypothesis that the migration caused the "token not found in vault" failures. It serves the open commitment to update the customer by 2026-11-05 16:00 UTC, so the Tier 2 owner should send an update by then, stating what is known without promising a fix date (policy 6.2).

Alternatives:
1. Tier 2 owner or Tier 1 lead: get the customer's support level corrected in the account record (with the account owner or contracts) so the service-level status can be set. Serves the deadline calculation.
2. Tier 2 owner: contact Callum Reid directly to confirm he has the October credit request and will respond in writing on the ticket (policy 6.3). Serves the customer's written-confirmation demand. Tier 2 must not promise a credit itself.
3. Tier 2 owner: once the cause is understood, test whether re-saving one affected card works as a workaround (cards saved on or after 1 Nov succeeded). This would confirm a workaround exists, which also bears on whether P2 is the right priority (policy 2.2 and 2.3). Do not offer it to the customer as a fix until tested.

## 7. Gaps and conflicts

- Messages 1 to 6 (2026-11-03 14:20 to 2026-11-04 15:00 UTC) are missing. The reconnect instructions, other steps tried, and any alleged credit statement cannot be checked. Retrieve them from the full ticket.
- Account record has no support level. Service-level targets, deadline and breach status cannot be set.
- Customer says an agent promised the credit "yesterday". Not verifiable here; the policy would not allow an agent to promise it.
- Customer says "every single card payment has failed since Monday"; logs show 7 of 38 succeeded, all on cards saved on or after 1 Nov. Customer's start date (Monday 2 Nov) matches the log window start (14:00 UTC), but the earliest failure time is not stated.
- Release v8.2.3 was deployed 2026-11-01; the log window begins 2026-11-02 14:00 UTC. Whether any failures occurred before that is not stated. Cause is not confirmed.
- Whether any pre-1 Nov card still works is not stated (all 31 failures were pre-1 Nov cards, but how many pre-1 Nov attempts exist overall is not stated, so all pre-1 Nov cards failing is not shown).
- No record of Callum Reid's reply or acknowledgement.
- Policy gaps: no support level terms for this account; Duty Manager notification status unknown.
