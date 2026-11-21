---
name: support-escalation-handoff
description: Escalation handoff for a support case. Use when a support ticket must pass to a next-tier engineer, or the user asks to escalate a case or brief tier 2/3 on it.
---

Turn a support case into a handoff the next-tier engineer can act on without rereading the thread. The case has three inputs: the **ticket thread**, the customer's **account record**, and the **support policy** with its service levels. Every statement in the handoff carries its **provenance**: the line in those inputs it came from.

## Provenance tags

Tag every fact about the problem with one of:

- **Reported**: the customer said it. A support agent repeating or paraphrasing the customer's claim keeps it Reported.
- **Verified**: support observed it directly (reproduced it, read it in logs or the account record, saw it in a screenshot or test). Cite who verified it and where in the thread.
- **Hypothesis**: someone's explanation not yet confirmed. Name whose hypothesis it is.

When in doubt between Reported and Verified, use Reported: the engineer can re-verify cheaply, but a false Verified sends them down the wrong path.

## Steps

1. **Check the inputs.** Confirm the thread, account record and policy are all present. If one is missing, tell the user which one and what it blocks (no policy: no service-level terms; no account record: no tier or entitlements). If they want to go ahead, write "Not determinable: <input> not supplied" in each section it blocks. Done when each input is either in hand or its gap is named.

2. **Build the fact list.** Read the thread start to finish and list every claim about the problem (symptoms, scope, environment, timing, error messages, business impact) with its tag and source message. Done when every message in the thread has been read and every problem claim in it appears in the list.

3. **Log the attempts.** For each troubleshooting action: what was done, who did it, when, and the result. A result the thread leaves out is written "result not recorded". Done when every action in the thread has a row.

4. **Extract the commitments.** A commitment is a promise made to the customer, in a customer-facing message, by someone on the support side: a callback, an update by a time, a fix, a workaround, a credit, an escalation. Record each at the strength it was made: "I'll check with billing about a credit" is a commitment to check, and the credit itself stays a request. For each, quote the words, name who made it and when, and give its status (met, open, overdue). Customer requests that support never agreed to go in a separate "Requested, not committed" list. Done when every customer-facing support message has been checked for promises; if none exist, write "No commitments found in the thread".

5. **Work out the service level.** From the account record take the customer's tier or plan; from the thread take the case priority and who set it. Then quote, from the policy, each target that applies (first response, update cadence, resolution), the event that starts each clock, and any pause or business-hours rule. For each target, compute its deadline from those quoted terms and the thread timestamps, showing the arithmetic, and give its status: met, within target, at risk, or breached. State the reference time you measured against. Every term comes from a policy quote; where the policy is silent, write "Policy does not state <term>" and stop that calculation there. Where a term is ambiguous (a time zone, what counts as a "business day"), quote it and state the reading you used. Done when every applicable target has a deadline and status tracing to quoted policy text and thread timestamps, or a named gap.

6. **State the problem and the next action.** Write the problem as currently understood in two to four sentences, built on Verified facts, with Reported and Hypothesis material labelled as such. Then list the open questions the evidence leaves. Recommend one next action: the specific check or change that best narrows the problem, who should do it, and by when, set against the service-level deadline and any open commitment. Done when the next action names an owner and a time.

7. **Trace-check.** Before handing over, walk the draft: every Verified fact cites its source, every commitment quotes its message, every service-level term quotes the policy. Any line without a source moves to Reported, moves to "Not determinable", or is cut. Done when every line in the handoff traces to one of the three inputs or is marked as your own recommendation.

## Handoff format

```markdown
# Escalation handoff: <case ID> <one-line summary>

**Customer:** <name>, <tier/plan> | **Priority:** <priority> (set by <who>)
**Service level:** <worst status>, next deadline <timestamp> (<time remaining or overdue by>)
**Open commitments:** <count>, earliest due <timestamp>

## Problem as currently understood
<2-4 sentences>

| Fact | Tag | Source |
|---|---|---|

**Open questions:** <what the evidence does not yet settle>

## What has been tried
| Action | By | When | Result |
|---|---|---|---|

## Commitments to the customer
| Commitment (quoted) | Made by | When | Status |
|---|---|---|---|

**Requested, not committed:** <list or "none">

## Service level
Measured at <reference time>. Readings used for ambiguous terms: <list or "none">

| Target (policy quote) | Clock start | Deadline (arithmetic) | Status |
|---|---|---|---|

Pauses: <policy quote or "Policy does not state">

## Recommended next action
<action>, owner <who>, by <time>, because <reason tied to evidence, deadline or commitment>
```
