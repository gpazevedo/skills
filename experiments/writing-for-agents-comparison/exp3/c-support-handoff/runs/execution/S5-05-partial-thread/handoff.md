Clarifying question: The account record's "Support level" field is blank. Which support level (Standard, Business or Enterprise) does Brackenridge Veterinary Group (BV-3307) have, and can you supply messages 1 to 6 of QB-202861 and any ticket events after 2026-11-05 11:00 UTC?

## Escalation handoff: QB-202861 Saved-card payments failing with "PCX-402 token not found"
As of: 2026-11-21 15:34 UTC (Saturday; Europe/London is GMT = UTC)
Customer: Brackenridge Veterinary Group Ltd (BV-3307), plan Quillbill Clinic, support level not recorded; Quillbill Invoicing (cloud), PayCollect card payments integration (saved cards, desk payments), Clinic front-desk add-on (4 practices); data region UK. Primary contact Sunil Mehta (Practice Operations Manager); CSM Callum Reid (account record)

### Problem as currently understood
Card payments using cards saved before 1 November fail with "PCX-402 token not found"; cards saved on or after 1 November succeed. Reconnecting PayCollect did not help. The leading explanation from support is that the v8.2.3 card vault migration to PayCollect v3 (deployed 1 Nov) did not carry over older tokens; the pattern fits, but the causal link is not confirmed (low to moderate confidence).
Evidence:
- [Verified] Since 2026-11-02 14:00 UTC, 38 card attempts: 31 failed with "PCX-402 token not found", 7 succeeded (James Whitfield, payment logs, 5 Nov 09:40)
- [Verified] All 31 failures used cards saved before 1 Nov; all 7 successes used cards saved on or after 1 Nov (James Whitfield, payment logs, 5 Nov 09:40)
- [Verified] PayCollect API response on retry: "token not found in vault"; that token was created 14 Oct 2026 (James Whitfield, internal note, 5 Nov 10:20)
- [Verified] v8.2.3 release notes, deployed 1 Nov: "Card vault migrated to PayCollect v3." Link to the failures not confirmed (James Whitfield, internal note, 5 Nov 10:20)
- [Reported] "Every single card payment has failed since Monday" (Sunil Mehta, 4 Nov 17:10). Contradicted in part by the logs: 7 of 38 succeeded
- [Reported] Saved cards declined at the desk when clients collect pets; problem "not on our side" (Sunil Mehta, 4 Nov 17:10)

### Tried so far
- Before 2026-11-04 14:41 UTC, customer, on Priya Nair's earlier instructions: reconnected PayCollect → failures continued. [Verified] re-authorisation at 14:41 on 4 Nov and 14 of the 31 failures after it (James Whitfield, integration log, 5 Nov 10:20). Which reconnect steps were sent is not visible (messages 1 to 6).
- 2026-11-05 James Whitfield (Tier 1): checked payment logs → failure pattern above [Verified]
- 2026-11-05 10:12 UTC James Whitfield, with customer consent (message 10): retried collection on INV-BV-20931 → failed again, "PCX-402 token not found", no charge made [Verified]
- Anything else tried in messages 1 to 6: not visible in this export.

### Commitments to the customer
- Look at the payment logs and "come back to you tomorrow morning" | made by Priya Nair, Support Agent Tier 1, on 2026-11-04 15:40 UTC | due 2026-11-05 morning (no exact time) | met (James Whitfield replied with log results 5 Nov 09:40)
- "I'll update you by 16:00 UTC today" | made by James Whitfield, Support Agent Tier 1, on 2026-11-05 10:40 UTC | due 2026-11-05 16:00 UTC | missed as far as the supplied thread shows (no update recorded; export ends 5 Nov 11:00). Tier 2 now owns this commitment (policy 5.2)

### Service level
- Priority P2 under policy 2.2 ("payment collection ... does not work and there is no practical workaround"); plan Quillbill Clinic; support level not recorded, so the applicable targets are not computable (policy 1.3: support level is "the level recorded in the customer's account record"). P2 fits the verified evidence; if re-saving a card proves to be a practical workaround, policy 2.3 would make it P3.
- First response: sent 2026-11-03 15:02, 42 minutes after creation at 14:20 (policy 1.4, 4.1) | met at every support level (shortest P2 target is 2 hours, Enterprise)
- Resolution: not computable without the support level. For reference, the P2 target has passed at every level (clock from creation, policy 4.1; paused 4 Nov 09:30 to 15:00, policy 4.2; business hours 08:00 to 18:00 UTC, policy 1.1, 3.3):
  - Enterprise, "24 hours, 24x7": 3 Nov 14:20 + 24h + 5h30 paused = 5 Nov 19:50 UTC | would be breached by 15d 19h44m
  - Business, "20 business hours": 3 Nov 3h40 + 4 Nov 4h30 + 5 Nov 10h = 18h10, + 1h50 on 6 Nov = 6 Nov 09:50 UTC | would be breached by 108h10 business hours
  - Standard, "40 business hours": 18h10 by 5 Nov + 6 Nov 10h + 9 Nov 10h = 38h10, + 1h50 = 10 Nov 09:50 UTC | would be breached by 88h10 business hours
- Customer updates, P2 "at least once each business day" (policy 7.1): no update recorded after 5 Nov 10:40 | missed as far as the thread shows; next business day starts Mon 23 Nov 08:00 UTC

### Recommended next action
The Tier 2 ticket owner should check the full ticket for anything after 5 Nov 11:00 and, if nothing was sent, update Sunil Mehta now (no later than Mon 23 Nov 08:00 UTC), because James Whitfield's 16:00 UTC 5 Nov update and the daily P2 updates appear missed and Tier 2 owns those commitments (policy 5.2, 7.1).
Then: tell the Support Duty Manager the P2 is breached (policy 5.3; breached at any support level). Verify the leading explanation by checking whether the 14 Oct token on INV-BV-20931, and other pre-1 Nov tokens for BV-3307, exist in the PayCollect v3 vault after the v8.2.3 migration.

### Gaps
- Account record "Support level" field is blank: resolution target and SLA status not computable until it is supplied.
- Messages 1 to 6 (3 Nov 14:20 to 4 Nov 15:00) not supplied: earlier troubleshooting, Priya Nair's reconnect instructions and any earlier commitments are not visible.
- Thread export ends 2026-11-05 11:00 UTC; the as-of time is 21 Nov. SLA and commitment statuses assume no later status changes, updates or resolution. Policy is silent on whether "Escalated" status pauses the clock; read as not paused (policy 4.2 pauses only for "Pending customer").
- [Reported] commitment, not found in thread: October subscription fee credit, which Sunil Mehta says Priya Nair promised "in your message yesterday" (4 Nov 17:10). Not in the supplied messages; agents may not promise credits (policy 6.2) and only CSM Callum Reid or the Head of Support may offer one, recorded in writing (6.3). Account record shows "Open credits: None recorded". James Whitfield passed the request to Callum Reid (5 Nov 09:40); the customer wants written confirmation. No outcome recorded.
- Leading explanation (v8.2.3 vault migration) is unconfirmed; whether other customers with pre-1 Nov tokens are affected is unknown.
- Workaround not tested: whether re-saving a customer's card restores payment. This bears on priority (P2 vs P3).
