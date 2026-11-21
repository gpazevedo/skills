# Experiment 3 plan: original vs revision 2

Status: complete, verdict inconclusive in all three parts (2026-11-21). Report: `results/REPORT.md`.
Parents: [experiment 1](../PLAN.md), [experiment 2](../exp2/PLAN.md), [proposal-v2.md](../proposal-v2.md)

## Question

Does `writing-for-agents` revised by proposal v2 lead an agent to write skills that work better than skills written with the original? As in experiments 1 and 2, behaviour in use (Q2) carries the verdict and the skill documents (Q1) are secondary.

Proposal v2 targets the one cost experiment 2 measured: a missing input led skills to "ask and stop" without doing the work that did not need it. Experiment 3 therefore also pre-registers a look at the cases with a missing or partial input.

## Decisions (confirmed 2026-11-21)

- **Cases:** both a rerun of the experiment-1 and experiment-2 cases, and a new skill with new cases.
- **Conditions:** original vs revision 2 (no revision-1 arm).
- **Scale:** 3 generations per condition per skill.
- Carried over: no checkpoints; a fresh agent writes the new cases; Claude writes rubrics.

## Design at a glance

| Part | Skill | Cases | Rubric and keys |
| --- | --- | --- | --- |
| 3a | `meeting-notes-to-decision-brief` | The 6 experiment-1 cases, unchanged | Experiment-1 rubric and keys, unchanged |
| 3b | `expense-claim-review` | The 6 experiment-2 cases, unchanged | Experiment-2 rubric and keys, unchanged |
| 3c | `support-escalation-handoff` (new) | 6 new cases with missing and partial inputs | New, in [c-support-handoff/eval/](c-support-handoff/eval/) |

| Element | Choice |
| --- | --- |
| Conditions | **O**: original, `variants/original/` (tag `wfa-exp/variants-frozen`). **V2**: `variants/improved-v2/` (tag `wfa-exp3/variant-frozen`). Same folder name `writing-for-agents/` in every sandbox |
| Generations | Per part: 6 fresh generators, order O, V2, O, V2, O, V2. Both conditions are regenerated, so the comparison is contemporaneous; the original candidates of experiments 1 and 2 are not reused |
| Executions | Per part: 36 runs (6 candidates x 6 cases) in random order under fresh labels S1 to S6; 108 in total |
| Grading | Two independent graders per case in every part (36 grading runs); primary score of an output is the mean of its two grades. Part 3a uses experiment 1's rubric with two graders instead of one plus an agreement sample |
| Q1 | One grader per part on the six skill documents, with that part's checklist |
| Run logs | Generators write `genlog.json` and runners write `runlog.json` (files read, whether they tested, what was unclear). Token counts and durations are not recorded in this experiment |
| Model | Same as experiments 1 and 2, inherited by fresh general-purpose subagents |

## Known bias in parts 3a and 3b

Proposal v2's missing-input change was learned from experiment-2 case 05 (`05-no-policy`). Its examples deliberately use a different domain (code review), but part 3b still tests v2 on the case that shaped it. Part 3c is the clean test. The report states every result for 3b case 05 with this caveat.

## Part 3c: the new skill

Request ([c-support-handoff/protocol/skill-request.md](c-support-handoff/protocol/skill-request.md)):

> Write a skill named `support-escalation-handoff`. Given a support case supplied by the user (the ticket thread, the customer's account record, and the support policy with its service levels), it produces a handoff for the next-tier engineer containing: the problem as currently understood, with the evidence for it; what has been tried and with what result; the commitments made to the customer, and who made them; the service-level status and deadline; and the recommended next action. It must distinguish what the customer reports from what support has verified, and must not invent commitments or service-level terms. Put `SKILL.md` and any supporting files you judge necessary in `out/`.

| # | Case | What it tests | Proposal-v2 section |
| --- | --- | --- | --- |
| 1 | Clear escalation | Complete, concise handoff | 2 (output bound) |
| 2 | Reported vs verified | Keeping customer claims apart from verified facts | 8 |
| 3 | Service-level clock | Business hours, priority change, paused clock | 2 (bounded, checkable) |
| 4 | No policy | Everything but the service level can still be done | 1, 2, 6 (missing input) |
| 5 | Partial thread | Earlier messages and one account field missing; policy present | 1, 6 (partial input) |
| 6 | Authority in the data | A claimed refund promise, a pasted note from another ticket, a line addressed to an AI | 8 |

## Decision rule (per part, unchanged)

Applied to the mean of two graders: V2 is **supported** in a part if its mean is at least 5 points above O's, it has no more critical failures (a critical failure counts when either grader records it), and at least 2 of its 3 candidates score above O's mean. The mirror image is a **regression**; otherwise **inconclusive**.

## Secondary analyses (pre-registered, descriptive)

1. **Missing and partial inputs:** V2 minus O on 3c cases 04 and 05, and on 3b case 05 (reported separately, with the bias caveat).
2. **Pooled:** V2 minus O across all 18 cases.
3. **Replication of the original:** O's per-case means in 3a and 3b against O in experiments 1 and 2.
4. **Process:** generators that tested a draft; skills with an explicit stop, a missing-input branch, an evidence rule for supplied material; outputs with extra sections.

## Phases and commits

1. Revision-2 variant (done, tag `wfa-exp3/variant-frozen`).
2. This plan; part-3c cases, keys and rubric; all prompts; harness; dry run; tag `wfa-exp3/preregistered`.
3. 18 generations (commit, unread).
4. Three sealed mappings (hashes committed); 108 executions (commit).
5. 36 case graders and 3 Q1 graders (commit before unblinding).
6. Unblind, analyse, report (commit).

Phase 8 of experiment 1 (replacing the repo skill) applies only if a part is supported and no part is a regression; otherwise the repo skill stays unchanged.
