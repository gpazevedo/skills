# Escalation handoff: QB-202861, Brackenridge Veterinary Group Ltd (BV-3307)

**In one line:** Saved cards created before 1 Nov 2026 fail card payments with "PCX-402 token not found" (31 of 38 attempts since 2 Nov), probably linked to the v8.2.3 card vault migration. A customer update is due by 16:00 UTC today (5 Nov), and the support level is blank in the account record, so the resolution deadline is unknown (it could already be breached).

## Problem as currently understood
- [verified] 38 card payment attempts on the account since 2 Nov 14:00 UTC: 31 failed with "PCX-402 token not found", 7 succeeded. (evidence: payment log check, James Whitfield, message 9, 5 Nov 09:40)
- [verified] All 31 failures used cards saved before 1 Nov; all 7 successes used cards saved on or after 1 Nov. (evidence: same payment log check, message 9)
- [verified] Retry of INV-BV-20931 at 10:12 on 5 Nov failed with "PCX-402 token not found". The token was created 14 Oct 2026, and the PayCollect API said "token not found in vault". (evidence: retry, James Whitfield, internal note message 11, 5 Nov 10:20; customer consented in message 10)
- [verified] The PayCollect connection was re-authorised on 4 Nov at 14:41 UTC, and 14 of the 31 failures happened after that. So the customer's reconnect happened and did not fix it. (evidence: integration log read by James Whitfield, message 11)
- [verified] Release notes for v8.2.3 (deployed 1 Nov) say "Card vault migrated to PayCollect v3." (evidence: release notes read by James Whitfield, message 11)
- [suspected] The v3 vault migration did not carry over tokens saved before 1 Nov. (held by: James Whitfield, messages 11 and 12; basis: the timing matches, and every failure is a pre-1 Nov token and every success a post-1 Nov token; the note says "not confirmed")
- [reported] Clients' saved cards are being declined at the desk, which embarrasses staff. (source: Sunil Mehta, 4 Nov 17:10)
- [reported] "Every single card payment has failed since Monday" (Monday is 2 Nov). (source: Sunil Mehta, 4 Nov 17:10)
- [reported] The customer reconnected PayCollect as instructed by support. (source: Sunil Mehta, message 8. The reconnect itself is verified above, but which steps were sent is not visible, see Gaps.)
- Conflicts: the customer says every card payment has failed; the payment logs show 7 of 38 succeeded (all with cards saved on or after 1 Nov). The customer says October's fee was promised as a credit ("as you said in your message yesterday"); nothing in messages 7 to 12 shows that promise, and messages 1 to 6 were not supplied, so it is unconfirmed (see Commitments). No conflicts on account facts (plan, region, contacts).

## Tried so far
| What was tried | Who, when | Result |
|---|---|---|
| Reconnect of PayCollect (steps sent in messages 1 to 6, content not visible) | Customer at support's request; re-authorised 4 Nov 14:41 UTC | Did not help; failures continued after it (14 of 31) |
| Payment log review | James Whitfield, 5 Nov 09:40 | Found the pre/post 1 Nov card pattern (see above) |
| Retry collection on INV-BV-20931 (customer consented) | James Whitfield, 5 Nov 10:12 | Failed again with "PCX-402 token not found"; no charge made |
| Credit request passed to Callum Reid (Customer Success Manager) | James Whitfield, 5 Nov 09:40 | No result recorded |
| Other steps in messages 1 to 6 | Priya Nair and customer, 3 to 4 Nov | Not visible: partial export |

## Commitments to the customer
| Commitment (quoted) | Made by | When | Due | Status |
|---|---|---|---|---|
| "I'll come back to you tomorrow morning." | Priya Nair (Tier 1) | 4 Nov 15:40 | morning of 5 Nov | met: James Whitfield replied at 09:40 on 5 Nov |
| "I'll update you by 16:00 UTC today." | James Whitfield (Tier 1) | 5 Nov 10:40 | 5 Nov 16:00 UTC | pending, 5h00m left as of 11:00 UTC. Tier 2 owns it (policy 5.2) |

Not commitments in the supplied material: the customer's request that October's fee be credited and confirmed in writing (a claim and a request; James said "I'm not able to agree credits" and passed it on). Sunil's statement that support promised the credit cannot be checked: the message he refers to is not in the export, and policy 6.2 and 6.3 say agents cannot promise credits. Only Callum Reid or the Head of Support can offer one, in writing on the ticket or account record. No offer is recorded.

## Service level
- Tier: not stated in the account record. "Support level:" is blank; "Quillbill Clinic" is the plan name, not a support level. Policy 1.3: "A customer's support level (Standard, Business or Enterprise) is the level recorded in the customer's account record." Do not assume one.
- Priority/severity: P2, set at ticket creation and shown again at escalation (ticket event log, 3 Nov 14:20 and 5 Nov 11:00). Policy 2.2: "a major function, such as invoice sending, payment collection or bank feeds, does not work and there is no practical workaround."
- Target (policy 3.1, P2 resolution, by level; the applicable one is unknown):
  - Enterprise: 24 hours, 24x7.
  - Business: 20 business hours.
  - Standard: 40 business hours.
  - First response (P2): Enterprise 2 hours, Business 4 business hours, Standard 8 business hours. Met at every level: the first agent response (message 2) was at 15:02 on 3 Nov, 42 minutes after creation.
