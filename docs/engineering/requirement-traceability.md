## What it does

`requirement-traceability` ties each requirement in a [spec](https://www.aihero.dev/ai-coding-dictionary/spec) to a test, and checks the tie. Requirements get stable IDs like `CPN-3:`, tests carry the ID as a name prefix, and a coverage gap check reports every requirement that no test names. That turns "covers all requirements" from a judgement call into something you can run.

It is opt-in, and the switch is the spec itself. To get IDs, type `/requirement-traceability` once, after [to-spec](https://aihero.dev/skills-to-spec) and [to-tickets](https://aihero.dev/skills-to-tickets). It adds the IDs and a seam table to the spec and a `Covers:` line to each ticket, and checks structurally that every ID sits on exactly one ticket, fixing what it can itself and asking you only about a requirement no ticket builds. A spec that carries IDs then turns the rest on; a spec without them changes nothing downstream. `to-spec`, `to-tickets` and `code-review` are untouched by this convention. There is no config and no setup question.

An optional second step, the **Judgement pass**, goes a level further. It asks [Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev), a small fast model from TypeSafe, whether the tests tagged with each requirement check all of what it says, and sorts requirements into ok, flagged and uncertain. A flagged requirement is not fully covered, so the agent names the part no assertion checks, adds tests for it, and re-runs the pass. After three rounds with the requirement still flagged, it stops and asks you how to proceed. It never fails a build, and [code-review](https://aihero.dev/skills-code-review) still reviews the tests against the spec as it always did. It stays off unless the repo opts in.

## When to reach for it

Type `/requirement-traceability` once per feature, right after `/to-tickets` (or after `/to-spec` for a one-session build, which has no tickets). From then on [tdd](https://aihero.dev/skills-tdd) and [implement](https://aihero.dev/skills-implement) call it themselves, because the spec carries IDs.

| Your situation | Where to go |
| --- | --- |
| You want every requirement provably tested, and can check it | `requirement-traceability` |
| The spec has no IDs and you don't need that guarantee | Nothing: skip it, and nothing in the chain changes |
| You want the test seams agreed before code exists | [to-spec](https://aihero.dev/skills-to-spec); annotation then maps each seam to IDs |
| You want to know whether a requirement's tests really cover it | The Judgement pass, then [code-review](https://aihero.dev/skills-code-review)'s Spec axis |

## Prerequisites

None for the ID convention. The Judgement pass is optional and needs all three of these:

- `TYPESAFE_API_KEY` set in the environment of the shell that launches your agent. The key is only ever read from the environment.
- A line `Judgement: jev` in `docs/agents/traceability.md`. A key in your shell is not consent for every repo you work in, so the pass stays off until the repo says yes.
- Node, to run the bundled script. It needs no packages.

## The contract

The leading word is the **requirement ID**, and it always ends in a colon. Four pieces carry it from the spec to the tests:

| Piece | Where it lives | Shape |
| --- | --- | --- |
| Requirement ID | The spec's user stories, after the list number | `1. CPN-1: As a shopper, I want to apply a coupon, so that I pay less.` |
| Seam table | The spec's testing decisions | `Seam` and `Requirement IDs` columns; an ID that won't be tested gets a `waived: <reason>` row |
| Test tag | The test name | `CPN-3: rejects expired coupons` |
| `Covers:` line | Each ticket, added by annotation | `Covers: CPN-1, CPN-4` |

The colon is load-bearing. `CPN-1` is a prefix of `CPN-10`, so a match without the colon reports an untested `CPN-1` as covered the moment `CPN-10` gets a test. A false "covered" is the one failure this convention exists to prevent, so every grep and every runner filter anchors on the colon.

`Covers:` means the IDs an issue makes **fully testable**, not the ones it touches. A requirement built across two slices is named on the later slice only, which lets the earlier slice's check pass honestly.

The check needs no setup. By default it is a small Node script bundled with the skill (no packages) that reads the test files as text and reports three things:

| Report | Meaning | Effect |
| --- | --- | --- |
| Untested | A requirement no test names | Fails |
| Undefined ID | A test tagged with an ID the spec does not define | Warns: a typo or a stale test |
| No ID | A test with no ID | Warns: possible scope creep |

If your repo has its own check command, name it in `docs/agents/traceability.md` and `implement` runs that instead. Each line of that file is optional, so a repo can opt in to the Judgement pass without a check command.

## Common questions

**Does a passing check mean every requirement is tested properly?**

No. The check confirms that each requirement has at least one test that names it; it cannot tell whether those tests, together, assert everything the requirement says. A requirement can need several tests, each tagged with the same ID. That judgement is split in two: the optional Judgement pass reads every tagged test before review, and [code-review](https://aihero.dev/skills-code-review)'s Spec [subagent](https://www.aihero.dev/ai-coding-dictionary/subagent) reads the tests against the spec as it always does. No third review axis is added.

**Does my code leave my machine?**

Only when the repo has opted in, and then only spec lines and the tagged tests themselves go to TypeSafe's API: each excerpt stops where its test ends, so helpers and neighbouring tests are not sent, and a test longer than 200 lines is cut there and marked `(cut)`. Nothing is sent without both the key and the `Judgement: jev` line; otherwise the skill says "Judgement pass skipped" and moves on. TypeSafe's [docs](https://docs.typesafe.ai/) describe the service. It was in early access when this was written, so availability is not guaranteed, and the pass falls back to the behaviour above when it is down.

**Can the Judgement pass approve a bad test?**

It can, which is why it is a first tier and not a gate. Its known weak spots are literal reading and multi-hop reasoning. An assertion hidden inside a helper is the clear case, so a test with no assertion call in its own body is never judged and goes straight to a read. A dry run on twelve hand-built cases produced no confident wrong "ok", but that is a smoke test, not calibration. Scores drift by about 0.03 between runs, so a borderline test can switch between ok and uncertain, and English specs give the best accuracy.

**Does a commented-out or skipped test still count as coverage?**

No. The check deliberately ignores lines that are commented out and tests marked `it.skip`, `it.todo`, `xit` or `xtest` (also when the test name wraps onto the next line), and Python tests under `@pytest.mark.skip` or `@unittest.skip`. A requirement whose only test is switched off is reported untested, which is the point: a skipped test is not a passing one. The reverse case cannot happen in JS/TS, Python or Go: an ID counts only where a test name sits (the first argument of `it(`, `test(` or `t.Run(`, or a pytest docstring's first line), so an ID inside an assertion value is not coverage. In other languages any string that starts with an ID and a colon still counts, so keep IDs out of string literals that are not test names.

**Does it catch a decision from a grilling session that never made it into the spec?**

No. It starts at the spec, so a decision that never became a story has no ID and is invisible to the check. It closes the spec-to-test half of the gap reported in [issue #341](https://github.com/mattpocock/skills/issues/341) (resolved answers are not traceable through spec, issues and implementation). The answer-to-spec half is still open, and [issue #959](https://github.com/mattpocock/skills/issues/959) covers commitments lost when a spec is split into tickets. Until those close, re-reading the spec against your own answers is still your job.

**Will it change how my existing specs behave?**

No. A spec with no IDs is left alone: the chain runs exactly as it did, and IDs are only ever added when you run `/requirement-traceability` on a spec. It is meant for a spec and tickets you have just written, before any `/implement`; retrofitting IDs onto a spec whose code already exists is out of scope.

## It's working if

- Every user story in the spec starts with an ID and a colon, and no ID is ever reused (a withdrawn one is kept and marked `(dropped)`).
- The seam table has no requirement missing from every row unless it is marked `waived` with a reason.
- Test names begin with their ID, and a gap list names an intentionally untested ID before the code review runs.
- Adding a test for `CPN-10` does not make `CPN-1` look covered.
- Commenting a test out, or marking it `skip`, puts its requirement straight back on the untested list.
- After annotation, each ticket carries a `Covers:` line, every ID appears on exactly one of them, and you were asked nothing unless a requirement fit no ticket.
- On the last open ticket, `implement` checks every ID in the spec, not just the ticket's; on any earlier one it names the tickets still open.
- A spec with no IDs produces no gap list and no `Covers:` lines anywhere in the flow.
- With the Judgement pass on, a requirement whose tests check only part of it shows up as flagged before review, and the agent adds the missing tests instead of passing the flag on, for at most three rounds before it asks you what to do.

## Where it fits

`requirement-traceability` is a **cross-cutting reference** that sits underneath the main chain rather than in it, the way [codebase-design](https://aihero.dev/skills-codebase-design) sits underneath the design skills. You run it once after [to-spec](https://aihero.dev/skills-to-spec) and [to-tickets](https://aihero.dev/skills-to-tickets), neither of which knows about it: it adds the IDs, the seam table and the `Covers:` lines to what they wrote. After that, [tdd](https://aihero.dev/skills-tdd) tags the tests and [implement](https://aihero.dev/skills-implement) runs the gap check (and the Judgement pass, if the repo opted in) before [code-review](https://aihero.dev/skills-code-review), which reviews as it always did. Only `tdd` and `implement` carry a line about it. When you are unsure which skill fits your situation, [ask-matt](https://aihero.dev/skills-ask-matt) routes you.
