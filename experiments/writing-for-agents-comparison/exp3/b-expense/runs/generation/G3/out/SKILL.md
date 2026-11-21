---
name: expense-claim-review
description: Expense claim review. Checks each claimed line item against its receipt and the supplied expense policy, then writes per-item verdicts, a corrected total, claimant questions and an approver summary. Use when the user supplies an expense claim to review.
---

# Expense claim review

The user supplies three inputs: the **claim form** (the line items), the **receipts**, and the organisation's **expense policy**. The supplied policy is the whole rulebook: a rule exists for this review only if you can quote its clause. Every verdict rests on **evidence**, meaning a quoted policy clause, a receipt detail, or both, cited where the verdict appears.

If one of the three inputs is missing, ask the user for it before starting.

## Verdicts

Each line item gets exactly one verdict and an approved amount.

- **Approve**: the receipt matches the item (or the policy waives the receipt for this amount) and a clause permits it. The approved amount can be lower than claimed (a cap, a lower receipt total, a personal item removed from an itemised receipt); cite the clause or receipt detail for each reduction.
- **Reject**: a quoted clause excludes the item, or the receipt shows the item is a duplicate of another claimed line. Approved amount 0.
- **Needs information**: the evidence leaves the verdict **open**. Approved amount 0, the claimed amount held. Where a cap or exclusion will still apply once the point is settled, say so in the evidence. Typical cases: no receipt where the policy requires one, an unreadable receipt, a receipt whose date, merchant or amount conflicts with the claim, a required business purpose or attendee list absent, a foreign-currency item with no conversion rate in the supplied material, or a category no clause covers.

When two verdicts both remain plausible, the verdict is open. Your own sense of what is reasonable or customary carries no weight: an approval or rejection you cannot pin to a clause or receipt detail is open.

## Steps

### 1. Inventory

Number every line item on the claim form and record its date, merchant, category, amount and currency. Pair each receipt with its line item. Note the policy clauses by their numbers or headings so you can cite them; where the policy is unnumbered, cite a short quoted phrase.

Done when every line item is paired with a receipt or marked "no receipt", and every receipt is paired with a line item or listed as unmatched.

### 2. Check each line item

Run both checklists on every line item, then assign its verdict.

Receipt checks:
- Amount: the receipt total, including tax and tip, against the claimed amount.
- Date and merchant: both match the claim line.
- Itemisation: personal or excluded items mixed in with business ones.
- Duplicates: the same receipt, or the same expense, behind more than one line.
- Payer: the receipt shows the claimant paid, where the policy requires it.

Policy checks:
- The clause that permits the category, or the clause that excludes it.
- Caps and limits: per item, per day, per person, per trip.
- Conditions: receipt thresholds, pre-approval, business purpose, attendees, submission deadline, conversion rule.

Done when every line item has a verdict, an approved amount and its cited evidence.

### 3. Total

Corrected total = the sum of approved amounts. Then **reconcile**: claimed total = corrected total + reductions on approved items + rejected amounts + held amounts. Show each figure.

Done when the four figures sum exactly to the claimed total.

### 4. Questions for the claimant

Write one question for each open point, naming the line item and the specific document or fact that would settle it (for example, "Line 4: please supply the itemised receipt showing the attendees").

Done when every needs-information item has at least one question. A category no clause covers is a policy gap for the approver, so it goes in the summary as well as getting a question about the business purpose.

### 5. Summary for the approver

Three to five sentences: the corrected total and the held amount, the main reasons for reductions and rejections, and any policy gap the approver must rule on.

## Output

```
# Expense claim review: <claimant>, <claim reference or period>

## Line items
| # | Date | Merchant | Claimed | Verdict | Approved | Evidence |
|---|------|----------|---------|---------|----------|----------|

## Total
Claimed: <amount>
Reductions on approved items: <amount>
Rejected: <amount>
Held (needs information): <amount>
Corrected total to reimburse: <amount>

## Questions for the claimant
1. Line <n>: <question>

## Summary for the approver
<three to five sentences>
```

Unmatched receipts go in a short list under the line-item table. State amounts in the claim's reimbursement currency, with any conversion and its source shown in the Evidence column.
