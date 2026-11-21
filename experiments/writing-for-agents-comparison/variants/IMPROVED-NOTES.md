# Improved variant: build notes

Built from [proposal.md](../proposal.md) on 2026-11-21, starting from a byte-identical copy of `skills/productivity/writing-for-agents/` at upstream commit `abeeaf9`. `agents/openai.yaml` is unchanged in both variants. Spelling follows the original (British).

Checkpoint A (review of the variant diff) was skipped by decision 3 in [PLAN.md](../PLAN.md); review the diff with the final report:

```
git diff --no-index variants/original/writing-for-agents variants/improved/writing-for-agents
```

## Check against the proposal's completion signals

Each check is an author's reading of the text, not an observed agent run.

| # | Proposal section | Where applied | Completion signal | Result |
| --- | --- | --- | --- | --- |
| 1 | Short entry process | New "Authoring process" section first in `SKILL.md`, five steps linking to the reference sections, scaled to the edit, reference-only documents allowed, with a sufficiency line | A new author can identify what to do first and when the edit is sufficient | Met: step 1 is the first action; the closing line states when the edit is sufficient |
| 2 | Bound exhaustiveness | "Steps and completion criteria": closing line replaced with the proposal's wording, bounded-wording table added, Demand bullet ends "so bound it" | A reader can tell incomplete work from an optional extension | Met: "Work beyond the boundary is then an optional extension, not incomplete work" |
| 3 | Precision over intensity | "Pruning", no-ops bullet: "stronger word (_relentless_)" fix replaced with remove-or-replace-with-action, plus the consistency example | Revised instructions specify behaviour instead of stronger adjectives | Met: no instruction in either file now recommends a stronger adjective |
| 4 | Heuristics, not guarantees | "Leading words" rewritten: causal pretraining claims softened, the proposal's suggested wording added, "go find them" removed, examples kept with a meaning-preservation test. "Negation" paragraph replaced by "Positive phrasing", which keeps necessary prohibitions | A first-time reader can recover the action; necessary boundaries stay explicit | Met. Both examples (_tight_, _red_) kept because each is a common term that preserves the meaning |
| 5 | Structural decision aid | New "Choosing a structural fix" table (sprawl folded into the buried-path row). Sprawl's cure sentence now points to the table. "When to split" now requires an observed problem and repeats the context-boundary condition by reference | An author can pick one targeted correction | Met: the table maps each problem to one first adjustment and says not to create new files by default |
| 6 | Behavioural evaluation | New "Behavioural check" section; the no-op test links to it | The wording addresses the problem without losing required behaviour; execution claims need actual runs | Met: walkthrough versus observed run distinction stated |
| 7 | Discovery and mechanics | Description rewritten from the proposal's candidate, keeping `AGENTS.md or CLAUDE.md` as trigger words and "creating" as a branch. `SKILL-MECHANICS.md`: new "Three ways material is reached" section, host-neutral invocation advice, and a "Platform behaviour" table with sources and an unverified list | Description reaches the intended types; mechanics claims state verified scope or uncertainty | Partly met. Mechanics: met. Description: not tested against ordinary prose-editing requests (no triggering eval was run), so the "stays out of scope" half is unverified |

## Section 7 verification

Checked 2026-11-21:

- Verified for Claude Code (code.claude.com/docs/en/skills): the invocation table for default, `disable-model-invocation: true` and `user-invocable: false`; blocking of Skill tool calls to a `disable-model-invocation` skill; no subagent preloading.
- Verified for Codex (learn.chatgpt.com/docs/build-skills): `allow_implicit_invocation: false` stops implicit invocation and keeps explicit `$skill` invocation; the initial-list budget.
- Not found in either source: direct skill-to-skill invocation, and whether a Codex skill with implicit invocation off stays in the initial list. Both are marked unverified in `SKILL-MECHANICS.md`.

The original's claims "no other skill can [reach a user-invoked skill]" and "with no descriptions, neither can fire the other" hold for invocation on Claude Code. They do not cover following a file reference, which the improved variant now separates.

## Deviations from the proposal

- The description keeps the words "AGENTS.md or CLAUDE.md" and the creating branch, which the proposal's candidate dropped. The original's pointer rules favour trigger words the user actually types.
- "(a review's rules, this skill)" became "(a review's rules)", since the skill now opens with steps.
- Sprawl got no separate row in the decision table; it shares the buried-path row.
