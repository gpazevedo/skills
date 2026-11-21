---
name: support-escalation-handoff
description: Handoff for a next-tier engineer from a support case. Use when escalating a ticket, given a ticket thread, account record and support policy.
---

Produce a handoff the next-tier engineer can act on without opening the thread. Inputs: the ticket thread, the account record, the support policy with its service levels. Every claim in the handoff traces to one of these three sources.

## Evidence grades

Grade each statement of fact by its source:

- **Reported**: the customer said it (thread, customer messages). Includes the customer's account of what they did, saw, or were promised.
- **Verified**: support or a system confirmed it (logs, reproduction, account record fields, policy text, a support-side test result). Name the confirming source.

Customer-reported stays _reported_ until a support-side source confirms it. A customer quote that matches the account record is verified by the record, so cite the record. Where sources conflict, state both and mark the conflict.

## Steps

1. **Read all three inputs fully.** Done when you can name the first and last message in the thread, the account's plan and relevant dates, and the policy clause governing this case's severity and plan.
2. **Build the commitment ledger.** One row per commitment found in the thread: what was promised, who made it (name and role as the thread shows), when, and the exact quoted words. A commitment is a promise of an action, outcome, date, credit, or exception made to the customer. Done when every outbound message has been scanned and each row quotes its source line. Leave out anything not stated: no inferred promises, no policy defaults presented as promises.
3. **Establish service-level status.** From the policy and account plan, find the applicable response and resolution terms, the clock start, and the deadline. Copy terms as the policy words them. Done when the output holds the term, its source clause, the clock start, the deadline, and time remaining or breach status as of the latest thread timestamp. If the policy, plan, severity, or clock start is missing or ambiguous, write `Not determinable:` plus what is missing. Never fill the gap with a typical value.
4. **Reconstruct the problem and the attempts.** State the problem as currently understood in a few sentences, each supported by cited evidence graded _reported_ or _verified_. List every attempt in order: action, who did it, result. Done when no thread action is missing from the list and each result is stated (worked, failed, no response, unknown).
5. **Recommend the next action.** One primary action, the reason it follows from the evidence, and what it must satisfy (open commitments, the deadline). Name unverified assumptions it rests on and the check that would settle each.
6. **Check before delivering.** Done when each of these holds: every commitment row has a quote; every service-level term has a clause or `Not determinable`; every problem statement carries a grade; the recommended action addresses each open commitment.

## Output

Use these headings in this order.

```
# Handoff: <ticket id or subject>

## Problem
<understanding, one claim per line, each tagged [Reported] or [Verified: source]>

## Open questions
<what remains unverified, and how to verify>

## Attempts
<numbered: action, by whom, result>

## Commitments to the customer
| Commitment | Made by | When | Quote |

## Service level
Term: <policy wording> (<clause>)
Clock start: ...
Deadline: ...
Status: <time remaining or breached, as of timestamp>

## Recommended next action
<action, reason, what it must satisfy, assumptions>
```

When a section has no content, write `None found in the thread` under its heading so the engineer knows it was checked.
