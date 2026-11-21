---
name: expense-claim-review
description: Expense claim review, line by line, against its receipts and the organisation's supplied expense policy. Use when the user supplies an expense claim to review.
---

# Expense claim review

The review rests on two kinds of **evidence**: the receipts and the expense policy the user supplied. Cite only those two. A verdict is **settled** when cited evidence decides it; every other verdict stays **open**, as _needs information_. An open verdict with a precise question is a correct result, as good as an approval or a rejection.

## Steps

1. **Index the inputs.** Number every claimed line item (#1, #2, ...) with its date, description, category, amount and currency as claimed. Label every receipt (R1, R2, ...). Note the policy clauses by their own numbers or headings, and quote the ones that set eligibility, caps, exclusions, receipt requirements, pre-approval, deadlines and exchange rates. If the policy or the claim form is missing, ask the user for it before going on: no verdict can be settled without them. A missing receipt is a finding for step 2. Done when every line of the claim form has a number, every receipt a label, and every clause you will cite a reference.

2. **Reconcile items with receipts.** Match each item to its receipt or receipts, comparing date, merchant, amount, currency and what was bought. Record every mismatch. Flag as a possible duplicate any receipt matched to two items, and any two items that describe one expense. Done when every item has a matched receipt or is marked _no receipt_, and every receipt is matched or marked _unclaimed_.

3. **Apply the policy to each item.** For each item, find the clauses that govern it: whether the category is eligible, caps and per-diems, excluded components (a single receipt can mix allowed and excluded purchases), receipt requirements, pre-approval and submission deadlines. Where the policy is silent on the point that decides an item, record the gap; the item is open and the gap goes to the approver. Done when every item has its governing clauses cited, or a recorded gap.

4. **Give each item a verdict.** Use the verdict rules below. Done when every item has one verdict (or a split), an amount, and evidence: a clause reference, a receipt label, or both.

5. **Compute the corrected total.** Split each item's claimed amount across three buckets: approved, rejected (including any reduction) and open. Sum each bucket, showing the line-by-line working. The approved total is the corrected total to reimburse now. If the claim form's own arithmetic is wrong, say so. Done when approved + rejected + open equals the claimed total.

6. **Write the questions for the claimant.** For each open item the claimant can settle, ask for the exact evidence that would settle it, naming the item number ("#4: please supply the itemised receipt showing what the $86 at Harbour Grill covered"). Done when every such open item has a question.

7. **Write the approver summary** in five sentences or fewer: the totals, each rejection and its reason, what the open items wait on, the policy gaps that need the approver's decision, and any duplicate or anomaly flags.

8. **Check the review.** Every item number from step 1 appears in the verdict table; every cited clause and receipt label exists in the supplied inputs; the totals balance.

## Verdict rules

- **Approve** when a receipt supports the item and a clause allows it. The approved amount is the lowest of the claimed amount, the receipt amount and any policy cap; name the reason for any reduction.
- **Reject** when a cited clause excludes the item: an ineligible category, an excluded component, a missed deadline, a pre-approval the policy requires and the claim shows was not obtained.
- **Needs information** whenever the evidence does not settle the item: a missing or illegible receipt, a mismatch the claimant could explain, a required pre-approval the claim neither shows nor rules out, a policy silent on the deciding point.
- **Split** an item whose receipt mixes allowed and excluded components: approve the allowed part and reject the excluded part, each with its own evidence. If the receipt does not itemise the parts, the item is open.
- **Currency**: convert at a rate the evidence supplies (on the receipt, on a supplied card statement, or by the method the policy sets). With no such rate, the item is open.

## Output

```markdown
## Verdicts

| # | Item | Claimed | Receipt | Verdict | Approved | Evidence |
|---|------|---------|---------|---------|----------|----------|

## Corrected total

Claimed: ... | Approved: ... | Rejected: ... | Open: ...
Reimburse now: <approved total>
<line-by-line working>

## Questions for the claimant

1. #n: ...

## Summary for the approver

...
```

Unclaimed receipts and duplicate flags go under the verdict table, each with its receipt label.
