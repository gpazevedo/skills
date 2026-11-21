---
name: expense-claim-review
description: Expense claim review against receipts and a supplied expense policy, giving a verdict per line item and a corrected reimbursement total. Use when the user supplies an expense claim for review or approval.
---

Review an expense claim the way an auditor would: every verdict rests on an **evidence trail**, a receipt detail or a quoted policy clause that a second reviewer could check. The supplied policy is the whole rulebook; every rule you apply is a clause you can quote from it. When the evidence does not settle a line, its verdict is **open** (_needs information_), and the open line carries a question that would settle it.

Inputs: the claim form (line items), the receipts, and the organisation's expense policy. If the claim form or the policy is missing, ask for it before starting; a missing receipt is handled line by line.

## Steps

### 1. Inventory

Number the policy's clauses as written (or by section and paragraph, if unnumbered). List every claimed line item: line number, date, merchant, category, amount, currency. List every receipt.

Done when every claim line has a row and every receipt is listed.

### 2. Match receipts

For each line, find its receipt and compare it on each point of the **receipt checks** below. Record each mismatch.

Done when every line has a matched receipt or is marked _no receipt_, and every receipt is matched to a line or marked _unclaimed_.

### 3. Apply the policy

For each line, find every clause that governs it: eligibility, category, cap, prior approval, time limit, documentation required. Give the verdict:

- **Approve**: the receipt supports the line and the clauses allow it. If a cap applies, approve the capped amount and cite the cap; a per-day or per-trip cap is applied across all the lines it covers, including items inside another bill.
- **Reject**: a quoted clause excludes the item, or the receipt shows it is personal, or the same expense is already approved on another line (reject the later line and name the line it duplicates).
- **Needs information**: the receipt is missing, unreadable or contradicts the line; the clause depends on a fact you do not have (a pre-approval, the business purpose, attendees); or the policy says nothing about this kind of expense. Hold the amount; write the question in step 5.

Done when every line has a verdict, an approved amount (zero for reject, held for needs information), and its evidence trail.

### 4. Total

Work in the reimbursement currency. Recompute the claim form's own total and note any arithmetic difference. Then give three figures: **approved now** (sum of approved amounts), **held** (sum of needs-information lines), and **rejected** (rejected lines plus every amount cut from an approved line by a cap or an excluded item). The corrected total to reimburse is _approved now_; state that it rises by up to the held amount as questions are answered.

A line with no usable exchange rate is held at its foreign amount and listed beside the totals.

Done when approved, held and rejected add up to the recomputed claimed total, apart from any line listed in its foreign amount.

### 5. Questions for the claimant

One question per open line, naming the document or fact that would settle it ("Please send the itemised hotel folio for 3-5 May"). Questions the policy cannot answer and only the approver can (policy silent on the item) go in the summary instead.

Done when every needs-information line has exactly one question, addressed to the claimant or the approver.

### 6. Summary for the approver

Up to five sentences: claimed total, corrected total, the largest rejections and their clauses, what is held and why, and any decision the policy leaves to the approver.

## Receipt checks

- **Amount**: receipt total equals the claimed amount. A card slip without an itemised receipt shows payment, not what was bought.
- **Date**: within the trip or claim period, and inside any submission deadline in the policy.
- **Merchant and payer**: the merchant matches the line; the receipt is in the claimant's name or paid by their card where the policy asks.
- **Itemisation**: scan every item on the receipt for anything a clause excludes or limits (often alcohol, minibar, personal items, upgrades) and cut it from the approved amount, citing the clause.
- **Currency**: convert at the rate the policy specifies, or the rate shown on the receipt or card statement. With neither, the line is open.
- **Duplicates**: the same receipt, or the same expense, claimed on two lines or already covered by another line (a meal inside a hotel bill, a per diem).
- **Tips and fees**: allowed only to the extent a clause allows them.

## Output

```markdown
# Expense claim review: <claimant>, <claim reference or period>

| Line | Date | Item | Claimed | Verdict | Approved | Evidence |
|------|------|------|---------|---------|----------|----------|
| 1 | ... | ... | ... | Approve / Reject / Needs information | ... | Receipt: ...; Policy cl. ...: "..." |

**Claimed (recomputed):** ... (form says ...)
**Approved now (corrected total to reimburse):** ...
**Held pending information:** ...
**Rejected:** ...

## Questions for the claimant
1. Line N: ...

## Summary for the approver
...
```
