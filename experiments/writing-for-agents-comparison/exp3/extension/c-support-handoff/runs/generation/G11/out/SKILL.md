---
name: support-escalation-handoff
description: Escalation handoff built from a support case's ticket thread, account record and support policy. Use when escalating a support ticket to a next-tier engineer.
---

Turn one support case into a handoff the next-tier engineer can act on without rereading the thread. The case arrives as three sources: the **ticket thread**, the customer's **account record**, and the **support policy** with its service levels. Every line of the handoff traces to a place in one of them.

## Provenance

Each fact about the problem carries one status, chosen by who established it:

- **Verified**: support confirmed it by observation (reproduced it, read a log, checked a system, saw it in the account record). State how it was confirmed.
- **Reported**: the customer says it, and no one in support has confirmed it. A customer's claim stays Reported however confident or detailed it is, and however often it is repeated.
- **Hypothesis**: a support agent's untested explanation. It becomes Verified only when the thread shows the test and its result.

Each line also carries a **cite**: the thread message (sender and timestamp), the account record field, or the policy clause it comes from. A fact with no cite has no place in the handoff; record the gap instead (see step 5).

## Steps

1. **Read every source in full.** Read every message in the thread, including internal notes, in order. Done when you can name each message's sender, time and purpose. If any of the three sources is missing, ask the user for it before going on; if they cannot supply it, carry on and record the missing source as a gap.

2. **Build the problem statement.** Write the problem as currently understood in two or three sentences, then list the facts behind it, each with its status and cite. Where the customer's account and support's findings disagree, list both and name the disagreement. Done when every symptom, error, scope detail (who, which systems, since when) and impact claim in the thread appears with a status.

3. **List what has been tried.** One entry per attempt: what was done, who did it, when, and the result as the thread records it. An attempt with no recorded result gets the result "not recorded". Done when every action taken by support or the customer in the thread has an entry.

4. **Collect commitments.** A commitment is anything said to the customer that promises an action, a time, an outcome, a credit or a contact: "we will", "you'll hear back by", "I'll escalate", "we'll refund". For each one, quote the words verbatim, and give who made it, their role, the message it is in, any deadline it sets, and its state: Kept, Open (deadline not yet passed), or Missed. Where a commitment exceeds what the policy allows the person who made it (a credit only an account manager may grant, a deadline shorter than the policy's), cite the clause beside it. Customer requests and internal notes are context, not commitments. Done when every message sent to the customer has been checked for commitments; if none exist, write "No commitments found in the thread."

5. **Work out the service-level status.** Every term comes from the policy text and the account record, quoted with its clause:
   - Find the customer's tier or plan in the account record, and the policy clauses that apply to it and to the case's priority or severity.
   - For each clock the policy defines (first response, update interval, resolution, or whatever it names), give the start event and its timestamp from the thread, any pause or business-hours rule the policy states, the deadline, and the arithmetic that produced it.
   - Give the status of each clock: met, on track, at risk, or breached, measured against the current time. Ask the user for the current time and time zone if you do not have them.
   Whenever the sources leave a term open (tier not in the record, severity never set, a pause rule the policy does not state), write "Not determinable" with the missing input named. If one missing input blocks the calculation, also give the deadline for each value the policy allows for it, labelled conditional ("if Sev2: ..."). Done when every clock in the applicable clauses has a deadline and status, or a "Not determinable" with its reason.

6. **Recommend the next action.** One action for the next-tier engineer, the evidence that points to it, and what its result would settle. Add the most urgent deadline it must beat: the nearest open commitment or service-level clock. If a fact the action depends on is only Reported or Hypothesis, make confirming it part of the action.

7. **Audit, then write the handoff.** Check every line of the draft against the sources: each fact has a status and cite, each commitment is a verbatim quote that exists in the thread, each service-level term is a quote that exists in the policy or record. Rewrite or remove any line that fails. Done when no line fails. Then write the handoff in the format below.

## Handoff format

```markdown
# Escalation handoff: <case ID> <one-line problem>

**Customer:** <name, account ID, tier/plan>   **Severity/priority:** <value and cite, or Not determinable>
**Most urgent deadline:** <what, when, cite>

## Problem as currently understood
<two or three sentences>

| Fact | Status | How established / cite |
|---|---|---|
| ... | Verified / Reported / Hypothesis | ... |

**Open disagreements:** <customer account vs support findings, or "None">

## What has been tried
| When | Who | Action | Result | Cite |
|---|---|---|---|---|

## Commitments to the customer
| Commitment (verbatim) | Made by (role) | When / cite | Deadline | Kept / Open / Missed |
|---|---|---|---|---|

## Service-level status
| Clock | Policy clause (quoted) | Started | Deadline (with arithmetic) | Status |
|---|---|---|---|---|

## Recommended next action
<action, the evidence behind it, what its result would settle, deadline it must beat>

## Gaps
<missing sources, unrecorded results, Not determinable terms, each with what would close it; or "None">
```
