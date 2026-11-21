# Escalation handoff: QB-202861 | Brackenridge Veterinary Group Ltd | Card payments fail with PCX-402 for older saved cards

**Service level:** Next dated item: 16:00 UTC on 2026-11-05, the customer update James Whitfield promised (a commitment, not a policy target) | Pending, 5 hours remaining at 11:00 UTC. Policy resolution and first-response targets: Not determined: the account record leaves "Support level" blank, so the tier is unknown.

## Problem as currently understood
Card payments using saved cards fail with "PCX-402 token not found". Support's log check (Verified) shows 31 of 38 attempts since 2 Nov 14:00 UTC failed, all on cards saved before 1 Nov, while all 7 successes used cards saved on or after 1 Nov. A retry on INV-BV-20931 failed the same way, and failures continue after the customer's reconnect of PayCollect (Verified). The likely cause is the v8.2.3 card vault migration to PayCollect v3 deployed 1 Nov, but that is Suspected and untested. Messages 1 to 6 are not in this export.

| Statement | Label | Source (author, timestamp) |
| --- | --- | --- |
| 38 card payment attempts since 2 Nov 14:00 UTC; 31 failed with "PCX-402 token not found", 7 succeeded | Verified | James Whitfield, payment logs, msg 9, 2026-11-05 09:40 |
| All 31 failures used cards saved before 1 Nov; all 7 successes used cards saved on or after 1 Nov | Verified | James Whitfield, payment logs, msg 9, 2026-11-05 09:40 |
| Retry of INV-BV-20931 failed at 10:12 with "PCX-402 token not found"; PayCollect API says "token not found in vault"; the token was created 14 Oct 2026 | Verified | James Whitfield, internal note msg 11, 2026-11-05 10:20 |
| PayCollect connection was re-authorised 4 Nov 14:41 UTC; 14 of the 31 failures occurred after that | Verified | James Whitfield, integration log, msg 11, 2026-11-05 10:20 |
| "Every single card payment has failed since Monday" | Reported (partly contradicted: 7 attempts succeeded per the logs) | Sunil Mehta, msg 8, 2026-11-04 17:10 |
| Clients' saved cards are declined at the front desk | Reported | Sunil Mehta, msg 8, 2026-11-04 17:10 |
| The customer's settings are not the cause ("this is not on our side") | Reported; the reconnect itself is Verified, and the continuing failures after it support the claim | Sunil Mehta, msg 8, 2026-11-04 17:10 |
| v8.2.3 (deployed 1 Nov), "Card vault migrated to PayCollect v3", may be linked to tokens saved before 1 Nov | Suspected | James Whitfield, msg 11, 2026-11-05 10:20 (release notes quoted; "not confirmed") |
| "A problem on our side with older saved cards rather than with your settings" | Suspected | James Whitfield, msg 12, 2026-11-05 10:40 |

## What has been tried
| Action | By | When | Result | Label |
| --- | --- | --- | --- | --- |
| Reconnect PayCollect (steps sent by Priya Nair in messages 1 to 6, not visible here) | Customer (Sunil Mehta) | Re-authorised 2026-11-04 14:41 | Did not help; failures continue after 14:41 | Verified (re-authorisation in integration log; failures in payment logs) |
| Check payment logs on the Quillbill side | James Whitfield (Priya Nair had said she would, msg 7) | 2026-11-05 09:40 | Found the pre-1-Nov saved-card pattern | Verified |
| Retry collection on INV-BV-20931, with customer consent (msg 10, 09:55) | James Whitfield | 2026-11-05 10:12 | Failed again, PCX-402; no charge made | Verified |
| Other steps from messages 1 to 6 | Unknown | 2026-11-03 14:20 to 2026-11-04 15:00 | Unknown: messages not in export. The customer says they "did exactly what your earlier message said" | Reported |
| Pass the credit request to Callum Reid (Customer Success Manager) | James Whitfield | 2026-11-05 09:40 | No record of it on the ticket or the account record | Reported (stated by James, msg 9) |

