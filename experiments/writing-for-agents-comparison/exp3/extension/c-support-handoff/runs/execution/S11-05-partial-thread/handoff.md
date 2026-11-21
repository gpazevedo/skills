Clarifying question: The account record for BV-3307 has an empty "Support level" field, and the thread export omits messages 1 to 6. Can you supply the customer's support level (Standard, Business or Enterprise) and the full text of messages 1 to 6?

# Escalation handoff: QB-202861: Card payments with cards saved before 1 Nov 2026 fail with "PCX-402 token not found"

**Customer:** Brackenridge Veterinary Group Ltd (BV-3307), Quillbill Clinic plan, support level not recorded · **Priority:** P2 · **Next deadline:** 2026-11-05 16:00 UTC, customer update promised by James Whitfield, outstanding, 5h left (as of 2026-11-05 11:00 UTC, the last event in the supplied export). SLA resolution deadline: cannot determine (support level not recorded).

## Problem as currently understood
Since 2 November 2026 about 14:00 UTC, card payments on the customer's account fail with "PCX-402 token not found" when the saved card was stored before 1 November; cards saved on or after 1 November succeed. The customer's front desks at their practices cannot take payment from clients' saved cards. Reconnecting PayCollect on 4 November did not stop the failures. The leading explanation, not confirmed, is that the v8.2.3 card vault migration to PayCollect v3 (deployed 1 November) did not carry over tokens saved before it.

Evidence:
- [Verified] 38 card payment attempts since 2 Nov 14:00 UTC: 31 failed with "PCX-402 token not found", 7 succeeded (James Whitfield, message 9, 2026-11-05 09:40 UTC, from payment logs)
- [Verified] All 31 failures used cards saved before 1 Nov; all 7 successes used cards saved on or after 1 Nov (James Whitfield, message 9, 2026-11-05 09:40 UTC)
- [Verified] Retry of INV-BV-20931 at 10:12 UTC on 5 Nov failed with "PCX-402 token not found"; that invoice's card token was created 14 Oct 2026; PayCollect API response: "token not found in vault"; no charge made (James Whitfield, internal note message 11, 2026-11-05 10:20 UTC; message 12, 10:40 UTC)
- [Verified] PayCollect connection was re-authorised on 4 Nov at 14:41 UTC; 14 of the 31 failures occurred after that (James Whitfield, internal note message 11, 2026-11-05 10:20 UTC, from integration log)
- [Verified] v8.2.3 release notes (deployed 1 Nov): "Card vault migrated to PayCollect v3." (James Whitfield, internal note message 11, 2026-11-05 10:20 UTC; link to the failures noted as "not confirmed")
- [Reported] "Every single card payment has failed since Monday" and saved cards are declined at the desk when clients collect pets (Sunil Mehta, message 8, 2026-11-04 17:10 UTC); the logs contradict "every single": 7 of 38 succeeded
- [Reported] Customer reconnected PayCollect as instructed in an earlier support message (Sunil Mehta, message 8, 2026-11-04 17:10 UTC); the reconnect itself is confirmed by the integration log above
- [Inferred] The failures are caused by pre-1 Nov tokens missing from the PayCollect v3 vault after the v8.2.3 migration, not by customer settings (rests on: 1 Nov cut-off splitting all failures from all successes, "token not found in vault" response, migration in v8.2.3 deployed 1 Nov, failures continuing after the reconnect)
- [Inferred] The issue may affect other customers with cards saved before 1 Nov (rests on: the cut-off matches a platform release, not anything specific to this account)

## Tried so far
| When | Who | Action | Result |
|---|---|---|---|
| 2026-11-03 to 2026-11-04 (messages 1 to 6) | Priya Nair / customer | Unknown troubleshooting; messages not in export | No result recorded in the supplied material |
| Before 2026-11-04 15:40 UTC (per messages 7 and 8) | Customer, on Priya Nair's instructions | Reconnected PayCollect | Re-authorised 2026-11-04 14:41 UTC; failures continued (14 after it). Rules out a stale connection as the cause |
| 2026-11-05 09:40 UTC | James Whitfield | Reviewed payment logs | 31 of 38 failed, all with cards saved before 1 Nov |
| 2026-11-05 09:40 UTC | James Whitfield | Passed October credit request to CSM Callum Reid | No result recorded |
| 2026-11-05 10:12 UTC | James Whitfield | Retried collection on INV-BV-20931 (customer approved, message 10) | Failed, "PCX-402 token not found" / "token not found in vault"; token created 14 Oct |
| 2026-11-05 10:20 UTC | James Whitfield | Checked integration log and v8.2.3 release notes | Reconnect confirmed; vault migration to PayCollect v3 on 1 Nov found, link not confirmed |
| 2026-11-05 11:00 UTC | James Whitfield | Escalated to Tier 2 | Status Escalated, P2 |

