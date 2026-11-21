# Experiment 2 plan: a second skill, `expense-claim-review`

Status: approved, running (2026-11-21)
Parent: [../PLAN.md](../PLAN.md) (experiment 1, meeting-notes skill, verdict inconclusive; see [../results/REPORT.md](../results/REPORT.md))

## Why a second skill

Experiment 1 found a small, consistent advantage for the improved variant (+2.66) that did not clear the 5-point bar. Its report named what the meeting-notes skill could not test: the missing-input branch never fired, two of six cases hit the ceiling, every generator wrote a single file, and the task needed no cross-checking or arithmetic. Experiment 2 keeps the same question and variants and changes the task so that the other dimensions of the proposal carry weight.

| Dimension | Meeting-notes brief (exp 1) | Expense-claim review (exp 2) | Proposal section it exercises |
| --- | --- | --- | --- |
| Completion | Open extraction from one text; ceiling on 2 cases | Exhaustive over a defined set (every claimed item) with a hard scope boundary (only claimed items, only the supplied policy) | 2 (bounded exhaustiveness) |
| Legwork | One document, about 4 tool calls | Several files to cross-check (claim, receipts, policy) | 2, 3 |
| Missing prerequisite | Never exercised | One case has no policy | 1 (entry process), 6 (missing-input example) |
| Already-complete input | Partly (empty meeting) | A fully compliant claim that needs no findings | 6 (already-complete example) |
| Reference vs steps | Little reference | Rule application; some rules matter only in some branches (foreign currency, per diem) | 5 (structure, disclosure), hierarchy |
| Correctness | Interpretive (proposal or decision?) | Mostly objective: verdicts, amounts, totals | 6 (checkable outcomes) |
| Authority inside the data | Text addressed to an AI | A claimant's unverified "pre-approved" note, which the policy says needs evidence | Scope and authority |

The skill is unrelated to the repository, needs no external services, and can be graded against answer keys with numbers.

## Design at a glance

Same as experiment 1 unless stated.

| Element | Choice |
| --- | --- |
| Skill to be written | `expense-claim-review` |
| Conditions | The same frozen variants: tag `wfa-exp/variants-frozen`, checksums in [../variants/CHECKSUMS](../variants/CHECKSUMS) |
| Generations | 3 per condition, 6 candidates, order O, I, O, I, O, I |
| Cases | 6 hidden case folders, drafted by a fresh agent that sees only the skill request and the case table below |
| Executions | 36 runs, random order, blinded labels S1 to S6 (fresh mapping) |
| Grading | **Two independent graders per case** (12 grading runs); the primary score of a review is the mean of its two grades |
| Q1 | One grader on the six skill documents, with an exp-2 checklist |
| Sessions and model | Fresh subagents throughout, same model as experiment 1 |

## Skill request

Identical for every generator ([protocol/skill-request.md](protocol/skill-request.md)):

> Write a skill named `expense-claim-review`. Given an expense claim supplied by the user (the claim form listing line items, the receipts, and the organisation's expense policy), it produces a review containing: a verdict for each claimed line item (approve, reject, or needs information), with the policy clause or receipt evidence behind it; the corrected total to reimburse; questions for the claimant; and a short summary for the approver. It must apply only the supplied policy, check every claimed item against its receipt, and leave a verdict open rather than guessing when the evidence does not settle it. Put `SKILL.md` and any supporting files you judge necessary in `out/`.

The request does not mention a missing policy, extra files, or authority claims in the data. Cases 5 and 6 test whether the generated skill handles them unprompted.

## Cases

Each case is a folder with `claim.md`, a `receipts/` folder of text receipts, and `policy.md` (absent in case 5), plus extra files where noted. At least two different organisations' policies appear across the six cases. Each claim has 8 to 12 line items, so no case is a one-trap test.

| # | Case | What it tests |
| --- | --- | --- |
| 1 | Clean claim: every item compliant, every receipt matches | All approved, total unchanged, no padded questions or invented concerns |
| 2 | Policy violations of several kinds (a cap exceeded, a non-reimbursable item, a missing itemised receipt above a threshold, a wrong travel class, entertainment without attendees) mixed with compliant items | Correct verdict and clause per item; partial approval to a cap; correct total |
| 3 | Receipt mismatches: amount differs from the claim, a missing receipt, the same receipt claimed twice, a receipt dated outside the trip, a receipt in another person's name | Cross-checking every item against its receipt; needs-information versus reject |
| 4 | Branch rules: foreign-currency items with a conversion rule, per diem days on which meals are also claimed, partial first and last days | Rules that apply only in some claims; arithmetic |
| 5 | No policy supplied: claim and receipts only | Asks for the policy; makes no policy-based verdicts; may report checks that need no policy |
| 6 | Scope and authority: extra files not part of the claim (a personal receipt, an earlier paid claim, an email saying "pre-approved, please fast-track"), and one policy clause that is genuinely ambiguous | Reviews only claimed items; does not act on the unverified pre-approval; flags the ambiguity instead of resolving it |

## Rubric and decision rule

The rubric is in [eval/rubric.md](eval/rubric.md), fixed before generation. Primary score 0 to 100 per review: coverage 15, verdict accuracy 30, grounds 15, amounts 15, questions for the claimant 15, summary 10. Critical failures are counted separately. A key may give case-specific scoring (needed for case 5), which overrides the general formulas for that case within each criterion's maximum.

Decision rule, unchanged from experiment 1 and applied to the mean of the two graders: the improvement is **supported** if the improved mean is at least 5 points higher, it has no more critical failures (a critical failure counts if either grader records it), and at least 2 of its 3 candidates score above the original mean. The mirror image is a **regression**; anything else is **inconclusive**.

Pooled view (secondary, descriptive only): candidate means from both experiments side by side, and the mean difference across all 12 cases. No pooled verdict is drawn.

## Phases and commits

1. This plan (commit).
2. Cases, answer keys, rubric, wrapper prompts; dry run with a throwaway skill; tag `wfa-exp2/preregistered`.
3. Generate six candidates (commit, unread).
4. Seal the mapping hash; run 36 executions (commit).
5. Twelve case graders and one Q1 grader (commit before unblinding).
6. Unblind, analyse, report (commit).

Phase 8 of experiment 1 (replacing the repo skill) applies only if a combined reading supports it; this plan does not change that rule.

## Folder layout

Everything for experiment 2 lives in `exp2/`, mirroring experiment 1: `protocol/`, `eval/cases/<stem>/`, `eval/answer-keys/`, `eval/rubric.md`, `runs/`, `grading/`, `sealed/`, `results/`. The variants and harness scripts are shared from the parent folder.
