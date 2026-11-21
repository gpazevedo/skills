Clarifying question: The account record's "Support level" field is blank. Which level (Standard, Business or Enterprise) is Brackenridge Veterinary Group on? Sections below mark what depends on it.

# Handoff: QB-202861, Brackenridge Veterinary Group (BV-3307), as of 2026-11-05 11:00 UTC

Note: the export holds messages 7 to 12 only. Messages 1 to 6 (2026-11-03 14:20 to 2026-11-04 15:00 UTC) were not supplied.

## 1. Problem as understood
Card payments through the PayCollect integration fail with "PCX-402 token not found" for cards saved before 1 Nov 2026, and the reconnect did not fix it. Cause is not established; a link to the 1 Nov card vault migration is only suspected.

- Reported (Sunil Mehta, 2026-11-04 17:10): every card payment has failed since Monday; saved cards are declined at the front desk. Partly contradicted by logs: 7 payments succeeded.
- Verified (payment logs, James Whitfield, 2026-11-05 09:40): since 2 Nov 14:00 UTC, 38 attempts, 31 failed with PCX-402, 7 succeeded. All 31 failures used cards saved before 1 Nov; all 7 successes used cards saved on or after 1 Nov.
- Verified (retry, James, internal note 2026-11-05 10:20): retry of INV-BV-20931 at 10:12 failed with PCX-402; the PayCollect API says "token not found in vault". The token was created 14 Oct 2026. No charge was made (message 12).
- Verified (integration log, 2026-11-05 10:20): PayCollect was re-authorised on 4 Nov at 14:41 UTC. 14 of the 31 failures are after that, so the reconnect happened and did not fix it.
- Reported (release notes v8.2.3, deployed 1 Nov): "Card vault migrated to PayCollect v3." Link to the failures is not confirmed.
- Open questions: Why are tokens for pre-1 Nov cards missing from the vault (migration defect or other)? Are tokens from before 1 Nov all affected, or only some? What exactly did messages 1 to 6 ask the customer to do? Is the Duty Manager aware (see section 4)?

## 2. Tried so far
- Customer reconnected PayCollect (14:41 UTC 4 Nov, per integration log): failed to fix. Reconnect steps sent in messages 1 to 6 are not visible to us.
- Priya Nair, Tier 1: reviewed/proposed log check (message 7, 2026-11-04 15:40); not completed by her. Inconclusive.
- James Whitfield, Tier 1: payment log analysis (2026-11-05 09:40): worked, produced the pattern above.
- James Whitfield: retry of INV-BV-20931 at 10:12 with customer consent (message 10, 09:55): failed, same error.
- Messages 1 to 6 may hold other attempts; not known.

## 3. Commitments to the customer
- Update by 16:00 UTC on 2026-11-05: James Whitfield, 2026-11-05 10:40 (message 12). Under policy 5.2 Tier 2 now owns this commitment.
- Priya Nair, 2026-11-04 15:40 (message 7): "I'll come back to you tomorrow morning." Soft assurance (time of next update); James replied at 09:40 on 5 Nov.
- Credit: no commitment found in the supplied thread. Sunil claims (2026-11-04 17:10) that Priya said "in your message yesterday" October's fee would be credited. This is unverified (it would sit in messages 1 to 6, not supplied) and policy 6.2/6.3 bar agents from promising credits; only the Customer Success Manager (Callum Reid) or Head of Support may offer one, in writing on the ticket or account record. James told the customer he could not agree credits and had "passed your request to Callum Reid" (09:40); there is no evidence in the thread that Callum has received or answered it. Sunil asked for written confirmation (09:55). Open credits on the account: None recorded.

## 4. Service-level status
- Plan: Quillbill Clinic. Support level: Unknown. The account record field is blank; needed: the level from the account owner or billing system (policy 1.3 takes it from the record only). Policy: Customer Support Policy v4.2.
- Priority: P2, set at creation 2026-11-03 14:20 and unchanged (event log, 11:00 UTC 5 Nov). The customer's "every payment fails" is contradicted by 7 successes, and a workaround may exist for new cards, but priority changes only when an agent records it (2.5); do not change it without a decision.
- Clock start: 2026-11-03 14:20 UTC (4.1). Paused 2026-11-04 09:30 to 15:00 UTC (Pending customer, 5h30m). First response 15:02 on 3 Nov (42 minutes), inside every target.
- Business hours are 08:00 to 18:00 London = UTC in this period (1.1); 3 to 5 Nov are Tue to Thu. Business hours used: 3 Nov 14:20-18:00 = 3h40; 4 Nov 08:00-09:30 and 15:00-18:00 = 4h30; 5 Nov 08:00-11:00 = 3h. Total 11h10m. (I assumed no England bank holiday on those days.)
- Deadline and status by level, because the level is unknown:
  - Business (P2 resolution 20 business hours): 8h50m left; deadline 2026-11-06 09:50 UTC; within target (at risk below 5h).
  - Standard (40 business hours): 28h50m left; deadline 2026-11-10 09:50 UTC; within target (at risk below 10h).
  - Enterprise (24 hours, 24x7, calendar): elapsed 44h40m minus 5h30m paused = 39h10m; breached by 15h10m (deadline was 2026-11-04 19:50 UTC). Policy 5.3 then requires the Support Duty Manager to be told; the thread does not show this was done.
- Escalation: P2 at 11:00 UTC 5 Nov, Tier 2 owns the ticket from then (5.1, 5.2). Customer update cadence for P2: at least once each business day (7.1).

## 5. Recommended next action
Tier 2 (Product Engineering Support) should check the PayCollect v3 vault migration against the failed tokens (e.g. the 14 Oct token on INV-BV-20931) and establish whether pre-1 Nov saved cards are missing from the vault, so a fix or workaround can be set. Reason: the logs correlate failures exactly with cards saved before 1 Nov and the reconnect was verified not to help. Unverified: that the v8.2.3 migration is the cause, how many cards are affected, and which workaround (e.g. re-saving cards) is safe.

In parallel, today:
- Confirm the support level from the account owner; if Enterprise, notify the Support Duty Manager now.
- Send the customer update due by 16:00 UTC today (Tier 2 owns it): say the failures are tied to cards saved before 1 Nov and are with Product Engineering; give the time of the next update. Do not promise a fix date, release date or credit (6.2).
- Ask Callum Reid (CSM) to respond on the October credit in writing on the ticket; tell Sunil the credit decision is Callum's and that it has been routed, only once Callum confirms receipt.
