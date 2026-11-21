# Escalation handoff: QB-204518 Recurring invoices from pre-v8.3 schedules generated but never dispatched

**Customer:** Harrow & Finch Accounting Ltd (HF-0192), Quillbill Practice plan, Enterprise support level (account record: Account ID, Plan, Support level)
**Earliest deadline:** 2026-11-12 16:00 UTC, promised email update to the customer (Priya Nair, 2026-11-12 11:05). The customer's next scheduled run is 2026-11-13 07:00 UTC (customer, 10:52; restated by Priya, 11:05), and the P2 resolution target falls at 2026-11-13 09:14 UTC (policy 3.1).

## Problem as currently understood
The 07:00 UTC recurring run on 12 Nov generated 112 invoices, and the dispatcher made no send attempt for any of them and logged no error; all 112 come from schedules created before the v8.3 release on 10 Nov. Manual sending works, and one schedule dispatched in test mode after being re-saved unchanged. Open hypotheses: the cause is known issue KI-3381, and re-saving a schedule clears the fault; neither is confirmed on a real scheduled run.

### Verified
- The recurring run started at 07:00:03 UTC on 12 Nov and generated 112 invoices; the customer estimated "around 110" (Priya Nair internal note, 2026-11-12 10:20; Daniel Okafor, 09:14)
- All 112 invoices are in dispatch state "Queued - not dispatched", matching the customer's report that they show "Queued" (Priya Nair internal note, 10:20; Daniel Okafor, 09:14)
- The dispatcher shows 0 send attempts and no errors for the 112, so no client was sent an invoice by the run (Priya Nair internal note, 10:20)
- All 112 come from schedules created before 10 Nov (v8.3 release) (Priya Nair internal note, 10:20)
- The account has 3 schedules created after 10 Nov; none was due on 12 Nov, so no post-v8.3 comparison exists yet (Priya Nair internal note, 10:20)
- Manual Send works: INV-2026-11-0457 sent at 10:15 was accepted by the recipient's mail server at 10:16 (Priya Nair internal note, 10:20)
- After schedule "Meadowgate monthly retainer" was re-saved without changes, "Run now (test mode)" dispatched the test invoice within 40 seconds (Priya Nair internal note, 10:20)

### Reported, not verified
- Two clients have rung to ask where their invoice is (Daniel Okafor, 09:14)
- The customer has not changed any settings (Daniel Okafor, 09:14)
- Impact: client payment terms run from the send date, so each day of delay pushes back collections (Daniel Okafor, 09:14)
- The customer has 340 schedules (Daniel Okafor, 10:52); the account record lists 340 active schedules as of 1 November 2026 (account record: Products, Recurring Billing add-on). The thread does not check how many are pre-v8.3.
- Next runs: 13 Nov 07:00 with 64 invoices and Sunday 15 Nov with 90 invoices (Daniel Okafor, 09:14 and 10:52)

### Contradicted
- None

### Hypotheses
- The fault is known issue KI-3381 "Legacy recurring schedules skip auto-send after v8.3" (opened by Engineering 11 Nov, status Investigating, 2 other customers linked); symptoms match but the cause is not confirmed, proposed by Priya Nair (internal note 10:20; customer message 10:34; ticket linked to KI-3381 at 11:30)
- Re-saving a schedule clears the fault for that schedule; seen only in test mode, not on a real scheduled run, proposed by Priya Nair (internal note 10:20; customer message 10:34)

## Tried so far
| # | Action | By | Result | Source |
| --- | --- | --- | --- | --- |
| 1 | Checked the job log for HF-0192 | Priya Nair | 112 invoices generated at 07:00:03, all "Queued - not dispatched", 0 send attempts, no errors | Internal note, 10:20 |
| 2 | Compared schedule creation dates with the v8.3 release | Priya Nair | All 112 from pre-10 Nov schedules; 3 post-10 Nov schedules, none due on 12 Nov | Internal note, 10:20 |
| 3 | Searched known issues | Priya Nair | KI-3381 matches symptoms; same cause not confirmed | Internal note, 10:20 |
| 4 | Manual Send of INV-2026-11-0457 from the invoice list at 10:15, with customer approval (Daniel Okafor, 09:58) | Priya Nair | Accepted by recipient's mail server at 10:16 | Internal note, 10:20 |
| 5 | Re-saved schedule "Meadowgate monthly retainer" without changes, then "Run now (test mode)" (sends only to account owner) | Priya Nair | Test invoice dispatched within 40 seconds; not yet seen on a real scheduled run | Internal note, 10:20 |
| 6 | Bulk-send of the other 111 queued invoices from the invoice list (filter "Queued", up to 50 at a time), on Priya's instructions | Customer (Daniel Okafor), planned for the afternoon of 12 Nov | Result not recorded | Priya Nair, 10:34; Daniel Okafor, 10:52 |

