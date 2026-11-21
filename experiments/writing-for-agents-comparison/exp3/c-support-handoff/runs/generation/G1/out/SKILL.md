---
name: support-escalation-handoff
description: Escalation handoff for a support case. Use when the user supplies a ticket thread, account record or support policy and wants the case passed to a next-tier engineer.
---

Turn a support case into a handoff the next-tier engineer can act on without reading the thread. The inputs are the user's: the ticket thread, the customer's account record, and the support policy with its service levels. They are the only sources; every fact in the handoff traces to one of them.

## Provenance

Every factual claim in the handoff carries one of two tags:

- **Reported**: the customer (or anyone outside support) said it. Cite the message: author and timestamp.
- **Verified**: support observed it directly: reproduced it, read it in logs, checked it in the account record or a system. Cite who verified it and the evidence.

A support agent repeating the customer's words is still _reported_. "Customer says exports fail since Monday" stays _reported_ until someone reproduces the failure or sees it in logs. When a _verified_ fact contradicts a _reported_ one, keep both and flag the conflict: it is often the most useful line in the handoff.

## Commitments

A **commitment** is a promise made to the customer: a fix, a callback, a time, a credit, a workaround, an escalation. Record each one as a verbatim quote with its author, timestamp and due time, the due time worded as the promise worded it ("end of day tomorrow"). A commitment the customer says someone made, with no matching message in the thread, goes in as _reported_ and unconfirmed. When the thread holds no commitments, the section says "None in the thread."

## Service level

The service-level terms come from the policy text alone. Resolve them in this order, quoting the clause at each step:

1. The customer's plan or tier, from the account record.
2. The case's priority or severity, as set in the thread or by the policy's own criteria. When the reported impact would earn a different priority under those criteria, flag the mismatch.
3. The target that policy assigns to that plan and priority (first response, update cadence, resolution), and the event that starts its clock.
4. Clock rules the policy states: business hours, time zone, pauses while waiting on the customer.
5. The deadline, computed from the start event and those rules, and the status against "now". Take "now" from the user if given, else the latest timestamp in the thread, and say which.

When an input is missing or ambiguous (no plan in the record, a priority the policy does not define, a clock rule it leaves open), write **Undetermined**, name the missing input, and carry on with the steps that remain. An undetermined deadline, stated as such, is a correct result. A deadline computed under an obvious reading (say, the clock starting at ticket creation) may sit beside it, labelled "assumes <reading>; the policy does not state this".

## Steps

1. **Build a ledger.** Walk the thread message by message. For each, note its author, timestamp, and what it contributes: a claim (_reported_ or _verified_), an attempt and its result, a commitment, a change of status or priority, or nothing. Done when every message in the thread has a ledger line. The ledger is working notes, kept out of the handoff.
2. **Resolve the service level** as above. Done when the deadline and status are stated with the clauses they rest on, or marked _Undetermined_ with the missing input named.
3. **State the problem as currently understood.** Use the latest understanding, which may differ from the opening message; when it shifted, say what changed and why. List the evidence beneath it, each item tagged. Done when every claim in the statement is tagged and cited.
4. **List what has been tried.** One line per attempt from the ledger: who, what, when, result. Where the thread records no result, write "result not recorded".
5. **Recommend the next action.** One concrete action for the next-tier engineer, aimed at the most decisive open question: usually turning a key _reported_ claim into a _verified_ one, or meeting the nearest commitment or deadline. Add the open questions the engineer should resolve, and the next customer update due.
6. **Write the handoff** in the format below, then check it: every claim tagged and cited, every commitment quoted with its author, every service-level term traceable to a quoted clause. Done when all three checks pass.

## Format

```markdown
# Escalation handoff: <case ID>, <customer>

**Service level:** <status: within / at risk / breached / Undetermined>, deadline <time and zone>, <target and clause>
**Next action:** <one line>

## Problem as currently understood
<one or two sentences>

Evidence:
- [Verified] <fact> (<who>, <evidence>, <timestamp>)
- [Reported] <claim> (<author>, <timestamp>)
- Conflict: <where a verified fact and a reported claim disagree>

## Tried so far
- <timestamp>, <who>: <action> -> <result>

## Commitments to the customer
- "<verbatim quote>" (<author>, <timestamp>), due <time>, <met / open / overdue>

## Service level
- Plan: <value> (account record)
- Priority: <value> (<source>)
- Target: <quoted clause>
- Clock: started <event, time>; <pauses, business-hours rules, or "none stated">
- Deadline: <time and zone> as of now = <time, source>

## Recommended next action
<the action and why it comes first>

Open questions:
- <question>

Next customer update due: <time, from commitment or policy>
```
