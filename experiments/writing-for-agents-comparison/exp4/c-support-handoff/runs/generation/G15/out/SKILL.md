---
name: support-escalation-handoff
description: Handoff for the next-tier engineer from a support case (ticket thread, account record, support policy). Use when escalating, transferring, or summarising a support case for another tier.
---

Produce a handoff the next-tier engineer can act on without reopening the thread. Inputs: the ticket thread, the customer's account record, the support policy with its service levels. If one is missing, say so in the handoff and proceed with what exists.

Two leading words govern the work:

- **Reported**: the customer said it, or a support message asserts it, with no check shown.
- **Verified**: support observed it directly (logs, reproduction, account record, policy text). Cite the source.

Anything not Verified is Reported, however confident the thread sounds.

## Steps

1. **Read all three inputs end to end.** Done when you can name, for each thread message, who wrote it and when.
2. **Build the timeline.** One line per event: date, actor (customer, named agent, system), what happened. Done when every message and action maps to a line.
3. **Extract commitments.** Each is something promised to the customer: a fix date, a callback, a refund, a workaround, a credit. Record the exact words, the person who said it, and the date. Done when every promise-like sentence in the thread is either logged or judged not a promise. A commitment appears only if the thread contains it; when ownership or wording is unclear, write "unclear" and quote the text.
4. **Determine service-level status.** Take terms (tier, response and resolution targets, clock start, pause conditions) only from the policy and account record, quoting the clause. Compute the deadline from the clock start and show the arithmetic. When a term or the clock start is missing or ambiguous, write "not stated in provided material" and name what is needed to settle it. Done when status reads one of: met, on track, at risk, breached, or undetermined, with the deadline or the reason it is undetermined.
5. **Assemble the problem statement.** Separate what the customer Reports from what support Verified, each Verified item with its source. Done when no claim sits unlabelled.
6. **List attempts.** Each: action, who, result (worked, failed, inconclusive, unknown), evidence. Done when every action in the timeline that tried to fix or diagnose appears.
7. **Recommend one next action** for the receiving engineer, the reason it follows from the evidence, and anything to do before the deadline. Name open questions for the customer if they block it.

## Output

Use these headings in this order, so the engineer can scan:

1. **Summary** (two sentences: problem, urgency)
2. **Problem as understood** (Reported / Verified, with sources)
3. **Tried so far** (table: action, by, result)
4. **Commitments to the customer** (quote, who, when)
5. **Service level** (status, clause, deadline, arithmetic)
6. **Recommended next action**
7. **Gaps** (missing inputs, unclear terms, unverified claims that matter)

When a section has nothing, write "None found in the provided material".
