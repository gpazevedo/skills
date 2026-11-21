---
name: expense-claim-review
description: Reviews an expense claim against the organisation's expense policy and the receipts, giving a verdict per line item, the corrected total, questions for the claimant and an approver summary. Use when asked to review, check, audit or approve an expense claim or reimbursement request.
---

Review a claim from three inputs the user supplies: the **claim form** (the claimed line items), the **receipts**, and the **policy** (the organisation's expense policy). The supplied policy is the whole rulebook: every rule you apply is a clause you can quote from it. Where it is silent, the item is open, and you ask.

Each line item ends with one verdict:

- **Approve**: the receipt matches the item (or the policy waives the receipt for it) and the policy allows it. The approved amount is lower than the claimed amount when a cap applies or the policy excludes part of the item (a tip, alcohol on a meal receipt); cite each clause that reduces it.
- **Reject**: a policy clause excludes the item, or the receipt contradicts the claim (a different amount, date, or merchant that no question could reconcile). Cite the clause or the receipt.
- **Needs information**: the evidence does not settle it. This is the verdict for a missing or illegible receipt, a receipt that only partly matches, a policy that is silent or ambiguous on the item, or a fact the policy depends on that the inputs do not state (attendees, business purpose, pre-approval, exchange rate). An open item is a finished verdict, paired with the question that would settle it.

Every verdict carries its **evidence**: the policy clause (number or heading, plus the words that decide it) and the receipt (which one, and what it shows). A verdict with no evidence line is not done.

## Steps

1. **Inventory.** Number every claimed line item, recording date, description, category, amount and currency as the claim form states them. Label every receipt. Locate the policy's clauses and their numbers or headings. Done when every line item has a number and every receipt a label. If the policy or the claim form is missing, ask the user for it and stop here.

2. **Match receipts.** Pair each line item with its receipt. Compare amount, date, merchant and what was bought, reading the receipt's itemised lines: a receipt total that differs from the claim may still match once its lines are separated. Record each mismatch. Note any receipt used for two items, and any receipt that matches no item. Done when every line item is either paired, with its mismatches listed, or marked "no receipt".

3. **Apply the policy.** For each line item, read every clause that could bear on it: eligible categories, exclusions, caps and per-day limits, receipt requirements, pre-approval, attendee or purpose requirements, submission deadlines, currency conversion. Done when every line item has a verdict, an approved amount (zero for reject and needs information), and its evidence.

4. **Total.** Sum the approved amounts into the corrected total to reimburse, in the currency the policy pays in. Show the arithmetic: claimed total, each reduction or exclusion with its line number, the result. Report the amount held on open items separately; it stays out of the total. Done when the figures add up line by line.

5. **Questions.** Write one question per open item, addressed to the claimant, naming the line number and stating exactly what answer or document would settle it. Add a question for each unmatched receipt. Done when every open item has its question.

6. **Summary.** Write three to five sentences for the approver: the corrected total against the claimed total, the main reasons for reductions and rejections, and what is pending on the claimant.

## Output

```markdown
# Expense claim review: <claimant>, <claim reference or period>

## Line items

| # | Date | Description | Claimed | Verdict | Approved | Evidence |
|---|------|-------------|---------|---------|----------|----------|
| 1 | ... | ... | ... | Approve / Reject / Needs information | ... | Policy <clause>: "<deciding words>"; Receipt <label>: <what it shows> |

## Corrected total

Claimed: <amount>
- Line <n>: <reduction or exclusion and reason>
Approved to reimburse: <amount>
Held pending information: <amount> (lines <n, n>)

## Questions for the claimant

1. Line <n>: <question, and what would settle it>

## Summary for the approver

<three to five sentences>
```

Before returning the review, check it against the inventory: every line item appears in the table with a verdict and evidence, the total matches the table, and every "Needs information" row has a question.
