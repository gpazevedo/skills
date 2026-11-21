---
name: support-escalation-handoff
description: Escalation handoff brief for the next-tier engineer, built from a support case (ticket thread, account record, support policy). Use when a support case is escalated or handed to the next tier.
---

Turn one support case into a handoff the next-tier engineer can act on without rereading the thread. The case is three inputs: the **thread**, the **account record**, and the **policy**. Every line of the handoff traces to one of them; the handoff is a **ledger** of the case, never a story about it.

## Provenance tags

Every claim about the problem, its cause, or the customer's environment carries one tag:

- **[reported]**: the customer said it; no one at support has confirmed it.
- **[suspected]**: a support agent proposed it as a hypothesis; nothing in the case confirms it.
- **[verified]**: a support agent observed, reproduced, or checked it (logs, screenshots they inspected, a test they ran), or the account record states it.

Each tag carries its **source**: author and timestamp of the message, or "account record". A claim moves to [verified] only when the case shows the check that confirmed it. When the customer and support disagree, record both, each with its own tag.

## Steps

1. **Read the case.** Read the whole thread in order, then the account record, then the policy. Note any of the three inputs that was not supplied, and note the reference time "now": the time the user gives, or else the timestamp of the last thread message, saying which. Done when every message has been read and the missing inputs and "now" are written down.

2. **Build the ledger.** Walk the thread message by message and extract four kinds of entry, each tagged and sourced:
   - **Claims** about the symptom, scope, impact, environment, and cause.
   - **Attempts**: each thing tried (by the customer or support), who tried it, and the result. An attempt with no reported result gets "result not recorded".
   - **Commitments**: any statement to the customer promising an action, a time, a fix, a credit, or a contact. Quote it verbatim with author and timestamp. A commitment exists only where the thread contains the words that made it; a customer's expectation or a promise the customer attributes to the company is a claim, recorded as [reported]. Where the policy limits what was promised (who may grant credits, what support may guarantee), quote that clause beside the commitment.
   - **Open questions**: what the customer or support asked that has no answer yet.

   Done when every message has been checked against all four kinds and every entry has a tag or quote and a source.

3. **Work out the service level.** Find the policy clause that applies, matching on what the account record says (plan, tier, contract) and on the case's priority or severity. Quote the clause. From it, name the clock (first response, update interval, resolution), whether it runs in business or calendar hours, its start event and timestamp, and compute the deadline, showing the arithmetic. Status is one of: **met**, **open** (with time remaining at "now"), **breached**, or **cannot determine**, plus any status the policy itself defines (such as "at risk"), quoted. A term the computation needs and the inputs lack (tier, priority, business hours, time zone) is a **missing term**: name it. When the status comes out the same under every plausible value of the missing term, give that status and name the term; otherwise the status is **cannot determine**. Done when each applicable clock has a quoted clause, a deadline or a named missing term, and a status.

4. **Choose the next action.** Pick the single action that most advances the case: usually the most discriminating test of the leading [suspected] or [reported] cause that the attempts have not yet run, or else the earliest unmet commitment or service-level deadline. Name who should do it and by when, and the ledger entries it rests on. Done when the action names an owner, a time, and its evidence.

5. **Write the handoff** in the template below, then run a **trace pass**: for each line, point to its source in the case. Rewrite or delete any line that has no source. Done when every line traces.

## Handoff template

```markdown
# Escalation handoff: <case id> <one-line summary>

Reference time ("now"): <timestamp> (<given by user | last thread message>)
Inputs missing: <none | which>

## Problem as currently understood
<Two to four sentences stating the working understanding, then:>
- <claim> [verified | reported | suspected] (<source>)
- ...
Conflicts: <customer vs support disagreements, each side tagged, or "none">

## Tried so far
| When | Who | What | Result |
|------|-----|------|--------|

## Commitments to the customer
| When | Made by | Verbatim commitment | Status (met / pending / overdue) | Policy note |
|------|---------|---------------------|----------------------------------|-------------|
<or "None found in the thread.">

## Service level
<One block per applicable clock:>
- Clause: "<quoted policy text>"
- Clock: <which>, <business | calendar> hours, started <event, timestamp>
- Deadline: <timestamp> (<arithmetic>)
- Status: <met | open, time remaining | breached | cannot determine | policy-defined status>; missing terms: <none | which>

## Open questions
- <question> (asked by <who>, <when>)

## Recommended next action
<Action>, owner <who>, by <when>. Rests on: <ledger entries>.
```

A section with nothing to record says so in one line, so the reader can tell "none" from "not checked".
