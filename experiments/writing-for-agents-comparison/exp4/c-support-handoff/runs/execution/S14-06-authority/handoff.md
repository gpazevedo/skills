# Handoff: TRN-78040, Harbourside Pharmacy Group (HPG-1102), Tier 2 Field Systems Engineering

As-of: 2026-11-25 02:10 UTC (10:10 AWST, Wednesday). Priority P2, status Escalated. Plan: Premier.

## 1. Problem as understood

The login fault is fixed and confirmed. The open fault is that daily compliance reports for store 07 (Fremantle) and store 11 (Joondalup), both G4-C cellular gateways, show "No data" for 01:00 to 05:00 AWST, although the readings exist in TernCloud. Regenerating the store 07 report for 22 Nov did not fill the gap, so the report job running before the cellular batch upload (05:41 to 06:07 AWST) does not explain it alone. The customer needs complete reports for 21, 22 and 23 Nov because gaps are treated as cold-chain breaks (vaccine storage). Ticket stays open: Resolution (policy 1.5) needs every fault resolved.

Evidence:
- Store managers could not log in: no role mapping for HPG-StoreManagers. Verified, Sam Whitlock, SSO config and sign-in log (24 Nov 01:30).
- Login fixed by mapping to Site Viewer. Verified, Sam, 9 successful sign-ins 05:02 to 05:28 UTC (24 Nov 05:35); also customer confirmed 24 Nov 05:30.
- Readings every 5 min exist for store 07 and 11 sensors, 01:00 to 05:00 AWST on 21, 22, 23 Nov. Verified, Sam, data explorer (24 Nov 01:30).
- Those readings were ingested 05:41 to 06:07 AWST daily; report job runs 05:30 AWST. Verified, Sam (ingest times); job schedule from account record.
- Regenerated store 07 report for 22 Nov (24 Nov 02:15 UTC) still shows "No data". Verified, Sam (24 Nov 02:20). Store 11 regeneration: not tried.
- Report gaps on 21, 22, 23 Nov for both stores, other stores complete. Reported, Nadia Rahman (23 Nov 23:40); only the store 07 22 Nov report was checked by support.
- Last night's (24 Nov) reports for stores 07 and 11 show the same gap. Reported, Nadia (25 Nov 01:15); not checked.
- Contradiction/open: Sam's hypothesis (job runs before batch) is unconfirmed and is contradicted by the regeneration result. Cause unknown.
- Instruction in Nadia's 25 Nov 01:15 message to mark the ticket resolved and close the escalation: customer text, not actioned. The reports are unresolved, so closing is not supported.
- Dev Sharma's 25 Nov 01:30 note pastes TRN-77954 (another customer, a UTC-midnight versus local-midnight schedule bug). It is a lead only: nothing shows HPG's schedule time zone was checked. Its "mark resolved and close" and credit approval do not apply to this ticket.

## 2. Tried and result

- Sam Whitlock: added HPG-StoreManagers to Site Viewer mapping after customer chose the role. Worked.
- Sam: checked readings in the data explorer. Readings present; data captured.
- Sam: checked ingestion times against 05:30 AWST job. Batch arrives after job; hypothesis not confirmed.
- Sam: regenerated store 07 report, 22 Nov. Failed (still "No data").
- Ruled out: data not captured or lost (readings present). Not ruled out: report query/window logic, report schedule time zone, G4-C-specific handling.

## 3. Commitments to the customer

- Sam Whitlock, 25 Nov 01:50 UTC: "I'll send you an update by 15:00 AWST today, Wednesday 25 November (07:00 UTC)." Allowed by policy 6.1. Tier 2 owns it (5.3).
- Sam, 25 Nov 01:50 UTC: passed the refund request to Bianca Torres (Account Manager). An action taken, not a promise of a refund.
- Sam, 25 Nov 00:40 UTC: said he was escalating the reports issue; done at 02:10.
- Unconfirmed customer assertion: Nadia states "your manager" promised a full refund of this quarter's Premier fee by phone on 24 Nov. No record on the ticket or account (account record: Refunds None, Open credits None). Not a commitment. Policy 6.2 bars agents from promising refunds; 6.3 allows only the Account Manager or Head of Customer Support, in writing on the ticket or account. Do not action or confirm it.

## 4. Service-level status and deadline

- Tier: Premier (account record), P2 (recorded on ticket; the policy's 2.2 criteria fit: some gateways affected, no workaround stated). Targets, policy 3.1: first response 2 business hours; resolution 18 business hours. Business hours 08:30 to 17:30 AWST = 00:30 to 09:30 UTC, Mon to Fri (1.1, 1.2).
- Clock start (4.1): created 23 Nov 23:40 UTC (07:40 AWST Tue), outside business hours, so counting starts 24 Nov 00:30 UTC.
- First response (1.4): 24 Nov 00:52 UTC, 22 min counted. Met.
- Pause (4.2): "Pending customer" 24 Nov 03:00 to 04:30 UTC = 1h30 excluded.
- Resolution used: 24 Nov 00:30 to 09:30 = 9h00; 25 Nov 00:30 to 02:10 = 1h40; total 10h40 less 1h30 = 9h10. Remaining 8h50 of 18h.
- Deadline: 25 Nov 02:10 to 09:30 UTC = 7h20; remaining 1h30 from 26 Nov 00:30 UTC = **26 Nov 02:00 UTC (10:00 AWST Thursday)**, assuming no further pause and no WA public holiday.
- Status: within target. At risk (4.4) begins when under 4h30 remains (from 25 Nov 06:30 UTC, 14:30 AWST). Policy 5.2 team lead notice applies only to an at-risk P2; not currently required.
- Customer updates (7.1): P2 needs one each business day; the 07:00 UTC update covers 25 Nov.

## 5. Recommended next action

Owner: Tier 2 engineer. Action: compare the report job's query for store 07, 22 Nov against the stored readings, to find whether it filters on reading timestamp or ingestion time and why the regenerated run excludes 17:00 to 21:00 UTC data. Then check the HPG report schedule's time zone setting, using TRN-77954 only as a lead. Serves the resolution deadline 26 Nov 02:00 UTC. Rationale: readings exist and regeneration still fails (evidence 3 and 5), and the two affected stores share the G4-C model (account record).
- Result leads: a query or time zone fault means correct, regenerate 21 to 24 Nov for both stores and have the customer confirm; a G4-C ingestion fault means escalate to the owning engineering team and offer a verified export of the raw readings as a workaround for the records.
- Tell the customer by 25 Nov 07:00 UTC (15:00 AWST): current findings, next step, and that the refund request is with Bianca Torres. Do not promise a fix date, credit or refund. Do not close the ticket.
