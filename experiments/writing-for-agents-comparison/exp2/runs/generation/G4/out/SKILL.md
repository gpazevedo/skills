---
name: expense-claim-review
description: Expense claim review against the organisation's supplied policy and receipts, giving a verdict per line item, the corrected total to reimburse, questions for the claimant and a summary for the approver. Use when the user supplies an expense claim to check or prepare for approval.
---

Review one expense claim for the approver, who makes the final decision. The user supplies three inputs: the claim form listing line items, the receipts, and the organisation's expense policy. The review is the deliverable; it ends when the four output sections are written (see [Output](#output)).

## Evidence rule

The supplied policy and the supplied receipts are the only evidence. Every verdict cites what settles it:

- a **policy clause**, identified the way the policy labels it (number or heading) and quoted where the wording decides the case;
- **receipt evidence**: which receipt, and the date, merchant, amount or item on it that the verdict rests on.

General custom, other organisations' rules, tax law and your own sense of what is reasonable are not evidence. When only they would settle an item, the item is **open**: its verdict is "needs information", and the review names the fact that would settle it. Open is the correct result for an unsettled item, not a failure to finish it.

## Steps

### 1. Check the inputs

If the policy or the claim form is missing, ask the user for it and stop: without the policy no verdict can cite a clause, and without the form there is no list of items to review. Missing or partial receipts do not stop the review; step 3 handles them item by item.

Done when you hold the claim form and the policy.

### 2. List the line items

List every line item on the claim form, keeping the form's own numbering if it has one (otherwise number them in form order). For each, record the date, description, category, claimed amount and currency. Record the claim's stated total, and note if it differs from the sum of its line items.

This list is the scope of the review: each item on it gets exactly one verdict, and nothing outside it gets one.

### 3. Match each item to its receipt

For each line item, find its receipt and compare date, merchant, amount, currency and what was bought. Record one result per item:

- **matched**: the receipt agrees with the line item on all of these;
- **mismatched**: name the field that disagrees and both values;
- **no receipt**, or a receipt too illegible to read the deciding field.

Then record two things that affect the approver but not the item list: receipts that match no line item, and any receipt claimed under more than one line item.

Done when every line item has one of the three results.

### 4. Give each item a verdict

Read the policy clauses that apply to the item's category, then give one verdict:

| Verdict | When | Approved amount |
| --- | --- | --- |
| Approve | The receipt is matched, a clause covers the expense, and every condition that clause sets (pre-approval, business purpose, attendee list, time limit) is shown in the claim or receipt. | The claimed amount, less any amount over a cap and any part of the receipt a clause excludes (such as a minibar charge on a hotel bill). Cite each reducing clause and show the reduction. |
| Reject | A clause excludes the expense, and the claim or receipt shows the expense falls under it. Cite the clause and the evidence. | Zero. |
| Needs information | Anything else: no receipt, a mismatched or illegible receipt, a clause condition not shown, the policy silent on this kind of expense, or a clause whose wording does not settle this case. | None yet. Record the amount at stake. |

For a needs-information item, name the single fact or document that would settle it, and who can supply it:

- the **claimant**, for a missing receipt, an explanation of a mismatch, or a missing condition such as proof of pre-approval;
- the **approver**, when the policy itself is silent or ambiguous. Quote the clause (or state that no clause covers the expense) so the approver can rule.

If the policy says what happens to items without receipts, cite that clause in the item's question so the claimant knows the consequence; the item still stays open, since the claimant may hold a receipt that was not supplied.

If an item is in a foreign currency, convert it using the policy's conversion rule, or the converted amount shown on the receipt or card statement. If neither exists, the item needs information.

Done when every item from step 2 has one verdict, an approved amount (or amount at stake), and its evidence.

### 5. Compute the corrected total

The corrected total is the sum of the approved amounts. Show the working so the approver can check it:

- claimed total;
- minus each rejected item;
- minus each reduction on an approved item;
- minus each needs-information item (listed with its amount at stake);
- equals the corrected total.

Done when the corrected total equals the sum of the Approve rows' approved amounts, in the reimbursement currency.

### 6. Write the questions and the summary

Write one claimant question per needs-information item the claimant can settle. Each names the item number, the document or fact needed, and, where a clause applies, what the policy requires.

Write the approver summary in at most six sentences: verdict counts, claimed total against corrected total, the largest reductions and their clauses, the amount still open, any policy gaps the approver must rule on, and any unmatched or duplicated receipts from step 3.

## Output

Produce the review in this shape:

```markdown
# Expense claim review: <claimant>, <claim reference or date>

## Line items

| # | Date | Description | Claimed | Verdict | Approved | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | ... | ... | ... | Approve / Reject / Needs information | amount, or "open: <amount at stake>" | Clause <id>: "<quote>"; Receipt <id>: <field and value> |

## Corrected total

<working from step 5>

**Corrected total to reimburse: <amount and currency>**
**Open, pending information: <amount and currency>**

## Questions for the claimant

1. Item <#>: <question>

## Summary for the approver

<summary from step 6>
```

Write "None" under a section that has no entries rather than leaving it out.

The review is complete when every line item from step 2 has exactly one row, every row cites a clause or receipt evidence, the corrected total matches the Approve rows, and every needs-information row is covered by either a claimant question or an approver policy-gap note in the summary.
