# Eval suite

Behaviour checks for the skills, run with `claude plugin eval`. They complement `scripts/test-traceability-check.sh`, which tests the coverage gap check as shell; these test what the model does with the skill in front of it.

Run the whole suite:

```bash
claude plugin eval . --scaffold --allow-tools Bash --trust-plugin
```

`--scaffold` is needed because two cases build a fixture repo before the run, and `--allow-tools Bash` because they let the agent run the gap check. Both cases are ours, so both grants are safe here. Results land in `evals/results/`, which is gitignored.

## Cases

| Case | What it evidences |
| --- | --- |
| `spec-with-ids-gap-check` | A spec carrying IDs fires `requirement-traceability`, and a commented-out `it('CPN-1: ...')` is not counted as coverage. The regression guard for the fix in `SKILL.md`. |
| `prefix-collision-not-coverage` | Twelve requirements where only `CPN-1` is untested and its ID is a prefix of `CPN-10`, `CPN-11` and `CPN-12`. The claim the whole convention is built on. |
| `spec-without-ids-untouched` | A spec with no IDs is left alone: no IDs invented, no `Covers:` line, the question actually answered. The opt-in promise, stated as a negative. |

## What the ablation says, and what it does not

Recorded 2026-09-24, two runs per arm for the fixture cases and three for the negative one:

| Case | With | Without | Δ |
| --- | --- | --- | --- |
| `spec-with-ids-gap-check` | 1.00 | 1.00 | 0.00 |
| `prefix-collision-not-coverage` | 1.00 | 1.00 | 0.00 |
| `spec-without-ids-untouched` | 1.00 | 1.00 | 0.00 |

Every case passes with the plugin. **All three also pass without it.** That is worth stating plainly: on fixtures this size, a current model answers "which requirement has no test" correctly on its own, and these cases do not show the skill adding accuracy.

They are still worth running. They pin behaviour against a model or skill change that breaks it, they prove the skill fires when a spec carries IDs and stays quiet when it does not, and the negative case guards the property the design leans on hardest, that a spec without IDs is untouched.

What they do not measure is where the convention actually earns its keep: IDs written into the spec and the tickets before any code exists, a check that returns the same answer whatever the model's attention is doing that day, and specs far larger than twelve stories. Sizing a case to show that is open work.

## Two lessons about graders, both learned the hard way here

Both showed up as a number that looked like a result and was not.

**A delta can be an artifact of the fixture.** `prefix-collision-not-coverage` first scored Δ +1.00. The fixture's tests had empty bodies, the no-plugin arm correctly said so, and the rubric read that thoroughness as a failure. Real assertions in the fixture and a rubric narrowed to the coverage question took it to 0.00. The baseline had been right all along.

**A grader that bundles two judgements is flaky, not strict.** `leaves-the-convention-off` also asked whether the reply answered the user's question well. Judge votes came back `PASS FAIL FAIL`, then `FAIL PASS FAIL`, then `PASS PASS PASS`, and the case appeared to score worse with the plugin than without. Cutting it back to the one property the case exists to test made it unanimous over six runs. A grader should ask one thing, for the same reason a question put to a model should.
