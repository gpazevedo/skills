---
name: expense-claim-review
description: Expense claim review against a supplied policy and receipts. Use when asked to review, check, audit or approve an expense claim, reimbursement request or expense report.
---

Review an expense claim using three inputs the user supplies: the **claim form** (the claimed line items), the **receipts**, and the organisation's **expense policy**. The output is one review document for the approver.

Two rules govern every step:

- **The supplied policy is the whole rulebook.** Every approval and rejection cites a clause of it, by its number or heading, with the deciding words quoted. When the policy is silent on a point, the point is unsettled, and general practice or other organisations' norms stay out of it.
- **Unsettled means open.** When the evidence does not settle an item, its verdict is `needs information`, and the gap becomes a question for the claimant. An open verdict is a correct result, not a failure to finish.

If one of the three inputs is missing, ask the user for it before starting. A claim with no policy cannot be reviewed; a missing receipt for one item is a finding, handled in step 2.

## Steps

### 1. Inventory

Number every claimed line item (L1, L2, ...) with its date, description, category and claimed amount as written on the form. Number every receipt (R1, R2, ...). List the policy clauses that bear on expenses (caps, eligible and excluded categories, receipt requirements, approval thresholds, time limits, currency rules).

Done when every line on the form has an ID, including lines that look duplicated or trivial.

### 2. Match receipts

For each line item, find its receipt and compare the two field by field: date, merchant, amount, currency, and what was bought. Record each discrepancy exactly (e.g. "claimed 84.00, receipt shows 48.00"). Note receipts that cover items the policy treats differently (a hotel bill with a minibar charge, a restaurant bill with alcohol, a receipt covering other people).

Results per item: `matched`, `matched with discrepancies` (list them), or `no receipt`. Two line items claiming the same expense (same date, merchant and amount, or one receipt matched to both) are a possible duplicate: mark both. Receipts matched to no line item are listed as unmatched.

Done when every line item has a match result and every receipt is either matched or listed as unmatched.

### 3. Apply the policy

For each line item, find the clauses that govern it and test the item against each: is the category eligible, is the amount within the cap, is a receipt required at this amount, was any required pre-approval given, is it within the submission deadline, is the currency conversion done the way the policy says.

Done when every line item has every applicable clause tested, with the clause cited.

### 4. Decide each verdict

- `approve`: the receipt supports the item (or the policy waives the receipt at this amount) and a clause permits it. When a cap or a non-reimbursable part reduces the amount, approve the allowed amount and state the reduction and its clause.
- `reject`: a clause excludes the item, or the receipt contradicts the claim. Cite the clause or the receipt.
- `needs information`: anything else. Typical cases: no receipt where one is required, a discrepancy the claimant may be able to explain, a possible duplicate, a clause whose condition depends on facts not in the documents (business purpose, attendees, pre-approval, the exchange rate the policy names), or a policy that does not cover the item. When a clause already excludes part of the item (alcohol on a meal bill), record that part as a reduction now and hold the rest.

Done when every line item has exactly one verdict, an approved amount (0.00 for reject and needs information), a held amount for needs information (the most that could still be approved once answered), and the clause or receipt evidence behind it.

### 5. Compute the corrected total

The corrected total is the sum of approved amounts. Show the held total separately, so the approver sees what may still be added. Take the claimed total as the sum of the line items; if the form's stated total differs, report both in Notes.

Done when this reconciliation holds and is shown: claimed total = approved + reductions + rejected + held.

### 6. Write questions for the claimant

Write at least one question per `needs information` item, and one per unexplained discrepancy. Each question names the line item, asks for one specific fact or document, and says what that answer would settle. A fact only the organisation holds (an official exchange rate) goes in Notes for the approver instead.

Done when every `needs information` item is covered by a question or a Note.

### 7. Write the review

Use this structure:

```
# Expense claim review: <claimant>, <claim reference or period>

## Summary for the approver
<3 to 5 sentences: claimed total, corrected total, held total, the main reasons for reductions and rejections, and what is waiting on the claimant.>

## Line items
| ID | Date | Description | Claimed | Receipt | Verdict | Approved | Held | Evidence |
|----|------|-------------|---------|---------|---------|----------|------|----------|
<one row per line item; Evidence cites the clause (quoted deciding words) and/or the receipt finding>

## Totals
Claimed: <amount>
Approved (corrected total to reimburse): <amount>
Reductions: <amount>
Rejected: <amount>
Held pending information: <amount>

## Questions for the claimant
1. <L#>: <question> (settles: <what>)

## Notes
<facts for the approver to supply, unmatched receipts, form total errors, policy gaps the approver may want to fix; omit the section if empty>
```

Done when every line item from step 1 appears in the table, every verdict carries evidence, and the totals reconcile.
