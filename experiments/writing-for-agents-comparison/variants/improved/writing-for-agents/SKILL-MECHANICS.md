# Skill mechanics

The skill-specific branch of [`writing-for-agents`](SKILL.md): what changes when the document is a skill (frontmatter, the invocation choice, and router skills). Everything else about writing it is the universal reference in `SKILL.md`. This file separates authoring advice, which holds on any host, from host behaviour, which is listed with its sources under [Platform behaviour](#platform-behaviour).

## Three ways material is reached

Keep these distinct when reasoning about a skill's reach:

- **Automatic discovery**: the agent sees a skill's description in its skill listing and chooses the skill itself. Only a skill whose description is in the listing can be discovered.
- **Invocation**: the host loads the skill through its skill mechanism, because the human named it or the agent chose it.
- **Following a file reference**: the agent reads a file because a document already in context links to it. This is ordinary file reading, not invocation, so it reaches any file the agent can read, including a file inside another skill's folder. Nothing triggers it except the linking document.

## Invocation

Two choices, trading the two loads:

- A **model-invoked** skill keeps a model-facing `description`, so the agent can discover and invoke it, and the human can still invoke it by name. The description is the skill's top-level context pointer and stays loaded: permanent context load in exchange for discoverability. Write it as a pointer carrying the trigger branches (the pointer-writing rules in `SKILL.md` apply in full). A model-invoked skill whose content is all reference can be the one home for reference several skills share: another skill's steps tell the agent to invoke it.
- A **user-invoked** skill is invoked only when the human names it. It saves context load but spends cognitive load: you are the index that must remember it exists. Its `description` becomes human-facing: a one-line summary, trigger lists stripped. The frontmatter that makes a skill user-invoked differs by host (see [Platform behaviour](#platform-behaviour)).

Pick model-invocation only when the agent must reach the skill on its own, or another skill's steps must invoke it. If it only ever fires by hand, make it user-invoked.

Shared reference that two user-invoked skills both need can live in neither, since the agent cannot invoke either one. Push it to a plain file outside the skill system that both skills link to: external reference, reached by following a file reference.

## Splitting by invocation

The invocation cut of splitting (the sequence cut lives in `SKILL.md`): split off a model-invoked skill when you have a distinct leading word that should trigger it on its own (a trigger word you actually use in your prompts), or another skill must invoke it. You pay context load for the new always-loaded description, so that independent reach has to be worth it.

## Router skills

When user-invoked skills multiply past what you can remember, that piled-up cognitive load is cured by a **router skill**: one user-invoked skill that names the others and when to reach for each, so the human has one skill to remember instead of many. It can only hint: the agent cannot invoke the user-invoked skills it names, so the router tells the human which one to invoke.

## Platform behaviour

Checked on 2026-11-21 against each host's documentation. Re-check a detail before relying on it, since hosts change.

| Host | Verified behaviour | Source |
| --- | --- | --- |
| Claude Code | By default a skill's description is in context and both the human and Claude can invoke it. `disable-model-invocation: true` makes it user-invoked: the description is not in context, Claude does not invoke it on its own, a Skill tool call to it is blocked, and it is not preloaded into subagents. `user-invocable: false` does the reverse: hidden from the `/` menu, still invocable by Claude. | [Claude Code skills](https://code.claude.com/docs/en/skills) |
| Codex | `policy.allow_implicit_invocation: false` in `agents/openai.yaml` stops Codex invoking the skill on its own; explicit `$skill` invocation still works. Skills start with name, description and path in an initial list capped at about 2% of the context window. | [Build skills](https://learn.chatgpt.com/docs/build-skills) |

Unverified, so treat as uncertain:

- Whether Codex leaves a skill with implicit invocation turned off in the initial list, which decides whether it costs context load there.
- Whether either host offers skill-to-skill invocation other than the agent invoking a model-invoked skill because a loaded document tells it to. Neither page documents one skill invoking another directly.
