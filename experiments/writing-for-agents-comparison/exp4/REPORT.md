# Experiment 4 report: does revision 2 reduce error by at least 20%?

## Verdict: supported

All three pre-registered conditions hold (commit `59242e2`, `PLAN.md`):

| Condition | Result | Met |
|---|---|---|
| Pooled error reduction at least 20% | O 92.58, V2 94.48, reduction 25.6% | yes |
| Stratified one-sided permutation test p < 0.05 | p = 0.0006 (Monte Carlo, 10^6 draws, SE 0.00002) | yes |
| V2 has no more critical failures than O | O 7, V2 2 | yes |

The mirror test (regression) gives p = 0.9995. Pooling takes each condition's mean over the three parts, equally weighted. Error is 100 minus the mean score.

## By part

| Part | O | V2 | Error reduction | Critical failures O / V2 |
|---|---|---|---|---|
| a, meeting notes | 93.71 | 94.47 | 12.0% | 5 / 1 |
| b, expense review | 94.62 | 96.90 | 42.3% | 1 / 0 |
| c, support handoff | 89.41 | 92.06 | 25.1% | 1 / 1 |

V2 is ahead in every part, but only b and c clear 20% on their own. Part a is below the threshold and its cases are close to ceiling.

## Robustness

- New candidates only (G13 to G20, never seen when the plan was written): O 93.26, V2 95.14, reduction 27.8%, exact p = 0.026 (343,000 labelings), critical failures 2 / 0.
- Reused candidates only (G1 to G12): O 92.13, V2 94.04, reduction 24.3%.
- Without case b-05 (no policy supplied): O 93.24, V2 94.50, reduction 18.6%, p = 0.005. **This is below 20%.** Case b-05 is the largest single gap (O 84.67, V2 96.50). The verdict leans on V2 handling a missing policy better. Excluding that case, V2 is still clearly ahead, but by less than the pre-registered margin.
- Partial-input cases: c-04 +2.2 for V2, c-05 -0.25, b-05 +11.8.

## Other measures

- Skill quality checklist (Q1, 12 points): means O 7.6 / V2 11.2 (a), 9.8 / 11.4 (b), 8.7 / 11.5 (c).
- Output length: V2 outputs are shorter in all three parts (mean words, V2 vs O: a 687 vs 733, b 875 vs 968, c 1,248 vs 1,747).
- Description trigger test, reported separately: both descriptions scored 20 of 20 in all four runs (`trigger-test/RESULTS.json`). The test has a ceiling effect and cannot separate them.

## Limits

- Same-model generation and grading. The two graders disagreed on some scores (mean absolute difference 1.59 points in part a, up to 11.4 on one output), so single scores are noisy. Both graders' totals are averaged.
- Part c's as-of time line and concision bound are pre-registered in `PLAN.md`.
- The permutation test for the full 30-per-condition design is a Monte Carlo estimate, not exact, as noted in the phase 3 commit.
- Q1 part a's first run gave generic justifications and was rerun; Q1 b and c were rerun after rate-limit failures. See `GRADE-NOTES.md`.
- Coordinator subagents could not launch runs; all 216 executions were launched directly. See `EXEC-NOTES.md`.
- Counts: 216 is the number of runs executed in this experiment (parts a and b: 8 new candidates x 6 cases each; part c: all 20 candidates x 6 cases, rerun because its cases changed). Parts a and b reused the stored outputs of their 12 earlier candidates and regraded them, so the graded outputs total 20 x 6 x 3 = 360, each scored by two graders (36 case-grader runs, plus 3 Q1 runs).

## Action taken

Because the verdict is supported, `skills/productivity/writing-for-agents/SKILL.md` and `SKILL-MECHANICS.md` were replaced with the improved-v2 variant. The repo's frontmatter script could not run here (missing node modules); the frontmatter keeps the same `name` and `description` fields and contains no em-dashes.
