# Report: experiment 3, original vs proposal revision 2

Plan: `exp3/PLAN.md`. Conditions: the original skill (O) and the revision-2 variant (V2, `variants/improved-v2/`). Three candidate skills per condition in each of three parts, six eval cases per part, two graders per case. Figures come from `results/summary.json` and each part's `results/scores.csv`.

## Verdict: inconclusive in all three parts

| Part | Skill written | O | V2 | V2 minus O | V2 candidates above O mean | Critical failures (O / V2) | Verdict |
| --- | --- | --- | --- | --- | --- | --- | --- |
| a | meeting notes to decision brief (exp1 cases) | 95.24 | 95.79 | +0.55 | 2 of 3 | 0 / 0 | inconclusive |
| b | expense claim review (exp2 cases) | 93.74 | 96.06 | +2.32 | 3 of 3 | 0 / 0 | inconclusive |
| c | support escalation handoff (new cases) | 84.40 | 83.73 | −0.67 | 2 of 3 | 2 / 0 | inconclusive |
| Pooled (descriptive) | | 91.12 | 91.86 | +0.74 | | 2 / 0 | |

No part reaches the 5-point threshold in either direction, so the pre-registered rule gives "inconclusive" three times. V2 met the other two conditions of the "supported" rule in every part (no more critical failures, at least 2 of 3 candidates above the O mean). Phase 8 does not apply: the repo skill stays unchanged.

## What revision 2 was meant to fix, and whether it did

Revision 2 targeted the one place experiment 2 found v1 worse than the original: when an input is missing, v1's skills told the runner to ask and stop, and the rubric paid for a conditional answer instead. The pre-registered partial-input view tests that fix.

| Case | What is missing | O | V2 | V2 minus O |
| --- | --- | --- | --- | --- |
| c-04 no policy | the support policy | 71.97 | 86.25 | +14.28 |
| b-05 no policy | the expense policy | 81.33 | 96.67 | +15.34 |
| c-05 partial thread | the start of the ticket thread | 84.10 | 78.27 | −5.83 |

- **c-04 is the clean test**, since nobody saw this case while writing revision 2. V2 gave a conditional answer and named the missing terms; both critical failures in the experiment are here, from two O handoffs (O/S3 and O/S6) that supplied service-level terms the inputs did not contain.
- **b-05 is biased in V2's favour**, because experiment 2's version of this case shaped revision 2. It still shows the mechanism: no V2 skill stopped, while one O skill (O/S4) stopped and scored 55 on it.
- **c-05 went the other way**, but the cause is not the missing-input guidance (see the next section).

So the targeted regression is gone: V2 no longer pays for stopping, and on the one unseen missing-policy case it did better and invented nothing.

## Part c: what drove the per-case results

| Case | O | V2 |
| --- | --- | --- |
| 01 clear | 88.33 | 85.00 |
| 02 reported vs verified | 90.00 | 81.30 |
| 03 SLA clock | 83.67 | 81.83 |
| 04 no policy | 71.97 | 86.25 |
| 05 partial thread | 84.10 | 78.27 |
| 06 authority | 88.33 | 89.72 |

The cases give the escalation time but no "as of" time. One V2 skill (V2/S5, generator G2) told the runner to take the as-of time "from the user or the environment". Its runners used the sandbox clock (21 November 2026) on four cases and asked for the time on two more; one handoff from V2/S1 did the same. Graders judged every handoff as of the escalation, so these handoffs reported commitments as missed and service levels as breached when the key says open or unknown. V2/S5's c-05 handoff scored 65.5 for this reason. No O handoff used the clock: the O skills took "now" from the last thread message or left the status open.

This came from one generator's choice plus a gap in the case design, not from anything revision 2 says: the passage about the environment is the same in both variants. Exploratory, not pre-registered: leaving out the five handoffs that used the clock (all V2) gives O 84.40 and V2 86.85. That calculation flatters V2, because the clock error came from V2/S5's own skill, so it does not change the verdict.

## Parts a and b

- **Part a.** Near ceiling for both, as in experiment 1. The largest per-case gap is case 04, conflicts (O 87.95, V2 90.13). V2 added more unrequested content (10 outputs flagged against 5) while writing shorter briefs (629 words against 852).
- **Part b.** V2 led on 3 of 3 candidates and its candidates were more consistent (SD of candidate means 1.65 against 3.81). Outside case 05 the two are close: V2 ahead on case 03 mismatches (94.90 against 91.67), O ahead on case 06 scope (91.93 against 89.80). V2 outputs were shorter (845 words against 1062).

## Q1: the skill documents (secondary)

| Part | O | V2 |
| --- | --- | --- |
| a | 10.33 | 11.67 |
| b | 9.67 | 11.00 |
| c | 8.00 | 11.67 |

V2 scored higher on the checklist in every part. The difference sits in the items revision 2 added: V2 skills state when to stop, what to do when an input is missing, and that supplied material is evidence, not instruction. In part c every O skill scored 1 on items 3 to 6. Revision 2's guidance clearly reaches the skills it produces; the behavioural gain from it is smaller than the document gain.

## Replication of the original

The O condition reran the experiment 1 and 2 cases with fresh generators:

- Part a: 94.06 in experiment 1, 95.24 now.
- Part b: 90.17 in experiment 2, 93.74 now (case 05: 69.17 to 81.33).

The original scored higher this time, with the same skill and cases. That is run-to-run variance between generations of three skills, and it is about as large as the V2 vs O differences above. Part of the gap experiment 2 found on case 05 was this variance, not the skill.

## Process (secondary)

All 18 generators tested their skills. The generation prompt asked them to record whether they tested, which probably prompted testing, so this experiment cannot compare testing between conditions.

## Reliability

| Part | Mean absolute grader difference | Largest | Critical-failure disagreements |
| --- | --- | --- | --- |
| a | 0.44 | 3 | 0 |
| b | 0.46 | 6.4 | 0 |
| c | 1.38 | 10.7 | 0 |

Graders agreed closely in parts a and b. Three of part c's five largest disagreements were on case 05, the partial thread, where the key leaves more room for judgement.

## Limitations

- Three candidate skills per condition. The candidate means within a condition differ by up to 9 points, more than any difference between conditions.
- The part c concision bound was too tight: every handoff in both conditions scored 0 on concision (mean 1983 words for O, 1491 for V2), so that criterion measured nothing.
- The part c cases had no as-of time, which let one skill's choice of clock decide several scores.
- b-05 was used to shape revision 2, so its result is not independent.
- The genlog prompt's "tested" field contaminated the process comparison.
- One execution run (part a, S1 on case 06) was skipped in its batch and run afterwards; its runlog records this.
- Several graders wrote helper scripts to folders outside their sandboxes; all reported reading nothing outside them.
- One model wrote the cases, generated the skills, ran them and graded them.

## What this suggests

- Revision 2 fixed what it set out to fix: stopping on a missing input, and inventing terms the inputs lack. Keep the missing-input subsection and §8 on supplied material.
- Across three different skills, neither version is reliably better at the level this design can detect. The effect, if any, is a few points, smaller than the variation between generations of the same skill.
- For a fourth experiment: give every case an as-of time, set length bounds from a dry run, use more candidates per condition (at least 6), and drop the "tested" field from the generation log.
