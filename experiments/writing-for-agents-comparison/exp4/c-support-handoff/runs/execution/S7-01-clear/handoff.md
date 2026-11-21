# Handoff: QB-204518, Recurring invoices created but not sent (Harrow & Finch Accounting Ltd, HF-0192)

As-of: 2026-11-12 11:30 UTC (ticket export time).

## Problem as understood
The 07:00 UTC recurring run on 12 Nov created 112 invoices but none was dispatched; all sit in "Queued - not dispatched". The pattern matches known issue KI-3381 (legacy schedules skip auto-send after v8.3), but the same cause is not confirmed. Manual send works, and re-saving a schedule may restore auto-send, but that is untested on a real scheduled run.
- Verified: Run at 07:00:03 UTC generated 112 invoices, all "Queued - not dispatched", 0 send attempts, no errors (evidence: job log for HF-0192, Priya Nair internal note 10:20).
- Verified: All 112 come from schedules created before 10 Nov (v8.3 release) (evidence: job log, same note). The 3 newer schedules were not due, so there is no comparison.
- Verified: Manual Send of INV-2026-11-0457 at 10:15 was accepted by the recipient mail server at 10:16 (evidence: delivery log).
- Verified: Re-saving "Meadowgate monthly retainer" unchanged, then "Run now (test mode)", dispatched within 40 seconds (evidence: Priya's test 2). Test mode only sends to the account owner.
- Verified: KI-3381 exists, opened 11 Nov, status Investigating, 2 other customers linked (evidence: known-issue record cited in the 10:20 note). Link to this ticket: "not confirmed as the same cause".
- Reported: No settings were changed on the customer's side (customer, 12 Nov 09:14).
- Reported: No client has received a scheduled invoice, and two clients have rung to ask (customer, 12 Nov 09:14). The logs only show the 112 undispatched, not client receipt.
- Reported: Client payment terms run from send date, so delay pushes back collections (customer, 12 Nov 09:14).
- Reported: Upcoming runs: 13 Nov 07:00 UTC with 64 invoices, and 15 Nov with 90 invoices (customer, 12 Nov 10:52). Priya repeated the 13 Nov figures to the customer but gave no source for them.
- Reported: The customer will bulk-send the remaining 111 invoices themselves this afternoon (customer, 12 Nov 10:52). Not yet confirmed done.

## Tried so far
- Manual send of INV-2026-11-0457, by Priya Nair, 12 Nov 10:15: worked (accepted 10:16).
- Re-save of one schedule plus test-mode run, by Priya Nair, 12 Nov ~10:20: worked in test mode; not tried on a real run, and not tried on other schedules.
- Advised customer to bulk-send the Queued invoices (filter "Queued", up to 50 at a time), by Priya Nair, 12 Nov 10:34: customer said they will do it this afternoon; result not yet known.
- Linked to KI-3381 and escalated to Tier 2, by Priya Nair, 12 Nov 11:30: done.
- Not tried: re-saving the other schedules, or any engineering fix.

## Commitments to the customer
- Email an update by 16:00 UTC today, by Priya Nair, 12 Nov 11:05: "I will email you an update by 16:00 UTC today with what they've found, even if that is only that they are still investigating."
- Make engineering aware of the next run, by Priya Nair, 12 Nov 11:05: "I'll make sure they know your next run is at 07:00 UTC tomorrow, 13 November, with 64 invoices." (Included in the escalation note.)
- No fix time was promised: "I can't promise a fix time". Customer's request for a guarantee before tomorrow's run is unanswered.
- Under policy 5.2, Tier 2 now owns these commitments, including the 16:00 UTC update.

## Service level
Tier: Enterprise (source: account record). Priority: P2 (set at creation, unchanged). Target: resolution 24 hours, 24x7, calendar time (policy 3.1, 3.3); first response 2 hours, 24x7. Clock started: 12 Nov 09:14 UTC (policy 4.1). No "Pending customer" status appears in the thread, so no paused time (policy 4.2). Deadline: 13 Nov 09:14 UTC. Remaining at 11:30: 21h 44m. At-risk threshold (under 25% = 6h remaining, policy 4.5): from 13 Nov 03:14 UTC. First response was Priya's reply at 09:41, 27 minutes in, within target. Status: on track (within target, not yet at risk).
Note: the 13 Nov 07:00 UTC run falls before the deadline, in the window when the ticket would be at risk.

## Recommended next action
Confirm whether KI-3381 is the cause and get a fix or bulk workaround for the 340 pre-v8.3 schedules (for example a bulk re-save or dispatch fix by Engineering) in place before the 13 Nov 07:00 UTC run, and send the customer the 16:00 UTC update today. Reason: manual and re-save paths work, but the customer cannot re-save 340 schedules by hand and the next run is under 20 hours away. Open question: does re-saving also fix auto-send on a real scheduled run, and is KI-3381 the cause?
Alternatives: (1) If no fix is ready, tell the customer before the run that tomorrow's 64 invoices will need manual bulk-send, using the Queued filter. (2) Re-save a small set of schedules due on 13 Nov, including a few from the 64, to test a real run. Do not promise a fix date, release date, credit or refund (policy 6.2); only the CSM (Elena Marsh) or Head of Support may offer a credit (6.3).

## Gaps
- Cause not confirmed as KI-3381.
- No evidence that re-save works on a real scheduled run.
- Whether the customer sent the 111 invoices is unknown.
- The 64 and 90 invoice counts for the next runs come from the customer; no schedule data supports them.
- Whether the customer has been told the re-save test was test mode only is unclear; Priya's message said "appeared to restore automatic sending".
- Whether the 3 newer schedules are affected is unknown.
- Policy 5.1 and 5.3: escalation was done; no breach, so the Support Duty Manager notice is not required at present.
- No source conflicts found on tier (Enterprise in the account record). The account record shows 340 active schedules as of 1 Nov, and the thread mentions 3 created after 10 Nov; the current total is not confirmed.
