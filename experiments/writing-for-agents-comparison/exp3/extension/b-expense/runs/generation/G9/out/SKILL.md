---
name: expense-claim-review
description: Expense claim review against a supplied expense policy and receipts, giving a verdict per line item, the corrected reimbursement total, questions for the claimant and an approver summary. Use when asked to review, check or approve an expense claim or reimbursement request.
---

Review an expense claim using three inputs the user supplies: the **claim form** (the claimed line items), the **receipts**, and the organisation's **expense policy**. Start once you hold all three; if one is missing, ask for it and stop there.

The supplied policy is the whole rulebook. Every rule you apply carries a clause reference from it; a judgement you cannot tie to a clause is a question, not a ruling. Every claimed amount is backed by receipt evidence you can point at.

## Verdicts

Each line item gets exactly one verdict:

- **Approve**: the receipt supports the item (amount, date, merchant, what was bought), or the item falls under a clause that accepts something else in place of a receipt, and a policy clause allows the expense. When a clause caps the item or excludes part of it (a capped meal, wine on a dinner bill), approve the remaining amount and cite each clause that cut it.
- **Reject**: a policy clause excludes the item, or the receipt shows it is something other than what was claimed. Cite the clause or the receipt detail.
- **Needs information**: the evidence does not settle it. This is the verdict whenever you would otherwise be guessing: no matching receipt where the policy requires one, an unreadable or partial receipt, an amount or date that does not match, a currency with no conversion basis in the policy, a missing pre-approval the policy requires, or a policy silent on whether this kind of expense is reimbursable. Name exactly what would settle it.

Settle a verdict on the evidence in front of you. A plausible story about what the claimant probably meant leaves the verdict open.

## Steps

1. **Inventory.** Number every claimed line item as it appears on the claim form (date, description, category, amount, currency). Label every receipt. Note the policy's clauses by their numbers or headings. Done when every line item and every receipt has a label, and you have checked whether the line items sum to the total the form states.

2. **Match receipts.** For each line item, find its receipt and compare amount, date, merchant, currency, item description and payer. Record each mismatch. Flag a receipt used for more than one item, a line item with no receipt, and a receipt with no line item. Done when every line item is matched to a receipt or marked as unmatched, and every receipt is accounted for.

3. **Apply the policy.** For each line item, find every clause that bears on it: eligible categories, per-item or daily caps, receipt requirements, time limits for submitting, pre-approval thresholds, excluded items, conversion rules. Done when each line item lists the clauses that bear on it, or records that the policy is silent on it.

4. **Rule.** Give each line item its verdict, approved amount and evidence (the clause and the receipt detail it rests on). Done when every line item has a verdict with evidence; an item without one is not done.

5. **Total.** Corrected total to reimburse = the sum of approved amounts. Report beside it the rejected amount (rejected items plus the amounts cut from approved items) and the pending amount (items needing information, counted at zero until settled). Done when approved + rejected + pending equals the claimed total; if it does not, find the line that breaks the sum before going on.

6. **Questions for the claimant.** Write one question per needs-information item that the claimant can answer, each naming the line item and the document or fact that would settle it. Questions about policy gaps go to the approver in the summary instead.

7. **Approver summary.** Write at most five sentences: the claimed and corrected totals, how many items fall under each verdict, the largest adjustments and why, and any policy gap or pattern (a duplicated receipt, a total that does not add up) the approver must decide.

## Output

```markdown
# Expense claim review: <claimant>, <claim reference or period>

## Approver summary
<step 7>

## Line items
| # | Date | Description | Claimed | Verdict | Approved | Evidence |
|---|------|-------------|---------|---------|----------|----------|
| 1 | ... | ... | ... | Approve / Reject / Needs information | ... | Clause <ref>; Receipt <label>: <detail> |

## Total
- Claimed: <amount>
- Approved (corrected total to reimburse): <amount>
- Rejected: <amount>
- Pending information: <amount>

## Questions for the claimant
1. Item <#>: <question>

## Other findings
<unmatched receipts, form total mismatches, policy gaps; omit the section if none>
```

Show amounts in the claim's currency, with the currency code on every total.
