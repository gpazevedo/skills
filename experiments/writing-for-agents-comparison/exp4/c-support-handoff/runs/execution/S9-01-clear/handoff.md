# Escalation handoff: QB-204518: Recurring invoices created but not sent (112 stuck "Queued", next run 13 Nov 07:00 UTC)

**Customer:** Harrow & Finch Accounting Ltd (HF-0192), Quillbill Practice, Enterprise support · **Priority:** P2 · **Next deadline:** 2026-11-13 07:00 UTC customer's next recurring run (64 invoices), then 2026-11-12 16:00 UTC promised customer update; contractual resolution deadline 2026-11-13 09:14 UTC, open (as of 2026-11-12 11:30 UTC)

## Problem as currently understood
The 07:00 UTC recurring run on 12 Nov generated 112 invoices, all stuck in "Queued - not dispatched" with no send attempts and no errors. All 112 come from schedules created before the 10 Nov v8.3 release, which matches known issue KI-3381, though the same cause is not confirmed. Manual send works, and re-saving one schedule appeared to restore dispatch in test mode only. The customer has 340 schedules, so re-saving each by hand is not practical, and the next runs are 13 Nov 07:00 UTC (64 invoices) and 15 Nov (90 invoices).

Evidence:
- [Verified] 07:00:03 UTC run generated 112 invoices, all "Queued - not dispatched", 0 send attempts, no errors (Priya Nair internal note, 10:20)
- [Verified] All 112 come from schedules created before 10 Nov; 3 schedules created after 10 Nov exist, none due today, so no comparison yet (Priya Nair internal note, 10:20)
- [Verified] KI-3381 (opened 11 Nov, Investigating, 2 other customers linked) has matching symptoms; same cause not confirmed (Priya Nair internal note, 10:20)
- [Verified] Manual Send of INV-2026-11-0457 at 10:15 was accepted by the recipient's mail server at 10:16 (Priya Nair internal note, 10:20)
- [Verified] Re-saving "Meadowgate monthly retainer" unchanged, then "Run now (test mode)", dispatched in about 40 seconds; test mode only, not seen on a real scheduled run (Priya Nair internal note, 10:20)
- [Reported] No client has received an invoice, and two clients have phoned asking (Daniel Okafor, 09:14)
- [Reported] No settings were changed on the customer's side (Daniel Okafor, 09:14)
- [Reported] Client payment terms run from the send date, so delay pushes back collections (Daniel Okafor, 09:14)
- [Reported] Next runs are 13 Nov 07:00 UTC with 64 invoices and 15 Nov with 90 invoices (Daniel Okafor, 10:52; Priya Nair repeated the 64 and 07:00 in her 11:05 message without saying she checked it)
- [Reported] The customer will bulk-send today's remaining 111 themselves this afternoon (Daniel Okafor, 10:52)
- [Inferred] The 340 schedules on the account are mostly or all pre-v8.3, so tomorrow's and Sunday's runs are likely to be affected too (rests on: all 112 stuck invoices are from pre-v8.3 schedules; account record shows 340 active schedules as of 1 Nov)

## Tried so far
| When | Who | Action | Result |
| --- | --- | --- | --- |
| 10:15 | Priya Nair | Manual Send of INV-2026-11-0457 (customer consented at 09:58) | Accepted by Meadowgate's mail server 10:16 |
| before 10:20 | Priya Nair | Re-saved schedule "Meadowgate monthly retainer" unchanged, then Run now (test mode) | Dispatched within 40 seconds; test mode only |
| 10:20 | Priya Nair | Checked job log and known issues | 112 queued, 0 attempts, no errors; KI-3381 matches, unconfirmed |
| 10:34 | Priya Nair | Gave customer workaround: filter "Queued", select up to 50, Send | Customer will do it this afternoon; no result recorded |
| 11:05 to 11:30 | Priya Nair | Escalated to Tier 2, linked to KI-3381 | Status Escalated, P2 unchanged |

Ruled out: nothing yet. A customer-side settings change is claimed not to have happened (Reported only).

## Commitments to the customer
| Commitment (quoted) | Made by | When | Status |
| --- | --- | --- | --- |
| "I will email you an update by 16:00 UTC today with what they've found, even if that is only that they are still investigating." (16:00 UTC 12 Nov) | Priya Nair | 2026-11-12 11:05 | Outstanding, 4h 30m left. Tier 2 owns it from escalation (policy 5.2) |
| "I'll make sure they know your next run is at 07:00 UTC tomorrow, 13 November, with 64 invoices." | Priya Nair | 2026-11-12 11:05 | Met: stated in the 11:30 escalation note |

Declined, not a commitment: "I can't promise a fix time" (11:05), in answer to the customer's request for a guarantee before tomorrow's run. Do not give one (policy 6.2).
Claimed by the customer, not found in the thread: none

## Service level
- Plan: Quillbill Practice; support level Enterprise (Verified, account record).
- Priority: P2, recorded on the ticket at creation (Verified, ticket event 09:14). The customer's urgency request does not set priority (policy 2.5).
- Targets, policy 3.1, Enterprise P2: first response "2 hours, 24x7"; resolution "24 hours, 24x7". Policy 3.3: 24x7 targets run on calendar time.
- Clock: starts at ticket creation (policy 4.1), 2026-11-12 09:14 UTC (Verified). UTC is the same as Europe/London in November (policy 1.1). Pause only while "Pending customer" (policy 4.2); the thread shows no such status, so no pause applied (Inferred from the status changes shown).
- First response: due 11:14 UTC. Priya Nair replied at 09:41 UTC. Met (27 minutes).
- Resolution: due 2026-11-13 09:14 UTC. Open, 21h 44m remaining as of 2026-11-12 11:30 UTC. Policy 4.5 "at risk" is under 25% remaining, i.e. under 6 hours; status is within target. It becomes at risk at 03:14 UTC on 13 Nov.
- Note: the customer's run at 07:00 UTC on 13 Nov falls 2h 14m before the contractual resolution deadline, so the business deadline is earlier than the SLA deadline.

## Recommended next action
Tier 2 engineer: confirm whether KI-3381 is the cause for HF-0192 and apply an account-level fix or workaround (for example a bulk re-save or engineering-side fix of the pre-v8.3 schedules, checked on a real run if possible), ready before the 13 Nov 07:00 UTC run. Send the 16:00 UTC update today whether or not the cause is found. This follows from the main unverified point: re-saving was only seen in test mode, and the 340-schedule scale rules out the customer fixing it by hand. Follow-ups: (1) check whether the 64 invoices due on 13 Nov are from pre-v8.3 schedules; (2) record the finding on KI-3381.

## Gaps and open questions
- No missing inputs (thread, account record and policy all supplied).
- Same cause as KI-3381 is unconfirmed; re-save fix not seen on a real scheduled run.
- Number of pre-v8.3 schedules: the record's 340 is as of 1 Nov and 3 later schedules exist, so the exact split is unknown. The 64 and 90 invoice counts are customer figures, unchecked.
- Customer says about 110 invoices; the log shows 112. Customer says no client received one; only the manual Meadowgate send is confirmed delivered.
- Priority: policy 2.3 puts P3 where a practical workaround exists. Manual send works for today's batch but not at schedule scale; priority was left at P2 and was not changed by me. Under P3 the targets would differ (30 business hours).
- Whether the customer has bulk-sent the 111 is unknown (customer's stated plan only).
