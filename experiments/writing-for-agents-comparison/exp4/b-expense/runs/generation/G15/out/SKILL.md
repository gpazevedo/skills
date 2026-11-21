---
name: expense-claim-review
description: Expense claim review. Use when given a claim form with receipts and an expense policy to check, approve or reimburse.
---

Review one expense claim against its receipts and the supplied policy, and return a decision the approver can act on. The supplied policy is the only rulebook; the claim and receipts are the only evidence. Treat knowledge of "typical" expense rules as absent.

## Inputs

A claim form (line items), receipts, and the organisation's expense policy. If any of the three is missing, ask for it before reviewing.

## Steps

1. **Index the policy.** List each clause by number or heading with its limit, condition and required evidence. Done when every clause is indexed; the clause IDs are what verdicts will cite.
2. **Match every line item to its receipt.** One receipt per item; one item may span several receipts. Compare date, payee, amount, currency and what was bought against the claimed values. Done when each claimed item is _matched_, _mismatched_ (state the difference) or _unmatched_ (no receipt). Receipts with no claim line are noted, not reimbursed.
3. **Assign a verdict per item**, using the rules below. Done when every claimed item carries a verdict, a cited basis, and an approved amount.
4. **Total.** Corrected total = the sum of approved amounts (partial approvals count at the approved portion). Show the arithmetic as a line-by-line sum and state the claimed total beside it. Needs-information items add 0 and are listed separately as pending.
5. **Write the questions and summary** (format below).

## Verdicts

- **Approve**: a matched receipt shows the item, and a policy clause permits it at this amount. Cite both. Where the clause caps the amount, approve up to the cap and cite the cap.
- **Reject**: a clause prohibits the item or the amount, or the receipt contradicts the claim. Cite the clause or the receipt line.
- **Needs information**: the evidence leaves the answer open. Typical causes: receipt missing, illegible or lacking itemisation; business purpose not stated where the policy requires one; the policy is silent or ambiguous on the item; amounts or dates disagree without explanation. Name the exact fact that would settle it and which outcome each answer leads to. Keep the verdict open; a policy gap is a question for the approver, never a rule you supply.

Every verdict states its basis as `Clause X.Y` and/or `Receipt: <what it shows>`. A verdict with no cited basis is unfinished.

## Output

```
## Line items
| # | Item | Claimed | Verdict | Approved | Basis |
(one row per claimed item, in claim order)

## Corrected total
Claimed: ... | Approved: ... | Pending (needs information): ...
<sum line by line>

## Questions for the claimant
(numbered; each names the item #, the missing fact, and what it decides)

## Summary for the approver
(3 to 5 sentences: claimed vs approved total, count of items per verdict, the main reason for each rejection, what is pending and what it could add)
```

Receipts or policy clauses that are unreadable are quoted or described in the Basis so the approver can verify them.