- Clock rule: policy 4.1 "The clock starts when the ticket is created." Policy 4.2 "The clock is paused only while the ticket status is 'Pending customer'." Business hours (1.1): 08:00 to 18:00 Europe/London, Monday to Friday; London is GMT = UTC from 25 Oct 2026. "24x7" targets run on calendar time (3.3). The event log is complete, so the pause is known: Pending customer 4 Nov 09:30 to 15:00 (5h30m). 3 to 5 Nov are weekdays; no bank holidays are stated in the sources.
- Deadline (arithmetic shown, with the pause applied, per 4.2; start 3 Nov 14:20 UTC):
  - Enterprise (24h calendar): 14:20 to 09:30 on 4 Nov = 19h10m used; 4h50m remains after resume at 15:00, so the deadline is **4 Nov 19:50 UTC**. Without the pause it would be 4 Nov 14:20.
  - Business (20 business hours): 3 Nov 14:20 to 18:00 = 3h40m; 4 Nov 08:00 to 09:30 = 1h30m (5h10m); 4 Nov 15:00 to 18:00 = 3h (8h10m); 5 Nov 08:00 to 18:00 = 10h (18h10m); 1h50m remains, so the deadline is **6 Nov 09:50 UTC**. Without the pause: 3h40m + 10h + 6h20m, so 5 Nov 14:20 UTC.
  - Standard (40 business hours): 18h10m used by the end of 5 Nov (as above); 6 Nov full day 10h (28h10m); 9 Nov (Monday) 10h (38h10m); 1h50m remains, so the deadline is **10 Nov 09:50 UTC**. Without the pause: 9 Nov 14:20 UTC.
- Status as of now (5 Nov 11:00 UTC, the export's stated as-of time). Time used with the pause applied: 3h40m + 4h30m (4 Nov 08:00 to 09:30 and 15:00 to 18:00) + 3h (5 Nov 08:00 to 11:00) = 11h10m business hours. Calendar time used: 44h40m minus 5h30m pause = 39h10m. Not resolved (status Escalated).
  - Enterprise: **breached**, 15h10m over (39h10m used against 24h). Policy 5.3 would then require telling the Support Duty Manager.
  - Business: **within target**, 8h50m left (44%; "at risk" is under 25%, i.e. under 5h). Without the pause: at risk, 3h20m left.
  - Standard: **within target**, 28h50m left. Without the pause: within target, 23h20m left.
  - Overall status: cannot be determined until the support level is confirmed.
- Update cadence (policy 7.1): P2, an update at least once each business day.

## Recommended next action
1. Resolve the service level first: ask Callum Reid or the contracts owner (Fiona Brackenridge is the contract contact) for the support level recorded on BV-3307, and fix the blank record. If it is Enterprise, the ticket is breached, so tell the Support Duty Manager (policy 5.3).
2. Technical check (cheapest test of the leading suspicion): look up the token on INV-BV-20931 (created 14 Oct) and the migration job log for the v8.2.3 card vault migration to PayCollect v3, and check whether tokens created before 1 Nov were migrated (UK region).
   - If the pre-1 Nov tokens are missing from the v3 vault: the cause is confirmed. Engineering then needs a re-migration or fix; do not give the customer a fix date (policy 6.2). Also scope the impact on other accounts.
   - If the tokens are present in the v3 vault: the migration is ruled out as the cause. Look at the v3 token lookup path (region or key handling) and the re-authorisation, since failures continued after it.
3. Customer update by 16:00 UTC today (Tier 2 owns this commitment). Content: the finding that failures affect cards saved before 1 Nov and that engineering is investigating; the 7 successes with newer cards (so "every payment" is not quite right, which can be said gently); the time of the next update; the credit request is with Callum Reid. Do not promise a fix date, a release date, a credit or a refund (policy 6.2).
4. Credit: chase Callum Reid for a written response on the ticket or account record (policy 6.3). Sunil asked for written confirmation.
5. Retrieve messages 1 to 6 to check what was said about the reconnect steps and whether any credit promise was made.
6. Possible workaround, unverified: re-saving cards after 1 Nov appears to work (7 successes). Test it before offering it.

## Gaps
- Support level is blank in the account record: the target, deadline and breach status all depend on it.
- Messages 1 to 6 (3 Nov 14:20 to 4 Nov 15:00 UTC) are missing: the customer's original description, the reconnect steps given, and whether anyone mentioned a credit (the customer says so; unconfirmed).
- No bank holiday information in the sources (none is assumed for 3 to 10 Nov).
- Nobody has checked whether tokens were migrated, whether other customers are affected, or whether re-saving a card works as a workaround.
- Whether the Support Duty Manager has been told: not stated in the thread.
- No response from Callum Reid recorded.
