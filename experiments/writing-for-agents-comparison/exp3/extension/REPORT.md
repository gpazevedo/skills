# Report: experiment 3 extension, six candidates per condition

Plan: [PLAN.md](PLAN.md) (tag `wfa3x/preregistered`). Conditions: the original skill (O) and the revision-2 variant (V2). Each part now has 6 candidate skills per condition: the 3 from experiment 3 plus 3 new ones (G7 to G12). All 12 candidates per part were regraded together under fresh labels, two graders per case. Figures come from [summary.json](summary.json) and each part's `scores.csv`.

## Verdict: inconclusive in all three parts, with V2 ahead in all three

| Part | Skill written | O | V2 | V2 minus O | V2 candidates above O mean | Critical failures (O / V2) | Verdict |
| --- | --- | --- | --- | --- | --- | --- | --- |
| a | meeting notes to decision brief | 94.04 | 95.91 | +1.87 | 6 of 6 | 1 / 0 | inconclusive |
| b | expense claim review | 93.53 | 96.61 | +3.08 | 6 of 6 | 1 / 0 | inconclusive |
| c | support escalation handoff | 83.46 | 84.92 | +1.46 | 4 of 6 | 5 / 1 | inconclusive |
| Pooled (descriptive) | | 90.34 | 92.48 | +2.14 | 16 of 18 | 7 / 1 | |

V2 met two of the three conditions for "supported" in every part: no more critical failures than O, and at least 4 of 6 candidates above O's mean. It missed the third: no part reached the 5-point threshold. Under the pre-registered rule every part is inconclusive, and the repo skill stays unchanged.

The extra candidates changed the picture in one way. With 3 per condition, experiment 3 had V2 ahead in two parts and behind in one (part c, −0.67). With 6, V2 is ahead in all three parts, and in parts a and b every V2 candidate beat the O mean.

## How much the extra candidates mattered

**By batch.** V2 minus O within the original three candidates and within the new three:

| Part | First batch (G1 to G6) | New batch (G7 to G12) |
| --- | --- | --- |
| a | −0.39 | +4.14 |
| b | +2.21 | +3.93 |
| c | +0.89 | +2.02 |

The direction held in every batch except part a's first, and one batch of three moved part a by about 4.5 points. That is the noise the extension was meant to reduce, and it is about as large as the effect.

**Spread between candidates.** The SD of candidate means within a condition was 2.03 (O) and 0.96 (V2) in part a, 4.23 and 1.15 in part b, and 3.26 and 3.67 in part c. V2 skills were more consistent in two parts.

**Exploratory significance check (not pre-registered).** An exact one-sided permutation test on the 12 candidate means per part (V2 vs O labels shuffled, 924 splits) gives p = 0.036 for part a, 0.063 for part b and 0.232 for part c. These are three uncorrected tests chosen after seeing the data, so they suggest a real but small effect without establishing one.

## Missing and partial inputs

| Case | What is missing | O | V2 | V2 minus O |
| --- | --- | --- | --- | --- |
| c-04 no policy | the support policy | 70.48 | 85.12 | +14.64 |
| b-05 no policy | the expense policy (biased: shaped revision 2) | 81.08 | 96.25 | +15.17 |
| c-05 partial thread | the start of the ticket thread | 81.42 | 79.53 | −1.89 |

c-04 is where the critical failures concentrate: 5 of the 6 O candidates supplied a service-level deadline that the inputs did not contain (`invented_service_term`), against 1 of 6 V2 candidates. Five V2 candidates scored 86.7 to 90 on the case; one O candidate did (88.35). With six candidates the c-05 gap shrank from −5.83 to −1.89.

## Other findings

- **Output length.** V2 outputs were shorter in every part: 658 against 776 words in a, 918 against 1042 in b, 1523 against 2188 in c. Part c's concision criterion still scored 0 for every handoff.
- **Q1, the skill documents.** V2 scored higher in every part: a 11.67 against 8.83, b 11.17 against 9.67, c 11.67 against 8.33 (out of 12). As in experiment 3, the gain sits in the items revision 2 added: an explicit stop, a missing-input branch, and treating supplied material as evidence.
- **The as-of clock in part c.** 24 of the 72 handoffs mention the sandbox date (21 November), which usually means the runner measured service levels against the clock instead of the escalation time. They split 15 V2 and 9 O, concentrated in four skills: G2 and G10 (V2) and G9 and G7 (O). This is a case-design flaw (no as-of time) that hits whichever skill tells the runner to use the environment's clock, and it still pulls V2's part c score down.
- **Process.** All 36 generators tested their skills; the prompt asked them to record it, so this cannot separate the conditions.

## Reliability

| Part | Grader mean abs diff | Largest | Regrade vs first round (first-batch outputs) |
| --- | --- | --- | --- |
| a | 1.33 | 10.5 | r = 0.909, mean abs diff 0.97 |
| b | 0.57 | 5 | r = 0.987, mean abs diff 0.54 |
| c | 1.15 | 8.7 | r = 0.912, mean abs diff 1.66 |

Regrading the same 108 first-batch outputs moved their V2 minus O by up to 1.6 points (part a: +0.55 to −0.39; part c: −0.67 to +0.89; part b: +2.32 to +2.21). Grading noise is therefore about half the size of the effect being measured. There were no critical-failure disagreements between graders.

## Limitations

- Six candidates per condition is still small. A rough calculation from the candidate SDs (about 3 points) suggests about 28 candidates per condition would give an 80% chance of detecting a 2-point difference (one-sided, 5% level). Pooling the three parts gets this design to 18 per condition.
- The 5-point threshold was set in experiment 1, before anything was known about effect sizes. The effect seen here is about 2 points, so this design cannot return "supported" for it. Changing the threshold now would be post hoc; it would need a new pre-registered experiment.
- Part c's cases lack an as-of time and have a concision bound no handoff met. b-05 shaped revision 2.
- Run irregularities ([EXEC-NOTES.md](EXEC-NOTES.md)): one run repeated after a usage-limit interruption, one kept after its final reply failed, one run late. One part-c grader was replaced before unblinding because it had not read one handoff in full ([GRADING-NOTES.md](GRADING-NOTES.md)). Several graders wrote helper scripts outside their sandboxes.
- One model wrote the cases, generated the skills, ran them and graded them.

## What this suggests

- Revision 2 probably helps a little: about 2 points on average, in the same direction across three different skills, with far fewer critical failures (1 against 7), shorter outputs and better skill documents. The clearest gain is on missing inputs, where it stops agents inventing terms the inputs lack.
- The effect is too small for the pre-registered 5-point bar, so the formal verdict stays inconclusive and the repo skill stays unchanged.
- If you want a decisive answer, a fourth experiment would need: an as-of time in every case, length bounds set from a dry run, and a threshold chosen in advance for an effect of this size (for example 2 points), tested on candidate means pooled across parts with about 28 candidates per condition in total.
