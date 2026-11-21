# Handoff: QB-204518, Harrow & Finch Accounting Ltd (HF-0192)

To: Tier 2 (Product Engineering Support). As of escalation, Thu 12 Nov 2026 11:30 UTC. All times UTC.

## Problem

Recurring invoices are generated but never sent. The 07:00 run on 12 Nov created 112 invoices. All are "Queued - not dispatched", with 0 send attempts and no errors. All 112 come from schedules created before the v8.3 release (10 Nov). This looks like known issue KI-3381 (Investigating, opened 11 Nov), but that is not confirmed. The customer has 340 schedules. Upcoming runs: Fri 13 Nov 07:00 (64 invoices) and Sun 15 Nov (90 invoices). Payment terms run from the send date, so each delay pushes back the customer's collections. Contact: Daniel Okafor, Finance Systems Lead.

## Tried

- Manual send of INV-2026-11-0457 (customer approved): the recipient's mail server accepted it at 10:16.
- Re-saved the "Meadowgate monthly retainer" schedule without changes, then ran "Run now (test mode)": dispatched within 40 seconds. Not yet seen on a real scheduled run.
- No comparison yet with the account's 3 post-v8.3 schedules (none was due on 12 Nov).
- Customer told to bulk-send the other 111 queued invoices (filter "Queued", up to 50 at a time). Daniel says they will do this on the afternoon of 12 Nov. Re-saving 340 schedules by hand is not realistic for them.

## Commitments

Tier 2 now owns these (policy 5.2):
- **Update to Daniel by 16:00 UTC on 12 Nov**, even if the only news is that the investigation is still going.
- Tier 1 said Tier 2 would know about the 13 Nov 07:00 run (64 invoices). The escalation note covers this.
- No fix time was promised. Daniel asked for a guarantee before the 13 Nov run and was told no (policy 6.2). No credit or refund has been offered. Only Elena Marsh (CSM) or the Head of Support may offer one.

## Service level

- Enterprise, P2: targets run 24x7 on calendar time. The ticket was never "Pending customer", so the clock has not paused.
- First response: met (09:41, 27 minutes after creation, target 2 hours).
- Resolution due **Fri 13 Nov 09:14 UTC** (24 hours). This is after the 07:00 run. The ticket becomes at risk at 03:14 on 13 Nov, when less than 6 hours remain. As of 11:30 on 12 Nov it is within target.
- If it is not resolved by 09:14 on 13 Nov, it is breached and the Support Duty Manager must be told (5.3).
- Updates: at least once each business day (7.1).
- A workaround exists (manual bulk send), and that may count as resolution (1.5). It also arguably fits P3 better than P2. Priority stays P2 unless an agent changes it.

## Next action

Send Daniel the 16:00 update. Before then, ask engineering to confirm or rule out KI-3381, and whether pre-v8.3 schedules can be fixed in bulk (for example by a server-side re-save) before the 13 Nov 07:00 run. If that is not possible, tell Daniel to expect to bulk-send the 64 queued invoices after 07:00 on 13 Nov, and the 90 after Sunday's run.
