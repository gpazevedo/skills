# Handoff: QB-202861, Brackenridge Veterinary Group Ltd (BV-3307), to Tier 2 (Product Engineering Support)

As-of: 2026-11-05 11:00 UTC (escalated at 11:00). Priority P2. Status Escalated.

## 1. Problem and evidence

**Problem:** Saved-card payments through PayCollect fail with "PCX-402 token not found" for cards saved before 1 November 2026. Cards saved on or after 1 November work. Likely link to the v8.2.3 card vault migration (not confirmed).

Evidence:
- Verified (payment logs, James Whitfield, msg 9, 2026-11-05 09:40): since 2 Nov 14:00 UTC, 38 attempts, 31 failed with "PCX-402 token not found", 7 succeeded.
- Verified (same logs, msg 9): all 31 failures used cards saved before 1 Nov; all 7 successes used cards saved on or after 1 Nov.
- Verified (retry, msg 11, 10:20): retry of INV-BV-20931 at 10:12 failed with the same error. Token was created 14 Oct 2026. PayCollect API said "token not found in vault". No charge was made (msg 12).
- Verified (integration log, msg 11): PayCollect was re-authorised 4 Nov 14:41 UTC. 14 of the 31 failures are after 14:41 on 4 Nov. The reconnect did not fix it.
- Verified (release notes, msg 11): v8.2.3, deployed 1 Nov: "Card vault migrated to PayCollect v3." The link to the failures is a hypothesis only. Not confirmed.
- Reported (Sunil Mehta, msg 8, 11-04 17:10): "every single card payment has failed since Monday"; clients' saved cards declined at the desk. Conflict: logs show 7 successes, so not every payment failed. Start date (Mon 2 Nov) is consistent with the log window start, but the log window begins 2 Nov 14:00, so earlier failures are not checked.
- Reported (Sunil, msg 8): they reconnected PayCollect as instructed. Partly verified: a re-authorisation on 4 Nov 14:41 is in the integration log. The steps Priya sent are not visible to us.
- Unverified: whether failures occurred between 1 Nov and 2 Nov 14:00; whether any pre-1 Nov token works.

## 2. Tried and results

Messages 1 to 6 (2026-11-03 14:20 to 2026-11-04 15:00) are not in the export, so earlier attempts are largely unknown.

| Who | When (UTC) | What | Result |
| --- | --- | --- | --- |
| Priya Nair (T1) | 11-03 15:02 | First response (msg 2) | Content not available |
| Priya Nair | 11-04 09:30 | Status set to Pending customer | Customer replied 15:00 |
| Customer / Priya | before 11-04 15:00 | Reconnect of PayCollect (per Sunil msg 8 and Priya msg 7) | Failed. Re-authorisation logged 11-04 14:41; failures continued |
| Priya Nair | after 11-04 15:40 | Look at payment logs (said she would, msg 7) | No result recorded. James did the log review instead |
| James Whitfield | 11-05 09:40 | Payment log review (msg 9) | Pattern found: pre-1 Nov saved cards fail |
| James Whitfield | 11-05 10:12 | Retry collection on INV-BV-20931, with customer consent (msgs 9, 10) | Failed, same error; no charge |
| James Whitfield | 11-05 10:40 / 11:00 | Escalated to Tier 2 | Done |
| James Whitfield | 11-05 09:40 | Passed the credit request to Callum Reid (msg 9) | No record on the ticket that Callum received or answered it |

James could not see which reconnect steps were sent or what else was tried in messages 1 to 6. Please read the full ticket.

## 3. Commitments to the customer

- Priya Nair, msg 7, 2026-11-04 15:40: "I'll come back to you tomorrow morning." Appears met by msg 9 at 09:40 on 11-05. Ambiguous whether "tomorrow morning" was meant as a results update.
- James Whitfield, msg 9, 2026-11-05 09:40: "I've passed your request to Callum Reid." This is a statement of an action taken, not a promise of an outcome. No credit was promised ("I'm not able to agree credits").
- James Whitfield, msg 12, 2026-11-05 10:40: "I'll update you by 16:00 UTC today." Open. Due 2026-11-05 16:00 UTC. Under policy 5.2, Tier 2 now owns this commitment.
- Disputed, not verifiable: Sunil (msg 8) says Priya said in a message "yesterday" (11-03 or 11-04, within messages 1 to 6 or msg 7) that October's subscription fee would be credited. Msg 7 as exported contains no credit promise. Check messages 1 to 6. Policy 6.2 and 6.3 bar agents from offering credits. Only the Customer Success Manager named in the account record (Callum Reid) or the Head of Support may. A valid offer must be written on the ticket or account record. None is recorded ("Open credits: None recorded").
- Customer demand, msg 10: "I want the credit confirmed in writing, not passed around." Unanswered. Needs a Callum Reid decision.

## 4. Service level and deadline

