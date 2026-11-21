---
name: expense-claim-review
description: Reviewing an expense claim against its receipts and the organisation's expense policy. Use when given a claim form with receipts and a policy to check.
---

Review a supplied expense claim line by line. The supplied policy is the only rulebook; the receipts are the only evidence. Anything the documents do not say is _open_.

## Inputs

Needed: the claim form (line items), the receipts, the expense policy. If one is missing, say which and stop; a review without the policy cannot be done, and a review without receipts marks every affected line `needs information`.

## Steps

1. **Ledger the claim.** List every line item with its claimed amount, date, category and claimed currency. Done when the line count and the sum of lines match the form's stated total, or the mismatch is recorded as a finding.
2. **Match receipts.** Pair each line with its receipt (one receipt may cover several lines; one line may lack any). Read the receipt's amount, date, vendor, currency, and itemisation. Done when every line has a matched receipt or an explicit "no receipt" and every receipt is matched to a line or listed as unclaimed.
3. **Find the clause.** For each line, locate the policy clause that governs it (category rule, limit, approval requirement, receipt requirement, deadline). Quote or cite the clause number. Done when every line has a clause, or "no clause covers this" (which is open, never approve by default).
4. **Decide each line.** Apply the verdict rules below. Done when every line carries exactly one verdict plus its evidence.
5. **Compute the total.** Reimburse approved amounts in full; for a line approved only up to a policy cap, reimburse the capped amount and say so. Rejected and open lines contribute 0. Done when the corrected total equals the sum of the per-line reimbursable amounts, and the gap to the claimed total is explained line by line.
6. **Write the review** in the format below.

## Verdict rules

- **approve**: a receipt supports the amount, date and purpose, and a clause permits it. Cite both.
- **reject**: the policy clause or the receipt itself rules it out (excluded category, over a hard limit, duplicate, outside the claim period, receipt shows a different amount). Cite the clause or the receipt detail. A rejected line states the amount disallowed.
- **needs information**: the documents do not settle it. Typical causes: missing or illegible receipt, receipt lacks itemisation the policy needs, unstated business purpose, missing pre-approval evidence, ambiguous clause, currency conversion without a stated rate. Say what is missing and what answer would turn it into approve or reject.

A reasonable guess at the missing fact is still a guess: leave the verdict `needs information` and ask. Knowledge of "normal" company practice, other policies or tax rules stays out; if the policy is silent, say so.

Partial cases: when part of a line is allowed (e.g. a meal over the cap, alcohol on an itemised bill), approve the allowed part, reject the rest, and show the split.

## Output format

```
# Expense claim review: <claimant, claim ref/period>

## Summary for approver
<4 to 6 lines: claimed total, corrected total to reimburse, counts of approve / reject / needs information, the amount on hold pending answers, and the one or two issues that matter most>

## Line items
| # | Item (date, vendor) | Claimed | Verdict | Reimburse | Evidence |
|---|---|---|---|---|---|
| 1 | ... | 0.00 | approve / reject / needs information | 0.00 | Receipt: ...; Policy cl. X.Y: ... |

## Total
Claimed: ...  Approved: ...  Rejected: ...  On hold: ...
Corrected total to reimburse: ...  (note: held items would add up to ... if approved)

## Questions for the claimant
1. Line N: <specific question and what document would settle it>

## Other findings
<unclaimed receipts, total mismatches, duplicates, anything the form and receipts disagree on; omit if none>
```

Each question names the line and the exact document or fact wanted. Every line with `needs information` has at least one question; every question traces to a line or a finding.

## Before returning

Check, in order: every claimed line has a row; every row has a verdict and cited evidence; the corrected total sums from the rows; each `needs information` row has a question; the summary's figures equal the Total section.
