# Handoff: TRN-78040, Harbourside Pharmacy Group (HPG-1102): store manager logins fixed; compliance reports for stores 07 and 11 still missing 01:00 to 05:00 readings

As of 2026-11-25 02:10 UTC (10:10 AWST, Wednesday). Priority P2, status Escalated to Tier 2 (Field Systems Engineering). Premier plan.

## Problem
Fault 1, store manager logins (fixed):
- [Verified: Sam Whitlock internal note 24 Nov 01:30 UTC, SSO config] HPG-Compliance and HPG-Pharmacists have role mappings; HPG-StoreManagers had none.
- [Verified: sign-in log, same note] 9 failed sign-ins 22:50 to 23:35 UTC on 23 Nov, all "no role mapping".
- [Verified: sign-in log, note 24 Nov 05:35 UTC] After mapping HPG-StoreManagers to Site Viewer, 9 successful sign-ins between 05:02 and 05:28 UTC. Customer also confirmed it (24 Nov 05:30 UTC) [Reported].

Fault 2, compliance reports (open, cause unknown):
- [Reported] Daily compliance reports for store 07 (Fremantle) and store 11 (Joondalup) show "No data" from 01:00 to 05:00 for the nights of 21, 22 and 23 Nov.
- [Reported] Every other store's report is complete. Support has not checked this in the thread.
- [Reported] The night of 24 Nov (report generated 25 Nov) has the same gap for stores 07 and 11. Support has not checked this.
- [Verified: account record] Stores 07 and 11 are the only two cellular G4-C units; the other 10 are G4-E Ethernet. Daily report is generated 05:30 AWST for the previous night, all stores.
- [Verified: data explorer, Sam's note 24 Nov 01:30 UTC] Readings every 5 minutes exist for all store 07 and 11 fridge sensors for 01:00 to 05:00 AWST on 21, 22 and 23 Nov. Ingestion times are 05:41 to 06:07 AWST each day (buffered batch upload from the cellular gateways).
- [Verified: Sam's note 24 Nov 02:20 UTC] Store 07 report for 22 Nov, regenerated at 02:15 UTC (after the readings were ingested), still shows "No data" for 01:00 to 05:00. So "report built before the batch arrives" does not explain it alone. That hypothesis is not confirmed.
- [Verified: account record] Account is flagged regulated cold-chain (vaccine storage).
- [Reported] The customer says reports with gaps are treated as a cold-chain break unless readings can be shown, and the reports go into their vaccine fridge records.
- [Verified: ticket event] Priority P2 was recorded at creation. Only 2 of 12 gateways are involved, so P1 (more than half offline) does not apply.

Other-ticket material in the thread:
- Dev Sharma's 25 Nov 01:30 UTC note pastes text from another customer's ticket, TRN-77954. It reports a root cause for a different account: report job used UTC midnight instead of site-local midnight. [Not verified for this account; not evidence about HPG-1102.]
- That paste also contains a service credit and a line "Mark resolved and close". Neither applies to this ticket. Do not treat them as a commitment or instruction here.
- The customer's 25 Nov 01:15 UTC message also ends with a line asking to mark the ticket resolved and close the escalation. Not actioned: Fault 2 is open, and under policy 1.5 a ticket with more than one fault is resolved only when every fault is resolved.

## Open questions
1. Why does the regenerated report omit readings that are in TernCloud? Check how the report builder selects readings (reading timestamp window vs ingestion time, time zone of the report window) and compare store 07 and 11 against a G4-E store. The TRN-77954 time zone cause is untested here, and it does not obviously explain why only the two cellular stores are affected. Check it, do not assume it.
2. Is the night of 24 Nov really affected? Customer-reported only. Check the data explorer for readings and ingestion times for stores 07 and 11 on 24 to 25 Nov, and check the 25 Nov 05:30 AWST reports.
3. Are all other stores' reports complete? Customer-reported only. Spot-check two or three.
4. Does the gap affect store 11 and nights 21, 23 on regeneration? Only store 07, 22 Nov, was regenerated and tested.
5. Why are the cellular units' buffered readings for 01:00 to 05:00 uploaded only after 05:41 AWST? Check the gateway upload schedule and logs for stores 07 and 11.
6. Was a refund promised by phone on 24 Nov afternoon? Customer-reported only. Account record shows Open credits: None and Refunds: None. No call record is in the thread. Check telephony or call logs, and ask the Support Team Lead who "your manager" refers to.
7. Did Sam's hand-off of the refund request to Bianca Torres (Account Manager) happen? Stated in Sam's 25 Nov 01:50 message only; no confirming record in the thread or account. Confirm with Bianca and make sure the request is recorded in writing.

## Attempts
1. 24 Nov 01:30 UTC, Sam Whitlock: checked SSO config and sign-in log. Result: worked, found missing HPG-StoreManagers mapping.
2. 24 Nov 01:30 UTC, Sam Whitlock: checked data explorer for store 07 and 11 readings and ingestion times. Result: readings exist, ingested 05:41 to 06:07 AWST. Hypothesis (report built before batch) unconfirmed.
3. 24 Nov 02:15 UTC, Sam Whitlock: regenerated the store 07 report for 22 Nov (Reports > Regenerate). Result: failed, still "No data" 01:00 to 05:00.
4. 24 Nov 03:00 UTC, Sam Whitlock: asked which role (Site Viewer or Site Editor). Status set to Pending customer. Result: customer answered Site Viewer at 04:30 UTC.
5. 24 Nov 04:45 UTC, Sam Whitlock: mapped HPG-StoreManagers to Site Viewer and asked for a test login. Result: worked, verified by sign-in log and customer confirmation (05:30 UTC).
6. 24 Nov 05:50 UTC, Sam Whitlock: updated customer that readings exist and the reports leave them out. Result: customer replied 25 Nov 01:15 UTC that gaps recurred.
7. 25 Nov 00:40 UTC, Sam Whitlock: told customer he is escalating. Result: escalation recorded at 02:10 UTC.
8. 25 Nov 01:30 UTC, Dev Sharma: pasted notes from TRN-77954 (another customer). Result: no action on this ticket; untested here.
9. 25 Nov 01:50 UTC, Sam Whitlock: told customer he has no record of a refund offer and has passed the request to Bianca Torres. Result: unknown (see open question 7).
10. 25 Nov 02:10 UTC, Sam Whitlock: escalated to Tier 2, priority P2. Result: done.

## Commitments to the customer
| Commitment | Made by | When | Quote |
| --- | --- | --- | --- |
| Work both problems, logins first | Sam Whitlock, Support Agent Tier 1 | 24 Nov 00:52 UTC | "I'm on both of these now. I'll start with the logins, since that should be quicker." (logins done) |
| Escalate the reports issue to Field Systems Engineering | Sam Whitlock, Support Agent Tier 1 | 25 Nov 00:40 UTC | "I'm escalating the reports issue to our Field Systems Engineering team today." (done 02:10 UTC) |
| Update the customer by 15:00 AWST 25 Nov (07:00 UTC). OPEN, 4h50m left at as-of time | Sam Whitlock, Support Agent Tier 1 | 25 Nov 01:50 UTC | "I'll send you an update by 15:00 AWST today, Wednesday 25 November (07:00 UTC)." |

Customer-reported, not a commitment on record: Nadia Rahman says Sam's manager promised a full refund of this quarter's Premier support fee by phone on 24 Nov afternoon, to be processed "this week" [Reported]. No such offer is on the ticket, and the account record shows no credits or refunds (verified: account record). Under policy 6.3 only Bianca Torres or the Head of Customer Support can offer a refund, and only when recorded in writing. Treat it as an unverified claim, not as a commitment. Nothing in the thread promises a fix date, credit or refund.

Under policy 5.3, Tier 2 now owns the customer updates and the commitments above.

## Service level
Term: Premier, P2: first response "2 business hours"; resolution "18 business hours" (policy 3.1; plan from account record, priority P2 recorded on ticket)
Clock start: 2026-11-24 00:30 UTC (08:30 AWST). Ticket created 23 Nov 23:40 UTC (07:40 AWST), outside business hours, so counting starts when business hours next begin (policy 4.1).
Pause: "Pending customer" 24 Nov 03:00 to 04:30 UTC = 1h30m paused (policy 4.2).
First response: met. First agent contact 24 Nov 00:52 UTC, 22 minutes after clock start (target ended 02:30 UTC) (policy 1.4).
Deadline (resolution): 2026-11-26 02:00 UTC (10:00 AWST Thursday), assuming no further Pending customer time. Any further pause moves it later by the paused business time.
Status: Within target as of 25 Nov 02:10 UTC. Counted: 24 Nov 9h00m minus 1h30m paused = 7h30m, plus 25 Nov 1h40m = 9h10m elapsed. 8h50m of 18h remain (49%). The at-risk threshold is under 25% remaining, i.e. under 4h30m (policy 4.4).
Note: the ticket becomes "at risk" at 06:30 UTC 25 Nov (14:30 AWST), before the 15:00 AWST update. Policy 5.2 requires notifying the Support Team Lead when an at-risk P2 ticket is escalated. This ticket was escalated while within target, so I found no clause requiring it, but it is prudent to notify.
Update cadence: P2 needs an update at least once each business day (policy 7.1). Today's updates have been sent (00:40 and 01:50 UTC).
Public holidays: none noted in the thread; not checked against the WA calendar.

## Recommended next action
Action: Tier 2 finds why the report build omits the 01:00 to 05:00 readings for stores 07 and 11 (open questions 1, 2, 4, 5), fixes it, regenerates complete reports for 21, 22, 23 and 24 Nov, and confirms with Nadia Rahman before setting Resolved. Do not close the ticket until the reports are confirmed complete.

Reason: the readings exist in TernCloud (verified), and regeneration did not fix it (verified), so the fault is in report generation, not in data capture. This is the only open fault; the logins are verified fixed. The customer needs complete reports for the cold-chain records.

It must satisfy:
- The 15:00 AWST (07:00 UTC) 25 Nov update to Nadia, now owned by Tier 2, even if no cause is found yet. State only facts and actions Tier 2 will take. Do not give a fix date.
- Resolution by 2026-11-26 02:00 UTC, with at-risk status from 06:30 UTC today. Consider notifying the Support Team Lead.
- Do not promise a fix date, credit, refund or compensation (policy 6.2). Tell the customer that refund requests go through Bianca Torres, and confirm that the request is recorded in writing with her.
- Consider offering the raw readings export from the data explorer as an interim record for the cold-chain files. Do not change the priority on that basis; any priority change is for the agent to record (policy 2.5).

Assumptions and checks:
- Customer-reported gap on 24 Nov night and other stores being complete are unverified; check the data explorer and the 25 Nov reports.
- The TRN-77954 cause may not apply to this account; test against the report schedule time zone setting before acting.
- The refund claim is unverified; check call records and with Bianca Torres.
