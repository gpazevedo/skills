---
name: expense-claim-review
description: Expense claim review against the receipts and the organisation's supplied expense policy. Use when the user supplies an expense claim to check, approve, or audit.
---

Review an expense claim **closed-book**: the only rules are the clauses of the policy the user supplied, and the only facts are the claim form and the receipts. Every verdict cites one of them. When they do not settle an item, its verdict stays **open** (needs information) and becomes a question; an open verdict is a correct result, not a failure.

## Inputs

You need three things: the claim form (its line items), the receipts, and the expense policy. If the policy is missing, ask for it and stop: without it no item can be approved or rejected. If receipts are missing, carry on; the affected items go open.

## Steps

1. **Inventory.** Number every line item exactly as the claim form lists it (date, description, category, amount, currency). Label every receipt (R1, R2, ...). Note the policy's clause numbers, or quote short headings if it has none. Done when every claim line has an ID and every receipt has a label.

2. **Match.** Pair each line item with its receipt and compare four fields: amount, date, merchant, and what was bought. Record each mismatch in a few words. Done when every line item is either matched or marked "no receipt", and every receipt is either matched or listed as unmatched. If a pairing is not one-to-one (one receipt split across items, a shared bill, a foreign currency, partly personal items, the same receipt used twice), read [`EDGE-CASES.md`](EDGE-CASES.md) before going on.

3. **Apply the policy.** For each line item, find every clause that governs it: eligibility, category caps, per-day or per-person limits, receipt requirements, pre-approval requirements, time limits for claiming. Done when each item has its governing clauses listed, or is marked "policy silent".

4. **Verdict.** Give each line item one verdict, using the rules below. Done when every line item has a verdict, an approved amount, and a citation.

5. **Total.** Corrected total to reimburse = the sum of approved amounts. Show the sum, then the amount rejected and the amount held as open, so that approved + rejected + open = the claimed total. Re-add the claim form's own total and report any arithmetic error on the form. Done when the three parts reconcile to the cent.

6. **Questions for the claimant.** One question per open item, naming the item ID and the exact document or fact that would close it ("Please send the itemised receipt for item 4, the Hotel Rex bill of 12 March"). Questions about what the policy means go to the approver in the summary, not to the claimant.

7. **Summary for the approver.** Three to five sentences: the claimed total, the corrected total, the main reasons for any rejections, what is held open and why, and any policy gap the approver must rule on.

## Verdict rules

- **Approve**: the receipt matches the item, a clause permits the expense, and the amount is within every cap. If a cap applies and the amount exceeds it, approve the capped amount and cite the cap; the excess counts as rejected.
- **Reject**: a clause excludes the expense, or the claim breaks a hard requirement the policy states (for example, claimed after the deadline). Cite the clause.
- **Open**: the evidence does not settle it. Typical causes: no receipt where the policy requires one, a mismatch between receipt and claim, a required pre-approval not shown, or a policy that is silent or ambiguous on this expense. Approved amount is 0 until it closes. Name what would close it.

Citations take the form "Policy 4.2" or "R3: total $48.20, dated 3 May". A verdict with no citation is unfinished. Common practice, typical company rules, and tax rules are outside the closed book: when they would decide an item, the item is open and the gap goes in the approver summary.

## Output

```
## Expense claim review: <claimant>, <claim reference or period>

### Line items
| # | Date | Description | Claimed | Receipt | Verdict | Approved | Evidence |
|---|------|-------------|---------|---------|---------|----------|----------|
| 1 | ...  | ...         | $x      | R1      | Approve | $x       | Policy 3.1; R1 matches |

Unmatched receipts: <labels and one line each, or "none">

### Corrected total
Approved: $a (items ...)
Rejected: $b (items ...)
Open:     $c (items ...)
Claimed:  $a + $b + $c = $total
Claim form arithmetic: <correct, or the error>

### Questions for the claimant
1. Item N: ...

### Summary for the approver
...
```

Use the claim's currency throughout. Check before finishing: every line item has a row, every row cites evidence, every open item has a question, and the totals reconcile.