## Commitments to the customer
| Commitment (quoted) | Made by | When | Status |
|---|---|---|---|
| "the next step is for me to look at the payment logs on our side. I'll come back to you tomorrow morning." (tomorrow morning = 2026-11-05 morning, Inferred) | Priya Nair | 2026-11-04 15:40 UTC (message 7) | Met: James Whitfield checked the logs and replied 2026-11-05 09:40 UTC |
| "I'm escalating this to our Product Engineering Support team now." | James Whitfield | 2026-11-05 10:40 UTC (message 12) | Met: escalated 2026-11-05 11:00 UTC |
| "I'll update you by 16:00 UTC today." (= 2026-11-05 16:00 UTC) | James Whitfield | 2026-11-05 10:40 UTC (message 12) | Outstanding, 5h left as of 11:00 UTC. Tier 2 now owns it (policy 5.2) |

Claimed by the customer, not found in the thread:
- Credit of October's subscription fee, "as you said in your message yesterday" (Sunil Mehta, message 8, 2026-11-04 17:10 UTC). The referenced message would be among messages 1 to 6, which are not in the export. Policy 6.2 forbids support agents promising credits; 6.3 makes an offer valid only from the CSM or Head of Support and only when recorded in writing; the account record shows "Open credits: None recorded". James Whitfield did not agree it and passed it to Callum Reid (message 9). Customer asked for written confirmation (message 10).

## Service level
- Plan: Quillbill Clinic [Verified] (account record, Plan field)
- Support level: cannot determine: the account record's "Support level" field is empty, and policy 1.3 takes the level only from the account record [Verified] (account record, Support level field)
- Priority: P2 [Verified] (ticket event, created 2026-11-03 14:20 UTC; reconfirmed at escalation 2026-11-05 11:00 UTC). Fits policy 2.2: "payment collection ... does not work and there is no practical workaround" [Inferred] (rests on: pre-1 Nov saved cards fail; no workaround in the thread)
- Target: cannot determine: policy 3.1 sets P2 targets per support level ("Enterprise | P2 | 2 hours, 24x7 | 24 hours, 24x7"; "Business | P2 | 4 business hours | 20 business hours"; "Standard | P2 | 8 business hours | 40 business hours"), and the level is not recorded
- Clock start: 2026-11-03 14:20 UTC, ticket created [Verified] (ticket event; policy 4.1 "The clock starts when the ticket is created"). Europe/London = UTC in this period (policy 1.1)
- Pause: 2026-11-04 09:30 to 15:00 UTC, Pending customer, 5h30m [Verified] (ticket events; policy 4.2)
- Elapsed as of 2026-11-05 11:00 UTC: 11h10m business hours; 39h10m calendar hours excluding the pause [Inferred] (rests on: clock start, pause, business hours 08:00 to 18:00 Mon to Fri per policy 1.1)
- First response: 2026-11-03 15:02 UTC, 42 business minutes after creation [Verified] (ticket event); met under every P2 level [Inferred] (rests on: 42 min against 2h / 4bh / 8bh)
- Resolution deadline and status: cannot determine: support level not recorded

## Recommended next action
Tier 2 engineer: before 2026-11-05 16:00 UTC, confirm whether pre-1 Nov card tokens for BV-3307 exist in the PayCollect v3 vault after the v8.2.3 migration, starting with the 14 Oct token on INV-BV-20931. This is the unverified link the whole diagnosis rests on, and the result is what the 16:00 update needs to say.

Follow-ups:
1. Tier 2 owner: send the customer update promised for 16:00 UTC on 2026-11-05 (policy 5.2), without any credit or fix-date promise (policy 6.2).
2. Tier 2 owner: get the support level confirmed (account owner or CSM Callum Reid) today; if Enterprise, the resolution target has already passed and the Support Duty Manager must be told (policy 5.3).

## Gaps and open questions
- Support level missing from the account record; SLA targets, resolution deadline and breach status cannot be set. If it is Enterprise, the 24-hour calendar target would already be passed.
- Messages 1 to 6 (2026-11-03 14:20 to 2026-11-04 15:00 UTC) are not in the export: what Priya Nair tried, what reconnect steps she sent, and whether she wrote anything about a credit.
- October credit: customer claims a support promise; not visible in the thread, not recorded in the account record, and outside agent authority under policy 6.2 and 6.3. Awaiting Callum Reid.
- The vault-migration explanation is unconfirmed (James Whitfield, message 11).
- Unknown whether other customers with pre-1 Nov saved cards are affected.
- Statuses are as of 2026-11-05 11:00 UTC, the last event in the export; recheck the 16:00 UTC commitment and the SLA against the current time.
