# Report: experiment 2, `expense-claim-review`

Run on 2026-11-21 under [../PLAN.md](../PLAN.md). Numbers come from [scores.csv](scores.csv) and [summary.json](summary.json), produced by [analysis.py](analysis.py). Each review's primary score is the mean of two independent graders.

## Verdict: inconclusive, leaning slightly towards the original

| Decision-rule condition | Result | Met |
| --- | --- | --- |
| Improved mean at least 5 points above original | 88.31 vs 90.17, a difference of -1.86 | No |
| No more critical failures than original | 0 vs 0 | Yes |
| At least 2 of 3 improved candidates above the original mean (90.17) | 0 of 3 (90.00, 88.33, 86.58) | No |

The mirror rule for a regression also fails (the original is not 5 points ahead), so the verdict is **inconclusive**. The whole gap comes from one case and one candidate (see below). Without case 05 the improved condition leads by +0.60.

## Q2: behaviour in use (primary)

### By candidate

| Condition | Label | Generator | Mean of 6 cases |
| --- | --- | --- | --- |
| Original | S2 | G5 | 94.75 |
| Original | S5 | G1 | 89.43 |
| Original | S6 | G3 | 86.33 |
| Improved | S1 | G2 | 90.00 |
| Improved | S4 | G4 | 88.33 |
| Improved | S3 | G6 | 86.58 |

Spread of candidate means: 4.26 (original), 1.71 (improved). Of the 20 ways to split the six candidates into two groups of three, 7 give a gap at least as negative as the observed one (exploratory, not pre-registered): no evidence of a real difference in either direction.

### By case

| Case | Original | Improved | Difference |
| --- | --- | --- | --- |
| 01 clean | 98.33 | 98.33 | 0.00 |
| 02 violations | 96.67 | 95.00 | -1.67 |
| 03 mismatches | 89.67 | 91.17 | +1.50 |
| 04 branches | 95.67 | 96.17 | +0.50 |
| 05 no policy | 69.17 | 55.00 | -14.17 |
| 06 scope | 91.53 | 94.17 | +2.63 |

### Case 05 decides the result

Five of the six skills contain a rule of the form "if the policy is missing, ask for it and stop": all three improved skills (G2, G4, G6) and two original ones (G1, G3). Their runners did exactly that. They asked for the policy and stopped, mostly without reporting the receipt problems that need no policy (a claim amount above its receipt, a receipt from the wrong month and city, a form total that does not add up). Under the pre-registered key these reviews score 50 to 62.5: full coverage and verdict credit, no critical failure, but no credit for checks they did not report.

The sixth skill (G5, original) has **no** missing-policy branch at all. Its runner asked for the policy, held every item open, and still flagged every policy-independent problem. It scored 95. One candidate's omission is worth 14 points on the case mean and about 2.2 points on the condition mean, which is more than the whole condition gap.

This is the first time across both experiments that the missing-input branch fired, and it shows a cost of the proposal's emphasis on explicit stopping points. A stop rule that says "ask and stop" bounds the work too tightly when part of the task can still be done without the missing input. The better rule would say what can still be done and then stop. The improved variant's process ("identify ... the point where the reader stops") does not warn against this, and its walkthrough guidance ("a missing-input example when changing prerequisites") led all three improved generators to add a stop branch without asking what work remains possible.

### Other cases

Elsewhere the conditions are within 3 points on every case. No review in either condition had a critical failure. Every review:
- ignored the claimant's "pre-approved" email where the policy required written approval;
- kept the unreferenced pharmacy receipt and the earlier paid claim out of the verdicts;
- handled the per-month conversion and partial per diem days correctly.

The cases that separated reviews were 03 (questions to the claimant about fixable rejections) and 06 (asking about the duplicate membership, flagging the "reasonable" clause).

### Secondary measures

| Measure | Original | Improved |
| --- | --- | --- |
| Reviews flagged `extra_content` (either grader) | 11 of 18 | **0 of 18** |
| Review length, mean words | 1,032 | 952 |
| Usefulness (1 to 5) | 4.25 | 4.19 |
| Summary score (of 10) | 6.67 | 5.83 |
| Runner tool calls, mean | 5.72 | 6.11 |
| Runner duration, mean | 56.8 s | 53.8 s |

