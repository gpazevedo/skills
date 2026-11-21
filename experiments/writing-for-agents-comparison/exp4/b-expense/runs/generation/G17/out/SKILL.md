---
name: expense-claim-review
description: Review an expense claim against its receipts and the organisation's expense policy. Use when given a claim form, receipts and a policy to check, approve or reimburse.
---

Produce a review of one expense claim. The supplied policy is the only rulebook; the receipts are the only evidence. Hold both _strictly_: no outside norms ("most companies allow..."), no assumed facts.

## Inputs

Claim form (line items), receipts, policy. If any of the three is missing, say so first and review what can be reviewed; every item then lacking its source gets `Needs information`.

## Steps

1. **Index the policy.** List each clause with its number or heading. Cite only from this list.
2. **Match receipts.** For every line item on the claim form, find its receipt. Record: date, merchant, amount, currency, what was bought. Receipts with no claimed line are listed under Questions.
3. **Audit each line item.** Compare the claim to the receipt (amount, date, merchant, currency, description), then to the policy (category, limits, approvals, deadlines). Assign one verdict:
   - **Approve**: the receipt matches the claim and a clause permits it. Cite both.
   - **Reject**: a clause forbids it, or the receipt contradicts the claim. Cite the clause or the receipt fact.
   - **Needs information**: the evidence does not settle it (missing or illegible receipt, unclear business purpose, policy silent or ambiguous). Leave it open and state exactly what would settle it.
   Partial amounts: approve the permitted part and reject the rest as two stated amounts.
4. **Total.** Corrected total = sum of approved amounts. Show the sum of every approved amount, and list `Needs information` amounts separately as pending, outside the total.
5. **Close the audit.** Done when every claimed line item has a verdict, a citation, and a receipt reference, and the corrected total reconciles with the verdicts. Recount the line items against the claim form.

## Output

Use exactly these sections.

**Line items**: a table with columns: #, item, claimed amount, verdict, approved amount, basis (clause number plus receipt evidence).

**Corrected total to reimburse**: figure, with currency, plus the pending amount.

**Questions for the claimant**: one per open or rejected-on-evidence item, each naming the item and the document or fact needed.

**Summary for the approver**: three to five sentences: claimed vs. recommended total, counts of approved / rejected / open items, and the main issue.
