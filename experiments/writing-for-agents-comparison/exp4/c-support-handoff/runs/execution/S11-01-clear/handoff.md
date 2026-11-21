# Escalation handoff: QB-204518 Recurring invoices created but not dispatched (112 stuck "Queued", pre-v8.3 schedules, KI-3381 linked)

**Customer:** Harrow & Finch Accounting Ltd (HF-0192), Quillbill Practice plan, Enterprise support level (account record: Plan, Support level)
**Earliest deadline:** 2026-11-12 16:00 UTC, customer update promised by Priya Nair (thread, 11:05). Next in line: customer's next recurring run 2026-11-13 07:00 UTC with 64 invoices (customer message 10:52; Priya 11:05). That run is a business event, not a policy deadline. The policy resolution target falls at 2026-11-13 09:14 UTC.

## Problem as currently understood
The 07:00 run on 12 Nov generated 112 invoices that are all in "Queued - not dispatched" with 0 send attempts and no errors. All 112 come from schedules created before the 10 Nov v8.3 release. Manual send works, and re-saving a schedule followed by a test-mode run dispatched in test mode. Hypothesis, not confirmed: this is KI-3381.

### Verified
- Run at 07:00:03 UTC generated 112 invoices; all 112 are "Queued - not dispatched"; dispatcher shows 0 send attempts and no errors (internal note, Priya Nair, 10:20)
- All 112 come from schedules created before 10 Nov (v8.3 release); the account has 3 schedules created after 10 Nov, none due today, so there is no comparison yet (internal note, 10:20)
- Manual Send of INV-2026-11-0457 at 10:15 was accepted by the recipient's mail server at 10:16 (internal note, 10:20, delivery log)
- After re-saving "Meadowgate monthly retainer" unchanged, "Run now (test mode)" dispatched the test invoice within 40 seconds. This is test mode only, sent to the account owner (internal note, 10:20)
- KI-3381 "Legacy recurring schedules skip auto-send after v8.3" exists, opened by Engineering on 11 Nov, status Investigating, 2 other customers linked (internal note, 10:20)
- The account has 340 active schedules as of 1 Nov 2026 (account record: Products)
### Reported, not verified
- Around 110 invoices were expected at 07:00 (Daniel Okafor, 09:14). Support's count is 112, so this is consistent.
- No client has received an invoice, and two clients rang to ask (Daniel Okafor, 09:14)
- No settings were changed on the customer side (Daniel Okafor, 09:14)
- Client payment terms run from the send date, so delay pushes back collections (Daniel Okafor, 09:14)
- Next runs: 13 Nov 07:00 UTC with 64 invoices, and Sunday 15 Nov with 90 (Daniel Okafor, 10:52; 64 also restated by Priya Nair, 11:05, from the customer's figure)
- Customer will bulk-send the 111 remaining invoices themselves this afternoon (Daniel Okafor, 10:52)
- Re-saving restores automatic sending on a real scheduled run: not yet seen (internal note, 10:20)
### Contradicted
- None
### Hypotheses
- The fault is KI-3381 (legacy schedules skip auto-send after v8.3), proposed by Priya Nair; she states it is not confirmed as the same cause (internal note 10:20; Priya Nair 10:34; escalation note 11:30)
- Re-saving a schedule clears the fault, proposed by Priya Nair ("seems to", test mode only) (internal note, 10:20)

## Tried so far
| # | Action | By | Result | Source |
| --- | --- | --- | --- | --- |
| 1 | Reviewed job log and dispatcher for HF-0192 | Priya Nair | 112 queued, 0 attempts, no errors | Internal note 10:20 |
| 2 | Checked known issues | Priya Nair | KI-3381 symptoms match; cause not confirmed | Internal note 10:20 |
| 3 | Manual Send of INV-2026-11-0457 (customer consented, 09:58) | Priya Nair | Accepted by recipient server 10:16 | Internal note 10:20; Daniel Okafor 09:58 |
| 4 | Re-saved schedule "Meadowgate monthly retainer" without changes, then "Run now (test mode)" | Priya Nair | Dispatched within 40 seconds (test mode, account owner only) | Internal note 10:20 |
| 5 | Customer told to bulk-send the Queued invoices from the invoice list (filter "Queued", up to 50 at a time, Send) | Priya Nair instructed; Daniel Okafor to do it this afternoon | Result not recorded | Priya Nair 10:34; Daniel Okafor 10:52 |

## Commitments to the customer
| Commitment (quoted) | Made by | When | Due | Kept / Missed / Open | Source |
| --- | --- | --- | --- | --- | --- |
| "I will email you an update by 16:00 UTC today with what they've found, even if that is only that they are still investigating." | Priya Nair | 2026-11-12 11:05 | 2026-11-12 16:00 UTC | Open (4h30m left at 11:30). Under policy 5.2 Tier 2 now owns it. | Thread 11:05; escalation note 11:30; Policy 5.2, 6.1 |
| "I'm escalating your ticket to our Product Engineering Support team now" | Priya Nair | 2026-11-12 11:05 | "now" | Kept (escalated to Tier 2 at 11:30) | Thread 11:05; event 11:30 |
| "I'll make sure they know your next run is at 07:00 UTC tomorrow, 13 November, with 64 invoices." | Priya Nair | 2026-11-12 11:05 | No time stated | Kept (the 11:30 escalation note states 13 Nov 07:00 UTC, 64 invoices) | Thread 11:05; escalation note 11:30 |

Customer-claimed, not found in thread:
- None. Daniel's "Can you guarantee this will be fixed before tomorrow morning's run?" (10:52) is a question, and Priya declined to promise a fix time (11:05), which is consistent with Policy 6.2. It may be treated as an expectation: do not promise a fix date.

## Service level
- Tier and priority: Enterprise support level (account record); P2 recorded at ticket creation, unchanged at escalation (thread 09:14 and 11:30). The priority was not requested by the customer in the text. Daniel's "treat this as urgent" is a request, not a priority change (Policy 2.5).
- Status as of: 2026-11-12 11:30 UTC (the thread's stated as-of time, treated as current)
- Clock: starts at ticket creation 09:14 (Policy 4.1). No "Pending customer" status appears in the thread (statuses: New, Open, Escalated), so no pause (Policy 4.2).

| Target (quoted) | Policy section | Clock start / pauses | Deadline (arithmetic) | Status |
| --- | --- | --- | --- | --- |
| First response: "2 hours, 24x7" (Enterprise P2) | 3.1, 3.3 | Start 09:14; no pauses | 09:14 + 2h = 11:14 on 12 Nov. First agent reply was 09:41 (27 min) | Met |
| Resolution: "24 hours, 24x7" (Enterprise P2) | 3.1, 3.3, 4.5 | Start 09:14; no pauses | 09:14 + 24h = 09:14 on 13 Nov; elapsed 2h16m, remaining 21h44m | Not yet due; within target (at-risk line is under 6h left, 25% of 24h, i.e. from 03:14 on 13 Nov) |
| Customer update: "once each business day" (P2) | 7.1 | Business day 12 Nov (Thursday) | Priya's updates at 10:34 and 11:05 count | Met for 12 Nov; next due by 13 Nov (Friday). The 16:00 commitment is the nearer promise. |

Notes: The 13 Nov 07:00 run falls before the resolution deadline, so the policy target does not cover it. The Support Duty Manager must be told only of P2 tickets that are breached (Policy 5.3), so not now. Policy 5.1 escalation applied when the ticket could not be resolved with documented procedures.

## Recommended next action
Confirm whether KI-3381 is the cause for HF-0192, and find a fix or a bulk workaround for all 340 schedules (the policy gives no fix date to promise). Send the customer the promised update by 16:00 UTC today even if it is only a progress note. Ideally have a decision before the 13 Nov 07:00 UTC run (64 invoices).

## Gaps
- The cause is not confirmed: KI-3381 is a match but not proven. The re-save effect is seen only in test mode, not on a real scheduled run.
- The 3 post-10 Nov schedules have not yet run, so there is no control comparison.
- No result recorded for the customer's bulk send (item 5).
- Whether the 340 schedules are all pre-10 Nov is not stated. Only the 112 invoices are confirmed as from pre-v8.3 schedules.
- Policy 2.2 defines P2 as "no practical workaround". Manual and bulk send exist, so a P3 argument is possible. Support assigned P2 and nothing in the policy has been changed, so P2 is used here. This is an assessment, not a recorded change.
- The customer is told 13 Nov and 15 Nov runs (customer-stated counts 64 and 90): not checked against system data.
