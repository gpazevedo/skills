# Handoff: QB-204518, Harrow & Finch (HF-0192), escalated to Tier 2

Status as of 2026-11-12 11:30 UTC. Enterprise support, P2. Owner from escalation: Tier 2 (policy 5.2). Escalated by Priya Nair.

## Do first
Before the 13 Nov 07:00 UTC run (64 invoices), get the 340 pre-v8.3 recurring schedules sending automatically. Failing that, agree a workaround with the customer. Send the customer the 16:00 UTC update today (see Commitments).

## 1. Problem
Recurring invoices are created but not dispatched.

Verified by support:
- The 07:00:03 UTC run on 12 Nov generated 112 invoices. All 112 are "Queued - not dispatched", with 0 send attempts and no errors.
- All 112 come from schedules created before 10 Nov (the v8.3 release).
- The account has 3 schedules created after 10 Nov. None was due today, so there is no comparison yet.
- Known issue KI-3381 (Legacy recurring schedules skip auto-send after v8.3) has symptoms that match. It is an Engineering issue, Investigating, with 2 other customers linked. Same cause is not confirmed.

Reported by customer, not verified:
- The customer says about 110 invoices were expected, no client received one, and two clients have phoned.
- The customer says it changed no settings.
- The customer says it has 340 schedules (the account record agrees: 340 active as of 1 Nov).
- The customer says the next runs are 13 Nov with 64 invoices and 15 Nov with 90. Support has not checked these counts.
- The customer says payment terms run from the send date, so delay pushes back collections.

## 2. Tried
- Manual Send of INV-2026-11-0457 (Meadowgate Ltd), with customer consent, at 10:15. It worked: the recipient's mail server accepted it at 10:16.
- Re-saved the schedule "Meadowgate monthly retainer" with no changes, then ran "Run now (test mode)" (sends to the account owner only). It dispatched in about 40 seconds. This suggests a re-save clears the fault, but it is not seen on a real scheduled run, and a real run is not due for that schedule until next month. The fault was not tested on the other schedules.
- Customer told to bulk-send the other 111 queued invoices from the invoice list (filter "Queued", up to 50 at a time). The customer says it will do this this afternoon (not yet confirmed done).

## 3. Commitments to the customer
Made by Priya Nair (Tier 1) at 11:05, by email to Daniel Okafor:
- An update by 16:00 UTC today, even if it is only "still investigating". Tier 2 now owns this.
- Priya told the customer she would make sure engineering knows about the 13 Nov 07:00 UTC run (64 invoices).
- No fix date, credit or refund was promised. Priya said explicitly that she cannot promise a fix time. The account record shows no credits or refunds.

## 4. Service level
Enterprise P2: first response 2 hours, resolution 24 hours, both on calendar time (24x7).
- First response: met. Ticket created 09:14, first reply 09:41 (27 minutes).
- Resolution deadline: **13 Nov 2026 09:14 UTC**. The clock has never been paused: no "Pending customer" status in the history.
- Status: within target. 2h16m of 24h used and 21h44m left, against the 6h at-risk threshold. It becomes "at risk" after 13 Nov 03:14 UTC. The deadline falls 2h14m after the 07:00 run.
- The Duty Manager must be told only if the ticket breaches (policy 5.3). It has not.

## Questions and requests for Tier 2
1. Is the cause KI-3381? Does it affect all 340 pre-v8.3 schedules?
2. Can Engineering fix it, or bulk-re-save the schedules from the back end, before 07:00 UTC 13 Nov? If not, what should the customer do for the 64 invoices? The customer cannot re-save 340 schedules by hand.
3. If Engineering later flushes the queue, does it risk double-sending invoices the customer has already sent by hand? Agree this with the customer before acting.
4. Is P2 still the right priority? Policy 2.2 needs "no practical workaround", and bulk-send is a manual workaround (policy 2.3 would make it P3). Priya left it at P2. Only an agent can change it (2.5), and a change alters the target (4.4). Please decide and record it.
5. Only the Customer Success Manager (Elena Marsh) or the Head of Support may offer a credit or refund, in writing on the ticket (6.3). Nothing has been offered. Involve her if the customer raises compensation.
