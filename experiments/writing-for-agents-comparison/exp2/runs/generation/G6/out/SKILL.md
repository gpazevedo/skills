---
name: expense-claim-review
description: Expense claim review against the supplied expense policy and receipts, giving each line item a verdict with its evidence, the corrected total, claimant questions and an approver summary. Use when the user supplies an expense claim to check, or the claimant's answers to an earlier review's questions.
---

# Expense claim review

Review one expense claim using only what the user supplies: the **claim form** (the claimed line items), the **receipts**, and the organisation's **expense policy**. The review is written for the approver. It recommends; it does not decide, contact anyone, or change the claim.

## Ground rules

These hold in every step.

- **The supplied policy is the only rulebook.** Judge each item only against clauses of the supplied policy. Tax rules, common practice elsewhere and what seems reasonable are not grounds for a verdict. Where the policy is silent, ambiguous, or has two clauses that conflict on an item, the verdict stays open and the gap goes to the approver in the summary.
- **Evidence settles a verdict, or the verdict stays open.** Every verdict cites its evidence: a policy clause (its number or heading, plus the deciding words quoted briefly) and, for any item that has a receipt, the receipt (its identifier, plus the fields that decide it: date, merchant, amount, currency, items bought). When the cited evidence does not settle the item, the verdict is **needs information**. Read figures only as printed: an illegible amount, a missing date, an unstated business purpose or an absent pre-approval is missing evidence, not something to fill in.
- **The approved amount never exceeds the claimed amount**, even when a receipt shows more.

### Verdicts

| Verdict | Use when | Approved amount |
| --- | --- | --- |
| **Approve** | A policy clause permits the item, and its receipt matches the claim (or the policy does not require a receipt for it). | The claimed amount, or a lower amount when the receipt shows less, a policy limit caps the item, or an itemised receipt lets you remove excluded items. State each reduction and cite the clause or receipt line behind it. |
| **Reject** | A policy clause excludes the item (ineligible type, submission deadline passed, and so on), or the line repeats another line on the same receipt with the same date, merchant and amount. | 0 |
| **Needs information** | The evidence does not settle the item: no receipt where the policy requires one, a receipt that disagrees with the claim in a way you cannot resolve, excluded items possibly inside a non-itemised total, no conversion rate in the inputs, or a policy gap. | Pending: left out of the reimbursable total. |

## Steps

1. **Check the inputs.** You need the claim form and the policy. If either is missing, stop and ask the user for it; do not review against assumed rules. Missing receipts are not a reason to stop: those lines are judged in step 3.
   If the user supplies the claimant's answers to an earlier review, re-run steps 3 to 6 for the lines that were left as needs information. An answer counts as evidence when it brings a document (a receipt, an approval email) or when a policy clause accepts the claimant's written statement; cite that clause. Keep the other verdicts unless the new material bears on them.
   _Done when_ you hold the claim form and the policy.

2. **List the lines and match the receipts.** Number every line on the claim form in its order, keeping the claimant's own numbering if it has one. Match each line to its receipt and note the receipt's date, merchant, amount, currency and items. Also note any receipt that matches no line, any receipt that two lines both rely on, and whether the claim form's stated total equals the sum of its lines.
   _Done when_ every claim line is matched to a receipt or marked "no receipt".

3. **Give each line a verdict.** Check the receipt against the line (amount, date, merchant, what was bought), then the line against every policy clause that applies to it: eligibility, limits and caps, receipt requirements, pre-approval, attendee or purpose requirements, and submission deadlines. Choose the verdict from the table above.
   _Done when_ every line has exactly one verdict, an approved amount or "pending", and the evidence the ground rules require.

4. **Compute the corrected total.** Add the approved amounts. Separately, add the claimed amounts of the needs-information lines as the pending amount. List every reduction and rejection against the claimed total. Report amounts in the currency the policy reimburses in; convert only at a rate the inputs supply (a receipt, a card statement, or a policy rule), and treat a line with no supplied rate as needs information.
   _Done when_ you have re-added the approved column from the table and it equals the stated total, and claimed = approved + pending + reductions and rejections.

5. **Write the questions for the claimant.** Write at least one question for each needs-information line whose gap the claimant can fill. Name the line and the exact evidence that would settle it, for example "Line 4: please supply the itemised restaurant receipt showing what was ordered." Policy gaps and conflicts are for the approver, so they go in the summary instead.
   _Done when_ every needs-information line has a question here or a policy gap in the summary.

6. **Write the summary for the approver.** At most six bullets: the count of each verdict; claimed, approved and pending totals; the main reasons for rejections and reductions; policy gaps or conflicts the approver must decide; and any unmatched receipts or errors in the claim form's arithmetic.

Deliver the review in the format below and stop there.

## Output format

```markdown
## Expense claim review: <claimant>, <claim reference or period>

### Line items

| Line | Date | Description | Claimed | Verdict | Approved | Evidence and reason |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | ... | ... | ... | Approve | ... | Receipt R1: ...; Policy 3.2 "..." |

### Corrected total

- Claimed: <amount>
- Approved to reimburse: <amount>
- Pending (needs information): <amount>, lines <n, n>
- Rejected or reduced: <amount>
  - Line <n>: -<amount>, <reason>

### Questions for the claimant

1. Line <n>: <question naming the evidence needed>

### Summary for the approver

- ...
```
