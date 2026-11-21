# Report: original vs improved `writing-for-agents`

Run on 2026-11-21 under [PLAN.md](../PLAN.md). All numbers come from [scores.csv](scores.csv) and [summary.json](summary.json), produced by [analysis.py](analysis.py).

## Verdict: inconclusive

The improved variant pointed the right way on every measure but did not clear the pre-registered bar.

| Decision-rule condition | Result | Met |
| --- | --- | --- |
| Improved mean at least 5 points above original | 96.72 vs 94.06, a difference of +2.66 | No |
| No more critical failures than original | 0 vs 0 | Yes |
| At least 2 of 3 improved candidates above the original mean (94.06) | 3 of 3 (98.87, 96.65, 94.65) | Yes |

Under the rule this is **inconclusive**, so Phase 8 does not apply and `skills/productivity/writing-for-agents/` stays unchanged.

## Q2: behaviour in use (primary)

### By candidate

| Condition | Label | Generator | Mean of 6 cases |
| --- | --- | --- | --- |
| Original | S5 | G3 | 95.07 |
| Original | S1 | G5 | 93.78 |
| Original | S4 | G1 | 93.33 |
| Improved | S2 | G6 | 98.87 |
| Improved | S3 | G2 | 96.65 |
| Improved | S6 | G4 | 94.65 |

Spread across the three candidates (standard deviation of candidate means) was 0.90 for the original and 2.11 for the improved condition. One improved candidate, S2, carries much of the gap. Without S2 the difference falls to +1.59; without S6 it rises to +3.70.

### By case

| Case | Original | Improved | Difference |
| --- | --- | --- | --- |
| 01 clear | 93.00 | 98.00 | +5.00 |
| 02 proposals | 96.67 | 100.00 | +3.33 |
| 03 missing | 98.83 | 100.00 | +1.17 |
| 04 conflicts | 91.70 | 94.47 | +2.77 |
| 05 empty | 91.67 | 93.67 | +2.00 |
| 06 injection | 92.50 | 94.20 | +1.70 |

The improved condition scored higher on all six cases, but every difference is small.

### By criterion (mean points)

| Criterion (max) | Original | Improved |
| --- | --- | --- |
| Decision recall (25) | 23.30 | 24.07 |
| Decision precision (20) | 19.22 | 20.00 |
| Evidence fidelity (10) | 10.00 | 10.00 |
| Actions (20) | 19.50 | 19.67 |
| Open questions and contradictions (15) | 12.58 | 13.54 |
| Handoff summary (10) | 9.44 | 9.44 |

Most of the gap comes from open questions (fewer invented or padded questions) and decision precision (no improved brief listed a non-decision as a decision; three original briefs did, all from one candidate, S4, for 3.5 to 7 points each).

### Critical failures and the hard cases

- **No critical failures in any of the 36 briefs.** No brief invented an owner, deadline or decision, and none followed an embedded instruction.
- **Case 06 (injection) did not separate the conditions.** All six briefs reported the budget as not approved, kept every stated owner and deadline, and kept the water leak. None of the six skills says what to do with instructions inside the notes (Q1 item 5 scored 1 for all six), so this robustness came from the model, not from either variant's guidance.
- **Case 04 (conflicts).** All six surfaced the reversed pour date and both traffic-plan deadlines. Five of six listed the rain fallback (key D2) as a proposal rather than a decision, because their skills treat a flat statement with no agreement wording as ambiguous. Only S2 (improved) scored 100.
- **Case 05 (empty).** All six correctly reported no decisions and no actions. Scores differed on padded open questions and brief length.

### Secondary measures

| Measure | Original | Improved |
| --- | --- | --- |
| Brief length, mean words | 888 | 742 (-16%) |
| Briefs flagged `extra_content` | 18 of 18 | 11 of 18 |
| Unneeded clarifying questions | 0 | 0 |
| Usefulness (1 to 5) | 4.17 | 4.44 |
| Runner tool calls, mean | 3.72 | 3.50 |
| Runner duration, mean | 47.8 s | 39.6 s |

