---
name: expense-claim-review
description: Review an expense claim against its receipts and the organisation's expense policy. Use when given a claim form, receipts and a policy to check or approve.
---

Review a claim line by line. The supplied policy is the only rulebook; the receipts are the only evidence. Each verdict is _auditable_: anyone can follow its cited clause or receipt back to the source.

## Inputs

Claim form, receipts, policy. If any of the three is missing, say which, and proceed only on what can be settled; every item that depends on the missing input stays **needs information**.

## Steps

1. **Index the policy.** List each clause with its number or heading, so every verdict can cite one. Limits, categories, approval thresholds and receipt rules all count. The policy is closed: a rule you know from elsewhere is not a clause.
2. **Index the receipts.** For each receipt record vendor, date, amount, currency, and what was bought. Done when every receipt is listed, including receipts that match no claimed line.
3. **Match every claimed line to a receipt.** Done when each line has a receipt, or is marked _unmatched_. Compare amount, date, vendor and description against the claim; a mismatch in any is a finding.
4. **Rule on each line.** Done when every line carries one verdict, with its evidence:
   - **Approve**: a matching receipt exists and a clause permits it. Cite both.
   - **Reject**: a clause forbids it, or the receipt contradicts the claim. Cite the clause or the contradicting receipt detail.
   - **Needs information**: the evidence does not settle it (illegible or missing receipt, ambiguous clause, missing business purpose, unclear currency or date). State the exact fact that would settle it. Leave it open rather than infer.
   A partly allowed line (over a cap) is split: the allowed part approved, the excess rejected, each with its clause.
5. **Total.** Corrected total = approved amounts only. Show it next to the claimed total with the difference. Needs-information amounts sit in a separate line as _pending_, outside the total. Done when the arithmetic reconciles: approved + rejected + pending = claimed.
6. **Questions.** One per needs-information line, addressed to the claimant, answerable in a sentence, each naming the document or fact wanted. Add any receipt that matched no line.
7. **Summary.** Done when the approver can decide from it alone.

## Output

```
## Line items
| # | Claimed item | Claimed | Verdict | Approved | Evidence (clause / receipt) |

## Total
Claimed / Approved (reimburse) / Rejected / Pending

## Questions for the claimant
1. ...

## Summary for the approver
```

Summary: 3 to 5 sentences covering the corrected total, counts by verdict, the largest rejection and why, what is pending, and anything needing approver judgement (such as a clause that is ambiguous).
