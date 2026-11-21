---
name: expense-claim-review
description: Expense claim review against receipts and a supplied expense policy, giving per-item verdicts and a corrected total. Use when the user supplies an expense claim to review or approve.
---

Review one expense claim using three inputs the user supplies: the **claim form** (the line items), the **receipts**, and the **policy** (the organisation's expense policy). The policy is the whole rulebook: every rule you apply is a clause you can quote from it.

Two leading words run through every step:

- **Evidence** is a quoted policy clause (with its number or heading) or a specific receipt fact (merchant, date, amount, currency, item lines). Every verdict names its evidence.
- A verdict is **settled** when its evidence decides it. An item whose evidence leaves it unsettled gets `needs information`, plus a question naming the exact fact that would settle it. Unsettled is a correct result, as valid as approve or reject.

## Step 1: Inventory the inputs

Give each line item an ID (use the form's own numbering if it has one, else `L1`, `L2`, ...), each receipt an ID (`R1`, `R2`, ...), and note how the policy labels its clauses so you can cite them. Record the claim form's stated total, and re-add the line items to check it.

If the policy is missing, stop here and ask the user for it: without the policy, no verdict can be settled.

**Done when** every line item and every receipt has an ID, and you know whether the form's stated total matches the sum of its lines.

## Step 2: Match every item to its receipt

For each line item, find its receipt and compare merchant, date, amount, currency and what was bought. Read the receipt's item lines, not only its total: a receipt total can include things the claimant did not claim, or things the policy excludes.

- One receipt may cover several line items, and one line item may need several receipts; record the mapping either way.
- Two line items drawing on the same receipt amount is a **duplicate**: the second claim is rejected, with the receipt as evidence.
- An item with no receipt is checked against the policy's clause on missing receipts. If the policy has none, the item is unsettled.
- A receipt in a currency other than the claim's is converted only by the method the policy states, or at a rate printed on the receipt or card statement. With neither, the converted amount is unsettled.
- A receipt that matches no line item is listed as **unclaimed**; it may signal a mistyped item.

**Done when** every line item has a matched receipt or is marked `no receipt`, and every receipt is matched to an item or listed as unclaimed.

## Step 3: Rule on every item

For each line item, decide one verdict and the **approved amount**:

- `approve`: the policy allows the expense and the receipt supports the amount. If a policy cap or the receipt amount is lower than the claimed amount, approve the lower figure and cite the clause or receipt fact that sets it.
- `reject`: a quoted clause excludes the expense, or the receipt shows it was not incurred as claimed. Approved amount is 0.
- `needs information`: the evidence leaves the item unsettled (the policy is silent or ambiguous on it, the receipt is missing, illegible, or disagrees with the form in a way either reading could explain). Approved amount is pending.

Read each applicable clause in full, including its conditions, limits and required approvals (pre-approval, business purpose, attendee names). A clause that needs a fact the claim does not give leaves the item unsettled.

**Done when** every line item has exactly one verdict, an approved amount (or `pending`), and named evidence; and every `needs information` item has at least one question that names the fact that would settle it.

## Step 4: Compute the corrected total

Split each item's claimed amount into three parts: **approved**, **withheld** (rejected items, plus the cut from any capped or reduced approval), and **pending** (`needs information` items). The corrected total to reimburse is the sum of approved amounts.

**Done when** approved + withheld + pending equals the claimed total (the sum of the line items) to the cent. If it does not, find the item that breaks it before moving on.

## Step 5: Write the review

Use this layout. Keep currency symbols and the claim's own item descriptions.

```markdown
# Expense claim review: <claimant>, <claim reference or period>

## Summary for the approver
<3 to 5 sentences: corrected total against claimed total, the main reasons for any
withheld amount, what is pending and on which questions, and anything the approver
must personally decide or sign off under the policy.>

## Verdicts
| ID | Date | Item | Claimed | Receipt | Verdict | Approved | Evidence |
|----|------|------|---------|---------|---------|----------|----------|
| L1 | ... | ... | ... | R1 | approve | ... | Policy 4.2 "..."; R1 total ... |

## Totals
- Claimed: <sum of line items> (form states <stated total>; note any difference)
- Approved, to reimburse: <amount>
- Withheld: <amount>
- Pending: <amount>, across <IDs>

## Questions for the claimant
1. <ID>: <question naming the fact needed, and what each answer would mean for the verdict>

## Other findings
<unclaimed receipts, arithmetic errors on the form, anything else the review turned up;
omit this section if empty>
```

**Done when** the review has every section above, every line item from Step 1 appears once in the verdicts table, and every figure in the summary matches the Totals section.