## Commitments to the customer
| Commitment (quoted) | Made by (name, role) | When | Due | Status |
| --- | --- | --- | --- | --- |
| "I'll come back to you tomorrow morning." | Priya Nair, Support Agent Tier 1 | 2026-11-04 15:40 | "tomorrow morning" = morning of 2026-11-05 (no time given) | Kept: James Whitfield replied at 09:40 on 2026-11-05 with the log findings |
| "I'd like to retry the collection on one failed invoice, INV-BV-20931 ... May I go ahead?" (offer to act, made contingent on consent) | James Whitfield, Support Agent Tier 1 | 2026-11-05 09:40 | No date given | Kept: retried at 10:12 after consent |
| "I've passed your request to Callum Reid." | James Whitfield, Support Agent Tier 1 | 2026-11-05 09:40 | No date given | Outstanding: no written reply on the ticket; the customer has asked for written confirmation (msg 10) |
| "I'm escalating this to our Product Engineering Support team now." | James Whitfield, Support Agent Tier 1 | 2026-11-05 10:40 | No date given | Kept: escalated at 11:00 |
| "I'll update you by 16:00 UTC today." | James Whitfield, Support Agent Tier 1 | 2026-11-05 10:40 | 2026-11-05 16:00 UTC | Outstanding. Under policy 5.2 Tier 2 now owns it |

Claimed by the customer but not found in the thread: that Priya said, in a message on 3 Nov ("yesterday"), that October's subscription fee would be credited (msg 8, "as you said in your message yesterday, we'll be expecting October's subscription fee to be credited"). Messages 1 to 6 are not in the export, so the claim cannot be checked here. Nothing in messages 7 to 12 offers a credit, and James said he cannot agree credits.

## Service level
- Tier: Unknown: no account record value ("Support level:" is blank; the plan name "Quillbill Clinic" is not one of Standard, Business or Enterprise under policy 1.3)
- Priority: P2, recorded on the ticket at creation (2026-11-03 14:20) and at escalation (2026-11-05 11:00)
- First response (policy 3.1): Not determined: tier unknown. Clock starts at ticket creation, 2026-11-03 14:20 UTC (policy 4.1). The first agent response was sent at 15:02 UTC, 42 minutes later.
- Resolution (policy 3.1, 4.4): Not determined: tier unknown. Policy 3.1 sets P2 at 40 business hours (Standard), 20 business hours (Business) or 24 hours on calendar time (Enterprise), all counted from 2026-11-03 14:20 UTC. No deadline or status is given, because each depends on the tier.
- Clock pause (policy 4.2, 4.3): "Pending customer" from 2026-11-04 09:30 to 15:00 UTC, 5 hours 30 minutes excluded.
- Elapsed time at the as-of time, for use once the tier is known: 11 hours 10 minutes of business hours (08:00 to 18:00 London time, which equals UTC in this period; policy 1.1) and 39 hours 10 minutes of calendar time, both with the pause excluded. This assumes no bank holiday between 3 and 5 Nov.
- Customer updates (policy 7.1, P2): at least once each business day. 5 Nov is covered by the 09:40 message. The next is due by end of the business day on 6 Nov.
- Duty Manager (policy 5.3): required only if the P2 ticket is breached, which cannot be determined until the tier is known.
- Status as of: 2026-11-05 11:00 UTC (the export's stated as-of time). All thread timestamps are UTC.

## Recommended next action
Tier 2 Product Engineering Support should check whether tokens saved before the v8.2.3 vault migration (such as the 14 Oct token on INV-BV-20931) exist in the PayCollect v3 vault, to test the migration hypothesis. This rests on the Verified saved-before-1-Nov pattern and the vault error. If the tokens are missing, the plan becomes finding how to restore or migrate them. If they are present, look for another cause. Either way, send the customer an update by 16:00 UTC.

## Open questions
- Support level is blank in the account record, so every tier-dependent target is blocked, including first response, resolution and breach status. Request: the account record's support level from the Customer Success Manager or account admin. No tier was inferred from the plan name.
- Messages 1 to 6 are missing from the export. Request: the full ticket, to confirm what reconnect steps Priya sent and whether any credit was mentioned on 3 Nov.
- Credit: Sunil asks for October's subscription fee to be credited and wants confirmation in writing "not passed around". Under policy 6.2 and 6.3 only Callum Reid (the CSM named in the account record) or the Head of Support may offer one, and only in writing on the ticket or account record. None is recorded. Request: Callum Reid to respond to the customer, and Tier 2 must not promise a credit, fix date or release date (policy 6.2).
- Conflict: the customer says every card payment failed; the logs show 7 of 38 succeeded, all with cards saved on or after 1 Nov.
- Whether a practical workaround exists (for example re-saving cards, which is untested) matters for P2 versus P3 under policy 2.2 and 2.3. The priority is P2 as recorded. Only an agent recording a change would alter it.
- The customer says they did exactly what the earlier message asked; this is Reported only, but the 4 Nov 14:41 re-authorisation in the integration log supports it.
- Bank holidays in England between 3 and 5 Nov were not checked against any supplied calendar.
