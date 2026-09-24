# Matt Pocock Skills

A collection of agent skills (slash commands and behaviors) loaded by Claude Code. Skills are organized into buckets and consumed by per-repo configuration emitted by `/setup-matt-pocock-skills`.

## Language

**Issue tracker**:
The tool that hosts a repo's issues: GitHub Issues, Linear, a local `.scratch/` markdown convention, or similar. Skills like `to-tickets`, `to-spec`, and `triage` read from and write to it.
_Avoid_: backlog manager, backlog backend, issue host

**Issue**:
A single tracked unit of work inside an **Issue tracker**: a bug, task, spec, or slice produced by `to-tickets`.
_Avoid_: ticket (use only when quoting external systems that call them tickets, or for a **Decision ticket**, see below)

**Decision ticket**:
A `wayfinder` unit: a child **Issue** of a `wayfinder:map` holding a *question* whose resolution is a decision, not a slice of a build to execute. The **decision** qualifier is what keeps it distinct from an implementation ticket; `wayfinder` introduces the term, then uses "ticket".

**Triage role**:
A canonical state-machine label applied to an **Issue** during triage (e.g. `needs-triage`, `ready-for-afk`). Each role maps to a real label string in the **Issue tracker** via `docs/agents/triage-labels.md`.

**Requirement ID**:
A stable identifier for one requirement in a spec, written `<KEY>-<n>:` at the start of a user story (`CPN-3:`) and repeated as a prefix on the tests that cover it. The trailing colon is part of the ID: it keeps `CPN-1` from matching `CPN-10`. A spec that carries them turns on `requirement-traceability`.
_Avoid_: acceptance criterion ID, story number, requirement number

**Judgement pass**:
The optional first tier of judging whether a tagged test asserts what its requirement says: one Jev call per **Requirement ID**, sorted into ok, flag, uncertain or not judged. It runs only when a key is set and the repo's `docs/agents/traceability.md` has a `Judgement: jev` line; `code-review`'s Spec sub-agent then reads the flagged and uncertain tests.
_Avoid_: LLM check, AI grading

## Relationships

- An **Issue tracker** holds many **Issues**
- An **Issue** carries one **Triage role** at a time
- A **Decision ticket** is an **Issue** (a child of a `wayfinder:map`)
- An **Issue** covers zero or more **Requirement IDs**
- The **Judgement pass** judges the tests tagged with each **Requirement ID**

## Flagged ambiguities

- "backlog" was previously used to mean both the *tool* hosting issues and the *body of work* inside it. Resolved: the tool is the **Issue tracker**; "backlog" is no longer used as a domain term.
- "backlog backend" / "backlog manager". Resolved: collapsed into **Issue tracker**.
