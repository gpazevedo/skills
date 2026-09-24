## What it does

`requirement-traceability` ties each requirement in a [spec](https://www.aihero.dev/ai-coding-dictionary/spec) to a test, and checks the tie. Requirements get stable IDs like `CPN-3:`, tests carry the ID as a name prefix, and a coverage gap check reports every requirement that no test names. That turns "covers all requirements" from a judgement call into something you can run.

It is opt-in, and the switch is the spec itself. A spec that carries requirement IDs turns the rest on; a spec without them changes nothing downstream, and the skill stops after one line if it is pointed at one. To get IDs, ask for them when you run [to-spec](https://aihero.dev/skills-to-spec), or say so once in your repo's `CLAUDE.md` or `AGENTS.md`. There is no config and no setup question.

An optional second step, the **Judgement pass**, goes a level further. It asks [Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev), a small fast model from TypeSafe, whether each tagged test asserts what its requirement says, and sorts the tests into ok, flagged and uncertain. It is a first tier, not a gate: it never fails anything, and [code-review](https://aihero.dev/skills-code-review) reads only the flagged and uncertain tests instead of all of them. It stays off unless the repo opts in.

## When to reach for it

Type `/requirement-traceability`, or the agent reaches for it automatically when a spec already carries IDs, or when you ask for a spec's requirements to be traceable to tests. The skills in the main chain call it themselves once the spec has IDs, so you will rarely type it.

| Your situation | Where to go |
| --- | --- |
| You want every requirement provably tested, and can check it | `requirement-traceability` |
| The spec has no IDs and you don't need that guarantee | Nothing: skip it, and nothing in the chain changes |
| You want the test seams agreed before code exists | [to-spec](https://aihero.dev/skills-to-spec), which the seam table extends |
| You want to know whether a tagged test really asserts the requirement | The Judgement pass, then [code-review](https://aihero.dev/skills-code-review), whose Spec axis reads what it flags |

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
| `Covers:` line | Each issue `to-tickets` produces | `Covers: CPN-1, CPN-4` |

The colon is load-bearing. `CPN-1` is a prefix of `CPN-10`, so a match without the colon reports an untested `CPN-1` as covered the moment `CPN-10` gets a test. A false "covered" is the one failure this convention exists to prevent, so every grep and every runner filter anchors on the colon.

`Covers:` means the IDs an issue makes **fully testable**, not the ones it touches. A requirement built across two slices is named on the later slice only, which lets the earlier slice's check pass honestly.

The check needs no tooling. By default it is a handful of colon-anchored greps that report three things:

| Report | Meaning | Effect |
| --- | --- | --- |
| Untested | A requirement no test names | Fails |
| Undefined ID | A test tagged with an ID the spec does not define | Warns: a typo or a stale test |
| No ID | A test with no ID | Warns: possible scope creep |

If your repo has its own check command, name it in `docs/agents/traceability.md` and the skills run that instead. Each line of that file is optional, so a repo can opt in to the Judgement pass without a check command.

## Common questions

**Does a passing check mean every requirement is tested properly?**

No. The check confirms that each requirement has a test that names it; it cannot tell whether that test asserts the right thing. That judgement is split in two: the optional Judgement pass reads every tagged test, and [code-review](https://aihero.dev/skills-code-review)'s Spec [subagent](https://www.aihero.dev/ai-coding-dictionary/subagent) reads the tests it flags or is unsure of, or every tagged test when the pass is off. No third review axis is added.

**Does my code leave my machine?**

Only when the repo has opted in, and then only spec lines and tagged test excerpts (at most 60 lines each) go to TypeSafe's API. Nothing is sent without both the key and the `Judgement: jev` line; otherwise the skill says "Judgement pass skipped" and moves on. TypeSafe's [docs](https://docs.typesafe.ai/) describe the service. It was in early access when this was written, so availability is not guaranteed, and the pass falls back to the behaviour above when it is down.

**Can the Judgement pass approve a bad test?**

It can, which is why it is a first tier and not a gate. Its known weak spots are literal reading and multi-hop reasoning. An assertion hidden inside a helper is the clear case, so a test with no assertion call in its own body is never judged and goes straight to a read. A dry run on twelve hand-built cases produced no confident wrong "ok", but that is a smoke test, not calibration. Scores drift by about 0.03 between runs, so a borderline test can switch between ok and uncertain, and English specs give the best accuracy.

**Does a commented-out or skipped test still count as coverage?**

No. The check reads test files as text, so it deliberately ignores lines that are commented out and tests marked `it.skip`, `it.todo`, `xit` or `xtest`. A requirement whose only test is switched off is reported untested, which is the point: a skipped test is not a passing one. The reverse case is the known blind spot, and it is narrow: a string that *starts* with an ID and a colon counts even if it is not a test name, so keep IDs out of string literals that are not test names.

**Does it catch a decision from a grilling session that never made it into the spec?**

No. It starts at the spec, so a decision that never became a story has no ID and is invisible to the check. It closes the spec-to-test half of the gap reported in [issue #341](https://github.com/mattpocock/skills/issues/341) (resolved answers are not traceable through spec, issues and implementation). The answer-to-spec half is still open, and [issue #959](https://github.com/mattpocock/skills/issues/959) covers commitments lost when a spec is split into tickets. Until those close, re-reading the spec against your own answers is still your job.

**Will it change how my existing specs behave?**

No. A spec with no IDs is left alone: the chain runs exactly as it did, and no skill adds IDs to a spec that does not use them. Retrofitting IDs onto existing specs is deliberately out of scope.

## It's working if

- Every user story in the spec starts with an ID and a colon, and no ID is ever reused (a withdrawn one is kept and marked `(dropped)`).
- The seam table has no requirement missing from every row unless it is marked `waived` with a reason.
- Test names begin with their ID, and a gap list names an intentionally untested ID before the code review runs.
- Adding a test for `CPN-10` does not make `CPN-1` look covered.
- Commenting a test out, or marking it `skip`, puts its requirement straight back on the untested list.
- Each issue carries a `Covers:` line, and every ID appears on exactly one of them.
- A spec with no IDs produces no gap list and no `Covers:` lines anywhere in the flow.
- With the Judgement pass on, a test that asserts nothing shows up as flagged or uncertain before review, and the review's Spec report covers only those tests.

## Where it fits

`requirement-traceability` is a **cross-cutting reference** that sits underneath the main chain rather than in it, the way [codebase-design](https://aihero.dev/skills-codebase-design) sits underneath the design skills. [to-spec](https://aihero.dev/skills-to-spec) writes the IDs and the seam table, [to-tickets](https://aihero.dev/skills-to-tickets) puts `Covers:` on each issue, [tdd](https://aihero.dev/skills-tdd) tags the tests, [implement](https://aihero.dev/skills-implement) runs the gap check (and the Judgement pass, if the repo opted in) before review, and [code-review](https://aihero.dev/skills-code-review) judges whether the tests assert what the requirements say, starting from what the pass flagged. When you are unsure which skill fits your situation, [ask-matt](https://aihero.dev/skills-ask-matt) routes you.
