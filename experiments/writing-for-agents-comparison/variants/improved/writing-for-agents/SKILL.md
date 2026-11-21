---
name: writing-for-agents
description: Write or review documents agents consume, including skills, AGENTS.md or CLAUDE.md, workflows, and the references they link. Use when creating or editing one, or improving its structure, scope, completion criteria, or context pointers.
---

Reference for writing any document an agent consumes: a skill, an `AGENTS.md` / `CLAUDE.md`, a doc reached by a pointer. The packaging differs; the writing does not: the same levers make each one predictable, since the agent takes the same _process_ every run rather than producing the same output.

When the document you're writing is a skill, read [`SKILL-MECHANICS.md`](SKILL-MECHANICS.md) for frontmatter, invocation choice, and router skills.

## Authoring process

Start here, then use the sections below as reference for each step. Apply the process at the scale of the edit: a narrow correction needs only the steps it touches. A reference-only document is still valid; for it, step 1 names the question the document answers, and no artificial procedure is added.

1. **Reader and purpose.** Identify the intended reader, the situation that triggers the document, the action or decision it drives, and the point where the reader stops.
2. **Authority.** Find where each requirement already lives (see the single source of truth under [Pruning](#pruning)). Separate required behaviour from examples and explanation.
3. **Common path.** Write the path every run takes, in reading order. Put each conditional instruction beside its trigger (see co-location under [Information hierarchy](#information-hierarchy)).
4. **Completion.** Make each completion criterion observable and bounded by the document's purpose (see [Steps and completion criteria](#steps-and-completion-criteria)).
5. **Check and prune.** Walk through the examples the edit affects (see [Behavioural check](#behavioural-check)), then prune ambiguity, duplication, and instructions with no observable effect.

The edit is sufficient when the walked-through examples reach the intended actions and stopping points, and the pruning pass finds nothing left to cut.

## Context pointers

A **context pointer** is a reference held in the agent's context that names some out-of-context material and encodes the condition for reaching it. A skill's description is one; a line in `AGENTS.md` naming a doc is the same object. The pointer's _wording_, not its target, decides when the agent reaches the material, and how reliably. A must-have target behind a weakly worded pointer is a variance bug: sharpen the wording first, and inline the material only if sharpening fails.

A pointer does two jobs: state what the material is, and list the **branches** that should trigger reaching it (a branch is a distinct case the document handles, so different runs take different paths through it). Every word of an always-loaded pointer costs on every turn, so it earns even harder pruning than the body:

- **Front-load the leading word**: the pointer is where it does its triggering work.
- **One trigger per branch.** Synonyms that rename a single branch are one branch written twice; collapse them and keep only genuinely distinct branches.
- **Cut identity the body already carries.**

## The two loads

Every document and pointer you add spends one of two budgets:

- **Context load** is the cost of always-loaded material on the agent's window: an `AGENTS.md` line, a skill description, anything sitting in context every turn, spending tokens and attention whether or not it fires.
- **Cognitive load** is the cost on the human: which documents exist and when to reach for each. The human is the index. Not a cost to minimise: it is the price of human agency; spend it where human judgement matters, remove it where it does not.

Material reached only through a pointer escapes context load at the price of the pointer's own line; material with no pointer at all rides entirely on cognitive load.

## Information hierarchy

A document is built from two content types: **steps** (the ordered actions the agent performs) and **reference** (definitions, rules, facts consulted on demand). The two mix freely: all steps (a recipe), all reference (a review's rules), or both. The core decision is where each piece sits on the **information hierarchy**, a ladder ranked by how immediately the agent needs the material:

1. **In-file step** is the primary tier: what the agent does, in order.
2. **In-file reference** is consulted on demand. Often a legitimately flat peer-set (every rule of a review on one rung), which is a fine arrangement, not a smell.
3. **Disclosed reference** is pushed out into a separate file, reached by a context pointer, loaded only when the pointer fires. Spans a sibling file in the same folder through fully external reference that lives anywhere and any document can point at.

Push too little down and the top bloats; push too much and you hide material the agent actually needs. That tension is the whole decision.

**Progressive disclosure** is the move down the ladder (out of the main file and behind a pointer) so the top stays legible. Not primarily a token optimisation: it is how the hierarchy is protected. Branching is the cleanest disclosure test: inline what every branch needs, and push behind a pointer what only some branches reach. When a document has steps, in-file reference that should be disclosed buries them and makes it less likely the agent attends to each one.

**Co-location** is the within-file companion: where the ladder decides _how far down_ a piece sits, co-location decides _what sits beside it_ once there. Keep a concept's definition, rules, and caveats under one heading rather than scattered, so reading one part brings its neighbours with it, and put each conditional instruction beside the trigger that activates it. The test: the document should read like documentation written for the agent. (Distinct from duplication: that repeats one meaning in two places; scattering fragments one meaning across many.)

**Sprawl** is the failure mode here: a document simply too long, even when every line is live and unique. Attention thins across the excess, and every extra line is one more to keep relevant. [Choosing a structural fix](#choosing-a-structural-fix) maps it, and the other structural problems, to a first adjustment.

## Steps and completion criteria

Every step ends on a **completion criterion**, the condition that tells the agent the work is done. Two properties make it a lever:

- **Clarity**: can the agent tell done from not-done? A vague bound ("understanding reached") invites **premature completion**: ending the step before it is genuinely done, attention slipping to _being done_. The visible steps still ahead (the **post-completion steps**) supply the pull; the criterion's clarity is the resistance. Defend in order: **sharpen the bound first** (local and cheap); only if it is irreducibly fuzzy _and_ you observe the rush, hide the later steps by splitting the sequence. Hiding only works across a real context boundary (a hand-off or a subagent dispatch; an inline call leaves the later steps in context and clears nothing).
- **Demand**: how much it requires. "Every modified model accounted for" forces thorough work where "produce a change list" does not. Demand drives **legwork** (the digging the agent does within the work, latent in the wording rather than written as its own step), and it is not step-bound: "every rule applied" binds a body of flat reference just as "every step done" binds a sequence, which is how an all-reference document still carries an exhaustiveness bar. Demand without a boundary drives expansion as readily as thoroughness, so bound it.

Make criteria checkable and exhaustive within the declared scope. Name the relevant set, the required result, and the stopping condition. Preserve required behaviour when clarifying the boundary. Work beyond the boundary is then an optional extension, not incomplete work.

| Open-ended wording | Bounded wording |
| --- | --- |
| Review every relevant document. | Review the documents linked from the supplied index; list broken or missing references. |
| Improve the instructions until they are clear. | Resolve the identified ambiguity and verify that the ordinary and exception examples lead to the intended actions. |
| Investigate thoroughly. | Identify the cause supported by the supplied evidence; mark unresolved explanations as uncertain. |

## When to split

Splitting one document into two spends one of the two loads, so split only in response to an observed comprehension or execution problem, not as routine formatting:

- **By sequence**: split a run of steps where you observe the post-completion steps pulling the agent to rush the one in front of it, and only across a real context boundary (see Clarity above). Keeping them out of view drives more legwork on the current task. Beware the reverse: merging sequences exposes each step's later steps to what follows, inviting premature completion.
- **By invocation**, skill-specific: see [`SKILL-MECHANICS.md`](SKILL-MECHANICS.md).

## Choosing a structural fix

Match the observed problem to one first adjustment, rather than applying every technique or creating new files:

| Writing problem | First adjustment |
| --- | --- |
| Important instruction is missed | Clarify its trigger and place it at the point of use. |
| Main path is buried, or the document sprawls | Move conditional detail behind a precise pointer. |
| One concept is fragmented | Put its definition, rule, and exception together. |
| Requirement appears in several places | Keep one authoritative statement and link to it. |
| Reader stops too early or keeps expanding the task | Clarify the completion criterion and scope. |
| Short wording becomes cryptic | Restore the detail needed to choose the correct action. |

## Leading words

A **leading word** is a compact, familiar concept the agent can think with while running the document (_lesson_, _fog of war_, _tracer bullets_). Used consistently as a term, it can carry a whole region of behaviour in a few tokens, because the reader already knows what it means. Coining your own works only if you define it clearly: a made-up word brings no prior meaning, so you pay in definition tokens what a familiar word gives free. Reach for an existing word first.

Prefer familiar, precise terms. Introduce a shorthand when it compresses a repeated concept without hiding its meaning. Check that a reader encountering the term for the first time can recover the intended action. The same word used in your prompts, your docs, and your codebase also makes a pointer easier to match.

Look for restatements a single term could replace: a triad spelled out at three sites, a pointer spending a sentence to gesture at one idea. Keep the shorter term only when it preserves the full intended meaning; a compact label that needs repeated explanation has not reduced the reader's work.

- "fast, deterministic, low-overhead" → _tight_ (a _tight_ loop).
- "a loop you believe in" → _red_, turning a fuzzy gate into a binary observable state (the loop goes _red_ on the bug, or it doesn't).

**Positive phrasing**: prefer direct descriptions of desired behaviour ("write one-line comments") over a list of what to avoid, since naming a behaviour can make it more salient. Keep explicit prohibitions where they state a necessary boundary, and pair each with the positive target. Evaluate wording by whether readers follow the requirement accurately.

## Pruning

- Keep each meaning in a **single source of truth**: one authoritative place, so changing the behaviour is a one-place edit. **Duplication** (the same meaning in more than one place) costs maintenance and tokens, and inflates a meaning's prominence on the ladder past its real rank. (The accidental inverse of a leading word, which repeats a term on purpose, never the meaning.)
- The **environment** is a source of truth too (`package.json` scripts, config files, the directory layout, `--help` output), and a document that restates it is a **cache**: a copy of a lookup, earning its load only when the lookup is expensive. Cache what the agent cannot find by looking: the unwritten convention, the reason behind a choice, the gotcha no config confesses. Leave the one-file, one-command lookups to the environment, where they cannot go stale.
- Check every line for **relevance**: does it still bear on what the document does? A line loses relevance by never bearing on the task (mere exposition, or a branch that should be disclosed) or by going stale as the behaviour or world it describes changes. Shorter documents are easier to keep relevant. Without a pruning discipline the default fate is **sediment**: stale layers that settle because adding feels safe and removing feels risky, until you must core down through them to find what is still live.
- Hunt **no-ops** sentence by sentence: an instruction the model already obeys by default pays load to say nothing. The test (does it change behaviour versus the default?) is model-relative, not reader-relative: two people disagreeing about a no-op disagree about the default, and settle it by running the document (see [Behavioural check](#behavioural-check)), not by debate. When an instruction has no observable effect, remove it or replace it with a specific action and completion criterion. Judge the replacement by the behaviour it changes: replace "be relentless about consistency" with "use the same term for this concept throughout the document and its linked examples". A stronger adjective raises effort without defining the action, scope, or stopping point.

## Behavioural check

Running the document settles what reading cannot. Keep the check proportionate to the edit:

- Choose an ordinary example and the exception the edit affects. Add an already-complete example when changing completion criteria, and a missing-input example when changing prerequisites. A spelling correction needs no check.
- State the expected action and stopping point for each.
- Compare the old and revised wording on equivalent inputs and the same available context.
- Record missed requirements, wrong branches, unnecessary actions, and unresolved ambiguity.

The check passes when the revised wording addresses the identified problem without losing required behaviour in the selected examples. An author's walkthrough exposes ambiguity; only an observed agent run supports a claim that execution improved, so say which one you did.
