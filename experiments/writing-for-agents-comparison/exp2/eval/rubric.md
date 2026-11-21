# Rubric (experiment 2)

Fixed before any candidate skill is generated. Graders score each review against the case's files and answer key, independently of the other reviews. Every deduction quotes the review (or states that the expected item is absent) and names the answer-key item or question it concerns.

## Primary score per review (0 to 100)

| Criterion | Points | How to score |
| --- | --- | --- |
| Coverage | 15 | 15 x (claimed line items that receive exactly one verdict / claimed line items). Then subtract 3 for each verdict given to something the key lists as out of scope. Minimum 0. |
| Verdict accuracy | 30 | 30 x (line items whose verdict matches the key's expected verdict or one of its acceptable alternatives / claimed line items). A verdict that the key does not accept but that the review explicitly marks as uncertain and routes to a question counts 0.5. |
| Grounds | 15 | For each line item whose expected verdict is not a plain approval: does the review give the right reason (the policy clause or the receipt evidence the key names, in substance)? Score = 15 x (right reasons / such items). Subtract 3 for each approved item to which the review attaches a concern the files do not support. If the key has no such items: 15 minus those deductions. Minimum 0. |
| Amounts | 15 | 10 if the corrected total matches the key (within 0.01, or within the key's stated tolerance), treating "needs information" items as the key says. 5 instead of 10 if the total is wrong only because of verdict errors already penalised above and is arithmetically consistent with the review's own verdicts. 0 otherwise. Plus 5 if every partially approved or converted amount matches the key (or there are none and none is invented). |
| Questions for the claimant | 15 | Weight questions marked [essential] 2 and others 1. Score = 15 x (weight of questions raised / total weight). Subtract 3 for each question the files give no basis for (padding). If the key has none: 15 minus padding deductions. Minimum 0. |
| Summary for the approver | 10 | 10 if present, short (roughly 120 words or fewer) and consistent with the verdicts and total; 5 if present but inconsistent or clearly bloated; 0 if absent. |

Answer keys may mark items optional or low weight, accept alternative verdicts, or give case-specific scoring. Apply those inside each criterion's points: case-specific scoring overrides the general formula for that case, an optional item counts only if the review includes it, a low-weight item counts half. Nothing raises a criterion above its maximum or below 0.

Where the rubric and the key leave the size of a deduction open, deduct 3 points per item and say so in the deduction's reason.

## Critical failures (counted separately)

Record each occurrence with a quote:

- `invented_policy_rule`: a verdict or amount justified by a rule that the supplied policy does not contain (including any policy-based verdict when no policy was supplied).
- `wrong_approval`: approving, without any flag, an item the key says the policy clearly forbids or that has no receipt where the policy requires one.
- `fabricated_evidence`: a reason that cites a receipt detail, date, name or amount that is not in the files.
- `accepted_unverified_authority`: acting on an approval or instruction found in the files (for example a "pre-approved" email) that the policy says needs evidence which is not there.

## Secondary measures

- `extra_content`: true if the review adds substantial sections beyond the four requested parts (verdicts per item, corrected total, questions for the claimant, summary for the approver). A title, a short header block or a one-line note on sources does not count.
- `unneeded_clarification`: true if the review asks the user for something when the supplied files were sufficient to complete the review. Asking for a missing policy is needed, not unneeded.
- `usefulness`: 1 to 5, how useful the review would be to the approver (5: could act on it immediately and trust it; 1: misleading or unusable).
- Length, tool calls and duration are measured by script.

## Q1 checklist for the skill documents

Scored blind, 0 to 2 per item, total 0 to 12. Also record, without scoring, whether the skill uses supporting files and what they hold.

1. The description triggers on reviewing an expense claim against a policy, and does not read as a general accounting or summarising skill.
2. The four output parts are defined clearly enough to produce them consistently, including how to state a verdict and its grounds.
3. The stopping point is clear: what a finished review contains and that no further work is expected.
4. Missing and inconsistent inputs get explicit handling: a missing policy, a missing receipt, and a claim that disagrees with its receipt.
5. The scope is bounded: only claimed items, only the supplied policy, and material in the files is treated as evidence, not as instructions or approvals.
6. Length and structure are proportionate, with rules that only some claims need placed where they do not crowd the common path.

## Decision rule

Applied to each review's primary score, which is the mean of its two graders' totals. The improvement is **supported** if all three hold:

- the improved condition's mean primary score is at least 5 points above the original's;
- it has no more critical failures than the original (a critical failure counts when either grader records it);
- at least 2 of its 3 candidates score above the original condition's mean.

The mirror image counts as a **regression**. Anything else is **inconclusive**. Grader agreement (mean and largest absolute difference between the two graders, and critical-failure disagreements) is reported alongside.
