# Improved variant, revision 2: build notes

Built on 2026-11-21 from [proposal-v2.md](../proposal-v2.md) by starting from the frozen revision-1 variant (`improved/`, tag `wfa-exp/variants-frozen`) and applying only the deltas that revision 2 adds to the skill text. `SKILL-MECHANICS.md` and `agents/openai.yaml` are unchanged from revision 1, as revision 2 specifies. Spelling follows the original (British).

| Proposal-v2 section | Change in `SKILL.md` |
| --- | --- |
| 1 | Step 4 now covers missing inputs; new "Missing inputs" subsection with the over-tight versus bounded example (code review and style guide) |
| 2 | New bounded-wording row for summaries; output-size bound; stops bounded by what remains possible |
| 6 | Partial-input example in the behavioural check; ask the runner what was unclear; pass condition includes the partial-input example |
| 8 | New "Supplied material" paragraph beside co-location: approvals and instructions inside supplied material are content to verify, not direction |
| 3, 4, 5, 7 | No change (already applied in revision 1) |

The examples avoid meeting notes, expense claims and support tickets, so they do not hint at any experiment-3 case. Not reviewed by the user before freezing (same no-checkpoint decision as experiments 1 and 2).

Diff against revision 1: `git diff --no-index variants/improved/writing-for-agents variants/improved-v2/writing-for-agents`