**Not determinable from the supplied policy and account record.** The account record field "Support level:" is blank. Policy 1.3: "A customer's support level (Standard, Business or Enterprise) is the level recorded in the customer's account record." Needed: the support level for BV-3307 (the plan name "Quillbill Clinic" does not map to a level in the policy). Do not assume one.

What can be computed from the inputs:
- Priority P2, set at creation 2026-11-03 14:20 UTC, unchanged. Clock start (policy 4.1): ticket creation, 11-03 14:20 UTC.
- Pause (4.2): only while "Pending customer": 11-04 09:30 to 15:00 UTC (5h30m).
- Business hours (1.1): 08:00 to 18:00 London time Mon to Fri; London = UTC from 25 Oct 2026 (1.1). No England bank holiday found 3 to 5 Nov (not checked against a calendar).
- Business hours elapsed, excluding pause, to 11-05 11:00: 11-03 14:20 to 18:00 = 3h40m; 11-04 08:00 to 09:30 = 1h30m; 11-04 15:00 to 18:00 = 3h00m; 11-05 08:00 to 11:00 = 3h00m. Total 11h10m.
- Calendar hours elapsed, excluding pause: 11-03 14:20 to 11-05 11:00 = 44h40m, less 5h30m = 39h10m.
- First response: 11-03 15:02, 42 minutes after creation (0h42m business). Met under every level (Enterprise P2 2h 24x7; Business 4 business h; Standard 8 business h).

Resolution outcome by level (policy 3.1, P2; "at risk" = under 25% remaining, 4.5):

| Level | Resolution target | Elapsed | Remaining | Status |
| --- | --- | --- | --- | --- |
| Standard | 40 business hours | 11h10m | 28h50m (72%) | within target |
| Business | 20 business hours | 11h10m | 8h50m (44%) | within target |
| Enterprise | 24 hours, 24x7 | 39h10m calendar | -15h10m | **breached** |

If Enterprise: 5.3 requires the Support Duty Manager to be told (P2 breached).
If Business: 8h50m remain from 11-05 11:00 (7h to 18:00, then 1h50m from 08:00 on 11-06), so the deadline is 2026-11-06 09:50 UTC. It becomes "at risk" (under 5h left) at 2026-11-05 14:50 UTC.
If Standard: 28h50m remain (7h on 11-05, 10h on 11-06, 10h on Mon 11-09, then 1h50m), so the deadline is 2026-11-10 09:50 UTC.

Clauses used: 1.1, 1.3, 3.1, 3.3, 4.1 to 4.5, 5.3.

## 5. Recommended next action

**Owner: Tier 2 (Product Engineering Support).** Investigate whether the v8.2.3 card vault migration to PayCollect v3 left pre-1 Nov saved-card tokens unmigrated, and fix or migrate them.

Reason: all 31 failures are pre-1 Nov cards, all 7 successes are post-1 Nov cards, the error is "token not found in vault", the reconnect did not help, and the vault migration shipped 1 Nov.

First check: look up the token on INV-BV-20931 (created 14 Oct 2026) in the PayCollect v3 vault and in the migration log. Then check whether other BV-3307 tokens and other customers are affected.

Also, today:
1. Get the support level for BV-3307 from the account record owner (Callum Reid or Dr Fiona Brackenridge's contract) and fix the blank field; then apply section 4. If Enterprise, notify the Support Duty Manager.
2. Send the 16:00 UTC update to Sunil (Tier 2 owns it).
3. Ask Callum Reid to answer the credit request in writing on the ticket (only he or the Head of Support may). Do not promise a fix date, release date or credit (6.2).
4. Assess priority: consider whether data loss (tokens missing) meets P1 (2.1) and whether the workaround (customer entering cards again, which appears to work for cards saved after 1 Nov) is practical. The workaround is unverified.

Open questions for engineering: Are other customers' pre-1 Nov tokens affected? Were any tokens migrated, and did the 14 Oct token exist before? What happened 1 Nov to 2 Nov 14:00 (log window)?

Open questions for the customer: Did any failure occur before Monday 2 Nov? Does re-entering and saving a card work at the desk? Which message do you say contained a credit promise?

## 6. Gaps (missing inputs, conflicts, unverified assumptions)

- Missing: messages 1 to 6 (the original report, Priya's first response, the reconnect instructions, the alleged credit statement).
- Missing: support level in the account record (blank). Service-level deadline and breach status cannot be determined.
- Conflict: customer says all payments failed; logs show 7 of 38 succeeded.
- Conflict: customer says Priya promised a credit; the exported message 7 contains none; earlier messages not seen.
- Conflict: Priya's msg 7 refers to an earlier message about the next step ("As I said in my earlier message"); not visible.
- Unverified: link to v8.2.3 migration; whether credit request reached Callum Reid; no bank-holiday check; the per-level deadlines depend on the unknown support level.
