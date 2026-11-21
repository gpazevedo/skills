---
name: support-escalation-handoff
description: Escalation handoff for the next-tier engineer, built from a support case the user supplies (ticket thread, account record, support policy). Use when escalating a support ticket to a higher tier or engineering.
---

# Support escalation handoff

Turn one support case into a handoff the next-tier engineer can act on without rereading the thread. Every line of the handoff carries its **provenance**: the message, account field or policy clause it came from.

Two labels run through the whole skill:

- **Reported**: the customer said it. It stays _reported_ however often it is repeated.
- **Verified**: someone on the support side checked it (reproduced it, read it in logs, saw it in the account record, tested a fix) and the thread or record says how. Name the check.

A support agent's guess that nothing has confirmed is **suspected**, a third label used the same way.

## Steps

### 1. Collect the case

Confirm you have all three inputs: the ticket thread, the customer's account record, and the support policy with its service levels. Note the current date and time, with time zone, for the service-level check; take it from the user or the environment.

Done when all three inputs are in hand, or the user has told you to proceed without one. A missing input leaves its sections reading "not supplied", never filled from general knowledge.

### 2. Build the ledger

Read the thread in order, every message, including internal notes. Record each item in a working **ledger**, with its source (sender, timestamp) and label:

- **Problem facts**: symptoms, error text, scope (users, regions, features affected), environment, versions, first occurrence, business impact. Label each _reported_, _verified_ or _suspected_. When support verifies something the customer reported, keep one entry and upgrade its label, citing both messages. When the check confirms only part of a claim (one user of the "all users" reported, one region of three), split it into a _verified_ entry for the part checked and a _reported_ entry for the rest.
- **Attempts**: each thing tried (by support or by the customer), who did it, when, and the result as recorded. Where the thread gives no result, write "result not recorded".
- **Commitments**: each promise made _to the customer_: a callback or update time, a fix, a workaround, a credit, an escalation, a named contact. Quote it word for word, with who made it and when. Promises in the account record (for example a contract note) count too. Plans in internal notes the customer never saw go under attempts or open questions, not commitments.
- **Contradictions**: places where messages, or the thread and the account record, disagree. Keep both versions.

Done when every message has been read and every problem fact, attempt, commitment and contradiction in it has a ledger entry with a source.

### 3. Work out the service level

From the account record, find the customer's plan or tier and the ticket's priority or severity. From the policy, find the clauses that apply to that tier and priority, and quote them. Then work out, using the policy's own definitions:

- which clock applies (first response, update interval, resolution, or whatever the policy defines) and the event that starts it;
- whether business hours, holidays or a paused clock (for example while waiting on the customer) change the count, if the policy says so;
- the deadline, as a date and time with time zone, and the status now: _met_, _running_ (with time remaining), or _breached_ (with time since breach).

Show the arithmetic in one line per clock. Where the tier, the priority, or the clause is ambiguous or missing, state the gap and give the deadline under each reading, rather than choosing one.

Done when every clock the policy defines for this tier has a deadline and a status traced to a quoted clause, or a stated gap.

### 4. Choose the next action

Name one recommended next action for the engineer: the step that best closes the gap between what is _reported_ and what is _verified_, or tests the leading _suspected_ cause, ordered against the nearest deadline or due commitment. Add what result would confirm or rule it out. List further open questions beneath it, if any.

Done when the action is concrete enough to start now (what to check, where, with what), and its link to the evidence is stated.

### 5. Write the handoff

Fill in the template below from the ledger. Then trace every line back to a ledger entry, a policy clause or an account field; rewrite or remove any line that has no source. Every commitment and service-level term in the handoff is quoted from the case; where the case is silent, the handoff says "not stated".

Done when every line traces to a source and every ledger entry appears in the handoff or was deliberately left out as irrelevant to the problem.

## Handoff template

Deliver the handoff in the chat as Markdown, unless the user asks for a file.

```markdown
# Escalation handoff: <ticket ID> <short title>

**Customer:** <name, account ID, plan/tier>  **Priority:** <as recorded>  **Prepared:** <date, time, zone>

## Service level
| Clock | Policy clause | Started | Deadline | Status |
|---|---|---|---|---|
<one row per clock; arithmetic or gaps in a line beneath the table>

## Problem as currently understood
<two or three sentences: the most likely account of the problem, built on verified facts first>

| Fact | Status | Evidence |
|---|---|---|
<one row per problem fact; Status is Verified, Reported or Suspected; Evidence names the message, check or record>

Contradictions: <each disagreement, both versions, sources; or "none found">

## What has been tried
| When | Who | Action | Result |
|---|---|---|---|

## Commitments to the customer
| When | Made by | Commitment (quoted) | Due | State |
|---|---|---|---|---|
<State is met, open, or overdue; "none made" if the case has none>

## Recommended next action
<the action, what result would confirm or rule it out, and the deadline or commitment it is racing>

Open questions: <list>
```
