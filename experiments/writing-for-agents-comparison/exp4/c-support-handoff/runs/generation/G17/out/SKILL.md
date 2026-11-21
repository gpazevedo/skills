---
name: support-escalation-handoff
description: Handoff for the next-tier engineer from a support case. Use when escalating or transferring a ticket, given its thread, the customer's account record and the support policy.
---

Produce a handoff the next-tier engineer can act on without reopening the thread. Every claim carries its **provenance**: _reported_ (the customer said it) or _verified_ (support observed it in logs, the account record, a reproduction, or a policy text). Reported stays reported until a source in the case confirms it.

## Steps

1. **Read all three inputs in full**: the thread, the account record, the policy. Done when you can name, for every message in the thread, who wrote it and when. If an input is missing, say so in the handoff's Gaps section and carry on with what exists.

2. **Extract commitments.** A commitment is anything promised to the customer: a fix, a date, a callback, a credit, an exception, a workaround. Done when every message by support or an agent has been checked for one. Record each as: the promise in the author's words, who made it, when, and whether it was kept. Quote; do not paraphrase into something firmer or softer. A vague promise ("we'll look into it") is recorded as exactly that.

3. **Establish the service-level status.** Find the customer's tier in the account record, then the matching terms in the policy. Done when the status line cites the policy clause for each figure it uses (response time, resolution time, severity definition), the clock start and the resulting deadline, with the arithmetic shown. Where the policy or record lacks a term, the status line says "not stated in the supplied policy" for that term and gives no deadline for it. Use only terms present in the policy text.

4. **Build the problem statement** from the evidence. Done when each statement is tagged _reported_ or _verified_, with its source (message, log line, record field). Keep the customer's symptoms and support's diagnosis apart; a diagnosis nobody tested is a _hypothesis_.

5. **List what was tried**: each action, its result, and who did it. Done when every troubleshooting action in the thread appears, including failures and actions with no recorded result (marked "result not recorded").

6. **Recommend the next action**: one primary action, then alternatives if any. Done when the recommendation names an owner role, follows from the evidence above, and states what it would confirm or rule out. Mark which open commitment or deadline it serves.

## Output

Use these headings in this order:

1. **Summary**: two sentences: the problem, the urgency.
2. **Problem and evidence**: statements tagged _reported_ / _verified_ / _hypothesis_, each with its source.
3. **Tried so far**: action, result, who.
4. **Commitments to the customer**: quote, author, date, status.
5. **Service level**: tier, clause, clock start, deadline, time remaining or breached.
6. **Recommended next action**
7. **Gaps and conflicts**: missing inputs, contradictions between the customer's account and the record, terms the policy leaves out.

Write for a reader who has seen none of the thread: name the customer, the account, and the product area in the Summary. Dates are absolute, with timezone where the thread gives one.
