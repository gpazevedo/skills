---
name: support-escalation-handoff
description: Escalation handoff for the next-tier engineer, built from a support case (ticket thread, account record, support policy). Use when a support ticket is escalated or handed to a higher tier.
---

Turn a support case into a handoff the next-tier engineer can act on without rereading the thread. The user supplies three sources: the **ticket thread**, the **account record**, and the **support policy**. Every fact in the handoff traces to one of them.

## Provenance

Each fact about the problem carries one of three tags:

- **reported**: the customer says it. A customer-attached screenshot or log stays _reported_ until someone in support states they examined it and what it showed. A support agent repeating the customer's words is still _reported_.
- **verified**: support confirmed it with a named check (reproduced it, read a log, inspected the configuration) and the thread records the check and its result. Facts read from the account record are _verified_, citing the record.
- **suspected**: support's working theory with no check recorded yet.

When sources conflict, the account record wins for account facts (plan, tier, region, contacts) and the conflict goes in the handoff: "customer says Enterprise; account record says Pro".

Commitments and service-level terms are a **closed set**: they exist in the handoff only if the supplied material states them, quoted with their location. Where the material is silent, write `not stated in <source>`. This is the hard guardrail of the skill: a plausible-sounding promise or a typical industry SLA filled in from memory sends the engineer after a deadline that does not exist.

## Steps

### 1. Check the sources

Locate the thread, the account record and the policy in what the user supplied.

Done when: each of the three is either located or listed as missing. Continue with what you have; every section that depends on a missing source says so instead of being filled in.

### 2. Build the ledger

Read the thread from first message to last, internal notes included. Record every relevant item as a ledger entry with its source (author, role, timestamp):

- **Claim**: a fact about the problem, tagged _reported_, _verified_ or _suspected_.
- **Attempt**: something tried (by support or by the customer at support's request), who did it, and the result. "No result recorded" is a valid result.
- **Commitment**: a promise sent to the customer (a fix, a callback, a credit, an update by a time). Quote it verbatim, name who made it (a named agent, a manager, or an automated reply), and give its status against now: _met_, _pending_, _overdue_, or _no date given_. Internal notes are never commitments. A customer's request that nobody agreed to is a claim ("customer asked for a callback"), not a commitment.

Done when: every message in the thread has been read and each claim, attempt and commitment in it is a ledger entry with a source.

### 3. Work out the service level

From the policy and the account record, establish:

- the customer's tier (from the account record) and the case's priority or severity (from the thread or ticket fields);
- the target that applies to that tier and priority, quoting the policy clause;
- the clock rule: when it starts, whether it runs on business hours, what pauses it (for example, waiting on the customer), as the policy states;
- the deadline, with the arithmetic shown so the engineer can check it. When a clock rule depends on data you were not given (such as the ticket's status history), give the deadline both with and without that rule applied and name the missing data;
- the status against now: _met_ (the target event happened before the deadline), _open_ (deadline not yet passed) or _breached_, with time remaining or time over. State the "now" you used: the current time if you have it, otherwise the last thread timestamp, labelled as such.

Done when: each item above is filled from a quoted source or marked `not stated in <source>`, and the deadline (if determinable) is shown with its arithmetic.

### 4. Choose the recommended next action

From the ledger, pick one concrete action for the engineer: usually the cheapest check that would turn the leading _suspected_ cause into _verified_ or rule it out. Name what each outcome of that check would mean. If a commitment or the service-level deadline falls due before the action can finish, add the customer update that has to go out and by when.

Done when: the action is specific enough to start without asking a question, and it is consistent with every pending commitment and the deadline.

### 5. Write the handoff

Fill the template below. Then check it against the ledger:

- every bullet under _Problem_ has a provenance tag and its evidence;
- every ledger attempt appears under _Tried so far_;
- every ledger commitment appears under _Commitments_ with a quote and who made it, and nothing appears there that is not in the ledger;
- every service-level term quotes the policy or account record, or reads `not stated in <source>`.

Done when: all four checks pass.

## Template

```markdown
# Escalation handoff: <case ID>, <customer>

**In one line:** <the problem and the most urgent constraint>

## Problem as currently understood
- [verified] <fact> (evidence: <check and result, who, when>)
- [reported] <fact> (source: <customer, when>)
- [suspected] <theory> (held by: <who>; basis: <why>)
- Conflicts: <source-vs-source disagreements, or "none">

## Tried so far
| What was tried | Who, when | Result |
|---|---|---|

## Commitments to the customer
| Commitment (quoted) | Made by | When | Due | Status |
|---|---|---|---|---|
<or: "No commitments found in the thread.">

## Service level
- Tier: <value> (source)
- Priority/severity: <value> (source)
- Target: <value> (policy clause, quoted)
- Clock rule: <start, hours, pauses> (policy clause)
- Deadline: <timestamp, timezone> (arithmetic: <...>)
- Status: <met | open | breached>, <time remaining or over> as of <now, and how chosen>

## Recommended next action
<the action; what each outcome would mean; any customer update due first>

## Gaps
<missing sources, unanswered questions, facts nobody has checked>
```
