---
name: expense-claim-review
description: Expense claim review, line by line against the claim's receipts and the supplied expense policy. Use when the user supplies an expense claim to review, check or approve.
---

Review an expense claim from three inputs the user supplies: the **claim form** (the line items), the **receipts**, and the organisation's **expense policy**. The output is a review an approver can act on without reopening the inputs.

The supplied policy is the only authority. Every verdict rests on **evidence**: a clause quoted or cited from that policy, or a fact read off a receipt. A verdict that would need anything else (common practice, tax rules, what a typical company allows) has no evidence, so it stays **open**.

If the policy or the receipts are missing, ask the user for them before step 1, and list what you have so they can see the gap.

## Steps

### 1. Build the ledger

Make one **ledger** row per line item on the claim form: item number, date, description, category, amount and currency as claimed. Number the policy clauses the way the policy does (section numbers or headings); where it has none, cite by heading plus a short quote. Read every receipt, including images, and note its merchant, date, items, amount, currency and payer.

Done when: every line item on the form has a row, and the rows sum to the form's stated total. If they do not, record the difference; it becomes a claimant question.

### 2. Match receipts

Pair each row with its receipt. For each pair, check that the receipt matches the row on amount, date, merchant, what was bought, and currency, and that it is a receipt (a payment record or tax invoice) rather than a quote or booking confirmation, where the policy draws that line. Watch for one receipt attached to two rows, two rows claiming the same expense, and a receipt total that covers items the row does not claim (or the reverse). When one receipt is attached to two rows, it belongs to the row it matches; the other row has no receipt.

Done when: every row has a matched receipt or is marked "no receipt", and every receipt is either matched or listed as unmatched.

### 3. Test each row against the policy

For each row, find every clause that governs it: eligibility of the expense type, caps and per-diems, receipt requirements, pre-approval requirements, submission deadlines, excluded items (for example alcohol or upgrades), and currency conversion. Apply each one, then give the row a verdict under the rules below. Strip excluded items from a receipt first, then apply any cap to what remains.

Done when: every row has a verdict, an amount to reimburse, and at least one piece of evidence; every open verdict has the question or policy gap that would settle it.

### 4. Total and write the review

Compute the totals and write the review in the format below.

Done when: approved + rejected + held equals the claimed total, to the cent, with any form-total discrepancy from step 1 shown.

## Verdicts

- **Approve**: the receipt matches (or the policy waives a receipt for this item, for example under a value threshold) and no clause excludes the item. When a clause caps it, approve the capped amount, show the excess as rejected within that row, and cite the cap.
- **Reject**: the evidence settles it against the claimant: a clause excludes the item, the receipt shows something other than what was claimed, or the row claims the same expense as another row. Cite the clause or the receipt fact.
- **Needs information** (open): the evidence leaves the row unsettled. Typical causes: no receipt where the policy requires one, an unreadable receipt, a receipt that only partly matches, a missing business purpose or pre-approval the policy requires, or a policy that is silent or ambiguous on this kind of expense. The full claimed amount is **held**, neither approved nor rejected.

An open verdict is a finished verdict. When two readings of the evidence lead to different verdicts, keep the row open and name both readings.

Route each open row's gap to whoever can close it: facts only the claimant knows (purpose, attendees, a replacement receipt) become **claimant questions**; gaps in the policy itself go to the **approver summary**.

## Review format

```markdown
# Expense claim review: <claimant>, <claim reference or period>

## Line items

| # | Date | Description | Claimed | Verdict | Reimburse | Evidence |
|---|------|-------------|---------|---------|-----------|----------|
| 1 | ... | ... | 120.00 | Approve | 80.00 | Receipt R1 matches; policy 4.2 caps dinner at 80.00, 40.00 rejected |

## Totals

- Claimed: <amount> (form states <amount>; <difference, if any>)
- Approved to reimburse now: <amount>
- Rejected: <amount>
- Held pending information: <amount>

## Questions for the claimant

1. Item <#>: <specific question, naming the document or fact that would settle it>

## Summary for the approver

<Three to six sentences: the amount to reimburse now, what was rejected and why, what is held and what would release it, and any policy gaps or patterns (duplicates, repeated cap breaches) worth the approver's judgement.>
```

Write amounts in the claim's currency with its symbol or code. Where a row was converted from another currency, show the original amount and the rate used, and cite the clause or receipt that supplied the rate.
