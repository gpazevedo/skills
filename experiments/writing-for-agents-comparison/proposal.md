---
status: proposed
---

# Improving writing-for-agents

Make [writing-for-agents](../../../.agents/skills/writing-for-agents/SKILL.md) easier to apply by adding a short authoring process, bounding its demand for exhaustiveness, and making its writing heuristics testable. Preserve its strongest ideas: context pointers, progressive disclosure, co-location, and one authoritative home for each requirement.

This proposal concerns only the skill's instructions, description, and [SKILL-MECHANICS.md](../../../.agents/skills/writing-for-agents/SKILL-MECHANICS.md). It proposes changes without applying them. It does not attribute prior delivery delays to this skill; the recommendations follow from the current text and need evaluation.

## 1. Add a short entry process

The skill currently opens with concepts. Those concepts help an experienced author reason, but leave the author to assemble a method. Put a brief process before the reference sections:

1. Identify the intended reader, triggering situation, action or decision, and stopping condition.
2. Find the existing authority for requirements; distinguish required behavior from examples and explanation.
3. Write the common path in reading order. Put each conditional instruction beside its trigger.
4. Make completion criteria observable and bounded by the document's purpose.
5. Walk through relevant examples, then prune ambiguity, duplication, and unnecessary instructions.

Apply this at the scale of the edit. A narrow correction needs only the relevant steps. Reference-only documents remain valid: identify what question they answer rather than adding artificial procedures.

**Completion signal:** a new author can identify what to do first and when the edit is sufficient without reconstructing a process from the conceptual sections.

## 2. Bound exhaustiveness and legwork

The completion-criteria section ends with: “The strongest criteria are both checkable and exhaustive.” Its demand discussion also emphasizes forcing legwork. Neither explicitly bounds that effort.

Revise the conclusion to:

> Make criteria checkable and exhaustive within the declared scope. Name the relevant set, the required result, and the stopping condition. Preserve required behavior when clarifying the boundary.

Add examples that show a writing choice rather than introducing a new operational requirement:

| Open-ended wording | Bounded wording |
| --- | --- |
| Review every relevant document. | Review the documents linked from the supplied index; list broken or missing references. |
| Improve the instructions until they are clear. | Resolve the identified ambiguity and verify that the ordinary and exception examples lead to the intended actions. |
| Investigate thoroughly. | Identify the cause supported by the supplied evidence; mark unresolved explanations as uncertain. |

**Completion signal:** a reader can distinguish incomplete work from an optional extension without inventing a stopping rule.

## 3. Make the pruning advice favor precision over intensity

The pruning section suggests replacing a weak instruction such as “be thorough” with a stronger word such as “relentless.” Stronger emphasis still leaves the action, scope, and stopping condition undefined. It can increase effort without improving the result.

Replace that example with a concrete requirement:

> When an instruction has no observable effect, remove it or replace it with a specific action and completion criterion. Judge the replacement by the behavior it changes.

For example, replace “be relentless about consistency” with “use the same term for this concept throughout the document and its linked examples.”

**Completion signal:** revised instructions specify observable behavior instead of relying on stronger adjectives to communicate demand.

## 4. Present leading words and positive phrasing as heuristics

The leading-words and negation sections make broad causal claims about model behavior. Retain the practical advice while distinguishing a useful technique from a guarantee.

Suggested wording:

> Prefer familiar, precise terms. Introduce a shorthand when it compresses a repeated concept without hiding its meaning. Check that a reader encountering the term for the first time can recover the intended action.
>
> Prefer direct descriptions of desired behavior. Keep explicit prohibitions where they state a necessary boundary. Evaluate wording by whether readers follow the requirement accurately.

Retain a leading-word example only when the shorter term preserves the full intended meaning. A compact label that needs repeated explanation has not reduced the reader's work.

**Completion signal:** readers can explain the required action without knowing the author's private vocabulary, and necessary boundaries remain explicit.

## 5. Make structural advice easier to apply

The existing hierarchy, co-location, splitting, and pruning sections describe related choices across several headings. Add a compact decision aid, then remove overlapping explanations:

| Writing problem | First adjustment |
| --- | --- |
| Important instruction is missed | Clarify its trigger and place it at the point of use. |
| Main path is buried | Move conditional detail behind a precise pointer. |
| One concept is fragmented | Put its definition, rule, and exception together. |
| Requirement appears in several places | Keep one authoritative statement and link to it. |
| Reader stops too early or keeps expanding the task | Clarify the completion criterion and scope. |
| Short wording becomes cryptic | Restore the detail needed to choose the correct action. |

For splitting by sequence, retain the current condition that a real context boundary matters. Present splitting as a response to an observed comprehension or execution problem, rather than a routine formatting improvement.

**Completion signal:** an author can select one targeted structural correction without applying every technique or creating unnecessary files.

## 6. Give behavioral evaluation a small, explicit form

The skill already recommends running instructions to judge no-ops. Explain how to do that proportionately:

- Choose an ordinary example and the exception affected by the edit.
- State the expected action and stopping point for each.
- Compare the old and revised instructions using equivalent inputs and available context.
- Record missed requirements, wrong branches, unnecessary actions, and unresolved ambiguity.

Include an already-complete example when changing completion criteria. Include a missing-input example when changing prerequisites. A spelling correction needs no behavioral replay.

Distinguish an author's walkthrough from an observed agent run. A walkthrough can expose ambiguity; it does not establish measured improvement in agent behavior. Preserve required meaning when shortening prose.

**Completion signal:** the revised wording addresses the identified problem without losing required behavior in the selected examples. Claims of improved execution are supported by actual runs when made.

## 7. Align discovery and skill mechanics with the stated purpose

The description names skills, AGENTS.md, and CLAUDE.md. The body applies to any document consumed by agents. Align those scopes with a candidate description:

> Write or review instructions consumed by agents, including skills, repository guidance, workflows, and linked references. Use when improving their structure, scope, completion criteria, or context pointers.

Evaluate the candidate against both intended tasks and ordinary prose editing so it does not trigger unnecessarily.

In SKILL-MECHANICS.md, separate authoring advice from host-specific invocation claims. The statements about user-only invocation and cross-skill reachability need a verified platform scope. Distinguish automatic discovery, explicitly following a file reference, and invoking a skill. This proposal has not verified those platform claims.

**Completion signal:** the description reaches the intended document types, ordinary prose requests stay outside its scope, and mechanics claims identify their verified applicability or uncertainty.

## Proposed shape of the skill

Keep the short authoring process first, followed by the existing conceptual reference with the changes above integrated into the relevant sections. Keep skill-specific packaging and invocation guidance in SKILL-MECHANICS.md. Use examples beside the rule they explain; add another reference file only if a distinct conditional topic warrants one.

Implement the bounded-completion and precision changes first, then the entry process and evaluation guidance. Finally, consolidate structural advice and refine discovery and mechanics. Review the resulting skill against one narrow edit, one conditional instruction, and one open-ended completion criterion. The result should be easier to apply without adding a mandatory document-production workflow to every writing task.
