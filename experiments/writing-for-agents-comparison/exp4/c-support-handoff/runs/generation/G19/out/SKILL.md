---
name: support-escalation-handoff
description: Handoff for the next-tier engineer from a support case (ticket thread, account record, support policy). Use when escalating, transferring, or summarising a case for tier 2/3.
---

Produce a handoff the next-tier engineer can act on without reopening the thread. Inputs: the ticket thread, the account record, the support policy with its service levels. Missing input: name it in the handoff under Gaps and continue with the rest.

## Evidence grades

Every claim about the problem carries one grade:

- **Reported**: the customer said it.
- **Verified**: support observed it directly (log, reproduction, account record, test result). Name the source.

A customer claim becomes verified only on a support observation; a support agent repeating the customer's claim stays reported.

## Steps

1. **Ledger.** Read the thread message by message. List every message's author, timestamp, and each claim, action, and promise in it. Done when every message appears in the ledger.
2. **Problem.** State the problem as currently understood in one or two sentences. List the evidence behind it, each item graded and sourced (message and timestamp, or record field). Conflicts between reports, or between a report and the record, go in the list as conflicts.
3. **Attempts.** List each thing tried: who, when, what, and result (worked, failed, no result recorded). Done when every action in the ledger is listed or is not an attempt.
4. **Commitments.** List each promise made to the customer: what, who made it, when, quoted words. A promise is a statement of future action or outcome; an apology or an estimate is listed only if phrased as a promise. No commitments found: write "None found in the thread." Ambiguous wording: quote it and mark it ambiguous.
5. **Service level.** From the policy, take the customer's tier or plan as given in the account record, the applicable response and resolution targets, and the clock start. Compute the deadline and time remaining from the stated times, showing the inputs. Quote the policy clause used. Tier, clause, or clock rule missing or unclear: write "Not determinable from the supplied policy" and state what is needed. Pause or exclusion rules apply only where the policy states them.
6. **Next action.** One recommended action, with the reason it follows from the evidence, the owner tier, and the first check to run. Add open questions for the customer, if any, split from questions for engineering.

## Output

Use these headings in this order, each section starting with its answer:

1. Problem and evidence
2. Tried and results
3. Commitments to the customer
4. Service level and deadline
5. Recommended next action
6. Gaps (missing inputs, conflicts, unverified assumptions)

Closing check, done when all hold: each commitment and each service-level term quotes its source; each evidence item has a grade; every date or deadline shows its inputs.
