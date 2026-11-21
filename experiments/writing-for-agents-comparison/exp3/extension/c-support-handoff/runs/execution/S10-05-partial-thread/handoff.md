Clarifying question: The account record for BV-3307 has a blank "Support level" field. Which support level (Standard, Business or Enterprise) does Brackenridge Veterinary Group have? Please also supply messages 1 to 6 of QB-202861 (2026-11-03 14:20 UTC to 2026-11-04 15:00 UTC), which this export omits.

# Escalation handoff: QB-202861 | Brackenridge Veterinary Group Ltd | Saved-card payments failing with PCX-402 since 1 Nov release

**Service level:** Not determined: the support level is blank in the account record, so no resolution deadline can be computed (policy 1.3, 3.1). Tier-independent: first response Met; next customer update owed by 2026-11-05 16:00 UTC (James Whitfield's commitment, now Tier 2's under policy 5.2).

## Problem as currently understood
Since about 2026-11-02 14:00 UTC, card payments on the account fail with "PCX-402 token not found" for cards saved before 1 November, while cards saved on or after 1 November succeed (Verified by James Whitfield from payment logs). The customer's PayCollect reconnect did happen and did not stop the failures (Verified). The leading explanation, untested, is that the v8.2.3 release on 1 November ("Card vault migrated to PayCollect v3") did not carry over older card tokens. The customer's statement that every payment has failed is contradicted by the logs, which show 7 successes.

| Statement | Label | Source (author, timestamp) |
| --- | --- | --- |
| "Every single card payment has failed since Monday." | Reported (contradicted by logs: 7 of 38 succeeded) | Sunil Mehta (customer), 2026-11-04 17:10 UTC, message 8 |
| Clients' saved cards are declined at the front desk when collecting pets. | Reported | Sunil Mehta (customer), 2026-11-04 17:10 UTC, message 8 |
| Since 2 Nov 14:00 UTC: 38 card payment attempts, 31 failed with "PCX-402 token not found", 7 succeeded. | Verified (payment logs) | James Whitfield (Tier 1), 2026-11-05 09:40 UTC, message 9 |
| All 31 failures used cards saved before 1 Nov; all 7 successes used cards saved on or after 1 Nov. | Verified (payment logs) | James Whitfield (Tier 1), 2026-11-05 09:40 UTC, message 9 |
| The card token on INV-BV-20931 was created 14 Oct 2026; PayCollect API response says "token not found in vault". | Verified | James Whitfield (Tier 1), 2026-11-05 10:20 UTC, message 11 (internal) |
| PayCollect connection was re-authorised on 4 Nov at 14:41 UTC; 14 of the 31 failures occurred after that. | Verified (integration log) | James Whitfield (Tier 1), 2026-11-05 10:20 UTC, message 11 (internal) |
| v8.2.3 was deployed 1 Nov with release note "Card vault migrated to PayCollect v3." | Verified (release notes read by support) | James Whitfield (Tier 1), 2026-11-05 10:20 UTC, message 11 (internal) |
| The vault migration in v8.2.3 caused tokens saved before 1 Nov to be missing ("Possible link ... not confirmed"). | Suspected | James Whitfield (Tier 1), 2026-11-05 10:20 UTC, message 11; restated to customer 10:40 UTC, message 12 |
| The fault is "not on our side" (customer's account settings are not the cause). | Suspected (customer's explanation; consistent with logs but not tested) | Sunil Mehta (customer), 2026-11-04 17:10 UTC, message 8 |

## What has been tried
| Action | By | When | Result | Label |
| --- | --- | --- | --- | --- |
| Unknown steps in messages 1 to 6 (including the reconnect instructions Priya sent) | Priya Nair (Tier 1) | 2026-11-03 14:20 to 2026-11-04 15:00 UTC | Not determined: messages 1 to 6 not in the export; James also could not see them (message 11) | Not determined |
| Customer reconnected PayCollect, on Tier 1 advice | Sunil Mehta (customer) | Re-authorisation logged 2026-11-04 14:41 UTC | Failures continued: 14 of 31 failures after the reconnect | Verified (James Whitfield, integration log, 2026-11-05 10:20 UTC) |
| Reviewed payment logs for the account | James Whitfield (Tier 1) | Reported 2026-11-05 09:40 UTC | 31 of 38 attempts failed with PCX-402; failures split by card-save date (before vs on/after 1 Nov) | Verified (James Whitfield, 2026-11-05 09:40 UTC) |
| Retried collection on INV-BV-20931, with customer consent (message 10, 09:55 UTC) | James Whitfield (Tier 1) | 2026-11-05 10:12 UTC | Failed again with "PCX-402 token not found"; API "token not found in vault"; no charge made | Verified (James Whitfield, 2026-11-05 10:20 UTC) |
| Checked release notes for v8.2.3 | James Whitfield (Tier 1) | 2026-11-05 10:20 UTC | Found the 1 Nov card vault migration to PayCollect v3; link to failures not tested | Suspected |