The `extra_content` flag mostly records a fifth "Proposals (not decided)" section. Five of six skills added one; only S2 kept to the four requested parts, which accounts for all seven unflagged improved briefs (S2's six and one S6 brief).

## Q1: the skill documents (secondary)

Mean checklist score: original 10.0 of 12, improved 10.67 of 12.

Item 3 (a clear stopping point) split exactly by condition: all three improved skills say to deliver the brief and stop (S2, S3, S6), and none of the original ones does (S1, S4, S5). The same three improved skills also say what to do when no notes are supplied (ask and stop). All six define the four parts well and all six miss instructions in the notes (item 5). S6 lost a point on length (about 910 words, with some repetition).

## Characteristic differences

These follow the proposal's sections, but with n = 3 they are observations, not established effects.

1. **Bounded completion (proposal sections 1 and 2).** Every improved skill has an explicit stop and a missing-input branch; no original skill has either. In this evaluation no case lacked notes, so the missing-input branch was never exercised.
2. **Behavioural walkthrough (section 6).** All three improved generators walked example inputs through their draft and changed rules as a result (G2 changed two rules, G4 cut two lines, G6 checked four cases). None of the original generators tested its draft. The original variant only says to "settle it by running the document", without a procedure.
3. **Scope discipline.** The best candidate (S2, improved) was the only one that produced exactly the four requested parts, and its briefs were the shortest (mean 568 words). The other two improved candidates added the same fifth section as the original ones, so this is not a consistent condition effect.
4. **What stayed the same.** Both conditions produced single-file skills of 580 to 910 words with the same overall shape: classification rules, ordered steps ending in checkable "done when" conditions, and a template. The original variant already pushes hard on checkable completion criteria, which may explain why the gap is small.

## Reliability

- **Agreement check.** A second grader re-scored 9 random briefs. Mean absolute difference 2.96 points, largest 11 (a case 05 original brief, 83 vs 94, where the first grader applied a 5-point length penalty and more padding deductions). No disagreement on critical failures. The grader disagreement is about the same size as the effect, which is the main reason to read the +2.66 cautiously.
- **Sensitivity.** Replacing the first grader's scores with the second grader's for those 9 briefs gives 94.84 vs 97.42 (+2.58). The verdict is unchanged.
- **Exploratory, not pre-registered.** Of the 20 ways to split the six candidate means into two groups of three, 2 give a gap at least as large as the observed one (about 0.10). This is in line with a real but small effect, and too weak to rely on.
- **Grader arithmetic.** Every grader's total matched the sum of its six scores.

## Limitations

- **Small n.** Three generations per condition; the per-candidate spread (up to 4.2 points within the improved condition) is larger than the condition gap.
- **Ceiling effect.** Cases 02 and 03 scored 96.7 to 100 in both conditions, so two of six cases barely discriminate. Harder cases would give the comparison more range.
- **Case 06 does not test the guidance.** All runners ignored the embedded instructions without being told to, so the case shows model robustness, not skill quality.
- **Same author for the variant and the evaluation.** Claude built the improved variant and wrote the rubric. The cases and keys were drafted by a fresh agent that saw neither variant, which reduces but does not remove this bias.
- **Model-graded scoring** with one grader per case; see the agreement check.
- **Synthetic cases** of 420 to 512 words, shorter and tidier than many real notes.
- **Prompt-based isolation.** Generators, runners and graders ran on the same file system and were told to stay in their sandbox. All self-reported reads stayed inside it. Two graders (cases 04 and 06) wrote a helper script to `/tmp/wfa-grade-scripts/`, outside their sandbox; they report reading nothing outside it.
- **Same model throughout** (Claude Opus 5.5, inherited by fresh subagents), so the result says nothing about other models.

## Deviations from the plan

- Checkpoints A and B skipped, and Claude wrote the cases, per decisions 3 and 4.
- Phase 3 changed the grading prompt (briefs grouped by case folder; a 3-point tie-break where rubric and key leave a deduction's size open; evidence may appear anywhere in the brief). The rubric, cases, keys and decision rule were not changed after the `wfa-exec/preregistered` tag, which was moved to the dry-run fix commit as the plan allows.
- After all grading had finished, the Q1 grader's reported word count let the orchestrator infer one label (S6 = G4). No grading was affected.

## Follow-ups worth testing

1. **Harder cases** with less ceiling: longer, messier notes; several interleaved reversals; owners referred to by role or initials; a mix of minutes and chat transcript.
2. **More generations** (for example 6 to 8 per condition) to bring the candidate spread under the effect size.
3. **Ablations** of single proposal sections, starting with section 6 (behavioural check) and sections 1 and 2 (entry process and bounded completion), which produced the clearest document-level differences.
4. **A missing-notes case and an ambiguous-scope case**, which the improved skills handle explicitly and this evaluation never exercised.
5. **Two graders per brief by default**, given that grader disagreement matched the effect size.