## Commitments to the customer
| Commitment (quoted) | Made by | When | Due | Kept / Missed / Open | Source |
| --- | --- | --- | --- | --- | --- |
| "I'm escalating your ticket to our Product Engineering Support team now" | Priya Nair (Tier 1) | 2026-11-12 11:05 UTC | "now" | Kept: escalated to Tier 2 at 11:30 | Priya Nair, 11:05; event, 11:30 |
| "I'll make sure they know your next run is at 07:00 UTC tomorrow, 13 November, with 64 invoices." | Priya Nair (Tier 1) | 2026-11-12 11:05 UTC | No time stated | Kept: stated in escalation note | Priya Nair, 11:05; escalation note, 11:30 |
| "I will email you an update by 16:00 UTC today with what they've found, even if that is only that they are still investigating." | Priya Nair (Tier 1) | 2026-11-12 11:05 UTC | "by 16:00 UTC today" = 2026-11-12 16:00 UTC | Open; Tier 2 now owns it (policy 5.2) | Priya Nair, 11:05; escalation note, 11:30 |

Customer-claimed, not found in thread:
- None

Requested but not promised:
- Customer asked "Can you guarantee this will be fixed before tomorrow morning's run?" (Daniel Okafor, 10:52); Priya declined: "I can't promise a fix time, because that depends on what engineering finds." (Priya Nair, 11:05). Policy 6.2 bars promising a fix date for a product defect.

## Service level
- Tier and priority: Enterprise (account record: Support level); P2, set at creation and unchanged at escalation (events 09:14 and 11:30)
- Status as of: 2026-11-12 11:30 UTC, the last thread timestamp (current time relative to the case not known; see Gaps)
- Clock: starts at ticket creation, 2026-11-12 09:14 UTC (policy 4.1, event 09:14); pauses only while status is "Pending customer" (policy 4.2); the ticket has never been in that status (events 09:14, 09:41, 11:30), so no paused time

| Target (quoted) | Policy section | Clock start / pauses | Deadline (arithmetic) | Status |
| --- | --- | --- | --- | --- |
| First response "2 hours, 24x7" | 3.1, 3.3, 1.4 | Start 12 Nov 09:14 UTC; no pauses | 09:14 + 2 h = 12 Nov 11:14 UTC | Met: Priya Nair replied at 09:41 (27 min) |
| Resolution "24 hours, 24x7" | 3.1, 3.3, 1.5, 4.5 | Start 12 Nov 09:14 UTC; no pauses | 12 Nov 09:14 + 24 h = 13 Nov 09:14 UTC; "at risk" when < 25% remains: 13 Nov 09:14 − 6 h = 13 Nov 03:14 UTC | Not yet due: 21 h 44 min remaining; within target |
| P2 update "at least once each business day" | 7.1, 1.1 | Business day = 08:00 to 18:00 Europe/London, Mon to Fri; GMT = UTC on these dates | Thu 12 Nov: updates sent 09:41, 10:34, 11:05; Fri 13 Nov: by 13 Nov 18:00 UTC | Met for 12 Nov; Not yet due for 13 Nov (30 h 30 min remaining) |

If the resolution target is breached, the Support Duty Manager must be told (policy 5.3).

## Recommended next action
Confirm with the KI-3381 engineering team whether HF-0192's 112 undispatched invoices share that cause and whether a back-end fix, or a bulk re-save of the pre-v8.3 schedules, can be applied before the 13 Nov 07:00 UTC run of 64 invoices, since the verified evidence (pre-v8.3 schedules only, 0 send attempts, re-save restored dispatch in test mode) points there but the re-save fix is unproven on a real scheduled run. Send the customer the promised update by 12 Nov 16:00 UTC, which Tier 2 now owns (policy 5.2), stating what engineering found and that manual bulk-send from the invoice list remains the fallback for the 13 Nov run if no fix is in place. After the 13 Nov 07:00 run, check its dispatch state against the job log before the resolution target at 13 Nov 09:14 UTC.

## Gaps
- Current time: the thread ends at 2026-11-12 11:30 UTC, so all statuses are as of that time; if this handoff is read later, check whether the 16:00 UTC update was sent and whether the resolution target (13 Nov 09:14 UTC) has passed.
- Result of the customer's bulk-send of the 111 remaining invoices on 12 Nov is not recorded, so it is unknown whether any 12 Nov invoices are still undelivered.
- Whether KI-3381 is the same cause is unconfirmed (internal note, 10:20).
- Whether re-saving a schedule fixes a real scheduled run is untested (internal note, 10:20).
- How many of the customer's 340 schedules were created before v8.3 is not checked in the thread; the account record count dates from 1 November 2026.
- Invoice counts for the 13 Nov (64) and 15 Nov (90) runs and the time of the 15 Nov run come only from the customer; the 15 Nov run time is not stated.
- No post-v8.3 schedule has run yet, so there is no direct comparison (internal note, 10:20).
