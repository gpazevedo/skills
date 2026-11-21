---
name: expense-claim-review
description: Expense claim review against the organisation's own policy and the claim's receipts, giving a verdict per line item, the corrected total, questions for the claimant and a summary for the approver. Use when a user supplies an expense claim to review or approve.
---

# Expense claim review

You review one expense claim for the person who will approve it, and stop when the review, in the [output format](#output-format), is delivered.

## Inputs

- **Claim form**: the claimed line items, each with a date, description, amount and currency.
- **Receipts**: one or more per line item.
- **Expense policy**: the organisation's rules.

If the claim form or the policy is missing, ask for it and stop. If no receipts are supplied at all, ask whether they were left out; if the user confirms there are none, review each line item as having no receipt.

## Evidence and verdicts

**Evidence** is either a policy clause, cited by its number or heading with the deciding words quoted, or a fact read from a specific receipt, cited by its label (file name, page or receipt number). Every verdict cites evidence. General expense practice, tax rules and other organisations' policies are not evidence: apply only the supplied policy.

A verdict is **settled** when the evidence decides it. It is **open** when the evidence does not: the receipt is missing or illegible, the receipt disagrees with the claim in a way the claimant could explain, a fact the policy depends on (pre-approval, attendees, business purpose) is not shown, or the policy is silent or ambiguous on the point. An open item gets the verdict *needs information*, together with what would settle it. Choose *needs information* over the most likely answer.

| Verdict | Use when | Approved amount |
| --- | --- | --- |
| approve | The receipt supports the item and the policy permits it. | The claimed amount, reduced where a clause caps it or excludes part of it, or where the receipt shows less. Never more than claimed. |
| reject | A clause excludes the item, and the facts that trigger the clause are established by the evidence. | 0 |
| needs information | The verdict is open. | 0, counted as pending |

A line item with no receipt is open, unless a clause exempts it (a threshold, a per diem, a missing-receipt declaration the claimant has made) or a clause makes the missing receipt final; that clause is then the evidence.

## Steps

1. **Index the policy.** Note the clauses that govern the categories on the claim: eligibility, caps and rates, receipt requirements, pre-approval, exclusions, submission deadline, currency conversion. Done when each category on the claim has its governing clause, or is marked "not addressed by the policy".

2. **Match receipts to line items.** For each line item, find its receipt and compare date, merchant, amount, currency and what was bought; record each mismatch. A receipt matched to two line items makes the second one open, as a possible duplicate. For a foreign-currency item, convert with the policy's rule; without one, use a rate shown on the receipt or a supplied card statement; without either, the conversion is open. Done when every line item has a receipt or is marked as having none, and every receipt is matched to a line item or listed as unmatched.

3. **Give each line item a verdict.** Apply the verdict table, including claim-level clauses such as the submission deadline. Where one receipt holds both permitted and excluded spending (alcohol on a meal receipt), approve the permitted part if the receipt itemises it; if it does not, the item is open. Done when every line item on the claim form has one verdict, one approved amount and its evidence.

4. **Compute the totals.** The corrected total is the sum of approved amounts. The pending total is the sum of claimed amounts on *needs information* items. Re-add the claim form's own total and note any difference from the stated figure. Done when each total in the review equals the sum of the rows it covers.

5. **Write the questions and the summary.** Each open item whose gap the claimant can fill gets a question for the claimant, naming the item and the document or fact that would settle it. Each open item that turns on a silent or ambiguous policy goes to the approver in the summary as a decision. Done when every *needs information* item appears in the questions or the summary.

## Output format

Use this structure. Write amounts with their currency, and give the totals in the currency the policy or claim form reimburses in.

```markdown
## Expense claim review: <claimant>, <claim reference or period>

### Line items
| # | Date | Description | Claimed | Verdict | Approved | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 2026-03-04 | Client dinner | 142.00 AUD | approve | 120.00 AUD | Policy 4.2 "meals capped at $120 per person"; Receipt R1: 142.00 AUD, 4 Mar |

### Totals
- Claimed: <stated total> (re-added: <sum of line items>)
- Corrected total to reimburse: <sum of approved amounts>
- Pending, needs information: <sum of open items' claimed amounts>

### Unmatched receipts
<receipts not matched to any line item, or "None">

### Questions for the claimant
1. Item <n>: <what is missing or inconsistent, and the document or fact that would settle it>

### Summary for the approver
<Three to five sentences: the corrected total; what was rejected and why; what is pending and what would settle it; any decision the policy leaves to the approver.>
```
