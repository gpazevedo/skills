# Handoff: QB-204518, Harrow & Finch Accounting Ltd (HF-0192)

## 1. Problem as understood
The 07:00 UTC recurring run on 12 Nov created 112 invoices that all sit in "Queued - not dispatched" with no send attempts, so none reached clients automatically. It matches known issue KI-3381 (pre-v8.3 schedules skip auto-send), but that is not confirmed as the same cause.

Evidence:
- Reported: about 110 invoices should have been emailed at 07:00, none received by clients, two clients phoned to ask (Daniel Okafor, 12 Nov 09:14). No settings changed on the customer side (same entry).
- Verified (job log, Priya Nair note 10:20): the run at 07:00:03 generated 112 invoices, all "Queued - not dispatched", 0 send attempts, no errors.
- Verified (job log, 10:20): all 112 come from schedules created before 10 Nov (v8.3). The 3 schedules created after 10 Nov were not due, so there is no comparison.
- Verified (delivery log, 10:20): manual Send of INV-2026-11-0457 at 10:15 was accepted by the recipient's mail server at 10:16.
- Verified (test, 10:20): re-saving "Meadowgate monthly retainer" unchanged, then "Run now (test mode)", dispatched within 40 seconds. Test mode only, not seen on a real scheduled run.
- Verified (KI record, per 10:20 note): KI-3381 opened by Engineering 11 Nov, status Investigating, 2 other customers linked.
- Verified (account record): 340 active recurring schedules as of 1 Nov.
- Reported (Daniel 10:52, Priya 11:05 and 11:30 repeat it): next runs are 13 Nov 07:00 UTC with 64 invoices and 15 Nov with 90. Not checked against the schedules.
- Reported: client payment terms run from the send date, so delay defers collections (Daniel 09:14).

Open questions for Tier 2:
- Is the cause the same as KI-3381, and does a fix or bulk workaround exist for all pre-v8.3 schedules?
- Does a re-save also fix a real scheduled run, not just test mode?
- Can all 340 schedules be repaired centrally before 13 Nov 07:00 UTC?
- Are the 64 and 90 counts right, and are they all pre-v8.3 schedules?

## 2. Tried so far
- Priya Nair, 12 Nov 10:15: manual Send of INV-2026-11-0457. Worked (accepted 10:16).
- Priya Nair, 10:20: saved one schedule unchanged, then ran it in test mode. Worked in test mode (inconclusive for real runs).
- Priya Nair, 10:34: gave the customer a workaround to bulk-send from the invoice list (filter "Queued", up to 50 at a time). Not yet confirmed to work at bulk. Daniel said he will bulk-send the other 111 himself that afternoon (10:52). No result recorded.
- Customer attempts: none other than the above. Daniel made no settings changes (Reported).

## 3. Commitments to the customer
- Priya Nair, 12 Nov 11:05: will email Daniel an update by 16:00 UTC today with what engineering found, even if still investigating. Tier 2 owns this (policy 5.2).
- Soft assurance, Priya Nair, 11:05: "I'll make sure they know your next run is at 07:00 UTC tomorrow ... 64 invoices." Done in the 11:30 escalation note.
- Priya Nair, 11:05 explicitly declined to promise a fix time. No fix date, credit or refund promised (account record: no credits or refunds).

## 4. Service-level status
- Plan: Quillbill Practice, support level Enterprise (account record). Priority P2, unchanged (policy 2.2: invoice sending does not work; a manual workaround exists, so a P3 argument is possible, but the priority stands as recorded, 2.5).
- Clause: policy 3.1, Enterprise P2: first response 2 hours (24x7), resolution 24 hours (24x7).
- Clock start: ticket creation, 12 Nov 09:14 UTC (4.1). Time zone: UTC = GMT (1.1). No "Pending customer" status in the thread, so no paused time.
- First response: 09:41 UTC (Priya), 27 minutes after creation. Target 2 hours: met.
- Resolution deadline: 13 Nov 2026 09:14 UTC.
- As of 12 Nov 11:30: 2h16m elapsed, 21h44m remaining (about 90% of target). Status: within target. It becomes "at risk" when under 6 hours remain, from 13 Nov 03:14 UTC (4.5), and breached after 09:14 on 13 Nov if not Resolved.
- The next run (13 Nov 07:00 UTC) falls before the deadline, with about 2h14m left.
- Breach trigger: a breached P2 must be reported to the Support Duty Manager (5.3). The policy gives no credit or other consequence. Escalation to Tier 2 was due on at-risk P2 (5.1) and is done.
- Resolution (1.5) needs a fix or workaround that restores the function and the status set to Resolved. Whether the manual bulk-send counts as such a workaround is Unknown; the policy does not say, and the ticket is not Resolved.

## 5. Recommended next action
Primary: Tier 2 (Product Engineering Support) should find out now whether KI-3381 can be fixed or all of this account's pre-v8.3 schedules repaired centrally (for example by an engineering-side re-save) before 13 Nov 07:00 UTC. If that is not possible, tell the customer well before then so they can bulk-send the 64 invoices manually. Why: the 07:00 run is the next customer impact and falls inside the SLA window; the customer cannot re-save 340 schedules by hand.

Depends on unverified points: that KI-3381 is the same cause, that re-save fixes real runs and not only test mode, and the 64 and 90 invoice counts.

Customer update due: email Daniel Okafor by 16:00 UTC on 12 Nov (Tier 2 owns it). Give findings or "still investigating", and say whether the 13 Nov run is expected to send, with the manual bulk-send as fallback. Do not promise a fix date, credit or refund (6.2); only the CSM (Elena Marsh) or Head of Support can offer a credit (6.3). Duty Manager notice is not yet required (5.3) but would be if the ticket breaches at 09:14 on 13 Nov.
