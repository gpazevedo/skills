# Experiment 3 extension: six candidates per condition

Status: pre-registered (2026-11-21), before any new candidate exists.
Parent: [experiment 3 plan](../PLAN.md). Its first-round report stays as written in [../results/REPORT.md](../results/REPORT.md).

## Why

Experiment 3 found every part inconclusive, and the spread between candidates of the same condition (up to 9 points in part c) was larger than any difference between conditions. The original's own scores also moved by 1 to 3.5 points from earlier runs. Doubling the candidates per condition reduces that generation-to-generation noise.

## Decisions (confirmed 2026-11-21)

- **Scale:** 3 more candidates per condition in each part, for 6 per condition.
- **Decision rule:** the candidate clause becomes "at least 4 of its 6 candidates". This is a change to a pre-registered part, approved by Igor.
- **Grading:** all 12 candidates per part are regraded together under fresh labels and fresh random ids. The first-round grades stay committed and serve as a consistency check.
- **Part c:** cases, keys and rubric unchanged, with their known flaws (no as-of time, a concision bound every handoff failed), so both batches pool.

## Design

| Element | Choice |
| --- | --- |
| Cases, keys, rubrics, skill requests, variants | Unchanged from experiment 3 (tags `wfa-exp3/preregistered`, `wfa-exp3/variant-frozen`, `wfa-exp/variants-frozen`) |
| Generations | Per part: 6 fresh generators G7 to G12, order O, V2, O, V2, O, V2. Same generation prompt as experiment 3, verbatim, with sandboxes at `/tmp/wfa3x-gen/<part>-G?` |
| Labels | Per part, fresh random labels S1 to S12 over G1 to G12, sealed outside the repo; sha256 committed before execution |
| Executions | The 18 new candidates on the 6 cases of their part: 108 runs in random order, same execution prompts, sandboxes at `/tmp/wfa3x-exec/<part>/S?-C?`. First-batch outputs are reused, not rerun |
| Grading | Two fresh graders per case per part (36 runs), each grading all 12 outputs for the case under fresh random ids; prompts in [protocol/](protocol/), identical in their verbatim part to experiment 3's case-grader prompts. One Q1 grader per part on the 12 skill documents. Committed before unblinding |
| Analysis | [analysis.py](analysis.py), committed with this plan |

## Decision rule (per part)

Applied to the mean of the two regrade grades over all 12 candidates: V2 is **supported** in a part if its mean is at least 5 points above O's, it has no more critical failures (counted when either grader records one), and at least 4 of its 6 candidates score above O's mean. The mirror image is a **regression**; otherwise **inconclusive**. These verdicts are the extension's result; experiment 3's first-round verdicts are not revised.

Phase 8 of experiment 1 (replacing the repo skill) applies only if a part is supported and no part is a regression.

## Secondary analyses (descriptive)

1. **Missing and partial inputs:** V2 minus O on c-04, c-05 and b-05 (b-05 with the bias caveat from experiment 3).
2. **Pooled:** V2 minus O across all three parts.
3. **By batch:** V2 minus O within the first-batch candidates and within the new candidates, to show how much a batch of three can move the difference.
4. **Regrade consistency:** for the 108 first-batch outputs, first-round grades against regrade grades (mean difference, mean absolute difference, correlation, and the first-batch V2 minus O under each).
5. **Q1** on all 12 skills per part, and **process** (generators that tested; contaminated by the genlog prompt, as in experiment 3).
6. **Grader agreement** within the regrade.

## Phases and commits

1. This addendum, the extension prompts, harness and analysis; tag `wfa3x/preregistered`.
2. 18 generations (commit, unread).
3. Sealed mappings (hashes committed); 108 executions (commit).
4. 36 case graders and 3 Q1 graders (commit before unblinding).
5. Unblind, analyse, report (commit).