## Commitments to the customer
| Commitment (quoted) | Made by (name, role) | When | Due | Status |
| --- | --- | --- | --- | --- |
| "the next step is for me to look at the payment logs on our side" | Priya Nair, Support Agent (Tier 1) | 2026-11-04 15:40 UTC | No date given | Kept (logs checked by James Whitfield, reported 2026-11-05 09:40 UTC) |
| "I'll come back to you tomorrow morning." | Priya Nair, Support Agent (Tier 1) | 2026-11-04 15:40 UTC | 2026-11-05 morning ("tomorrow morning") | Kept (James Whitfield replied 2026-11-05 09:40 UTC) |
| "I'll update you by 16:00 UTC today." | James Whitfield, Support Agent (Tier 1) | 2026-11-05 10:40 UTC | 2026-11-05 16:00 UTC | Outstanding (Tier 2 now owns it, policy 5.2) |

Claimed by the customer but not found in the thread: Sunil Mehta (message 8, 2026-11-04 17:10 UTC) says Priya Nair promised, "in your message yesterday", that October's subscription fee would be credited. The message he refers to falls in messages 1 to 6, which are not in this export. The account record shows "Open credits: None recorded", and under policy 6.2 and 6.3 a Tier 1 agent may not promise a credit; only Callum Reid (CSM) or the Head of Support may, in writing.

## Service level
- Tier: Unknown: the account record's "Support level" field is blank (plan is "Quillbill Clinic", which the policy does not map to a support level).
- Priority: P2 (recorded at creation 2026-11-03 14:20 UTC and again at escalation 2026-11-05 11:00 UTC).
- First response: clock start 2026-11-03 14:20 UTC (ticket created, policy 4.1); first agent response 2026-11-03 15:02 UTC (42 minutes, within business hours). Met under every support level's P2 target (policy 3.1, 1.4).
- Resolution: clock start 2026-11-03 14:20 UTC; paused 2026-11-04 09:30 to 15:00 UTC while "Pending customer" (policy 4.2, 4.3). Elapsed excluding pause: 11 h 10 min business hours, 39 h 10 min calendar time. Deadline and status Not determined: target depends on the missing support level (policy 3.1).
- Customer updates: P2 requires an update at least once each business day (policy 7.1); next is already committed for 2026-11-05 16:00 UTC.
- Timestamps: all UTC (thread header, policy 1.2); business hours 08:00 to 18:00 Europe/London, equal to UTC in this period (policy 1.1).
- Status as of: 2026-11-05 11:00 UTC (latest timestamp in the thread).

## Recommended next action
Tier 2 (Product Engineering Support) should check whether the token for INV-BV-20931 (created 14 Oct 2026) and other pre-1 Nov tokens for BV-3307 exist in the pre-migration vault but are absent or unmapped in the PayCollect v3 vault after the v8.2.3 migration; this rests on the Verified split of failures by card-save date and the "token not found in vault" response. If the tokens are missing from v3, the migration is the cause and remediation (re-migration or re-mapping) follows; if they are present in v3, the migration theory fails and the PCX-402 lookup path needs investigating instead. Separately, send the customer the update promised for 16:00 UTC today.

## Open questions
- Support level missing: the account record's "Support level" field is blank, so the P2 resolution target, deadline and breach status cannot be set. Request: Callum Reid (CSM) or the account owner to confirm the level. If it is Enterprise, the P2 24-hour calendar target is already exceeded (39 h 10 min elapsed), which would require telling the Support Duty Manager (policy 5.3).
- Messages 1 to 6 missing from the export: needed to see Priya Nair's reconnect instructions, anything else tried, and whether any message promised the October credit. Request: the full ticket export.
- Credit claim unconfirmed: Sunil Mehta says Priya Nair promised an October subscription credit; not found in the available thread, no credit recorded in the account record, and a Tier 1 agent cannot offer one (policy 6.2, 6.3). James Whitfield said he passed the request to Callum Reid (message 9); no reply from Callum Reid is in the thread. Sunil has asked for written confirmation (message 10).
- Priority may need review: if pre-1 Nov card tokens were lost in the vault migration, that may meet the P1 definition "payment data has been lost or corrupted" (policy 2.1), and it affects other customers too, not only this account. Conversely, if re-saving a card works (new cards succeed), that could be a practical workaround pointing to P3 (policy 2.3); untested.
- Scope beyond this account: the suspected cause is a platform release (v8.2.3, 1 Nov), so other customers with pre-1 Nov saved cards may be affected; not checked.
- Failure start time: logs show failures since 2 Nov 14:00 UTC, but the release deployed 1 Nov; whether any payments ran between deployment and 2 Nov 14:00 is not stated.