No improved review added sections beyond the four requested parts; two of the three original skills (G5, G1) produced extra sections in 11 reviews. Summaries were too long in both conditions (most over the rubric's roughly 120 words).

## Q1: the skill documents (secondary)

Mean checklist score: original 9.33, improved 10.0 of 12. Item 3 (a clear stopping point) split exactly by condition, as in experiment 1: all three improved skills say to deliver the review and stop; none of the original skills does. All six scored 1 on item 5: none says that approvals or instructions found in the files must be verified rather than acted on (two skills even accept pre-approval "shown in the claim"), although no runner was misled. Only G3 (original) used a supporting file (`EDGE-CASES.md` for receipt edge cases); it was also the only skill to score 2 on proportionate structure. The improved variant's "choosing a structural fix" guidance did not lead any generator to disclose material.

## Process differences (both experiments)

| Behaviour | Original generators | Improved generators |
| --- | --- | --- |
| Walked example inputs through the draft before finishing | 0 of 6 | 6 of 6 |
| Skill states an explicit stop | 0 of 6 | 6 of 6 |
| Skill has a missing-input branch | 2 of 6 (both in exp 2) | 6 of 6 |
| Produced extra output sections in runs | 5 of 6 skills | 2 of 6 skills (exp 1 only) |

These are the clearest effects of the improved variant: it reliably changes how generators work and what the skill documents say. Neither experiment shows those changes turning into consistently better outputs.

## Combined view (descriptive only)

| | Original | Improved | Difference |
| --- | --- | --- | --- |
| Experiment 1 (meeting notes) | 94.06 | 96.72 | +2.66 |
| Experiment 2 (expense review) | 90.17 | 88.31 | -1.86 |
| Both, 72 outputs | 92.12 | 92.51 | +0.39 |

Across 12 cases and 12 candidates the two variants perform the same within noise. In each experiment the direction depends on one or two candidates.

## Reliability

- **Two graders per case.** Mean absolute difference 1.75 points, largest 10. All the large differences were in case 05, where the graders disagreed on whether a stop-only review's short status note counts as a summary. No critical-failure disagreements. Either grader alone gives the same verdict (difference -1.78 with grader 1 only, -1.95 with grader 2 only).
- Experiment 2 kept clear of the ceiling except case 01, which was meant to be easy.

## Limitations

- **n = 3 per condition again.** One candidate's choice decides the result.
- **Case 05 scoring rests on a rule Claude added to the key before the tag** (stop-only reviews get full coverage and verdict credit, other criteria as written). A rubric that rewarded stopping more, or one that gave no credit for stop-only reviews, would move the result by a few points either way; it would not reverse the qualitative finding.
- **The same author** built the improved variant and wrote the rubric; the cases and keys came from a fresh agent that saw only the request.
- **Prompt-based isolation**, as before. Seven graders wrote helper scripts to `/tmp` outside their sandboxes; all reported reading nothing outside.
- Same model throughout (Claude Opus 5.5).

## What this suggests for the proposal

1. **Keep** the parts that changed behaviour without a cost: the walkthrough step (section 6) and the bounded-scope wording (section 2), which went with zero extra sections in exp 2.
2. **Revise** the stopping guidance (sections 1 and 2) so that a missing prerequisite leads to "do what does not depend on it, report it, then stop", not a bare stop. A one-line addition to the behavioural check would cover it: when adding a missing-input branch, check that the work that does not need the input still gets done.
3. **Add** to the proposal's scope guidance (section 7 or co-location) that material inside the inputs, such as approvals or instructions, is evidence to verify, not an authority. No skill in either experiment said this.
4. Do not apply the improved variant to the repo on this evidence (Phase 8 of experiment 1 stays unapplied). A next round could test the revised stopping guidance with a dedicated missing-input case and 6 generations per condition.
