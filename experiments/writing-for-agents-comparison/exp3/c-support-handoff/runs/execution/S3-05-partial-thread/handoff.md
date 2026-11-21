# Escalation handoff: QB-202861, Brackenridge Veterinary Group Ltd

**Service level:** Undetermined (the account record's "Support level" field is blank), deadline Undetermined; P2 resolution target is 24 hours 24x7 (Enterprise), 20 business hours (Business) or 40 business hours (Standard) under policy 3.1. If Enterprise, already breached at 2026-11-04 19:50 UTC; if Business, within target, due 2026-11-06 09:50 UTC; if Standard, within target, due 2026-11-10 09:50 UTC.
**Next action:** Check the v8.2.3 card vault migration (PayCollect v3) for account BV-3307 and establish whether card tokens saved before 1 November were migrated, and whether they can be recovered; send the customer an update by 16:00 UTC on 5 Nov.

## Problem as currently understood
Saved-card payments fail with "PCX-402 token not found" only for cards saved before 1 November 2026. Cards saved on or after 1 November work. The likely cause is on Quillbill's side: possibly the card vault migration to PayCollect v3 in release v8.2.3 (deployed 1 Nov), but this is not confirmed. This narrows the customer's report ("every single card payment has failed since Monday", which they believe is not on their side after reconnecting): log evidence shows that only pre-1-November saved cards fail, and that the reconnect did take place but did not help.

Evidence:
- [Verified] Since 2 Nov 14:00 UTC, 38 card payment attempts on the account: 31 failed with "PCX-402 token not found", 7 succeeded (James Whitfield, Tier 1, payment logs, 2026-11-05 09:40 UTC, message 9)
- [Verified] All 31 failures used cards saved before 1 Nov; all 7 successes used cards saved on or after 1 Nov (James Whitfield, payment logs, 2026-11-05 09:40 UTC, message 9)
- [Verified] Retry of collection on INV-BV-20931 at 10:12 UTC failed again with "PCX-402 token not found". PayCollect API response: "token not found in vault". The card token on that invoice was created 14 Oct 2026. No charge was made (James Whitfield, retry plus API response, 2026-11-05 10:20 UTC, message 11 internal note; no-charge stated to customer in message 12)
- [Verified] PayCollect connection was re-authorised on 4 Nov at 14:41 UTC; 14 of the 31 failures happened after that (James Whitfield, integration log, 2026-11-05 10:20 UTC, message 11)
- [Verified] Release v8.2.3 (deployed 1 Nov) release notes: "Card vault migrated to PayCollect v3." The link to pre-1-Nov tokens is a hypothesis, not confirmed (James Whitfield, release notes, 2026-11-05 10:20 UTC, message 11)
- [Reported] "every single card payment has failed since Monday" (2 Nov); saved cards declined at the front desk when clients collect pets (Sunil Mehta, 2026-11-04 17:10 UTC, message 8)
- [Reported] Customer reconnected PayCollect as support's earlier message instructed (Sunil Mehta, 2026-11-04 17:10 UTC, message 8); confirmed by the integration log above
- Conflict: the customer reports that every card payment has failed; logs show 7 of 38 attempts succeeded (all with cards saved on or after 1 Nov). The failure is limited to older saved cards, not total.
- Gap: messages 1 to 6 (2026-11-03 14:20 UTC to 2026-11-04 15:00 UTC) are not in the export. The original report, the reconnect steps Priya sent and anything else tried are not visible (James Whitfield, 2026-11-05 10:20 UTC, message 11).

## Tried so far
- Between 2026-11-03 15:02 and 2026-11-04 15:00 UTC (messages 1 to 6, not in export), Priya Nair: asked the customer to reconnect PayCollect -> customer reconnected; failures continued (customer, message 8; Priya, message 7, "sorry the reconnect didn't help"; reconnect verified by integration log at 2026-11-04 14:41 UTC). Any other steps in messages 1 to 6: not recorded in this export.
- 2026-11-04 14:41 UTC, Sunil Mehta: re-authorised the PayCollect connection -> failures continued (14 of 31 failures after this time)
- 2026-11-05 09:40 UTC, James Whitfield: reviewed payment logs since 2 Nov -> 31 of 38 failed, all with cards saved before 1 Nov
- 2026-11-05 10:12 UTC, James Whitfield: retried collection on INV-BV-20931 with the customer's consent (message 10) -> failed, "PCX-402 token not found" / "token not found in vault"; no charge
- 2026-11-05 10:20 UTC, James Whitfield: checked the integration log and v8.2.3 release notes -> reconnect confirmed; possible link to vault migration, not confirmed
- 2026-11-05 09:40 UTC, James Whitfield: passed the customer's October credit request to Callum Reid (CSM) -> result not recorded

## Commitments to the customer
- "I'll come back to you tomorrow morning." (Priya Nair, 2026-11-04 15:40 UTC, message 7), due morning of 5 Nov, met (James Whitfield replied at 2026-11-05 09:40 UTC after reassignment)
- "the next step is for me to look at the payment logs on our side" (Priya Nair, 2026-11-04 15:40 UTC, message 7), no due time given, met (logs checked by James Whitfield, 2026-11-05 09:40 UTC)
- "I've passed your request to Callum Reid." (James Whitfield, 2026-11-05 09:40 UTC, message 9), no due time, met as stated; no reply from Callum Reid in the thread
- "I'm escalating this to our Product Engineering Support team now." (James Whitfield, 2026-11-05 10:40 UTC, message 12), due now, met (escalated to Tier 2 at 2026-11-05 11:00 UTC)
- "I'll update you by 16:00 UTC today." (James Whitfield, 2026-11-05 10:40 UTC, message 12), due 16:00 UTC 5 Nov, open. Tier 2 now owns it (policy 5.2: "From escalation, Tier 2 owns the ticket, including customer updates and any commitments already made to the customer.")
- [Reported, unconfirmed] October's subscription fee to be credited: "as you said in your message yesterday, we'll be expecting October's subscription fee to be credited for all this" (Sunil Mehta, 2026-11-04 17:10 UTC, message 8, attributing it to Priya Nair on 3 Nov). The message it refers to is in messages 1 to 6, not in this export, so it cannot be checked. Against it: the account record shows "Open credits: None recorded"; policy 6.2 says agents "must not promise ... a service credit or a refund"; policy 6.3 says only the CSM named in the account record (Callum Reid) or the Head of Support may offer one, and "An offer is valid only when it is recorded in writing on the ticket or in the account record." The customer asked for written confirmation (message 10). Due: no time stated; open.

## Service level
- Plan: Quillbill Clinic (account record). Support level: blank in the account record. Policy 1.3: "A customer's support level (Standard, Business or Enterprise) is the level recorded in the customer's account record." Support level is **Undetermined**: the plan name does not map to a level in the policy.
- Priority: P2 (set at ticket creation 2026-11-03 14:20 UTC, confirmed at escalation 2026-11-05 11:00 UTC). Policy 2.2: "P2 (High): a major function, such as invoice sending, payment collection or bank feeds, does not work and there is no practical workaround." Possible mismatch: if the pre-1-November tokens were lost in the vault migration, policy 2.1 may apply: "P1 (Critical): ... invoice or payment data has been lost or corrupted." If re-saving cards turns out to be a practical workaround, 2.3 (P3) may apply instead. Neither is established yet.
- Target: policy 3.1, P2 rows: "Enterprise | P2 | 2 hours, 24x7 | 24 hours, 24x7"; "Business | P2 | 4 business hours | 20 business hours"; "Standard | P2 | 8 business hours | 40 business hours". The first response was at 2026-11-03 15:02 UTC (42 minutes), which meets every level.
- Clock: started at ticket creation, 2026-11-03 14:20 UTC (policy 4.1: "The clock starts when the ticket is created."). Paused 2026-11-04 09:30 to 15:00 UTC while "Pending customer" (policy 4.2), 5 h 30 m. Business hours are "08:00 to 18:00 Europe/London time, Monday to Friday, excluding bank holidays in England", and Europe/London is GMT = UTC after 25 Oct 2026 (policy 1.1). "24x7" targets run on calendar time (policy 3.3). No bank holidays in England fall between 3 and 10 Nov 2026.
- Elapsed as of now: 11 h 10 m business hours (3 Nov 14:20 to 18:00 = 3 h 40 m; 4 Nov 08:00 to 09:30 = 1 h 30 m and 15:00 to 18:00 = 3 h; 5 Nov 08:00 to 11:00 = 3 h). Calendar time, excluding the pause: 39 h 10 m.
- Deadline: **Undetermined** (support level missing), as of now = 2026-11-05 11:00 UTC (latest timestamp in the thread, the escalation event; no "now" given by the user). By support level, applying policy 4.5 ("at risk" if less than 25% of the resolution target remains):
  - Enterprise: deadline 2026-11-04 19:50 UTC, **breached** (by 15 h 10 m calendar time)
  - Business: deadline 2026-11-06 09:50 UTC; 8 h 50 m of 20 business hours remain; **within target** (at-risk threshold is 5 h remaining, reached at 2026-11-05 14:50 UTC)
  - Standard: deadline 2026-11-10 09:50 UTC; 28 h 50 m of 40 business hours remain; **within target**
- If the ticket is re-prioritised to P1, policy 4.4 recounts the resolution target from creation: Enterprise (8 h) and Business (12 h 24x7) would already be breached; Standard (20 business hours) would be due 2026-11-06 09:50 UTC.

## Recommended next action
Check the v8.2.3 card vault migration for account BV-3307: look up the INV-BV-20931 token (created 14 Oct 2026) in the pre-migration vault and in PayCollect v3, and establish whether pre-1-November tokens were not migrated, were mis-mapped, or are lost. This is the most decisive open question. It turns the release-note hypothesis into a verified cause, says whether a fix (re-migrating or re-mapping tokens) is possible or whether clients must re-save cards, and decides whether the ticket meets P1 ("payment data has been lost or corrupted", policy 2.1), which would change the deadline and trigger Duty Manager notification (policy 5.3). Before 16:00 UTC today, send the customer the update James committed to, even if the investigation is not finished.

Open questions:
- Which support level (Standard, Business or Enterprise) does BV-3307 have? The account record field is blank; ask Callum Reid (CSM) or account administration. If Enterprise, the P2 ticket is already breached and the Support Duty Manager must be told (policy 5.3).
- Were pre-1-November card tokens migrated to PayCollect v3, and can they be recovered? Is this affecting other accounts migrated in v8.2.3?
- Is re-saving a card a practical workaround in the meantime (cards saved on or after 1 Nov succeed)? This affects the priority (P2 vs P3) and what to tell the front desks.
- What do messages 1 to 6 contain: the original report, the reconnect steps given, and whether Priya Nair wrote anything about an October credit?
- Has Callum Reid responded to the credit request? Only he or the Head of Support can make an offer, in writing on the ticket or account record (policy 6.3). No agent should confirm a credit.

Next customer update due: 2026-11-05 16:00 UTC (James Whitfield's commitment in message 12, now owned by Tier 2 under policy 5.2); after that, at least once each business day for P2 (policy 7.1: "P2 tickets: an update at least once each business day.").
