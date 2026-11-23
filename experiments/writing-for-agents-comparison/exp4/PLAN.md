# Experiment 4 plan: the decisive test of revision 2

Status: pre-registered (commit `59242e2`), 2026-11-21. Igor approved the plan ("Execute this plan"). Parent: [experiment 3 extension](../exp3/extension/PLAN.md).
Branch: `writing-for-agents-improvement` on `gpazevedo/skills`, under `experiments/writing-for-agents-comparison/exp4/`.

## Question

Does revision 2 of `writing-for-agents` reduce the error of the skills it helps write, compared with the original, by at least 20%?

Error is the distance from a perfect score: 100 minus the mean primary score. Error reduction = (V2 mean minus O mean) divided by (100 minus O mean). With 90.34 against 92.48, as in the extension, the reduction is 22%.

## What changes from experiments 1 to 3

| Item | Before | Experiment 4 |
| --- | --- | --- |
| Threshold | 5 points | Pooled error reduction of at least 20%, plus a significance test |
| Candidates per condition | 18 (6 per part) | 30 (10 per part) |
| Part c cases | No as-of time, length bound no handoff met | As-of time in every case, length bound set from a dry run |
| Generation log | Has a "tested" field | Field removed, so testing can be compared between conditions |
| Description trigger check | Not run | Run (see Phase 6) |

## Design

- **Conditions:** original (O) and revision 2 (V2), frozen as at tag `wfa3x/preregistered` (checksums in `variants/CHECKSUMS-v2` and `EVAL-CHECKSUMS` here).
- **Parts:** a (meeting notes to decision brief), b (expense claim review) and c (support escalation handoff), with six hidden cases each. Parts a and b use the experiment 1 and 2 cases, keys and rubrics unchanged. Part c uses the corrected set in `c-support-handoff/eval/`.
- **Candidates:** G1 to G12 per part (6 per condition) are reused. G13 to G20 are new: 4 per condition per part, alternating O, V2, O, V2, ..., so 10 per condition per part and 30 per condition in total. The new ones are 24 generations: 4 x 3 parts x 2 conditions.
- **Part c reruns:** its cases change, so all 20 part-c candidates are executed again on the corrected cases. Parts a and b keep the existing outputs of their 12 old candidates and execute only the 8 new ones.
- **Execution count:** 48 runs each for parts a and b, and 120 for part c, so 216 runs in total, in random order.
- **Grading:** all 20 candidates in a part are graded together under fresh labels S1 to S20 and fresh random output ids, two graders per case, so 36 case-grader runs, plus one Q1 grader per part on the 20 skill documents. Rubrics are unchanged, except that part c's concision criterion uses the new length bound.
- **Isolation:** as before. Every generator, runner and grader is a fresh agent with a clean context. Generators never see cases or keys, and the label map stays sealed until all grades are committed.

## Part c corrections (made before this tag; see `c-support-handoff/eval/README.md`)

1. **As-of time.** Every `thread.md` gets an "As-of time" line, equal to the escalation time that the answer key already uses as the time of judgement. It tells the runner to treat that time as the current time and not to use its machine's clock. Keys, facts and all other case content are unchanged.
2. **Length bound.** Dry run: two fresh agents with no skill, shown cases 01 and 03 (not the keys), were told to write the shortest complete handoff. They produced 707 and 1,047 words of own prose (files in `dry-run/`). The concision criterion becomes 10 for 800 words or fewer, 5 for 801 to 1,200, 0 beyond. The old bound (350 and 600) was unreachable. The dry-run handoffs are throwaway and not scored.

## Generation

Same prompt as experiment 3 with one change: the genlog has no `tested` or `testing_note` field ([protocol/generation-prompt.md](protocol/generation-prompt.md)). Each generator's `scratch/` folder is collected, and a generator counts as having tested if it left any file there. This is an imperfect proxy (a generator can test without files), and the new generators are not directly comparable with the reused ones on this point, because the reused ones were asked about testing.

## Decision rule (pre-registered before any new generation)

The unit is the candidate. A candidate's score is the mean over its 6 cases of the mean of the two graders' totals. A condition's mean in a part is the mean of its 10 candidates. The pooled mean takes each condition's mean over the three parts, with parts weighted equally. Pooled error reduction = (V2 pooled minus O pooled) / (100 minus O pooled).

The revision is **supported** if all three hold:

1. The pooled error reduction is at least 20%.
2. A stratified one-sided permutation test gives p < 0.05. It shuffles the O and V2 labels among the 20 candidate scores within each part (10 and 10) and uses the pooled error reduction as its statistic. The space is 184,756 cubed labelings, too many to enumerate, so p is a Monte Carlo estimate with 1,000,000 draws and a fixed seed (`20261121`), computed as (hits + 1) / (draws + 1), and its standard error is reported. The only clarification to the approved plan: it said "exact"; exact is infeasible at this size. The new-candidates-only test (70 cubed labelings) is enumerated exactly.
3. V2 has no more critical failures than O. A critical failure is counted once per output when either grader records one, as in experiments 2 and 3.

The mirror image, with O ahead by the same margin (O's error reduction relative to V2 at least 20%, p < 0.05, O no more critical failures), is a **regression**. Anything else is **inconclusive**. If the repo skill is to change, that happens only on "supported", as in Phase 8 of the original plan.

## Secondary and descriptive analyses

1. Result on all 30 per condition (primary), on the 12 new candidates per condition alone, and on the 18 reused alone.
2. Result without case b-05 (the case with no policy that shaped revision 2): pooled reduction and p.
3. Per-part means, per-part error reduction, per-case means, candidate means and their spread.
4. Critical failures by type; V2 minus O on c-04, c-05 and b-05.
5. Output length, `extra_content`, `unneeded_clarification`, usefulness, and the number of part-c handoffs that mention the sandbox date.
6. Q1 on the 20 skills per part, and process (scratch files left by the new generators).
7. Grader agreement, and the reused a and b candidates' scores here against their extension scores (a consistency check on regrading).

## Honest limits to state in the report

- The 18 reused candidates per condition were scored before this rule existed, and their pooled reduction (about 22%) is known. The report gives the result on all 30 and on the 12 new candidates alone.
- Part c's old outputs are discarded, so part c is a fresh measurement for all 20 candidates.
- One model writes, runs and grades everything, and the cases are synthetic.
- The expense case with no policy shaped revision 2. It stays in, and the report shows the result without it.
- The generation prompt differs from the reused candidates' (no `tested` field).

## Phases

1. **Recover the repo.** Done: branch checked out at `6e40b11`, six existing tags verified.
2. **Fix part c.** Done: as-of time in every case; dry run set the length bound.
3. **Pre-register.** This plan, the decision rule, the corrected part-c cases and the length bound, the protocol prompts, harness and analysis, the trigger-test protocol, and `EVAL-CHECKSUMS`. Commit it as `59242e2`. After this commit, changes to cases, keys, rubric or rule need Igor's approval.
4. **Generate.** 24 fresh generators, alternating O and V2, each in a sandbox holding only its variant and the skill request.
5. **Execute.** Seal a new label map for the 20 candidates per part and commit its hash. Then run the 216 executions.
6. **Check the description.** Run [trigger-test/PROTOCOL.md](trigger-test/PROTOCOL.md). Report it separately from the verdict.
7. **Grade and unblind.** Run the 36 case-grader runs and 3 Q1 runs, commit all grades, then commit the label map and check its hash.
8. **Analyse and report.** Run [analysis.py](analysis.py), write `REPORT.md` with the verdict, and add it to the project and to the explainer doc.
9. **Apply the result, only if supported.**
