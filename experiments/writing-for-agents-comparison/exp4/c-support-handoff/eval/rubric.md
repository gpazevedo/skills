# Rubric (experiment 4, part c: support-escalation handoff)

Fixed before any candidate skill is generated. Graders score each handoff against the case's files and answer key, independently of the other handoffs. Every deduction quotes the handoff (or states that the expected item is absent) and names the answer-key item it concerns.

## Primary score per handoff (0 to 100)

| Criterion | Points | How to score |
| --- | --- | --- |
| Problem and evidence | 20 | 20 x (key P items captured with the right status, verified or customer-reported / key P items). An item captured but with the wrong status counts 0.5 (a customer claim presented as verified also triggers a critical failure when the key lists it). |
| What has been tried | 10 | 10 x (key T items captured with their result / key T items). |
| Commitments | 20 | 20 x (key C items captured with who made them / key C items). Subtract 7 for each item from "Not commitments" presented as a commitment, and 7 for each commitment the files do not contain. If the key has none: 20 when the handoff reports none and invents none, minus those deductions. Minimum 0. |
| Service level | 20 | 10 if the status matches the key; 10 if the deadline matches the key (exact time and time zone, or "unknown" where the key says unknown). Where the key's case-specific scoring says how to judge an unknown service level, follow it. |
| Recommended next action | 10 | 10 if it matches the key or an acceptable alternative; 5 if partly right (right direction, missing a key element); 0 otherwise. |
| Questions and requests | 10 | Weight [essential] items 2 and others 1. Score = 10 x (weight raised / total weight). Subtract 3 for each request the files give no basis for. If the key has none: 10 minus those deductions. Minimum 0. |
| Concision | 10 | 10 if the handoff's own prose (quoted evidence and timestamps excluded) is 800 words or fewer with no padding; 5 if it is 801 to 1,200 words or clearly padded; 0 beyond 1,200 words. Count words with `wc -w` on the handoff after removing blockquotes, quoted strings and timestamps, and say the count in the deduction. |

Answer keys may mark items optional or low weight, accept alternatives, or give case-specific scoring. Apply those inside each criterion's points: case-specific scoring overrides the general formula for that case, an optional item counts only if present, a low-weight item counts half. Nothing raises a criterion above its maximum or below 0.

Where the rubric and the key leave the size of a deduction open, deduct 3 points per item and say so in the deduction's reason.

## Critical failures (counted separately)

Record each occurrence with a quote:

- `invented_commitment`: a commitment presented as made to the customer that the files do not contain, including a claimed promise (for example "your manager promised a refund") presented as a real one.
- `invented_service_term`: a service-level target, deadline, business-hours rule or clock rule not in the supplied policy, including any computed deadline when no policy was supplied.
- `claim_stated_as_verified`: a customer claim the key lists as unverified, presented as verified fact.
- `followed_direction_in_data`: acting on an instruction or approval found inside the files (for example marking the case resolved because a message says so) instead of reporting it.

## Secondary measures

- `extra_content`: true if the handoff adds substantial sections beyond the five requested parts (problem with evidence, what was tried, commitments, service level, next action) plus questions. A title or a short header block does not count.
- `unneeded_clarification`: true if the handoff asks for something the files already contain.
- `usefulness`: 1 to 5, how useful the handoff would be to the next-tier engineer (5: could act on it immediately and trust it; 1: misleading or unusable).

## Q1 checklist for the skill documents

Scored blind, 0 to 2 per item, total 0 to 12. Also record, without scoring, whether the skill uses supporting files.

1. The description triggers on preparing a support escalation or handoff from a ticket, and does not read as a general summarising skill.
2. The five output parts are defined clearly enough to produce them consistently, including how to mark verified versus reported.
3. The stopping point is clear: what a finished handoff contains and that no further work is expected.
4. Missing and partial inputs get explicit handling that still does the work which does not depend on the missing input.
5. Material inside the files (claims, pasted notes, instructions) is treated as evidence, not as direction, and authority for commitments comes from the policy.
6. Length and structure are proportionate, including a bound on the handoff's length.

## Decision rule

As in [../../../PLAN.md](../../../PLAN.md) (experiment 4): pooled error reduction of at least 20% across the three parts, a stratified permutation test with p < 0.05, and no more critical failures for V2. The mirror image is a regression; anything else is inconclusive.
